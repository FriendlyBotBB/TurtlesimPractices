#! /usr/bin/python

import rospy
import math
import random
from  geometry_msgs.msg import Twist
from turtlesim.msg import Pose

rate = 0
mover_t = Pose()
follower_t = Pose()
x_diff = 0
y_diff = 0
hipo = 0
div = 0

vel_turtle2 = Twist()

vel_turtle2.linear.x = 1.0
vel_turtle2.linear.y = 0.0
vel_turtle2.linear.z = 0.0
vel_turtle2.angular.x = 0.0
vel_turtle2.angular.y = 0.0
vel_turtle2.angular.z = 0.0


def follow_x_coor():
	global follower_t
	global mover_t
	global x_diff
	global y_diff
	global hipo
	global div
	
	x_diff = (mover_t.x) - (follower_t.x)
	y_diff = (mover_t.y) - (follower_t.y)
	hipo = math.sqrt((x_diff*x_diff) + (y_diff*y_diff))
			
	if x_diff > 0 :
		vel_turtle2.linear.x = 1.0
		div = y_diff/hipo
	elif(x_diff<0):
		vel_turtle2.linear.x = -1.0
		div = -y_diff/hipo
	elif(x_diff == 0):
		if(y_diff > 0):
			div = 1.33
			vel_turtle2.linear.x = 1.0
		elif(y_diff<0):
			div = 2.66
			vel_turtle2.linear.x = -1.0

	if follower_t.theta < div - 0.1:
    		vel_turtle2.angular.z = 1.0
	elif follower_t.theta > div + 0.1:
		vel_turtle2.angular.z = -1.0
	elif follower_t.theta < div + 0.1 and follower_t.theta > div - 0.1:
		vel_turtle2.angular.z = 0.0
	


def callback_mover_turtle1(data):
	global mover_t
	mover_t = data
    
def callback_follower_turtle2(data):
	global follower_t
	follower_t = data
	follow_x_coor()
    
def listener():
	global rate
	rospy.init_node('follower')
	rate = rospy.Rate(3.0)
	rospy.Subscriber("/turtle1/pose", Pose, callback_mover_turtle1)
  	rospy.Subscriber("/turtle2/pose", Pose, callback_follower_turtle2)
	publisher_turtle2 = rospy.Publisher('/turtle2/cmd_vel' , Twist ,queue_size = 1)  
   	while not rospy.is_shutdown():
  	     publisher_turtle2.publish(vel_turtle2) 	
	     rate.sleep()
	rospy.spin()

if __name__ == '__main__':
	listener()




