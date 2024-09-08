#pragma once

#include "./Transform.h"
#include <stdio.h>
#include <math.h>
#include <vector>

const double PI = 2*asin(1);
const double SQRT2 = sqrt(2);
const double RAD_TO_DEG = 180.0/PI;

const double FAIL_VALUE = 15.0;



///////////////////////////////////////////////////////
//ZEUS ZRA-0515P VALUES
///////////////////////////////////////////////////////


const double shoulderOffsetZ = 0.145; //ground to shoulder pitch height
const double lowerArmLength=0.49;
const double upperArmLength=0.37;
const double wristOffsetY= 0.10; //shoulder yaw joint to wrist yaw joint
const double wristLength = 0.065; //wrist joint to end effector mount

const double toolOffsetX = 0.0;
const double toolOffsetZ = 0.0;

double mod_angle(double q);
Transform ARM6_kinematics_forward_arm(std::vector<double> q);
std::vector<double> ARM6_kinematics_inverse_iterative_arm(Transform trArm, const double *qOrg,bool wristRoll);
std::vector<double> ARM6_kinematics_inverse_arm(Transform trArm, const std::vector<double> qOrg ,bool wristRoll);
