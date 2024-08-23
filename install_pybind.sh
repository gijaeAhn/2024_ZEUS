#!/usr/bin/env bash

cd pybind/kinematics || exit

cmake -S . -B build

cmake --build build

# Clean Build



shared_objects=$(find build -name "*.so")

echo $shared_objects

# Move all found .so files to the target directory
for shared_object in $shared_objects; 
do 
    mv "$shared_object" ../../lib/
done

# Clean up the build directory
rm -rf build