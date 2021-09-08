%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-franka-hw
Version:        0.8.1
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS franka_hw package

License:        Apache 2.0
URL:            http://wiki.ros.org/franka_hw
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-actionlib
Requires:       ros-noetic-actionlib-msgs
Requires:       ros-noetic-combined-robot-hw
Requires:       ros-noetic-controller-interface
Requires:       ros-noetic-franka-msgs
Requires:       ros-noetic-hardware-interface
Requires:       ros-noetic-joint-limits-interface
Requires:       ros-noetic-libfranka
Requires:       ros-noetic-pluginlib
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-std-srvs
Requires:       ros-noetic-urdf
BuildRequires:  gtest-devel
BuildRequires:  ros-noetic-actionlib
BuildRequires:  ros-noetic-actionlib-msgs
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-combined-robot-hw
BuildRequires:  ros-noetic-controller-interface
BuildRequires:  ros-noetic-franka-description
BuildRequires:  ros-noetic-franka-msgs
BuildRequires:  ros-noetic-hardware-interface
BuildRequires:  ros-noetic-joint-limits-interface
BuildRequires:  ros-noetic-libfranka
BuildRequires:  ros-noetic-message-generation
BuildRequires:  ros-noetic-pluginlib
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-rostest
BuildRequires:  ros-noetic-std-srvs
BuildRequires:  ros-noetic-urdf
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
franka_hw provides hardware interfaces for using Franka Emika research robots
with ros_control

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
* Wed Sep 08 2021 Franka Emika GmbH <support@franka.de> - 0.8.1-1
- Autogenerated by Bloom

* Tue Aug 03 2021 Franka Emika GmbH <support@franka.de> - 0.8.0-1
- Autogenerated by Bloom

* Wed Mar 31 2021 Franka Emika GmbH <support@franka.de> - 0.7.1-2
- Autogenerated by Bloom

* Thu Oct 22 2020 Franka Emika GmbH <support@franka.de> - 0.7.1-1
- Autogenerated by Bloom

* Wed Sep 02 2020 Franka Emika GmbH <support@franka.de> - 0.7.0-1
- Autogenerated by Bloom

