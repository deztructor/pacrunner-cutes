Summary: Pacrunner javascript plugin using cutes
Name: pacrunner-cutes
Version: 0.0.1
Release: 1
License: GPL21
Group: Development/Liraries
URL: https://github.com/nemomobile/pacrunner-cutes
Source0: %{name}-%{version}.tar.bz2
BuildRequires: cmake >= 2.8
BuildRequires: pkgconfig(pacrunner-1.0)
BuildRequires: pkgconfig(cutes)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(cor) >= 0.1.6
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(tut) >= 0.0.1
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
%description
%{summary}

%package tests
Summary:    Tests for pacrunner-cutes
License:    GPLv2.1
Group:      System Environment/Libraries
Requires:   %{name} = %{version}-%{release}
%description tests
%summary

%prep
%setup -q

%build
%cmake %{?_with_multiarch:-DENABLE_MULTIARCH=ON}
make %{?jobs:-j%jobs}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=%{buildroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/pacrunner/plugins/libpacrunner-cutes.so
%{_datadir}/pacrunner/pacrunner.js

%files tests
%defattr(-,root,root,-)
/opt/tests/pacrunner-cutes/*
