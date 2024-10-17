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
Url:		https://synce.sourceforge.net

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


%changelog
* Mon Nov 22 2010 Funda Wang <fwang@mandriva.org> 0.1-3mdv2011.0
+ Revision: 599636
- fix BR

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sat Dec 27 2008 Adam Williamson <awilliamson@mandriva.org> 0.1-2mdv2009.1
+ Revision: 319680
- buildrequires popt-devel
- use configure2_5x not configure
- rebuild with python 2.6

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.1-1mdv2008.1
+ Revision: 140738
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Jul 01 2007 Emmanuel Andry <eandry@mandriva.org> 0.1-1mdv2008.0
+ Revision: 46537
- fix buildrequires
- Import pywbxml

