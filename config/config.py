import sys
import os

home_dir = os.path.expanduser('~')

sys.path.append(os.path.join(home_dir, 'Desktop/2024_ZEUS/'))
from lib.zeus_kinematics import *
import math

PI = 3.14159265359
SQRT2 = math.sqrt(2)
RAD_TO_DEG = 57.2957795131

# Webots Config
class WebotsConfig :

    TIME_STEP = 0.01
    SHORT_SLEEP  = 1.0
    NORMAL_SLEEP = 0.5
    LONG_SLEEP   = 0.1

    ROTATE_DIRECTION = [1.0, -1.0, -1.0, 1.0, -1.0, 1.0]
    
 #------------ Robot ----------------------------------

    jointNameList = ['joint1',
                     'joint2',
                     'joint3',
                     'joint4',
                     'joint5',
                     'joint6']

    DOF = 6
   
#------------- For Webots Position Logger -------------
    smallCommandStep = 0.01
    bigCommandStep   = 0.1

# -----------------------------------------------------

    baseLength     = 0.145
    upperArmLength = 0.49
    foreArmLength  = 0.37
    wrist1Length   = 0.1
    wrist2Length   = 0.065

    toolOffsetX = 0.0
    toolOffsetZ = 0.0
    

    initPoseA = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    initPoseT = Transform().rotateY(-PI/2).translateX(upperArmLength).translateX(foreArmLength).translateY(-wrist1Length).translateX(wrist2Length)

    defaultAngleVelocity = [2.0,2.0,2.0,2.0,2.0,2.0]

    

# ----------- PREDEFINED POSITIONS  -------------------

# ----------- Name Refactoring Required ---------------

# ----------- Two Types of Pose Available -------------

# ----------- 1. Pose represented in angle(degree) ----

# ----------- 2. Pose represented in Transfomr Matrix -

    startPoseT = Transform().translateZ(0.4).translateX(0.3).rotateY(PI/2)

    dispensorT = Transform()

    shakingT = Transform()

    greetT = Transform()
    
    servicePositionT = Transform()

#--------------------------------------------------------

    menuList = ['A', 'B', 'C', 'D', 'E']

    menuOffset = {
    'A': [0, 0, 0],
    'B': [0, 0, 0],
    'C': [0, 0, 0],
    'D': [0, 0, 0],
    'E': [0, 0, 0]
    }

    pourAngle = PI * 0.666




# ----------------------------------Real----------------------------------------------------------------------


class realConfig :
    
    TIME_STEP = 0.01
    
    SHORT_SLEEP  = 2.0      # 0.4s
    NORMAL_SLEEP = 1.0      # 1.0s
    LONG_SLEEP   = 0.1      # 10.0s
    
 #------------ Robot ----------------------------------

    jointNameList = ['joint1',
                     'joint2',
                     'joint3',
                     'joint4',
                     'joint5',
                     'joint6']

    DOF = 6

    ROTATE_DIRECTION = [1.0, -1.0, -1.0, 1.0, -1.0, 1.0]

    baseLength     = 0.145
    upperArmLength = 0.49
    foreArmLength  = 0.37
    wrist1Length   = 0.1
    wrist2Length   = 0.065
        
    defaultAngleVelocity = [2.0,2.0,2.0,2.0,2.0,2.0]

   
#------------- For Real Position Logger -------------
    smallCommandStep = 0.05
    bigCommandStep   = 0.05

# ----------- PREDEFINED POSITIONS  -------------------

# ----------- Name Refactoring Required ---------------

# ----------- Two Types of Pose Available -------------

# ----------- 1. Pose represented in angle(degree) ----

# ----------- 2. Pose represented in Transfomr Matrix -
    
    initPoseA = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    initPoseT        = Transform().rotateY(-PI/2).translateX(upperArmLength).translateX(foreArmLength).translateY(-wrist1Length).translateX(wrist2Length)
    startPoseT       = Transform().rotateZ(PI).translateZ(0.3).translateX(0.3).rotateY(PI/2)
    barPoseT         = Transform().rotateZ(PI/2).translateZ(0.3).translateX(0.3).rotateY(PI/2)
    shakingT         = Transform().translateZ(0.3).translateX(0.3).rotateY(PI/2)
    servicePositionT = Transform.trcopy(shakingT)
    servicePositionT = servicePositionT.translateZ(0.1).translateX(0.1)

    shakeType1 = os.path.join(os.path.expanduser('~'), "Desktop", "2024_ZEUS", "shake_traj", "shake3.txt")


#--------------- For Menu -----------------------------------------
    # Robot Orig = {0.1, 0.1, 0.0152}
    # Plate Offset = 0.0152
    # Unit : Meter 

    # Menu Setup
    menuList = ['1', '2', '3', '4', '5', '6']
    menuComponent = {
        '1' : ['A','B'],
        '2' : ['A','C'],
        '3' : ['A','D'],
        '4' : ['B','C'],
        '5' : ['B','D'],
        '6' : ['C','D']
    }

    toProfile = 0.75 
    disOffset = 0.086
    plateOffset = 0.0152
    toolOffsetZ = 0.068
    toolOffsetX = 0.068
    disFromOrig = toProfile - disOffset - toolOffsetZ

    # Distance from Z = 0.3
    goUP1 = 0.118 - plateOffset - toolOffsetX
    goUP2 = 0.018
    goFront = disFromOrig - barPoseT.getVal(1,3)

    componentOffset = {
    'A': [ 0.05,    goFront, goUP1, goUP2],
    'B': [ 0.15,    goFront, goUP1, goUP2],
    'C': [ 0.25,    goFront, goUP1, goUP2],
    'D': [ 0.35,    goFront, goUP1, goUP2],
    'E': [ 0.45,    goFront, goUP1, goUP2]
    }

    pourAngle = PI * 0.666

    # -------------- For Bottle Flip ------------------
    bottleGripZ = 0.227 + 0.07925 - plateOffset

    tempJointBF       = [0,0,0,0,0]

    bottleGripPreZ    = 0.5
    bottleGripOffset  = 0.005
    bfPosition1       = Transform().translateZ(bottleGripPreZ).translateY(0.1).translateX(0.25).rotateY(PI)
    bfPosition1A      = ARM6_kinematics_inverse_arm(bfPosition1,tempJointBF)

    bfMovingUp        =  bottleGripPreZ - bottleGripZ + bottleGripOffset
    bfMovingDown      = -bfMovingUp

    bfPosition2A      = bfPosition1A.copy()
    bfPosition2A[0]   += (PI/18.0) * 4    
    bfPosition2A[5]   += (PI/18.0) * 5 
    bfPosition2A[5]   -= 0.06288061279

    bfPosition3A      = bfPosition2A.copy()
    bfPosition3A[1]  += (PI/18.0) * 3
    bfPosition3A[2]  += (PI/18.0) * 2

    bfPosition4A      = bfPosition3A.copy()
    bfPosition4A[1]  -= (PI/18.0) * 6
    bfPosition4A[2]  -= (PI/18.0) * 5
    bfPosition4A[4]  -= (PI/18.0) * 8.5
    # -------------------------------------------------




