#!/usr/bin/env python

import rospy
from std_msgs.msg import String
 """The Above lines have been Explained in publisher.py"""

def callback(msg):
	"""This is a very Special Function. it's parameter is a container, it contains the message data that is recieved"""
    rospy.loginfo(msg.data)
    """rospy.loginfo analogous to print function in Python"""
    """Why are we doing msg.data? There are certain keywords that are associated with the type of data a message has.
    For instance, In this case, we are using String and the string documentation shows that the data type is string
    and the keyword for accessing said string is 'data'."""



def listener():
    rospy.init_node('listener', anonymous=True)
    """The above line has been explained in publisher.py"""
    rospy.Subscriber("Chatter", String, callback)
    """This initializes a Subscriber, it's syntax: ('Topic_To_Subscribe_to', expected_message_type, callback_function)"""
    """This function takes the messages and inserts it into callback function the callback further uses the message"""
    rospy.spin()
    """Everytime a subscriber recieves a message it stops running, but spin restarts, which makes a loop"""


if __name__ == '__main__':
    listener()
