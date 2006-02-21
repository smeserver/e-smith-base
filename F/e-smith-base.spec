Summary: e-smith server and gateway - base module
%define name e-smith-base
Name: %{name}
%define version 4.15.9
%define release 03
Version: %{version}
Release: %{release}
License: GPL
Vendor: Mitel Networks Corporation
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch0: e-smith-base-4.15.9-ReconfigureMenuItem.patch
Packager: SME Server developers <bugteam@contribs.org>
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires: mod_auth_external
Requires: e-smith-lib >= 1.15.3-42
Requires: server-manager-images, server-manager
Requires: e-smith-formmagick >= 0.2.0
Requires: initscripts >= 6.67-1es17
Requires: e-smith-daemontools >= 1.7.1-04
Requires: perl(Locale::gettext)
Requires: perl(Crypt::Cracklib)
Requires: perl(Date::Manip)
Requires: perl(Data::UUID)
Requires: perl(Net::IPv4Addr)
Requires: kernel-utils
Requires: dbus
Requires: hal
Requires: acpid
Requires: apmd
Requires: whiptail
Requires: rssh
Requires: bridge-utils
Requires: vconfig
Requires: e-smith-bootloader
Requires: mdadm
Obsoletes: rlinetd, e-smith-mod_ssl
Obsoletes: e-smith-serial-console
Obsoletes: sshell
Obsoletes: e-smith-rp-pppoe
BuildRequires: perl, perl(Test::Inline) >= 0.12
BuildRequires: e-smith-devtools >= 1.13.1-03
%define dbfiles accounts configuration domains hosts networks
AutoReqProv: no

%description
e-smith server and gateway software - base module.

%changelog
* Mon Feb 21 2006 Gordon Rowell <gordonr@gormand.com.au> 4.15.9-03
- Change 'Reconfigure' to lower case in menu [SME: 2]

* Mon Feb 20 2006 Gordon Rowell <gordonr@gormand.com.au> 4.15.9-02
- Add requires for mdadm. We use it in the console and raid monitor
  and it won't get installed for 5.x upgrades [SME: 767]

* Fri Feb 17 2006 Gordon Rowell <gordonr@gormand.com.au> 4.15.9-01
- Roll patches to 4.15.8-60
- Trim changelog before 4.15.3-01 [SME: 828]

* Fri Feb 17 2006 Gordon Rowell <gordonr@gormand.com.au> 4.15.8-60
- Also rotate /var/log/anaconda.{log,syslog} in post-upgrade [SME: 808]

* Fri Feb 17 2006 Gordon Rowell <gordonr@gormand.com.au> 4.15.8-59
- Change 'Reconfigure' to lower case in -57 change [SME: 2]

* Fri Feb 17 2006 Gordon Rowell <gordonr@gormand.com.au> 4.15.8-58
- Add /root/upgrade.log and /root/upgrade.log.syslog to 
  logfiles2timestamp in post-upgrade event so we preserve 
  them across multiple upgrades [SME: 808]

* Fri Feb 17 2006 Gavin Weight <gweight@gmail.com> 4.15.8-57
- Added Reconfigure and Reboot option in console, changed
  main console menu to reflect Reconfigure option [SME: 2]

* Thu Feb 16 2006 Gordon Rowell <gordonr@gormand.com.au> 4.15.8-56
- Default EmailForward to 'local' in case that part of the panel
  is hidden from view [SME: 704]

* Thu Feb 16 2006 Gordon Rowell <gordonr@gormand.com.au> 4.15.8-55
- Adjust console title bar to 'SME Server' [SME: 726]
- Change title on "Choose administrator password" screens

* Mon Feb 13 2006 Mark Knox <mark_knox@mitel.com> 4.15.8-54
- Set EthernetDriver2 property when bonding is enabled [SME: 776]

* Mon Feb 13 2006 Gordon Rowell <gordonr@gormand.com.au> 4.15.8-53
- Remove cpuspeed.contrib ClearCase droppings [SME: 754]

* Sun Feb 12 2006 Charlie Brady <charlie_brady@mitel.com> 4.15.8-52
- Start bootstrap-console earlier - in particular before raidmonitor.
  Don't try to restart 'random'. [SME: 743]

* Sun Feb 12 2006 Charlie Brady <charlie_brady@mitel.com> 4.15.8-51
- Obsolete keytable service. [SME: 746]

* Sat Feb 11 2006 Shad L. Lords <slords@mail.com> 4.15.8-50
- Run kudzu -q from inittab [SME: 727]

* Tue Feb 9 2006 Charlie Brady <charlie_brady@mitel.com> 4.15.8-49
- Make bootp support optional, defaulting to 'deny'. [SME: 660]

