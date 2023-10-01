#!/usr/bin/env python3
import rospy
import cv2
import time
from cv_bridge import CvBridge,CvBridgeError 
from sensor_msgs.msg import Image 

FPS =30.0
dspFBS = 10.0
dspImg = True
def pubImage():
    rospy.init_node("image_pub")
    rate = rospy.Rate(10)
    cap = cv2.VideoCapture(0)
 
    img_pub = rospy.Publisher('/custom_img_feed',Image,queue_size = 10)
    bridge = CvBridge()
   
    while not rospy.is_shutdown():
        ret,frame = cap.read()
        if ret:
            try:
                ros_img = bridge.cv2_to_imgmsg(frame,encoding="bgr8")
                img_pub.publish(ros_img)
            except CvBridgeError as e:
                print(e)
            rate.sleep()
    cap.release()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    try:
        pubImage()
    except rospy.ROSInterruptException:
        pass
