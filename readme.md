# Robotics Intelligence Lab, Mobile Manipulation Robot (RIL_MMR)
 
## Overview
The UR5 with Robotiq Gripper85 and Husky mobile manipulation robot tutorial will show you how to operate a mobile manipulation robot using Gazebo, RViz, MoveIt


**Author**   
- **Sangbeom Park, [github]:https://github.com/Beom0611**  

### Before start the tutorial, please check your ROS version, this pakage for ROS Melodic version


## Guide

- For RIL_MMR
[UR5+Robotiq Gripper85+Husky Model](https://github.com/Beom0611/ril_mmr.git)  
```
$ cd ~/catkin_ws/src && git clone
$ cd ~/catkin_ws/src && catkin_make
$ sudo rosdep init
$ rosdep update
$ rosdep install --from-paths src --ignore-src -r -y
```

## Sample code for beginer 
- Spawning RIL_MMR on Gazebo and Rviz   
$ roslaunch ril_mmr_gazebo ril_mmr_empty_world.launch

- Moving RIL_MMR to the goal point  
$ rosrun ril_mmr_python husky_point.py 

- Contorlloing the RIL_MMR' arm and gripper    
$ rosrun ril_mmr_python joint_test1.py 



## Description    

<img width="800" height="500" src="https://user-images.githubusercontent.com/78074831/109133146-08b8df80-7798-11eb-98a7-53325b398b83.png"  alt="Screenshot" title="Screenshot">
