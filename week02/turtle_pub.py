import rclpy

from geometry_msgs.msg import Twist


def publisher():
    rclpy.init()
    node = rclpy.create_node('turtle_pub')

    publisher =node.create_publisher(Twist, '/turtle1/cmd_vel', 10)
    vel_msg = Twist()

    vel_msg.linear.x = 1.0
    vel_msg.angular.z= 1.0

    publisher.publish(vel_msg)

    rclpy.spin(node)
    node.destroy_timer(timer)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    publisher()

