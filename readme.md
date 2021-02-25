# Robotics Intelligence Lab, Mobile Manipulator (RIL_MM)
 
## Overview
The UR5 with Robotiq Gripper85 and Husky mobile manipulator tutorial will show you how to operate a mobile manipulator using Gazebo, RViz, MoveIt



**Author**   
- **Sangbeom Park, [github]:https://github.com/Beom0611**  

### Before start the tutorial, please check your ROS version, this package for ROS Melodic version



## Guide

- For RIL_MMR
[UR5+Robotiq Gripper85+Husky Model](https://github.com/Beom0611/ril_mmr.git)  
```
$ cd ~/catkin_ws/src && git clone 
$ cd ~/catkin_ws && catkin_make
$ rosdep update
$ rosdep install --from-paths src --ignore-src -r -y
```


## Sample code for beginer 
- Spawning RIL_MM on Gazebo and Rviz 
```  
$ roslaunch ril_mmr_gazebo ril_mmr_empty_world.launch
```
- Moving RIL_MMR to the goal point  
``` 
$ cd ~/catkin_ws/src/ril_mmr_python   
$ chmod +x husky_point.py
$ rosrun ril_mmr_python husky_point.py 
```
- Contorlloing the mobile manipuatlor arm and gripper   
```
$ cd ~/catkin_ws/src/ril_mmr_python
$ chmod +x joint_test1.py
$ rosrun ril_mmr_python joint_test1.py 
```




## Description    

<img width="800" height="500" src="https://user-images.githubusercontent.com/78074831/109133146-08b8df80-7798-11eb-98a7-53325b398b83.png"  alt="Screenshot" title="Screenshot">
