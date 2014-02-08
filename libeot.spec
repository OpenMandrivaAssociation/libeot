%define major 0
%define libname %mklibname eot %{major}
%define devname %mklibname eot -d
%define staticname %mklibname eot -d -s

Name: libeot
Version: 0.01
# Packaged from v0.01 tag in https://github.com/umanwizard/libeot.git
Release: 2
Source0: %{name}-%{version}.tar.xz
Summary: Library for parsing Embedded OpenType files
URL: https://github.com/umanwizard/libeot.git
License: MPL 2.0
Group: System/Libraries

%description
Library for parsing Embedded OpenType (Microsoft font format) files

%package -n %{libname}
Summary: Library for parsing Embedded OpenType files
Group: System/Libraries

%description -n %{libname}
Library for parsing Embedded OpenType (Microsoft font format) files

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
libtoolize --force
aclocal
autoheader
automake -a
autoconf
%configure

%build
%make

%install
%makeinstall_std

%files
%{_bindir}/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
