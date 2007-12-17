%define name	pywbxml
%define version	0.1
%define release	%mkrel 1

Summary:	Python binding for wbxml2
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
License:	GPL
Group:		Development/Python
BuildRequires:	wbxml2-devel >= 0.9.2
BuildRequires:	python-devel libxml2-devel python-pyrex
Url:		http://synce.sourceforge.net

%description
Python binding for wbxml2

%prep
%setup -q

%build
aclocal
autoconf
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

rm -rf %buildroot%{py_platsitedir}/*.a
rm -rf %buildroot%{py_platsitedir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc README AUTHORS NEWS
%{py_platsitedir}/*.so
