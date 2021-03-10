#!/usr/bin/env python
import rospy
import tf
import rospkg
import os

from gazebo_msgs.srv import (
    SpawnModel,
    DeleteModel,
)

from geometry_msgs.msg import (
    PoseStamped,
    Pose,
    Point,
    Quaternion,
)

rospy.init_node('object_spawn', anonymous=True)




def spawn_gazebo_model(model_path, model_name, model_pose, reference_frame="world"):
  """
  Spawn model in gazebo
  """
  model_xml = ''
  with open(model_path, "r") as model_file:
    model_xml = model_file.read().replace('\n', '')
  rospy.wait_for_service('/gazebo/spawn_urdf_model')
  try:
    spawn_urdf = rospy.ServiceProxy('/gazebo/spawn_urdf_model', SpawnModel)
    resp_urdf = spawn_urdf(model_name, model_xml, "/", model_pose, reference_frame)
  except rospy.ServiceException, e:
    rospy.logerr("Spawn URDF service call failed: {0}".format(e))

def delete_gazebo_model(models):
  """
  Delete model in gazebo
  """
  try:
    delete_model = rospy.ServiceProxy('/gazebo/delete_model', DeleteModel)
    for a_model in models:
      resp_delete = delete_model(a_model)
  except rospy.ServiceException, e:
    rospy.loginfo("Delete Model service call failed: {0}".format(e))

rospack = rospkg.RosPack()
pack_path = rospack.get_path('ril_mm_gazebo')


table_path = pack_path+os.sep+'urdf'+os.sep+'objects'+os.sep+'table.urdf'
table_name = 'table'
table_pose = Pose(position=Point(x=1.2, y=0.0, z=0.62))

block_path = pack_path+os.sep+'urdf'+os.sep+'objects'+os.sep+'block.urdf'
block_name = 'block'
block_pose = Pose(position=Point(x=1.0, y=0.22, z=0.67))

banana_path = pack_path+os.sep+'urdf'+os.sep+'objects'+os.sep+'banana.urdf'
banana_name = 'banana'
banana_pose = Pose(position=Point(x=1.0, y=0.18, z=0.67))

delete_gazebo_model([table_name, block_name])
spawn_gazebo_model(table_path, table_name, table_pose)
spawn_gazebo_model(block_path, block_name, block_pose)
spawn_gazebo_model(banana_path, banana_name, banana_pose)
