# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "ms_pkg: 1 messages, 5 services")

set(MSG_I_FLAGS "-Ims_pkg:/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg;-Isensor_msgs:/opt/ros/noetic/share/sensor_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/noetic/share/geometry_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(ms_pkg_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/msg/img_num.msg" NAME_WE)
add_custom_target(_ms_pkg_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ms_pkg" "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/msg/img_num.msg" "sensor_msgs/Image:std_msgs/Header"
)

get_filename_component(_filename "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/FER_service.srv" NAME_WE)
add_custom_target(_ms_pkg_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ms_pkg" "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/FER_service.srv" "sensor_msgs/Image:std_msgs/Header"
)

get_filename_component(_filename "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/STT_service.srv" NAME_WE)
add_custom_target(_ms_pkg_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ms_pkg" "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/STT_service.srv" ""
)

get_filename_component(_filename "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/TF_service.srv" NAME_WE)
add_custom_target(_ms_pkg_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ms_pkg" "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/TF_service.srv" ""
)

get_filename_component(_filename "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/LLMC_service.srv" NAME_WE)
add_custom_target(_ms_pkg_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ms_pkg" "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/LLMC_service.srv" ""
)

get_filename_component(_filename "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/TTS_service.srv" NAME_WE)
add_custom_target(_ms_pkg_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ms_pkg" "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/TTS_service.srv" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(ms_pkg
  "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/msg/img_num.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/sensor_msgs/cmake/../msg/Image.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ms_pkg
)

### Generating Services
_generate_srv_cpp(ms_pkg
  "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/FER_service.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/sensor_msgs/cmake/../msg/Image.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ms_pkg
)
_generate_srv_cpp(ms_pkg
  "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/STT_service.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ms_pkg
)
_generate_srv_cpp(ms_pkg
  "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/TF_service.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ms_pkg
)
_generate_srv_cpp(ms_pkg
  "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/LLMC_service.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ms_pkg
)
_generate_srv_cpp(ms_pkg
  "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/TTS_service.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ms_pkg
)

