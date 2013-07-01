%define name multitail
%define version 5.2.8
%define release 2

Summary: Lets you view one or multiple files like the original tail program
Name: %name
Version: %version
Release: %release
License: GPL
Group: Text tools
Url: http://www.vanheusden.com/multitail/
Source: %{name}-%{version}.tgz
BuildRequires:	ncurses-devel

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




%changelog
* Wed Apr 20 2011 Michael Scherer <misc@mandriva.org> 5.2.8-1mdv2011.0
+ Revision: 656144
- update to new version 5.2.8

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 5.2.6-2mdv2011.0
+ Revision: 612953
- the mass rebuild of 2010.1 packages

* Thu Feb 18 2010 Frederik Himpe <fhimpe@mandriva.org> 5.2.6-1mdv2010.1
+ Revision: 507892
- update to new version 5.2.6

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 5.2.2-3mdv2010.0
+ Revision: 430122
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 5.2.2-2mdv2009.0
+ Revision: 268204
- rebuild early 2009.0 package (before pixel changes)

* Wed May 28 2008 Nicolas Vigier <nvigier@mandriva.com> 5.2.2-1mdv2009.0
+ Revision: 212639
- update to 5.2.2

* Sat Mar 01 2008 Michael Scherer <misc@mandriva.org> 5.2.1-1mdv2008.1
+ Revision: 177284
- update to new version 5.2.1

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Jul 11 2007 Nicolas Vigier <nvigier@mandriva.com> 5.2.0-1mdv2008.0
+ Revision: 51226
- new version

* Sun Jul 08 2007 Nicolas Vigier <nvigier@mandriva.com> 5.0.5-1mdv2008.0
+ Revision: 49642
- new version

* Fri Apr 27 2007 Lenny Cartier <lenny@mandriva.org> 5.0.1-1mdv2008.0
+ Revision: 18690
- Update to 5.0.1


* Wed Jan 17 2007 Lenny Cartier <lenny@mandriva.com> 4.2.0-1mdv2007.0
+ Revision: 109766
- Update to stable 4.2.0
- Import multitail

* Thu Jul 13 2006 Lenny Cartier <lenny@mandriva.com> 4.1.0-1mdv2007.0
- 4.1.0

* Wed Jun 07 2006 Lenny Cartier <lenny@mandriva.com> 4.0.5-1mdv2007.0
- 4.0.5

* Wed May 24 2006 Lenny Cartier <lenny@mandriva.com> 4.0.4-1mdk
- 4.0.4

* Sat Apr 22 2006 Jerome Soyer <saispo@mandriva.org> 4.0.3-1mdk
- New release 4.0.3

* Fri Apr 14 2006 Jerome Soyer <saispo@mandriva.org> 4.0.0-1mdk
- New release 4.0.0

* Fri Apr 14 2006 Lenny Cartier <lenny@mandriva.com> 4.0.0-1mdk
- 4.0.0

* Wed Mar 29 2006 Lenny Cartier <lenny@mandriva.com> 3.8.10-1mdk
- 3.8.10

* Wed Mar 15 2006 Lenny Cartier <lenny@mandriva.com> 3.8.9.1-1mdk
- 3.8.9.1

* Thu Mar 09 2006 Lenny Cartier <lenny@mandriva.com> 3.8.8-1mdk
- 3.8.8

* Thu Feb 02 2006 Lenny Cartier <lenny@mandriva.com> 3.8.5-1mdk
- 3.8.5

* Mon Jan 16 2006 Lenny Cartier <lenny@mandriva.com> 3.8.4-1mdk
- 3.8.4

* Tue Dec 27 2005 Lenny Cartier <lenny@mandriva.com> 3.8.0-1mdk
- 3.8.0

* Wed Dec 07 2005 Lenny Cartier <lenny@mandriva.com> 3.6.1-1mdk
- 3.6.1

* Mon Jan 24 2005 Lenny Cartier <lenny@mandrakesoft.com> 3.4.5-1mdk
- 3.4.5

* Mon Jan 17 2005 Lenny Cartier <lenny@mandrakesoft.com> 3.4.4-1mdk
- 3.4.4

* Tue Nov 30 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.4.2-1mdk
- 3.4.2

* Wed Oct 20 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.4.0-1mdk
- 3.4.0

* Tue Jul 27 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.2.3-1mdk
- 3.2.3

* Tue Jun 08 2004 Franck Villaume <fvill@freesurf.fr> 3.2.1-1mdk
- new version
- fix buildrequires

* Wed May 05 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.0.6-1mdk
- new

