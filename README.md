# rgbd_align
[![ROS1 VERSION](https://img.shields.io/badge/ROS-Noetic-red)](http://wiki.ros.org/noetic)
&nbsp;
[![Ubuntu VERSION](https://img.shields.io/badge/Ubuntu-20.04-green)](https://ubuntu.com/)
&nbsp;
[![Author](https://img.shields.io/badge/Space-Burger-blue)](https://hzx.blue/)
&nbsp;

*This package is an improved version of my previous work [depth_yolo](https://https://github.com/0nhc/depth_yolo). There were several problems reported by some guys who used [depth_yolo](https://https://github.com/0nhc/depth_yolo):*
* *[depth_yolo](https://https://github.com/0nhc/depth_yolo) uses a Kinect V2 RGB-D camera, which is too old. Most people don't use such camera nowadays.*
* *[depth_yolo](https://https://github.com/0nhc/depth_yolo) uses [darknet_ros](https://github.com/leggedrobotics/darknet_ros) which is based on YOLOv3. It's 2024 now, and there are so many advanced object detection algorithms released.*

*I deveopled [depth_yolo](https://https://github.com/0nhc/depth_yolo) when I was a sophomore, originally intended to achieve a central point grasping demo. But frankly speaking central point grasping method is out of time (both in performace and novelty). If you are also trying to achive central point grasping, I'd recommend you to know more about advanced grasping algorithms such as [anygrasp(graspnet)](https://graspnet.net/anygrasp.html).*

## Roadmap
* Get rid of hardware dependency. Give a demo in Gazebo so that everyone can try it.
* Use advanced object detection method. I'm planning to try SAM(Segment Anything Model).

## Installation
TODO

## Examples

```sh
roslaunch rgbd_align demo.launch
```