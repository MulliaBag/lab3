#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Int16MultiArray
from random import randint

rospy.init_node('reqNode')
pub = rospy.Publisher('reqTopic', Int16MultiArray, queue_size=10, latch = True)
rate = rospy.Rate(10)

def startReqNode():
    three_numbers = Int16MultiArray()
    three_numbers.data = [randint(0,10) for x in range(3)]
    pub.publish(three_numbers)
    rospy.loginfo(three_numbers.data)
    rate.sleep()
def InfSumNode(msg):
    rospy.loginfo(msg.data)  

rospy.Subscriber('sumTopic', Int16, InfSumNode, queue_size=10)
try:
    startReqNode()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')

