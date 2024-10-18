#!/usr/bin/env bash

if [ ! -d "./lib/zeus_kinematics" ]; then
    echo "Please run this script from the project root directory."
    exit 1
fi

rm -fv ./lib/zeus_kinematics/transform* ./lib/zeus_kinematics/zeus_kinematics_solver*

cd ./pybind/kinematics || { echo "Directory ./pybind/kinematics not found!"; exit 1; }

cmake -S . -B build || { echo "CMake configuration failed!"; exit 1; }

cmake --build build || { echo "Build failed!"; exit 1; }

shared_objects=$(find build -name "*.so")

if [ -z "$shared_objects" ]; then
    echo "No .so files found!"
    exit 1
fi

echo "Found shared objects: $shared_objects"

for shared_object in $shared_objects; do
    mv "$shared_object" ../../lib/zeus_kinematics/ || { echo "Failed to move $shared_object!"; exit 1; }
done

rm -rf build
