Name:           ros-kinetic-franka-example-controllers
Version:        0.2.2
Release:        0%{?dist}
Summary:        ROS franka_example_controllers package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://wiki.ros.org/franka_example_controllers
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-controller-interface
Requires:       ros-kinetic-dynamic-reconfigure
Requires:       ros-kinetic-franka-description
Requires:       ros-kinetic-franka-hw
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-hardware-interface
Requires:       ros-kinetic-libfranka
Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-pluginlib
Requires:       ros-kinetic-realtime-tools
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-rospy
BuildRequires:  eigen3-devel
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-controller-interface
BuildRequires:  ros-kinetic-dynamic-reconfigure
BuildRequires:  ros-kinetic-franka-hw
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-hardware-interface
BuildRequires:  ros-kinetic-libfranka
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-pluginlib
BuildRequires:  ros-kinetic-realtime-tools
BuildRequires:  ros-kinetic-roscpp

%description
franka_example_controllers provides example code for controlling Franka Emika
research robots with ros_control

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
* Wed Jan 31 2018 Franka Emika GmbH <support@franka.de> - 0.2.2-0
- Autogenerated by Bloom

* Tue Jan 30 2018 Franka Emika GmbH <support@franka.de> - 0.2.1-0
- Autogenerated by Bloom

* Tue Oct 10 2017 Franka Emika GmbH <info@franka.de> - 0.1.2-0
- Autogenerated by Bloom

* Mon Oct 09 2017 Franka Emika GmbH <info@franka.de> - 0.1.1-0
- Autogenerated by Bloom

