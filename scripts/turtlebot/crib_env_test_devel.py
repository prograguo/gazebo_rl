#!/usr/bin/env python
from __future__ import print_function

import gym
import numpy as np
import time
import random
from gym import wrappers
# ROS packages required
import rospy
import rospkg
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Twist
from gazebo_msgs.msg import ModelStates, LinkStates

# import our training environment
from turtlebot_envs import continuous_crib_task_env # need write task env

rospy.init_node('env_test', anonymous=True, log_level=rospy.DEBUG)    
env = gym.make('TurtlebotCrib-v2')