* Thu Feb 9 2006 Gavin Weight <gweight@gmail.com> 4.15.8-48
- Removed the online-manual. [SME: 407]

* Thu Feb 9 2006 Gordon Rowell <gordonr@gormand.com.au> 4.15.8-47
- Hide email forwarding options on useraccounts page if there is 
  no 'smtpd' record [SME: 704]

* Wed Feb  8 2006 Charlie Brady <charlie_brady@mitel.com> 4.15.8-46
- Fix conversion of user shell from sshell to rssh. [SME: 699]

* Tue Feb 7 2006 Gordon Rowell <gordonr@gormand.com.au> 4.15.8-45
- Fix up location of 00openRW fragments from change 41 [SME: 659. 679]

* Mon Feb 6 2006 Gordon Rowell <gordonr@gormand.com.au> 4.15.8-44
- Change logic for determining RAID partitions in use [SME: 516]
- Add detailed output of the RAID state to messages log [SME: 516]

* Mon Feb 6 2006 Gordon Rowell <gordonr@gormand.com.au> 4.15.8-43
- Only say that a RAID device is clean if truly clean [SME: 516]
- Adjusted warning to say 'may be required' instead of 'is'

* Mon Feb 6 2006 Gordon Rowell <gordonr@gormand.com.au> 4.15.8-42
- Delete 'deny bootp' fragment from dhcpd.conf, reverting to
  default, which is to allow bootp. [SME: 660]

* Sun Feb  5 2006 Charlie Brady <charlie_brady@mitel.com> 4.15.8-41
- Use appropriate esmith::*DB class for 00openRW migrate fragments.
  [SME: 659]

* Tue Jan 31 2006 Gavin Weight <gweight@gmail.com> 4.15.8-40
- Added EmailForward migrate fragment [SME: 598]

* Tue Jan 31 2006 Gavin Weight <gweight@gmail.com> 4.15.8-39
- Added text periods and underscores in useraccounts [SME: 531]

* Tue Jan 31 2006 Gavin Weight <gweight@gmail.com> 4.15.8-38
- Updated copyright text in server-manager [SME: 459]

* Tue Jan 31 2006 Gavin Weight <gweight@gmail.com> 4.15.8-37
- The menu text incorrect for RAID5 configurations [SME: 404]

* Tue Jan 31 2006 Shad L. Lords <slords@mail.com> 4.15.8-36
- Disable zeroconf so 169.254.0.0/16 route isn't created [SME: 613]

* Sun Jan 29 2006 Charlie Brady <charlie_brady@mitel.com> 4.15.8-35
- Fix flip of access settings to default on first post-upgrade (e.g.
  sshd from public to private). [SME: 495]

* Sun Jan 29 2006 Charlie Brady <charlie_brady@mitel.com> 4.15.8-34
- Remove remnants of statustest. [SME: 450]

* Wed Jan 25 2006 Charlie Brady <charlie_brady@mitel.com> 4.15.8-33
- Add templated elinks config file. [SME: 444]

* Mon Jan 23 2006 Shad L. Lords <slords@mail.com> 4.15.8-32
- Help raidmonitor report more than just failures [SME: 496]

* Mon Jan 23 2006 Gordon Rowell <gordonr@gormand.com.au> 4.15.8-31
- Create ~/.ssh as part of skeleton home directory [SME: 456]

* Wed Jan 18 2006 Charlie Brady <charlieb@e-smith.com> 4.15.8-30
- Fix reboot problem when switching WAN from dynamic to static
  address. [SME: 500]

* Fri Jan 13 2006 Mark Knox <mark_knox@mitel.com> 4.15.8-29
- New migrate fragment to clean up NIC bonding property [SME: 449]

* Fri Jan 13 2006 Gordon Rowell <gordonr@gormand.com.au> 4.15.8-28
- Fix account regexp for set_password case [SME: 24]

* Wed Jan 11 2006 Mark Knox <mark_knox@mitel.com> 4.15.8-27
- New console option for ethernet bonding [SME: 449]

* Mon Jan  9 2006 Gordon Rowell <gordonr@gormand.com.au> 4.15.8-26
- Allow dot and underscore in account names [SME: 24]
- Default maxAcctNameLength and maxGroupNameLength to 31 [SME: 24]

* Thu Jan  5 2006 Charlie Brady <charlieb@e-smith.com> 4.15.8-25
- Avoid generating warning messages during interfaces migration
  template fragment. [SME: 354]

