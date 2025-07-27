#!/usr/bin/env python3
import rospy
import cv2
import numpy as np
from fsd_common_msgs.msg import ConeDetections, Cone
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

#内外参数矩阵 包括维度转换
intrinsic_matrix = np.array([532.795,0.0,632.15,
                            0.0,532.72,-3.428,
                            0.0, 0.0,1.0 ]).reshape(3,3)

extrinsic_matrix = np.array([3.5594209875121074e-03,-9.9987761481865733e-01,
                            -1.5234365979146680e-02,8.9277270417879417e-02,
                            1.9781062410225703e-03,1.5241472820252011e-02,
                            -9.9988188532544631e-01,9.1100499695349946e-01,
                            9.9999170877459420e-01,3.5288653732390984e-03,
                            2.0321149683686368e-03,1.9154049062915668e+00]).reshape(3,4)

bridge = CvBridge()

def callback(msg):
    #创建空白图像
    img = np.zeros((360,1280,3),  dtype=np.uint8) #height width channel

    for cone in msg.cone_detections:
        #获取锥桶坐标
        cone_3d = np.array([cone.position.x, cone.position.y, cone.position.z, 1]) 
        #坐标转换
        rusult = np.dot(extrinsic_matrix, cone_3d)
        cone_2d = np.dot(intrinsic_matrix, result)
        #归一化
        u = int(cone_2d[0]/cone_2d[2])
        v = int(cone_2d[1]/cone_2d[2])

        #按颜色划分
        if cone.color == 'r':
            color = (255,0,0)
        elif cone.color == 'b':
            color = (0,0,255)
        elif cone.color == 'y':
            color = (255,255,0)
        elif cone.color == 'o':
            color = (255,165,0)

        #绘制投影点
        cv2.circle(img, (u,v), 5, color, -1)

    #发布图像话题
    img_msg = bridge.cv2_to_imgmsg(img, 'Image') #转换数据类型
    projected_img_pub.publish(img_msg)

if __name__ == '__main__':
    rospy.init_node('cone_projection_node')
    #订阅锥桶检测话题
    rospy.Subscriber('/perception/lidar/cone_detections',
                     ConeDetections, callback)
    #发布投影话题
    projected_img_pub = rospy.Publisher('/projected_img', Image, queue_size=10)
    rospy.spin()


