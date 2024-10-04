;; Auto-generated. Do not edit!


(when (boundp 'ms_pkg::FER_service)
  (if (not (find-package "MS_PKG"))
    (make-package "MS_PKG"))
  (shadow 'FER_service (find-package "MS_PKG")))
(unless (find-package "MS_PKG::FER_SERVICE")
  (make-package "MS_PKG::FER_SERVICE"))
(unless (find-package "MS_PKG::FER_SERVICEREQUEST")
  (make-package "MS_PKG::FER_SERVICEREQUEST"))
(unless (find-package "MS_PKG::FER_SERVICERESPONSE")
  (make-package "MS_PKG::FER_SERVICERESPONSE"))

(in-package "ROS")





(defclass ms_pkg::FER_serviceRequest
  :super ros::object
  :slots ())

(defmethod ms_pkg::FER_serviceRequest
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass ms_pkg::FER_serviceResponse
  :super ros::object
  :slots (_result ))

(defmethod ms_pkg::FER_serviceResponse
  (:init
   (&key
    ((:result __result) 0.0)
    )
   (send-super :init)
   (setq _result (float __result))
   self)
  (:result
   (&optional __result)
   (if __result (setq _result __result)) _result)
  (:serialization-length
   ()
   (+
    ;; float32 _result
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _result
       (sys::poke _result (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _result
     (setq _result (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass ms_pkg::FER_service
  :super ros::object
  :slots ())

(setf (get ms_pkg::FER_service :md5sum-) "db954e5de3aba73b237d07575e5cac28")
(setf (get ms_pkg::FER_service :datatype-) "ms_pkg/FER_service")
(setf (get ms_pkg::FER_service :request) ms_pkg::FER_serviceRequest)
(setf (get ms_pkg::FER_service :response) ms_pkg::FER_serviceResponse)

(defmethod ms_pkg::FER_serviceRequest
  (:response () (instance ms_pkg::FER_serviceResponse :init)))

(setf (get ms_pkg::FER_serviceRequest :md5sum-) "db954e5de3aba73b237d07575e5cac28")
(setf (get ms_pkg::FER_serviceRequest :datatype-) "ms_pkg/FER_serviceRequest")
(setf (get ms_pkg::FER_serviceRequest :definition-)
      "
---
float32 result
")

(setf (get ms_pkg::FER_serviceResponse :md5sum-) "db954e5de3aba73b237d07575e5cac28")
(setf (get ms_pkg::FER_serviceResponse :datatype-) "ms_pkg/FER_serviceResponse")
(setf (get ms_pkg::FER_serviceResponse :definition-)
      "
---
float32 result
")



(provide :ms_pkg/FER_service "db954e5de3aba73b237d07575e5cac28")


