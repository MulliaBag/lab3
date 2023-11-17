#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16

rospy.init_node('polyNode')
pub = rospy.Publisher('polyTopic', Int16, queue_size=10
rate = rospy.Rate(10)

def start_polyNode():
	 
