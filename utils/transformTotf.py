import sys

sys.path.append('/home/sjlab3090/Desktop/2024_ZEUS/')


from lib.zeus_kinematics import *

import tf2_msgs.msg
import tf2_ros
import tf2_msgs
import geometry_msgs.msg
import tf_conversions

import rospy 

from scipy.spatial.transform import Rotation as R   



DEG_TO_RAD = 0.0174533



def transformToTfMessage(tr):
    translate  = [tr.getVal(0,3),tr.getVal(1,3),tr.getVal(2,3)]

    trDiagonal = tr.getVal(0,0) + tr.getVal(1,1) + tr.getVal(2,2)
    
    rotation_matrix = [
        [tr.getVal(0, 0), tr.getVal(0, 1), tr.getVal(0, 2)],
        [tr.getVal(1, 0), tr.getVal(1, 1), tr.getVal(1, 2)],
        [tr.getVal(2, 0), tr.getVal(2, 1), tr.getVal(2, 2)]]
    

    r = R.from_matrix(rotation_matrix)
    quaternion = r.as_quat()

    t =geometry_msgs.msg.TransformStamped()
    t.transform.translation.x = translate[0]
    t.transform.translation.y = translate[1]
    t.transform.translation.z = translate[2]

    t.transform.rotation.x = quaternion[0]
    t.transform.rotation.y = quaternion[1]
    t.transform.rotation.z = quaternion[2]
    t.transform.rotation.w = quaternion[3]

    print(translate)
    print(quaternion)

    return t

def TfMessageToTransform(Msg):
    
    tr = Transform()
    
    translate = (Msg.transform.translation.x,
                 Msg.transform.translation.y,
                 Msg.transform.translation.z)
        
    qrotation = (Msg.transform.rotation.x,
                 Msg.transform.rotation.y,
                 Msg.transform.rotation.z,
                 Msg.transform.rotation.w)
    
    #  Cannot assign to function call
    tr.setVal(0, 0, 1 - 2 * qrotation[1]**2 - 2 * qrotation[2]**2)
    tr.setVal(0, 1, 2 * qrotation[0] * qrotation[1] - 2 * qrotation[2] * qrotation[3])
    tr.setVal(0, 2, 2 * qrotation[0] * qrotation[2] + 2 * qrotation[1] * qrotation[3])
    tr.setVal(0, 3, translate[0])
    
    tr.setVal(1, 0 ,2 * qrotation[0] * qrotation[1] + 2 * qrotation[2] * qrotation[3])
    tr.setVal(1, 1 ,1 - 2 * qrotation[0]**2 - 2 * qrotation[2]**2)
    tr.setVal(1, 2 ,2 * qrotation[1] * qrotation[2] - 2 * qrotation[0] * qrotation[3])
    tr.setVal(1, 3 ,translate[1])
    
    tr.setVal(2, 0, 2 * qrotation[0] * qrotation[2] - 2 * qrotation[1] * qrotation[3])
    tr.setVal(2, 1, 2 * qrotation[1] * qrotation[2] + 2 * qrotation[0] * qrotation[3])
    tr.setVal(2, 2, 1 - 2 * qrotation[0]**2 - 2 * qrotation[1]**2)
    tr.setVal(2, 3, translate[2])

    return tr



def main():

    br = tf2_ros.TransformBroadcaster()
    rospy.init_node('transform_test', anonymous=True)
    
    testTR = Transform()

    testTR.translateX(0.5)
    testTR.translateY(0.5)
    testTR.translateZ(-0.5)

    testTR.rotateX(90*DEG_TO_RAD)


    Transform.printTransform(testTR)

    testTF = transformToTfMessage(testTR)

  

    testTF.child_frame_id = "world"
    testTF.header.frame_id = "test_link"
    testTF.header.stamp = rospy.Time.now()

    tfMsg = tf2_msgs.msg.TFMessage([testTF])

    br.pub_tf.publish(tfMsg)


if __name__ == '__main__':
    main() 


