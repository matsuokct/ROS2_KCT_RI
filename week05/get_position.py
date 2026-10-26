import rclpy
#Question 1#

#Question 2#

def position_sub():
    rclpy.init()
    node = rclpy.create_node('turtle_position')
    #Question 3#

    try:
        rclpy.spin(node)
    
    except KeyboardInterrupt:
        print('Node shutdown requested by user!')

    finally:
        if rclpy.ok():
            node.destroy_node()
            rclpy.shutdown()

if __name__=='__main__':
    position_sub()