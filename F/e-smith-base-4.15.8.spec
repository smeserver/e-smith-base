Summary: e-smith server and gateway - base module
%define name e-smith-base
Name: %{name}
%define version 4.15.8
%define release 46
Version: %{version}
Release: %{release}
License: GPL
Vendor: Mitel Networks Corporation
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch0: e-smith-base-4.15.8-02.mitel_patch
Patch1: e-smith-base-4.15.8-routeethX.patch
Patch2: e-smith-base-4.15.8-standby.patch
Patch3: e-smith-base-4.15.8-manageRAID.patch
Patch4: e-smith-base-4.15.8-DHCP_console.patch
Patch5: e-smith-base-4.15.8-manageRAID.patch2
Patch6: e-smith-base-4.15.8-console_loop.patch
Patch7: e-smith-base-4.15.8-testInternet.patch
Patch8: e-smith-base-4.15.8-DefaultPreviousSystemMode.patch
Patch9: e-smith-base-4.15.8-sysstat.patch
Patch10: e-smith-base-4.15.8-sysstat.patch2
Patch11: e-smith-base-4.15.8-SystemDomainNameservers.patch
Patch12: e-smith-base-4.15.8-URLreservations.patch
Patch13: e-smith-base-4.15.8-microcode_ctl.patch
Patch14: e-smith-base-4.15.8-CipherSuite.patch
Patch15: e-smith-base-4.15.8-EightSeconds.patch
Patch16: e-smith-base-4.15.8-add_mirror.l10n.patch
Patch17: smith-base-4.15.8-testInternet.patch2
Patch18: e-smith-base-4.15.8-DiskHeuristic.patch
Patch19: e-smith-base-4.15.8-admin.passwd.check.patch
Patch20: e-smith-base-4.15.8-net-fp-aliases.patch
Patch21: e-smith-base-4.15.8-interface.migration.patch
Patch22: e-smith-base-4.15.8-DotUnderscoreUsers.patch
Patch23: e-smith-base-4.15.8-bonding.patch
Patch24: e-smith-base-4.15.8-setpasswordregexp.patch
Patch25: e-smith-base-4.15.8-bonding2.patch
Patch26: e-smith-base-4.15.8-restart.patch
Patch27: e-smith-base-4.15.8-mdadm.patch
Patch28: e-smith-base-4.15.8-elinks.conf.patch
Patch29: e-smith-base-4.15.8-no.statusreport.patch
Patch30: e-smith-base-4.15.8-access.defaults.patch
Patch31: e-smith-base-4.15.8-zeroconf.patch
Patch32: e-smith-base-4.15.8-raid1text.patch
Patch33: e-smith-base-4.15.8-copyrightupdated.patch
Patch34: e-smith-base-4.15.8-usertext.patch
Patch35: e-smith-base-4.15.8-emailforwardmigration.patch
Patch36: e-smith-base-4.15.8-openRW.patch
Patch37: e-smith-base-4.15.8-AllowBootp.patch
Patch38: e-smith-base-4.15.8-manageRAID.patch3
Patch39: e-smith-base-4.15.8-manageRAID.patch4
Patch40: e-smith-base-4.15.8-openRW.patch2
Patch41: e-smith-base-4.15.8-shell.patch
Packager: SME Server developers <bugteam@contribs.org>
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires: mod_auth_external
Requires: e-smith-lib >= 1.15.1-19
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

* Thu Jun  9 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-93]
- Fix garbage output from 95ModulesPath fragment of modules.conf
  template.

* Wed Jun  8 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-92]
- Remove obsolete setting of path in modules.conf - "updates" is
  now implicitly searched first.

* Wed Jun  8 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-91]
- Remove default for ExternalIP - it serves no purpose, and confuses
  people. [SF: 1216822]

* Tue Jun  7 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-90]
- Fix errors in syslogd.conf/70Console template fragment.

* Tue Jun  7 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-89]
- Don't bother to create unneeded panels/{manager,password}/common
  directories.

* Tue Jun  7 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-88]
- Remove duplicated creation of httpd-admin start symlink.
- Fix handling of /server-manager/navigation and
  /server-manager/support URLs
- Update head.tmpl to use /server-manager/navigation URL.
- Remove bogus ScriptAlias of /cgi-bin URLs.
- Use full http URL in server-manager access from console.

* Tue Jun  7 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-87]
- Resolve duplication of webmail db default fragments (leave them
  here, and delete from e-smith-imp).

* Wed Jun  1 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-86]
- Add default "Shell" property for admin account.

* Wed Jun  1 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-85]
- Write only critical messages to syslog with sync. [MN00086487]
- Add optional support for syslog to a VT.

* Tue May 31 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-84]
- Fix /etc/sysconfig/i18n munging. [SF: 1189222]

* Tue May 31 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-83]
- Add template to "clean up" /etc/sysconfig/i18n (i.e. remove UTF-8
  references), to  work around console display issues.
  [SF: 1189222,1189223,1210923,1211167]
- do further cleanup of admin web server namespace (return /common,
  /e-smith-*, /server-brand).  [SF: 1172203]
- Fix noframes manager access. [SF: 1210715]

* Wed May 25 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-82]
- Ensure that /etc/e-smith/events/local directory exists.

* Wed May 25 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-81]
- Remove restart of syslogd during bootstrap-console-save. We no longer
  need it, and it's troublesome. [SF: 1208769]

* Wed May 25 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-80]
- Replace sysconfig-update action with a migrate fragment, and strip
  any trailing .UTF-8 from the language tag. [SF: 1189222]

* Wed May 25 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-79]
- Fix dangling /etc/cron.daily/conf-mod_ssl symlink (replace
  with script). [SF: 1204759]

* Tue May 24 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-78]
- Fix "back" button from Local IP entry dialog. [SF: 1207521]

* Tue May 17 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-77]
- Add 'll' section to inittab template, so that "signal-event local"
  is run at the appropriate time. The avoids a fork or templating of
  the rc.local script from initscripts.

* Mon May 16 2005 Mark Knox <markk@e-smith.com>
- [4.15.2-76]
- Do not twiddle the serial-console settings [markk MN00084537]

* Fri May 13 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-75]
- Add in all content from e-smith-rp-pppoe.

* Thu May 12 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-74]
- A few bugfixes from Gordon (in group management).

* Mon May  9 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-73]
- Fix migration of interface name if "swapped" and "serveronly" are
  both set.
- Delete unused expansion of lo:0 interface configuration file.

* Fri May  6 2005 Mark Knox <markk@e-smith.com>
- [4.15.2-72]
- Include updates in module load path [markk MN00081876]

* Thu May  5 2005 Mark Knox <markk@e-smith.com>
- [4.15.2-71]
- Set ENV{TERM} if one is specified in the serial-console properties [markk
  73183]

* Sun Apr 24 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-70]
- Update copyright date displayed in panel footers.

* Fri Apr 15 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-69]
- Fix problem with user-group-modify running group-modify with an
  empty group list (if adding user who belongs to no groups).
  
* Thu Apr 14 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-68]
- Can't open accounts db R/O in user-lock-passwd. Remove
  unneeded esmith::util.

* Wed Apr 13 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-67]
- Add default fragments for passwordstrength settings.
- Unroll cascaded group modify events from user-{create,modify,delete}
  events.

* Mon Apr 11 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-66]
- Remove troublesome -T flag from user-group-modify action. TODO:
  fix the underlying problem.
- Only migrate users with shell of /bin/sshell to /usr/bin/rssh.
- Add "authoritative" to template for dhcpd.conf.

* Fri Apr  1 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-65]
- Rotate logfiles during post-install/post-upgrade, rather than during
  bootstrap-console-save. That'll make bootup issues easier to debug.

* Fri Apr  1 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-64]
- Fix typo in reset-unsavedflag

* Fri Apr  1 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-63]
- Set default user shell to /usr/bin/rssh. User can have non-default
  shell by setting 'Shell' property of user account record. Shell for
  all users is updated during post-update event. [MN00063796]

* Fri Apr  1 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-62]
- Replace e-smith, inc copyright notices with Mitel ones
  in all action scripts.
- Remove all use of deprecated esmith::config and esmith::db
  APIs in action scripts.

* Thu Mar 31 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-61]
- Avoid a couple of warnings from network startup scripts.

* Wed Mar 30 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-60]
- Add default TCPPort and access properties to modSSL "service", so
  that appropriate firewall holes are created.

* Wed Mar 30 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-59]
- Migrate /etc/sysconfig/static-routes into network-scripts/route-ethX files.
  [MN00061314]

* Thu Mar 24 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-58]
- Add httpd-admin reconfiguration to remoteaccess-update event,
  as ValidFrom may have changed.

* Thu Mar 24 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-57]
- Fix processTemplate() calls in SSL cert template fragments.

* Tue Mar 22 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-56]
- Avoid addition of newline every time SSL cert file templates
  are expanded.

* Tue Mar 22 2005 Mark Knox <markk@e-smith.com>
- [4.15.2-55]
- Added Terminal property to serial-console record [markk MN00073183]

* Sun Mar 20 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-54]
- Remove obsolete conf-other action (and symlinks). Do log symlink
  rotation in bootstrap-console-save as well as logrotate.

* Fri Mar 18 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-53]
- Rewrite get_telnet_mode() so that warnings aren't generated when
  there is no telnet db record.

* Thu Mar 17 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-52]
- Fix a problem with SSL pem templates expansion.

* Thu Mar 17 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-51]
- Fix various problems with SSL key and crt template expansion.

* Thu Mar 17 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-50]
- Replace conf_mod_ssl action by templates.

* Thu Mar 17 2005 Mark Knox <markk@e-smith.com>
- [4.15.2-49]
- Use sysconfig{VlanWAN} if available in 10interfaces migrate fragment

* Tue Mar 15 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-48]
- Fix typo in createlinks script, which broke expansion of
  /etc/statusreports. Only expand /etc/statusreports in
  bootstrap-console-save.

* Mon Mar 14 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-47]
- Unroll some loops in createlinks script to allow for future optimisation.
- Remove rest-unsavedflag links for a couple of actions. [MN00074383]

* Fri Mar 11 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-46]
- Fix problem with reload of syslogd in logrotate event (typo).
  [MN00065576]

* Fri Mar 11 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-45]
- Avoid warning from expansion of dhcpd/config in serveronly mode.

* Thu Mar 10 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-44]
- Fold in various patches (mostly panel error checking fixes) from
  Shad Lord's 6.5 release.

* Thu Mar 10 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-43]
- Change default EmailUnknownUser from "return" to "returntosender".
  [MN00073740]
- Fix problem with cracklib validation of old password during attempt
  to change. [MN00073794]
- Back out smbpasswd change in user-delete, from 4.15.1-11, as it doesn't work
  correctly. [MN00035806]

* Thu Feb 24 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-42]
- Update Copyright date in console.
- Do probing for ethernet adaptors just once in console. [MN00069993]
- Remove VLAN confirmation - if user asks for servergateway and has
  single NIC, they get the vlan config. If user has only a single NIC,
  and doesn't have $sysconfig{VlanWAN} set in config, they are blocked
  from choosing s-g dedicated. [MN00069124]
- Don't duplicate ownership of /etc/httpd/conf/ssl.{key,crt} which
  are provided by mod_ssl.

* Wed Feb 23 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-41]
- Fix taint problems in displayManager() in console. [charlieb MN00061213]

* Tue Feb 22 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-40]
- Remove LAN driver choice screen if two NICs with same driver are detected.
  [MN00069124]

* Wed Feb 16 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-39]
- Remove now bogus klogd rc7.d link. [MN00061217]

* Wed Feb 16 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-38]
- Add ifcfg-eth0.4094 to templates2expand for bootstrap-console-save
  event. [MN00069124]

* Tue Feb 15 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-37]
- Restore a little more of conf-startup, so bootstrap-console runs correctly.
  [MN00056225]

* Tue Feb 15 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-36]
- Remove LAN driver choice screen if only a single NIC is detected.
  [MN00069124]
- Allow dialup WAN support in console to be disabled via a database
  property. [MN00069124]

* Tue Feb 15 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-35]
- Don't supervise (yet) syslogd and klogd. [MN00061217]
- Revert changes in bootstrap-console - not working well enough yet.
  [MN00056225]

* Mon Feb 14 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-34]
- Add console dialog to confirm VLAN configuration if dedicated server-gateway
  is chosen with a single ethernet interface. [MN00069124]

* Mon Feb 14 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-33]
- Fix typo in ifcfg-ethX template fragment. [MN00069124]

* Mon Feb 14 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-32]
- Make sure that ForceSave prop is set to "no" before running activate_config.
  [charlieb MN00056225]

* Mon Feb 14 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-31]
- Fix replacement of 00openRW file with a broken symlink. [MN00066635]

* Fri Feb 11 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-30]
- Add preliminary support for VLAN external interface [MN00069124]

* Fri Feb  4 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-29]
- Installer needs /home/e-smith/configuration, so remove %ghost
  specification. [MN00066635]

