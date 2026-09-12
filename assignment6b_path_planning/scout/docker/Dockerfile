FROM osrf/ros:noetic-desktop-full

ARG DEBIAN_FRONTEND=noninteractive
#base
RUN apt-get update && apt-get install -y lsb-release curl wget ca-certificates git gnupg gdb

RUN apt-get update && apt-get install -y python3-pip python3-catkin-tools
RUN apt-get update && apt-get install -y ros-noetic-ros-control ros-noetic-ros-controllers
# RUN echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc   
RUN echo "export DISABLE_ROS1_EOL_WARNINGS=1" >> ~/.bashrc

WORKDIR /root

#cartographer
RUN apt-get update && apt-get install -y libceres-dev libgmock-dev lua5.2 liblua5.2-dev ninja-build stow
RUN git clone https://github.com/abseil/abseil-cpp.git && cd abseil-cpp && \
    git checkout 215105818dfde3174fe799600bb0f3cae233d0bf && \
    mkdir build && cd build && \
    cmake -G Ninja -DCMAKE_BUILD_TYPE=Release -DCMAKE_POSITION_INDEPENDENT_CODE=ON -DCMAKE_INSTALL_PREFIX=/usr/local/stow/absl .. && \
    ninja && ninja install && cd /usr/local/stow && stow absl  && rm -rf /root/abseil-cpp

# ros dependencies workspace
RUN mkdir -p /root/dependencies_catkin_ws/src
RUN git clone https://github.com/cartographer-project/cartographer.git --depth 1 -b master /root/dependencies_catkin_ws/src/cartographer
RUN git clone https://github.com/cartographer-project/cartographer_ros.git --depth 1 -b master /root/dependencies_catkin_ws/src/cartographer_ros
RUN git clone https://bitbucket.org/DataspeedInc/velodyne_simulator.git --depth 1 -b master /root/dependencies_catkin_ws/src/velodyne_simulator
RUN git clone https://github.com/agilexrobotics/ugv_gazebo_sim.git --depth 1 -b master /root/dependencies_catkin_ws/src/ugv_gazebo_sim
RUN git clone https://github.com/WenyuLWY/autonomous_exploration_development_environment.git --depth 1 -b main /root/dependencies_catkin_ws/src/autonomous_exploration_development_environment
# RUN git clone https://github.com/vectr-ucla/direct_lidar_odometry.git --depth 1 -b master /root/dependencies_catkin_ws/src/direct_lidar_odometry
# RUN git clone https://github.com/vectr-ucla/direct_lidar_inertial_odometry.git --depth 1 -b master /root/dependencies_catkin_ws/src/direct_lidar_inertial_odometry
RUN git clone https://github.com/WenyuLWY/direct_lidar_odometry.git --depth 1 -b master /root/dependencies_catkin_ws/src/direct_lidar_odometry
RUN git clone https://github.com/WenyuLWY/direct_lidar_inertial_odometry.git --depth 1 -b master /root/dependencies_catkin_ws/src/direct_lidar_inertial_odometry


#develop
# RUN apt-get update && apt-get install -y ros-noetic-hector-trajectory-server  ros-noetic-tf2-sensor-msgs ros-noetic-geographic-msgs

#DLO
# RUN apt-get update && apt-get install -y libomp-dev libpcl-dev libeigen3-dev 
#DSV planner
# RUN apt-get update && apt-get install -y ros-noetic-octomap-ros libgoogle-glog-dev libgflags-dev
#RTABMAP
# RUN apt-get update && apt-get install -y ros-noetic-rtabmap-ros ros-noetic-libpointmatcher ros-noetic-libg2o ros-noetic-gtsam
#2D nav
# RUN apt-get update && apt-get install -y ros-noetic-pointcloud-to-laserscan ros-noetic-point-cloud2-filters ros-noetic-navigation ros-noetic-teb-local-planner
# RUN apt-get update && apt-get install -y ros-noetic-explore-lite

# RUN git clone https://github.com/hku-mars/FAST_LIO.git --depth 1 /root/dependencies_catkin_ws/src/FAST_LIO && cd /root/dependencies_catkin_ws/src/FAST_LIO && \
    # git submodule update --init


RUN cd /root/dependencies_catkin_ws && \
    bash -c "source /opt/ros/noetic/setup.bash && catkin build" && \
    echo "source /root/dependencies_catkin_ws/devel/setup.bash" >> ~/.bashrc

RUN mkdir -p /root/catkin_ws/src && \
    cd /root/catkin_ws && \
    bash -c "source /opt/ros/noetic/setup.bash && catkin build" && \
    echo "source /root/catkin_ws/devel/setup.bash" >> ~/.bashrc

RUN apt-get update && apt-get install -y ros-noetic-hector-trajectory-server ros-noetic-hector-gazebo-plugins ros-noetic-pointcloud-to-laserscan ros-noetic-navigation
RUN apt-get update && apt-get install -y ros-noetic-rtabmap-ros ros-noetic-libpointmatcher ros-noetic-libg2o ros-noetic-gtsam
# RUN apt-get update && apt-get install -y ros-noetic-husky*
#autonomous_exploration_development_environment
RUN apt-get update && apt-get install -y libusb-dev

RUN echo "#!/bin/bash" > /root/start.sh && \
    echo "cd /root/catkin_ws" >> /root/start.sh && \
    echo "source /opt/ros/noetic/setup.bash" >> /root/start.sh && \
    echo "source ~/dependencies_catkin_ws/devel/setup.bash" >> /root/start.sh && \
    echo "catkin config --extend /root/dependencies_catkin_ws/devel" >> /root/start.sh && \
    echo "catkin config --cmake-args -DCMAKE_BUILD_TYPE=Release" >> /root/start.sh && \
    echo "CORES=\$(nproc)" >> /root/start.sh && \
    echo "JOBS=\$((CORES>1 ? CORES-1 : 1))" >> /root/start.sh && \
    echo "catkin build -j\$JOBS" >> /root/start.sh && \
    echo "source ~/catkin_ws/devel/setup.bash" >> /root/start.sh && \
    echo "exec \"\$@\"" >> /root/start.sh && \
    chmod +x /root/start.sh

    
# ENV XDG_RUNTIME_DIR=/tmp/runtime-root
# RUN mkdir -p /tmp/runtime-root && chmod 700 /tmp/runtime-root

ENTRYPOINT ["/root/start.sh"]

CMD ["/bin/bash"]
