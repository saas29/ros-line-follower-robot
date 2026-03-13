Project Overview

This project demonstrates a simple robot simulation using ROS2, Gazebo, and RViz.
The robot is modeled using URDF/Xacro and can be visualized and controlled inside the ROS2 environment.

The simulation includes:

A 1-DOF robotic arm

A Gazebo simulation world

A track model

Visualization using RViz

A joint commander node for controlling the robot joint

This project helps beginners understand:

ROS2 package structure

URDF/Xacro robot modeling

Launch files in ROS2

Gazebo simulation integration

🛠 Technologies Used

ROS2

Gazebo

RViz

Python

URDF / Xacro

📂 Project Structure
ros2_project
│
├── launch
│   ├── gazebo.launch.py
│   └── rviz.launch.py
│
├── models
│   ├── arm_1dof
│   └── track
│
├── worlds
│   └── empty.world
│
├── config
│   └── arm_1dof.yaml
│
├── rviz
│   └── arm.rviz
│
└── simple_robot_description
    └── joint_commander.py
