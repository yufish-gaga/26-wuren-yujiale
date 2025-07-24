#!/usr/bin/env python3
import rospy
# 导入自定义消息类型
from turtle_msgs.msg import linear_vel  

if __name__ == '__main__':
    rospy.init_node('linear_pub')
    #话题名称 消息包类型 缓冲长度
    pub = rospy.Publisher('linear_vel', linear_vel , queue_size=10)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        vel_msg = linear_vel()
        vel_msg.linear_x = 0.5  # 设置线速度 x 分量
        vel_msg.linear_y = 0.3  # 设置线速度 y 分量
        pub.publish(vel_msg)
        rate.sleep()