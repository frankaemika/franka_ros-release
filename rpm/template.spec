%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-franka-control
Version:        0.8.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS franka_control package

License:        Apache 2.0
URL:            http://wiki.ros.org/franka_control
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-controller-interface
Requires:       ros-noetic-controller-manager
Requires:       ros-noetic-franka-description
Requires:       ros-noetic-franka-gripper
Requires:       ros-noetic-franka-hw
Requires:       ros-noetic-franka-msgs
Requires:       ros-noetic-geometry-msgs
Requires:       ros-noetic-joint-state-publisher
Requires:       ros-noetic-libfranka
Requires:       ros-noetic-pluginlib
Requires:       ros-noetic-realtime-tools
Requires:       ros-noetic-robot-state-publisher
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-sensor-msgs
Requires:       ros-noetic-std-srvs
Requires:       ros-noetic-tf
Requires:       ros-noetic-tf2-msgs
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-controller-interface
BuildRequires:  ros-noetic-controller-manager
BuildRequires:  ros-noetic-franka-hw
BuildRequires:  ros-noetic-franka-msgs
BuildRequires:  ros-noetic-geometry-msgs
BuildRequires:  ros-noetic-libfranka
BuildRequires:  ros-noetic-pluginlib
BuildRequires:  ros-noetic-realtime-tools
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-sensor-msgs
BuildRequires:  ros-noetic-std-srvs
BuildRequires:  ros-noetic-tf
BuildRequires:  ros-noetic-tf2-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
franka_control provides a hardware node to control a Franka Emika research robot

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

* Wed Mar 31 2021 Franka Emika GmbH <support@franka.de> - 0.7.1-2
- Autogenerated by Bloom

* Thu Oct 22 2020 Franka Emika GmbH <support@franka.de> - 0.7.1-1
- Autogenerated by Bloom

* Wed Sep 02 2020 Franka Emika GmbH <support@franka.de> - 0.7.0-1
- Autogenerated by Bloom

