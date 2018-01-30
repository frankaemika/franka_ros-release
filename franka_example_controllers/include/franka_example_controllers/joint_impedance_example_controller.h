// Copyright (c) 2017 Franka Emika GmbH
// Use of this source code is governed by the Apache-2.0 license, see LICENSE
#pragma once

#include <memory>
#include <string>
#include <vector>

#include <controller_interface/multi_interface_controller.h>
#include <hardware_interface/joint_command_interface.h>
#include <hardware_interface/robot_hw.h>
#include <realtime_tools/realtime_publisher.h>
#include <ros/node_handle.h>
#include <ros/time.h>

#include <franka_example_controllers/JointTorqueComparison.h>
#include <franka_hw/franka_cartesian_command_interface.h>
#include <franka_hw/franka_model_interface.h>
#include <franka_hw/trigger_rate.h>

namespace franka_example_controllers {

class JointImpedanceExampleController : public controller_interface::MultiInterfaceController<
                                            franka_hw::FrankaModelInterface,
                                            hardware_interface::EffortJointInterface,
                                            franka_hw::FrankaPoseCartesianInterface> {
 public:
  JointImpedanceExampleController();
  bool init(hardware_interface::RobotHW* robot_hw, ros::NodeHandle& node_handle);
  void starting(const ros::Time&);
  void update(const ros::Time&, const ros::Duration& period);

 private:
  std::unique_ptr<franka_hw::FrankaCartesianPoseHandle> cartesian_pose_handle_;
  std::unique_ptr<franka_hw::FrankaModelHandle> model_handle_;
  std::vector<hardware_interface::JointHandle> joint_handles_;
  std::array<double, 7> last_tau_d_ = {{0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0}};
  franka_hw::TriggerRate rate_trigger_;
  double radius_{0.1};
  double acceleration_time_{2.0};
  double vel_max_{0.05};
  std::vector<std::string> joint_names_;
  std::vector<double> k_gains_;
  std::vector<double> d_gains_;
  double angle_{0.0};
  double vel_current_{0.0};
  std::array<double, 16> initial_pose_;
  realtime_tools::RealtimePublisher<JointTorqueComparison> torques_publisher_;
  double coriolis_factor_{1.0};
};

}  // namespace franka_example_controllers