* Thu Jan  5 2006 Charlie Brady <charlieb@e-smith.com> 4.15.8-24
- Don't add obsolete ipsec net-pf aliases to modprobe.conf, and
  remove them if found. [SME: 390]

* Sun Jan 2 2006 Charlie Brady <charlieb@e-smith.com> 4.15.8-23
- Use regexp as well as cracklib to check admin password in console.
  [SME: 335]

* Mon Jan 2 2006 Gordon Rowell <gordonr@gormand.com.au> 4.15.8-22
- Change heuristic for finding disks in manageRAID.pl [SME: 342]

* Sat Dec 25 2005 Gordon Rowell <gordonr@gormand.com.au> 4.15.8-21
- Move testInternet console menu item to smeserver-support [SME: 364]

* Fri Dec 16 2005 Charlie Brady <charlieb@e-smith.com> 4.15.8-20
- Fix localization bug in add_mirror. [SME: 341]

* Thu Dec 15 2005 Gordon Rowell <gordonr@gormand.com.au> 4.15.8-19
- Remove the "In eight seconds" untruth from shutdown/reboot [SME: 86]

* Thu Dec 15 2005 Gordon Rowell <gordonr@gormand.com.au> 4.15.8-18
- Added modSSL{CipherSuite} default [SME: 194]

* Wed Dec 14 2005 Gordon Rowell <gordonr@gormand.com.au> 4.15.8-17
- Enable microcode_ctl service by default [SME: 74]

* Wed Dec 14 2005 Gordon Rowell <gordonr@gormand.com.au> 4.15.8-16
- Removed accounts db default for 'common'
- Added accounts db defaults for server-common and server-resources [SME: 77]

* Wed Dec 14 2005 Gordon Rowell <gordonr@gormand.com.au> 4.15.8-15
- Ensure that Nameservers==localhost is set for the primary domain [SME: 137]

* Wed Dec 14 2005 Gordon Rowell <gordonr@gormand.com.au> 4.15.8-14
- And remove db defaults for sysstat service [SME: 327]

* Wed Dec 14 2005 Gordon Rowell <gordonr@gormand.com.au> 4.15.8-13
- Remove sysstat startup symlink [SME: 327]

* Wed Dec 14 2005 Gordon Rowell <gordonr@gormand.com.au> 4.15.8-12
- Default sysconfig{PreviousSystemMode} == unknown [SME: 75]

* Wed Dec 14 2005 Gordon Rowell <gordonr@gormand.com.au> 4.15.8-11
- Remove Requires: sysstat [SME: 327]

* Sat Dec 10 2005 Charlie Brady <charlieb@e-smith.com> 4.15.8-10
- Move code for testing internet access into menu item file.
  [SME: 261]

* Thu Dec 8 2005 Charlie Brady <charlieb@e-smith.com> 4.15.8-09
- Fix looping in console at swap ethernet choice page. [SME: 68]

* Wed Dec 7 2005 Gordon Rowell <gordonr@gormand.com.au> 4.15.8-08
- Fix taint issues with RAID management menu item [SME: 253]

* Mon Dec 05 2005 Filippo Carletti <carletti@mobilia.it> 4.15.8-07
- console: DHCP range (wrong path chosen for non-English) [SME: 157]

* Fri Dec 2 2005 Gordon Rowell <gordonr@gormand.com.au> 4.15.8-06
- Initial cut at console menu item to (re)add RAID-1 mirror [SME: 253]
- Needs to move to /sbin/e-smith/console-menu-items, once I work out
  what I believe is a taint issue.

* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au> 4.15.8-05
- Change 'standby' to 'stand by' in console [SME: 66]

* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au> 4.15.8-04
- Fix routing on eth0 for multiple local networks [SME: 203]

* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au> 4.15.8-03
- Bump release number only

* Mon Nov 28 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.8-02]
- Re-import head to CVS.
- Regenerate both key and cert when cert expires, not just crt. [SF: 1365965]

* Sun Nov 20 2005 Gordon Rowell <gordonr@e-smith.com>
- [4.15.8-01]
- Default cpuspeed to disabled [MN00107779]

* Wed Nov 16 2005 Mark Knox <mark_knox@mitel.com>
- [4.15.7-01]
- Imported to ClearCase
- Changed console sort order from ASCII to numeric [MN00107120]

* Sun Nov 13 2005 Gordon Rowell <gordonr@e-smith.com>
- [4.15.6-09]
- Add -f option to add_mirror to allow use of disks with existing
  partition tables [MN00101667]

* Sun Nov 13 2005 Gordon Rowell <gordonr@e-smith.com>
- [4.15.6-08]
- Add reconfiguration reboot option to reboot panel [SF: 1349946]
- TODO: Cleanup so that the red warning header doesn't display since
  the reboot is going to happen anyway

