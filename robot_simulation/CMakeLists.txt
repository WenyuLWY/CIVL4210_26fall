cmake_minimum_required(VERSION 3.0.2)
project(robot_simulation)

set(CMAKE_WARN_DEPRECATED OFF CACHE BOOL "" FORCE)

find_package(catkin REQUIRED COMPONENTS
    roscpp
    tf2_ros
    std_msgs
    gazebo_msgs
    sensor_msgs
    nav_msgs
    )


find_package(Eigen3 REQUIRED)

catkin_package(
)


include_directories(
    ${catkin_INCLUDE_DIRS}
    ${EIGEN3_INCLUDE_DIR}
)

add_executable(localization_sim src/localization_sim.cpp)
target_link_libraries(localization_sim ${catkin_LIBRARIES})