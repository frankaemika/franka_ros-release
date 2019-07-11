Name:           ros-melodic-franka-ros
Version:        0.6.0
Release:        1%{?dist}
Summary:        ROS franka_ros package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://wiki.ros.org/franka_ros
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-melodic-franka-control
Requires:       ros-melodic-franka-description
Requires:       ros-melodic-franka-example-controllers
Requires:       ros-melodic-franka-gripper
Requires:       ros-melodic-franka-hw
Requires:       ros-melodic-franka-msgs
Requires:       ros-melodic-franka-visualization
Requires:       ros-melodic-panda-moveit-config
BuildRequires:  ros-melodic-catkin

%description
franka_ros is a metapackage for all Franka Emika ROS packages

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Thu Jul 11 2019 Franka Emika GmbH <support@franka.de> - 0.6.0-1
- Autogenerated by Bloom

