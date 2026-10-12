import rclpy
## edit point 1 ##

def callback(msg):
    ## edit point 2 ##

def number_sub():
    rclpy.init()
    ## edit point 3 ##
    ## edit point 4 ##

    try:
        ## edit point 5 ##
    
    except KeyboardInterrupt:
        printf('Node shutdown requested by user!')

    finally:
        if rclpy.ok():
            node.destroy_node()
            rclpy.shutdown()

if __name__=='__main__':
    ## edit point 6 ##

