#!/usr/bin/env bash

# Ensure the script is being run from the project root
if [ ! -d "./lib/zeus_kinematics" ]; then
    echo "Please run this script from the project root directory."
    exit 1
fi

# Remove all files that start with 'transform' or 'zeus_kinematics_solver' in the target directory
rm -fv ./lib/zeus_kinematics/transform* ./lib/zeus_kinematics/zeus_kinematics_solver*

# Change to the 'pybind/kinematics' directory or exit if it fails
cd ./pybind/kinematics || { echo "Directory ./pybind/kinematics not found!"; exit 1; }

# Run CMake to configure and build the project
cmake -S . -B build || { echo "CMake configuration failed!"; exit 1; }

cmake --build build || { echo "Build failed!"; exit 1; }

# Find all .so (shared object) files in the build directory
shared_objects=$(find build -name "*.so")

# Check if .so files were found, and if not, print a message
if [ -z "$shared_objects" ]; then
    echo "No .so files found!"
    exit 1
fi

# Print the list of shared objects found
echo "Found shared objects: $shared_objects"

# Move all found .so files to the target directory
for shared_object in $shared_objects; do
    mv "$shared_object" ../../lib/zeus_kinematics/ || { echo "Failed to move $shared_object!"; exit 1; }
done

# Clean up the build directory
rm -rf build
