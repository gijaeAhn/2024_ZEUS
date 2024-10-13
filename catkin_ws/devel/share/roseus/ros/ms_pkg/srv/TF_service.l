;; Auto-generated. Do not edit!


(when (boundp 'ms_pkg::TF_service)
  (if (not (find-package "MS_PKG"))
    (make-package "MS_PKG"))
  (shadow 'TF_service (find-package "MS_PKG")))
(unless (find-package "MS_PKG::TF_SERVICE")
  (make-package "MS_PKG::TF_SERVICE"))
(unless (find-package "MS_PKG::TF_SERVICEREQUEST")
  (make-package "MS_PKG::TF_SERVICEREQUEST"))
(unless (find-package "MS_PKG::TF_SERVICERESPONSE")
  (make-package "MS_PKG::TF_SERVICERESPONSE"))

(in-package "ROS")





(defclass ms_pkg::TF_serviceRequest
  :super ros::object
  :slots (_text ))

(defmethod ms_pkg::TF_serviceRequest
  (:init
   (&key
    ((:text __text) "")
    )
   (send-super :init)
   (setq _text (string __text))
   self)
  (:text
   (&optional __text)
   (if __text (setq _text __text)) _text)
  (:serialization-length
   ()
   (+
    ;; string _text
    4 (length _text)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _text
       (write-long (length _text) s) (princ _text s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _text
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _text (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass ms_pkg::TF_serviceResponse
  :super ros::object
  :slots (_result ))

(defmethod ms_pkg::TF_serviceResponse
  (:init
   (&key
    ((:result __result) 0)
    )
   (send-super :init)
   (setq _result (round __result))
   self)
  (:result
   (&optional __result)
   (if __result (setq _result __result)) _result)
  (:serialization-length
   ()
   (+
    ;; int8 _result
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int8 _result
       (write-byte _result s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int8 _result
     (setq _result (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _result 127) (setq _result (- _result 256)))
   ;;
   self)
  )

(defclass ms_pkg::TF_service
  :super ros::object
  :slots ())

(setf (get ms_pkg::TF_service :md5sum-) "05354734935e371f83dc4d09f1c13d77")
(setf (get ms_pkg::TF_service :datatype-) "ms_pkg/TF_service")
(setf (get ms_pkg::TF_service :request) ms_pkg::TF_serviceRequest)
(setf (get ms_pkg::TF_service :response) ms_pkg::TF_serviceResponse)

(defmethod ms_pkg::TF_serviceRequest
  (:response () (instance ms_pkg::TF_serviceResponse :init)))

(setf (get ms_pkg::TF_serviceRequest :md5sum-) "05354734935e371f83dc4d09f1c13d77")
(setf (get ms_pkg::TF_serviceRequest :datatype-) "ms_pkg/TF_serviceRequest")
(setf (get ms_pkg::TF_serviceRequest :definition-)
      "string text
---
int8 result
")

(setf (get ms_pkg::TF_serviceResponse :md5sum-) "05354734935e371f83dc4d09f1c13d77")
(setf (get ms_pkg::TF_serviceResponse :datatype-) "ms_pkg/TF_serviceResponse")
(setf (get ms_pkg::TF_serviceResponse :definition-)
      "string text
---
int8 result
")



(provide :ms_pkg/TF_service "05354734935e371f83dc4d09f1c13d77")


