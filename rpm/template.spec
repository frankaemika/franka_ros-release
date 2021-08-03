%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-franka-gazebo
Version:        0.8.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS franka_gazebo package

License:        Apache 2.0
URL:            http://wiki.ros.org/franka_gazebo
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-angles
Requires:       ros-noetic-control-msgs
Requires:       ros-noetic-control-toolbox
Requires:       ros-noetic-controller-interface
Requires:       ros-noetic-controller-manager
Requires:       ros-noetic-eigen-conversions
Requires:       ros-noetic-franka-example-controllers
Requires:       ros-noetic-franka-gripper
Requires:       ros-noetic-franka-hw
Requires:       ros-noetic-franka-msgs
Requires:       ros-noetic-gazebo-ros
Requires:       ros-noetic-gazebo-ros-control
Requires:       ros-noetic-hardware-interface
Requires:       ros-noetic-joint-limits-interface
Requires:       ros-noetic-kdl-parser
Requires:       ros-noetic-pluginlib
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-std-msgs
Requires:       ros-noetic-transmission-interface
Requires:       ros-noetic-urdf
BuildRequires:  gtest-devel
BuildRequires:  ros-noetic-angles
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-control-msgs
BuildRequires:  ros-noetic-control-toolbox
BuildRequires:  ros-noetic-controller-interface
BuildRequires:  ros-noetic-controller-manager
BuildRequires:  ros-noetic-eigen-conversions
BuildRequires:  ros-noetic-franka-example-controllers
BuildRequires:  ros-noetic-franka-gripper
BuildRequires:  ros-noetic-franka-hw
BuildRequires:  ros-noetic-franka-msgs
BuildRequires:  ros-noetic-gazebo-dev
BuildRequires:  ros-noetic-gazebo-ros-control
BuildRequires:  ros-noetic-hardware-interface
BuildRequires:  ros-noetic-joint-limits-interface
BuildRequires:  ros-noetic-kdl-parser
BuildRequires:  ros-noetic-pluginlib
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-rostest
BuildRequires:  ros-noetic-std-msgs
BuildRequires:  ros-noetic-transmission-interface
BuildRequires:  ros-noetic-urdf
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
This package offers the FrankaHWSim Class to simulate a Franka Robot in Gazebo

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Tue Aug 03 2021 Franka Emika GmbH <support@franka.de> - 0.8.0-1
- Autogenerated by Bloom

