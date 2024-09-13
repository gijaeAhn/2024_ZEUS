;; Auto-generated. Do not edit!


(when (boundp 'ms_pkg::STT_service)
  (if (not (find-package "MS_PKG"))
    (make-package "MS_PKG"))
  (shadow 'STT_service (find-package "MS_PKG")))
(unless (find-package "MS_PKG::STT_SERVICE")
  (make-package "MS_PKG::STT_SERVICE"))
(unless (find-package "MS_PKG::STT_SERVICEREQUEST")
  (make-package "MS_PKG::STT_SERVICEREQUEST"))
(unless (find-package "MS_PKG::STT_SERVICERESPONSE")
  (make-package "MS_PKG::STT_SERVICERESPONSE"))

(in-package "ROS")





(defclass ms_pkg::STT_serviceRequest
  :super ros::object
  :slots (_file_path ))

(defmethod ms_pkg::STT_serviceRequest
  (:init
   (&key
    ((:file_path __file_path) "")
    )
   (send-super :init)
   (setq _file_path (string __file_path))
   self)
  (:file_path
   (&optional __file_path)
   (if __file_path (setq _file_path __file_path)) _file_path)
  (:serialization-length
   ()
   (+
    ;; string _file_path
    4 (length _file_path)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _file_path
       (write-long (length _file_path) s) (princ _file_path s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _file_path
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _file_path (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass ms_pkg::STT_serviceResponse
  :super ros::object
  :slots (_result ))

(defmethod ms_pkg::STT_serviceResponse
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

(defclass ms_pkg::STT_service
  :super ros::object
  :slots ())

(setf (get ms_pkg::STT_service :md5sum-) "0b7e0c9192d9ca1d34c68e21095b2124")
(setf (get ms_pkg::STT_service :datatype-) "ms_pkg/STT_service")
(setf (get ms_pkg::STT_service :request) ms_pkg::STT_serviceRequest)
(setf (get ms_pkg::STT_service :response) ms_pkg::STT_serviceResponse)

(defmethod ms_pkg::STT_serviceRequest
  (:response () (instance ms_pkg::STT_serviceResponse :init)))

(setf (get ms_pkg::STT_serviceRequest :md5sum-) "0b7e0c9192d9ca1d34c68e21095b2124")
(setf (get ms_pkg::STT_serviceRequest :datatype-) "ms_pkg/STT_serviceRequest")
(setf (get ms_pkg::STT_serviceRequest :definition-)
      "string file_path
---
string result
")

(setf (get ms_pkg::STT_serviceResponse :md5sum-) "0b7e0c9192d9ca1d34c68e21095b2124")
(setf (get ms_pkg::STT_serviceResponse :datatype-) "ms_pkg/STT_serviceResponse")
(setf (get ms_pkg::STT_serviceResponse :definition-)
      "string file_path
---
string result
")



(provide :ms_pkg/STT_service "0b7e0c9192d9ca1d34c68e21095b2124")


