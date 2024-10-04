; Auto-generated. Do not edit!


(cl:in-package ms_pkg-srv)


;//! \htmlinclude STT_service-request.msg.html

(cl:defclass <STT_service-request> (roslisp-msg-protocol:ros-message)
  ((file_path
    :reader file_path
    :initarg :file_path
    :type cl:string
    :initform ""))
)

(cl:defclass STT_service-request (<STT_service-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <STT_service-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'STT_service-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ms_pkg-srv:<STT_service-request> is deprecated: use ms_pkg-srv:STT_service-request instead.")))

(cl:ensure-generic-function 'file_path-val :lambda-list '(m))
(cl:defmethod file_path-val ((m <STT_service-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ms_pkg-srv:file_path-val is deprecated.  Use ms_pkg-srv:file_path instead.")
  (file_path m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <STT_service-request>) ostream)
  "Serializes a message object of type '<STT_service-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'file_path))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'file_path))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <STT_service-request>) istream)
  "Deserializes a message object of type '<STT_service-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'file_path) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'file_path) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<STT_service-request>)))
  "Returns string type for a service object of type '<STT_service-request>"
  "ms_pkg/STT_serviceRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'STT_service-request)))
  "Returns string type for a service object of type 'STT_service-request"
  "ms_pkg/STT_serviceRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<STT_service-request>)))
  "Returns md5sum for a message object of type '<STT_service-request>"
  "0b7e0c9192d9ca1d34c68e21095b2124")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'STT_service-request)))
  "Returns md5sum for a message object of type 'STT_service-request"
  "0b7e0c9192d9ca1d34c68e21095b2124")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<STT_service-request>)))
  "Returns full string definition for message of type '<STT_service-request>"
  (cl:format cl:nil "string file_path~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'STT_service-request)))
  "Returns full string definition for message of type 'STT_service-request"
  (cl:format cl:nil "string file_path~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <STT_service-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'file_path))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <STT_service-request>))
  "Converts a ROS message object to a list"
  (cl:list 'STT_service-request
    (cl:cons ':file_path (file_path msg))
))
;//! \htmlinclude STT_service-response.msg.html

(cl:defclass <STT_service-response> (roslisp-msg-protocol:ros-message)
  ((result
    :reader result
    :initarg :result
    :type cl:string
    :initform ""))
)

(cl:defclass STT_service-response (<STT_service-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <STT_service-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'STT_service-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ms_pkg-srv:<STT_service-response> is deprecated: use ms_pkg-srv:STT_service-response instead.")))

(cl:ensure-generic-function 'result-val :lambda-list '(m))
(cl:defmethod result-val ((m <STT_service-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ms_pkg-srv:result-val is deprecated.  Use ms_pkg-srv:result instead.")
  (result m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <STT_service-response>) ostream)
  "Serializes a message object of type '<STT_service-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'result))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'result))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <STT_service-response>) istream)
  "Deserializes a message object of type '<STT_service-response>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'result) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'result) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<STT_service-response>)))
  "Returns string type for a service object of type '<STT_service-response>"
  "ms_pkg/STT_serviceResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'STT_service-response)))
  "Returns string type for a service object of type 'STT_service-response"
  "ms_pkg/STT_serviceResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<STT_service-response>)))
  "Returns md5sum for a message object of type '<STT_service-response>"
  "0b7e0c9192d9ca1d34c68e21095b2124")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'STT_service-response)))
  "Returns md5sum for a message object of type 'STT_service-response"
  "0b7e0c9192d9ca1d34c68e21095b2124")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<STT_service-response>)))
  "Returns full string definition for message of type '<STT_service-response>"
  (cl:format cl:nil "string result~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'STT_service-response)))
  "Returns full string definition for message of type 'STT_service-response"
  (cl:format cl:nil "string result~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <STT_service-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'result))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <STT_service-response>))
  "Converts a ROS message object to a list"
  (cl:list 'STT_service-response
    (cl:cons ':result (result msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'STT_service)))
  'STT_service-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'STT_service)))
  'STT_service-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'STT_service)))
  "Returns string type for a service object of type '<STT_service>"
  "ms_pkg/STT_service")