#!/usr/bin/env python2

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

"""Disclaimer: Inorder to understand this program, make sure you understand the publisher.py and
subscriber.py. Further, this program needs the understanding of Two message types which are Twist 
and Pose (Pose under turtlesim not geometry). Please read thier documentation. If you do not know classes
in python, GeeksforGeeks or similar websites would be advised to refer to."""


class turtlemove:

    """The Idea behind using Classes here is to have an easier way to access message data. 
    Message data is always local to the callback, but with classes, we have a way to access these
    local variables through self."""

    def __init__(self):
        """We store every object in the self container, this will ensure 
        that we can call methods from these objects."""
        self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=2)
        rospy.init_node('node_turtle_revolve')
        self.sub = rospy.Subscriber('/turtle1/pose', Pose, self.callback)
        self.linear_velocity = None

    def callback(self, msg):
        """Same as a Normal Subscriber"""
        rospy.loginfo(msg.linear_velocity)
        self.linear_velocity = msg.linear_velocity

    def move(self):
        """Please refer to the Twist documentation to understand the declerations and assignments"""
        r = rospy.Rate(10)
        vel_msg = Twist()
        [vel_msg.linear.x, vel_msg.linear.y, vel_msg.linear.z] = [0, 0, 0]
        [vel_msg.angular.x, vel_msg.angular.y, vel_msg.angular.z] = [0, 0, 0]
        vel_msg.linear.x = 2.0
        vel_msg.angular.z = 1.8
        while not rospy.is_shutdown():
            self.pub.publish(vel_msg)
            r.sleep()


def main():
    """Execution"""
    r = turtlemove()
    r.move()


if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        print "You have pressed Ctrl + C"
