import rclpy
from rclpy.node import Node

from sensor_msgs.msg import PointCloud2
from nav_msgs.msg import Odometry

from tf2_ros import Buffer, TransformListener
from tf2_ros import TransformException
from tf2_sensor_msgs.tf2_sensor_msgs import do_transform_cloud



class TopicTransformer(Node):

    def __init__(self):
        super().__init__('topic_transformer')

        # TF
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(
            self.tf_buffer,
            self
        )

        # Point cloud subscriber
        self.sub = self.create_subscription(
            PointCloud2,
            '/velodyne_points',
            self.cloud_callback,
            10
        )

        # Transformed cloud publisher
        self.cloud_pub = self.create_publisher(
            PointCloud2,
            '/registered_scan',
            10
        )

        self.odom_pub = self.create_publisher(
            Odometry,
            '/state_estimation',
            10
        )

    def cloud_callback(self, msg):

        try:
            transform = self.tf_buffer.lookup_transform(
                'odom',
                msg.header.frame_id,
                rclpy.time.Time()
            )

        except TransformException as ex:
            self.get_logger().warn(
                f'Cannot transform {msg.header.frame_id} -> odom: {ex}'
            )
            return

        cloud_out = do_transform_cloud(
            msg,
            transform
        )

        cloud_out.header.frame_id = 'odom'

        odom_msg = Odometry()
        odom_msg.header.stamp = self.get_clock().now().to_msg() 
        odom_msg.header.frame_id = 'map'
        odom_msg.child_frame_id = "sensor"
        odom_msg.pose.pose.position.x = transform.transform.translation.x
        odom_msg.pose.pose.position.y = transform.transform.translation.y
        odom_msg.pose.pose.position.z = transform.transform.translation.z
        odom_msg.pose.pose.orientation = transform.transform.rotation
        odom_msg.twist.twist.linear.x = 0.0
        odom_msg.twist.twist.angular.z = 0.0


        self.odom_pub.publish(odom_msg)
        self.cloud_pub.publish(cloud_out)


def main(args=None):

    rclpy.init(args=args)

    node = TopicTransformer()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

