cmake_minimum_required(VERSION 3.16.3)

project(zeus_pybind)

find_package(pybind11 REQUIRED)


include_directories("/home/sj/.local/lib/python3.8/site-packages/pybind11/include")
include_directories(${CMAKE_SOURCE_DIR})

pybind11_add_module(transform Transform_pybind.cpp Transform.cpp )
pybind11_add_module(zeus_kinematics zeusKinematics_pybind.cpp zeusKinematics.cpp Transform.cpp)
