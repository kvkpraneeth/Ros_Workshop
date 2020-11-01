#!/usr/bin/env python

""" The Shebang which is denoted by '#!' in the above line is used to point to the python interpreter of the system."""

import rospy  # Rospy is the python library that contains all the ROS related Functions and classes
# Std_msgs is a message library that contains Message types which can be used
from std_msgs.msg import String

# Note that apart from the standard set of Messages that can be called from libs like these, you can make your custom ones


def Say(x):
    # pub is an object that is created that holds the rospy class Publisher. The Arguments given to it are ('Topic_To_Publish_To', Message_Type_To_Publish, QueueSize)
    pub = rospy.Publisher('Chatter', String, queue_size=10)
# The Queue Size parameter determines the amount of messages that wait in a queue before the subscriber can catch up.
    # This line  initializes the node with a name 'Speaker' and the other parameter gives the node a unique ID that is concatenated to it. This ensures there is no confusion due to Node names to the master
    rospy.init_node('Speaker', anonymous=True)
    # rate is an object that is created that holds the rospy class Rate. The Argument given to it determines the rate at which the publisher loops and does what it does.
    rate = rospy.Rate(10)
    # The rospy.is_shutdown(), is a flag function that returns either 0 or 1. 0 -> No Shutdown Request (Ctrl + C) and 1-> if there is a Shutdown Request.
    while not rospy.is_shutdown():
        # This function has three functions, the use for it generally is to print the output to the screen much like the print function in python.
        rospy.loginfo("Helu")
        # This is a method of the class Publisher. It helps publish 'x' which is a parameter to the function into the topic specified above in pub line.
        pub.publish(x)
        # This is a method of the class sleep. It helps loop at the frequency specified in the rate line.
        rate.sleep()


if __name__ == "__main__":
    try:
        # We call the function with a parameter, which is going to be sent to the subscriber: "Wazzzzzzup"
        Say("Wazzzzzzup")
    # This is an exception thrown when Ctrl + C(Inside the Terminal) is pressed to interrupt/stop the Node that is running.
    except rospy.ROSInterruptException:
        # Message that will print when this exception is thrown.
        print "You have pressed Ctrl + C"


"""Official Documentation of the above content is at: Making a RosNode in Python: https://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29"""
