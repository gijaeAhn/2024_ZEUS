# Install script for directory: /home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ms_pkg/msg" TYPE FILE FILES "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/msg/img_num.msg")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ms_pkg/srv" TYPE FILE FILES
    "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/FER_service.srv"
    "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/STT_service.srv"
    "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/TF_service.srv"
    "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/LLMC_service.srv"
    "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/srv/TTS_service.srv"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ms_pkg/cmake" TYPE FILE FILES "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/build/ms_pkg/catkin_generated/installspace/ms_pkg-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/devel/include/ms_pkg")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/devel/share/roseus/ros/ms_pkg")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/devel/share/common-lisp/ros/ms_pkg")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/devel/share/gennodejs/ros/ms_pkg")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/home/sjlab3090/anaconda3/bin/python3" -m compileall "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/devel/lib/python3/dist-packages/ms_pkg")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages" TYPE DIRECTORY FILES "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/devel/lib/python3/dist-packages/ms_pkg")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/build/ms_pkg/catkin_generated/installspace/ms_pkg.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ms_pkg/cmake" TYPE FILE FILES "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/build/ms_pkg/catkin_generated/installspace/ms_pkg-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ms_pkg/cmake" TYPE FILE FILES
    "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/build/ms_pkg/catkin_generated/installspace/ms_pkgConfig.cmake"
    "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/build/ms_pkg/catkin_generated/installspace/ms_pkgConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ms_pkg" TYPE FILE FILES "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/ms_pkg" TYPE PROGRAM FILES "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/build/ms_pkg/catkin_generated/installspace/FERServiceServer_script.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/ms_pkg" TYPE PROGRAM FILES "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/build/ms_pkg/catkin_generated/installspace/input_handler.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/ms_pkg" TYPE PROGRAM FILES "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/build/ms_pkg/catkin_generated/installspace/STTServiceServer_script.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/ms_pkg" TYPE PROGRAM FILES "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/build/ms_pkg/catkin_generated/installspace/TFServiceServer_script.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/ms_pkg" TYPE PROGRAM FILES "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/build/ms_pkg/catkin_generated/installspace/LLMCServiceServer_script.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/ms_pkg" TYPE PROGRAM FILES "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/build/ms_pkg/catkin_generated/installspace/TTSServiceServer_script.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/ms_pkg" TYPE PROGRAM FILES "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/build/ms_pkg/catkin_generated/installspace/test.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ms_pkg" TYPE FILE FILES "/home/sjlab3090/Desktop/2024_ZEUS/catkin_ws/src/ms_pkg/launch/UserInterface.launch")
endif()

