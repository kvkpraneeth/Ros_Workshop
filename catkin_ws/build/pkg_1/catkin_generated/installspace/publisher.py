#!/usr/bin/env python2

""" The Shebang which is denoted by '#!' in the above line is used to point to the python interpreter of the system."""

import rospy # Rospy is the python library that contains all the ROS related Functions and classes
from std_msgs.msg import String # Std_msgs is a message library that contains Message types which can be used

# Note that apart from the standard set of Messages that can be called from libs like these, you can make your custom ones


def Say(x):
    pub = rospy.Publisher('Chatter', String, queue_size=10) #pub is an object that is created that holds the rospy class Publisher. The Arguments given to it are ('Topic_To_Publish_To', Message_Type_To_Publish, QueueSize)
# The Queue Size parameter determines the amount of messages that wait in a queue before the subscriber can catch up.
    rospy.init_node('Speaker', anonymous=True) # This line  initializes the node with a name 'Speaker' and the other parameter gives the node a unique ID that is concatenated to it. This ensures there is no confusion due to Node names to the master
    rate = rospy.Rate(10)  # rate is an object that is created that holds the rospy class Rate. The Argument given to it determines the rate at which the publisher loops and does what it does.
    while not rospy.is_shutdown(): # The rospy.is_shutdown(), is a flag function that returns either 0 or 1. 0 -> No Shutdown Request (Ctrl + C) and 1-> if there is a Shutdown Request.
        rospy.loginfo("Helu") # This function has three functions, the use for it generally is to print the output to the screen much like the print function in python.
        pub.publish(x) # This is a method of the class Publisher. It helps publish 'x' which is a parameter to the function into the topic specified above in pub line.
        rate.sleep() # This is a method of the class sleep. It helps loop at the frequency specified in the rate line.


if __name__ == "__main__":
    try:
        Say("Wazzzzzzup") # We call the function with a parameter, which is going to be sent to the subscriber: "Wazzzzzzup"
    except rospy.ROSInterruptException: # This is an exception thrown when Ctrl + C(Inside the Terminal) is pressed to interrupt/stop the Node that is running. 
	print "You have pressed Ctrl + C" # Message that will print when this exception is thrown.



"""Official Documentation of the above content is at: Making a RosNode in Python: https://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29"""