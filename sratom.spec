%define lib_major       0
%define lib_name        %mklibname %{name} %{lib_major}
%define lib_name_devel  %mklibname %{name} -d

Name:           sratom
Version:	0.6.12
Release:	1
Summary:        Library for serialising LV2 atoms to/from RDF, particularly the Turtle syntax
Source0:         http://download.drobilla.net/%{name}-%{version}.tar.xz
URL:            http://drobilla.net/software/%{name}/
License:        MIT-like
Group:          System/Libraries

BuildRequires:  cmake
BuildRequires:  waf, pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  serd-devel
BuildRequires:  sord-devel
BuildRequires:  pkgconfig(lv2)
BuildRequires:  lv2
BuildRequires:  meson
BuildRequires:  doxygen
BuildRequires:  python3dist(sphinx)

%description
Lightweight C library for storing RDF data in memory.

%files
%doc COPYING

#-----------------------------------
%package -n %{lib_name}

Summary:        Library for serialising LV2 atoms to/from RDF, particularly the Turtle syntax
Group:          System/Libraries

%description -n %{lib_name}
Lightweight C library for storing RDF data in memory.


%files -n %{lib_name}
%{_libdir}/lib%{name}-%{lib_major}.so.*

#-----------------------------------
%package -n %{lib_name_devel}
Summary:        Headers for the sord RDF storage library
Group:          System/Libraries
Requires:       %{lib_name} = %{version}-%{release}
Requires:       pkgconfig
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{lib_name_devel}
Development files needed to build applications against %{name}.

%files -n %{lib_name_devel}
%{_libdir}/lib%{name}-%{lib_major}.so
%dir %{_includedir}/%{name}-%{lib_major}/%{name}
%{_includedir}/%{name}-%{lib_major}/%{name}/*.h
%{_libdir}/pkgconfig/%{name}-%{lib_major}.pc

#-----------------------------------
%prep
%setup -q

%build
%meson -Ddocs=disabled
%meson_build

%install
%meson_install
