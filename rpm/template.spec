Name:           ros-kinetic-franka-ros
Version:        0.1.1
Release:        0%{?dist}
Summary:        ROS franka_ros package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://wiki.ros.org/franka_ros
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-franka-control
Requires:       ros-kinetic-franka-description
Requires:       ros-kinetic-franka-example-controllers
Requires:       ros-kinetic-franka-gripper
Requires:       ros-kinetic-franka-hw
Requires:       ros-kinetic-franka-msgs
Requires:       ros-kinetic-franka-visualization
Requires:       ros-kinetic-panda-moveit-config
BuildRequires:  ros-kinetic-catkin

%description
franka_ros is a metapackage for all Franka Emika ROS packages

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

