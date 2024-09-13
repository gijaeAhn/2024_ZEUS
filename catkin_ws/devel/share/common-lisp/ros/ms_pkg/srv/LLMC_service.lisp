; Auto-generated. Do not edit!


(cl:in-package ms_pkg-srv)


;//! \htmlinclude LLMC_service-request.msg.html

(cl:defclass <LLMC_service-request> (roslisp-msg-protocol:ros-message)
  ((user_text
    :reader user_text
    :initarg :user_text
    :type cl:string
    :initform ""))
)

(cl:defclass LLMC_service-request (<LLMC_service-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <LLMC_service-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'LLMC_service-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ms_pkg-srv:<LLMC_service-request> is deprecated: use ms_pkg-srv:LLMC_service-request instead.")))

(cl:ensure-generic-function 'user_text-val :lambda-list '(m))
(cl:defmethod user_text-val ((m <LLMC_service-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ms_pkg-srv:user_text-val is deprecated.  Use ms_pkg-srv:user_text instead.")
  (user_text m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <LLMC_service-request>) ostream)
  "Serializes a message object of type '<LLMC_service-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'user_text))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'user_text))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <LLMC_service-request>) istream)
  "Deserializes a message object of type '<LLMC_service-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'user_text) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'user_text) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<LLMC_service-request>)))
  "Returns string type for a service object of type '<LLMC_service-request>"
  "ms_pkg/LLMC_serviceRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'LLMC_service-request)))
  "Returns string type for a service object of type 'LLMC_service-request"
  "ms_pkg/LLMC_serviceRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<LLMC_service-request>)))
  "Returns md5sum for a message object of type '<LLMC_service-request>"
  "c855b39a90951aa6be44ba4ed4e45902")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'LLMC_service-request)))
  "Returns md5sum for a message object of type 'LLMC_service-request"
  "c855b39a90951aa6be44ba4ed4e45902")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<LLMC_service-request>)))
  "Returns full string definition for message of type '<LLMC_service-request>"
  (cl:format cl:nil "string user_text~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'LLMC_service-request)))
  "Returns full string definition for message of type 'LLMC_service-request"
  (cl:format cl:nil "string user_text~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <LLMC_service-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'user_text))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <LLMC_service-request>))
  "Converts a ROS message object to a list"
  (cl:list 'LLMC_service-request
    (cl:cons ':user_text (user_text msg))
))
;//! \htmlinclude LLMC_service-response.msg.html

(cl:defclass <LLMC_service-response> (roslisp-msg-protocol:ros-message)
  ((model_text
    :reader model_text
    :initarg :model_text
    :type cl:string
    :initform ""))
)

(cl:defclass LLMC_service-response (<LLMC_service-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <LLMC_service-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'LLMC_service-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ms_pkg-srv:<LLMC_service-response> is deprecated: use ms_pkg-srv:LLMC_service-response instead.")))

(cl:ensure-generic-function 'model_text-val :lambda-list '(m))
(cl:defmethod model_text-val ((m <LLMC_service-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ms_pkg-srv:model_text-val is deprecated.  Use ms_pkg-srv:model_text instead.")
  (model_text m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <LLMC_service-response>) ostream)
  "Serializes a message object of type '<LLMC_service-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'model_text))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'model_text))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <LLMC_service-response>) istream)
  "Deserializes a message object of type '<LLMC_service-response>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'model_text) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'model_text) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<LLMC_service-response>)))
  "Returns string type for a service object of type '<LLMC_service-response>"
  "ms_pkg/LLMC_serviceResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'LLMC_service-response)))
  "Returns string type for a service object of type 'LLMC_service-response"
  "ms_pkg/LLMC_serviceResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<LLMC_service-response>)))
  "Returns md5sum for a message object of type '<LLMC_service-response>"
  "c855b39a90951aa6be44ba4ed4e45902")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'LLMC_service-response)))
  "Returns md5sum for a message object of type 'LLMC_service-response"
  "c855b39a90951aa6be44ba4ed4e45902")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<LLMC_service-response>)))
  "Returns full string definition for message of type '<LLMC_service-response>"
  (cl:format cl:nil "string model_text~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'LLMC_service-response)))
  "Returns full string definition for message of type 'LLMC_service-response"
  (cl:format cl:nil "string model_text~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <LLMC_service-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'model_text))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <LLMC_service-response>))
  "Converts a ROS message object to a list"
  (cl:list 'LLMC_service-response
    (cl:cons ':model_text (model_text msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'LLMC_service)))
  'LLMC_service-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'LLMC_service)))
  'LLMC_service-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'LLMC_service)))
  "Returns string type for a service object of type '<LLMC_service>"
  "ms_pkg/LLMC_service")