import rclpy

from geometry_msgs.msg import Twist

def callback(msg):
    print('linear.x=', msg.linear.x)
    print('linear.x=', msg.linear.y)
    print('linear.x=', msg.linear.z)
    print('angular.x=', msg.angular.x)
    print('angular.x=', msg.angular.y)
    print('angular.x=', msg.angular.z)



def subscriber():
    rclpy.init()
    node=rclpy.create_node('turtle_sub')
    subscription = node.create_subscription(Twist, '/turtle1/cmd_vel', callback, 10)

    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    subscriber()
    