
(cl:in-package :asdf)

(defsystem "ms_pkg-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :sensor_msgs-msg
)
  :components ((:file "_package")
    (:file "FER_service" :depends-on ("_package_FER_service"))
    (:file "_package_FER_service" :depends-on ("_package"))
    (:file "LLMC_service" :depends-on ("_package_LLMC_service"))
    (:file "_package_LLMC_service" :depends-on ("_package"))
    (:file "STT_service" :depends-on ("_package_STT_service"))
    (:file "_package_STT_service" :depends-on ("_package"))
    (:file "TF_service" :depends-on ("_package_TF_service"))
    (:file "_package_TF_service" :depends-on ("_package"))
    (:file "TTS_service" :depends-on ("_package_TTS_service"))
    (:file "_package_TTS_service" :depends-on ("_package"))
  ))