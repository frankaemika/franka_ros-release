Name:           ros-kinetic-franka-control
Version:        0.1.1
Release:        0%{?dist}
Summary:        ROS franka_control package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://wiki.ros.org/franka_control
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-actionlib
Requires:       ros-kinetic-actionlib-msgs
Requires:       ros-kinetic-controller-interface
Requires:       ros-kinetic-controller-manager
Requires:       ros-kinetic-franka-description
Requires:       ros-kinetic-franka-hw
Requires:       ros-kinetic-franka-msgs
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-libfranka
Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-pluginlib
Requires:       ros-kinetic-realtime-tools
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-tf
Requires:       ros-kinetic-tf2-msgs
BuildRequires:  ros-kinetic-actionlib
BuildRequires:  ros-kinetic-actionlib-msgs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-controller-interface
BuildRequires:  ros-kinetic-controller-manager
BuildRequires:  ros-kinetic-franka-description
BuildRequires:  ros-kinetic-franka-hw
BuildRequires:  ros-kinetic-franka-msgs
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-libfranka
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-pluginlib
BuildRequires:  ros-kinetic-realtime-tools
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-tf
BuildRequires:  ros-kinetic-tf2-msgs

%description
franka_control provides a hardware node to control a Franka Emika research robot

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Mon Oct 09 2017 Franka Emika GmbH <info@franka.de> - 0.1.1-0
- Autogenerated by Bloom

