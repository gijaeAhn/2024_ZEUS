#include "./zeusKinematics.h"

//IK for ZEUS series arm (yaw-pitch-pitch-yaw-pitch-yaw)

bool show_debug=false;

double mod_angle(double q){
  if (q>PI) return q-2*PI;
  if (q<-PI) return q+2*PI;
  return q;
}

Transform ARM6_kinematics_forward_arm(const double *q){
  Transform t;
  t = t
    .translateZ(shoulderOffsetZ)
    .rotateZ(q[0])
    .rotateY(q[1])
    .translateZ(lowerArmLength)
    .rotateY(q[2])
    .translateZ(upperArmLength)
    .rotateX(q[3])
    .rotateY(q[4])
    .translateY(wristOffsetY)
    .translateZ(wristLength)
    .rotateX(q[5])  //now X is Z is ee forward, X is down
    .rotateY(-PI/2) //now X is forward, Z is up
    .translate(toolOffsetX,0,toolOffsetZ);
  return t;
}



std::vector<double>
ARM6_kinematics_inverse_arm(Transform trArm, const double *qOrg,bool wristRoll1){
  //SJ: quick and dirty IK (only works with vertically down orientation)

  trArm=trArm.translate(-toolOffsetX-wristLength,0,-toolOffsetZ).rotateY(PI/2);
  Transform t1;
  t1=t1.translateZ(-shoulderOffsetZ)*trArm;
  double xEE[3]; t1.apply0(xEE); //shoulder center to the wrist pitch/yaw center position
  double targetXY=sqrt(xEE[0]*xEE[0]+xEE[1]*xEE[1]);
  double armXY=sqrt(targetXY*targetXY-wristOffsetY*wristOffsetY);
  double armXZ=sqrt(xEE[2]*xEE[2] + armXY*armXY);

  // printf("XEE:%f %f %f\n",xEE[0],xEE[1],xEE[2]);
  // printf("TargetXY:%f ArmXY:%f ArmXZ:%f\n",targetXY, armXY,armXZ);

  double c_shoulderYawOffset=(armXY*armXY + targetXY*targetXY - wristOffsetY*wristOffsetY)/ (2.0*armXY*targetXY);
  double shoulderYaw = atan2(xEE[1],xEE[0])-acos(c_shoulderYawOffset);


  // printf("ShoulderYaw: %f %f\n", atan2(xEE[1],xEE[0])*180.0/PI, shoulderYaw*180.0/PI) ;

  double shoulderPitch0=atan2(xEE[2],armXY);


  double c_elbow=(lowerArmLength*lowerArmLength + upperArmLength*upperArmLength - armXZ*armXZ )/(2.0*lowerArmLength*upperArmLength);
  double elbowPitch =PI-acos(c_elbow);


  double c_shoulderPitch=(lowerArmLength*lowerArmLength+armXZ*armXZ-upperArmLength*upperArmLength)/(2.0*armXZ*lowerArmLength);
  double shoulderPitch= PI/2.0 - (shoulderPitch0 + acos(c_shoulderPitch));

  // printf("ShoulderPitch:%f %f\n", shoulderPitch0 *180.0/PI, shoulderPitch *180.0/PI);
  // printf("ElbowPitch:%f\n", elbowPitch *180.0/PI);

  double wristYaw=0.0;
  double wristPitch= PI-shoulderPitch-elbowPitch;
  double wristYaw2=0.0;


  std::vector<double> qArm(6);
  qArm[0] = shoulderYaw;
  qArm[1] = shoulderPitch;
  qArm[2] = elbowPitch;
  qArm[3] = wristYaw;
  qArm[4] = wristPitch;
  qArm[5] = wristYaw2;

  return qArm;
}