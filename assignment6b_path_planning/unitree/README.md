git clone --recursive https://github.com/chvmp/champ -b ros2
git clone https://github.com/chvmp/champ_teleop -b ros2

git clone https://github.com/WenyuLWY/autonomy_stack_go2.git

git clone https://github.com/anujjain-dev/unitree-go2-ros2
ros2 launch go2_config gazebo_velodyne.launch.py rviz:=true

ros2 launch robot_simulation simulation.launch.py

ros2 run tf2_ros tf2_echo base_link map
ros2 run teleop_twist_keyboard teleop_twist_keyboard

map - velodyne

map - sensor = odom-base-footprint


