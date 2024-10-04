;; Auto-generated. Do not edit!


(when (boundp 'ms_pkg::IC_service)
  (if (not (find-package "MS_PKG"))
    (make-package "MS_PKG"))
  (shadow 'IC_service (find-package "MS_PKG")))
(unless (find-package "MS_PKG::IC_SERVICE")
  (make-package "MS_PKG::IC_SERVICE"))
(unless (find-package "MS_PKG::IC_SERVICEREQUEST")
  (make-package "MS_PKG::IC_SERVICEREQUEST"))
(unless (find-package "MS_PKG::IC_SERVICERESPONSE")
  (make-package "MS_PKG::IC_SERVICERESPONSE"))

(in-package "ROS")





(defclass ms_pkg::IC_serviceRequest
  :super ros::object
  :slots ())

(defmethod ms_pkg::IC_serviceRequest
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

(defclass ms_pkg::IC_serviceResponse
  :super ros::object
  :slots (_result ))

(defmethod ms_pkg::IC_serviceResponse
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

(defclass ms_pkg::IC_service
  :super ros::object
  :slots ())

(setf (get ms_pkg::IC_service :md5sum-) "4414c67819626a1b8e0f043a9a0d6c9a")
(setf (get ms_pkg::IC_service :datatype-) "ms_pkg/IC_service")
(setf (get ms_pkg::IC_service :request) ms_pkg::IC_serviceRequest)
(setf (get ms_pkg::IC_service :response) ms_pkg::IC_serviceResponse)

(defmethod ms_pkg::IC_serviceRequest
  (:response () (instance ms_pkg::IC_serviceResponse :init)))

(setf (get ms_pkg::IC_serviceRequest :md5sum-) "4414c67819626a1b8e0f043a9a0d6c9a")
(setf (get ms_pkg::IC_serviceRequest :datatype-) "ms_pkg/IC_serviceRequest")
(setf (get ms_pkg::IC_serviceRequest :definition-)
      "
---
int8 result
")

(setf (get ms_pkg::IC_serviceResponse :md5sum-) "4414c67819626a1b8e0f043a9a0d6c9a")
(setf (get ms_pkg::IC_serviceResponse :datatype-) "ms_pkg/IC_serviceResponse")
(setf (get ms_pkg::IC_serviceResponse :definition-)
      "
---
int8 result
")



(provide :ms_pkg/IC_service "4414c67819626a1b8e0f043a9a0d6c9a")


