# install wsl and docker desktop on windows

download docker desktop

run 
wsl --install
in powershell

wsl --set-default Ubuntu

# workspace setup

in wsl

git clone https://github.com/WenyuLWY/CIVL4210_26fall.git

# assignment6b path planning


## agilex scout



git clone https://github.com/agilexrobotics/ugv_gazebo_sim.git

roslaunch scout_gazebo_sim scout_mini_playpen.launch

roslaunch robot_simulation run.launch
roslaunch robot_simulation robot_localization.launch
roslaunch robot_simulation robot_pathplanning.launch

git lfs track "assignment6b_path_planning/unitree/docker/unity_env_home_building_1.zip"
git lfs track "assignment6b_path_planning/unitree/docker/smith_hall_2nd_floor.db3"

git lfs untrack "assignment6b_path_planning/unitree/docker/unity_env_home_building_1.zip"
git lfs untrack "assignment6b_path_planning/unitree/docker/smith_hall_2nd_floor.db3"

## unitree go2

docker pull joriswenyuli/ros_go2_sim
bash run.sh