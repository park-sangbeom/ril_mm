#!/usr/bin/env python

import sys
import rospy
import moveit_commander
import math 

rospy.init_node('ril_mmr', anonymous=True)
moveit_commander.roscpp_initialize(sys.argv)

robot=moveit_commander.RobotCommander()
scene=moveit_commander.PlanningSceneInterface()

group_name=robot.get_group_names()
group_name

robot.get_current_state()

def move_joints(move_group, goal):
    move_group.go(goal, wait=True)
    move_group.stop()


move_group=moveit_commander.MoveGroupCommander(group_name[1])
print(group_name[1])
print(move_group)
move_group.set_named_target('open')
plan=move_group.plan()
move_group.execute(plan, wait=True)

def get_joint_state(move_group):
    joint_state = move_group.get_current_joint_values()
    print "-->current joint state as follows (rad): "
    print joint_state
    print "-->current joint state as follows (degree): "
    print [joint*180./math.pi for joint in joint_state]



move_group=moveit_commander.MoveGroupCommander(group_name[0])
get_joint_state(move_group)

goal1 =[n*math.pi/180. for n in [-30.,-20., 50., -90., 90., 0.]]
#move_joints(move_group, goal1)

goal2 =[n*math.pi/180. for n in [-30.,-100., 50., -70., 90., 0.]]
#move_joints(move_group, goal2)

goal3 =[n*math.pi/180. for n in [30.,-100., 60., -30., 20., 0.]]
#move_joints(move_group, goal3)

goal4 =[n*math.pi/180. for n in [-30.,-100., 60., -30., 20., 0.]]
#move_joints(move_group, goal4)

finish =[n*math.pi/180. for n in [0.,0., 0., 0., 0., 0.]]


for i in range(1):
    
    #goal1 execute
    move_joints(move_group, goal1)
    get_joint_state(move_group)
    
    #goal2 execute   
    move_joints(move_group, goal2)
    get_joint_state(move_group)

    #goal3 execute   
    move_joints(move_group, goal3)
    get_joint_state(move_group)
    
    move_joints(move_group, goal4)
    get_joint_state(move_group)
    
move_joints(move_group, finish)
get_joint_state(move_group)