* Mon Nov  7 2005 Gordon Rowell <gordonr@e-smith.com>
- [4.15.6-07]
- Only signal-event ip-change on the BOUND action of dhclient [SF: 1344853]

* Tue Nov  1 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.6-06]
- Change DISABLED -> OFF in init script messages, and go back to standard
  alignment. [SF: 1264702, 134543]

* Mon Oct 24 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.6-05]
- Add default value of SYSFONTACM to /etc/sysconfig/i18n. [SF: 1295293]

* Mon Oct 24 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.6-04]
- Replace grub setup commands in add_mirror with an exec of an external
  script. This script will be provided by a bootloader specific package,
  e.g. e-smith-lilo or e-smith-grub. That package should include a
  "Provides: e-smith-bootloader" header, to satisfy a Requires in this
  package. [SF: 1335937]

* Thu Oct 20 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.6-03]
- Unload network drivers immediately after rc.sysinit runs, so that
  we can control the order of allocation of eth0 and eth1. [SF: 1332366]

* Mon Oct 17 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.6-02]
- Disable raid monitor if /boot/grub/device.map suggests that the system
  is a single disk system. [SF: 1269091]

* Fri Oct 14 2005 Gordon Rowell <gordonr@e-smith.com>
- [4.15.6-01]
- Remove L10Ns from base packages [SF: 1309520]

* Fri Oct 14 2005 Gordon Rowell <gordonr@e-smith.com>
- [4.15.5-01]
- New dev stream before relocating L10Ns

* Thu Oct 13 2005 Gordon Rowell <gordonr@gormand.com.au>
- [4.15.4-52]
- Add /sbin/e-smith/add_mirror [SF: 1325479]

* Tue Oct 11 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.4-51]
- Untaint menu choice when ethernet driver is chosen from menu. [SF: 1323270]

* Tue Oct 11 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.4-50]
- Move user-create-unix action before template expansions, so
  that getpwnam can be used in template fragments. Ditto
  for group-create-unix. [SF. 1322231]

* Sun Oct  9 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.4-49]
- Fix spelling mistake in useraccounts panel. [SF: 1320002]

* Fri Sep 30 2005 Gordon Rowell <gordonr@e-smith.com>
- [4.15.4-48]
- Revised translation of groups panel, reordered to match
  the English lexicon - Thanks Didier Rambeau [SF: 1305184]

* Fri Sep 30 2005 Gordon Rowell <gordonr@e-smith.com>
- [4.15.4-47]
- Added foot.tmpl for Italian [SF: 1309266]

* Fri Sep 30 2005 Gordon Rowell <gordonr@e-smith.com>
- [4.15.4-46]
- Added Italian L10Ns - Thanks Filippo Carletti [SF: 1309266]

* Fri Sep 30 2005 Gordon Rowell <gordonr@e-smith.com>
- [4.15.4-45]
- Added Italian for Please wait - we should do this through gettext
  or similar [SF: 1309288]

* Thu Sep 29 2005 Gordon Rowell <gordonr@e-smith.com>
- [4.15.4-44]
- Reword Master DNS Server screen as "Corporated DNS Server", in
  line with domains panel [gordonr MN00096914]

* Mon Sep 26 2005 Gordon Rowell <gordonr@e-smith.com>
- [4.15.4-43]
- German L10Ns for userpassword and console - Thanks Dietmar Berteld 
  [SF: 1293325]

* Sun Sep 25 2005 Gordon Rowell <gordonr@e-smith.com>
- [4.15.4-42]
- Added German L10N - Thanks Dietmar Berteld [SF: 1293325]

* Sun Sep 25 2005 Gordon Rowell <gordonr@e-smith.com>
- [4.15.4-41]
- Added "de" to pleasewait ugliness case statement and
  sorted the list alphabetically [SF: 1293325]

* Fri Sep 23 2005 Gordon Rowell <gordonr@e-smith.com>
- [4.15.4-40]
- Convert [s]smtpfront-qmail to [s]smtpd in migrate fragment [SF: 1291265]

* Thu Sep 22 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.4-39]
- Add preliminary support for ethernet bonding on local interface.
- Modify user-modify-unix so that usermod is not called to change
  shell or GCOS field unless they need to change.

* Mon Sep 12 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.4-38]
- Update filelist entries for databases which have moved
  from /home/e-smith to /home/e-smith/db [SF: 1216546]

* Tue Sep  6 2005 Tony Clayton <apc@e-smith.com>
- [4.15.4-37]
- Create /mnt/floppy symlink if required in post-{install,upgrade}.
  [MN00095821]
