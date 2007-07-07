%define name multitail
%define version 5.0.5
%define release %mkrel 1

Summary: Multitail lets you view one or multiple files like the original tail program
Name: %name
Version: %version
Release: %release
License: GPL
Group: Text tools
Url: http://www.vanheusden.com/multitail/
Source: %{name}-%{version}.tgz
BuildRoot: %{_tmppath}/%name-buildroot
BuildRequires:	libncurses-devel

%description
multitail lets you view one or multiple files like the original tail program.
The difference is that it creates multiple windows on your console (with 
ncurses). It can also use colors while displaying the logfiles, for faster
recognition of which lines are important and which are not. It supports regular
expressions. It has interactive menus for editing given regular expressions and
deleting and adding windows.

%prep

%setup -q 

%build

%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%_bindir
mkdir -p $RPM_BUILD_ROOT%_mandir/man1
install -m 755 %name $RPM_BUILD_ROOT%_bindir/
install -m 644 %name.1 $RPM_BUILD_ROOT%_mandir/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man1/*


