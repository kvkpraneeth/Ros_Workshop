#!/usr/bin/env python2

import rospy
from std_msgs.msg import String


def Say(x):
    pub = rospy.Publisher('Chatter', String, queue_size=10)
    rospy.init_node('Speaker', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():
        rospy.loginfo("Helu")
        pub.publish(x)
        rate.sleep()


if __name__ == "__main__":
    try:
        Say("Wazzzzzzup")
    except rospy.ROSInterruptException:
        pass

