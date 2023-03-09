# Copyright 2018 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from franka_msgs.action import (Grasp, Homing, Move)
from control_msgs.msg import GripperCommand

import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node


class PandaGripperClient(Node):

    def __init__(self):
        super().__init__('panda_gripper_action_client')
        
        # create action clients
        self.homing_action_client = ActionClient(self, Homing, '/panda_gripper/homing')
        self.move_action_client = ActionClient(self, Move, '/panda_gripper/move')
        self.grasp_action_client = ActionClient(self, Grasp, '/panda_gripper/grasp')
        self.gripper_command_action_client = ActionClient(self, GripperCommand, '/panda_gripper/gripper_action')
        

    def homing(self):
        self.homing_action_client.wait_for_server()
        return self.homing_action_client.send_goal_async(Homing.Goal())

    def move(self, width, speed):
        m = Move.Goal()
        m.width = width
        m.speed = speed
        self.move_action_client.wait_for_server()
        return self.move_action_client.send_goal_async(m)

    def grasp(self, width, epsilon_inner, epsilon_outer, speed, force):
        g = Grasp.Goal()
        g.width = width
        g.epsilon_inner = epsilon_inner
        g.epsilon_outer = epsilon_outer
        g.speed = speed
        g.force = force
        self.grasp_action_client.wait_for_server()
        return self.grasp_action_client.send_goal_async(g)

    def gripper_command(self, width, max_effort):
        g = GripperCommand.Goal()
        g.command.position = width
        g.command.max_effort = max_effort
        self.gripper_command_action_client.wait_for_server()
        return self.gripper_command_action_client.send_goal_async(g)
