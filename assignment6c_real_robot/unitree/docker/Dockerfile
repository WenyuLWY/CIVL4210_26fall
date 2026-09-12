FROM nvidia/opengl:1.0-glvnd-devel-ubuntu20.04

ARG DEBIAN_FRONTEND=noninteractive
#base
RUN apt-get update && apt-get install -y lsb-release curl wget ca-certificates git gnupg gdb

RUN apt-get update && apt-get install -y software-properties-common
RUN add-apt-repository universe
RUN curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | tee /etc/apt/sources.list.d/ros2.list > /dev/null
RUN apt-get update && apt-get install -y ros-foxy-desktop python3-argcomplete ros-dev-tools
RUN echo "source /opt/ros/foxy/setup.bash" >> ~/.bashrc   

WORKDIR /root

# RUN apt-get update && apt-get install -y libfmt-dev
# RUN git clone https://github.com/unitreerobotics/unitree_sdk2.git && cd unitree_sdk2 && \
#     mkdir build && cd build &&\
#     cmake .. && \
#     make install
    
# RUN cd unitree_sdk2/build && \   
#     cmake .. && \
#     make

RUN apt-get update && apt-get install -y iputils-ping iproute2

# RUN mkdir -p /root/catkin_ws/src && \
#     cd /root/catkin_ws && \
#     bash -c "source /opt/ros/noetic/setup.bash && catkin build" && \
#     echo "source /root/catkin_ws/devel/setup.bash" >> ~/.bashrc

# RUN echo "#!/bin/bash" > /root/start.sh && \
#     echo "cd /root/catkin_ws" >> /root/start.sh && \
#     echo "source /opt/ros/noetic/setup.bash" >> /root/start.sh && \
#     echo "catkin config --cmake-args -DCMAKE_BUILD_TYPE=Release" >> /root/start.sh && \
#     echo "CORES=\$(nproc)" >> /root/start.sh && \
#     echo "JOBS=\$((CORES>1 ? CORES-1 : 1))" >> /root/start.sh && \
#     echo "catkin build -j\$JOBS" >> /root/start.sh && \
#     echo "source ~/catkin_ws/devel/setup.bash" >> /root/start.sh && \
#     echo "exec \"\$@\"" >> /root/start.sh && \
#     chmod +x /root/start.sh

    
# ENV XDG_RUNTIME_DIR=/tmp/runtime-root
# RUN mkdir -p /tmp/runtime-root && chmod 700 /tmp/runtime-root

ENTRYPOINT ["/root/start.sh"]

CMD ["/bin/bash"]
