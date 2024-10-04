
(cl:in-package :asdf)

(defsystem "ms_pkg-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :sensor_msgs-msg
)
  :components ((:file "_package")
    (:file "img_num" :depends-on ("_package_img_num"))
    (:file "_package_img_num" :depends-on ("_package"))
  ))