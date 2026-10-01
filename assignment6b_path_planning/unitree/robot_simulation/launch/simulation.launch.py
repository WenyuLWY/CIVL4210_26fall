import os

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource,AnyLaunchDescriptionSource

from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    gazebo_velodyne = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('go2_config'),
                'launch',
                'gazebo_velodyne.launch.py'
            )
        )
    )

    topic_transform_node = Node(
        package='robot_simulation',
        executable='topic_transform',
        name='topic_transform',
        output='screen'
    )

    static_transform_node = Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='map_to_odom_tf',
            output='screen',
            arguments=['--x', '0',
                        '--y', '0',
                        '--z', '0',
                        '--yaw', '0',
                        '--pitch', '0',
                        '--roll', '0',
                        '--frame-id', 'map',
                        '--child-frame-id', 'odom',
                    ],
        )


    autonomy_stack_go2 = IncludeLaunchDescription(
        AnyLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('robot_simulation'),
                'launch',
                'system_simulation.launch.xml'
            )
        )
    )

    return LaunchDescription([
        gazebo_velodyne,
        topic_transform_node,
        static_transform_node,
        autonomy_stack_go2
    ])