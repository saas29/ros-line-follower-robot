import rclpy
from rclpy.node import Node
import cv2
import numpy as np
from scipy.ndimage import center_of_mass 
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class LineFollower(Node):
    def __init__(self):
        super().__init__('line_follower')
        self.bridge = CvBridge()
        
        # Subscribe to the topic in your XACRO
        self.sub = self.create_subscription(Image, '/camera/image_raw', self.image_callback, 10)
        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)
        
        self.img_grayscale = None
        self.timer = self.create_timer(0.05, self.control_loop) # 20Hz update rate
        
        # --- TUNING PARAMETERS ---
        self.linear_speed = 0.1      # Steady speed for sharp turns
        self.kp = 0.007              # How hard the robot turns. Increase if it misses curves.
        # -------------------------

    def image_callback(self, msg):
        self.img_grayscale = self.bridge.imgmsg_to_cv2(msg, desired_encoding='mono8')

    def control_loop(self):
        if self.img_grayscale is None:
            return

        try:
            # AUTO-THRESHOLD: Finds the black line even if lighting changes
            _, img_bin = cv2.threshold(self.img_grayscale, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
            
            # ROI: Look at a horizontal strip in the bottom-middle of the screen
            h, w = img_bin.shape
            roi = img_bin[int(h*0.6):int(h*0.9), :]
            
            # Show the binary view to YOU so you can debug
            cv2.imshow("Robot_Brain_View", img_bin)
            cv2.waitKey(1)

            if np.sum(roi) > 0:
                # Get center of mass of the white pixels (the line)
                coords = center_of_mass(roi)
                cx = coords[1]
                
                # Calculate Error (center of 800px image is 400)
                error = cx - (w / 2)
                
                msg = Twist()
                msg.linear.x = self.linear_speed
                # Angular velocity is proportional to the error
                msg.angular.z = -float(error) * self.kp
                self.pub.publish(msg)
                
                # Draw a red dot on the tracking point for the debug window
                display = cv2.cvtColor(self.img_grayscale, cv2.COLOR_GRAY2BGR)
                cv2.circle(display, (int(cx), int(h*0.75)), 15, (0, 0, 255), -1)
                cv2.imshow("Tracking_Debug", display)
            else:
                # If no line seen, stop and spin to find it
                msg = Twist()
                msg.linear.x = 0.0
                msg.angular.z = 0.3
                self.pub.publish(msg)
                self.get_logger().info("Searching for track...")

        except Exception as e:
            self.get_logger().error(f"Error: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = LineFollower()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    cv2.destroyAllWindows()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
