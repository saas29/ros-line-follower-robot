ROS2 Robot Simulation Project
 Project Description

This project demonstrates a basic robot simulation using ROS2, Gazebo, and RViz. The robot is modeled using URDF and simulated in a virtual environment to visualize its movement and structure.

The project helps beginners understand how to:

Create and organize a ROS2 package

Design a robot using URDF

Run robot simulations in Gazebo

Visualize the robot in RViz

Use Python nodes to control robot joints

🛠 Technologies Used

ROS2

Gazebo Simulator

RViz Visualization Tool

Python

URDF (Unified Robot Description Format)

📂 Project Structure
ros2_robot_simulation/
│
├── launch/
│   ├── gazebo.launch.py
│   └── rviz.launch.py
│
├── node/
│   └── joint_commander.py
│
├── urdf/
│   └── robot_model.urdf
│
├── worlds/
│   └── simulation_world.world
│
├── rviz/
│   └── robot_config.rviz
│
└── config/
    └── robot_parameters.yaml

    
⚙️ Installation

1️ Clone the repository
git clone https://github.com/your-username/ros2_robot_simulation.git

2️ Navigate to the workspace
cd ros2_robot_simulation

3️ Build the project
colcon build

4️ Source the workspace
source install/setup.bash

Running the Simulation

Launch Gazebo
ros2 launch simple_robot_description gazebo.launch.py

Launch RViz
ros2 launch simple_robot_description rviz.launch.py

 Features

Robot modeled using URDF

Simulation environment using Gazebo

Robot visualization using RViz

Python node to control robot joint movement

Organized ROS2 package structure

 Learning Outcomes

Through this project, you will learn:

ROS2 workspace and package structure

Robot modeling with URDF

Simulation using Gazebo

Robot visualization using RViz

Writing Python nodes in ROS2

 License

This project is licensed under the MIT License.

 Authors
 
Sashank Sai 
A vijay Kiran Reddy
Koluri Tulasi Ram
charan
B.Tech – AI & Data Science
Amrita Vishwa Vidyapeetham
