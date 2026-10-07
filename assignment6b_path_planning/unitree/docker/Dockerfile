FROM osrf/ros:humble-desktop-full

ARG DEBIAN_FRONTEND=noninteractive

WORKDIR /root
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc   
RUN git clone https://github.com/osrf/gazebo_models.git gazebo_models
RUN echo "export GAZEBO_MODEL_PATH=/root/gazebo_models:$GAZEBO_MODEL_PATH" >> ~/.bashrc
RUN apt-get update && apt-get install -y python-is-python3 python3-pip unzip xterm
RUN pip install gdown

#base
# RUN apt-get update && apt-get install -y lsb-release curl wget ca-certificates git gnupg gdb

# RUN apt-get update && apt-get install -y software-properties-common
# RUN add-apt-repository universe
# RUN curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
# RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | tee /etc/apt/sources.list.d/ros2.list > /dev/null
# RUN apt-get update && apt-get install -y ros-humble-desktop python3-argcomplete ros-dev-tools


#go2_nav_ros2
RUN apt-get update && apt-get install -y ros-humble-gazebo-ros \
                                        ros-humble-gazebo-ros-pkgs \
                                        ros-humble-gazebo-dev \
                                        ros-humble-gazebo-plugins \
                                        ros-humble-gazebo-ros2-control \
                                        ros-humble-ros2-control \
                                        ros-humble-ros2-controllers \
                                        ros-humble-robot-localization \
                                        ros-humble-navigation2 \
                                        ros-humble-nav2-bringup \
                                        ros-humble-xacro \
                                        ros-humble-velodyne \
                                        ros-humble-velodyne-gazebo-plugins \
                                        ros-humble-velodyne-description

# autonomy_stack_go2
RUN apt-get update && apt-get install -y libusb-dev ros-humble-perception-pcl ros-humble-sensor-msgs-py ros-humble-tf-transformations ros-humble-joy ros-humble-rmw-cyclonedds-cpp ros-humble-rosidl-generator-dds-idl python3-colcon-common-extensions python-is-python3 
RUN pip install transforms3d pyyaml

#for ros2 humble
# RUN pip install setuptools==58.2.0
# RUN apt-get update && apt-get install -y libpcap-dev

RUN apt-get update && apt-get install -y ros-humble-rqt* ros-humble-tf2-ros ros-humble-tf2-sensor-msgs ros-humble-pointcloud-to-laserscan

RUN mkdir -p /root/dependencies_ros2_ws/src && \
    cd ~/dependencies_ros2_ws && \
    git clone https://github.com/MOGI-ROS/mogi_trajectory_server.git src/mogi_trajectory_server && \
    bash -c "source /opt/ros/humble/setup.bash && colcon build" && \
    echo "source /root/dependencies_ros2_ws/install/setup.bash" >> ~/.bashrc



# RUN git clone https://github.com/WenyuLWY/autonomy_stack_go2.git /root/dependencies_ros2_ws/src/autonomy_stack_go2
# RUN git clone https://github.com/WenyuLWY/unitree-go2-ros2 /root/dependencies_ros2_ws/src/unitree-go2-ros2



RUN cd ~/dependencies_ros2_ws && \
    bash -c "source /opt/ros/humble/setup.bash && colcon build"

RUN mkdir -p /root/ros2_ws/src && \
    cd ~/ros2_ws && \
    bash -c "source /opt/ros/humble/setup.bash && colcon build --symlink-install" && \
    echo "source /root/ros2_ws/install/setup.bash" >> ~/.bashrc

RUN apt-get update && apt-get install -y ros-humble-realsense2-description ros-humble-gz-ros2-control  ros-humble-joint-state-publisher ros-humble-joint-state-publisher-gui

RUN echo "#!/bin/bash" > /root/start.sh && \
    echo "cd /root/ros2_ws" >> /root/start.sh && \
    echo "source /opt/ros/humble/setup.bash" >> /root/start.sh && \
    echo "source /root/dependencies_ros2_ws/install/setup.bash" >> /root/start.sh && \
    echo "colcon build --symlink-install" >> /root/start.sh && \
    echo "source /root/ros2_ws/install/setup.bash" >> /root/start.sh && \
    # echo "ros2 launch robot_simulation simulation.launch.py" >> /root/start.sh && \
    echo "exec \"\$@\"" >> /root/start.sh && \
    chmod +x /root/start.sh

    
# ENV XDG_RUNTIME_DIR=/tmp/runtime-root
# RUN mkdir -p /tmp/runtime-root && chmod 700 /tmp/runtime-root

ENTRYPOINT ["/root/start.sh"]

CMD ["/bin/bash"]