- Haldaemon race conditions seem quite recalcitrant, so don't try to create
  /mnt/cdrom symlink. [SF: 1260322]
- Disable CTRL-C in console [tonyc SF: 1264697]
- Catch CTRL-C in console during Test Internet [tonyc SF: 1264697]

* Tue Sep  6 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.4-36]
- Rework user-group-modify to work around perl bug in getgrent(). [SF 1276553]

* Tue Sep  6 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.4-35]
- Also create /mnt/floppy symlink if required. [MN00095821]

* Mon Sep  5 2005 Gordon Rowell <gordonr@e-smith.com>
- [4.15.4-34]
- Re-add Master DNS Server console screen [gordonr MN00096910, MN00088222]

* Fri Sep  2 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.4-33]
- Fix race condition in /mnt/cdrom symlink creation, by creating
  symlink from haldaemon action. [SF: 1260322]

* Thu Sep  1 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.4-32]
- Really create /mnt/cdrom symlink if required.  [SF: 1260322]

* Tue Aug 30 2005 Shad Lords <slords@mail.com>
- [4.15.4-31]
- Update services entries to conform with RHEL4 services [SF: 1276479]

* Mon Aug 29 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.4-30]
- Correctly handle multiple net specification in ValidFrom for httpd-admin.
  [SF: 1273756]

* Tue Aug 23 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.4-29]
- Fix taint problem in license text in option 6 of the console menu.
  [SF: 1267284]

* Tue Aug 23 2005 Gordon Rowell <gordonr@gormand.com.au>
- [4.15.4-28]
- Respect Shell property of user accounts [SF: 1266706]

* Thu Aug 18 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.4-27]
- Modify /sbin/e-smith/service so that it runs /sbin/service unless
  runlevel is 7. [SF: 1237968]
- Only prefix /sbin/e-smith to PATH if user is root. [SF: 1250579]

* Tue Aug 16 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.4-26]
- Add Requires for bridge-utils and vconfig.

* Tue Aug 16 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.4-25]
- Add "Requires: rssh".

* Mon Aug 15 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.4-24]
- Update %ghost filelist entries for databases which have moved
  from /home/e-smith to /home/e-smith/db [SF: 1216546]

* Mon Aug 15 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.4-23]
- Create /mnt/cdrom symlink if required.  [SF: 1260322]

* Thu Aug 11 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.4-22]
- Add Requires: whiptail so that the out fork of whiptail from the
  newt package is installed on upgrade.

* Tue Aug  9 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.4-21]
- Add Requires: headers for all the additional standard daemons, to
  ensure they are installed on upgrade.

* Tue Aug  9 2005 Shad Lords <slords@mail.com>
- [4.15.4-20]
- Change httpd-admin access from local to localhost [SF: 1246986]
- Change console to use 980 instead of https to avoid warnings [SF: 1246182]
- tie console to new httpd-admin{TCPPort} property. [SF: 1246986]

* Tue Aug  2 2005 Shad Lords <slords@email.com>
- [4.15.4-19]
- Add TCPPort and access for httpd-admin [SF: 1246986]
- Fix UnsavedChanges in console [SF: 1245238]

* Thu Jul 28 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.4-18]
- Remove all use db_ API except in console (which will come later).

* Wed Jul 27 2005 Shad Lords <slords@mail.com>
- [4.15.4-17]
- Add systemid property to sysconfig db record. [SF: 1246367]

* Wed Jul 27 2005 Shad Lords <slords@mail.com>
- [4.15.4-16]
- Upgrade database APIs to latest standard.
- Move databases from /home/e-smith to /home/e-smith/db [SF: 1216546]

* Wed Jul 27 2005 Shad Lords <slords@mail.com>
- [4.15.4-15]
- Use https to access server-manager from console, to avoid redirect
  problems. [SF: 1246182]

* Wed Jul 27 2005 Shad Lords <slords@mail.com>
- [4.15.4-14]
- Remove hwconfig db default entry. [SF: 1246180]

* Wed Jul 27 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.4-13]
- Remove checking against 32 group limit from UI. Thanks to Gordon Rowell
  for the main patch. [SF: 1245421]

* Tue Jul 26 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.4-12]
- Patches from Shad Lords.
- Complete fix of user password validation started in 4.15.3-06.
  [SF: 1242098]
- Change default password strength to "strong". [SF: 1246178]

* Tue Jul 19 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.4-11]
- Patches submitted by Gordon Rowell.
- Change /etc/modules.conf templates to /etc/modprobe.conf
  and add templates.metadata/etc/modprobe.conf [SF: 1227251]
