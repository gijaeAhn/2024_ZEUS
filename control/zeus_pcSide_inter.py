#!/usr/bin/python3
import rospy
import sys
import termios
import tty
import threading
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from std_msgs.msg import Int32
def getch():
    """Read a single character from standard input without echoing to the console."""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    except Exception as e:
        print(e)
        ch = ''
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
def main():
    rospy.init_node('keyboard_control_node')
    # Publishers
    joint_pub = rospy.Publisher('/joint_group_position_controller/command', JointTrajectory, queue_size=1)
    relmove_pub = rospy.Publisher('/joint_finger_position_controller/command', JointTrajectory, queue_size=1)
    mapcmd_pub = rospy.Publisher('/mapcmd', Int32, queue_size=1)
    print("Keyboard Control Node Initialized.")
    print("Use 'w', 'a', 's', 'd', 'q', 'e' keys for relative movement.")
    print("Use '1', '2', '3', '4' for predefined joint positions.")
    print("Press 'g' to open gripper, 'h' to close gripper, 'c' to clear gripper, 'm' for motion parameter.")
    # Define relative movement increments (in meters)
    dx = 0.01  # 1 cm movement
    dy = 0.01
    dz = 0.01
    # Define predefined joint positions (in radians)
    # Adjust these positions according to your robot's configuration
    joint_positions = {
        '1': [0, 20, -110, 120, 0, 0],  # Home position
        '2': [0.5, -0.5, 0.5, -0.5, 0.5, -0.5],
        '3': [1.0, 0.0, -1.0, 0.0, 1.0, 0.0],
        '4': [-0.5, 0.5, -0.5, 0.5, -0.5, 0.5],
        '0': [0,0,0,0,0,0]
    }
    # Relative movement mapping
    rel_move_mapping = {
        'w': (dx, 0, 0),     # Move +x
        's': (-dx, 0, 0),    # Move -x
        'a': (0, dy, 0),     # Move +y
        'd': (0, -dy, 0),    # Move -y
        'q': (0, 0, dz),     # Move +z
        'e': (0, 0, -dz)     # Move -z
    }
    # Gripper commands mapping
    gripper_commands = {
        'g': 0,  # Open gripper
        'h': 1,  # Close gripper
        'c': 2,  # Clear gripper
        'm': 3   # Motion parameter command
    }
    print("Ready to receive keyboard inputs.")
    try:
        while not rospy.is_shutdown():
            ch = getch()
            if ch in rel_move_mapping:
                dx_cmd, dy_cmd, dz_cmd = rel_move_mapping[ch]
                print("Relative move command: dx={}, dy={}, dz={}".format(dx_cmd, dy_cmd, dz_cmd))
                # Create JointTrajectory message for relative movement
                traj_msg = JointTrajectory()
                traj_msg.header.stamp = rospy.Time.now()
                traj_point = JointTrajectoryPoint()
                traj_point.positions = [dx_cmd, dy_cmd, dz_cmd,0.0, 0.0, 0.0]
                traj_point.time_from_start = rospy.Duration(0.5)
                traj_msg.points.append(traj_point)
                relmove_pub.publish(traj_msg)
            elif ch in joint_positions:
                positions = joint_positions[ch]
                print("Moving to predefined joint position {}: {}".format(ch, positions))
                # Create JointTrajectory message for joint movement
                traj_msg = JointTrajectory()
                traj_msg.header.stamp = rospy.Time.now()
                traj_msg.joint_names = ['joint1', 'joint2', 'joint3', 'joint4', 'joint5', 'joint6']
                traj_point = JointTrajectoryPoint()
                traj_point.positions = positions
                traj_point.time_from_start = rospy.Duration(1.0)
                traj_msg.points.append(traj_point)
                joint_pub.publish(traj_msg)
            elif ch in gripper_commands:
                cmd = gripper_commands[ch]
                print("Gripper command '{}': {}".format(ch, cmd))
                mapcmd_msg = Int32()
                mapcmd_msg.data = cmd
                mapcmd_pub.publish(mapcmd_msg)
            elif ch == '\x03' or ch == '\x04':  # Ctrl-C or Ctrl-D to exit
                print("Exiting.")
                break
            else:
                print("Invalid key pressed: '{}'".format(ch))
    except rospy.ROSInterruptException:
        pass
    except Exception as e:
        print(e)
    finally:
        print("Shutting down.")
if __name__ == '__main__':
    main()
