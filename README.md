2024_ZEUS

Setup Guide

1. Install ROS Noetic (Ubuntu 20.04) & CUDA (Optional)
- Follow the official instructions to install ROS Noetic: http://wiki.ros.org/noetic/Installation/Ubuntu
- Install CUDA if needed for your project (Optional, depending on GPU-related tasks).

2. Install Anaconda
- Download and install Anaconda from Anaconda's official website: https://www.anaconda.com/products/distribution#download-section
- After installation, create and manage your Python environments as required.

3. Install Webots 2022b
- Download the Webots 2022b Debian package from Webots GitHub Releases: https://github.com/cyberbotics/webots/releases
- Install the package:
```bash
  sudo dpkg -i webots_2022b_Ubuntu-20.04_amd64.deb
```
- Install Webots dependencies:
```bash
  sudo apt --fix-broken install
```
4. Build Catkin Workspace (ROS Packages)
- To build your ROS packages, run the following command in the root of your project:
  bash ./build_catkin.sh

5. Install Pybind Library
- Install the Pybind library needed for Python-C++ bindings:
  bash ./install_pybind.sh

6. Webots Simulation
- Open Webots.
- Run the Webots client:
  python webot_client.py
- Run the position logger tool:
  python Tools/positionLogger.py
- Coordinate system: The robot's frame follows the FLU (Front, Left, Up) convention.
- Control Commands:
  - Press i: Set the robot to the initial position.
  - Press w, s: Move forward or backward along the x-axis.
  - Press a, d: Move left or right along the y-axis.
  - Press q, e: Move up or down along the z-axis.

7. Update Dependencies
- Keep track of your dependencies by updating the relevant .txt file. This file should contain a list of the required packages for the project.
