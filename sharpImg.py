#!/usr/bin/env python3
import rospy
import cv2
import time
from cv_bridge import CvBridge,CvBridgeError 
from sensor_msgs.msg import Image 
import numpy as np
class imgSharpener():
    def __init__(self):
        rospy.init_node("imgSharpener")
        self.img_sub = rospy.Subscriber("/custom_img_feed",Image,self.img_callback)
        self.img_pub = rospy.Publisher("/sharped_img",Image,queue_size =10)
        self.bridge = CvBridge()
    def img_callback(self,data):
        try:
            cv_img = self.bridge.imgmsg_to_cv2(data,"bgr8")
        except CvBridgeError as e:
            rospy.logerr(e)
            return
        kernel = np.array([[-1,-1,-1],
                           [-1,9,-1],
                           [-1,-1,-1]])
        sharped_img = cv2.filter2D(cv_img,-1,kernel)
        
        try:
            sharped_img_msg = self.bridge.cv2_to_imgmsg(sharped_img,'bgr8')
            self.img_pub.publish(sharped_img_msg)
        except CvBridgeError as e:
            rospy.logerr(e)
if __name__ == '__main__':
    try:
        img_sharpener = imgSharpener()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
            
