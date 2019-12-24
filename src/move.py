#! /usr/bin/python

import rospy
import random
from  geometry_msgs.msg import Twist

rospy.init_node('bilge_node')

publisher_turtle1 = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 4)
rate = rospy.Rate(3.0) #3hz

vel_turtle1 = Twist()

vel_turtle1.linear.x =1.0
vel_turtle1.linear.y = 0.0
vel_turtle1.linear.z = 0.0
vel_turtle1.angular.x = 0.0
vel_turtle1.angular.y = 0.0
vel_turtle1.angular.z = 1.0


while not rospy.is_shutdown():
	velo = random.random() * 5
	angu = random.random() * 3
	if random.random() < 0.5:
		angu = - angu
	vel_turtle1.linear.x = velo
	vel_turtle1.angular.z = angu
	publisher_turtle1.publish(vel_turtle1) 
	rate.sleep()
