cmake_minimum_required(VERSION 3.16.3)
project(zeus_controller)


find_package(catkin REQUIRED COMPONENTS roscpp rospy std_msgs sensor_msgs message_generation tf )

include_directories(
  ${catkin_INCLUDE_DIRS}
  # ${CPLUS_INCLUDE_PATH}
)

link_directories(/usr/local/webots/lib/controller)
set (LIBRARIES m ${CMAKE_SHARED_LIBRARY_PREFIX}Controller${CMAKE_SHARED_LIBRARY_SUFFIX} ${CMAKE_SHARED_LIBRARY_PREFIX}CppController${CMAKE_SHARED_LIBRARY_SUFFIX})
include_directories(/usr/local/webots/include/controller/cpp/)

add_executable(zeus_controller src/zeus_controller.cpp)

target_link_libraries(zeus_controller
	${catkin_LIBRARIES}
  ${LIBRARIES}
)


install(TARGETS zeus_controller
        RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
