#!/usr/bin/env python3
import rospy
from visualization_msgs.msg import Marker, MarkerArray

def visualize_color_cones():
    rospy.init_node('color_cone_visualizer')
    pub = rospy.Publisher('/cone_color', MarkerArray, queue_size=10)
    rate = rospy.Rate(1) #发消息的频率

    #stl模型的文件
    red_stl = "file:///home/yu/meshes/red.stl"
    blue_stl = "file:///home/yu/meshes/blue.stl"

    while not rospy.is_shutdown():
        marker_arr = MarkerArray()

        #红色锥桶
        red_marker = Marker()
        #坐标系 要与riz中的fixed frame一样
        red_marker.header.frame_id = 'map'
        red_marker.header.stamp = rospy.Time.now()
        #命名空间
        red_marker.ns = 'color_cone'
        red_marker.id = 0
        #模型类型
        red_marker.type = Marker.MESH_RESOURCE
        #标记
        red_marker.action = Marker.ADD
        #红色锥桶位置
        red_marker.pose.position.x = 2.0
        red_marker.pose.position.y = 0.0
        red_marker.pose.position.z = 0.0
        red_marker.pose.orientation.w = 1.0
        #大小
        red_marker.scale.x = 1.0
        red_marker.scale.y = 1.0
        red_marker.scale.z = 1.0
        #颜色
        red_marker.color.r = 1.0
        red_marker.color.g = 0.0
        red_marker.color.b = 0.0
        red_marker.color.a = 1.0 #不透明
        #模型路径
        red_marker.mesh_resource = red_stl
        red_marker.mesh_use_embedded_materials = True #原来的颜色

        #蓝色锥桶
        blue_marker = Marker()
        #坐标系 要与riz中的fixed frame一样
        blue_marker.header.frame_id = 'map'
        blue_marker.header.stamp = rospy.Time.now()
        #命名空间
        blue_marker.ns = 'color_cone'
        blue_marker.id = 1
        #模型类型
        blue_marker.type = Marker.MESH_RESOURCE
        #标记
        blue_marker.action = Marker.ADD
        #蓝色锥桶位置
        blue_marker.pose.position.x = 4.0
        blue_marker.pose.position.y = 0.0
        blue_marker.pose.position.z = 0.0
        blue_marker.pose.orientation.w = 1.0
        #大小
        blue_marker.scale.x = 1.0
        blue_marker.scale.y = 1.0
        blue_marker.scale.z = 1.0
        #颜色
        blue_marker.color.r = 0.0
        blue_marker.color.g = 0.0
        blue_marker.color.b = 1.0
        blue_marker.color.a = 1.0
        #模型路径
        blue_marker.mesh_resource = blue_stl
        blue_marker.mesh_use_embedded_materials = True #原来的颜色

        #添加到markerarray中
        marker_arr.markers.append(red_marker)
        marker_arr.markers.append(blue_marker)

        #发布
        pub.publish(marker_arr)
        rate.sleep()

if __name__ == '__main__':
    visualize_color_cones()
