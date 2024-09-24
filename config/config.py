import sys
import os

home_dir = os.path.expanduser('~')

sys.path.append(os.path.join(home_dir, 'Desktop/2024_ZEUS/'))
from lib.zeus_kinematics import *
import math

PI = 3.14159265359
SQRT2 = math.sqrt(2)
RAD_TO_DEG = 180.0/PI

# Webots Config
class WebotsConfig :

    TIME_STEP = 0.01
    SHORT_SLEEP  = 0.1
    NORMAL_SLEEP = 1.0
    LONG_SLEEP   = 10.0

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

    # ----- These values will gonna change
    pose1A   = [10,10,10,10,10,10]   

    pose2A   = [20,20,20,20,20,20]

    pose3A   = [20,20,20,20,20,20]

    pose4A   = [20,20,20,20,20,20]

    pose5A   = [20,20,20,20,20,20]

    pose6A   = [20,20,20,20,20,20]

    startPoseT = Transform().translateZ(0.4).translateX(0.3).rotateY(PI/2)

    startPoseA = ARM6_kinematics_inverse_arm(startPoseT,initPoseA)

    dispensorT = Transform()

    shakingT = Transform()
    
    servicePositionT = Transform()

#--------------------------------------------------------

    # menuList = ['A', 'B', 'C', 'D', 'E']
    # menuOffset = {
    # 'A': [0, 0, 0],
    # 'B': [0, 0, 0],
    # 'C': [0, 0, 0],
    # 'D': [0, 0, 0],
    # 'E': [0, 0, 0]
    # }

    menuList = ['마티니', '깔루아밀크', '미도리샤워']
    menuOffset = {
    '마티니': [0, 0, 0],
    '깔루아밀크': [0, 0, 0],
    '미도리샤워': [0, 0, 0],
    'D': [0, 0, 0],
    'E': [0, 0, 0]
    }

    pourAngle = PI * 0.666


class realConfig :
    
    TIME_STEP = 0.01
    SHORT_SLEEP  = 0.1
    NORMAL_SLEEP = 1.0
    LONG_SLEEP   = 10.0
    
 #------------ Robot ----------------------------------

    jointNameList = ['joint1',
                     'joint2',
                     'joint3',
                     'joint4',
                     'joint5',
                     'joint6']

    DOF = 6

    ROTATE_DIRECTION = [1.0, -1.0, -1.0, 1.0, -1.0, 1.0]

   
#------------- For Real Position Logger -------------
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

    # ----- These values will gonna change
    pose1A   = [10,10,10,10,10,10]   

    pose2A   = [20,20,20,20,20,20]

    pose3A   = [20,20,20,20,20,20]

    pose4A   = [20,20,20,20,20,20]



    startPoseT = Transform().translateZ(0.4).translateX(0.3).rotateY(PI/2)

    startPoseA = ARM6_kinematics_inverse_arm(startPoseT,initPoseA)

    dispensorT = Transform()

    shakingT = Transform()
    
    servicePositionT = Transform()


#--------------------------------------------------------

    menuList = ['A', 'B', 'C', 'D', 'E']


    #OFFSET Unit : Meter
    menuOffset = {
    'A': [0, 0, 0],
    'B': [0, 0, 0],
    'C': [0, 0, 0],
    'D': [0, 0, 0],
    'E': [0, 0, 0]
    }

    pourAngle = PI * 0.666



