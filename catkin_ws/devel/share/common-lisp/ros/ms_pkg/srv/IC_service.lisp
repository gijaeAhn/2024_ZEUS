; Auto-generated. Do not edit!


(cl:in-package ms_pkg-srv)


;//! \htmlinclude IC_service-request.msg.html

(cl:defclass <IC_service-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass IC_service-request (<IC_service-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <IC_service-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'IC_service-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ms_pkg-srv:<IC_service-request> is deprecated: use ms_pkg-srv:IC_service-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <IC_service-request>) ostream)
  "Serializes a message object of type '<IC_service-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <IC_service-request>) istream)
  "Deserializes a message object of type '<IC_service-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<IC_service-request>)))
  "Returns string type for a service object of type '<IC_service-request>"
  "ms_pkg/IC_serviceRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'IC_service-request)))
  "Returns string type for a service object of type 'IC_service-request"
  "ms_pkg/IC_serviceRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<IC_service-request>)))
  "Returns md5sum for a message object of type '<IC_service-request>"
  "4414c67819626a1b8e0f043a9a0d6c9a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'IC_service-request)))
  "Returns md5sum for a message object of type 'IC_service-request"
  "4414c67819626a1b8e0f043a9a0d6c9a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<IC_service-request>)))
  "Returns full string definition for message of type '<IC_service-request>"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'IC_service-request)))
  "Returns full string definition for message of type 'IC_service-request"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <IC_service-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <IC_service-request>))
  "Converts a ROS message object to a list"
  (cl:list 'IC_service-request
))
;//! \htmlinclude IC_service-response.msg.html

(cl:defclass <IC_service-response> (roslisp-msg-protocol:ros-message)
  ((result
    :reader result
    :initarg :result
    :type cl:fixnum
    :initform 0))
)

(cl:defclass IC_service-response (<IC_service-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <IC_service-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'IC_service-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ms_pkg-srv:<IC_service-response> is deprecated: use ms_pkg-srv:IC_service-response instead.")))

(cl:ensure-generic-function 'result-val :lambda-list '(m))
(cl:defmethod result-val ((m <IC_service-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ms_pkg-srv:result-val is deprecated.  Use ms_pkg-srv:result instead.")
  (result m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <IC_service-response>) ostream)
  "Serializes a message object of type '<IC_service-response>"
  (cl:let* ((signed (cl:slot-value msg 'result)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <IC_service-response>) istream)
  "Deserializes a message object of type '<IC_service-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'result) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<IC_service-response>)))
  "Returns string type for a service object of type '<IC_service-response>"
  "ms_pkg/IC_serviceResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'IC_service-response)))
  "Returns string type for a service object of type 'IC_service-response"
  "ms_pkg/IC_serviceResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<IC_service-response>)))
  "Returns md5sum for a message object of type '<IC_service-response>"
  "4414c67819626a1b8e0f043a9a0d6c9a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'IC_service-response)))
  "Returns md5sum for a message object of type 'IC_service-response"
  "4414c67819626a1b8e0f043a9a0d6c9a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<IC_service-response>)))
  "Returns full string definition for message of type '<IC_service-response>"
  (cl:format cl:nil "int8 result~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'IC_service-response)))
  "Returns full string definition for message of type 'IC_service-response"
  (cl:format cl:nil "int8 result~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <IC_service-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <IC_service-response>))
  "Converts a ROS message object to a list"
  (cl:list 'IC_service-response
    (cl:cons ':result (result msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'IC_service)))
  'IC_service-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'IC_service)))
  'IC_service-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'IC_service)))
  "Returns string type for a service object of type '<IC_service>"
  "ms_pkg/IC_service")