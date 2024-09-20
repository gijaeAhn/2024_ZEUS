# ------- For testing the Pybind11-bound library --------



import sys 

sys.path.append('/home/sj/Desktop/2024_ZEUS/')


import math
from lib.zeus_kinematics import *


NEAR_ZER0 = 1e-5
DEGREE_TO_RADIAN = 0.0174533
PI = 3.14159265359

def nearZero(a,b) :
    if( abs(a - b) < NEAR_ZER0) :
        return 0.0
    else :
        return False



def testInversKinematics() :

    test_cases = [
    {
        "input": [angle * DEGREE_TO_RADIAN for angle in [0, 45, 90, 0, 45, 0]]
    },
    {
        "input": [angle * DEGREE_TO_RADIAN for angle in [0, 10, 20, 30, 45, 50]]
    },
    {
        "input": [angle * DEGREE_TO_RADIAN for angle in [1, 2, 4, 5, 40, 5]]
    }
    ]


    q = [0,0,0,0,0,0]



    for idx, test in enumerate(test_cases):

        qTest = [*test["input"]]    
        trTest = ARM6_kinematics_forward_armReal(qTest)
        # trTest = Transform().translateZ(0.4).translateX(0.3).rotateY(PI/2)
        calculated_result = ARM6_kinematics_inverse_arm(trTest, q)
        calculated_result = [0.0 if nearZero(component,NEAR_ZER0) else component for component in calculated_result]        
        print(qTest)
        print(calculated_result)




if __name__ == '__main__' :
    testInversKinematics()