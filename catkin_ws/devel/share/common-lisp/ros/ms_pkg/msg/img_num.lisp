; Auto-generated. Do not edit!


(cl:in-package ms_pkg-msg)


;//! \htmlinclude img_num.msg.html

(cl:defclass <img_num> (roslisp-msg-protocol:ros-message)
  ((img
    :reader img
    :initarg :img
    :type sensor_msgs-msg:Image
    :initform (cl:make-instance 'sensor_msgs-msg:Image))
   (msg_seq
    :reader msg_seq
    :initarg :msg_seq
    :type cl:fixnum
    :initform 0))
)

(cl:defclass img_num (<img_num>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <img_num>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'img_num)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ms_pkg-msg:<img_num> is deprecated: use ms_pkg-msg:img_num instead.")))

(cl:ensure-generic-function 'img-val :lambda-list '(m))
(cl:defmethod img-val ((m <img_num>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ms_pkg-msg:img-val is deprecated.  Use ms_pkg-msg:img instead.")
  (img m))

(cl:ensure-generic-function 'msg_seq-val :lambda-list '(m))
(cl:defmethod msg_seq-val ((m <img_num>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ms_pkg-msg:msg_seq-val is deprecated.  Use ms_pkg-msg:msg_seq instead.")
  (msg_seq m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <img_num>) ostream)
  "Serializes a message object of type '<img_num>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'img) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'msg_seq)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'msg_seq)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <img_num>) istream)
  "Deserializes a message object of type '<img_num>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'img) istream)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'msg_seq)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'msg_seq)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<img_num>)))
  "Returns string type for a message object of type '<img_num>"
  "ms_pkg/img_num")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'img_num)))
  "Returns string type for a message object of type 'img_num"
  "ms_pkg/img_num")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<img_num>)))
  "Returns md5sum for a message object of type '<img_num>"
  "f03678201ea54f45ff6f4b17e7685f68")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'img_num)))
  "Returns md5sum for a message object of type 'img_num"
  "f03678201ea54f45ff6f4b17e7685f68")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<img_num>)))
  "Returns full string definition for message of type '<img_num>"
  (cl:format cl:nil "sensor_msgs/Image img~%uint16 msg_seq~%================================================================================~%MSG: sensor_msgs/Image~%# This message contains an uncompressed image~%# (0, 0) is at top-left corner of image~%#~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of camera~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%                     # If the frame_id here and the frame_id of the CameraInfo~%                     # message associated with the image conflict~%                     # the behavior is undefined~%~%uint32 height         # image height, that is, number of rows~%uint32 width          # image width, that is, number of columns~%~%# The legal values for encoding are in file src/image_encodings.cpp~%# If you want to standardize a new string format, join~%# ros-users@lists.sourceforge.net and send an email proposing a new encoding.~%~%string encoding       # Encoding of pixels -- channel meaning, ordering, size~%                      # taken from the list of strings in include/sensor_msgs/image_encodings.h~%~%uint8 is_bigendian    # is this data bigendian?~%uint32 step           # Full row length in bytes~%uint8[] data          # actual matrix data, size is (step * rows)~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'img_num)))
  "Returns full string definition for message of type 'img_num"
  (cl:format cl:nil "sensor_msgs/Image img~%uint16 msg_seq~%================================================================================~%MSG: sensor_msgs/Image~%# This message contains an uncompressed image~%# (0, 0) is at top-left corner of image~%#~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of camera~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%                     # If the frame_id here and the frame_id of the CameraInfo~%                     # message associated with the image conflict~%                     # the behavior is undefined~%~%uint32 height         # image height, that is, number of rows~%uint32 width          # image width, that is, number of columns~%~%# The legal values for encoding are in file src/image_encodings.cpp~%# If you want to standardize a new string format, join~%# ros-users@lists.sourceforge.net and send an email proposing a new encoding.~%~%string encoding       # Encoding of pixels -- channel meaning, ordering, size~%                      # taken from the list of strings in include/sensor_msgs/image_encodings.h~%~%uint8 is_bigendian    # is this data bigendian?~%uint32 step           # Full row length in bytes~%uint8[] data          # actual matrix data, size is (step * rows)~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <img_num>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'img))
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <img_num>))
  "Converts a ROS message object to a list"
  (cl:list 'img_num
    (cl:cons ':img (img msg))
    (cl:cons ':msg_seq (msg_seq msg))
))
