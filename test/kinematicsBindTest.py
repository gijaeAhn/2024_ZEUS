# ------- This file is for testing the Pybind11-bound library --------


import math


NEAR_ZER0 = 1e-6

def nearZero(a,b) :
    if( abs(a - b) < NEAR_ZER0) :
        return True
    else :
        return False




def testInversKinematics() :
    from lib import zeus_kinematics
    from lib import transform


    test_cases = [
        {
            "input": zeus_kinematics.Transform().translate(1, 2, 3).rotateX(0.5),  
            "expected": [0, 0, 0, 0, 0, 0]
        },
        {
            "input": zeus_kinematics.Transform().translate(1, 2, 3).rotateX(0.5),
            "expected": [0, 0, 0, 0, 0, 0]
        },
        # Add more test cases as needed
    ]



    for idx, test in enumerate(test_cases):
        calculated_result = zeus_kinematics.ARM6_kinematics_inverse_arm(*test["input"])
        assert all(nearZero(a, b) for a, b in zip(calculated_result, test["expected"])), f"Inverse Kinematics TEST Failed for test case {idx + 1}"