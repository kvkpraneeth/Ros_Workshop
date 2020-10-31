cmake_minimum_required(VERSION 3.0.2)
project(pkg_1)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  rospy
  std_msgs
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES pkg_1
#  CATKIN_DEPENDS geometry_msgs rospy std_msgs
#  DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS scripts/publisher.py scripts/subscriber.py scripts/pubandsub.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
