; Auto-generated. Do not edit!


(cl:in-package ms_pkg-srv)


;//! \htmlinclude TTS_service-request.msg.html

(cl:defclass <TTS_service-request> (roslisp-msg-protocol:ros-message)
  ((text
    :reader text
    :initarg :text
    :type cl:string
    :initform ""))
)

(cl:defclass TTS_service-request (<TTS_service-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TTS_service-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TTS_service-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ms_pkg-srv:<TTS_service-request> is deprecated: use ms_pkg-srv:TTS_service-request instead.")))

(cl:ensure-generic-function 'text-val :lambda-list '(m))
(cl:defmethod text-val ((m <TTS_service-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ms_pkg-srv:text-val is deprecated.  Use ms_pkg-srv:text instead.")
  (text m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TTS_service-request>) ostream)
  "Serializes a message object of type '<TTS_service-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'text))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'text))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TTS_service-request>) istream)
  "Deserializes a message object of type '<TTS_service-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'text) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'text) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TTS_service-request>)))
  "Returns string type for a service object of type '<TTS_service-request>"
  "ms_pkg/TTS_serviceRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TTS_service-request)))
  "Returns string type for a service object of type 'TTS_service-request"
  "ms_pkg/TTS_serviceRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TTS_service-request>)))
  "Returns md5sum for a message object of type '<TTS_service-request>"
  "05354734935e371f83dc4d09f1c13d77")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TTS_service-request)))
  "Returns md5sum for a message object of type 'TTS_service-request"
  "05354734935e371f83dc4d09f1c13d77")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TTS_service-request>)))
  "Returns full string definition for message of type '<TTS_service-request>"
  (cl:format cl:nil "string text~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TTS_service-request)))
  "Returns full string definition for message of type 'TTS_service-request"
  (cl:format cl:nil "string text~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TTS_service-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'text))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TTS_service-request>))
  "Converts a ROS message object to a list"
  (cl:list 'TTS_service-request
    (cl:cons ':text (text msg))
))
;//! \htmlinclude TTS_service-response.msg.html

(cl:defclass <TTS_service-response> (roslisp-msg-protocol:ros-message)
  ((result
    :reader result
    :initarg :result
    :type cl:fixnum
    :initform 0))
)

(cl:defclass TTS_service-response (<TTS_service-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TTS_service-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TTS_service-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ms_pkg-srv:<TTS_service-response> is deprecated: use ms_pkg-srv:TTS_service-response instead.")))

(cl:ensure-generic-function 'result-val :lambda-list '(m))
(cl:defmethod result-val ((m <TTS_service-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ms_pkg-srv:result-val is deprecated.  Use ms_pkg-srv:result instead.")
  (result m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TTS_service-response>) ostream)
  "Serializes a message object of type '<TTS_service-response>"
  (cl:let* ((signed (cl:slot-value msg 'result)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TTS_service-response>) istream)
  "Deserializes a message object of type '<TTS_service-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'result) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TTS_service-response>)))
  "Returns string type for a service object of type '<TTS_service-response>"
  "ms_pkg/TTS_serviceResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TTS_service-response)))
  "Returns string type for a service object of type 'TTS_service-response"
  "ms_pkg/TTS_serviceResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TTS_service-response>)))
  "Returns md5sum for a message object of type '<TTS_service-response>"
  "05354734935e371f83dc4d09f1c13d77")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TTS_service-response)))
  "Returns md5sum for a message object of type 'TTS_service-response"
  "05354734935e371f83dc4d09f1c13d77")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TTS_service-response>)))
  "Returns full string definition for message of type '<TTS_service-response>"
  (cl:format cl:nil "int8 result~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TTS_service-response)))
  "Returns full string definition for message of type 'TTS_service-response"
  (cl:format cl:nil "int8 result~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TTS_service-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TTS_service-response>))
  "Converts a ROS message object to a list"
  (cl:list 'TTS_service-response
    (cl:cons ':result (result msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'TTS_service)))
  'TTS_service-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'TTS_service)))
  'TTS_service-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TTS_service)))
  "Returns string type for a service object of type '<TTS_service>"
  "ms_pkg/TTS_service")