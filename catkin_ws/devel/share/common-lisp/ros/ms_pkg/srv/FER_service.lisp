; Auto-generated. Do not edit!


(cl:in-package ms_pkg-srv)


;//! \htmlinclude FER_service-request.msg.html

(cl:defclass <FER_service-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass FER_service-request (<FER_service-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <FER_service-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'FER_service-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ms_pkg-srv:<FER_service-request> is deprecated: use ms_pkg-srv:FER_service-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <FER_service-request>) ostream)
  "Serializes a message object of type '<FER_service-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <FER_service-request>) istream)
  "Deserializes a message object of type '<FER_service-request>"
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
  "db954e5de3aba73b237d07575e5cac28")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'FER_service-request)))
  "Returns md5sum for a message object of type 'FER_service-request"
  "db954e5de3aba73b237d07575e5cac28")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<FER_service-request>)))
  "Returns full string definition for message of type '<FER_service-request>"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'FER_service-request)))
  "Returns full string definition for message of type 'FER_service-request"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <FER_service-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <FER_service-request>))
  "Converts a ROS message object to a list"
  (cl:list 'FER_service-request
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
  "db954e5de3aba73b237d07575e5cac28")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'FER_service-response)))
  "Returns md5sum for a message object of type 'FER_service-response"
  "db954e5de3aba73b237d07575e5cac28")
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