import sys
import os

home_dir = os.path.expanduser('~')
sys.path.append(os.path.join(home_dir, 'Desktop/2024_ZEUS/'))

import rospy
import numpy as np

# ----------------- ROS Message -----------------

from trajectory_msgs.msg import JointTrajectory ,JointTrajectoryPoint

# -----------------------------------------------

from lib.zeus_kinematics import *
from config.config import realConfig
from config.config import RAD_TO_DEG


def dataTrajectory(shaketype):
    rotate_directions = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    trajectory_msg = JointTrajectory()
    trajectory_msg.joint_names = ['joint1', 'joint2', 'joint3', 'joint4', 'joint5', 'joint6']
    
    with open(shaketype, 'r') as file:
        for idx, line in enumerate(file):
            angles = [float(x) for x in line.strip().split()]
            
            if len(angles) != 6:
                rospy.logwarn("Invalid joint angle line: {}".format(line))
                continue
            
            # Angle = [angle *  RAD_TO_DEG for angle in angles]
            # Angle = [angle * direction for angle, direction in zip(Angle, rotate_directions)]\
            Angle = angles
            
            point = JointTrajectoryPoint()
            point.positions = Angle
            point.time_from_start = rospy.Duration(1) 
            
            trajectory_msg.points.append(point)
    
    return trajectory_msg