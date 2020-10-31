# Ros_Workshop

This Repo contains all the codes present with comments on every single Code.



How to run this repo:

1) Clone the Repo to your local computer
2) If there are build and devel files in catkin_ws delete those files
3) Run 'catkin_make' when you are in the catkin_ws directory in your folder
4) use the command 'cd' plainly in the terminal to go to the home directory
5) use the command 'nano .bashrc' to see a file filled with greek
6) Scroll to the very bottom and add the lines 'source /whereyousavedtherosworkshop/Ros_Workshop/catkin_ws/devel/setup.bash'
7) then exit the terminal and restart, if everything goes well, the command 'roscd' will take you to devel folder in this workspace inside the terminal.

How to use this repo?

1) Make sure you understand how workspaces work and how to build one
if not refer to: Recording or [this](#https://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment)

2) Make sure you understand what is a package and its default creations: CMakeLists.txt and Package.xml
if not refer to: Recording or [this](#https://wiki.ros.org/ROS/Tutorials/CreatingPackage) and [this](#https://wiki.ros.org/ROS/Tutorials/BuildingPackages)

3) if you're done with the above two, and you know how nodes come to where they are in this file, then you can clearly understand what is going on with the comments in publisher.py and subscriber.py 
if not refer to: Recording or [this](#https://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29)

4) if you're done with those nodes, analyse them by using rqt tools and other message types
for help refer to: [Rqt_Tools](#https://wiki.ros.org/ROS/Tutorials/UnderstandingNodes) and [msg_documentation](#http://docs.ros.org/en/melodic/api/std_msgs/html/index-msg.html)

disclaimer: The above msg_documentation is only for std_msgs, please google for the rest.

5) If you're done with all that, and are familiar with how nodes are run, commandline tools and python classes, then read
the pubandsub.py node. If not please go through python oops online and the above steps.


All hail the Original Documentation:

https://wiki.ros.org/
