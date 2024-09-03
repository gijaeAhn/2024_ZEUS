#include "./zeusKinematics.h"

// IK for ZEUS series arm (yaw-pitch-pitch-yaw-pitch-yaw)
// Modified by gj
// Additional restriction
// 1. Arm is bent
// 2. If target x < 0 , Arm should reach out to the target position by rotatting 1st yaw
// 3. Yaw - Pitch - Pitch - Yaw - Pitch - Yaw
// 4. Final Z axis > 0 

bool show_debug=false;

double mod_angle(double q){
  if (q>PI) return q-2*PI;
  if (q<-PI) return q+2*PI;
  return q;
}

Transform ARM6_kinematics_forward_arm(std::vector<double> q){
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


std::vector<double>
ARM6_kinematics_inverse_arm(Transform trArm){


  //Boundary Check
  double boundaryCheck = sqrt(std::pow(trArm.getVal(0,3),2) 
                            + std::pow(trArm.getVal(1,3),2) 
                            + std::pow(trArm.getVal(2,3),2));
  if(boundaryCheck > 1.08 ){
    std::vector<double> qArm6_fail(6);
    qArm6_fail[0] = FAIL_VALUE;
    qArm6_fail[1] = FAIL_VALUE;
    qArm6_fail[2] = FAIL_VALUE;
    qArm6_fail[3] = FAIL_VALUE;
    qArm6_fail[4] = FAIL_VALUE;
    qArm6_fail[5] = FAIL_VALUE;
    return qArm6_fail; 
  }

  Transform trArmOrig = trArm;  // Copy Original Transform

  // We should get Joint 6 first
  // Transform finalTransform = trArm.translate(-toolOffsetX,0,-toolOffsetZ).rotateY(PI/2);

  Transform finalTransform = trArm.translate(-toolOffsetX,0,-toolOffsetZ);
  

  double alphaTemp = finalTransform.getVal(0,1)/finalTransform.getVal(0,0);
  double wristYaw = atan( (-alphaTemp+ std::pow(alphaTemp*alphaTemp + 4, 0.5 )) * 0.5 );

  Transform trPoint5 = finalTransform.translateZ(-wristLength).rotateZ(-wristYaw);
  double xPoint5[3]; trPoint5.apply0(xPoint5);
  Transform trPoint4 = trPoint5.translateY(-wristOffsetY);                              // Before the rotate deletion

  double xPoint4[3]; trPoint4.apply0(xPoint4);

  double shoulderYaw = atan2(xPoint4[1],xPoint4[0]);

  double xy_noOffset  = std::pow((xPoint4[0]*xPoint4[0] + xPoint4[1]*xPoint4[1] ),0.5);
  double xyz_noOffset = std::pow((xPoint4[0]*xPoint4[0] + xPoint4[1]*xPoint4[1] + xPoint4[2]*xPoint4[2]),0.5);

  double elbowPitch   = PI - std::acos( (lowerArmLength*lowerArmLength + upperArmLength*upperArmLength - xyz_noOffset*xyz_noOffset)
                                       /(2*upperArmLength*lowerArmLength) );

  double point4Angle = std::atan2(xPoint4[2],xy_noOffset);
  double tempAngle   = std::acos((lowerArmLength*lowerArmLength + xyz_noOffset* xyz_noOffset - upperArmLength*upperArmLength)
                                / (2*lowerArmLength*xyz_noOffset));
  double shoulderPitch = PI * 0.5 - (point4Angle + tempAngle);


  double tempDistance = xPoint5[2] - xPoint4[2];

  double elbowYaw = std::asin(tempDistance/(wristOffsetY * std::sin(PI - shoulderPitch - elbowPitch)));


  Transform trCopyForP5 = trArmOrig;
  // trCopyForP5 = trCopyForP5.translate(-toolOffsetX,0,-toolOffsetZ).rotateY(PI/2);
  trCopyForP5 = trCopyForP5.translate(-toolOffsetX,0,-toolOffsetZ);

  Transform tempTr;
  tempTr = tempTr.rotateZ(-elbowYaw)
                 .rotateY(-elbowPitch)
                 .translateZ(-lowerArmLength)
                 .rotateY(-shoulderPitch)
                 .rotateZ(-shoulderYaw)
                 .translateZ(-shoulderOffsetZ);


  Transform forCalcJ5 = tempTr * trCopyForP5;
  double xCalcJ5[3]; forCalcJ5.apply0(xCalcJ5);
  double wristPitch = std::atan2(-xCalcJ5[0],xCalcJ5[2]-upperArmLength);

  std::vector<double> result(6);

  result[0] = shoulderYaw;
  result[1] = shoulderPitch;
  result[2] = -elbowPitch;
  result[3] = elbowYaw;
  result[4] = wristPitch;
  result[5] = wristYaw;

  return result;


    






}