- Remove fragments 10appletalk and 95ModulePaths, since they are
  for very old migrations of /etc/modules.conf

* Tue Jul 19 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.4-10]
- Move quota setup in fstab template into e-smith-quota, where it
  belongs.

* Tue Jul 12 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.4-09]
- Add default db entries for messagebus and haldaemon. [SF: 1225899]

* Tue Jul 12 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.4-08]
- Add messagebus and haldaemon services, so that cdrom mount point
  etc is created as required. [SF: 1225899]

* Fri Jul  8 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.4-07]
- Add miscelleous performance related standard RHEL/CentOS services.

* Thu Jul  7 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.4-06]
- Add RAID monitoring service. [SF: 1222143]

* Tue Jul  5 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.4-05]
- Fix log noise from DynDNS update script. [SF: 1231871]

* Fri Jun 24 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.4-04]
- Change default domain name setting - I'm sure that xxx is deprecated.

* Tue Jun 21 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.4-03]
- Deal gracefully with missing /etc/sysconfig/keyboard file.

* Tue Jun 21 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.4-02]
- Remove "random" service startup symlink - no longer required, as
  prng is seeded by rc.sysinit.

* Tue Jun 21 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.4-01]
- Make new development stream - 4.15.4

* Mon Jun 20 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.3-07]
- Move httpd-admin logging from inside /var/log/httpd to /var/log/httpd-admin.
- Remove mouseconfig hack. [MN00057145]

* Fri Jun 17 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.3-06]
- Fix password strength checking of user passwords. [SF: 1222255]

* Thu Jun 16 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.3-05]
- Prefix /sbin/e-smith to $PATH, rather than append. [SF: 1222092]

* Tue Jun 14 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.3-04]
- Fix set-external-ip in case of missing ExternalIP db record. [SF: 1217877]

* Tue Jun 14 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.3-03]
- Remove smbpasswd references from chap-secrets file. Don't re-expand
  chap-secrets file during various user related events. [SF: 1215401]

* Tue Jun 14 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.3-02]
- Break up template for /etc/shells into fragments, and add
  /usr/bin/rssh. [SF: 1220145]

* Thu Jun  9 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.3-01]
- Roll new development stream - 4.15.3

%prep
%setup
%patch0 -p1

