#include "./zeusKinematics.h"

// IK for ZEUS series arm (yaw-pitch-pitch-yaw-pitch-yaw)
// Modified by gj
// Additional restriction
// 1. Arm is bent
// 2. If target x < 0 , Arm should reach out to the target position by rotatting 1st yaw
// 3. Yaw - Pitch - Pitch - Yaw - Pitch - Yaw
// 4. Final Z axis > 0 

bool show_debug= false;

double mod_angle(double q){
  if (q>PI) return q-2*PI;
  if (q<-PI) return q+2*PI;
  return q;
}


template <typename T>
T clamp(T value, T min, T max) {
    if (value < min) return min;
    if (value > max) return max;
    return value;
}

double continuous_angle(double new_angle, double prev_angle){
    new_angle = mod_angle(new_angle);
    double delta = new_angle - prev_angle;
    if(delta > 6.0){
        new_angle = 2 * PI - new_angle;
    } else if(delta < -6.0){
        new_angle = 2 * PI + new_angle;
    }
    return new_angle;
}


// J2, J4, J6 inverted for simple calc
Transform ARM6_kinematics_forward_arm(std::vector<double> q){
      Transform t;
      t = t
      .translateZ(shoulderOffsetZ)
      .rotateZ(q[0])
      .rotateY(q[1])
      .translateZ(lowerArmLength)
      .rotateY(q[2])
      .rotateZ(q[3])
      .translateZ(upperArmLength)
      .rotateY(q[4])
      .translateY(-wristOffsetY)
      .rotateZ(q[5])
      .translate(toolOffsetX,0,toolOffsetZ+wristLength);
    return t;
}

Transform ARM6_kinematics_forward_armReal(std::vector<double> q){
      Transform t;
      t = t
      .rotateZ(PI/2)
      .translateZ(shoulderOffsetZ)
      .rotateZ(q[0])
      .rotateY(q[1])
      .translateZ(lowerArmLength)
      .rotateY(q[2])
      .rotateZ(q[3])
      .translateZ(upperArmLength)
      .rotateY(q[4])
      .translateY(-wristOffsetY)
      .rotateZ(q[5])
      .translate(toolOffsetX,0,toolOffsetZ+wristLength);
    return t;
}




std::vector<double>
ARM6_kinematics_inverse_iterative_arm(Transform trArm,const double *qOrg){

  trArm=trArm.translate(-toolOffsetX,0,-toolOffsetZ-wristLength);
  Transform t1;
  t1=t1.translateZ(-shoulderOffsetZ)*trArm;
  double xEE[3]; t1.apply0(xEE); //shoulder center to the wrist pitch/yaw center position
  double shoulderYaw = atan2(xEE[1],xEE[0]);
  double armXY=sqrt(xEE[0]*xEE[0]+xEE[1]*xEE[1]);
  double armXZ=sqrt(xEE[2]*xEE[2] + armXY*armXY);
  double shoulderPitch0=atan2(xEE[2],armXY);
  double c_elbow=(lowerArmLength*lowerArmLength + upperArmLength*upperArmLength - armXZ*armXZ )/(2.0*lowerArmLength*upperArmLength);
  // Should be Clamped because of no-offset
  c_elbow = clamp(c_elbow, -1.0, 1.0);
  double elbowPitch =PI-acos(c_elbow);
  double c_shoulderPitch=(lowerArmLength*lowerArmLength+armXZ*armXZ-upperArmLength*upperArmLength)/(2.0*armXZ*lowerArmLength);
  // Should be Clamped because of no-offset
  c_shoulderPitch = clamp(c_shoulderPitch,-1.0,1.0);
  double shoulderPitch= PI/2.0 - (shoulderPitch0 + acos(c_shoulderPitch));
  //now we know SY, SP, EP
  Transform t5;
  t5=t5 //this transform is the wrist transform
    .translateZ(-upperArmLength)
    .rotateY(-elbowPitch)
    .translateZ(-lowerArmLength)
    .rotateY(-shoulderPitch)
    .translateZ(-shoulderOffsetZ)
    .rotateZ(-shoulderYaw)
    *trArm;
  //t3 is the wrist rotation (Z-Y-Z)
   double wristPitch_1=acos(t5(2,2));
   double wrist_pitch_th=0.001745331; //0.1 degree
   double wristYaw1, wristYaw2, wristPitch;
   if(fabs(wristPitch_1)<wrist_pitch_th){
      printf("wrist pitch singular!!!  \n");
      wristPitch= qOrg[5];
      wristYaw1 = qOrg[4];
      wristYaw2 = qOrg[6];
    }else{
      wristPitch=wristPitch_1;
      double s_wp=sin(wristPitch);
      wristYaw1 = atan2(t5(1,2)/s_wp,t5(0,2)/s_wp);
      wristYaw2 = atan2(t5(2,1)/s_wp,-t5(2,0)/s_wp);
    }

    std::vector<double> qArm(6);
    qArm[0] = shoulderYaw;
    qArm[1] = shoulderPitch;
    qArm[2] = elbowPitch;
    qArm[3] = continuous_angle(wristYaw1,qOrg[3]);
    qArm[4] = continuous_angle(wristPitch,qOrg[4]);
    qArm[5] = continuous_angle(wristYaw2,qOrg[5]);

    return qArm;

}


std::vector<double>
ARM6_kinematics_inverse_arm(Transform trArm, const std::vector<double> qOrg) {
    const size_t MAX_ITER       =  100;
    const double errorGain      = -0.5;
    const double errorThreshold = 1.0E-6;


    Transform frameSetTR = Transform().rotateZ(-PI/2);
    Transform targetTR =  frameSetTR * trArm;
    Transform targetTRorig = targetTR;

    
    std::vector<double> solution = qOrg;
    double errorNorm;
    for(size_t iter = 1; iter <= MAX_ITER; iter++) {
        solution = ARM6_kinematics_inverse_iterative_arm(targetTR, solution.data());


        Transform trForCheck = ARM6_kinematics_forward_arm(solution);
        
        std::vector<double> error = {
            trForCheck(0,3)  -  targetTRorig(0,3),
            trForCheck(1,3)  -  targetTRorig(1,3),
            trForCheck(2,3)  -  targetTRorig(2,3)
        };

        errorNorm = std::sqrt(error[0]*error[0] + error[1]*error[1] + error[2]*error[2]);

        if (errorNorm < errorThreshold) {
            // Converged
            if (show_debug) {
                printf("Converged in %zu iterations. Error norm: %f\n", iter, errorNorm);
            }
            break;
        }

        // Adjust target transformation to aid convergence
        targetTR.setVal(0, 3, targetTR(0, 3) + (errorGain * error[0]));
        targetTR.setVal(1, 3, targetTR(1, 3) + (errorGain * error[1]));
        targetTR.setVal(2, 3, targetTR(2, 3) + (errorGain * error[2]));

        if (iter == MAX_ITER && errorNorm > errorThreshold) {
            printf("Failure: IK did not converge within %zu iterations. Final error norm: %f\n", MAX_ITER, errorNorm);
            return qOrg;
        }
    }

    for(size_t i = 0; i < 6 ; i++){
      solution[i] = mod_angle(solution[i]);
      solution[i] = continuous_angle(solution[i], qOrg[i]);
    }
    return solution; 
  }    
    
