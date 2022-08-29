// Copyright (c) 2022 Franka Emika GmbH
#pragma once

#include <array>
#include <memory>

// clang-format off
/**
 * @file joint_wall.h
 * Contains functions for calculating torques generated by virtual walls.
 |<---- PD_zone_width ------>|<---D_zone_width--->|                  |<---D_zone_width--->|<--- PD_zone_width --->|
 |:::::::::::::::::::::::::::|- - - - - - - - - - |                  | - - - - - - - - - -|:::::::::::::::::::::::|
 ^ soft_lower_joint_position_limit                   normal ^ range               soft_upper_joint_position_limit ^
        PD_zone_boundary_min ^                                                            ^ PD_zone_boundary_max
                              D_zone_boundary_min ^                  ^ D_zone_boundary_max
*/
// clang-format on

namespace franka_example_controllers {

/// A class that offers an implementation of a virtual wall for a single joint.
class JointWall {
 public:
  /**
   * Creates a JointWall instance with default params.
   */
  JointWall() = delete;

  /**
   * Creates a JointWall instance with configurable parameters.
   * @param[in] soft_upper_joint_position_limit (rad)
   * @param[in] soft_lower_joint_position_limit (rad)
   * @param[in] PD_zone_width (meter)
   * @param[in] D_zone_width (meter)
   * @param[in] PD_zone_stiffness (N*meter/rad)
   * @param[in] PD_zone_damping (N*meter*s/rad)
   * @param[in] D_zone_damping (N*meter*s/rad)
   */
  JointWall(double soft_upper_joint_position_limit,
            double soft_lower_joint_position_limit,
            double PD_zone_width,
            double D_zone_width,
            double PD_zone_stiffness,
            double PD_zone_damping,
            double D_zone_damping);

  /**
   * Computes the torque with given q and dq. Be aware that the torque is also affected by previous
   * states.
   * @param[in] q current joint position.
   * @param[in] dq the current joint velocity.
   * @return the resulting torque
   */
  double computeTorque(double q, double dq);

  /**
   * Resets the initialized flag to false. After calling reset, the next call to computeTorque
   * resets the internal states for joint position and velocity (q, dq). Call this method before
   * restarting your controller, e.g. when the position might have changed during control pauses due
   * to guiding.
   */
  void reset();

 private:
  /**
   * Indicates the status of moving wall, which occurs after initializing the state inside a wall.
   */
  enum class MotionInWall {
    EnteringNormal,
    PenetratingLowerLimit,
    LeavingLowerLimit,
    PenetratingUpperLimit,
    LeavingUpperLimit
  };

  // Joint wall parameters
  double soft_upper_joint_position_limit_{0};
  double soft_lower_joint_position_limit_{0};
  double PD_zone_width_{0};
  double D_zone_width_{0};
  double PD_zone_stiffness_{0};
  double PD_zone_damping_{0};
  double D_zone_damping_{0};

  bool initialized_{false};  // Internal states q, dq will be reset to the current states in
                             // computeTorque if initialized_ = false;

  // Indicates whether the joint wall is still moving, which occurs after initializing the state
  // inside joint wall.
  bool moving_wall_{false};

  double zone_width_scale_{1};

  /**
   * Checks if x is in range [low, high]
   * @param[in] low lower limit of the range.
   * @param[in] high upper limit of the range.
   * @param[in] x value to check.
   * @return true if in range, false otherwise.
   */
  static bool inRange(double low, double high, double x);

  /**
   * Check if the input is positive number, if not print error and return its abs
   * @param[in] value The value to check.
   * @return the absolute value of the value.
   */
  static double positiveCheck(double value);

  /**
   * Initializes the joint wall computation with initial states.
   * @param[in] q the current joint position.
   * @param[in] dq the current joint velocity.
   */
  void init(double q, double dq);

  /**
   * Moves the wall with given state if the state is initialized inside the wall
   * @param[in] q the current joint position.
   * @param[in] dq the current joint velocity.
   */
  void adjustMovingWall(double q, double dq);

  /**
   * Checks the motion type in joint wall
   * @param[in] q the current joint position.
   * @param[in] dq the current joint velocity.
   */
  MotionInWall getMotionInWall(double q, double dq) const;
};

/**
 * A class that organizes multiple virtual joint walls.
 * @tparam num_dof the number of joints to create virtual walls for.
 */
template <size_t num_dof>
class JointWallContainer {
 public:
  /**
   * Creates a new virtual joint position wall instance. (see joint_wall.h for more details on joint
   * wall parameters.)
   *
   * @param[in] soft_upper_joint_position_limits
   * @param[in] soft_lower_joint_position_limits
   * @param[in] PD_zone_widths
   * @param[in] D_zone_widths
   * @param[in] PD_zone_stiffnesses
   * @param[in] PD_zone_dampings
   * @param[in] D_zone_dampings
   */
  JointWallContainer(const std::array<double, num_dof>& soft_upper_joint_position_limits,
                     const std::array<double, num_dof>& soft_lower_joint_position_limits,
                     const std::array<double, num_dof>& PD_zone_widths,
                     const std::array<double, num_dof>& D_zone_widths,
                     const std::array<double, num_dof>& PD_zone_stiffnesses,
                     const std::array<double, num_dof>& PD_zone_dampings,
                     const std::array<double, num_dof>& D_zone_dampings) {
    for (size_t i = 0; i < num_dof; i++) {
      joint_walls_.at(i) = std::make_unique<JointWall>(
          soft_upper_joint_position_limits[i], soft_lower_joint_position_limits[i],
          PD_zone_widths[i], D_zone_widths[i], PD_zone_stiffnesses[i], PD_zone_dampings[i],
          D_zone_dampings[i]);
    }
  }

  JointWallContainer() = delete;

  /**
   * Computes the torques generated by virtual walls.
   * @param[in] q the current joint positions.
   * @param[in] dq the current joint velocities.
   * @return the repelling torques/efforts from the virtual wall.
   */
  std::array<double, num_dof> computeTorque(const std::array<double, num_dof>& q,
                                            const std::array<double, num_dof>& dq) {
    std::array<double, num_dof> torque;
    for (size_t i = 0; i < num_dof; i++) {
      torque[i] = joint_walls_[i]->computeTorque(q[i], dq[i]);
    };
    return torque;
  }

  /**
   * Resets the initialized flags of all walls to false. After calling reset, the next call to
   * computeTorque resets the internal states for joint position and velocity (q, dq). Call this
   * method before restarting your controller, e.g. when the position might have changed during
   * control pauses due to guiding.
   */
  void reset() {
    for (auto& jw : joint_walls_) {
      jw->reset();
    }
  }

 private:
  std::array<std::unique_ptr<JointWall>, num_dof> joint_walls_;
};

}  // namespace franka_example_controllers
