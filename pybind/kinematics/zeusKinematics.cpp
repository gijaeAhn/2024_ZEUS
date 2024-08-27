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




// Modification Needed
// Can't deal with x<0 area

std::vector<double>
ARM6_kinematics_inverse_arm(Transform trArm){
  //SJ: quick and dirty IK (only works with vertically down orientation)


  //Boundary Check
  double boundaryCheck = sqrt(std::pow(trArm.getVal(0,3),2) 
                            + std::pow(trArm.getVal(1,3),2) 
                            + std::pow(trArm.getVal(2,3),2));
  if(boundaryCheck > 0.925 ){
    std::vector<double> qArm6_fail(6);
    qArm6_fail[0] = 0.0;
    qArm6_fail[1] = 0.0;
    qArm6_fail[2] = 0.0;
    qArm6_fail[3] = 0.0;
    qArm6_fail[4] = 0.0;
    qArm6_fail[5] = 0.0;
    return qArm6_fail; 
  }

  trArm=trArm.translate(-toolOffsetX-wristLength,0,-toolOffsetZ).rotateY(PI/2);
  Transform t1;
  t1=t1.translateZ(-shoulderOffsetZ)*trArm;
  double xEE[3]; t1.apply0(xEE); //shoulder center to the wrist pitch/yaw center position
  double targetXY=sqrt(xEE[0]*xEE[0]+xEE[1]*xEE[1]);
  double armXY=sqrt(targetXY*targetXY-wristOffsetY*wristOffsetY);
  double armXZ=sqrt(xEE[2]*xEE[2] + armXY*armXY);
  double c_shoulderYawOffset=(armXY*armXY + targetXY*targetXY - wristOffsetY*wristOffsetY)/ (2.0*armXY*targetXY);
  double shoulderYaw = atan2(xEE[1],xEE[0])-acos(c_shoulderYawOffset);
  double shoulderPitch0=atan2(xEE[2],armXY);
  double c_elbow=(lowerArmLength*lowerArmLength + upperArmLength*upperArmLength - armXZ*armXZ )/(2.0*lowerArmLength*upperArmLength);
  double elbowPitch =PI-acos(c_elbow);
  double c_shoulderPitch=(lowerArmLength*lowerArmLength+armXZ*armXZ-upperArmLength*upperArmLength)/(2.0*armXZ*lowerArmLength);
  double shoulderPitch= PI/2.0 - (shoulderPitch0 + acos(c_shoulderPitch));


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