from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch.substitutions import PathJoinSubstitution, Command
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node


def generate_launch_description():

    package_name = "simple_robot_description"

    # World file
    world_file = PathJoinSubstitution(
        [FindPackageShare(package_name), 'worlds', 'empty.world']
    )

    # Start Gazebo (Ignition/GZ)
    gazebo = ExecuteProcess(
        cmd=['gz', 'sim', world_file],
        output='screen'
    )

    # Robot description using xacro
    robot_description = Command([
        'xacro ',
        PathJoinSubstitution([
            FindPackageShare(package_name),
            'models',
            'arm_1dof',
            'arm_1dof.xacro'
        ])
    ])

    # Robot State Publisher
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': robot_description}],
        output='screen'
    )

    # Joint State Publisher
    joint_state_publisher = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        output='screen'
    )

    # Spawn robot in Gazebo
    spawn_robot = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-name', 'robot',
            '-topic', 'robot_description',
            '-x', '0',
            '-y', '0',
            '-z', '1'
        ],
        output='screen'
    )

    return LaunchDescription([
        gazebo,
        robot_state_publisher,
        joint_state_publisher,
        spawn_robot
    ])

