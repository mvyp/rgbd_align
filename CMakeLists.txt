cmake_minimum_required(VERSION 3.0.2)
project(rgbd_align)

find_package(catkin REQUIRED COMPONENTS
  rospy
  roscpp
)

catkin_package(
  INCLUDE_DIRS
  LIBRARIES
  CATKIN_DEPENDS 
  rospy
  roscpp
)
