// Copyright (c) 2017 Franka Emika GmbH
// Use of this source code is governed by the Apache-2.0 license, see LICENSE
#include <franka_example_controllers/joint_position_example_controller.h>

#include <cmath>

#include <controller_interface/controller_base.h>
#include <hardware_interface/hardware_interface.h>
#include <hardware_interface/joint_command_interface.h>
#include <pluginlib/class_list_macros.h>
#include <ros/ros.h>
#include <xmlrpcpp/XmlRpcValue.h>

namespace franka_example_controllers {

JointPositionExampleController::JointPositionExampleController()
    : position_joint_interface_(nullptr), elapsed_time_(0.0) {}

bool JointPositionExampleController::init(hardware_interface::RobotHW* robot_hardware,
                                          ros::NodeHandle& root_node_handle,
                                          ros::NodeHandle& /*controller_node_handle*/) {
  position_joint_interface_ = robot_hardware->get<hardware_interface::PositionJointInterface>();
  if (position_joint_interface_ == nullptr) {
    ROS_ERROR(
        "JointPositionExampleController: Error getting position joint interface from hardware!");
    return false;
  }
  XmlRpc::XmlRpcValue parameters;
  if (!root_node_handle.getParam("joint_names", parameters)) {
    ROS_ERROR("JointPositionExampleController: Could not parse joint names");
  }
  if (parameters.size() != 7) {
    ROS_ERROR_STREAM("JointPositionExampleController: Wrong number of joint names, got "
                     << int(parameters.size()) << " instead of 7 names!");
    return false;
  }
  position_joint_handles_.resize(7);
  joint_names_.resize(7);
  for (size_t i = 0; i < 7; ++i) {
    joint_names_[i] = static_cast<std::string>(parameters[i]);
    try {
      position_joint_handles_[i] = position_joint_interface_->getHandle(joint_names_[i]);
    } catch (const hardware_interface::HardwareInterfaceException& e) {
      ROS_ERROR_STREAM(
          "JointPositionExampleController: Exception getting joint handles: " << e.what());
      return false;
    }
  }
  elapsed_time_ = ros::Duration(0.0);
  return true;
}

void JointPositionExampleController::starting(const ros::Time& /*time*/) {
  for (size_t i = 0; i < 7; ++i) {
    initial_pose_[i] = position_joint_handles_[i].getPosition();
  }
}

void JointPositionExampleController::update(const ros::Time& /*time*/,
                                            const ros::Duration& period) {
  elapsed_time_ += period;

  double delta_angle = M_PI / 16 * (1 - std::cos(M_PI / 5.0 * elapsed_time_.toSec())) * 0.2;
  for (size_t i = 0; i < 7; ++i) {
    if (i == 4) {
      position_joint_handles_[i].setCommand(initial_pose_[i] - delta_angle);
    } else {
      position_joint_handles_[i].setCommand(initial_pose_[i] + delta_angle);
    }
  }
}

}  // namespace franka_example_controllers

PLUGINLIB_EXPORT_CLASS(franka_example_controllers::JointPositionExampleController,
                       controller_interface::ControllerBase)
