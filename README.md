# install wsl

download docker desktop

run 
wsl --install
in powershell


# assignment6b path planning

git clone https://github.com/WenyuLWY/CIVL4210_26fall.git

git clone https://github.com/agilexrobotics/ugv_gazebo_sim.git

roslaunch scout_gazebo_sim scout_mini_playpen.launch

roslaunch robot_simulation run.launch
roslaunch robot_simulation robot_localization.launch
roslaunch robot_simulation robot_pathplanning.launch