#include "./zeusKinematics.h"

// IK for ZEUS series arm (yaw-pitch-pitch-yaw-pitch-yaw)
// Modified by gj
// Additional restriction
// 1. Arm is bent
// 2. If target x < 0 , Arm should reach out to the target position by rotatting 1st yaw


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
    .rotateY(-q[2])                 // Using original axis
    .rotateZ(q[3])
    .translateZ(upperArmLength)
    .rotateY(-q[4])
    .translateY(-wristOffsetY)
    .translateZ(wristLength)
    .rotateZ(q[5]);
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
    qArm6_fail[0] = FAIL_VALUE;
    qArm6_fail[1] = FAIL_VALUE;
    qArm6_fail[2] = FAIL_VALUE;
    qArm6_fail[3] = FAIL_VALUE;
    qArm6_fail[4] = FAIL_VALUE;
    qArm6_fail[5] = FAIL_VALUE;
    return qArm6_fail; 
  }
  Transform trArmOrig = trArm;
  trArm=trArm.translate(-toolOffsetX-wristLength,0,-toolOffsetZ);
  Transform t1;
  Transform tTemp1;
  

  // World Frame is different.
  // Should be modified
  
  t1=t1.translateZ(-shoulderOffsetZ)*trArm;
  double xTemp1[3]; t1.apply0(xTemp1); //shoulder center to the wrist pitch/yaw center position
  double targetXY=sqrt(xTemp1[0]*xTemp1[0]+xTemp1[1]*xTemp1[1]);
  double armXY=sqrt(targetXY*targetXY-wristOffsetY*wristOffsetY);
  double armXYZ=sqrt(xTemp1[2]*xTemp1[2] + armXY*armXY);                     // armXY and armXZ are the very straight position form the arm shoulder
  double c_shoulderYawOffset=(armXY*armXY + targetXY*targetXY - wristOffsetY*wristOffsetY)/ (2.0*armXY*targetXY);
  double shoulderYaw = atan2(xTemp1[0],xTemp1[1])-acos(c_shoulderYawOffset);


  double shoulderPitch0=atan2(xTemp1[2],armXY);
  double c_elbow=(lowerArmLength*lowerArmLength + upperArmLength*upperArmLength - armXYZ*armXYZ )/(2.0*lowerArmLength*upperArmLength);
  double elbowPitch =PI-acos(c_elbow);




  double c_shoulderPitch=(lowerArmLength*lowerArmLength+armXYZ*armXYZ-upperArmLength*upperArmLength)/(2.0*armXYZ*lowerArmLength);
  double shoulderPitch= PI/2.0 - (shoulderPitch0 + acos(c_shoulderPitch));






  tTemp1 = tTemp1.translateZ(-shoulderOffsetZ).
                rotateZ(-shoulderYaw).
                rotateY(-shoulderPitch).
                translateZ(-lowerArmLength).
                rotateY(-elbowPitch);                     //tTemp1 is a frame for deleting join1,2,3 rotation


  Transform tTemp2 = tTemp1 * trArmOrig;
  double xTemp3[3]; tTemp2.apply(xTemp3);             
  Transform tTemp3 = tTemp2;

  tTemp2 = tTemp2.translate(-toolOffsetX-wristLength,0,-toolOffsetZ);
  double xTemp2[3]; tTemp2.apply0(xTemp2);           
  double wristYaw = atan2(xTemp2[0],xTemp2[1]);

  tTemp3 = tTemp3.rotateZ(-wristYaw);
  double wristYaw2 = acos(tTemp3.getVal(1,1));
  double wristPitch = acos((xTemp3[2]- upperArmLength) / wristLength);
  


  std::vector<double> qArm(6);
  qArm[0] = shoulderYaw;    
  qArm[1] = shoulderPitch;  
  qArm[2] = -elbowPitch;    
  qArm[3] = wristYaw;       //Done
  qArm[4] = -wristPitch;    //Done
  qArm[5] = wristYaw2;      //Done

  return qArm;
}