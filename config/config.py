from lib.transform import Transform
import math

PI = 3.14159265359
SQRT2 = math.sqrt(2)
RAD_TO_DEG = 180.0/PI

class WebotsConfig :
    

    TIME_STEP = 0.01
    


#------------- For Webots Position Logger -------------
    smallCommandStep = 0.01
    bigCommandStep = 0.1

    

# -----------------------------------------------------

    baseLength     = 0.145
    upperArmLength = 0.49
    foreArmLength  = 0.37
    wrist1Length   = 0.1
    wrist2Length   = 0.065

    toolOffsetX = 0.0
    toolOffsetZ = 0.0
    

    initPoseA = [0,0,0,0,0,0]

    initPoseT = Transform.transform().rotateY(-PI/2).translateX(upperArmLength).translateX(foreArmLength).translateY(-wrist1Length).translateX(wrist2Length)

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











# class RealConfig :