; Auto-generated. Do not edit!


(cl:in-package ms_pkg-srv)


;//! \htmlinclude FER_service-request.msg.html

(cl:defclass <FER_service-request> (roslisp-msg-protocol:ros-message)
  ((img
    :reader img
    :initarg :img
    :type sensor_msgs-msg:Image
    :initform (cl:make-instance 'sensor_msgs-msg:Image)))
)

(cl:defclass FER_service-request (<FER_service-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <FER_service-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'FER_service-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ms_pkg-srv:<FER_service-request> is deprecated: use ms_pkg-srv:FER_service-request instead.")))

(cl:ensure-generic-function 'img-val :lambda-list '(m))
(cl:defmethod img-val ((m <FER_service-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ms_pkg-srv:img-val is deprecated.  Use ms_pkg-srv:img instead.")
  (img m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <FER_service-request>) ostream)
  "Serializes a message object of type '<FER_service-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'img) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <FER_service-request>) istream)
  "Deserializes a message object of type '<FER_service-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'img) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<FER_service-request>)))
  "Returns string type for a service object of type '<FER_service-request>"
  "ms_pkg/FER_serviceRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'FER_service-request)))
  "Returns string type for a service object of type 'FER_service-request"
  "ms_pkg/FER_serviceRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<FER_service-request>)))
  "Returns md5sum for a message object of type '<FER_service-request>"
  "7265aed7a01c523a6d802a58fa938c44")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'FER_service-request)))
  "Returns md5sum for a message object of type 'FER_service-request"
  "7265aed7a01c523a6d802a58fa938c44")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<FER_service-request>)))
  "Returns full string definition for message of type '<FER_service-request>"
  (cl:format cl:nil "sensor_msgs/Image img~%~%================================================================================~%MSG: sensor_msgs/Image~%# This message contains an uncompressed image~%# (0, 0) is at top-left corner of image~%#~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of camera~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%                     # If the frame_id here and the frame_id of the CameraInfo~%                     # message associated with the image conflict~%                     # the behavior is undefined~%~%uint32 height         # image height, that is, number of rows~%uint32 width          # image width, that is, number of columns~%~%# The legal values for encoding are in file src/image_encodings.cpp~%# If you want to standardize a new string format, join~%# ros-users@lists.sourceforge.net and send an email proposing a new encoding.~%~%string encoding       # Encoding of pixels -- channel meaning, ordering, size~%                      # taken from the list of strings in include/sensor_msgs/image_encodings.h~%~%uint8 is_bigendian    # is this data bigendian?~%uint32 step           # Full row length in bytes~%uint8[] data          # actual matrix data, size is (step * rows)~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'FER_service-request)))
  "Returns full string definition for message of type 'FER_service-request"
  (cl:format cl:nil "sensor_msgs/Image img~%~%================================================================================~%MSG: sensor_msgs/Image~%# This message contains an uncompressed image~%# (0, 0) is at top-left corner of image~%#~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of camera~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%                     # If the frame_id here and the frame_id of the CameraInfo~%                     # message associated with the image conflict~%                     # the behavior is undefined~%~%uint32 height         # image height, that is, number of rows~%uint32 width          # image width, that is, number of columns~%~%# The legal values for encoding are in file src/image_encodings.cpp~%# If you want to standardize a new string format, join~%# ros-users@lists.sourceforge.net and send an email proposing a new encoding.~%~%string encoding       # Encoding of pixels -- channel meaning, ordering, size~%                      # taken from the list of strings in include/sensor_msgs/image_encodings.h~%~%uint8 is_bigendian    # is this data bigendian?~%uint32 step           # Full row length in bytes~%uint8[] data          # actual matrix data, size is (step * rows)~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <FER_service-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'img))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <FER_service-request>))
  "Converts a ROS message object to a list"
  (cl:list 'FER_service-request
    (cl:cons ':img (img msg))
))
;//! \htmlinclude FER_service-response.msg.html

(cl:defclass <FER_service-response> (roslisp-msg-protocol:ros-message)
  ((result
    :reader result
    :initarg :result
    :type cl:float
    :initform 0.0))
)

(cl:defclass FER_service-response (<FER_service-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <FER_service-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'FER_service-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ms_pkg-srv:<FER_service-response> is deprecated: use ms_pkg-srv:FER_service-response instead.")))

(cl:ensure-generic-function 'result-val :lambda-list '(m))
(cl:defmethod result-val ((m <FER_service-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ms_pkg-srv:result-val is deprecated.  Use ms_pkg-srv:result instead.")
  (result m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <FER_service-response>) ostream)
  "Serializes a message object of type '<FER_service-response>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'result))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <FER_service-response>) istream)
  "Deserializes a message object of type '<FER_service-response>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'result) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<FER_service-response>)))
  "Returns string type for a service object of type '<FER_service-response>"
  "ms_pkg/FER_serviceResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'FER_service-response)))
  "Returns string type for a service object of type 'FER_service-response"
  "ms_pkg/FER_serviceResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<FER_service-response>)))
  "Returns md5sum for a message object of type '<FER_service-response>"
  "7265aed7a01c523a6d802a58fa938c44")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'FER_service-response)))
  "Returns md5sum for a message object of type 'FER_service-response"
  "7265aed7a01c523a6d802a58fa938c44")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<FER_service-response>)))
  "Returns full string definition for message of type '<FER_service-response>"
  (cl:format cl:nil "float32 result~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'FER_service-response)))
  "Returns full string definition for message of type 'FER_service-response"
  (cl:format cl:nil "float32 result~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <FER_service-response>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <FER_service-response>))
  "Converts a ROS message object to a list"
  (cl:list 'FER_service-response
    (cl:cons ':result (result msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'FER_service)))
  'FER_service-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'FER_service)))
  'FER_service-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'FER_service)))
  "Returns string type for a service object of type '<FER_service>"
  "ms_pkg/FER_service")