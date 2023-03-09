import subprocess

#TODO: properly document class and clean implementation
class PandaGripperClient:
    def homing(self):
        subprocess.run(["ros2","action", "send_goal", "/panda_gripper/homing", "franka_msgs/action/Homing", "{}"])

    def move(self, width, speed):
        subprocess.run(["ros2","action", "send_goal", "/panda_gripper/move", "franka_msgs/action/Move", "{width: " + str(width) + ", speed: " + str(speed) + "}"])

    def grasp(self, width, speed, force, epsilon_inner, epsilon_outer):
        subprocess.run(["ros2","action", "send_goal", "franka_msgs/action/Grasp", "/panda_gripper/grasp", "{width: " + str(width) + ", speed: " + str(speed) + ", force: " + str(force) + ", epsilon_inner: " + str(epsilon_inner) + ", epsilon_outer: " + str(epsilon_outer) + "}"])

    def gripper_command(self, width, max_effort):
        subprocess.run(["ros2","topic", "pub", "/panda_gripper/gripper_cmd", "franka_msgs/msg/GripperCommand", "{width: " + str(width) + ", max_effort: " + str(max_effort) + "}"])


if __name__=="__main__":
    panda_gripper_client = PandaGripperClient()
    panda_gripper_client.test()
    panda_gripper_client.move(0.0, 0.1)
    panda_gripper_client.move(0.1, 0.1)
    panda_gripper_client.homing()
