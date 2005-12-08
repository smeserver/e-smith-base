Summary: An authoritative and recursive DNS server made with security in mind
Name: maradns
Version: 1.1.90
Release: 1
Copyright: BSD (Two-clause)
Group: Networking/Daemons
Source: http://www.maradns.org/download/1.1/maradns-1.1.90.tar.bz2
Patch0: maradns-1.1.59-rpm.patch
Patch1: maradns-1.1.90.tar.bz2.sha1.asc
Patch1: maradns-1.1.90.tar.bz2.rmd.asc
BuildRoot: /var/tmp/%{name}-buildroot

%description
Erre con erre cigarro
Erre con erre barril
Rápido ruedan los carros
En el ferrocarril

MaraDNS is an authoritative and recursive DNS server made with 
security and embedded systems in mind.  More information is at 
http://www.maradns.org

%prep
%setup 
%patch0 -p1

%build
make 

%install
rm -fr $RPM_BUILD_ROOT/
mkdirhier $RPM_BUILD_ROOT/usr/sbin
mkdirhier $RPM_BUILD_ROOT/usr/bin
mkdirhier $RPM_BUILD_ROOT/usr/doc
mkdirhier $RPM_BUILD_ROOT/usr/man/man8
mkdirhier $RPM_BUILD_ROOT/usr/man/man1
mkdirhier $RPM_BUILD_ROOT/usr/man/man5
mkdirhier $RPM_BUILD_ROOT/etc
mkdirhier $RPM_BUILD_ROOT/etc/maradns
mkdirhier $RPM_BUILD_ROOT/etc/rc.d
mkdirhier $RPM_BUILD_ROOT/etc/rc.d/init.d
mkdirhier $RPM_BUILD_ROOT/etc/rc.d/rc3.d
mkdirhier $RPM_BUILD_ROOT/etc/rc.d/rc5.d
make install
cp build/rpm.mararc $RPM_BUILD_ROOT/etc/mararc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc doc/

/usr/sbin/maradns
/usr/sbin/zoneserver
/usr/bin/getzone
/usr/bin/fetchzone
/usr/bin/askmara
/usr/bin/duende
/usr/man/man1/askmara.1
/usr/man/man1/getzone.1
/usr/man/man1/fetchzone.1
/usr/man/man8/maradns.8
/usr/man/man8/zoneserver.8
/usr/man/man8/duende.8
/usr/man/man5/csv1.5
/usr/man/man5/csv2.5
/usr/man/man5/csv2_txt.5
/usr/man/man5/mararc.5
/etc/rc.d/rc3.d/S60maradns
/etc/rc.d/rc5.d/S60maradns
%config /etc/mararc
%config /etc/maradns/db.example.net
%config /etc/rc.d/init.d/maradns

%preun
# End all instances of MaraDNS
echo Sending all MaraDNS processes the TERM signal
ps -ef | awk '{print $2":"$8}' | grep maradns | grep -v $$ | \
  cut -f1 -d: | xargs kill > /dev/null 2>&1
echo waiting 1 second
sleep 1
echo Sending all MaraDNS processes the KILL signal
ps -e | awk '{print $1":"$NF}' | grep maradns | grep -v $$ | \
  cut -f1 -d: | xargs kill -9 > /dev/null 2>&1
echo MaraDNS should have been stopped

%changelog
* Wed Dec  7 2005 Sam Trenholme <sam+i55e6bt@chaosring.org>
- MaraDNS rpm package updated for version 1.1.90

* Mon Dec  5 2005 Sam Trenholme <sam+i55e6bt@chaosring.org>
- MaraDNS rpm package updated for version 1.1.61

* Sat Dec  3 2005 Sam Trenholme <sam+i55e6bt@chaosring.org>
- MaraDNS rpm package updated for version 1.1.60

* Mon Nov 28 2005 Sam Trenholme <sam+i55e6bt@chaosring.org>
- MaraDNS rpm package updated for version 1.1.59

* Sun Sep 1 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 1.1.04

* Sat Jul 20 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 1.1.03

* Sun Jul 14 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 1.0.04