* Wed Feb  2 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-28]
- Change refs to server-manager and user-password to https:// [MN00067147]
- Move /home/e-smith/* from e-smith-base. [MN00066635]
- Change console mode default to login, and remove console mode and upstream
  proxy questions from console. [MN00067162, MN00066408]

* Wed Jan 26 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-27]
- Avoid warning from 10SetAccessDefaults migration fragment. [MN00064414]
- Fix device and file reference in ifcfg-eth1 template metadata.
  Fix template for ifcfg-lo:0 so that configuration is dependent
  on SystemMode being set to servergateway-publicserver. [MN00064130]
- Update e-smith-devtools dependency. [MN00065576]

* Tue Jan 25 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-26]
- Replace all restart-* and most reload-* actions with calls to 'adjust-services'.
  Update e-smith-lib version dependency. [MN00065576]

* Thu Jan 20 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-25]
- Change default status of ippp to disabled. Console will enable it if
  required. [MN00064441]
- Fix CustomLog directive. [MN00064132]
- Remove reference to Mitel support in "custom" dyndns menu option.
- Rename activate-config to activate_config.  [MN00056225]
- Remove obsolete clean-rc7.d script. [MN00064174]
- Remove redundant init-reload. [MN00064756]

* Mon Jan 17 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-24]
- Make further interim change in bootstrap-console. [charlieb MN00056225]
- Fix ownership of log directory for httpd-admin service. [charlieb MN00050083]
- Avoid warning message from SetAccessDefaults migrate fragment.
  [charlieb MN00064414]

* Mon Jan 17 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-23]
- Add generic_template_expand action to email-update event.
  [MN00064130]
- Fix removal of status reports screens from console. [MN00062553]

* Fri Jan 14 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-22]
- Fix conf-start script so that bootstrap-console is run on new
  install.  [charlieb MN00056225]

* Fri Jan 14 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-21]
- Remove contact details and status reports screens from console.
  [MN00062553]
- Add missing /etc/HOSTNAME template expansion. [MN00064130]
- Make further interim change in bootstrap-console. [charlieb MN00056225]
- Fix dangling conf-networking symlink. [MN00064130]

* Fri Jan 14 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-20]
- Remove default settings for obsoleted service "auth". [MN00064128]
- Use generic_template_expand action where possible, in place
  of specific actions. Update e-smith-lib dependency. [MN00064130]
- Take ownership of /etc/e-smith/pam, /home/e-smith/ssl.key and
  /home/e-smith/ssl.crt directories [MN00064131]
- Remove mangling of syslog and apache log filenames - just
  retargeting the symlinks has the same effect. [MN00064132]

* Wed Jan  5 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-19]
- Make further interim change in bootstrap-console. [charlieb MN00056225]

* Wed Jan  5 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-18]
- Make further interim change in bootstrap-console. [charlieb MN00056225]
- Add log directory for httpd-admin service. [charlieb MN00050083]
- Add rudimentary "service" command, which is db and supervise aware.
  [charlieb MN00062534]

* Wed Jan  5 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-17]
- Make further interim change in bootstrap-console. [charlieb MN00056225]

* Wed Jan  5 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-16]
- Add bogus /usr/sbin/mouseconfig symlink to clean up install [MN00057145]
- Start work on dhclient configuration. [MN00056716]

* Tue Jan  4 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-15]
- Remove reload-xinetd action [charlieb MN00061216]
- Fix more taint problems in set-admin-password and backup-in-progress.
  Rename backup-in-progress to restore-in-progress.
  Refactor bootstrap-console init script. [charlieb MN00056225]

* Wed Dec 29 2004 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-14]
- We don't need to reconf/reload httpd-admin if networks/users/groups
  are changed. [MN00051141]
- Fix taint problem in set-admin-password (and console), affecting
  password strength check. Activate set-admin-password console program
  during post-install.  [charlieb MN00056225]

* Tue Dec 28 2004 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-13]
- Add ddns-update-style directive to dhcpd.conf template -
  required for newer dhcpd. [charlieb MN00062560]
- Add "chpst -P" to httpd-admin run script, to protect runsv/supervise
  from term signals (wrongly) relayed by apache.  [charlieb MN00051144]

* Fri Dec 24 2004 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-12]
- Move daemontools init.d symlinks into init.d/supervise. [MN00061217]

* Wed Dec 22 2004 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-11]
- Remove unnecessary trap code and pidfile handling in dhcpd run script.
  [charlieb MN00050801]

* Thu Dec 16 2004 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-10]
- Supervise syslogd and klogd. [charlieb MN00061217]

* Thu Dec 16 2004 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-09]
- Move quota file creation stuff to e-smith-quota, where it belongs.
  [charlieb MN00061221]

* Tue Dec 14 2004 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-08]
- Fix taint problems in displayStatus() in console. [charlieb MN00061213]

* Tue Dec 14 2004 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-07]
- Remove xinetd configuration [charlieb MN00061216]

* Mon Dec 13 2004 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-06]
- Run /etc/rc.d/rc.quota_create before rc.sysinit. [charlieb MN00061221]

* Mon Dec 13 2004 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-05]
- Remove obsoleted /etc/pam.d/{imap,pop} templated files. [charlieb MN00061222]

* Fri Dec 10 2004 Mark Knox <markk@e-smith.com>
- [4.15.2-04]
- Updated copyright notices [markk MN00060958]

* Thu Nov 18 2004 Michael Soulier <msoulier@e-smith.com>
- [4.15.2-03]
- Set external interface to not ifup if dhcp is used. [msoulier MN00058005]

* Thu Nov 11 2004 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-02]
- Remove dangling conf-passwordstrength symlink in bootstrap-console-save
  event. [charlieb MN00057101]
- Untaint user and group and network names before using in system()
  in panel code. [charlieb MN00050161]

* Thu Nov 11 2004 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-01]
- Changing version to new development stream number - 4.15.2

* Thu Nov 11 2004 Charlie Brady <charlieb@e-smith.com>
- [4.15.1-29]
- Use config database away rc script for runlevels 0 and 6 as well.
  [charlieb MN00056823]
- Modify admin apache config for compatibility with apache 2. Most of these
  changes were contributed by Shad Lords. [charlieb MN00051144]

* Wed Nov 10 2004 Mark Knox <markk@e-smith.com>
- [4.15.1-28]
- Backed out fix for MN00055601 from 4.15.1-27 [markk]

* Wed Nov 10 2004 Charlie Brady <charlieb@e-smith.com>
- [4.15.1-25]
- Make sure that /etc/rc.d/rc.e-smith script has execute permission.
  [charlieb MN00056823]

* Wed Nov 10 2004 Charlie Brady <charlieb@e-smith.com>
- [4.15.1-24]
- Remove the obsolete /sbin/update fragment from /etc/inittab.
  [charlieb MN00056744]
- Remove obsolete keytable startup symlink [charlieb MN00056691]
- Set package in backup-in-progress and set-admin-password to esmith::console
  so that gettext() can be found. [charlieb MN00056225]
- Use rc.e-smith script for runlevel 7 startup rather than stock rc.
  [charlieb MN00056823]

* Tue Nov  9 2004 Charlie Brady <charlieb@e-smith.com>
- [4.15.1-23]
- Add activate-config backup-in-progress and set-admin-password programs.
  Not yet fully functional or integrated into startup. [charlieb MN00056225]
- Update run script for compatibility with apache2. [charlieb MN00051144]

* Mon Nov  8 2004 Charlie Brady <charlieb@e-smith.com>
- [4.15.1-22]
- Add empty default ValidFrom property for httpd-admin [charlieb MN00056429]
- Fix broken validators in userpassword panel [charlieb MN00055802]
- Fix broken validator in groups panel [charlieb MN00056279]

* Fri Nov  5 2004 Michael Soulier <msoulier@e-smith.com>
- [4.15.1-21]
- Removing migrateSwap fstab fragment. Decided we don't care about this case.
  [msoulier MN00055206]

* Thu Nov  4 2004 Michael Soulier <msoulier@e-smith.com>
- [4.15.1-20]
- Forward port of improved fstab swap partition migration.
  [msoulier MN00055206]

* Thu Nov  4 2004 Mark Knox <markk@e-smith.com>
- [4.15.1-19]
- Added check for valid record during add new user process, fixes missing
  button on validation failure [markk MN00055044]

* Mon Nov  1 2004 Michael Soulier <msoulier@e-smith.com>
- [4.15.1-17]
- Fixed syntax error in template. [msoulier MN00055206]

* Mon Nov  1 2004 Michael Soulier <msoulier@e-smith.com>
- [4.15.1-16]
- Added migration of a bad swap-file reference in fstab. [msoulier MN00055206]

* Tue Sep 21 2004 Mark Knox <markk@e-smith.com>
- [4.15.1-15]
- Back out hooks for remote manager access from AMC (dead code) [markk 
  MN00049735]

* Thu Sep  9 2004 Michael Soulier <msoulier@e-smith.com>
- [4.15.1-13]
- Re-roll after upgrade of perl-Test-Inline. [msoulier MN00048140]

* Thu Sep  9 2004 Michael Soulier <msoulier@e-smith.com>
- [4.15.1-12]
- Updated buildrequires with new perl dependency format. [msoulier MN00040240]
- Clean BuildRequires. [charlieb MN00043055]
- Fixed bad call in remoteaccess.pm [msoulier MN00048140]

* Fri Sep  3 2004 Michael Soulier <msoulier@e-smith.com>
- [4.15.1-11]
- Added deletion of user from smbpasswd on user-delete. [msoulier MN00035806]

* Mon Aug 30 2004 Michael Soulier <msoulier@e-smith.com>
- [4.15.1-10]
- Added audit of the hosts db on local networks removal.
  [msoulier MN00036006]

* Thu Aug 26 2004 Michael Soulier <msoulier@e-smith.com>
- [4.15.1-09]
- Added localisation for CANCEL in localnetworks panel. [msoulier MN00036146]

* Fri Aug 20 2004 Michael Soulier <msoulier@e-smith.com>
- [4.15.1-08]
- Updated perl dependencies to new format.

* Fri Aug 20 2004 Michael Soulier <msoulier@e-smith.com>
- [4.15.1-07]
- Added dependency to perl Date::Manip module. [msoulier MN00046144]

* Fri Aug 20 2004 Michael Soulier <msoulier@e-smith.com>
- [4.15.1-06]
- Updated conf-mod_ssl to check the expiry date on the cert.
  [msoulier MN00046144]

* Wed Aug  4 2004 Michael Soulier <msoulier@e-smith.com>
- [4.15.1-05]
- Backed-out changes to e-smith-service regarding svenable/disable.
  [msoulier MN00042616]

* Thu Jul 29 2004 Gordon Rowell <gordonr@e-smith.com>
- [4.15.1-04]
- Change default serial-console{BaudRate} to 19k2  [gordonr MN00044157]

* Thu Jul  8 2004 Michael Soulier <msoulier@e-smith.com>
- [4.15.1-03]
- Updated console to report the driver that failed to load.
  [msoulier MN00021437]

* Mon May 10 2004 Michael Soulier <msoulier@e-smith.com>
- [4.15.1-02]
- Added to validation of forwarding address in useraccounts panel, such that
  it may only be blank if the forwarding setting is local.
  [msoulier MN00032671]

* Mon May 10 2004 Michael Soulier <msoulier@e-smith.com>
- [4.15.1-01]
- Added PermitPlainTextAccess property to httpd-admin, defaulting to no.
  [msoulier MN00020885]

* Thu May  6 2004 Michael Soulier <msoulier@e-smith.com>
- [4.15.0-41]
- s/Mitel Networks/Mitel/ [msoulier MN00024635]

* Wed May  5 2004 Michael Soulier <msoulier@e-smith.com>
- [4.15.0-40]
- Fixed red success of locking account. [msoulier MN00027892]

* Fri Apr  2 2004 Tony Clayton <apc@e-smith.com>
- [4.15.0-39]
- s/enable/svenable/,s/disable/svdisable/ for supervise status [tonyc 9170]
- Bumping dependency on e-smith-daemontools to >= 1.7.1-04 [tonyc 9170]

* Thu Apr  1 2004 Tony Clayton <apc@e-smith.com>
- [4.15.0-38]
- Improve daemontools/e-smith-service integration in initscripts [tonyc 9170]
- Bumping dependency on e-smith-daemontools to >= 1.7.1-03 [tonyc 9170]

* Mon Feb 23 2004 Michael Soulier <msoulier@e-smith.com>
- [4.15.0-37]
- Added a modprobe test of ethernet drivers before accepting them.
  [msoulier dpar-21437]

* Wed Feb 18 2004 Michael Soulier <msoulier@e-smith.com>
- [4.15.0-36]
- Updated requires for e-smith-daemontools. [msoulier 7629]

* Wed Feb 18 2004 Michael Soulier <msoulier@e-smith.com>
- [4.15.0-35]
- Updated reload-httpd-admin to use the new sigusr1 option to daemontools.
  [msoulier 7629]

* Fri Jan 30 2004 Michael Soulier <msoulier@e-smith.com>
- [4.15.0-34]
- Moved the new column to the left to ensure the action links were last.
  [msoulier 9100]

* Fri Jan 30 2004 Michael Soulier <msoulier@e-smith.com>
- [4.15.0-33]
- Added a new column to the useraccounts panel to show the status of each
  user's vpn access. [msoulier 9100]

* Wed Jan 28 2004 Michael Soulier <msoulier@e-smith.com>
- [4.15.0-32]
- Added a trace option to masq, to toggle iptables-trace. [msoulier 8117]

* Mon Jan 19 2004 Michael Soulier <msoulier@e-smith.com>
- [4.15.0-31]
- Added additional 6.0 styling to success and error messages in the
  useraccounts panel. [msoulier 8787]

* Thu Jan 15 2004 Michael Soulier <msoulier@e-smith.com>
- [4.15.0-30]
- Added e-smith.sh to /etc/profile.d to modify the PATH. [msoulier 5740]

* Sat Dec 20 2003 Michael Soulier <msoulier@e-smith.com>
- [4.15.0-29]
- Added httpd-admin symlink creation to createlinks. [msoulier 10864]

* Tue Dec  9 2003 Michael Soulier <msoulier@e-smith.com>
- [4.15.0-28]
- Rewrote reload-httpd-admin for supervise. [msoulier 7629]

* Tue Dec  9 2003 Michael Soulier <msoulier@e-smith.com>
- [4.15.0-27]
- Trying reintroduction of supervise, using -F arg. Confused yet?
  [msoulier 7629]

* Tue Dec  9 2003 Michael Soulier <msoulier@e-smith.com>
- [4.15.0-26]
- Backout of supervise attempt. Must wait for apache 2.0. [msoulier 7629]

* Tue Dec  9 2003 Michael Soulier <msoulier@e-smith.com>
- [4.15.0-25]
- Fixed the lack of a config file arg in the run script. [msoulier 7629]

* Tue Dec  9 2003 Michael Soulier <msoulier@e-smith.com>
- [4.15.0-24]
- Fixed a quoting problem, and the path to httpd-admin. [msoulier 7629]

* Tue Dec  9 2003 Michael Soulier <msoulier@e-smith.com>
- [4.15.0-23]
- Additional tweaks on changes from previous change. [msoulier 7629]

* Tue Dec  9 2003 Michael Soulier <msoulier@e-smith.com>
- [4.15.0-22]
- First attempt to supervise httpd-admin. [msoulier 7629]

* Fri Dec  5 2003 Michael Soulier <msoulier@e-smith.com>
- [4.15.0-21]
- Changed signal to HUP in reload-xinetd. [msoulier 10749]

* Mon Dec  1 2003 Mark Knox <markk@e-smith.com>
- [4.15.0-20]
- Tweak previous mode detection in 10SetAccessDefaults [markk 10465]

* Tue Nov 25 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.15.0-19]
- Add defaults fragment for ${'serial-console'}{BaudRate} == 115200
- Use this property in /etc/inittab fragment [gordonr 5827]

* Tue Nov  4 2003 Michael Soulier <msoulier@e-smith.com>
- [4.15.0-18]
- Fixed a bad variable declaration. [msoulier 9811]

* Tue Nov  4 2003 Mark Knox <markk@e-smith.com>
- [4.15.0-17]
- Roll back broken fix for bug 9760 [markk 9760]

* Mon Nov  3 2003 Mark Knox <markk@e-smith.com>
- [4.15.0-16]
- Added some missing variable declarations [markk 9420]

* Mon Nov  3 2003 Mark Knox <markk@e-smith.com>
- [4.15.0-15]
- Added missing 'removed networks' messages in en/fr/es lexicons [markk 9420]

* Fri Oct 17 2003 Michael Soulier <msoulier@e-smith.com>
- [4.15.0-14]
- Added more directives to the lynx.cfg template fragments, mainly a HELPFILE
  directive to replace the default. [msoulier 10126]

* Thu Oct 16 2003 Michael Soulier <msoulier@e-smith.com>
- [4.15.0-13]
- Moved untie below the use of conf so that code has a point. [msoulier 9454]

* Thu Oct 16 2003 Michael Soulier <msoulier@e-smith.com>
- [4.15.0-12]
- Moved the Run=no again to SAVE_CONFIG. [msoulier 9454]

* Thu Oct 16 2003 Michael Soulier <msoulier@e-smith.com>
- [4.15.0-11]
- Moved the point where bootstrap-console Run is set to no, to prevent cases
  of the console coming up during boot interactively other than during
  install. [msoulier 9454]

* Fri Oct 10 2003 Mark Knox <markk@e-smith.com>
- [4.15.0-10]
- Changed a word in the warning message [markk 10420]

* Thu Oct  9 2003 Mark Knox <markk@e-smith.com>
- [4.15.0-09]
- Added a warning message on every panel when a reboot is needed [markk
  10420]

* Sun Sep 21 2003 Charlie Brady <charlieb@e-smith.com>
- [4.15.0-08]
- Incorporate optimization suggested by Gordon in e-smith-service script.
  [charlieb 9930]
- Use /etc/rc.d/init.d/supervise symlink for dhcpd, to avoid breaking
  verification of the RPM. Make use of esmith::Build::Createlinks in
  createlinks script while we are at it (add BuildRequires to enforce
  availability). [charlieb 10066]

* Sun Sep 21 2003 Charlie Brady <charlieb@e-smith.com>
- [4.15.0-07]
- Generalise rtl8139 driver migrate code to also handle old_tulip->tulip.
  [charlieb 9811]

* Tue Sep  9 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.15.0-06]
- Reserve 'primary' account as a system account, along with
  the 'Primary' ibay account [gordonr 9478]

* Fri Sep  5 2003 Charlie Brady <charlieb@e-smith.com>
- [4.15.0-05]
- Allow e-smith-service script to prefer supervise script
  to /etc/rc.d/init.d/ stock script. [charlieb 9930]

* Fri Sep  5 2003 Charlie Brady <charlieb@e-smith.com>
- [4.15.0-04]
- Remove DNS forwarder configuration page from console.
  [charlieb 9726]

* Tue Sep  2 2003 Charlie Brady <charlieb@e-smith.com>
- [4.15.0-03]
- Fix device name code in /etc/sysconfig/static-routes template.
  [charlieb 9876]

* Thu Aug 28 2003 Charlie Brady <charlieb@e-smith.com>
- [4.15.0-02]
- Add failsafe code to httpd-admin init script. [charlieb 9760]
- Add 6.0 styling changes to localnetworks panel. [charlieb 9420]

* Thu Aug 28 2003 Charlie Brady <charlieb@e-smith.com>
- [4.15.0-01]
- Changing version to development stream number - 4.15.0

* Wed Aug 27 2003 Michael Soulier <msoulier@e-smith.com>
- [4.14.1-04]
- Updated dhcpd and dhcpcd shutdown order, and added runlevel 1.
  [msoulier 9761]

* Mon Aug 25 2003 Michael Soulier <msoulier@e-smith.com>
- [4.14.1-03]
- Fixed error in symlink creation from last revision. [msoulier 9761]

* Mon Aug 25 2003 Michael Soulier <msoulier@e-smith.com>
- [4.14.1-02]
- Added K* symlinks for runlevels 0 and 6 for dhcpcd and dhcpd daemons.
  [msoulier 9761]

* Mon Jul 14 2003 Charlie Brady <charlieb@e-smith.com>
- [4.14.1-01]
- Roll new tarball to fix CVS patch breakage - 4.14.1

* Wed Jul  9 2003 Charlie Brady <charlieb@e-smith.com>
- [4.14.0-05]
- Start gettys after sysinit and before "rc" script. [charlieb 9344]

* Wed Jul  9 2003 Charlie Brady <charlieb@e-smith.com>
- [4.14.0-04]
- Start up tty2/tty3 and enable ctrlaltdel before running rcX script
  (especially, before the bootstrap-console). [charlieb 9344]
- Remove reload-httpd-admin and restart-masq from
  bootstrap-console-save event.  [charlieb 9338]

* Wed Jul  9 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.14.0-03]
- Start up tty2/tty3 before attempting to display the console [gordonr 9344]

* Wed Jul  9 2003 Michael Soulier <msoulier@e-smith.com>
- [4.14.0-02]
- Fixed broken caching of group details in groups panel. [msoulier 9230]

* Thu Jun 26 2003 Charlie Brady <charlieb@e-smith.com>
- [4.14.0-01]
- Changing version to stable stream number - 4.14.0

* Wed Jun 25 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.20-15]
- Revert 4.13.20-11 and fix 10SetAccessDefaults to handle
  6.0 upgrades correctly [gordonr 9000]

* Wed Jun 25 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.20-14]
- Ensure dhcpcd is disabled in serveronly mode [gordonr 8485]

* Tue Jun 24 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.20-13]
- Make sure to purge any Router property of new SystemLocalNetwork.
  [charlieb 9112]

* Tue Jun 24 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.20-12]
- Create system account for root [gordonr 9127]

* Mon Jun 23 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.20-11]
- Add sysconfig{PreviousSystemMode} default to ensure we don't
  migrate access setting to "defaults" on an upgrade [gordonr 9000]

* Mon Jun 23 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.20-10]
- Fix mismatch between function names and panel code in FTP section
  of remote access panel. [charlieb 9104]

* Thu Jun 19 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.20-09]
- Start masq after bootstrap-console has had a change to
  configure the script, and put masq|status default back to
  enabled [gordonr 9054]

* Wed Jun 18 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.20-08]
- Default masq|status to disabled until we've had time to configure
  from the console [gordonr 9054]
- Don't call conf-masq in post-{install,upgrade} - wait until
  we've configured from the console [gordonr 9054]

* Wed Jun 18 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.20-07]
- Create fr-ca -> fr symlink outside directory relocation
  %pre section [gordonr 9029]

* Tue Jun 17 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.20-06]
- s/Forwarder1/Forwarder/ in property name for DNS master setting.
  [charlieb 8745]

* Tue Jun 17 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.20-05]
- Fix conf-routes to use new library APIs, and to do as little as possible
  - only add or delete routes as required. [charlieb 8646]

* Fri Jun 13 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.20-04]
- Remove nameserver resolv.conf fragment, and DNS Forwarder migrate
  fragment now in e-smith-dnscache RPM. [charlieb 9032]

* Fri Jun 13 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.20-03]
- Don't blindly create /etc/smbpasswd - we're using 
  /etc/samba/smbpasswd now, and smbpasswd will create the file
  for us. Also delete unused libraries/conf ties [gordonr 8747]

* Thu Jun 12 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.20-02]
- Don't call groupadd/useradd - just let useradd do it [gordonr 4930]

* Thu Jun 12 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.20-01]
- Added order tags to migrate fragments [gordonr 9015]

* Thu Jun 12 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.19-01]
- Rename migrate/interfaces -> 10interfaces to allow order [gordonr 5053]

* Wed Jun 11 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.18-16]
- Add Lockable|no, Removable|no properties to admin account [gordonr 9013]

* Wed Jun 11 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.18-15]
- Make config database during build rather than storying in CVS.
  [charlieb 8982]

* Wed Jun 11 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.18-14]
- Include empty configuration database so that anaconda can tweak it before
  post-install runs. [charlieb 8982]
- Use new genfilelist feature for exceptions in filelist, rather than sed
  post-processing [charlieb 7719]

* Wed Jun 11 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.18-13]
- Force SystemName and DomainName to lower case. [charlieb 8672]

* Wed Jun 11 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.18-12]
- Remove the IPSEC client section bar [lijied 8992]

* Wed Jun 11 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.18-11]
- Added fr and es lexicon for IPSEC client [lijied 8992]

* Wed Jun 11 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.18-10]
- Missing semi-colons in dhcpd.conf output [gordonr 8996]

* Tue Jun 10 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.18-09]
- Do fr-ca -> fr symlink in %pre [gordonr 8969]

* Tue Jun 10 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.18-08]
- Corrected formatting on remoteaccess panel [gordonr 8983]

* Tue Jun 10 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.18-07]
- Set default dhcpd status to enabled in migrate fragment (as we do in
  default fragment). [charlieb 8984]

* Tue Jun 10 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.18-06]
- Fix problems with interfaces migrate fragment which manifest in dialup mode.
  Reformat white space to local standard while we are at it. [charlieb 8985]

* Tue Jun 10 2003 Tony Clayton <apc@e-smith.com>
- [4.13.18-05]
- Add restart-dhcpd to remoteaccess-update event [tonyc 8883]

* Tue Jun 10 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.18-04]
- Add logic to interfaces migrate fragment to enable/disable diald
  as required. [charlieb 8981]

* Mon Jun  9 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.18-03]
- Remove WebServer migrate fragment, since we no longer deprecate
  httpd-e-smith in base server. [charlieb 8903]

* Mon Jun  9 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.18-02]
- Alias "block-major-3" to "off", in case lilo tries to modprobe it.
  [charlieb 8971]

* Fri Jun  6 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.18-01]
- Remove optional binding to 80/443 for admin webserver [gordonr 8903]

* Wed Jun  4 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.17-32]
- Permitting local forwarding addresses for users. [msoulier 3388]

* Wed Jun  4 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.17-31]
- Use create-system-user to create required users. [charlieb 6033]

* Wed Jun  4 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.17-30]
- Remove accounts/defaults records now duplicated in e-smith-email.
  [charlieb 6460]

* Tue Jun  3 2003 Tony Clayton <apc@e-smith.com>
- [4.13.17-29]
- Add missing semi-colon to dhcpd.conf 25Range fragment [tonyc 8883]

* Tue Jun  3 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.17-28]
- Add fr translation for DHCP error msg [lijied 8858]

* Mon Jun  2 2003 Tony Clayton <apc@e-smith.com>
- [4.13.17-27]
- Remove /255.255.255.255 from all "allow from" manager networks [tonyc 8918]

* Mon Jun  2 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.17-26]
- Re-organise dhcpd.conf to allow VPNs to "steal" addresses from the
  DHCP range, and remove obsolete 00useDB fragment. [charlieb 8883]
- Removed remaining references to LocalDomainPrefix.  [charlieb 4812]

* Mon Jun  2 2003 Tony Clayton <apc@e-smith.com>
- [4.13.17-25]
- Call /sbin/e-smith/roadwarrior from panels [tonyc 1819]
- Don't show roadwarrior section if /sbin/e-smith/roadwarrior doesn't exist
  [tonyc 1819]

* Fri May 30 2003 Tony Clayton <apc@e-smith.com>
- [4.13.17-24]
- Several small fixes for roadwarrior hooks [tonyc 1819]

* Fri May 30 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.17-23]
- Putting my fix back into useraccounts.pm, as it was clobbered a revision
  later. [msoulier 3388]

* Fri May 30 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.17-22]
- Add fstab fragment (from e-smith-qouta) to enable quotas on the root file system.
  The UI code and actions stays in e-smith-quota.  [charlieb 8868]

* Fri May 30 2003 Tony Clayton <apc@e-smith.com>
- [4.13.17-21]
- Don't show cert download when creating user [tonyc 1819]
- Fix maxUsers bug when set to empty string [tonyc 8886]
- Fix another uninitialized value bug [tonyc]

* Thu May 29 2003 Tony Clayton <apc@e-smith.com>
- [4.13.17-20]
- Move ipsec cert download from remoteaccess to useraccounts panel [tonyc 1819]

* Thu May 29 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.17-19]
- Fix one more runtime error with a migration fragment. [charlieb 8880]

* Thu May 29 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.17-18]
- Fix various runtime errors with migration fragments. [charlieb 8880]

* Thu May 29 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.17-17]
- Remove dangling conf-migrate-variables symlink. [charlieb 8880]

* Thu May 29 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.17-16]
- Create migrate fragment to ensure that dhcp's start and end properties
  are defined and sensible. [charlieb 8874]
- Replace conf-migrate-variables with a set of migration fragments -
  discarding some obsolete stuff. [charlieb 8880]

* Thu May 29 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.17-15]
- Set valid dhcp start and end whether dhcp is enabled or not. [charlieb 8874]

* Thu May 29 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.17-14]
- Fix validation of system accounts in groups panel. [charlieb 6032]

* Wed May 28 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.17-13]
- Moving http-e-smith init script to e-smith-apache. [msoulier 8852]
- Move chap-secrets/60smbpasswd fragment from e-smith-pptpd [gordonr 8747]

* Wed May 28 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.17-12]
- Lexicon tag mismatch [gordonr 4847]

* Wed May 28 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.17-11]
- Translations for VPN_CLIENT_ACCESS [gordonr 4847]

* Wed May 28 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.17-10]
- Remove reference to out of date description from remoteaccess panel 
  [gordonr 8835]

* Wed May 28 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.17-09]
- Added L10N for MODIFY_ADMIN_TITLE [gordonr 8832]
- Changed IPSec -> IPSEC in remoteaccess panel, with minor rewording 
  [gordonr 1819]

* Wed May 28 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.17-08]
- Remove secure_shell links and anchors in remoteaccess panel lexica.
  [charlieb 8619]
- Add conf-routes symlink to bootstrap-console-save, in case
  primary network has been changed. [charlieb 8646]

* Wed May 28 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.17-07]
- Split /etc/ppp/{pap,chap}-secrets expansion into ppp-conf-users [gordonr 8849]
- Fix AdminPassword migration fragment. [msoulier 8842]
- Fix test fragment wrt dialup and pppoe connections. [msoulier 858]

* Wed May 28 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.17-06]
- Moving esmith::console from e-smith-base to e-smith-lib. [charlieb 8851]

* Wed May 28 2003 Tony Clayton <apc@e-smith.com>
- [4.13.17-05]
- Set PATH explicitly in console [tonyc 8856]

* Tue May 27 2003 Tony Clayton <apc@e-smith.com>
- [4.13.17-04]
- Add ipsec roadwarrior hooks into remoteaccess panel [tonyc 1819]

* Tue May 27 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.17-03]
- Fix some run-time errors in last console changes. [charlieb 8824]

* Tue May 27 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.17-02]
- Remove i-bay related stuff from init-accounts - moved to e-smith-ibays
  package. [charlieb 8841]
- Re-organise console code so that dhcp lease file is initialized
  when required, and not otherwise. [charlieb 8824]

* Tue May 27 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.17-01]
- Delete password panel, now merged into useaccounts [gordonr 8832]

* Tue May 27 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.16-38]
- Unlocalised string in French/Spanish after merge [gordonr 8832]

* Mon May 26 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.16-37]
- French and Spanish lexica for password->useraccounts merge [gordonr 8832]

* Mon May 26 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.16-36]
- Remove nonblank validator from system password verify field as it's already
  checked in the comparison validator [gordonr 8832]

* Mon May 26 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.16-35]
- Insert dummy page to stop FM from doing the post-event of the page before
  the one we're jumping to [gordonr 8832]

* Mon May 26 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.16-34]
- Removed check for 'admin' is reset-password as we have a special version
  for admin [gordonr 8832]
- TODO: The admin/user versions should be merged

* Mon May 26 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.16-33]
- Rebuild - missing Build dependency on timtam (fixed) [gordonr 8832]
- Make use of success() and error() methods, remove "Done" page [gordonr 8832]

* Mon May 26 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.16-32]
- Initial merge of password/useraccounts panels [gordonr 8832]
- TODO: French and Spanish lexica, remove password panel [gordonr 8832]

* Mon May 26 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.16-31]
- Require new e-smith-devtools, with fixed .mo generation [gordonr 8828]

* Mon May 26 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.16-30]
- Removing the choice of clearing the dhcp lease file, and making it
  automagick instead. [msoulier 8824]

* Fri May 23 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.16-29]
- Allow user-modify-unix to set the GCOS field for 'admin' [gordonr 4847]
- Added an intelligent recalculation of the dhcp start and end range.
  [msoulier 8713]
- Deleted update-uids migrate fragment [gordonr 8814]

* Fri May 23 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.16-28]
- Added user-modify-admin event, signalled when we modify admin. We could
  use user-modify, but most of the actions will be irrelevant [gordonr 4847]
- Deleted PPTP access default toggle since we can now do this for all
  users on the useraccounts panel [gordonr 4847]
- Continued clean up of PPTPAccess -> VPNClientAccess [gordonr 4847]
- Use setUnixSystemPassword when setting admin's password so we keep
  root and admin in sync [gordonr 4847]
- TODO: L10N of "VPN Client Access" (was "PPTP Access")

* Fri May 23 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.16-27]
- Initial work on adding 'admin' to useraccounts panel. You can change the
  admin FirstName and LastName, change admin's password and set 
  VPNClientAccess
  You cannot remove or lock the admin account.
  TODO: 
  - Post actions to deal with the changes
  - Unlocalised string MODIFY_ADMIN in panel
  - Handle setting of admin|PasswordSet from system PasswordSet
  [gordonr 4847]
- Migrate PPTPAccess property to VPNClientAccess and ensure defaults for
  all users/admin [gordonr 4847]

* Thu May 22 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.16-26]
- Fixed broken email validation in useraccounts.pm. [msoulier 3388]

* Thu May 22 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.16-25]
- Fixed typo in console wording [gordonr 8797]

* Thu May 22 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.16-24]
- Fixed an error in the test script. [msoulier 858]

* Thu May 22 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.16-23]
- Added a test script for testing the interface migration fragment.
  [msoulier 858]

* Thu May 22 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.16-22]
- Removed a "die" case from interfaces migration script [gordonr 858]

* Thu May 22 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.16-21]
- Add en-us, fr and es ssh section bar [lijied 8772]

* Thu May 22 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.16-20]
- Rearrange the section bar [lijied 8772]

* Thu May 22 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.16-19]
- re-add the ssh section [lijied 8772]

* Wed May 21 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.16-18]
- Removed empty CONFIGURE_BODY console screens directory [gordonr 7153]

* Wed May 21 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.16-17]
- Added en-us,fr and es telnet sectionbar [lijied 8772]

* Tue May 20 2003 Mark Knox <markk@e-smith.com>
- [4.13.16-16]
- Updated the tests in 00sanity-accounts.t to account for base breakup.
  [msoulier 1507]
- Reinstated DESC_TELNET_ACCESS entries in en and fr lexicons [markk 7917]
- Added DESC_TELNET_ACCESS to es lexicon [markk 7917]

* Tue May 20 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.16-15]
- Rearrange remoteaccess section bar [lijied 8772]
- check in again, last checkin error occurred
- Fixed MODIFY lexicon in useraccounts panel. [msoulier 8543]
- Fixed lexicon in groups panel, and placement of table header.
  [msoulier 8543]
- Updated many of the tests against the accounts db. [msoulier 1507]

* Thu May 15 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.16-14]
- Don't set empty defaults for DNSPrimaryIP/DNSSecondaryIP - they're legacy
  and have migrate fragments [gordonr 8752]

* Thu May 15 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.16-13]
- Move call to wins_server() to setup fragment [gordonr 5053]

* Thu May 15 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.16-12]
- Made use of ConfigDB::wins_server() [gordonr 5053]

* Wed May 14 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.16-11]
- Fix obsolete xinetd.conf default setting. [charlieb 8725]

* Wed May 14 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.16-10]
- Fix es lexicon breakage. [charlieb 4847]
- Add missing I18N in useraccounts.pm. [charlieb 8737]

* Wed May 14 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.16-09]
- Add workaround for mkdir quirk (setgid lost) in init-accounts. [charlieb 1507]

* Tue May 13 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.16-08]
- Add remaining es translations for PPTP access. [charlieb 4847]

* Tue May 13 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.16-07]
- Change PPTPAccess settings from enabled/disabled to yes/no. [charlieb 4847]
- Add missing fr translations for PPTP access stuff, and some of es
  translation. [charlieb 4847]

* Tue May 13 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.16-06]
- Clearing the dhcp range when the local IP changes. Suggesting a bad IP range
  is a bad thing. [msoulier 8713]

* Mon May 12 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.16-05]
- Updated one of the test scripts. [msoulier 8709]
- Fixed a homonymic failure in diald.conf template [gordonr 1396]

* Fri May  9 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.16-04]
- Fix admin-conf/httpd.conf to split error and access logs [gordonr 2527]

* Fri May  9 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.16-03]
- Fixed broken conf-security. [msoulier 8690]

* Thu May  8 2003 Tony Clayton <apc@e-smith.com>
- [4.13.16-02]
- Split up ip-up.local template [tonyc 1819]

* Thu May  8 2003 Mark Knox <markk@e-smith.com>
- [4.13.16-01]
- Removed more references to ibays in the spec file [markk 8610]

* Thu May  8 2003 Mark Knox <markk@e-smith.com>
- [4.13.15-76]
- Split out domains to e-smith-domains package [markk 8610]
- Split out ibays to e-smith-ibays package [markk 8610]

* Wed May  7 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.15-75]
- Fixed 10localroutes to remote warnings, and addition of unnecessary static
  routes. [msoulier 8646]

* Wed May  7 2003 Mark Knox <markk@e-smith.com>
- [4.13.15-74]
- Skip interfaces migrate fragment unless we've got valid settings [markk]

* Wed May  7 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.15-73]
- Move fr and es startwebsite to e-smith-starterwebsite [lijied 3793]

* Tue May  6 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.15-72]
- Add Spanish lexicon for base panels [lijied 3793]

* Mon May  5 2003 Mark Knox <markk@e-smith.com>
- [4.13.15-71]
- Export the new get_pptp_value sub [markk 4847]

* Mon May  5 2003 Mark Knox <markk@e-smith.com>
- [4.13.15-70]
- Fixed up a misspelled property name in useraccounts [markk 4847]

* Mon May  5 2003 Mark Knox <markk@e-smith.com>
- [4.13.15-69]
- Added per-user PPTP access toggle on create/modify page [markk 4847]
- Added configurable PPTP access default on remoteaccess panel [markk 4847]

* Mon May  5 2003 Tony Clayton <apc@e-smith.com>
- [4.13.15-68]
- Set serial-console to disabled by default [tonyc 3381]
- Remove serial-console section from panel [tonyc 3381]

* Tue Apr 29 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.15-67]
- Fix CSS and link in remoteaccess panel [gordonr 8619]
- Fixed an error message. [msoulier 8277]

* Tue Apr 29 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.15-66]
- set-access-defaults should just set properties, not create records [gordonr 8617]

* Tue Apr 29 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.15-65]
- Updated dependency on e-smith-lib. [msoulier 8277]
- Fixed bad logic in dhcp checks in console. [msoulier 8277]

* Tue Apr 29 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.15-64]
- Added strict screening of dhcp ip ranges. [msoulier 8277]

* Tue Apr 29 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.15-63]
- Corrected Copyright date [gordonr 8016]

* Mon Apr 28 2003 Tony Clayton <apc@e-smith.com>
- [4.13.15-62]
- s/exit/return/ in migrate fragment [tonyc 8535]

* Mon Apr 28 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.15-61]
- Split the en-us lexicon from userpassword panel [lijied 8577]

* Mon Apr 28 2003 Tony Clayton <apc@e-smith.com>
- [4.13.15-60]
- s/usb/usbcore/ in modules.conf alias [tonyc 6556]

* Mon Apr 28 2003 Tony Clayton <apc@e-smith.com>
- [4.13.15-59]
- Remove dead rmmod-ide-scsi action [tonyc 5692]
- Remove dead fix-cdrom action [tonyc 5692]

* Fri Apr 25 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.15-58]
- Remove the httpd-e-smith configdb record if nobody claims ownership of
  it [gordonr 8535]

* Fri Apr 25 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.15-57]
- Moved the network startup to S37, after bootstrap-console. [msoulier 8485]
- Removed the restart of the network in bootstrap-console. It's no longer
  needed. [msoulier 8485]

* Fri Apr 25 2003 Tony Clayton <apc@e-smith.com>
- [4.13.15-56]
- Fix update-passwd to skip Passwordable|no ibays [tonyc 8545]

* Fri Apr 25 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.15-55]
- Swapped the return values from run_screens. [msoulier 8539]

* Fri Apr 25 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.15-54]
- Fixed the return value from run_screens if the console_screens directory
  does not exist. [msoulier 8539]
- Fixed the fact that the server was bringing the external interface up in
  serveronly mode. [msoulier 8485]

* Fri Apr 25 2003 Tony Clayton <apc@e-smith.com>
- [4.13.15-53]
- Add french l10n for remote manager access [tonyc 4229]

* Fri Apr 25 2003 Tony Clayton <apc@e-smith.com>
- [4.13.15-52]
- Add hooks for remote manager access from the AMC [tonyc 4229]

* Fri Apr 25 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.15-51]
- Add dynamic console menu creation from parts in 
 /sbin/e-smith/console-menu-items [gordonr 3363]

* Fri Apr 25 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.15-50]
- Change default for serial console to be enabled on ttyS1. Fix inittab
  template so that gettys are started stopped as required. [charlieb 3381]

* Thu Apr 24 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.15-49]
- Change button name"Add Network" to "Add network" [bug 8491]

* Thu Apr 24 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.15-48]
- Added more strings for remoteaccess panel [gordonr 4229]

* Wed Apr 23 2003 Mark Knox <markk@e-smith.com>
- [4.13.15-47]
- Ask for password when configuring server if PasswordSet is not yes.
  Forward port of bug 8361. [markk 8459]

* Tue Apr 22 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.15-46]
- Adjust console page headers [gordonr 7894]

* Tue Apr 22 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.15-45]
- Removed call to conf-networking - done in bootstrap-console-save 
  [gordonr 8336]
- Create smelastsys uid/gid so random ones appear after this [gordonr 6033]

* Tue Apr 22 2003 Tony Clayton <apc@e-smith.com>
- [4.13.15-44]
- Add hwconfig default configdb record [tonyc 7744]

* Tue Apr 22 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.15-43]
- Force reconfiguration of dhcpcd and remove dhcpcd caches in
  conf-ethernet [gordonr 8336]
- Force migration of DHCPClient options [gordonr 8336]
- Updated Requires for initscripts [gordonr 8336]

* Mon Apr 21 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.15-42]
- Change console/set-access-defaults to use $sysconfig{PreviousSystemMode}
  and to set defaults on initial install/configure [gordonr 7920]

* Mon Apr 21 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.15-41]
- Standardize Add/Save button name [lijied 7921]

* Mon Apr 21 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.15-40]
- Call "id -u" to check whether uid is allocated [gordonr 7772]

* Mon Apr 21 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.15-39]
- Removed testing code SmallRedCell -> SmallCell [gordonr 8129]

* Mon Apr 21 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.15-38]
- Standardize the domain add/modify button name [lijied 7921]
- Make "Reset password" link red for new accounts [gordonr 8129]

* Thu Apr 17 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.15-37]
- Fold in code from e-smith-serial-console-0.0.1-06 [charlieb 3381]

* Thu Apr 17 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.15-36]
- Back out changes to console [gordonr 5163]
- Start dhcpcd after bootstrap-console in case settings have 
  changed [gordonr 5163]

* Thu Apr 17 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.15-35]
- Removed space from start of console title line [gordonr 7894]
- Clean up pid handling in dhcp run script [gordonr 7771]
- Ensure DHCP settings are correct in console [gordonr 5163]

* Wed Apr 16 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.15-34]
- Removed a redundant line from useraccounts.pm. [msoulier 7600]
- Change %pre to exit 0 if uid taken. Don't call useradd with
  the -g option - just let useradd do the work [gordonr 7772]

* Wed Apr 16 2003 Mark Knox <markk@e-smith.com>
- [4.13.15-33]
- Conditionally display and save ftp, serial-console, and telnet 
  properties [markk 8253]

* Wed Apr 16 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.15-32]
- Unify the release string bits into one variable [gordonr 7894]

* Wed Apr 16 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.15-31]
- Remove scsi-hostadapter alias munging from modules.conf [tonyc 5692]
- Remove product branding from console [gordonr 7894]

* Wed Apr 16 2003 Tony Clayton <apc@e-smith.com>
- [4.13.15-30]
- Add char-major-180 alias for usbcore in modules.conf [tonyc 6556]

* Wed Apr 16 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.15-29]
- Modified the serial console label [lijied 8313]

* Wed Apr 16 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.15-28]
- Fix migrate/interfaces to deal with only 'd' or 'dhi' options [gordonr 8336]
- Fix dhcpcd/run script to only send -h with DHCP - Hostname otion [gordonr 8336]

* Wed Apr 16 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.15-27]
- console: Only set 'd' option for DHCP - Send Ethernet address [gordonr 8344]

* Wed Apr 16 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.15-26]
- Add Serial console section bar [lijied 8313]

* Tue Apr 15 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.15-25]
- Modified serial console code [lijied 8313]

* Tue Apr 15 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.15-24]
- Add code to remoteaccess.pm to get/save serial-console settings
  [charlieb 8313]
- Added fr and en-us lexicon for serial-console [lijied 8313]

* Tue Apr 15 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.15-23]
- Add smelog user in %pre - used by dhcpcd/log/run script [gordonr 7772]

* Tue Apr 15 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.15-22]
- Refreshed the conf hash after run_screens to pick up any changes in the
  UnsavedChanges property. [msoulier 7962]

* Tue Apr 15 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.15-21]
- And fix /service/dhcpcd symlink [gordonr 5163]

* Tue Apr 15 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.15-20]
- Fixed typo in dhcpcd run script [gordonr 5163]

* Tue Apr 15 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.15-19]
- Handle the dhcpcd configuration options in run script [gordonr 5163]
- Add rc7.d link for dhcpcd [gordonr 5163]
- Reordered service2order in createlinks so it's easier to ser the order [gordonr 5163]
- Set BOOTPROTO="none" for dhcpcd configured interfaces [gordonr 5163]

* Mon Apr 14 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.15-18]
- Initial dhcpcd supervise environment (currently unused) [gordonr 5163]

* Mon Apr 14 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.15-17]
- Check whether to regenerate ssl key daily [gordonr 7831]

* Mon Apr 14 2003 Tony Clayton <apc@e-smith.com>
- [4.13.15-16]
- Add en l10n for groups table in useraccounts panel [tonyc 8131]
- Add fr l10n for groups table in useraccounts panel [tonyc 8131]

* Mon Apr 14 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.15-15]
- Fixed the anchor to the secure shell section of the remoteaccess panel.
  [msoulier 7949]
- Migrate named forwarders to dnscache properties [gordonr 8179]

* Fri Apr 11 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.15-14]
- Localised the Remove and Modify links. [msoulier 7949]

* Fri Apr 11 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.15-13]
- Modified Mitel Networks SME branding again [lijied 8016]

* Fri Apr 11 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.15-12]
- Modified group panel Modify button again [lijied 7921]

* Fri Apr 11 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.15-11]
- Bind http-admin to localhost:80 if main web server disabled [gordonr 8204]

* Thu Apr 10 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.15-10]
- Added spanish for password panel [gordonr 3793]

* Thu Apr 10 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.15-09]
- Added spanish L10N for pleasewait and page footer [gordonr 6382]

* Thu Apr 10 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.15-08]
- Modified "unsaved changes" warning [lijied 8166]
- Modified the initial "set your password" screen text [lijied 8165]
 
* Wed Apr  9 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.15-07]
- Flag primary domain as "Removable|no" and make use of that in the 
  domains panel to hide the "Remove" link [gordonr 8097]

* Wed Apr  9 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.15-06]
- Relocate conf-httpd to e-smith-apache [gordonr 8150]

* Wed Apr  9 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.15-05]
- Modified fr and en-us label text [lijied 7949]

* Wed Apr  9 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.15-04]
- Don't process srm.conf or access.conf - we just ignore them
  in the httpd.conf anyway [gordonr 8150]

* Tue Apr  8 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.15-03]
- Removed colon at the end of the label where necessary [lijied 7950]

* Tue Apr  8 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.15-02]
- Standardized Add/Save/Remove button names [lijied 7921]

* Mon Apr  7 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.15-01]
- Handle change of $squid{TransparentPort} in review [gordonr 4723]

* Mon Apr  7 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.14-38]
- Further fixups to the %pre migration of fr-ca -> fr [goordonr 8054]
- Create .AppleDesktop subdir when creating i-bays [gordonr 7855]

* Mon Apr  7 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.14-37]
- Fixed french lexicon. [msoulier 7949]
- Strip and simplify admin-conf/httpd.conf [gordonr 2527]
  If httpd-e-smith is enabled, bind only to 127.0.0.1:980
  If httpd-e-smith does not exist, or is disabled,
  bind to 127.0.0.1, $LocalIP:80, 0.0.0.0:443
- TODO: Strip out some unused Apache modules [gordonr 2527]
- Add /server-resources/ alias [gordonr 2527]

* Fri Apr  4 2003 Mark Knox <markk@e-smith.com>
- [4.13.14-36]
- Moved restart-httpd-* to e-smith-apache [markk 5509]

* Fri Apr  4 2003 Mark Knox <markk@e-smith.com>
- [4.13.14-35]
- Localised the "Modify" link in the useraccounts panel. [msoulier 7949]
- Disabled httpd-e-smith by default. [markk 5509]
- More work on %pre migration - only worrying about 5.6 upgrades - 
  may cause some early 6.0alpha upgrade annoyance [gordonr 8054]
- Removed httpd-e-smith stuff. [markk 5509]

* Thu Apr  3 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.14-34]
- Re-arrange console code so that we don't call
  "signal-event console" before a reboot; we leave things
  for bootstrap-console-save. [charlieb 4603]

* Thu Apr  3 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.14-33]
- Added %pre migration of fr-ca lexica to fr [gordonr 8054]

* Thu Apr  3 2003 Tony Clayton <apc@e-smith.com>
- [4.13.14-32]
- Fix groups panel to loop back to first page [tonyc 6515]

* Thu Apr  3 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.14-31]
- Modified SME Server manager to Server manager [lijied 8016]

* Thu Apr  3 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.14-30]
- Changed copyright year [lijied 8016]
- Modified SME Server branding [lijied 8016]

* Thu Apr  3 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.14-29]
- Removed installer Mitel Networks branding [lijied 8031]

* Thu Apr  3 2003 Tony Clayton <apc@e-smith.com>
- [4.13.14-28]
- Fix, indent localnetworks panel [tonyc 8034]
- Fix missing tag in en lexicon for remoteaccess [tonyc 4388]
- Fix domains panel for httpd restarts [tonyc 7751]

* Thu Apr  3 2003 Tony Clayton <apc@e-smith.com>
- [4.13.14-27]
- Fix labels on virtual domain page [tonyc 7950]
- Change $q->table to $q->start_table where necessary [tonyc 8034]

* Thu Apr  3 2003 Tony Clayton <apc@e-smith.com>
- [4.13.14-26]
- Ignore virtual domains in httpd-admin fragments [tonyc 8030]

* Wed Apr  2 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.14-25]
- Replaced validate_group_description and ibay_description routine
  with esmith::FormMagick validate_description [lijied 5054]
- Collapse SSL part of http-admin httpd.conf.
  If httpd-e-smith is enabled, we only bind to localhost:980
  If httpd-e-smith is disabled, we bind to localhost:980 and 0.0.0.0:443,
  but limit access by httpd-admin{ValidFrom} plus local networks.
  [gordonr 7900]

* Wed Apr  2 2003 Tony Clayton <apc@e-smith.com>
- [4.13.14-24]
- Removed all Mitel Networks SME Server branding [lijied 8016]
- Add french translations for remoteaccess panel [tonyc 4388]

* Wed Apr  2 2003 Tony Clayton <apc@e-smith.com>
- [4.13.14-23]
- Fix groups panel "remove" screen layout [tonyc 7950]

* Wed Apr  2 2003 Tony Clayton <apc@e-smith.com>
- [4.13.14-22]
- Adding fr translation for Telnet [tonyc 7917] 

* Wed Apr  2 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.14-21]
- Added additional French trans for FTP [lijied 7599]

* Wed Apr  2 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.14-20]
- Fixed english lexicon for SAVE in the useraccounts panel. [msoulier 7921]
- Fixed english and french lexicon for groups panel. [msoulier 7921]

* Wed Apr  2 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.14-19]
- Removed ../pam.d/{ftp,imap,login,passwd}/template-begin files
  and modified the %build code [lijied 3295]

* Tue Apr  1 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.14-18]
- Remove telnet from remoteaccess panel, or show "telnet not supported" text if
  it is manually/previously enabled.  [tonyc 7917]
- s/Apply/Save/ in remoteaccess,password panel (en-us and fr) [tonyc 7984]
- Added sectionbars to fr lexicon for remoteaccess [gordonr 7911]

* Tue Apr  1 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.14-17]
- Bind httpd-admin to localhost only [gordonr 7900]

* Tue Apr  1 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.14-16]
- French nav bar for domains [gordonr 7926]

* Tue Apr  1 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.14-15]
- Removed conf-dhcpd symlinks - now done in run script [gordonr 7771]

* Mon Mar 31 2003 Mike Dickson <miked@e-smith.com>
- [4.13.14-14]
- Remote Management section of remoteaccess panel no longer spawns new screens
  [tonyc 4388]
- remoteaccess panel now shows Operation Status Report instead of "Done" screen
  [tonyc 4388]
- re-synchronize lexicons a bit, fix spacing [tonyc 4388]
- fixed the "Action" column to be several columns instead of one [miked 7761]

* Mon Mar 31 2003 Tony Clayton <apc@e-smith.com>
- [4.13.14-13]
- Treat en the same as en-us [gordonr 7733]

* Mon Mar 31 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.14-12]
- Add section bars to remoteaccess panel [gordonr 7911]
- TODO: fr lexicon needs to resync with en-us as section headings 
  are missing in the fr lexicon [gordonr 7911]

* Mon Mar 31 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.14-11]
- Undo recent change to remoteaccess panel. [charlieb 7466]

* Fri Mar 28 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.14-10]
- Allow fr* in pleasewait [gordonr 6382]

* Fri Mar 28 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.14-09]
- Adjusted useraccounts lexicons due to panel name change [gordonr 7676]

* Fri Mar 28 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.14-08]
- Changed some mixed-case i-bays to i-bay [gordonr 7676]
- Added the new CSS styles to Information bay name in Add i-bay [gordonr 7676]

* Fri Mar 28 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.14-07]
- Added symlink /etc/e-smith/locale/fr-ca -> fr [gordonr 7733]

* Fri Mar 28 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.14-06]
- Modified directory name po/fr_CA to fr [lijied 6787]

* Fri Mar 28 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.14-05]
- Relocated {index,initial}.cgi to other packages [gordonr 7728]

* Fri Mar 28 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.14-04]
- Update FTP text in remoteaccess panel [charlieb 7466]

* Fri Mar 28 2003 Tony Clayton <apc@e-smith.com>
- [4.13.14-03]
- send STDOUT to /dev/null instead of closing it for last patch [tonyc 7751]

* Fri Mar 28 2003 Tony Clayton <apc@e-smith.com>
- [4.13.14-02]
- Fix primary domain display in domains panel, use multiple columns for action
  heading [tonyc 7751]
- close STDOUT before calling restart-httpd-full in domains panel [tonyc 7751]

* Fri Mar 28 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.14-01]
- Fix after failed concurrent builds
- First cut at clarification of FTP config options. At least fr lexicon will need
  to change. [charlieb 7466]
- Merged lexica for index.cgi and initial.cgi [gordonr 7728]
- TODO: The scripts should also be merged

* Thu Mar 27 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.13-08]
- Localise footer in domains panel [gordonr 3553]

* Thu Mar 27 2003 Tony Clayton <apc@e-smith.com>
- [4.13.13-07]
- Add french l10n strings in password panel [tonyc 6030]

* Thu Mar 27 2003 Mark Knox <markk@e-smith.com>
- [4.13.13-06]
- Dropped use of port 980 for text-mode web access in console [markk 4263]

* Thu Mar 27 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.13-05]
- Fixed a couple of flow-control problems in the new screen setup.
  [msoulier 7153]

* Thu Mar 27 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.13-04]
- Allow "Removable" property in networks, with "no" value blanking the
  "Remove" link.n local networks panel. [charlieb 2404]

* Thu Mar 27 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.13-03]
- Modified French lexicon to use lang="fr", rename the lexicon
  directory to fr [lijied 6787]

* Wed Mar 26 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.13-02]
- Save a process in dhcpd startup [gordonr 7771]
- Fix dhcpd run file to redirect stderr before running any commands.
  [charlieb 7771]
- Change localnetworks panel to display blank "remove" column
  for system local network, rather than "NOTREMOVABLE". [charlieb 7730]

* Wed Mar 26 2003 Mark Knox <markk@e-smith.com>
- [4.13.13-01]
- And link to the correct startup file :-) [gordonr 7771]
- Don't worrry if the pid file is missing [gordonr 7771]
- Added admin account back to accounts db defaults [markk 7726]

* Wed Mar 26 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.12-18]
- Workaround unlink/symlink for /etc/rc.d/init.d/dhcpd to
  resolve file conflict [gordonr 7771]

* Wed Mar 26 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.12-17]
- PODified console.pm. [msoulier 7153]
- Added navigation logic to run_screens. [msoulier 7153]

* Wed Mar 26 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.12-16]
- Objectified console.pm. [msoulier 7153]
- Changed calls from console to new objectified console.pm
  api. [msoulier 7153]
- Removed template-begin-shell for dhcpd as it is no longer a 
  template [gordonr 7771]

* Tue Mar 25 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.12-15]
- And two more stray references [gordonr 7771]

* Tue Mar 25 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.12-14]
- And fix %files to use %{name} macro for filelist [gordonr 7771]

* Tue Mar 25 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.12-13]
- Typo in %files section [gordonr 7771]

* Tue Mar 25 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.12-12]
- Run dhcpd under supervise 
- Delete template for /etc/rc.d/init.d/dhcpd and script to
  expand it [gordonr 7771]
- Expand /etc/dhcpd.conf in dhcpd run script [gordonr 7771]

* Tue Mar 25 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.12-11]
- Add Network and Broadcast properties for internal/external
  interface specifications so templates don't have to keep
  recalculating them [gordonr 858]

* Tue Mar 25 2003 Mark Knox <markk@e-smith.com>
- [4.13.12-10]
- Generate po on the fly like we do for server-console [markk 7715]
- Added missing 'use' in 25Copyright [markk 7715]

* Tue Mar 25 2003 Mark Knox <markk@e-smith.com>
- [4.13.12-09]
- Whoops, forgot to add file [markk 7715]

* Tue Mar 25 2003 Mark Knox <markk@e-smith.com>
- [4.13.12-08]
- Localised foot.tmpl 25Copyright fragment using esmith::I18N [mark 7715]

* Tue Mar 25 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.12-07]
- Removed template-end in head.tmpl and foot.tmpl templates [markk 7715]
- Added new common copyright notice fragment to foot.tmpl [markk 7715]
- Modified ibays public access en-us and fr-ca text [lijied 4081]

* Tue Mar 25 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.12-06]
- Modified secure shell access en-us and fr-ca text [lijied 4081]

* Sun Mar 23 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.12-05]
- Move initialisation of "shared" in accounts db from init-accounts to
  defaults db fragment. [charlieb 1507]

* Thu Mar 20 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.12-04]
- Replaced -T flag in /sbin/e-smith/console shebang line [gordonr 7153]
- Fixed tainting problem in console.pm [gordonr 7153]

* Thu Mar 20 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.12-03]
- Initial split-up of console with plug-in screens [gordonr 7153]

* Thu Mar 20 2003 Tony Clayton <apc@e-smith.com>
- [4.13.12-02]
- Set Ibay "Reset Password" link css to a.error class if password not set but
  required [tonyc 4718]

* Thu Mar 20 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.12-01]
- Clean up source tarball [gordonr 7153]

* Thu Mar 20 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.11-11]
- Removed unwanted console screen [gordonr 7153]

* Thu Mar 20 2003 Tony Clayton <apc@e-smith.com>
- [4.13.11-10]
- Fix ibay panel to use separate table columns for actions [tonyc 7734]
- Add dependency on esmith-lib >= 1.13.1-52 [tonyc 7734]

* Thu Mar 20 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.11-09]
- Modified en-us and fr-ca online-manual description [lijied 6788]
 
* Wed Mar 19 2003 Tony Clayton <apc@e-smith.com>
- [4.13.11-08]
- Require current password authentication when changing system password from
  password panel. [tonyc 6030]

* Wed Mar 19 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.11-07]
- Add null template-begin to generated index.html. We do actually
  want people to edit the generated prototype file [gordonr 6552]

* Wed Mar 19 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.11-06]
- Moved lots of directory creations from prep to $build so they
  are unaffected by patches which remove the directory :-) [gordonr 6552]

* Wed Mar 19 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.11-05]
- Process index.html for i-bays from a template, using the i-bay
  description "Name" in the header [gordonr 6552]

* Tue Mar 18 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.11-04]
- Modified domains panel order [lijied 7356]

* Tue Mar 18 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.11-03]
- Fix virtualdomains => domains text in lexica. [charlieb 7731]

* Tue Mar 18 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.11-02]
- Split ./etc/crontab/template-begin [lijied 3295]
- split ./etc/statusreport/template-begin [lijied 3295]

* Tue Mar 18 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.11-01]
- Remove special case ftp code in set-access-defaults migrate fragment.
  [charlieb 7683]
- Split ./ifcfg-ppp0/template-begin [lijied 3295]
- Delete .po entries for Review Configuration screen [gordonr 7722]

* Tue Mar 18 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.10-01]
- Deleted ./etc/rc.d/init.d/{masq, diald,dhcpd}/template-begin,
  modified %build [lijied 3295]
- Removed "Review Configuration" page from console [gordonr 7722]

* Tue Mar 18 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.9-03]
- Deleted /etc/dhcpc/dhcpcd.exe/template-begin
  modified %build code [lijied 3295]
- Added french translation. [msoulier 6401]
- Added French translation for "ERR_OCCURRED_MODIFYING_PASSWORD" [Lijied 4853]

* Tue Mar 18 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.9-02]
- Changed "Public IP Address" to "Internet Visible IP Address". [msoulier 6401]
- Added English translation for "ERR_OCCURRED_MODIFYING_PASSWORD"[lijied 4853]

* Mon Mar 17 2003 Mark Knox <markk@e-smith.com>
- [4.13.9-01]
- Third time's the charm.

* Mon Mar 17 2003 Mark Knox <markk@e-smith.com>
- [4.13.8-01]
- Deleted ./etc/inittab/template-begin [lijied 3295]
- Force as-source to pick up new files which are not appearing [markk 4722]

* Mon Mar 17 2003 Mark Knox <markk@e-smith.com>
- [4.13.7-15]
- Split out etc/nsswitch.conf/template-begin 
- Split out etc/hosts.deny/template-begin
- Split out etc/mime.types/template-begin 
- Deleted ./etc/sysconfig/static-routes/template-begin [lijied 3295]
- Added empty template-{begin,end} for {head,foot}.tmpl [markk 4722]

* Mon Mar 17 2003 Mark Knox <markk@e-smith.com>
- [4.13.7-14]
- Split up etc/nsswitch.conf/template-begin 
- Split up etc/hosts.deny/template-begin [lijied 3295]
- Merged expand-head-and-foot into conf-httpd-admin [markk 4722]

* Mon Mar 17 2003 Mark Knox <markk@e-smith.com>
- [4.13.7-13]
- Split up head.tmpl into template fragments [markk 4722]
- Added expand-head-and-foot action in post-{install,upgrade} [markk 4722]
- Split up foot.tmpl into template fragments [markk 7714]

* Mon Mar 17 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.7-12]
- Delete empty template-end files [lijied 3295]

* Sat Mar 15 2003 Mike Dickson <miked@e-smith.com>
- [4.13.7-11]
- updated package check in head.tmpl [miked 4722]

* Thu Mar 13 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.7-10]
- Added the PublicIP property of the sysconfig record to the review
  configuration panel, if it is set. [msoulier 6401]

* Thu Mar 13 2003 Tony Clayton <apc@e-smith.com>
- [4.13.7-09]
- Fix conf-mod_ssl to limit field lengths in X509 certificate [tonyc 7678]

* Thu Mar 13 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.7-08]
- Fixed reset password page for ibays to use a Save button. [msoulier 7260]

* Thu Mar 13 2003 Mark Knox <markk@e-smith.com>
- [4.13.7-07]
- Fix path to rpm and parens around condition in head.tmpl [markk 4722]

* Thu Mar 13 2003 Mark Knox <markk@e-smith.com>
- [4.13.7-06]
- Modified head.tmpl to determine release and show correct title
  [markk 4722]

* Thu Mar 13 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.7-05]
- Fix mapping of ftpaccess and ftplimits CGI variables to db properties, in remoteaccess
  FM code. I find those two sooo confusing! [charlieb 7466]

* Thu Mar 13 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.7-04]
- Restore ftp remoteaccess UI to 5.5 version, but use migrated property names
  access and LoginAccess in place of accessLimits and access. [charlieb 7466]

* Wed Mar 12 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.7-03]
- Removed force fragment for Primary account type, now that fix
  is in place in e-smith-lib. [charlieb 5652]

* Wed Mar 12 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.7-02]
- Change "domains" panel so that SystemPrimaryDomain can be modified (e.g.
  set to use a different i-bay for web content), but not removed.
  [charlieb 6810]

* Wed Mar 12 2003 Mike Dickson <miked@e-smith.com>
- [4.13.7-01]
- moved logrotate template fragment to weekly section of crontab file
  [miked 6734]

* Wed Mar 12 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.6-26]
- Add migrate fragment for Primary "system" record in accounts DB.
  Since that isn't currently working (bug 7652), add force fragment to
  set type to "ibay". [charlieb 5652]

* Wed Mar 12 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.6-25]
- Duh! Use value, not key, of 'DomainName' record when creating system domain
  domainsDB record. [charlieb 2670]

* Wed Mar 12 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.6-24]
- Use "Primary" pre-defined i-bay rather than "wwwpublic" as default
  "Content" for virtual domain websites [charlieb 5652].
- Move setup/change of SystemPrimaryDomain entry in domains DB from
  console to a migrate fragment. This allows upgrades to work. [charlieb 2670]

* Tue Mar 11 2003 Mike Dickson <miked@e-smith.com>
- [4.13.6-23]
- removed uneccessary commented-out code [miked 6403]

* Tue Mar 11 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.6-22]
- Use new db defaults/force scheme for getting sysconfig|ReleaseVersion
- Mark sysconfig=configuration here, ReleaseVersion property provided
  by e-smith-release package [gordonr 7531]
- Delete determine-release as we no longer need it [gordonr 7531]

* Tue Mar 11 2003 Mark Knox <markk@e-smith.com>
- [4.13.6-21]
- Cleaned up some warnings in useraccounts.pm, fixed a broken validation,
  and changed system account test [markk 1507]

* Tue Mar 11 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.6-20]
- Added gettext() .mo file generationt to %build [gordonr 7578]

* Tue Mar 11 2003 Mike Dickson <miked@e-smith.com>
- [4.13.6-19]
- updated iBay to i-Bay in en_us lexicon. [miked 6789]

* Tue Mar 11 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.6-18]
- Fixed typo in conf-masq - need to get the value of SystemMode, not the object [gordonr 7631]

* Mon Mar 10 2003 Mark Knox <markk@e-smith.com>
- [4.13.6-17]
- Changed validate_acctName to use new esmith::AccountsDB validator [markk
  1507]
- Removed explicit system account creation from init-accounts [markk 1507]

* Fri Mar  7 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.6-16]
- Deleted obsolete and now inaccurate README from en-us locale area [gordonr 4030]

* Fri Mar  7 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.6-15]
- Fix misplaced webmail default fragment of accounts db. [charlieb 1507]

* Fri Mar  7 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.6-14]
- Fix init-accounts creation of pre-defined Primary i-bay. [charlieb 7604]

* Fri Mar  7 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.6-13]
- Link "fr" locale directory to "fr-ca" so we can use either
  language tag [gordonr 6787]
- TODO: Handle .mo file links for gettext() [gordonr 6787]

* Fri Mar  7 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.6-12]
- And fix the panel link [gordonr 7408]

* Fri Mar  7 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.6-11]
- Re-modified en-us and fr-ca Users nav bar label [lijied 7356]

* Fri Mar  7 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.6-10]
- Rename virtualdomains panel to domains [gordonr 7408]

* Fri Mar  7 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.6-09]
- Gracefully handle some "not ready yet" conditions in migrate code for setting
  up local network entry. [charlieb 5650]
- Modified Users French nar bar label [lijied 7356]

* Fri Mar  7 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.6-08]
- Fix iteration syntax in i-bay migration script. Rename script to remove the
  redundant "migrate". [charlieb 7526]

* Fri Mar  7 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.6-07]
- Migrate fragment for local network db entry moved from networks
  to configuration (as migrate is skipped on empty db). Changes
  made to script to accommodate.  [charlieb 5650]

* Fri Mar  7 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.6-06]
- Modified en-us and fr-ca panel title for groups, ibays,users.
  modified en-us Users nav bar  [lijied 7356]
- Fix call to processTemplate in conf-startup - duh! need PERMS, not MODE.
  [charlieb 7526]

* Fri Mar  7 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.6-05]
- Fix runtime problems with interfaces migrate fragment. [charlieb 7343]

* Thu Mar  6 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.6-04]
- Move conf-migrate-interfaces code into migrate template fragment
  [charlieb 7343]
- Move setup of networks db entry for local network into migrate
  fragment [charlieb 5650]
- Remove setRealtoEffective from conf-mod_ssl - not required, and
  we no longer use esmith::util due to db refactoring changes. [charlieb 2670]
- Fix cut&paste breakage in system account validation change [charlieb 1507]

* Thu Mar  6 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.6-03]
- Fix call to processTemplate() in conf-startup [gordonr 7526]

* Thu Mar  6 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.6-02]
- Link conf-migrate-interfaces into post-{install,upgrade} and
  bootstrap-console-save for now - will become a migrate fragment 
  [gordonr 7343]

* Thu Mar  6 2003 Mike Dickson <miked@e-smith.com>
- [4.13.6-01]
- edited crontab fragment to remove reference to cron-wrapper [miked 6734]

* Thu Mar  6 2003 Mike Dickson <miked@e-smith.com>
- [4.13.5-01]
- removed cron-wrapper and crontab fragments [miked 6734]

* Thu Mar  6 2003 Mike Dickson <miked@e-smith.com>
- [4.13.4-01]
- added cron-wrapper and a few other crontab fragments [miked 6724]
- Modified panel order [lijied 7356]

* Thu Mar  6 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.3-05]
- Change name validators in group, useraccounts and i-bays panels to check
  password and group files after checking accounts db. [charlieb 1507]
- Remove stray "#groups#" empty file. [charlieb]

* Wed Mar  5 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.3-04]
- Split en-us lexicon from panels: groups, ibays,index.cgi,initial.cgi,
  localnetworks,online-manual,password,reboot,remoteaccesscontrol,
  review, useraccounts,virtualdomains    [lijied 4030]

* Tue Mar  4 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.3-03]
- Move more db initiatisation and migration into {defaults,migrate} directories.
  [charlieb 7526]

* Tue Mar  4 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.3-02]
- Regularise ftp access limits and panel content.
  TODO: carefully check panel text and update fr_CA lexicon. [charlieb 7466]
- Remove dynamic DNS scripts directory (now empty). [charlieb 5860]
- Move lots of configuration default settings from code to default
  fragments. [charlieb 7526]

* Tue Mar  4 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.3-01]
- Rebuild --as-source due to repository rearrangement [lijied 5003]

* Tue Mar  4 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.2-32]
- Rebuilding RPM [lijied 5003]

* Tue Mar  4 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.2-31]
- Remodify the lexicon file [lijied 7493]
- Remove 'userpassword' and 'password' web panel lexicon
  directories manually from e-smith-base CVS repository [jay 7493]

* Mon Mar  3 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.2-30]
- Added French lexicon for userpassword [lijied 7493]

* Mon Mar  3 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.2-29]
- RebuildRPM: commit missed last time [lijied 5003]

* Fri Feb 28 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.2-28]
- Converted a big chunk of init-accounts to new defaults system [markk 1507]
- Added French lexicon to package. [lijied 5003]
- Re-do hosts.allow template to use esmith::ConfigDB::hosts_allow_spec.
  Add dependency on up-to-date e-smith-lib. [charlieb 5650]

* Fri Feb 28 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.2-27]
- Added French lexicon for groups [lijied 5003]
- Update conf-security to use esmith::{{Config,Networks}DB,templates}.
  Make template expansion of /etc/securetty unconditional.
  [charlieb 5650]

* Thu Feb 27 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.2-26]
- Merge conf-ethernet into conf-networking
- Unlink conf-network from {domain,network}-{create,modify,delete} 
  [gordonr 7343]

* Thu Feb 27 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.2-25]
- Modify virtual domain panel to list primary domain, but show  "CANTMODIFY"
  rather than the remove/modify buttons. [charlieb 2670]
- Modify local networks panel so that system local network is displayed
  but marked non-removable. [charlieb 5650]
- Change navigation entry from "Virtual Domains" to "Domains", and change
  various lexicon entries. [charlieb 7408]

* Thu Feb 27 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.2-24]
- Handle pppoe in normal/swapped mode [gordonr 7343]

* Thu Feb 27 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.2-23]
- Further cleaning of interface templates [gordonr 7343]

* Thu Feb 27 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.2-22]
- Further cleaning of interface handling [gordonr 7343]

* Thu Feb 27 2003 Mark Knox <markk@e-smith.com>
- [4.13.2-21]
- Converted reset-config to new lib defaults system and removed it [markk 3299]

* Thu Feb 27 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.2-20]
- Updated conf-ethernet to ConfigDB interface [gordonr 7343]
- Used one template ifcfg-ethX for eth[01], passing THIS_DEVICE down
  as extra data in the MORE_DATA option to processTemplate() [gordonr 7343]

* Wed Feb 26 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.2-19]
- $EthernetAssign undefined as "normal", not "unknown" [gordonr 7343]
- Return "" at the end of ifcfg-eth[01]/00setup so we don't pass
  down a stray value we've just calculated [gordonr 7343]
- Fixed method calls in conf-migrate-interfaces [gordonr 7343]

* Tue Feb 25 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.2-18]
- Continued work on ifcfg-eth[01] to determine whether they should be 
  up at boot (unfinished) [gordonr 7343]
- Predefined i-bay is "Primary", so its directory must be "Primary",
  not "primary".  [charlieb 5652]
- Fix various problems with maintentance of networks db local network
  entries from console [charlieb 5650]
- Remove dynamic DNS console dialogs unless dynamic DNS scripts directory
  is present. Remove example custom dynamic DNS script. [charlieb 5860]

* Mon Feb 24 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.2-17]
- Set $pppoe{PhysicalInterface} so that PPPoE knows which physical
  device to use [gordonr 7343]

* Mon Feb 24 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.2-16]
- Changelogs fix s/7353/7343/ [gordonr 7343]

* Mon Feb 24 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.2-15]
- Actually delete template-begin from ifcfg-eth1 [gordonr 7343]
- Delete /etc/pump.conf template and "unlink" reference [gordonr 7343]

* Mon Feb 24 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.2-14]
- Split up ifcfg-eth{0,1} templates [gordonr 7343]
- Set up $this_interface in 00setup [gordonr 7343]
- TODO: Merge into one hierarchy [gordonr 7343]

* Mon Feb 24 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.2-13]
- Split up and cleaned up the /etc/sysconfig/network template [gordonr 7343]

* Mon Feb 24 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.2-12]
- Removed any references to LocalDomainPrefix. [msoulier 4812]

* Sat Feb 22 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.2-11]
- Fix prob in virtualdomains panel [charlieb 7345]

* Sat Feb 22 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.2-10]
- Split up dhcpd startup and and ExternalInterface details [gordonr 7343]
- Adjusted previous changelog s/dhcpd/dhcpcd/

* Sat Feb 22 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.2-09]
- Updated dhcpcd.exe template to use ExternalInterface details [gordonr 7343]

* Fri Feb 21 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.2-08]
- Update set-external-ip to modify the ExternalInterface{'IPAddress'}
  property as well as the $ExternalIP record [gordonr 858]

* Fri Feb 21 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.2-07]
- Link conf-migrate-variables into [bootstrap-]console-save [gordonr 858]
- Fix up a couple of semantic errors in conf-migrate-interfaces.
  Use merge_props rather than multiple set_prop to minimise log file
  noise. [charlieb 858]
- Add details about 'static' Configuration [gordonr 858]

* Fri Feb 21 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.2-06]
- conf-migrate-interfaces: Build "interface" records to aggregate 
  interface details from all of the singletons (unfinished). [gordonr 858]
- TODO: Merge into conf-migrate-variables [gordonr 858]
- NOTE: Old singletons are NOT deleted at this time so existing scripts
  and templates can use the old values [gordonr 858]
- Updated e-smith-lib Requires: for $db->get_{prop,val} methods [gordonr 858]

* Fri Feb 21 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.2-05]
- Create Primary domain entry in domains DB [charlieb 2670]
- Add local network entry in networks DB [charlieb 5650]
- Update DHCP range when we change local network [charlieb ]

* Fri Feb 21 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.2-04]
- Removed migrate-configdb, which just set the permissions to 0600.
  We can do that in esmith::config (and we want 0660) [gordonr 2676]

* Mon Feb 10 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.2-03]
- Added the ForceSave option to bootstrap-console to prevent the unnecessary
  interaction. [msoulier 6658]

* Mon Feb 10 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.2-02]
- Setting bootstrap-console's Run property to yes before rebooting.
  [msoulier 6658]

* Fri Feb  7 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.2-01]
- Collecting patches into a new tarball. 

* Tue Feb  4 2003 Mark Knox <markk@e-smith.com>
- [4.13.1-43]
- Use new-style DB access, not db_* commands [markk 6428]

* Tue Feb  4 2003 Mark Knox <markk@e-smith.com>
- [4.13.1-42]
- Include space between local nets and ValidFrom nets [markk 6428]
- Always run a vhost on localhost:980 [markk 6428]
- Reload httpd-admin after conf-httpd-admin in bootstrap-console-save 
  [markk 6428]
- Reload httpd-admin after any change to remoteaccess properties. We need
  to update the ValidFrom networks. [markk 6428]

* Mon Feb  3 2003 Mark Knox <markk@e-smith.com>
- [4.13.1-41]
- Formatting tidyup in /sbin/e-smith/console. [charlieb]
- Remove redundent setting of WebServerName [charlieb 6861]
- If no primary webserver, run on ports 80 and 980 on internal interfaces.
  SSL will run on external interface [markk 6428]
- Allow access to admin server only to ValidFrom networks even when
  running without primary web server [markk 6428]

* Thu Jan 30 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.1-40]
- Remove code from init-accounts which sets ownership and permission of
  files and directories [charlieb 1507]
- Rewrite accounts db updates in init-accounts to use esmith::AccountsDB.
  [charlieb 1507]
- Fix problem with move of primary directory to ibays [charlieb 5652]

* Wed Jan 29 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.1-39]
- Fix pathname error in init-accounts [charlieb 5652]
- Fix ownership of default index.htm file in primary i-bay
  [charlieb 5652]

* Wed Jan 29 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.1-38]
- Remove fix-primary-perms script. Move primary fixup code from %pre to
  init-accounts [charlieb 5652]
- Change i-bay panel to deal with i-bays which can't be modified or
  removed, or have a password set [charlieb 5652]

* Wed Jan 29 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.1-37]
- Fix inadvertent syntax error in init-accounts. [charlieb 5652]

* Wed Jan 29 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.1-36]
- removed ellipsis from virtual domain add button [miked]
- Allow "debug" option for ppp to be set by property of diald in
  config db. [charlieb 6021]
- Rolled back an unintentional change to 05Port fragment [markk]
- Make "Primary" a predefined i-bay [charlieb 5652]

* Sun Jan 26 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.1-35]
- Fix variable name errror in virtualdomains panel [charlieb 6765]

* Sat Jan 25 2003 Mike Dickson <miked@e-smith.com>
- [4.13.1-34]
- added "Action" to the lexicon [miked 6363]

* Fri Jan 24 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.1-33]
- And actually generate the cert with $SystemName.$DomainName rather
  than just changing the filename [gordonr 4874]

* Fri Jan 24 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.1-32]
- Generate SSL self-certficate as $SystemName.$DomainName instead
  of the fixed secure.$DomainName (which doesn't exist in any case)
  [gordonr 4874]

* Fri Jan 24 2003 Mark Knox <markk@e-smith.com>
- [4.13.1-31]
- Added warning if default password hasn't been changed [markk 6752]

* Sat Jan 18 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.1-30]
- Made the router in localnetworks mandatory, such that only networks on the
  local network may be added to the local networks list. [msoulier 5848]

* Fri Jan 17 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.1-29]
- Remove standard template-{begin,end} fragments where possible. The
  default ones will be used in their place [charlieb 3295]
- Add tunable backoff parameters to diald configuration [charlieb 1396]

* Wed Jan 15 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.1-28]
- Fix open of wrong db in group-create-unix. [charlieb 4930]
- Display netmask and gatewayIP in review config panel only for static
  configuration [charlieb 1524, 3791]

* Fri Jan 10 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.1-27]
- in user-create-unix, hold lock longer - we need to wait until
  we have taken new user/group ids. [charlieb 4930]
- Convert group-create-unix similarly to user-create-unix -
  use esmith:xxxxDB, set Uid/Gid if not set, and use
  lock file. [charlieb 4930]
- Remove Uid/Gid handling from groups/useraccounts panel
  code. [charlieb 4930]

* Thu Jan  9 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.1-26]
- Rework user-create-unix to use esmith::xxxxDB libs. [charlieb 4930]
- Handle missing Gid, Uid, LastName and FirstName props in
  user-create-unix script. [charlieb 4930]
- Use lockfile around Uid allocation in user-create-unix [charlieb 4930]

* Wed Jan  8 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.1-25]
- Re-organise code in virtualdomains panel to fit more nicely
  in 80 columns. 
- Re-organise various bits of code in virtualdomains panel; an
  unintentional side-effect of doing an independent conversion
  to use DomainsDB and friends. 
- In virtualdomains panel, do not list any domains with a 
  "SystemDomain" property set to "yes". [charlieb 2670]

* Wed Jan  8 2003 Mark Knox <markk@e-smith.com>
- [4.13.1-24]
- Removed httpd-e-smith from action conf-startup [markk 6428]
- Made admin-conf Port template smarter [markk 6428]

* Mon Jan  6 2003 Mark Knox <markk@e-smith.com>
- [4.13.1-23]
- Removed httpd-e-smith configuration to its own package [markk 6428]

* Mon Jan  6 2003 Mark Knox <markk@e-smith.com>
- [4.13.1-22]
- Removed starterwebsite to its own package [markk 5509]

* Fri Jan  3 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.1-21]
- Unify user-password panel image with other server-manager panels.
  Change wording on header of user-password [gordonr 6407]

* Thu Jan  2 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.1-20]
- Removed fake dependency on e-smith-samba [gordonr 5509]

* Thu Jan  2 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.1-19]
- Split lpd startup into e-smith-LPRng [gordonr 5509]

* Thu Jan  2 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.1-18]
- Split smb startup into e-smith-samba [gordonr 5509]

* Thu Jan  2 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.1-17]
- Backing out the pam-pam_smbpass change for now. It's not properly
  handling addition/deletion of users and it's probably not all that
  bad to keep smbpasswd around [gordonr 6388]

* Thu Jan  2 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.1-16]
- Put back pam.d/passwd/template-begin with updated Copyright notice.
  We need the PAM header in that file [gordonr 6388]

* Thu Jan  2 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.1-15]
- Use pam-pam_smbpass to set Samba password so we don't always need 
  Samba installed and can save some code in e-smith-lib [gordonr 6388]

* Wed Jan  1 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.1-14]
- Rewrote console I18N section to use esmith::I18N [gordonr 5212]

* Wed Jan  1 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.1-13]
- Default packet filter logging to 'most' (all but RIP and SMB) [gordonr 6140]

* Wed Jan  1 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.1-12]
- And remove /etc/e-smith/locale/en-us/root [gordonr 5493]

* Wed Jan  1 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.1-11]
- Relocate /etc/e-smith/locale/en-us/root/etc -> /etc/e-smith/locale/en-us/etc
  for consistency with fr-ca [gordonr 5493]

* Mon Dec 30 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.13.1-10]
- Fixed syntax error in httpd-admin|ValidFrom processing [gordonr 6218]

* Fri Dec 27 2002 Mike Dickson <miked@e-smith.com>
- [4.13.1-09]
- minor updates to UI [miked 5494]

* Tue Dec 24 2002 Charlie Brady <charlieb@e-smith.com>
- [4.13.1-08]
- Fall back to 5000 in groups panel if MinUid not set. [charlieb 5768]

* Mon Dec 16 2002 Charlie Brady <charlieb@e-smith.com>
- [4.13.1-07]
- Work around apache prob with /255.255.255.255 for admin ValidFrom
  property. [charlieb 6218]

* Mon Dec 16 2002 Mike Dickson <miked@e-smith.com>
- [4.13.1-06]
- ui update [miked 5494]

* Tue Dec 10 2002 Michael Soulier <msoulier@e-smith.com>
- [4.13.1-05]
- No longer directly dependent on Mail::RFC822::Address. [msoulier 3388]

* Tue Dec 10 2002 Michael Soulier <msoulier@e-smith.com>
- [4.13.1-04]
- Moving the use of the Mail::RFC822::Address module into
  CGI::FormMagick::Validator::Network. [msoulier 3388]

* Mon Dec  9 2002 Michael Soulier <msoulier@e-smith.com>
- [4.13.1-03]
- Improved the validation of the email forward field in useraccounts.pm.
  [msoulier 3388]

* Mon Dec  9 2002 Mike Dickson <miked@e-smith.com>
- [4.13.1-02]
- ui update [miked 5494]

* Mon Dec  2 2002 Mike Dickson <miked@e-smith.com>
- [4.13.1-01]
- ui update  [miked 5494]

* Fri Nov 22 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.13.0-05]
- Process /etc/e-smith/web/panels/manager/html/header.htm [gordonr 5826]

* Thu Nov 21 2002 Mike Dickson <miked@e-smith.com>
- [4.13.0-04]
- update to new UI system [miked 5494]

* Thu Nov 21 2002 Charlie Brady <charlieb@e-smith.com>
- [4.13.0-03]
- Refer to correct template in fstab template-begin [charlieb RT#20021120008]
- Change resolv.conf to put nameserver on $LocalIP rather than loopback.
  [charlieb 4058]

* Thu Nov 14 2002 Charlie Brady <charlieb@e-smith.com>
- [4.13.0-02]
- Add server FQDN to main menu screen of console. [charlieb 3720]
- Undo recent bogus whitespace change.

* Wed Nov  6 2002 Charlie Brady <charlieb@e-smith.com>
- [4.13.0-01]
- Rolling development stream version to 4.13.0

* Fri Oct 25 2002 Mike Dickson <miked@e-smith.com>
- [4.12.1-02]
- added css mim type to mime.types template [miked 5301]

* Fri Oct 18 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.12.1-01]
- Tarball rebuild to cater for deleted file [gordonr 5246]

* Fri Oct 18 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.12.0-02]
- Delete network-modify-iptables - no longer required
  Replace with masq-adjust in network-{create,delete} [gordonr 5246]

* Fri Oct 11 2002 Charlie Brady <charlieb@e-smith.com>
- [4.12.0-01]
- Roll to maintained version number to 4.12.0

* Fri Oct 11 2002 Mark Knox <markk@e-smith.com>
- [4.11.31-06]
- Allow periods when modifying virtual domain descriptions [markk 5180]

* Wed Oct  9 2002 Mark Knox <markk@e-smith.com>
- [4.11.31-05]
- Added server resources directory and alias [markk 5100]

* Tue Oct  8 2002 Mark Knox <markk@e-smith.com>
- [4.11.31-04]
- Fix minor display issues [markk 5135]

* Fri Oct  4 2002 Mike Dickson <miked@e-smith.com>
- [4.11.31-03]
- fixed the ethernet driver selection order, shortend the driver string [miked 5052]

* Wed Oct  2 2002 Mark Knox <markk@e-smith.com>
- [4.11.31-02]
- Fix IE display problems in useraccounts, groups and ibays panels [markk 4891]

* Fri Sep 27 2002 Mark Knox <markk@e-smith.com>
- [4.11.31-01]
- Rolling due to patching problems again 

* Fri Sep 27 2002 Mark Knox <markk@e-smith.com>
- [4.11.30-13]
- Re-fix group desc to allow period [markk 3694]

* Thu Sep 26 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.30-12]
- Fix the OO API change in group-modify-unix code. [charlieb 4932]

* Wed Sep 25 2002 Mark Knox <markk@e-smith.com>
- [4.11.30-11]
- Fix up cdrom link on IDE systems with IDE CDROM that use SCSI emulation
  [markk 4563]

* Tue Sep 24 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.30-10]
- Change all console panels to 76x22 format to help translated text to fit.
  [charlieb 4191]

* Mon Sep 23 2002 Mark Knox <markk@e-smith.com>
- [4.11.30-09]
- Removed deprecated split on pipe from virtualdomains, refactored to 
  use ConfigDB and friends (as much as possible) [markk 3786]
- Removed stray braces on argument in admin.conf 80Aliases00 [markk 3786]

* Fri Sep 20 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.11.30-08]
- Fixed call to create_user_auto_pseudonyms in createuser.
  Removed redundant open() on AccountsDB
  Closed AccountsDB before calling user-delete [gordonr 4669]

* Fri Sep 20 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.30-07]
- Fix group-modify-unix to iterate during post-upgrade, not
  bootstrap-console-save. Compile error in script fixed as a side-effect.
  [charlieb 4932,1335]

* Fri Sep 20 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.30-06]
- Have group-modify-unix iterate over all groups during post-upgrade,
  so that groups file matches accounts db. [charlieb 4932]

* Wed Sep 18 2002 Michael Soulier <msoulier@e-smith.com>
- [4.11.30-05]
- Sort user list [msoulier 4911]

* Sat Sep 14 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.30-04]
- Change group of various ppp config files from daemon to root.
  [charlieb 4864]

* Fri Sep 13 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.11.30-03]
- Rationalise external DHCP to use /etc/dhcpc/dhcpcd.exe rather than
  a specific one per interface. The new dhcpcd does this by default.
  Thanks Shad Lords for the patch [gordonr 4889]

* Fri Sep 13 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.30-02]
- Fix broken i-bay section of httpd.conf. [charlieb 4872]

* Thu Sep 12 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.30-01]
- Change useraccounts.pm to correspond to API changes in esmith::AccountsDB.
  Remove existing pseudonyms before merging new properties in user modify
  code. [charlieb 4669]

* Thu Sep 12 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.29-05]
- Add missing parenthesis in previous change (why doesn't co2rpm
  run the code police before building package?). [charlieb 4713]

* Thu Sep 12 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.29-04]
- Minor refactoring of previous fix [markk 3786]
- Fix a number of test failures - test data hadn't kept pace with
  code changes.
- UnsavedChanges wasn't being set on deletion of config value in
  the console [charlieb 4713]

* Tue Sep 10 2002 Mark Knox <markk@e-smith.com>
- [4.11.29-03]
- Remove deprecated split on pipe [markk 3786]

* Fri Sep  6 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.11.29-02]
- Removed extraneous whitespace added in previous two patches [gordon 4663]

* Fri Sep  6 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.11.29-01]
- Rolling new version for same reason as 4.11.28-01 [gordonr 4663]

* Fri Sep  6 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.11.28-04]
- Reverted mime_magic additions - doesn't detect PNG files without
  additions to the /etc/httpd/conf/magic file and it all seems just
  too much trouble (and a minor performance hit on the web server).
  Added AddType for PNG files [gordonr 4663]

* Fri Sep  6 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.11.28-03]
- Enabled mod_mime_magic, added MimeMagicFile directive and deleted
  "ForceType application/octet-stream" directives from main Apache
  configuration to allow better type auto-detection [gordonr 4663]

* Fri Sep  6 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.11.28-02]
- Properly handle MaxUsers of zero [gordonr 4813]

* Fri Sep  6 2002 Tony Clayton <apc@e-smith.com>
- [4.11.28-01]
- rolling new version to fix problem with old rcs Id tag in deleted file
  [tonyc 3700]

* Fri Sep  6 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.27-15]
- Add /bin/bash2 to /etc/shells. Remove template-end text while we are
  at it. [charlieb 4785]

* Thu Sep  5 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.27-14]
- Obsolete 'hdparm'. Remove script, and delete db entry if found.
  See /etc/sysconfig/harddisks for a replacement. [charlieb 4781]

* Thu Sep  5 2002 Mark Knox <markk@e-smith.com>
- [4.11.27-13]
- Don't die in groups.pm if system() returns non-zero. [charlieb 3539]
- Obsolete deprecated split() from accounts DB in group-{create,modify}-unix 
  actions. [charlieb 3786]
- Remove merge-groups-file action - the groups contrib add-on is
  ancient history [charlieb 3786]
- Removed backticks from user-group-modify [markk 1335]
- Localise current ethernet setting in console [markk 3657]

* Tue Sep  3 2002 Mark Knox <markk@e-smith.com>
- [4.11.27-12]
- Handle user with no supplementary groups properly in user-group-modify
  [markk 1335]
- Include description of Router field in localnetworks panel [markk 1404]

* Tue Sep  3 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.27-11]
- Don't die in useraccounts.pm if system() returns non-zero. [charlieb 3539]
- Be sure to re-instantiate $accountsdb if system() returns non-zero.
  [charlieb 1335]
- Remove remnant conf-identd symlinks [charlieb 4435]
- Replace auth with oidentd in set-access-defaults script. [charlieb 4435]
- Fix new install failure of set-access-defaults. [charlieb 4763]

* Fri Aug 30 2002 Mark Knox <markk@e-smith.com>
- [4.11.27-10]
- Moved more group-modification code from panel to events [markk 1335]

* Thu Aug 29 2002 Mark Knox <markk@e-smith.com>
- [4.11.27-09]
- Moved group and pseudonym deletion code into user-delete event [markk 1335]

* Thu Aug 29 2002 Mark Knox <markk@e-smith.com>
- [4.11.27-08]
- Removed group-modify signal-event call from useraccounts.pm, moved into
  action script user-group-modify [markk 1335]
- Removed ibay signal-events from groups.pm, moved into action script
  group-ibay-modify in group-delete event [markk 1335]

* Wed Aug 28 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.27-07]
- Remove deprecated serviceControl calls in conf-start. [charlieb 4458]
- Remove pidentd related files - to be replaced by e-smith-oidentd
  RPM [charlieb 4435]

* Wed Aug 28 2002 Mark Knox <markk@e-smith.com>
- [4.11.27-06]
- Include field length limit in descriptive text in ibays panel [markk 3346]
- Use a variable for the default length to keep changes in one place [markk
  3346] 

* Tue Aug 27 2002 Mark Knox <markk@e-smith.com>
- [4.11.27-05]
- Allow period in group descriptions (but not as first char) [markk 3694]

* Mon Aug 26 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.27-04]
- Don't restart masq when adding or deleting a local network, just insert
  or remove rules. [charlieb 4501]

* Mon Aug 26 2002 Mark Knox <markk@e-smith.com>
- [4.11.27-03]
- Added group names to list on ibays panel [markk 3789]

* Mon Aug 26 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.27-02]
- Fix typo in review configuration panel ch caused DNS server to be blank.
  [charlieb 4717]

* Mon Aug 26 2002 Mark Knox <markk@e-smith.com>
- [4.11.27-01]
- Made head.tmpl aware of French [markk 3612]

* Thu Aug 22 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.26-01]
- Ensure that slocate group and ntp user exist after restore [charlieb 4415]

* Tue Aug 20 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.25-01]
- Bypass serviceControl in adjust-masq script, as it doesn't grok "adjust".
- Add missing "$0 adjust" in 86startdone fragment of masq script.
  [charlieb 4501]

* Mon Aug 19 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.24-01]
- Add new adjust-masq action script, and use it when packet filter access
  rules are adjusted. [charlieb 4501]
- Fix build problem with rc1.d symlinks. [charlieb 4562]

* Fri Aug 16 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.23-01]
- Shut down both apaches when we switch to single user mode [charlieb 4562]
- Don't set deprecated InitscriptsOrder property of services. [charlieb 4458]
- Migrate some sysctl settings from masq script to sysctl.conf. [charlieb 4624]
- Add "adjust" verb to masq script, to allow non-disruptive changes in packet
  filtering. [charlieb 4501]

* Tue Aug 13 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.22-01]
- Fix 0 account problem in count-active-user-accounts. [charlieb 4554]
- Create rpm owned symlinks in /etc/rc.d/rc7.d/ - prelude to obsoleting
  InitscriptsOrder property of services. [charlieb 4458]

* Tue Aug 13 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.21-01]
- Move conf-startup earlier in post-install and post-upgrade events.
  [charlieb 4552]
- Expand /etc/httpd/conf/{srm,access}.conf during bootstrap-console-save
  event. [charlieb 4575]

* Thu Aug  8 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.20-01]
- Roll back last change. I'd already added the function in a new 00Functions
  fragment. [charlieb 4499]

* Thu Aug  8 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.19-01]
- Add allow_tcp_in() function to 00start masq fragment, for use in other
  parts of the script. For use with connection tracking changes to
  the packet firewall. [charlieb 4499]

* Thu Aug  8 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.18-01]
- Make sure that apache doesn't read {access,srm}.conf. [charlieb 4575]

* Wed Aug  7 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.17-01]
- Remove net.ipv4.ip_always_defrag from /etc/sysctl.conf template.
  [charlieb 4558]

* Wed Jul 31 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.16-01]
- Make some additional ppp alias changes in modules.conf template, and
  remove now redundent "remove blank lines" fragment. [charlieb 4278]

* Thu Jul 25 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.15-01]
- Add Mitel headers to /etc/modules.conf and /etc/fstab, and remove any
  blank lines. Move 00readfile code to template-begin.
- Enable /dev/shm, for POSIX shared memory. [charlieb 2558].
- Make sure that appropriate ppp and GRE related aliases appear in
  modules.conf, so that PPTP VPN will work. [charlieb 4278]

* Tue Jul 23 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.14-01]
- Remove redundant setting of forward policy in packet filter. [charlieb 1268]

* Mon Jul 22 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.13-01]
- Fix minor typo and button size issue in ibays panel [markk 4419]
- Remove populate-bootstrap-console-save action [charlieb 1939]

* Fri Jul 19 2002 Mark Knox <markk@e-smith.com>
- [4.11.12-01]
- Fixed ScriptAlias in 20IbayContent [markk 4416]

* Thu Jul 18 2002 Mark Knox <markk@e-smith.com>
- [4.11.11-01]
- Catch addition of duplicate entries in remoteaccess 'valid from' section
  [markk 4272]
- Allow removal of 'valid from' without netmasks [markk 4272]

* Wed Jul 17 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.10-01]
- Convert /etc/rc.d/init.d/masq fragments from ipchains to iptables
  syntax. Remove pointless template-end fragment. [charlieb 1268]

* Tue Jul 16 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.9-01]
- Migrate "rtl8139" ethernet module assignments to "8139too".
  [charlieb 4166]

* Fri Jul 12 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.8-01]
- Remove rmmod-ide-scsi action, to be replaced by a tweaking of
  /etc/rc.d/rc.sysinit in the initscripts package. [charlieb 4174]

* Fri Jul 12 2002 Mark Knox <markk@e-smith.com>
- [4.11.7-01]
- Allow modification of usernames containing hyphens [markk 4340]

* Fri Jul 12 2002 Mark Knox <markk@e-smith.com>
- [4.11.6-01]
- Changed online manual link to edocs site [markk 3545]

* Fri Jul  5 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.5-01]
- Handle missing netmask gracefully in remote access to manager part of
  remote access panel (default to 255.255.255.255) [charlieb 4117]

* Tue Jul  2 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.4-01]
- Add "alias net-pf-15 ipsec" to /etc/modules.conf template so that ipsec
  module is loaded on demand. [charlieb 4224]

* Sun Jun 30 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.3-01]
- Add empty /etc/identd.masq/template-begin file. [charlieb 4207]

* Wed Jun 19 2002 Mark Knox <markk@e-smith.com>
- [4.11.2-01]
- Move SSL mutex and cache out of /var/log [markk 3830]

* Wed Jun 19 2002 Mark Knox <markk@e-smith.com>
- [4.11.1-01]
- Changed "www" to "www." in review.pm [markk 3821]
- Fixed problem with displaying network router/mask in review config 
  [markk 3828]
- Fixed unlocalised string when adding local network, and applied a 
  validation patch [markk 3825]

* Wed Jun  5 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.0-01]
- Changing version to maintained stream number to 4.11.0

* Mon Jun  3 2002 Mark Knox <markk@e-smith.com>
- [4.10.5-01]
- Pass the right variable name to validation message [markk 3802]

* Mon Jun  3 2002 Charlie Brady <charlieb@e-smith.com>
- [4.10.4-01]
- Set default access type for i-bays to "none". [charlieb 3796]

* Sun Jun  2 2002 Charlie Brady <charlieb@e-smith.com>
- [4.10.3-01]
- Remove bogus arguments to genUsers() call in groups panel. [charlieb 3773]
- Add DHCP start and end to review configuration panel [charlieb 3790]

* Sun Jun  2 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.10.2-01]
- Removed 'nonblank' validation from optional fields. e-smith-lib now
  strips pipes from properties. Upped dependency versions on e-smith-lib
  and e-smith-formmagick versions [gordonr 3752]

* Sun Jun  2 2002 Charlie Brady <charlieb@e-smith.com>
- [4.10.1-01]
- Fixes to group handling in user create and user modify panel functions -
  we need to save group membership and we should also save them before calling
  signal-event.  [charlieb 3773]

* Fri May 31 2002 Charlie Brady <charlieb@e-smith.com>
- [4.10.0-01]
- Changing version to maintained stream number to 4.10.0

* Fri May 31 2002 Mark Knox <markk@e-smith.com>
- [4.9.189-01]
- Catch user-password entries of non-user accounts [markk 3767]

* Fri May 31 2002 Mark Knox <markk@e-smith.com>
- [4.9.188-01]
- Pass action=modify when modifying an ibay [markk 3769]

* Fri May 31 2002 Tony Clayton <apc@e-smith.com>
- [4.9.187-01]
- remove debug from review.pm [tonyc 3766]

* Fri May 31 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.186-01]
- Revert conf-routes to ignore remoteVPNSubnet entries
  [gordonr 3349]

* Thu May 30 2002 Mark Knox <markk@e-smith.com>
- [4.9.185-01]
- Delete ibay accounts after running delete event [markk 3742]
- Display create/modify form based on 'action' variable [markk 3742]

* Thu May 30 2002 Mark Knox <markk@e-smith.com>
- [4.9.184-01]
- Swapped localisations of ERROR_DELETING and SUCCESSFULLY_DELETED in
  ibays lexicon [markk 3742]

* Thu May 30 2002 Mark Knox <markk@e-smith.com>
- [4.9.183-01]
- Small patch to useraccounts to stop uninit value warnings [markk 3628]

* Thu May 30 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.182-01]
- Fixed typo in userpassword - veify -> verify [gordonr 3739]

* Thu May 30 2002 Charlie Brady <charlieb@e-smith.com>
- [4.9.181-01]
- Change eq test to pattern match in timeout change in /etc/resolv.conf
  template, to catch servergateway-private mode. [charlieb 3673]

* Wed May 29 2002 Mark Knox <markk@e-smith.com>
- [4.9.180-01]
- Minor fixes to the new ibay validation [markk 3690]
- Fixed up a few ibays.pm tests [markk 3690]

* Wed May 29 2002 Mark Knox <markk@e-smith.com>
- [4.9.179-01]
- Improved account name checking in ibays panel to match previous release's
  behaviour [markk 3690]

* Wed May 29 2002 Mark Knox <markk@e-smith.com>
- [4.9.178-01]
- "Tokenized" new error messages and added to useraccounts lexicon [markk 3628]

* Tue May 28 2002 Mark Knox <markk@e-smith.com>
- [4.9.177-01]
- Removed stray semi and quote from localnetworks lexicon [markk 3686]

* Tue May 28 2002 Mark Knox <markk@e-smith.com>
- [4.9.176-01]
- Compute and pass the 'simpleMask' parameter in localnetworks success
  message [markk 3686]

* Tue May 28 2002 Mark Knox <markk@e-smith.com>
- [4.9.175-01]
- Pass arguments to localise for localnetworks success messages [markk 3686]

* Mon May 27 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.174-01]
- Allow e-mail address without @ signs in emailForward to allow
  forwarding to local addresses [gordonr 3628]

* Mon May 27 2002 Charlie Brady <charlieb@e-smith.com>
- [4.9.173-01]
- Add timeout option to /etc/resolv.conf for modem dialout
  links. [charlieb 3673]

* Mon May 27 2002 Mark Knox <markk@e-smith.com>
- [4.9.172-01]
- Stop session info leakage when modifying users as well. [markk 3649]
- Stuff accountdb record data into CGI form unless we have CGI data already
  when modifying users [markk 3649]

* Mon May 27 2002 Mark Knox <markk@e-smith.com>
- [4.9.171-01]
- In useraccounts, don't pass all parameters in URL (we have a session token
  for that) and only pass token where needed. [markk 3649]

* Sat May 25 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.170-01]
- And fix useraccounts tests as well. The pseudonym tests were looking
  for {first,last}Name rather than {First,Last}Name [gordonr 3624]

* Sat May 25 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.169-01]
- Don't display ibay table when there are no i-bays [gordonr 3404]
- Added networks.conf, domains.conf and fixed environment for tests
  in FormMagick panels. All FM panels in e-smith-base except useraccounts 
  now pass their tests [gordonr 3624]

* Fri May 24 2002 Tony Clayton <apc@e-smith.com>
- [4.9.168-01]
- fix pseudonym routine in useraccounts.pm [tonyc 3664]
- remove unused username_clash validation routine [tonyc 3664]
- numerous new english l10n's for useraccounts panel [tonyc 3664]
- other minor useraccounts fixes [tonyc 3664]

* Fri May 24 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.167-01]
- Add two more lines to Ethernet card detection screen [gordonr 3644]

* Fri May 24 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.166-01]
- Fixed = to eq in swapped/normal screen [gordonr 3656]

* Fri May 24 2002 Mark Knox <markk@e-smith.com>
- [4.9.165-01]
- Localised a string and fixed syntax err in groups.pm [markk 3610]
- Fixed up some more logic and syntax errors in groups.pm [markk 3160]

* Fri May 24 2002 Mark Knox <markk@e-smith.com>
- [4.9.164-01]
- Made ibay password fields really password fields [markk 3561]
- Avoid passing all CGI args & session key around when not necessary in 
  ibays.pm [markk 3651]
- Fixed up errors in various tests in {groups,ibays,localnetworks}.pm and 
  useraccounts.pm [markk]

* Fri May 24 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.163-01]
- Dummy entry to check co2rpm - no code change [gordonr 3565]

* Thu May 23 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.162-01]
- RPM rebuild forced by cvsroot2rpm

* Thu May 23 2002 Mark Knox <markk@e-smith.com>
- [4.9.161-01]
- In useraccounts.pm, add_user_to_groups is a method of AccountsDB [markk]

* Thu May 23 2002 Mark Knox <markk@e-smith.com>
- [4.9.160-01]
- Fixed up ugly table headings in useraccounts and localnetworks [markk 3611]

* Thu May 23 2002 Tony Clayton <apc@e-smith.com>
- [4.9.159-01]
- fix localise call in useraccounts::validate_name() [tonyc 3628]

* Wed May 22 2002 Tony Clayton <apc@e-smith.com>
- [4.9.158-01]
- remove debug statements from localnetworks.pm [tonyc 3613]
- fix uninitialized value in conf-routes [tonyc 3614]

* Wed May 22 2002 Tony Clayton <apc@e-smith.com>
- [4.9.157-01]
- added useraccounts check for account conflict [tonyc 3628]

* Wed May 22 2002 Tony Clayton <apc@e-smith.com>
- [4.9.156-01]
- fixed groups panel field validation [tonyc 3610]
- added useraccounts account length validation [tonyc 3628]
- added missing english l10n for groups field validation error [tonyc 3610]
- added group "Everyone" to ibay panel listbox [tonyc 3610]

* Wed May 22 2002 Tony Clayton <apc@e-smith.com>
- [4.9.155-01]
- s/halt/shutdown/ in reboot.pm to get shutdowns working again [tonyc 3600]

* Wed May 22 2002 Mark Knox <markk@e-smith.com>
- [4.9.154-01]
- Applied new password validation logic to user-password panel [markk 3592]

* Wed May 22 2002 Mark Knox <markk@e-smith.com>
- [4.9.153-01]
- Moved password validation functions to e-smith-formmagick and added variable
  strength password checking to password, ibays and useraccounts panels [markk
  3592]
- Added action to configure password strength check that matches v5.1.2 
  behaviour [markk 3592]

* Wed May 22 2002 Charlie Brady <charlieb@e-smith.com>
- [4.9.152-01]
- Remove creation of obsolete Samba config db entries, from
  conf-migrate-variables and reset-config. [Charlieb 3160]

* Wed May 22 2002 Tony Clayton <apc@e-smith.com>
- [4.9.151-01]
- that's cgi-bin/support not /cgi-bin/support [tonyc 3585]

* Tue May 21 2002 Tony Clayton <apc@e-smith.com>
- [4.9.150-01]
- Link to cgi-bin/support from main pages [tonyc 3585]

* Mon May 20 2002 Mark Knox <markk@e-smith.com>
- [4.9.149-01]
- English localisation of ibay validation error message [markk 3548]

* Mon May 20 2002 Mark Knox <markk@e-smith.com>
- [4.9.148-01]
- Added validation of ibay name [markk 3548]

* Mon May 20 2002 Mark Knox <markk@e-smith.com>
- [4.9.147-01]
- Don't let the handle_user_accounts override our status message [markk 3314]

* Mon May 20 2002 Mark Knox <markk@e-smith.com>
- [4.9.146-01]
- Fix account name validation regex [markk 3314]

* Mon May 20 2002 Mark Knox <markk@e-smith.com>
- [4.9.145-01]
- Add account name validation [markk 3314]

* Sat May 18 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.144-01]
- Remove stray '1' from localnetworks and bold phrase [gordonr 3563]

* Sat May 18 2002 Charlie Brady <charlieb@e-smith.com>
- [4.9.143-01]
- It's SYSLOGD_OPTIONS, not SYSLOGD_OPTS. [charlieb 3476]
- Move fstab-conf back to post-{install,upgrade} and do it early. We
  need the quota options to run quotacheck [gordonr 3439]

* Sat May 18 2002 Charlie Brady <charlieb@e-smith.com>
- [4.9.142-01]
- Fix usb failures at first time bootup. Need to generate dependency map for
  run time UP (and SMP) kernel(s), not BOOT kernel at post-install time.
  [charlieb 3572]

* Sat May 18 2002 Mark Knox <markk@e-smith.com>
- [4.9.141-01]
- Quick patch to useraccounts for check max users on resetting password
  [markk 3134]

* Sat May 18 2002 Charlie Brady <charlieb@e-smith.com>
- [4.9.140-01]
- Woops, klogd option needs to be "-c 1 -2", not "2 -c 1" [charlieb 3476]

* Sat May 18 2002 Charlie Brady <charlieb@e-smith.com>
- [4.9.139-01]
- Change SYSLOG_OPTS to SYSLOGD_OPTS in /etc/sysconfig/syslog to accommodate
  change in RedHat's sysklogd. [charlieb]
- Add klogdOptions fragment to set options used when klogd is run.
  [charlieb 3549, 3476]

* Sat May 18 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.138-01]
- Check MaxUsers on account unlock [gordonr 3134]

* Sat May 18 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.137-01]
- Only expand fstab in bootstrap-console-save. We don't need to boot
  with quotas enabled after an install as enable-quotas will enable
  them for us. [gordonr 3439]

* Sat May 18 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.136-01]
- Expand /etc/fstab after enabling quotas so we don't see a bootup
  warning [gordonr 3439]

* Sat May 18 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.135-01]
- Reverted changes in 4.9.133 - was due to e-smith-lib breakage [gordonr 3439]

* Sat May 18 2002 Mark Knox <markk@e-smith.com>
- [4.9.134-01]
- Added password verification and validation, localisation of message [markk
  3488]
- Added ibay_description validator [markk 3404]

* Sat May 18 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.133-01]
- Fully qualify processTemplate() call in fstab-conf and add use POSIX
  [gordonr 3439]

* Sat May 18 2002 Mark Knox <markk@e-smith.com>
- [4.9.132-01]
- Increased e-smith-lib dep to 1.9.47 [markk 3404]
- Removed get_next_uid sub from ibays and useraccounts panels [markk 3404]

* Sat May 18 2002 Tony Clayton <apc@e-smith.com>
- [4.9.131-01]
- s/add_user_pseudonyms/create_user_pseudonyms/ in useraccounts.pm [tonyc 3517]

* Sat May 18 2002 Mark Knox <markk@e-smith.com>
- [4.9.130-01]
- Localised string NO_ADDITIONAL_NETWORKS [markk 3525]

* Sat May 18 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.129-01]
- Relocated /etc/fstab template from e-smith-quota and expand /etc/fstab
  in post-{install,upgrade} before system boot [gordonr 3439]

* Fri May 17 2002 Mark Knox <markk@e-smith.com>
- [4.9.128-01]
- Fixed test logic in ibays panel reset_password routine [markk 3488]

* Fri May 17 2002 Mark Knox <markk@e-smith.com>
- [4.9.127-01]
- Bolded table headings in ibays panel [markk 3404]
- Fixed bad xml in ibays panel (name -> id in field tag) [markk 3488]


* Fri May 17 2002 Mark Knox <markk@e-smith.com>
- [4.9.126-01]
- Cosmetic fixes to ibays panel. Added get_next_uid routine which was 
  preventing manipulation of ibay accounts. [markk 3404]

* Fri May 17 2002 Tony Clayton <apc@e-smith.com>
- [4.9.125-01]
- co2rpm didn't finish for 4.9.123-01.  committing now.

* Fri May 17 2002 Kirrily Robert <skud@e-smith.com>
- [4.9.124-01]
- Removed whitespace from ibay panel buttons [skud 3514]

* Fri May 17 2002 Tony Clayton <apc@e-smith.com>
- [4.9.123-01]
- unify header templates into head.tmpl, and footer templates into foot.tmpl,
  and create symlinks in build section [tonyc 3223]
- localise footers for french [tonyc 3223,3095]

* Fri May 17 2002 Mark Knox <markk@e-smith.com>
- [4.9.122-01]
- Added missing comma in ibays.pm (fixes syntax error) [markk 3503]

* Fri May 17 2002 Mark Knox <markk@e-smith.com>
- [4.9.121-01]
- Bold table headings in group panel [markk 3503]

* Fri May 17 2002 Kirrily Robert <skud@e-smith.com>
- [4.9.120-01]
- Added localisations for ibays panel dropdowns [skud 3505]

* Fri May 17 2002 Adrian Chung <mac@e-smith.com>
- [4.9.119-01]
- Modify conf-routes to look for RemoteVPNSubnet, rather than remoteVPNSubnet.
  [mac 3349]

* Fri May 17 2002 Kirrily Robert <skud@e-smith.com>
- [4.9.118-01]
- Added space to password error message [skud 3403]

* Thu May 16 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.117-01]
- Disable tmpfs in /etc/fstab as it shows up as a failure at
  boot time [gordonr 3472]

* Thu May 16 2002 Kirrily Robert <skud@e-smith.com>
- [4.9.116-01]
- Helps to actually export the validation routine [skud 3403]

* Thu May 16 2002 Kirrily Robert <skud@e-smith.com>
- [4.9.115-01]
- Changed password validation to use cracklib [skud 3403]

* Thu May 16 2002 Tony Clayton <apc@e-smith.com>
- [4.9.114-01]
- Set primary/files/* to world-readable in init-accounts [tonyc 3400]

* Thu May 16 2002 Adrian Chung <mac@e-smith.com>
- [4.9.113-01]
- Remove local network entries in localnetworks panel after changing type to
  network-deleted and signalling network-delete. [mac 3496].

* Thu May 16 2002 Kirrily Robert <skud@e-smith.com>
- [4.9.112-01]
- Fixed quoting problem on groups table [skud 3490]

* Thu May 16 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.111-01]
- Use list format for warn message [gordonr 3359]

* Thu May 16 2002 Kirrily Robert <skud@e-smith.com>
- [4.9.110-01]
- Added border to groups table [skud 3490]

* Thu May 16 2002 Kirrily Robert <skud@e-smith.com>
- [4.9.109-01]
- Fixed "reset password" no-op in ibays panel [skud 3488]
- Extra space between two strings in welcome page [gordonr 3483]
- Add colon/space after "warn" when Internet test fails [gordonr 3359]
- Removed extraneous "print" from test Internet access which showed
  up as a stray "1" (print within a print) [gordonr 3359]

* Wed May 15 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.108-01]
- Dequote KEYBOARDTYPE and KEYTABLE from /etc/sysconfig/keyboard and
  allow grep to return into an array [gordonr 3120]

* Wed May 15 2002 Mark Knox <markk@e-smith.com>
- [4.9.107-01]
- Tweaking the language pattern to ignore case and separator in pleasewait
  [markk 3250]

* Wed May 15 2002 Mark Knox <markk@e-smith.com>
- [4.9.106-01]
- Localised string "There are no entries yet" in remoteaccess [markk 3309]

* Wed May 15 2002 Kirrily Robert <skud@e-smith.com>
- [4.9.105-01]
- Fixed bug in displaying table of localnetworks [skud 3407]
- Added admin group to dropdown list that's shown on teh create/modify
  ibays panel [skud 3404]

* Mon May 13 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.104-01]
- Handle relative symlinks in clean-rc7.d [gordonr 2604]

* Mon May 13 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.103-01]
- Put Yes on Left in yesno pages [gordonr 3399]

* Mon May 13 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.102-01]
- Fixed outdated comment about AccountDB in 00sanity-accounts.t [gordonr 3287]
- Strip out /255.255.255.255 netmask from single host ValidFrom entries.
  Apache doesn't like such entries [gordonr 3435]

* Wed May  8 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.101-01]
- Removed duplicate footer from {index,initial}.cgi [gordonr 3223]
- Added version number to noframes_foot.tmpl [gordonr 3223]
- Removed noframes_foot.tmpl and moved to e-smith-release [gordonr 3223]

* Wed May  8 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.100-01]
- Removed /etc/e-smith/web/common/foot.tmpl Temporarily moved to
  e-smith-release package [gordonr 3223, 3371]

* Wed May  8 2002 Mark Knox <markk@e-smith.com>
- [4.9.99-01]
- Make sure passwords really do match in password panel [markk 3308]

* Wed May  8 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.98-01]
- Current sshd|PasswordAuthentication and sshd|PermitRootLogin settings 
  should be displayed regardless of whether the service is enabled or disabled
  [gordonr 3293]

* Wed May  8 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.97-01]
- Finally move determine-release late enough in post-install [gordonr 2297]

* Tue May  7 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.96-01]
- determine-release needs to run after config db is created [gordonr 2297]

* Tue May  7 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.95-01]
- Fixed deprecated defined() tests which were generating warnings in
  remoteaccess.pm [skud 3358]
- Don't migrate an empty DNSPrimaryIP [gordonr 3375]

* Tue May  7 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.94-01]
- Missing use esmith::util [gordonr 3372]

* Tue May  7 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.93-01]
- Changed foot.tmpl to grab sysconfig|ReleaseVersion from the 
  config db [gordonr 3223]
- Use Back/Next on password_page [gordonr 3369]
- Nav bar entries for virtualdomains [gordonr 3155]

* Mon May  6 2002 Charlie Brady <charlieb@e-smith.com>
- [4.9.92-01]
- Set access defaults should configure smtpfront-qmail rather than
  the not-yet-existent meta-service smtpd. [charlieb 2604]
- Remove references to smtpfwdd, in test data and in documentation
  of e-smith-service. [charlieb 2604]

* Mon May  6 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.91-01]
- Capture version of e-smith-release in post-{install,upgrade} and
  store in sysconfig=configuration|ReleaseVersion|5.5alpha5 [gordonr 2297]

* Mon May  6 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.90-01]
- Added 'use esmith::util;' for httpd.conf template fragment 
  01localAccessString [jay 3360]
- Added footer to all web panels - INCOMPLETE [gordonr 3223]
- TODO: This should be a template and needs to evaluate release version.
  However, CGI::FormMagick won't evaluate the template running in taint
  mode. We could also make use of esmith::cgi::genFooter() [gordonr 3223]

* Mon May  6 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.89-01]
- PPPoE account name screen didn't localise properly [gordonr 3028]
- Localise status reports setting in review configuration [gordonr 3028]
- Ok -> OK in console [gordonr 3028]
- Lexicon en -> en-us in groups [markk 3317]

* Fri May  3 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.88-01]
- Check lexicons before packaging [gordonr 3155]

* Fri May  3 2002 Adrian Chung <adrianc@e-smith.com>
- [4.9.87-01]
- Make useraccounts panel verify that new password inputs match. [mac 3315]

* Thu May  2 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.86-01]
- Header and footer on groups [gordonr 3316]

* Thu May  2 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.85-01]
- review lexicon en->en-us [gordonr 3313]

* Thu May  2 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.84-01]
- Header, footer, nav bar for review [gordonr 3313]

* Thu May  2 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.83-01]
- Expanded text area on PPPoE account page [markk 3329]
- Add return; calls to the groups.pm module so that extraneous '1' characters
  disappear from panel. [mac 3220]

* Wed May  1 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.82-01]
- esmith::AccountDB -> esmith::AccountsDB [schwern 3287]

* Tue Apr 30 2002 Charlie Brady <charlieb@e-smith.com>
- [4.9.81-01]
- Add code to reset-config to initialise DynDNS service to
  disabled [charlieb 2737]

* Tue Apr 30 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.80-01]
- Fixed changelog below - bug reference for sshd|PasswordAuthentication
- Remove ancient template-{begin,end} from /etc/hosts [gordonr 3295]
- Refer to 'Secure shell' in remoteaccess panel [gordonr 3294]

* Tue Apr 30 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.79-01]
- Removed redundant ip-change/S80conf-http [gordonr 2319]
- Removed redundant FIXME comments from console [gordonr 3255]
- Changed sshd|PasswordAuthentication default to "yes" as before [gordonr 3293]

* Tue Apr 30 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.78-01]
- Expand lynx.cfg in {bootstrap-,}console-save to allow for a language
  choice menu in the console in the future [gordonr 3279]

* Tue Apr 30 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.77-01]
- Added dependency on lynx since the console requires it [gordonr 3279]
- Added template for /etc/lynx.cfg to set PREFERRED_LANGUAGE [gordonr 3279]

* Tue Apr 30 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.76-01]
- Only clean dangling symlinks from rc7.d [gordonr 2604]

* Mon Apr 29 2002 Charlie Brady <charlieb@e-smith.com>
- [4.9.75-01]
- Make sure that DynDNS key exists in config DB, with default status disabled.

* Mon Apr 29 2002 Mark Knox <markk@e-smith.com>
- [4.9.74-01]
- Added FM version of review with nav bar entries [skud, gordonr 3027]
- Changed ibays lexicon to en-us and added nav bar entries [gordonr 3027]
- Changed virtualdomains lexicon to en-us [markk 3260]
- Pass arguments to localise() in virtualdomains, removed extra whitespace
  on trans entries for buttons [markk 3260]

* Fri Apr 26 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.73-01]
- Allow blank MSN and skip page in any case (only for dial-in) [gordonr 3255]

* Fri Apr 26 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.72-01]
- Properly initialise connection policies [gordonr 3238]

* Thu Apr 25 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.71-01]
- Simplistic L10N of pleasewait page [gordonr 3250]
- Added <META HTTP-EQUIV="refresh"> header, Refresh: 1 [gordonr 2765, 2326]
- Headers and footers on online-manual [gordonr 3223]
- Nav bar entries on all panels [gordonr 3155]

* Thu Apr 25 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.70-01]
- Rename internal-{initial,index}.cgi in respository [gordonr 3201]

* Wed Apr 24 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.69-01]
- No need to call them internal-{initial,index}.html - they aren't
  linked into the cgi-bin directory. Just give them normal names [gordonr 3201]

* Wed Apr 24 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.68-01]
- Made {initial,index}.html into scripts and relocated to
  functions/internal-{index,initial}.cgi linked as 
  {index,initial}.cgi in the panels/manager/html directory.
  Enabled ExecCGI in panels/manager/{cgi-bin,html} [gordonr 3201]

* Mon Apr 22 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.67-01]
- Swap yes and no buttons in yesno_page [gordonr 3028]
- Add USER_CREATED/MODIFIED lexicons to useraccounts panel [adrianc 1404]
- Modify checkMaxUsers to properly check MaxUsers value [adrianc]

* Fri Apr 19 2002 Michael Schwern <schwern@e-smith.com>
- [4.9.66-01]
- Moving IP functions in console to esmith::util::network for easier
  testing [schwern 3080]

* Fri Apr 19 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.65-01]
- Extra space on server-only gateway address [gordonr 3028]

* Fri Apr 19 2002 Michael Schwern <schwern@e-smith.com>
- [4.9.64-01]
- Semi-intellegently changing existing hosts when the system name changes
  [schwern 3045]

* Fri Apr 19 2002 Michael Schwern <schwern@e-smith.com>
- [4.9.63-01]
- Zero-padded IP addresses are now accepted and stripped [schwern 3080]
- Forgot dependency on perl-gettext [schwern]
- Removed USERID logging from xinetd.conf [markk 3125]

* Thu Apr 18 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.62-01]
- Removed - Skud tags from localnetworks panel name and URL [gordonr 3027]

* Thu Apr 18 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.61-01]
- Added left and right options for all page types [gordonr 3028]

* Thu Apr 18 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.60-01]
- Added auto-detect for a few more Eicon DIVA ISDN cards [gordonr 3186]
- Extra space required in call to gettext() for Cracklib output [[gordonr 3028]

* Thu Apr 18 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.59-01]
- Added Jesse's i18n'd groups panel [skud #3032]
- Actually display yes/no in yesno_pages [gordonr 3168]
- Missing parens in gettext() strings [gordonr 3028]
- Moved gettext() initialisation outside BEGIN block. Doing that, plus
  a getLocale() call causes perl -c to fail on test machines as we don't
  have access to /home/e-smith/configuration. It doesn't need to be in
  the BEGIN block in any case [gordonr 3028]

* Wed Apr 17 2002 Adrian Chung <adrianc@e-smith.com>
- [4.9.58-01]
- Added missing end parens in some phrases [gordonr 3028]
- i18n userpassword panel.  Merge old static HTML form elements page with CGI
  script. [mac 3146]
- Update /user-password and /e-smith-password links to point straight at
  userpassword CGI script. [mac 3146]

* Wed Apr 17 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.57-01]
- Added i18n'd localnetworks panel [skud #3027]
- Added conf-httpd and restart-httpd-graceful to event remoteaccess-update
  (needed by new ValidFrom editor in panel) [markk]
- Changed language to en-us in localnetworks [gordonr 3027]
- Update console to set smb|DomainMaster instead of SambaDomainMaster [gordonr]
- Final (I hope) gettext() review with Mark [gordonr 3027]

* Wed Apr 17 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.56-01]
- console: Made use of ConfigDB::getLocale() [gordonr 3120]
- console: Text rewording in ISDN panels from Chris Elliott [gordonr 3120]

* Tue Apr 16 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.55-01]
- Rearranged spacing on Cracklib line so "qu'il" doesn't have a space 
  [gordonr 3028]
- Missing gettext() on return value in reboot/shutdown option [gordonr 3028]
- Added sysconfig-update action to parse /etc/sysconfig/ files and store 
  language/keyboard settings in config db [markk 3120]
- Moved prototype server-console.po to en_US [gordonr 3028]
- Made use esmith::FormMagick localisation in navigation bar [gordonr 3155]

* Mon Apr 15 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.54-01]
- Added /etc/e-smith/locale/etc/e-smith/web/functions/README to say
  why we are not currently splitting the en-us lexicon out from the
  panel and to make the directory as a place-marker. [gordonr 3031]

* Mon Apr 15 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.53-01]
- Modified lexicons to "en-us" from "en" [gordonr 3031]

* Mon Apr 15 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.52-01]
- Added L10 for Cracklib output [gordonr #3167]
- Minor rewording for ISDN MSN page (still hidden) [gordonr #3090]

* Fri Apr 12 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.51-01]
- Some L10N formatting and missing L10N on manual Ethernet selection
  [gordonr #3028]

* Fri Apr 12 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.50-01]
- Localize keep/Yes/No in menus and check localized responses [gordonr #3028]

* Thu Apr 11 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.49-01]
- gettext() calls to testInternet() output [gordonr #3028]
- gettext() to "please try again" [gordonr #3028]

* Thu Apr 11 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.48-01]
- Fixed typo in sprintf/gettext parentheses [gordonr #3028]

* Thu Apr 11 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.47-01]
- Widened format string in displayConfiguration for French [gordonr #3028]
- Replaced interpolated $ifName with %s and sprintf [gordonr #3028]

* Thu Apr 11 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.46-01]
- Minor cleanups in console - missing gettext()s found when merging
  French L10N strings [gordonr  #3028]

* Wed Apr 10 2002 Mark Knox <markk@e-smith.com>
- [4.9.45-01]
- Migrated count-active-user-accounts to new esmith:{Account,Config}DB.
- Make useraccounts panel check for existence of sysconfig|MaxUsers property
  and complain if the number of user accounts exceeds this value. [mac #3134]
- Implemented UI in remoteaccess panel to manage list of remote networks 
  with access to server manager [markk 2099]

* Tue Apr  9 2002 Mark Knox <markk@e-smith.com>
- [4.9.44-01]
- Moved 30WebmailAliases fragment to e-smith-imp [markk]

* Mon Apr  8 2002 Michael Schwern <schwern@e-smith.com>
- [4.9.43-01]
- Online manual panel is now i18n'd [skud #3032]
- Added alias for /horde in VirtualHosts/30WebmailAliases (needed by IMP)
  [markk 2825]

* Fri Apr 05 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.42-01]
- Update dhcpd.conf templates for migration of SambaDomainMaster ->
  smb|DomainMaster property [adrianc]
- Update console to set smb|ServerName property when system name is set [adrianc]
- Rewrote set-access-defaults using new ConfigDB and added tests [gordonr #2812]

* Wed Apr 03 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.41-01]
- remoteaccess: Allow blank PPTP field to equal zero [markk]

* Wed Apr 03 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.40-01]
- useraccounts: Fixed table formatting for IE [gordonr]

* Wed Apr 03 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.39-01]
- Adjusted and added Copyright headers [gordonr]

* Wed Apr 03 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.38-01]
- Added nonblank validation to admin password panel [gordonr]
- Removed 'password' strength validation from useraccounts. There should
  be a confid db setting to enable strong password checking [gordonr]

* Wed Apr 03 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.37-01]
- Display "account is locked" rather than "Lock Account..." link if so [gordonr]

* Wed Apr 03 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.36-01]
- EXPORT lock_account, remove_account, reset_password which are used
  by the useraccounts panel [gordonr]
- Fix call to delete when deleting the user [gordonr]
- Display 'There are no user accounts' instead of table if no users [gordonr]
- Don't create an acctName property for the user (that's the db key) [gordonr]

* Wed Apr 03 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.35-01]
- Various bug fixes to useraccounts and useraccounts.pm [gordonr/skud]
- Various bug fixes to remoteaccess [markk]

* Wed Apr 03 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.34-01]
- Fixed linkage issues between remoteaccess panel and remoteaccess.pm so
  FTP/SSH settings work properly. [markk]
- Changed pptp validation function to allow 0 sessions. [markk] 
- Add 80NameVirtualHosts fragment back in, to make virtual domains work 
  again. [adrianc]
- mv httpd.conf/NameVirtualHosts/VirtualHosts/* httpd.conf/VirtualHosts/* 
  [gordonr]

* Tue Apr 02 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.33-01]
- Merge and obsolete e-smith-mod_ssl back into e-smith-base [gordonr]

* Tue Apr 02 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.32-01]
- console: layout cleanups [gordonr]
- httpd.conf: Revised 80VirtualHosts after discussion with Tony [gordonr]

* Tue Apr 02 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.31-01]
- init-accounts: Sigh, was previously checked in broken [gordonr]

* Tue Apr 02 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.30-01]
- fixed blatant brokenness in 80VirtualHosts fragment [tonyc]
- password: Added localized SAVE button [gordonr]
- password: Added strength checking to admin password (already existed for 
   useraccounts) [gordonr]
- remoteaccess: Localized SAVE button [gordonr]
- remoteaccess: Use "openssh" throughout visible screen [gordonr]
- useraccounts: Localized RESET_DESC2 [gordonr]

* Tue Apr 02 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.29-01]
- console: redo displayConfiguration() to allow for L10N of strings
  by removing hard-coded formatting [gordonr #3028]

* Thu Mar 28 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.28-01]
- httpd.conf: 35Listen80 needs to listen on 0.0.0.0 in serveronly and
  servergateway (non-private) [gordonr]

* Thu Mar 28 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.27-01]
- Formatting in console [gordonr #3028]

* Thu Mar 28 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.26-01]
- Auto-extract console messages into the en locale [gordonr #3028]

* Thu Mar 28 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.25-01]
- Skip ISDN_MSN screen [gordonr #3090]
- Rewording in console with Alex [gordonr]

* Thu Mar 28 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.24-01]
- Minor warning cleanups and bugfixes in useraccounts [skud]
- Set default for useraccounts to deliver mail locally [gordonr]

* Thu Mar 28 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.23-01]
- Fixed bad putback of 80VirtualHosts fix
- Minor rewording in ISDN MSN area from Chris Elliott [gordonr #3090]

* Wed Mar 27 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.22-01]
- httpd.conf 80VirtualHosts template should exit cleanly if none are
  defined

* Wed Mar 27 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.21-01]
- console: Liberal sprinklings of gettext(). Ugly, but it means we can use
  xgettext() to pull the relevant strings out for translation [gordonr #3028]
- TODO: displayConfiguration() needs to have a formatter applied to
  handle gettext() output. The static formatting isn't going to work
  if the returned strings differ in size from the English ones (as is
  to be expected).
- console: Reword MSN section [gordonr #3090]

* Tue Mar 26 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.20-01]
- console: Add startup for gettext/L10N support [gordonr #3028]

* Tue Mar 26 2002 Kirrily Robert <skud@e-smith.com>
- [4.9.19-01]
- manager: added i18n'd versions of remoteaccess, reboot, starterwebsite
  [skud #3032]
- manager: fixed some bugs in useraccounts [skud #3027]
- console: Only modify UnsavedChanges if value being stored differs [gordonr]

* Tue Mar 26 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.18-01]
- Added note to console that esmith::config::unsaved should not modify 
  UnsavedChanges if the value being stored has not changed
- Remove displayManual() from console [gordonr #2587]
- Major rework (incomplete) of console to allow for I18N [gordonr #3028]
  - Replaced most of the direct screen() calls with routines to display 
  the appropriate type of screen. These routines should check their
  arguments, but currently do not. The text parameters and the menu 
  items can be passed through gettext() for L10N support.
  TODO: 
  - Deal with variables interpolated in text sections - many can just be
  removed with rewording
  - Check arguments and tests for new functions
  - Deal with the variable length menus for ethernet driver, etc.
  - Add gettext() setup guff
  - Further refactoring of the new routines

* Fri Mar 15 2002 Charlie Brady <charlieb@e-smith.com>
- [4.9.17-01]
- In apache configuration, remove Listen directives, except for
  servergateway mode with access set to private. [charlieb #2319]
- In apache configuration, change virtual domain setups to use
  wildcard IP address of 0.0.0.0. Omit NameVirtualHost directives.
  [charlieb #2319]
- Remove restart-httpd-full from ip-change event. No longer required.
  [charlieb #2319]

* Thu Mar 14 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.16-01]
- CVS gotcha - need "cvs update -d" to catch directory changes by
  others. Picking up Charlie's httpd.conf rearrangements.

* Thu Mar 14 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.15-01]
- Rolled in FormMagicked admin password panel [skud]
- Removed '- skud' from useraccounts panel [skud]

* Wed Mar 13 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.14-01]
- Created a swag of potentially empty directories [gordonr 2885]

* Wed Mar 13 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.13-01]
- Fix to console for #2885 - ignore warnings when calling screen [schwern]

* Tue Mar 12 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.12-01]
- Workaround for #2885 - redirect console warnings to /var/log/consolelog
  until the cause of the warnings is determined [gordonr]

* Mon Mar 11 2002 Charlie Brady <charlieb@e-smith.com>
- [4.9.11-01]
- Various small fixes to useraccounts panel [skud]
- Move httpd.conf#NameVirtualHosts and httpd.conf#VirtualHosts into 
  subdirectory templates, before re-arranging to solve httpd start
  race condition #2319 [charlieb]. Update e-smith-lib dependency version
  as a result.

* Thu Feb 28 2002 Kirrily Robert <skud@e-smith.com>
- [4.9.10-01]
- Fixed some syntax errors in esmith::FormMagick::Panel::useraccounts.pm
  [skud]
- Updated dependencies [skud]

* Thu Feb 28 2002 Kirrily Robert <skud@e-smith.com>
- [4.9.9-01]
- Rewrite of useraccounts panel to use FormMagick [skud #2594]
- Added 'buildtests' to %build, to generate test suite [skud]
- Depends on esmith-formmagick 0.1.3 and e-smith-lib 1.9.7 [skud]
- Build depends on e-smith-devtools >= 1.6.6 [skud]
- Add action script to remove ide-scsi module at boot time (within
  "signal-event local"). [charlieb #1416]

* Wed Feb 20 2002 Mark Knox <markk@e-smith.com>
- [4.9.8-01]
- Re-built from clean checkout. Seems a stray file (80Aliases00) was left
  in the tree on the last build. Also, corrected bug numbers in previous
  log entry. 

* Wed Feb 20 2002 Mark Knox <markk@e-smith.com> 
- [4.9.7-01]
- Added 'Requires' on e-smith-lib >= 1.9.4 [tonyc #1799]
- Use new NameVirtualHost and VirtualHost templates for httpd.conf 
  [tonyc #1799]
- minor refactoring of httpd.conf template fragments [tonyc]
- released as 4.9.7-01

* Sat Feb 16 2002 Charlie Brady <charlieb@e-smith.com>
- [4.9.6-01]
- Fix two compile errors in console - weren't picked up by the "code police"
  check on the 4.9.0-01 change. Why not?

* Fri Feb 15 2002 Kirrily Robert <skud@e-smith.com>
- [4.9.5-01]
- Added dhcpc template files ignored by rpm2cvs

* Fri Feb 15 2002 Kirrily Robert <skud@e-smith.com>
- [4.9.4-01]
- Fixed createlinks further -- added safe_symlink routine.

* Fri Feb 15 2002 Kirrily Robert <skud@e-smith.com>
- [4.9.3-01]
- Fixed some typos in creatlinks script for Gordon :) s/bindir/cgibin/

* Fri Feb 15 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.2-01]
- Auto-create cgi-bin directory for panel links

* Fri Feb 15 2002 Kirrily Robert <skud@e-smith.com>
- [4.9.1-01]
- rollRPM: Rolled version number to 4.9.1-01. Includes patches up to 4.9.0-04.

* Fri Feb 15 2002 Charlie Brady <charlieb@e-smith.com>
- [4.9.0-03]
- Migrate Samba* config variables to properties of the smb service db entry.

* Thu Feb 14 2002 Charlie Brady <charlieb@e-smith.com>
- [4.9.0-02]
- Rename "custom" dynamicDNS script to "custom.example" so that custom scripts
  are not clobbered on upgrade.
- Add restart-masq action to console-save event, so that DHCP rules are
  set up correctly.

* Mon Feb 4 2002 Charlie Brady <charlieb@e-smith.com>
- [4.9.0-01]
- Migrate Dynamic DNS variables into properties of the DynDNS service.
- Move migration of obsolete DNSPrimaryIP to Forwarder1 property of named
  and DNSSecondaryIP to Forwarder2 from console to conf-migrate-variables.

* Mon Feb 4 2002 Charlie Brady <charlieb@e-smith.com>
- [4.9.0-01]
- rollRPM: Rolled version number to 4.9.0-01. Includes patches up to 4.8.0-18.

* Tue Jan 29 2002 Adrian Chung <adrianc@e-smith.com>
- [4.8.0-18]
- Fix logrotate event actions to rotate only files and not symlinks.
- Fix purge-old-logs action to remove old symlinks that had previously
  been rotated.

* Wed Jan 23 2002 Charlie Brady <charlieb@e-smith.com>
- [4.8.0-17]
- Add "common", "icons" and "files" to list of reserved account names, as
  they are Aliases in the apache configuration. See #2226.

* Tue Jan 22 2002 Charlie Brady <charlieb@e-smith.com>
- [4.8.0-16]
- Fix console so that proxy settings can be updated if enabled. See #2560.

* Fri Jan 11 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.8.0-15]
- Open diald.ctl for write access. See #2448

* Fri Jan 11 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.8.0-14]
- Adjusted Copyright dates on static HTML pages

* Thu Jan 10 2002 Charlie Brady <charlieb@e-smith.com>
- [4.8.0-13]
- Do dated log rotation of ssl_engine_log for both copies of apache.

* Wed Jan 09 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.8.0-12]
- Adjusted Copyright notices in console. See #2465

* Wed Jan 09 2002 Charlie Brady <charlieb@e-smith.com>
- [4.8.0-11]
- Make sure that diald controlled passive ISDN link handles an unexpected
  disconnection gracefully. See #2448.
- Instantiate /etc/ppp/ip-down.local script, which calls "signal-event ip-down".
  Use this hook for the diald change referred to above.

* Fri Jan 04 2002 Charlie Brady <charlieb@e-smith.com>
- [4.8.0-10]
- Change the way that depmod is run in conf-modules. Run it for every installed
  kernel, and run it using "-F /boot/System.map-x.y.z x.y.z". Forward port
  from 4.7.1-62.
- Use name param as well as user param for ippp, which should fix the CHAP
  authentication problem. Forward port from 4.7.1-62.
- Re-implement Internet test using LWP and POST method, to avoid problem
  with excessive length of request URL. Forward port from 4.7.1-63.
- Fix stray ' error in console configuration report text. Forward port
  from 4.7.1-63.

* Thu Jan  3 2002 Adrian Chung <adrianc@e-smith.com>
- [4.8.0-09]
- Cleanup webmail alias generation in 80Aliases00.
- Now only be done once per VirtualHost.

* Thu Jan  3 2002 Adrian Chung <adrianc@e-smith.com>
- [4.8.0-08]
- Change purge-old-logs to use $_ instead of File::Find::name.
- File::Find chdir's into each directory as it processes them, so
  a relative path won't work -- needs to be either absolute, or
  just the filename.
- Add $! error to error message string.

* Fri Dec 21 2001 Charlie Brady <charlieb@e-smith.com>
- [4.8.0-7]
- Forward port missed changes from 4.6.1-19 and 4.6.1-21
  - chmod +x /etc/cron.weekly/refresh-ddns
  - Corrected path to update-dns in /etc/cron.weekly/refresh-ddns

* Mon Dec 17 2001 Charlie Brady <charlieb@e-smith.com>
- [4.8.0-6]
- Fix two cosmetic problems in console, as reported by Robert Devantier.

* Wed Dec 12 2001 Charlie Brady <charlieb@e-smith.com>
- [4.8.0-5]
- Fix autodetect of Asustek ISDN card, add -ac and -pc options for ipppd
- move noipdefault and ipcp-accept-* options from /etc/ppp/ioptions to
  /etc/ippp.conf template, so that all options settings are done in one place.
- Force "ipparam diald" in /etc/ippp.conf, regardless of IpppdOptions
  customisation.
- Fix set-gateway-ip script so that it does not log perl warning if $6 is
  not defined.
- Remove 4.7.* changelog entries. See SME Server Version 5.1 release notes
  for change descriptions.

* Tue Dec 11 2001 Adrian Chung <adrianc@e-smith.com>
- [4.8.0-04]
- Make sure e-smith-base creates and owns /etc/e-smith/events/local

* Tue Dec 11 2001 Adrian Chung <adrianc@e-smith.com>
- [4.8.0-03]
- Fixing purge-old-logs to instead of check for a byte size > 100,000
  check for a matching filename format.

* Tue Dec 11 2001 Charlie Brady <charlieb@e-smith.com>
- [4.8.0-02]
- Small fixes to connect and isdn.hangup scripts so that diald can control ISDN.
- Fix up prep section to avoid repeating stuff which is already in the tarball.

* Tue Dec 11 2001 Adrian Chung <mac@e-smith.com>
- [4.8.0-01]
- rollRPM: Rolled version number to 4.8.0-01.

* Mon Aug 20 2001 Adrian Chung <adrianc@e-smith.com>
- [4.6.0-12]
- Change calculation of hosts allow string in 10globals fragment
  of smb.conf
- Calculate @access early in template generation.

* Mon Aug 20 2001 Gordon Rowell <gordonr@e-smith.com>
- [4.6.0-11]
- Changed dependency on e-smith-lib version

* Fri Aug 17 2001 gordonr
- [4.6.0-10]
- Autorebuild by rebuildRPM

* Wed Aug 15 2001 Charlie Brady <charlieb@e-smith.com>
- [4.6.0-09]
- Fix code in init-accounts which checks 'type' for expected system accounts
- Omit S40hdparm symlink which is just immediately deleted anyway
- Use /etc/rc6.d and /etc/rc7.d rather than /etc/rc.d/rcx.d directories

* Wed Aug 15 2001 Charlie Brady <charlieb@e-smith.com>
- [4.6.0-08]
- Delay restart of web server until after HTML is displayed, when creating,
  modifying or deleting a virtual domain. Do this by removing
  restart-httpd-full from the event direcetories, and running the action
  after the text is displayed by showInitial(). Add some text to inform
  the user that the web server is being restarted.

* Wed Aug 15 2001 Adrian Chung <adrianc@e-smith.com>
- [4.6.0-07]
- Change e-smith-common to allow from all access.

* Wed Aug 15 2001 Charlie Brady <charlieb@e-smith.com>
- [4.6.0-06]
- Reserve server-manager, user-password and server-manual URL names.

* Tue Aug 14 2001 Gordon Rowell <gordonr@e-smith.com>
- [4.6.0-05]
- Removed remnants of telnet PermitRootLogin from remoteaccess panel
  telnet access as root is now disabled, and can only be set directly in
  the configuration database

* Tue Aug 14 2001 Gordon Rowell <gordonr@e-smith.com>
- [4.6.0-04]
- Typo and formatting error on two console screens

* Tue Aug 14 2001 Charlie Brady <charlieb@e-smith.com>
- [4.6.0-03]
- Warn when accounts entries don't match the expected type
- Mark existing /etc/passwd accounts as "existing", not "system"

* Fri Aug 10 2001 Jason Miller <jmiller@e-smith.com>
- [4.6.0-02]
- Changes to panels and console to use a trailing slash (/) on all urls as
  part of marketing/branding standards 

* Wed Aug 8 2001 Charlie Brady <charlieb@e-smith.com>
- [4.6.0-01]
- Rolled version number to 4.6.0-01. Includes patches upto 4.5.1-37.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1

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
