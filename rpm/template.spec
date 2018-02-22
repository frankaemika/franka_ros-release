Name:           ros-kinetic-franka-visualization
Version:        0.3.0
Release:        0%{?dist}
Summary:        ROS franka_visualization package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://wiki.ros.org/franka_visualization
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-franka-description
Requires:       ros-kinetic-libfranka
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-xacro
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-libfranka
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-sensor-msgs

%description
This package contains visualization tools for Franka Emika.

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
* Thu Feb 22 2018 Franka Emika GmbH <support@franka.de> - 0.3.0-0
- Autogenerated by Bloom

* Wed Jan 31 2018 Franka Emika GmbH <support@franka.de> - 0.2.2-0
- Autogenerated by Bloom

* Tue Jan 30 2018 Franka Emika GmbH <support@franka.de> - 0.2.1-0
- Autogenerated by Bloom

* Tue Oct 10 2017 Franka Emika GmbH <info@franka.de> - 0.1.2-0
- Autogenerated by Bloom

* Mon Oct 09 2017 Franka Emika GmbH <info@franka.de> - 0.1.1-0
- Autogenerated by Bloom

