;; Auto-generated. Do not edit!


(when (boundp 'ms_pkg::LLMC_service)
  (if (not (find-package "MS_PKG"))
    (make-package "MS_PKG"))
  (shadow 'LLMC_service (find-package "MS_PKG")))
(unless (find-package "MS_PKG::LLMC_SERVICE")
  (make-package "MS_PKG::LLMC_SERVICE"))
(unless (find-package "MS_PKG::LLMC_SERVICEREQUEST")
  (make-package "MS_PKG::LLMC_SERVICEREQUEST"))
(unless (find-package "MS_PKG::LLMC_SERVICERESPONSE")
  (make-package "MS_PKG::LLMC_SERVICERESPONSE"))

(in-package "ROS")





(defclass ms_pkg::LLMC_serviceRequest
  :super ros::object
  :slots (_user_text ))

(defmethod ms_pkg::LLMC_serviceRequest
  (:init
   (&key
    ((:user_text __user_text) "")
    )
   (send-super :init)
   (setq _user_text (string __user_text))
   self)
  (:user_text
   (&optional __user_text)
   (if __user_text (setq _user_text __user_text)) _user_text)
  (:serialization-length
   ()
   (+
    ;; string _user_text
    4 (length _user_text)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _user_text
       (write-long (length _user_text) s) (princ _user_text s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _user_text
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _user_text (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass ms_pkg::LLMC_serviceResponse
  :super ros::object
  :slots (_model_text ))

(defmethod ms_pkg::LLMC_serviceResponse
  (:init
   (&key
    ((:model_text __model_text) "")
    )
   (send-super :init)
   (setq _model_text (string __model_text))
   self)
  (:model_text
   (&optional __model_text)
   (if __model_text (setq _model_text __model_text)) _model_text)
  (:serialization-length
   ()
   (+
    ;; string _model_text
    4 (length _model_text)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _model_text
       (write-long (length _model_text) s) (princ _model_text s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _model_text
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _model_text (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass ms_pkg::LLMC_service
  :super ros::object
  :slots ())

(setf (get ms_pkg::LLMC_service :md5sum-) "c855b39a90951aa6be44ba4ed4e45902")
(setf (get ms_pkg::LLMC_service :datatype-) "ms_pkg/LLMC_service")
(setf (get ms_pkg::LLMC_service :request) ms_pkg::LLMC_serviceRequest)
(setf (get ms_pkg::LLMC_service :response) ms_pkg::LLMC_serviceResponse)

(defmethod ms_pkg::LLMC_serviceRequest
  (:response () (instance ms_pkg::LLMC_serviceResponse :init)))

(setf (get ms_pkg::LLMC_serviceRequest :md5sum-) "c855b39a90951aa6be44ba4ed4e45902")
(setf (get ms_pkg::LLMC_serviceRequest :datatype-) "ms_pkg/LLMC_serviceRequest")
(setf (get ms_pkg::LLMC_serviceRequest :definition-)
      "string user_text
---
string model_text
")

(setf (get ms_pkg::LLMC_serviceResponse :md5sum-) "c855b39a90951aa6be44ba4ed4e45902")
(setf (get ms_pkg::LLMC_serviceResponse :datatype-) "ms_pkg/LLMC_serviceResponse")
(setf (get ms_pkg::LLMC_serviceResponse :definition-)
      "string user_text
---
string model_text
")



(provide :ms_pkg/LLMC_service "c855b39a90951aa6be44ba4ed4e45902")


