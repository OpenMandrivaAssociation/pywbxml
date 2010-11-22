%define name	pywbxml
%define version	0.1
%define release	%mkrel 3

Summary:	Python binding for wbxml2
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
License:	GPL
Group:		Development/Python
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	wbxml-devel >= 0.9.2
BuildRequires:	python-devel libxml2-devel python-pyrex
BuildRequires:	popt-devel
Url:		http://synce.sourceforge.net

%description
Python binding for wbxml2

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

rm -rf %buildroot%{py_platsitedir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc README AUTHORS NEWS
%{py_platsitedir}/*.so
