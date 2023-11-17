#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Int16MultiArray
pubPol = rospy.Publisher('polynTopic', Int16MultiArray, queue_size=10, latch = True)

def polyNode(msg):
    numbersToPowers=Int16MultiArray()
    numbersToPowers.data=[msg.data[i]**(i+1) for i in range(3)]
    rospy.loginfo(numbersToPowers.data)
    pubPol.publish(numbersToPowers) 

rospy.init_node('polyNode')
rospy.Subscriber('reqTopic', Int16MultiArray, polyNode, queue_size=10)
rospy.spin()

	 
