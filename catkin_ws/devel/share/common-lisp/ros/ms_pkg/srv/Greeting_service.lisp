; Auto-generated. Do not edit!


(cl:in-package ms_pkg-srv)


;//! \htmlinclude Greeting_service-request.msg.html

(cl:defclass <Greeting_service-request> (roslisp-msg-protocol:ros-message)
  ((action
    :reader action
    :initarg :action
    :type cl:string
    :initform "")
   (image_path
    :reader image_path
    :initarg :image_path
    :type cl:string
    :initform "")
   (user_prompt
    :reader user_prompt
    :initarg :user_prompt
    :type cl:string
    :initform ""))
)

(cl:defclass Greeting_service-request (<Greeting_service-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Greeting_service-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Greeting_service-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ms_pkg-srv:<Greeting_service-request> is deprecated: use ms_pkg-srv:Greeting_service-request instead.")))

(cl:ensure-generic-function 'action-val :lambda-list '(m))
(cl:defmethod action-val ((m <Greeting_service-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ms_pkg-srv:action-val is deprecated.  Use ms_pkg-srv:action instead.")
  (action m))

(cl:ensure-generic-function 'image_path-val :lambda-list '(m))
(cl:defmethod image_path-val ((m <Greeting_service-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ms_pkg-srv:image_path-val is deprecated.  Use ms_pkg-srv:image_path instead.")
  (image_path m))

(cl:ensure-generic-function 'user_prompt-val :lambda-list '(m))
(cl:defmethod user_prompt-val ((m <Greeting_service-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ms_pkg-srv:user_prompt-val is deprecated.  Use ms_pkg-srv:user_prompt instead.")
  (user_prompt m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Greeting_service-request>) ostream)
  "Serializes a message object of type '<Greeting_service-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'action))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'action))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'image_path))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'image_path))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'user_prompt))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'user_prompt))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Greeting_service-request>) istream)
  "Deserializes a message object of type '<Greeting_service-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'action) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'action) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'image_path) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'image_path) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'user_prompt) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'user_prompt) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Greeting_service-request>)))
  "Returns string type for a service object of type '<Greeting_service-request>"
  "ms_pkg/Greeting_serviceRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Greeting_service-request)))
  "Returns string type for a service object of type 'Greeting_service-request"
  "ms_pkg/Greeting_serviceRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Greeting_service-request>)))
  "Returns md5sum for a message object of type '<Greeting_service-request>"
  "f58cc1930ee734da0da3606508759ab9")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Greeting_service-request)))
  "Returns md5sum for a message object of type 'Greeting_service-request"
  "f58cc1930ee734da0da3606508759ab9")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Greeting_service-request>)))
  "Returns full string definition for message of type '<Greeting_service-request>"
  (cl:format cl:nil "string action~%string image_path~%string user_prompt~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Greeting_service-request)))
  "Returns full string definition for message of type 'Greeting_service-request"
  (cl:format cl:nil "string action~%string image_path~%string user_prompt~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Greeting_service-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'action))
     4 (cl:length (cl:slot-value msg 'image_path))
     4 (cl:length (cl:slot-value msg 'user_prompt))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Greeting_service-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Greeting_service-request
    (cl:cons ':action (action msg))
    (cl:cons ':image_path (image_path msg))
    (cl:cons ':user_prompt (user_prompt msg))
))
;//! \htmlinclude Greeting_service-response.msg.html

(cl:defclass <Greeting_service-response> (roslisp-msg-protocol:ros-message)
  ((result
    :reader result
    :initarg :result
    :type cl:string
    :initform ""))
)

(cl:defclass Greeting_service-response (<Greeting_service-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Greeting_service-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Greeting_service-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ms_pkg-srv:<Greeting_service-response> is deprecated: use ms_pkg-srv:Greeting_service-response instead.")))

(cl:ensure-generic-function 'result-val :lambda-list '(m))
(cl:defmethod result-val ((m <Greeting_service-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ms_pkg-srv:result-val is deprecated.  Use ms_pkg-srv:result instead.")
  (result m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Greeting_service-response>) ostream)
  "Serializes a message object of type '<Greeting_service-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'result))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'result))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Greeting_service-response>) istream)
  "Deserializes a message object of type '<Greeting_service-response>"
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Greeting_service-response>)))
  "Returns string type for a service object of type '<Greeting_service-response>"
  "ms_pkg/Greeting_serviceResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Greeting_service-response)))
  "Returns string type for a service object of type 'Greeting_service-response"
  "ms_pkg/Greeting_serviceResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Greeting_service-response>)))
  "Returns md5sum for a message object of type '<Greeting_service-response>"
  "f58cc1930ee734da0da3606508759ab9")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Greeting_service-response)))
  "Returns md5sum for a message object of type 'Greeting_service-response"
  "f58cc1930ee734da0da3606508759ab9")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Greeting_service-response>)))
  "Returns full string definition for message of type '<Greeting_service-response>"
  (cl:format cl:nil "string result~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Greeting_service-response)))
  "Returns full string definition for message of type 'Greeting_service-response"
  (cl:format cl:nil "string result~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Greeting_service-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'result))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Greeting_service-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Greeting_service-response
    (cl:cons ':result (result msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Greeting_service)))
  'Greeting_service-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Greeting_service)))
  'Greeting_service-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Greeting_service)))
  "Returns string type for a service object of type '<Greeting_service>"
  "ms_pkg/Greeting_service")