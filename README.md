# ROS2 Robot Simulation

A hands-on project that builds a basic robot simulation using ROS2, Gazebo, and RViz. The robot is described in URDF and dropped into a virtual world where you can watch it move and tweak its joints in real time.

I built this while learning ROS2 — it's not production code, but it covers enough ground to be useful if you're figuring out how ROS2 packages fit together or how to get a robot model running in simulation.

---

## What's Inside

- A URDF robot model
- Gazebo world file for simulation
- RViz config for visualization
- A Python node that sends joint commands
- Launch files for both Gazebo and RViz

```
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
```

---

## Technologies

- ROS2
- Gazebo
- RViz
- Python
- URDF

---

## Setup

Clone the repo:
```bash
git clone https://github.com/your-username/ros2_robot_simulation.git
cd ros2_robot_simulation
```

Build and source:
```bash
colcon build
source install/setup.bash
```

---

## Running It

Start the Gazebo simulation:
```bash
ros2 launch simple_robot_description gazebo.launch.py
```

Open RViz in a separate terminal:
```bash
ros2 launch simple_robot_description rviz.launch.py
```

---

## What You'll Learn

- How ROS2 workspaces and packages are structured
- Writing robot models in URDF
- Setting up launch files
- Running Gazebo simulations
- Writing basic ROS2 Python nodes

Good starting point if you've done the ROS2 tutorials and want something concrete to dig into.

---

## Author

**Sashank** 
**A vijay Kiran Reddy**
**Koluri Tulasi Ram**
**charan**
B.Tech – AI & Data Science  
Amrita Vishwa Vidyapeetham

---

## License

MIT