%pre
if [ -d /etc/e-smith/locale/fr-ca -a ! -L /etc/e-smith/locale/fr-ca ]
then
    cd /etc/e-smith/locale

    [ -L fr ] && rm fr
    mkdir fr
    mv fr-ca/* fr
    rmdir fr-ca
fi

[ ! -L /etc/e-smith/locale/fr-ca ] && ln -s fr /etc/e-smith/locale/fr-ca

/sbin/e-smith/create-system-user smelog 1002 \
    'smelog log user' /var/log/smelog /bin/false
/sbin/e-smith/create-system-user smelastsys 2999 \
    'sme last system user marker' /tmp /bin/false

%post

%build
# Force creation of potentially empty directories
mkdir -p root/etc/e-smith/licenses
mkdir -p root/etc/e-smith/skel/user/.ssh
mkdir -p root/etc/e-smith/skel/user/home
mkdir -p root/etc/e-smith/skel/user/Maildir/{cur,new,tmp}
mkdir -p root/etc/e-smith/skel/e-smith/files/users
mkdir -p root/etc/e-smith/skel/e-smith/files/users/admin/home
mkdir -p root/etc/e-smith/skel/e-smith/files/primary/{cgi-bin,files,html}
mkdir -p root/etc/e-smith/skel/e-smith/Maildir/{cur,new,tmp}
mkdir -p root/etc/e-smith/templates{,-custom,-user,-user-custom}
mkdir -p root/etc/e-smith/web/{common,functions}
mkdir -p root/etc/e-smith/web/panels/manager/{cgi-bin,html}
mkdir -p root/etc/e-smith/web/panels/password/{cgi-bin,html}
mkdir -p root/etc/httpd/admin-conf/users
mkdir -p root/home/e-smith/files/{users,server-resources}
mkdir -p root/home/e-smith/files/users/admin/home
mkdir -p root/home/e-smith/Maildir/{cur,new,tmp}
mkdir -p root/root/.ssh
mkdir -p root/var/log/diald
mkdir -p root/var/state/httpd

LEXICONS=$(find root/etc/e-smith/web/{functions,panels/password/cgi-bin} \
    -type f | grep -v CVS | grep -v pleasewait)

for lexicon in $LEXICONS
do
    /sbin/e-smith/validate-lexicon $lexicon
done

/sbin/e-smith/generate-lexicons

perl createlinks
/sbin/e-smith/buildtests 10e-smith-base
ln -s /etc/rc.d/rc.local root/etc/rc.d/init.d/local
mkdir -p root/etc/rc6.d
mkdir -p root/etc/rc.d/rc7.d
ln -s /etc/rc.d/rc7.d root/etc/rc7.d
# Improve "telinit 1 behaviour
mkdir -p root/etc/rc.d/rc1.d

# Add shutdown symlink for diald
ln -s ../init.d/diald root/etc/rc6.d/K90diald
mkdir -p root/usr/share/locale/en_US/LC_MESSAGES
xgettext -o root/usr/share/locale/en_US/LC_MESSAGES/server-console.po root/sbin/e-smith/console
xgettext -o root/usr/share/locale/en_US/LC_MESSAGES/foot.tmpl.po root/etc/e-smith/templates/etc/e-smith/web/common/foot.tmpl/25Copyright
# make header/footer symlinks
ln -s head.tmpl root/etc/e-smith/web/common/userpassword_head.tmpl
ln -s head.tmpl root/etc/e-smith/web/common/noframes_head.tmpl
ln -s foot.tmpl root/etc/e-smith/web/common/noframes_foot.tmpl

mkdir -p root/etc/e-smith/locale
# Make the fr-ca link in %pre to ease upgrades
# ln -s fr root/etc/e-smith/locale/fr-ca 
ln -s en-us root/etc/e-smith/locale/en

for file in index initial
do
    ln -s ../../../functions/${file}.cgi root/etc/e-smith/web/panels/manager/html/${file}.cgi
done

ln -s ../../var/state/httpd root/etc/httpd/state

mkdir -p root/etc/e-smith/templates/etc/dhcpc/dhcpcd.exe
ln -s /etc/e-smith/templates-default/template-begin-shell \
      root/etc/e-smith/templates/etc/dhcpc/dhcpcd.exe/template-begin

for file in masq diald
do
    mkdir -p root/etc/e-smith/templates/etc/rc.d/init.d/$file
    ln -s /etc/e-smith/templates-default/template-begin-shell \
      root/etc/e-smith/templates/etc/rc.d/init.d/$file/template-begin
done

for file in ftp imap login passwd
do
    mkdir -p root/etc/e-smith/templates/etc/pam.d/$file
    ln -s /etc/e-smith/templates-default/template-begin-pam \
      root/etc/e-smith/templates/etc/pam.d/$file/template-begin
done

mkdir -p root/etc/e-smith/templates/etc/statusreport
ln -s /etc/e-smith/templates-default/template-begin-perl \
      root/etc/e-smith/templates/etc/statusreport/template-begin

mkdir -p root/service
mkdir -p root/etc/rc.d/init.d/supervise

for service in dhcpd dhcpcd syslog klogd httpd-admin
do
  ln -s /var/service/$service root/service/$service
  mkdir -p root/var/service/$service/supervise
  touch root/var/service/$service/down
  if [ -d root/var/service/$service/log ]
  then
    mkdir -p root/var/service/$service/log/supervise
    mkdir -p root/var/log/$service
  fi
  ln -s ../daemontools root/etc/rc.d/init.d/supervise/$service
done

# Remove (for now) supervised syslog and klogd services
rm root/etc/rc.d/init.d/supervise/{syslog,klogd}
rm root/service/{syslog,klogd}

mkdir -p root/etc/e-smith/events/local
mkdir -p root/etc/e-smith/events/user-modify-admin
mkdir -p root/home/e-smith/db
touch root/home/e-smith/db/configuration

mkdir -p root/etc/e-smith/pam
mkdir -p root/home/e-smith/ssl.key
mkdir -p root/home/e-smith/ssl.crt
mkdir -p root/home/e-smith/ssl.pem

mkdir -p root/var/state/e-smith

for file in %{dbfiles}
do
    mkdir -p root/etc/e-smith/db/$file/{defaults,migrate,force}
    # Create ghost file for rpm
    touch root/home/e-smith/db/$file
done

mkdir -p root/etc/tcprules

mkdir -p root/service
ln -s /var/service/pppoe root/service/pppoe

mkdir -p root/var/service/pppoe/supervise
touch root/var/service/pppoe/down

mkdir -p root/var/service/pppoe/log/supervise

mkdir -p root/var/log/pppoe

ln -s /var/service/raidmonitor root/service/raidmonitor

mkdir -p root/var/service/raidmonitor/supervise
touch root/var/service/raidmonitor/down

mkdir -p root/var/service/raidmonitor/log/supervise

mkdir -p root/var/log/raidmonitor

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
    --file /etc/cron.daily/conf-mod_ssl 'attr(0544,root,root)' \
    --file /etc/rc.d/rc.e-smith 'attr(0750,root,root)' \
    --dir /var/service/dhcpd 'attr(01755,root,root)' \
    --file /var/service/dhcpd/down 'attr(0644,root,root)' \
    --file /var/service/dhcpd/run 'attr(0755,root,root)' \
    --dir /var/service/dhcpd/log 'attr(0755,root,root)' \
    --dir /var/service/dhcpd/log/supervise 'attr(0700,root,root)' \
    --dir /var/service/dhcpd/supervise 'attr(0700,root,root)' \
    --file /var/service/dhcpd/log/run 'attr(0755,root,root)' \
    --dir /var/log/dhcpd 'attr(2750,smelog,smelog)' \
    --dir /var/service/dhcpcd 'attr(01755,root,root)' \
    --file /var/service/dhcpcd/down 'attr(0644,root,root)' \
    --file /var/service/dhcpcd/run 'attr(0755,root,root)' \
    --dir /var/service/dhcpcd/log 'attr(0755,root,root)' \
    --dir /var/service/dhcpcd/log/supervise 'attr(0700,root,root)' \
    --dir /var/service/dhcpcd/supervise 'attr(0700,root,root)' \
    --file /var/service/dhcpcd/log/run 'attr(0755,root,root)' \
    --dir /var/log/dhcpcd 'attr(2750,smelog,smelog)' \
    --file /home/e-smith/db/configuration 'config(noreplace)' \
    --dir /var/service/httpd-admin 'attr(01755,root,root)' \
    --file /var/service/httpd-admin/down 'attr(0644,root,root)' \
    --file /var/service/httpd-admin/run 'attr(0755,root,root)' \
    --dir /var/service/httpd-admin/log 'attr(0755,root,root)' \
    --dir /var/service/httpd-admin/log/supervise 'attr(0700,root,root)' \
    --dir /var/service/httpd-admin/supervise 'attr(0700,root,root)' \
    --file /var/service/httpd-admin/log/run 'attr(0755,root,root)' \
    --dir /var/log/httpd-admin 'attr(0750,smelog,smelog)' \
    --dir /var/service/raidmonitor 'attr(01755,root,root)' \
    --file /var/service/raidmonitor/down 'attr(0644,root,root)' \
    --file /var/service/raidmonitor/run 'attr(0755,root,root)' \
    --dir /var/service/raidmonitor/log 'attr(0755,root,root)' \
    --dir /var/service/raidmonitor/log/supervise 'attr(0700,root,root)' \
    --dir /var/service/raidmonitor/supervise 'attr(0700,root,root)' \
    --file /var/service/raidmonitor/log/run 'attr(0755,root,root)' \
    --dir /var/log/raidmonitor 'attr(2750,smelog,smelog)' \
    --file /var/service/syslog/run 'attr(0755,root,root)' \
    --file /var/service/syslog/down 'attr(0644,root,root)' \
    --file /var/service/klogd/run 'attr(0755,root,root)' \
    --file /var/service/klogd/down 'attr(0644,root,root)' \
    --dir /etc/e-smith/pam 'attr(0700,root,root)' \
    --dir /home/e-smith/ssl.key 'attr(0700,root,root)' \
    --dir /home/e-smith/ssl.crt 'attr(0700,root,root)' \
    --dir /home/e-smith/ssl.pem 'attr(0700,root,root)' \
    --dir /var/service/pppoe 'attr(1755,root,root)' \
    --file /var/service/pppoe/down 'attr(0644,root,root)' \
    --file /var/service/pppoe/run 'attr(0755,root,root)' \
    --dir /var/service/pppoe/supervise 'attr(0700,root,root)' \
    --dir /var/service/pppoe/log 'attr(1755,root,root)' \
    --file /var/service/pppoe/log/run 'attr(0755,root,root)' \
    --dir /var/service/pppoe/log/supervise 'attr(0700,root,root)' \
    --dir /var/log/pppoe 'attr(2750,qmaill,nofiles)' \
    --dir /etc/e-smith/skel/user/.ssh 'attr(0700,root,root)' \
    > %{name}-%{version}-%{release}-filelist

mkdir -p $RPM_BUILD_ROOT/home/e-smith/db
for file in %{dbfiles}
do
    # Create ghost file for rpm
    touch $RPM_BUILD_ROOT/home/e-smith/db/$file
    echo "%config %attr(0640,root,admin) /home/e-smith/db/$file" \
        >> %{name}-%{version}-%{release}-filelist
done
echo "%doc COPYING"          >> %{name}-%{version}-%{release}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)