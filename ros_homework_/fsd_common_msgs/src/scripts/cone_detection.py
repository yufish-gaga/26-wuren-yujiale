#!/usr/bin/env python3
import rospy
from fsd_common_msgs.msg import ConeDetections, Cone 

red_count = 0 
blue_count = 0

def callback(msg):
    global red_count, blue_count
    for cone in msg.cone_detections:  # 遍历所有锥桶
        color = cone.color.data #data是防止乱码
        if color == 'b':          # 蓝锥桶
            blue_count += 1
        elif color == 'r':        # 红锥桶
            red_count += 1
    # 实时计数
    rospy.loginfo(f"红锥桶: {red_count} | 蓝锥桶: {blue_count}")

if __name__ == '__main__':
    rospy.init_node('cone_counter')
    rospy.Subscriber('/perception/lidar/cone_side', ConeDetections, callback)
    rospy.spin() 
