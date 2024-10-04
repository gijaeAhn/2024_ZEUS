;; Auto-generated. Do not edit!


(when (boundp 'ms_pkg::Greeting_service)
  (if (not (find-package "MS_PKG"))
    (make-package "MS_PKG"))
  (shadow 'Greeting_service (find-package "MS_PKG")))
(unless (find-package "MS_PKG::GREETING_SERVICE")
  (make-package "MS_PKG::GREETING_SERVICE"))
(unless (find-package "MS_PKG::GREETING_SERVICEREQUEST")
  (make-package "MS_PKG::GREETING_SERVICEREQUEST"))
(unless (find-package "MS_PKG::GREETING_SERVICERESPONSE")
  (make-package "MS_PKG::GREETING_SERVICERESPONSE"))

(in-package "ROS")





(defclass ms_pkg::Greeting_serviceRequest
  :super ros::object
  :slots (_action _image_path _user_prompt ))

(defmethod ms_pkg::Greeting_serviceRequest
  (:init
   (&key
    ((:action __action) "")
    ((:image_path __image_path) "")
    ((:user_prompt __user_prompt) "")
    )
   (send-super :init)
   (setq _action (string __action))
   (setq _image_path (string __image_path))
   (setq _user_prompt (string __user_prompt))
   self)
  (:action
   (&optional __action)
   (if __action (setq _action __action)) _action)
  (:image_path
   (&optional __image_path)
   (if __image_path (setq _image_path __image_path)) _image_path)
  (:user_prompt
   (&optional __user_prompt)
   (if __user_prompt (setq _user_prompt __user_prompt)) _user_prompt)
  (:serialization-length
   ()
   (+
    ;; string _action
    4 (length _action)
    ;; string _image_path
    4 (length _image_path)
    ;; string _user_prompt
    4 (length _user_prompt)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _action
       (write-long (length _action) s) (princ _action s)
     ;; string _image_path
       (write-long (length _image_path) s) (princ _image_path s)
     ;; string _user_prompt
       (write-long (length _user_prompt) s) (princ _user_prompt s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _action
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _action (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _image_path
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _image_path (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _user_prompt
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _user_prompt (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass ms_pkg::Greeting_serviceResponse
  :super ros::object
  :slots (_result ))

(defmethod ms_pkg::Greeting_serviceResponse
  (:init
   (&key
    ((:result __result) "")
    )
   (send-super :init)
   (setq _result (string __result))
   self)
  (:result
   (&optional __result)
   (if __result (setq _result __result)) _result)
  (:serialization-length
   ()
   (+
    ;; string _result
    4 (length _result)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _result
       (write-long (length _result) s) (princ _result s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _result
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _result (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass ms_pkg::Greeting_service
  :super ros::object
  :slots ())

(setf (get ms_pkg::Greeting_service :md5sum-) "f58cc1930ee734da0da3606508759ab9")
(setf (get ms_pkg::Greeting_service :datatype-) "ms_pkg/Greeting_service")
(setf (get ms_pkg::Greeting_service :request) ms_pkg::Greeting_serviceRequest)
(setf (get ms_pkg::Greeting_service :response) ms_pkg::Greeting_serviceResponse)

(defmethod ms_pkg::Greeting_serviceRequest
  (:response () (instance ms_pkg::Greeting_serviceResponse :init)))

(setf (get ms_pkg::Greeting_serviceRequest :md5sum-) "f58cc1930ee734da0da3606508759ab9")
(setf (get ms_pkg::Greeting_serviceRequest :datatype-) "ms_pkg/Greeting_serviceRequest")
(setf (get ms_pkg::Greeting_serviceRequest :definition-)
      "string action
string image_path
string user_prompt
---
string result


")

(setf (get ms_pkg::Greeting_serviceResponse :md5sum-) "f58cc1930ee734da0da3606508759ab9")
(setf (get ms_pkg::Greeting_serviceResponse :datatype-) "ms_pkg/Greeting_serviceResponse")
(setf (get ms_pkg::Greeting_serviceResponse :definition-)
      "string action
string image_path
string user_prompt
---
string result


")



(provide :ms_pkg/Greeting_service "f58cc1930ee734da0da3606508759ab9")


