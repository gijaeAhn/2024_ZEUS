# ------- For testing the Pybind11-bound library --------


import math
from lib.zeus_kinematics import transform
from lib.zeus_kinematics import ARM6_kinematics_inverse_arm


NEAR_ZER0 = 1e-5

def nearZero(a,b) :
    if( math.abs(a - b) < NEAR_ZER0) :
        return True
    else :
        return False




def testInversKinematics() :

    test_cases = [
        {
            "input": transform.Transform().translate(1, 2, 3).rotateX(0.5),  
            "expected": [0, 0, 0, 0, 0, 0]
        },
        {
            "input": transform.Transform().translate(1, 2, 3).rotateX(0.5),
            "expected": [0, 0, 0, 0, 0, 0]
        },
        # Add more test cases as needed
    ]



    for idx, test in enumerate(test_cases):
        calculated_result = ARM6_kinematics_inverse_arm(*test["input"])
        assert all(nearZero(a, b) for a, b in zip(calculated_result, test["expected"])), f"Inverse Kinematics TEST Failed for test case {idx + 1}"