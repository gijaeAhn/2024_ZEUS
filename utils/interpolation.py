import sys
import os

home_dir = os.path.expanduser('~')
sys.path.append(os.path.join(home_dir, 'Desktop/2024_ZEUS/'))

from lib.zeus_kinematics import *
from config.config import realConfig

import numpy as np
from scipy.spatial.transform import Rotation as R
from scipy.spatial.transform import Slerp


def print_transform(transform, label=None):
    if label:
        print(f"Transform {label}:")
    else:
        print("Transform:")
    matrix = [[transform.getVal(i, j) for j in range(4)] for i in range(4)]
    for row in matrix:
        print(' '.join(f"{val: .4f}" for val in row))
    print()  


#def interpolate_transforms(trans1, trans2, steps):
def interpolate_transforms(trans1, trans2, overlap):

    def transform_from_quatp(quatp):
        q = quatp[:4]  
        p = quatp[4:]  
        w, x, y, z = q
        tx, ty, tz = p

        t = Transform()

        t.setVal(0, 0, 1 - 2*(y**2) - 2*(z**2))
        t.setVal(0, 1, 2*x*y - 2*z*w)
        t.setVal(0, 2, 2*x*z + 2*y*w)
        t.setVal(0, 3, tx)

        t.setVal(1, 0, 2*x*y + 2*z*w)
        t.setVal(1, 1, 1 - 2*(x**2) - 2*(z**2))
        t.setVal(1, 2, 2*y*z - 2*x*w)
        t.setVal(1, 3, ty)

        t.setVal(2, 0, 2*x*z - 2*y*w)
        t.setVal(2, 1, 2*y*z + 2*x*w)
        t.setVal(2, 2, 1 - 2*(x**2) - 2*(y**2))
        t.setVal(2, 3, tz)

        t.setVal(3, 0, 0)
        t.setVal(3, 1, 0)
        t.setVal(3, 2, 0)
        t.setVal(3, 3, 1)

        return t

    quatp1 = Transform.to_quatp(trans1)
    quatp2 = Transform.to_quatp(trans2)

    q1 = np.array(quatp1[:4])  
    p1 = np.array(quatp1[4:])  

    q2 = np.array(quatp2[:4])  
    p2 = np.array(quatp2[4:])

    dist = np.linalg.norm(p1-p2)
    steps = dist/overlap

    q1 /= np.linalg.norm(q1)
    q2 /= np.linalg.norm(q2)

    q1_scipy = np.array([q1[1], q1[2], q1[3], q1[0]])
    q2_scipy = np.array([q2[1], q2[2], q2[3], q2[0]])

    rot1 = R.from_quat(q1_scipy)
    rot2 = R.from_quat(q2_scipy)

    key_times = [0, 1]
    key_rots = R.from_quat([q1_scipy, q2_scipy])
    slerp = Slerp(key_times, key_rots)

    interp_times = np.linspace(0, 1, steps + 1)
    rotations_interp = slerp(interp_times)
    positions_interp = np.outer(1 - interp_times, p1) + np.outer(interp_times, p2)
    transforms = []

    for i in range(steps + 1):
        q_interp_scipy = rotations_interp[i].as_quat()
        q_interp = np.array([q_interp_scipy[3], q_interp_scipy[0], q_interp_scipy[1], q_interp_scipy[2]])
        p_interp = positions_interp[i]
        quatp_interp = np.concatenate((q_interp, p_interp))
        trans_interp = transform_from_quatp(quatp_interp.tolist())
        transforms.append(trans_interp)
        # print_transform(trans_interp, label=f"Step {i}")

    return transforms

def solveAngle(transforms):
    returnAngles = []
    tempAngle = [0,0,0,0,0,0]

    for i, trans in enumerate(transforms):
        try:
            tempAngle = ARM6_kinematics_inverse_arm(trans,tempAngle)
            returnAngles.append(tempAngle)
            if i % 10 == 0 :
                print( f"Step {i} : {tempAngle}")
        except Exception as e:
            print(f"Error at step {i}: {e}")
            returnAngles.append(None)  
    
    return returnAngles

def inter_solve(trans1,trans2,overlap) :

    transforms = interpolate_transforms(trans1,trans2,overlap)
    solvedAngle = solveAngle(transforms)

    return solvedAngle

def main():
    trans1 = realConfig.bfPosition1
    trans2 = Transform.trcopy(trans1)  
    trans2.translateZ(realConfig.bfMovingDown)
    overlap = 0.005  
    transforms = interpolate_transforms(trans1, trans2, overlap)
    solvedAngle = solveAngle(transforms)

if __name__ == "__main__":
    main()