* Fri Jul 12 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 1.0.03

* Sun Jun 30 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 1.0.02

* Wed Jun 26 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 1.0.01

* Fri Jun 21 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 1.0.00

* Sat Jun 15 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 0.9.92

* Wed Jun 12 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 0.9.91

* Mon Jun 10 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 0.9.39

* Sat Jun  8 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 0.9.38

* Fri Jun  7 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 0.9.37

* Wed Jun  5 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 0.9.36

* Fri May 31 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 0.9.34

* Tue May 21 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 0.9.33

* Sat May 18 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 0.9.31

* Fri May 17 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 0.9.30

* Wed May 15 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 0.9.29

* Mon May 13 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 0.9.28

* Thu May 9 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 0.9.26

* Wed May 8 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 0.9.24

* Sun May 5 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 0.9.23

* Mon Feb 11 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 0.9.11

* Mon Feb 11 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 0.9.10

* Sun Jan 27 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 0.9.09

* Fri Jan 25 2002 Sam Trenholme <rpmbuild@samiam.org>
- MaraDNS rpm package updated for version 0.9.08

* Thu Jan 10 2002 Sam Trenholme <rpmbuild@maradns.org>
- MaraDNS rpm package updated to version 0.5.31

* Mon Sep 24 2001 Sam Trenholme <rpmbuild@maradns.org>
- MaraDNS rpm package updated to version 0.5.30

* Fri Aug 10 2001 Sam Trenholme <rpmbuild@maradns.org>
- MaraDNS rpm package updated to version 0.5.29

* Wed Jul 18 2001 Sam Trenholme <rpmbuild@maradns.org>
- MaraDNS rpm package updated to version 0.5.28

* Sun Jul 15 2001 Sam Trenholme <rpmbuild@maradns.org>
- MaraDNS rpm package updated to version 0.5.27

* Sun Jul 8 2001 Sam Trenholme <rpmbuild@maradns.org>
- MaraDNS rpm package updated to version 0.5.26

* Thu May 31 2001 Sam Trenholme <rpmbuild@maradns.org>
- MaraDNS rpm package updated to version 0.5.25

* Mon May 21 2001 Sam Trenholme <rpmbuild@maradns.org>
- MaraDNS rpm package updated to version 0.5.24

* Sat May 19 2001 Sam Trenholme <rpmbuild@maradns.org>
- MaraDNS rpm package updated to version 0.5.23

* Thu May 10 2001 Sam Trenholme <rpmbuild@maradns.org>
- MaraDNS rpm package updatd to version 0.5.22

* Mon May 7 2001 Sam Trenholme <rpmbuild@maradns.org> 
- MaraDNS rpm package updated to version 0.5.21

* Sun May 6 2001 Sam Trenholme <rpmbuild@maradns.org>
- MaraDNS rpm package updated to version 0.5.20

* Thu May 3 2001 Sam Trenholme <rpmbuild@maradns.org>
- MaraDNS rpm package updated to version 0.5.18.

* Mon Apr 30 2001 Sam Trehnolme <rpmbuild@maradns.org>
- MaraDNS rpm package upped to version 0.5.17.

* Sun Apr 22 2001 Sam Trenholme <rpmbuild@maradns.org>
- MaraDNS rpm package upped to version 0.5.13.  More info
  at http://www.maradns.org/changelog.html

* Sun Apr 22 2001 Sam Trenholme <rpmbuild@maradns.org>
- MaraDNS rpm package upped to version 0.5.12.  More info
  at http://www.maradns.org/changelog.html

* Fri Apr 20 2001 Sam Trenholme <rpmbuild@maradns.org>
- MaraDNS rpm package upped to version 0.5.10.  Details at
  http://www.maradns.org/changelog.html

* Fri Apr 20 2001 Sam Trenholme <rpmbuild@maradns,org>
- MaraDNS RPM package upped to version 0.5.09.  Go to www.maradns.org for
  full changelog.

* Thu Apr 19 2001 Sam Trenholme <rpmbuild@maradns.org>
- Initial RPM package of MaraDNS
      
