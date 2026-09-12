FROM osrf/ros:humble-desktop-full

ARG DEBIAN_FRONTEND=noninteractive
#base
# RUN apt-get update && apt-get install -y lsb-release curl wget ca-certificates git gnupg gdb

# RUN apt-get update && apt-get install -y software-properties-common
# RUN add-apt-repository universe
# RUN curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
# RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | tee /etc/apt/sources.list.d/ros2.list > /dev/null
# RUN apt-get update && apt-get install -y ros-humble-desktop python3-argcomplete ros-dev-tools

RUN apt-get update && apt-get install -y python-is-python3 python3-pip

RUN apt-get update && apt-get install -y libusb-dev ros-humble-perception-pcl ros-humble-sensor-msgs-py ros-humble-tf-transformations ros-humble-joy ros-humble-rmw-cyclonedds-cpp ros-humble-rosidl-generator-dds-idl python3-colcon-common-extensions python-is-python3 
RUN pip install transforms3d pyyaml

RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc   

WORKDIR /root

RUN mkdir -p /root/ros2_ws/src && \
    cd ~/ros2_ws && \
    git clone https://github.com/jizhang-cmu/autonomy_stack_go2.git  src/autonomy_stack_go2 && \
    bash -c "source /opt/ros/humble/setup.bash && colcon build  --symlink-install --cmake-args -DCMAKE_BUILD_TYPE=Release" && \
    echo "source /root/ros2_ws/install/setup.bash" >> ~/.bashrc

RUN pip install gdown
RUN gdown 14nv2wHFyWCAncolp82zXD_W5zBtWWhwj --speed 0 

RUN echo "#!/bin/bash" > /root/start.sh && \
    echo "cd /root/ros2_ws" >> /root/start.sh && \
    echo "source /opt/ros/humble/setup.bash" >> /root/start.sh && \
    echo "colcon build  --symlink-install --cmake-args -DCMAKE_BUILD_TYPE=Release" >> /root/start.sh && \
    echo "source /root/ros2_ws/install/setup.bash" >> /root/start.sh && \
    echo "exec \"\$@\"" >> /root/start.sh && \
    chmod +x /root/start.sh

    
# ENV XDG_RUNTIME_DIR=/tmp/runtime-root
# RUN mkdir -p /tmp/runtime-root && chmod 700 /tmp/runtime-root

ENTRYPOINT ["/root/start.sh"]

CMD ["/bin/bash"]