### Generating Module File
_generate_module_cpp(ms_pkg
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ms_pkg
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(ms_pkg_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(ms_pkg_generate_messages ms_pkg_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/msg/img_num.msg" NAME_WE)
add_dependencies(ms_pkg_generate_messages_cpp _ms_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/FER_service.srv" NAME_WE)
add_dependencies(ms_pkg_generate_messages_cpp _ms_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/STT_service.srv" NAME_WE)
add_dependencies(ms_pkg_generate_messages_cpp _ms_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/TF_service.srv" NAME_WE)
add_dependencies(ms_pkg_generate_messages_cpp _ms_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/LLMC_service.srv" NAME_WE)
add_dependencies(ms_pkg_generate_messages_cpp _ms_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/TTS_service.srv" NAME_WE)
add_dependencies(ms_pkg_generate_messages_cpp _ms_pkg_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ms_pkg_gencpp)
add_dependencies(ms_pkg_gencpp ms_pkg_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ms_pkg_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(ms_pkg
  "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/msg/img_num.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/sensor_msgs/cmake/../msg/Image.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ms_pkg
)

### Generating Services
_generate_srv_eus(ms_pkg
  "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/FER_service.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/sensor_msgs/cmake/../msg/Image.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ms_pkg
)
_generate_srv_eus(ms_pkg
  "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/STT_service.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ms_pkg
)
_generate_srv_eus(ms_pkg
  "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/TF_service.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ms_pkg
)
_generate_srv_eus(ms_pkg
  "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/LLMC_service.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ms_pkg
)
_generate_srv_eus(ms_pkg
  "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/TTS_service.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ms_pkg
)

### Generating Module File
_generate_module_eus(ms_pkg
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ms_pkg
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(ms_pkg_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(ms_pkg_generate_messages ms_pkg_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/msg/img_num.msg" NAME_WE)
add_dependencies(ms_pkg_generate_messages_eus _ms_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/FER_service.srv" NAME_WE)
add_dependencies(ms_pkg_generate_messages_eus _ms_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/STT_service.srv" NAME_WE)
add_dependencies(ms_pkg_generate_messages_eus _ms_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/TF_service.srv" NAME_WE)
add_dependencies(ms_pkg_generate_messages_eus _ms_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/LLMC_service.srv" NAME_WE)
add_dependencies(ms_pkg_generate_messages_eus _ms_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/TTS_service.srv" NAME_WE)
add_dependencies(ms_pkg_generate_messages_eus _ms_pkg_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ms_pkg_geneus)
add_dependencies(ms_pkg_geneus ms_pkg_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ms_pkg_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(ms_pkg
  "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/msg/img_num.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/sensor_msgs/cmake/../msg/Image.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ms_pkg
)

### Generating Services
_generate_srv_lisp(ms_pkg
  "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/FER_service.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/sensor_msgs/cmake/../msg/Image.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ms_pkg
)
_generate_srv_lisp(ms_pkg
  "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/STT_service.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ms_pkg
)
_generate_srv_lisp(ms_pkg
  "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/TF_service.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ms_pkg
)
_generate_srv_lisp(ms_pkg
  "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/LLMC_service.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ms_pkg
)
_generate_srv_lisp(ms_pkg
  "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/TTS_service.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ms_pkg
)

### Generating Module File
_generate_module_lisp(ms_pkg
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ms_pkg
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(ms_pkg_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(ms_pkg_generate_messages ms_pkg_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/msg/img_num.msg" NAME_WE)
add_dependencies(ms_pkg_generate_messages_lisp _ms_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/FER_service.srv" NAME_WE)
add_dependencies(ms_pkg_generate_messages_lisp _ms_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/STT_service.srv" NAME_WE)
add_dependencies(ms_pkg_generate_messages_lisp _ms_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/TF_service.srv" NAME_WE)
add_dependencies(ms_pkg_generate_messages_lisp _ms_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/LLMC_service.srv" NAME_WE)
add_dependencies(ms_pkg_generate_messages_lisp _ms_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/TTS_service.srv" NAME_WE)
add_dependencies(ms_pkg_generate_messages_lisp _ms_pkg_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ms_pkg_genlisp)
add_dependencies(ms_pkg_genlisp ms_pkg_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ms_pkg_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(ms_pkg
  "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/msg/img_num.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/sensor_msgs/cmake/../msg/Image.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ms_pkg
)

### Generating Services
_generate_srv_nodejs(ms_pkg
  "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/FER_service.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/sensor_msgs/cmake/../msg/Image.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ms_pkg
)
_generate_srv_nodejs(ms_pkg
  "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/STT_service.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ms_pkg
)
_generate_srv_nodejs(ms_pkg
  "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/TF_service.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ms_pkg
)
_generate_srv_nodejs(ms_pkg
  "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/LLMC_service.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ms_pkg
)
_generate_srv_nodejs(ms_pkg
  "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/TTS_service.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ms_pkg
)

### Generating Module File
_generate_module_nodejs(ms_pkg
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ms_pkg
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(ms_pkg_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(ms_pkg_generate_messages ms_pkg_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/msg/img_num.msg" NAME_WE)
add_dependencies(ms_pkg_generate_messages_nodejs _ms_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/FER_service.srv" NAME_WE)
add_dependencies(ms_pkg_generate_messages_nodejs _ms_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/STT_service.srv" NAME_WE)
add_dependencies(ms_pkg_generate_messages_nodejs _ms_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/TF_service.srv" NAME_WE)
add_dependencies(ms_pkg_generate_messages_nodejs _ms_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/LLMC_service.srv" NAME_WE)
add_dependencies(ms_pkg_generate_messages_nodejs _ms_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/TTS_service.srv" NAME_WE)
add_dependencies(ms_pkg_generate_messages_nodejs _ms_pkg_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ms_pkg_gennodejs)
add_dependencies(ms_pkg_gennodejs ms_pkg_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ms_pkg_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(ms_pkg
  "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/msg/img_num.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/sensor_msgs/cmake/../msg/Image.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ms_pkg
)

### Generating Services
_generate_srv_py(ms_pkg
  "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/FER_service.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/sensor_msgs/cmake/../msg/Image.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ms_pkg
)
_generate_srv_py(ms_pkg
  "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/STT_service.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ms_pkg
)
_generate_srv_py(ms_pkg
  "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/TF_service.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ms_pkg
)
_generate_srv_py(ms_pkg
  "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/LLMC_service.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ms_pkg
)
_generate_srv_py(ms_pkg
  "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/TTS_service.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ms_pkg
)

### Generating Module File
_generate_module_py(ms_pkg
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ms_pkg
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(ms_pkg_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(ms_pkg_generate_messages ms_pkg_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/msg/img_num.msg" NAME_WE)
add_dependencies(ms_pkg_generate_messages_py _ms_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/FER_service.srv" NAME_WE)
add_dependencies(ms_pkg_generate_messages_py _ms_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/STT_service.srv" NAME_WE)
add_dependencies(ms_pkg_generate_messages_py _ms_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/TF_service.srv" NAME_WE)
add_dependencies(ms_pkg_generate_messages_py _ms_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/LLMC_service.srv" NAME_WE)
add_dependencies(ms_pkg_generate_messages_py _ms_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/TTS_service.srv" NAME_WE)
add_dependencies(ms_pkg_generate_messages_py _ms_pkg_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ms_pkg_genpy)
add_dependencies(ms_pkg_genpy ms_pkg_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ms_pkg_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ms_pkg)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ms_pkg
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(ms_pkg_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET sensor_msgs_generate_messages_cpp)
  add_dependencies(ms_pkg_generate_messages_cpp sensor_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ms_pkg)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ms_pkg
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(ms_pkg_generate_messages_eus std_msgs_generate_messages_eus)
endif()
if(TARGET sensor_msgs_generate_messages_eus)
  add_dependencies(ms_pkg_generate_messages_eus sensor_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ms_pkg)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ms_pkg
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(ms_pkg_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET sensor_msgs_generate_messages_lisp)
  add_dependencies(ms_pkg_generate_messages_lisp sensor_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ms_pkg)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ms_pkg
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(ms_pkg_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()
if(TARGET sensor_msgs_generate_messages_nodejs)
  add_dependencies(ms_pkg_generate_messages_nodejs sensor_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ms_pkg)
  install(CODE "execute_process(COMMAND \"/home/sjlab3090/anaconda3/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ms_pkg\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ms_pkg
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(ms_pkg_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET sensor_msgs_generate_messages_py)
  add_dependencies(ms_pkg_generate_messages_py sensor_msgs_generate_messages_py)
endif()
