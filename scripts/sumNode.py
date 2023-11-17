#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Int16MultiArray
pubSum = rospy.Publisher('sumTopic', Int16, queue_size=10, latch = True)

def sumNode(msg):
	result=Int16()
	result.data=msg.data[0]+msg.data[1]+msg.data[2]
	pubSum.publish(result) 
	rospy.loginfo(result.data)

rospy.init_node('sumNode')
rospy.Subscriber('polynTopic', Int16MultiArray, sumNode, queue_size=10)
rospy.spin()
