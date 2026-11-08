import rclpy

from geometry_msgs.msg import Twist

def publisher():
    rclpy.init()
    node = rclpy.create_node('colorful_turtle')

    pub1 = node.create_publisher(Twist, '/turtle1/cmd_vel', 10)

    twist1 = Twist()

    twist1.linear.x = 1.0
    twist1.angular.z = 0.5

    def timer_callback():
        pub1.publish(twist1)

    timer_period = 1.0
    timer=node.create_timer(timer_period, timer_callback)

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print('Node shutdown requested by user!')
    finally:
        if rclpy.ok():
            node.destroy_timer(timer)
            node.destroy_node()
            rclpy.shutdown()

if __name__=='__main__':
    publisher()

