import os
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch import LaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import DeclareLaunchArgument, LogInfo
from launch.substitutions import LaunchConfiguration

from launch.actions import GroupAction
from launch_ros.actions import PushRosNamespace


def generate_launch_description():

    ur_type = LaunchConfiguration('ur_type') 
    Right_arm_robot_ip = LaunchConfiguration('Right_arm_robot_ip') 
    Right_arm_controller_file = LaunchConfiguration('Right_arm_controller_file') 
    Right_arm_tf_prefix = LaunchConfiguration('Right_arm_tf_prefix') 
    Right_arm_script_command_port = LaunchConfiguration('Right_arm_script_command_port')
    Right_arm_trajectory_port = LaunchConfiguration('Right_arm_trajectory_port')
    Right_arm_reverse_port = LaunchConfiguration('Right_arm_reverse_port')
    Right_arm_script_sender_port = LaunchConfiguration('Right_arm_script_sender_port')

    Left_arm_robot_ip = LaunchConfiguration('Left_arm_robot_ip') 
    Left_arm_controller_file = LaunchConfiguration('Left_arm_controller_file') 
    Left_arm_tf_prefix = LaunchConfiguration('Left_arm_tf_prefix') 
    Left_arm_script_command_port = LaunchConfiguration('Left_arm_script_command_port')
    Left_arm_trajectory_port = LaunchConfiguration('Left_arm_trajectory_port')
    Left_arm_reverse_port = LaunchConfiguration('Left_arm_reverse_port')
    Left_arm_script_sender_port = LaunchConfiguration('Left_arm_script_sender_port')
    right_rviz_conf = LaunchConfiguration('right_rviz')
    left_rviz_conf = LaunchConfiguration('left_rviz')

    # # UR specific arguments
    ur_type_arg = DeclareLaunchArgument(
            "ur_type",
            default_value='ur3e',
            description="Type/series of used UR robot.",
            choices=["ur3", "ur3e", "ur5", "ur5e", "ur10", "ur10e", "ur16e", "ur20"],
    )
    Right_arm_robot_ip_arg = DeclareLaunchArgument(
            "Right_arm_robot_ip",
            default_value='192.168.10.25',
            description="IP address by which the robot can be reached.",
    )
    Right_arm_controller_file_arg = DeclareLaunchArgument(
            "Right_arm_controller_file",
            default_value="Right_arm_ur_controllers.yaml",
            description="YAML file with the controllers configuration.",
    )
    Right_arm_tf_prefix_arg = DeclareLaunchArgument(
            "Right_arm_tf_prefix",
            default_value="Right_arm_",
            description="tf_prefix of the joint names, useful for \
            multi-robot setup. If changed, also joint names in the controllers' configuration \
            have to be updated.",
    )

    Right_arm_script_command_port_arg =  DeclareLaunchArgument(
            "Right_arm_script_command_port",
            default_value="50010",
            description="Port that will be opened to forward script commands from the driver to the robot",
        )
    Right_arm_trajectory_port_arg = DeclareLaunchArgument(
            "Right_arm_trajectory_port",
            default_value="50009",
            description="Port that will be opened to forward script commands from the driver to the robot",
        )
    Right_arm_reverse_port_arg = DeclareLaunchArgument(
            "Right_arm_reverse_port",
            default_value="50006",
            description="Port that will be opened to forward script commands from the driver to the robot",
        )
    Right_arm_script_sender_port_arg = DeclareLaunchArgument(
            "Right_arm_script_sender_port",
            default_value="50007",
            description="Port that will be opened to forward script commands from the driver to the robot",
        )
    right_rviz_conf_arg = DeclareLaunchArgument(
            "right_rviz",
            default_value="right_view_robot.rviz",
            description="rviz_config",
        )

    Left_arm_robot_ip_arg = DeclareLaunchArgument(
            "Left_arm_robot_ip",
            default_value='192.168.10.23',
            description="IP address by which the robot can be reached.",
    )
    Left_arm_controller_file_arg = DeclareLaunchArgument(
            "Left_arm_controller_file",
            default_value="Left_arm_ur_controllers.yaml",
            description="YAML file with the controllers configuration.",
    )
    Left_arm_tf_prefix_arg = DeclareLaunchArgument(
            "Left_arm_tf_prefix",
            default_value="Left_arm_",
            description="tf_prefix of the joint names, useful for \
            multi-robot setup. If changed, also joint names in the controllers' configuration \
            have to be updated.",
    )
    Left_arm_script_command_port_arg =  DeclareLaunchArgument(
            "Left_arm_script_command_port",
            default_value="50005",
            description="Port that will be opened to forward script commands from the driver to the robot",
    )

    Left_arm_trajectory_port_arg = DeclareLaunchArgument(
            "Left_arm_trajectory_port",
            default_value="50004",
            description="Port that will be opened to forward script commands from the driver to the robot",
        )
    Left_arm_reverse_port_arg = DeclareLaunchArgument(
            "Left_arm_reverse_port",
            default_value="50001",
            description="Port that will be opened to forward script commands from the driver to the robot",
        )
    Left_arm_script_sender_port_arg = DeclareLaunchArgument(
            "Left_arm_script_sender_port",
            default_value="50002",
            description="Port that will be opened to forward script commands from the driver to the robot",
        )

    left_rviz_conf_arg = DeclareLaunchArgument(
            "left_rviz",
            default_value="left_view_robot.rviz",
            description="rviz_config",
        )
    

    ur_launch_dir = get_package_share_directory('ur_robot_driver')

    Right_arm = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(ur_launch_dir, 'launch', 'ur_control.launch.py')),
        launch_arguments={'ur_type': ur_type,
                          'robot_ip': Right_arm_robot_ip,
                          'controllers_file': Right_arm_controller_file,
                          'tf_prefix': Right_arm_tf_prefix,
                          'script_command_port': Right_arm_script_command_port,
                          'trajectory_port': Right_arm_trajectory_port,
                          'reverse_port': Right_arm_reverse_port,
                          'script_sender_port': Right_arm_script_sender_port,
                          'rviz_view_file': right_rviz_conf,
                          }.items())
    
    Right_arm_with_namespace = GroupAction(
     actions=[
         PushRosNamespace('Right_arm'),
         Right_arm
      ]
    )

    Left_arm = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(ur_launch_dir, 'launch', 'ur_control.launch.py')),
        launch_arguments={'ur_type': ur_type,
                          'robot_ip': Left_arm_robot_ip,
                          'controllers_file': Left_arm_controller_file,
                          'tf_prefix': Left_arm_tf_prefix,
                          'script_command_port': Left_arm_script_command_port,
                          'trajectory_port': Left_arm_trajectory_port,
                          'reverse_port': Left_arm_reverse_port,
                          'script_sender_port': Left_arm_script_sender_port,
                          'rviz_view_file': left_rviz_conf,
                          }.items())
    
    Left_arm_with_namespace = GroupAction(
     actions=[
         PushRosNamespace('Left_arm'),
         Left_arm
      ]
    )

    
    return LaunchDescription([
        ur_type_arg,
        Right_arm_robot_ip_arg,
        Right_arm_controller_file_arg,
        Right_arm_tf_prefix_arg,
        Right_arm_script_command_port_arg,
        Right_arm_trajectory_port_arg,
        Right_arm_reverse_port_arg,
        Right_arm_script_sender_port_arg,
        Left_arm_robot_ip_arg,
        Left_arm_controller_file_arg,
        Left_arm_tf_prefix_arg,
        Left_arm_script_command_port_arg,
        Left_arm_trajectory_port_arg,
        Left_arm_reverse_port_arg,
        Left_arm_script_sender_port_arg,

        right_rviz_conf_arg,
        left_rviz_conf_arg,
        
        Right_arm_with_namespace,
        Left_arm_with_namespace
    ])

