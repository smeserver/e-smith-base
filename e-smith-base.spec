Summary: e-smith server and gateway - base module
%define name e-smith-base
Name: %{name}
%define version 4.18.1
%define release 14
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch1: e-smith-base-4.18.1-fixgettext.patch
Patch2: e-smith-base-4.18.1-deleteorder.patch
Patch3: e-smith-base-4.18.1-insertmode.patch
Patch4: e-smith-base-4.18.1-freebusy.patch
Patch5: e-smith-base-4.18.1-frames.patch
Patch6: e-smith-base-4.18.1-quitconsole.patch
Patch7: e-smith-base-4.18.1-freebusy.patch2
Patch8: e-smith-base-4.18.1-dateManip.patch
Patch9: e-smith-base-4.18.1-ethernetlist.patch
Patch10: e-smith-base-4.18.1-add2general.patch
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
Requires: mod_auth_external
Requires: e-smith-lib >= 1.18.0-19
Requires: server-manager-images, server-manager
Requires: e-smith-formmagick >= 1.4.0-12
Requires: initscripts >= 6.67-1es17
Requires: e-smith-daemontools >= 1.7.1-04
Requires: perl(Locale::gettext)
Requires: perl(Crypt::Cracklib)
Requires: perl(Date::Manip)
Requires: perl(Data::UUID)
Requires: perl(Net::IPv4Addr)
Requires: /usr/sbin/irqbalance
Requires: /usr/sbin/cpuspeed
Requires: /sbin/microcode_ctl
Requires: dbus
Requires: hal
Requires: acpid
Requires: whiptail
Requires: rssh
Requires: bridge-utils
Requires: vconfig
Requires: e-smith-bootloader
Requires: mdadm
Requires: pv
Requires: pam_abl
Obsoletes: rlinetd, e-smith-mod_ssl
Obsoletes: e-smith-serial-console
Obsoletes: sshell
Obsoletes: e-smith-rp-pppoe
%if "%{?rhel}" == "5"
Obsoletes: perl-Data-UUID
%endif
BuildRequires: perl, perl(Test::Inline) >= 0.12
BuildRequires: e-smith-devtools >= 1.13.1-03
BuildRequires: gettext
%ifarch i386
Requires: apmd
%endif

%define dbfiles accounts configuration domains hosts networks
AutoReqProv: no

%description
e-smith server and gateway software - base module.

%changelog
* Fri Jul 4 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 4.18.1-14
- Add common <base> tags to e-smith-formmagick's general [SME: 4279]

* Sun Apr 27 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 4.18.1-13
- Add common <base> tags to e-smith-formmagick's general [SME: 4279]

* Wed Apr 23 2008 Shad L. Lords <slords@mail.com> 4.18.1-12
- Fix for > 5 nics detected [SME: 4232]

* Tue Apr 22 2008 Shad L. Lords <slords@mail.com> 4.18.1-11
- Remove use of Date::Manip from ssl.crt [SME: 3155]

* Sat Apr 19 2008 Shad L. Lords <slords@mail.com> 4.18.1-10
- Fix FreeBusy param when disabled [SME: 1806]
- Remove .orig file [SME: 4228]

* Wed Apr 2 2008 Shad L. Lords <slords@mail.com> 4.18.1-9
- Remove quitConsole from menu [SME: 4154]

* Wed Apr 2 2008 Shad L. Lords <slords@mail.com> 4.18.1-8
- Really fix free/busy in usermanager [SME: 4157]

* Wed Apr 2 2008 Shad L. Lords <slords@mail.com> 4.18.1-7
- Use frames in elinks [SME: 4156]
- Set homepage for elinks [SME: 4160]

* Wed Apr 2 2008 Shad L. Lords <slords@mail.com> 4.18.1-6
- Fix free/busy field in useraccounts [SME: 4157]

* Tue Apr 1 2008 Shad L. Lords <slords@mail.com> 4.18.1-5
- Add free/busy URL entry to help kronolith contribs [SME: 1806]

* Fri Mar 28 2008 Shad L. Lords <slords@mail.com> 4.18.1-4
- Fix insert_mode for elinks on el5 platform [SME: 4127]

* Wed Mar 26 2008 Shad L. Lords <slords@mail.com> 4.18.1-3
- Set accounts to deleted before template expansion [SME: 4122]

* Wed Mar 26 2008 Shad L. Lords <slords@mail.com> 4.18.1-2
- Fix gettext strings returned by password checks [SME: 4104]

* Wed Mar 26 2008 Shad L. Lords <slords@mail.com> 4.18.1-1
- Roll new stable stream consolidating patches.

* Mon Mar 24 2008 Shad L. Lords <slords@mail.com> 4.18.0-104
- Finish removing pleasewait [SME: 126]

* Tue Mar 18 2008 Shad L. Lords <slords@mail.com> 4.18.0-103
- Add gettext to console titles. [SME: 4089]

* Sat Mar 15 2008 Stephen Noble <support@dungog.net> 4.18.0-102
- Minor translation fixes [SME: 4058] [SME: 4059]

* Wed Mar 12 2008 Shad L. Lords <slords@mail.com> 4.18.0-101
- Remove tests for removed FORM_TITLE's [SME: 4050]

* Wed Mar 12 2008 Shad L. Lords <slords@mail.com> 4.18.0-100
- Cleanup SAVE/ADD tag mixup [SME: 4045]

* Sat Mar 10 2008 Shad L. Lords <slords@mail.com> 4.18-99
- Fix dyndns custom gettext [SME: 4032]

* Sat Mar 07 2008 Stephen Noble <support@dungog.net> 4.18-98
- revised gettext messages [SME: 631]

* Sat Mar 07 2008 Stephen Noble <support@dungog.net> 4.18-97
- gettext messages [SME: 631]

* Sat Mar 07 2008 Stephen Noble <support@dungog.net> 4.18-96
- remove duplicate system password has been changed [SME: 3974]

* Sat Mar 07 2008 Stephen Noble <support@dungog.net> 4.18-95
- EthernetAssign shouldn't be translated [SME: 3947]

* Sun Feb 17 2008 Stephen Noble <support@dungog.net> 4.18-94
- Remove pleasewait function [SME: 126]

* Sun Feb 17 2008 Stephen Noble <support@dungog.net> 4.18-93
- fix gettext formatting in three files [SME: 3938]

* Wed Feb 13 2008 chris burnat <devlist@burnat.com> 4.18-92
- Fix creation of usernames and pseudonyms with one character
- [SME: 2451]

* Wed Feb 13 2008 Stephen Noble <support@dungog.net> 4.18-91
- Remove <base> tags now in general [SME: 3911]

* Sun Feb 10 2008 Stephen Noble <support@dungog.net> 4.18-90
- Remove duplicate <base> entries [SME: 3894]

* Sat Feb 09 2008 Stephen Noble <support@dungog.net> 4.18-89
- remove unused ROUTER_DESC token from lexicon [SME: 3879]

* Sat Jan 12 2008 Shad L. Lords <slords@mail.com> 4.18-88
- remove default of 1400 MTU for interfaces [SME: 549]

* Wed Jan 09 2008 Stephen Noble <support@dungog.net> 4.18-87
- db prop to dissociate admin password from root in useraccounts.pm [SME: 3117]

* Wed Jan 09 2008 Stephen Noble <support@dungog.net> 4.18-86
- pptp connections setting mtu/mru > 1400 [SME: 549]

* Tue Jan 08 2008 Stephen Noble <support@dungog.net> 4.18-85
- console to strength validate password choice on first entry [SME: 3131]

* Tue Jan 08 2008 Stephen Noble <support@dungog.net> 4.18-84
- Auto-mount USB REV-drive as usbdisk [SME: 2972]

* Sun Jan 06 2008 Stephen Noble <support@dungog.net> 4.18-83
- ignore error returns from tar [SME: 3127]

* Sun Jan 06 2008 Stephen Noble <support@dungog.net> 4.18-82
- Use esmith::util::validatePassword on console [SME: 2173]

* Mon Dec 24 2007 Gavin Weight <gweight@gmail.com> 4.18.0-81
- Link smartd.conf to bootstrap-save-console and console-save. [SME: 1445]

* Mon Dec 24 2007 Stephen Noble <support@dungog.net> 4.18-80
- Add smartd as a disabled service with template [SME: 1445]

* Sun Dec 16 2007 Shad L. Lords <slords@mail.com> 4.18.0-79
- Lock user accounts with usermod instead of passwd [SME: 3595]

* Sun Dec 16 2007 Gavin Weight <gweight@gmail.com> 4.18.0-78
- Add symlink to fr-fr locale. [SME: 3648]

* Mon Nov 12 2007 Shad L. Lords <slords@mail.com> 4.18.0-77
- Add fix for varying partition sizes in add_raid [SME: 3547]

* Sun Nov 11 2007 Gavin Weight <gweight@gmail.com> 4.18.0-76
- Fix removal of Corporate DNS from console.  [SME: 3532]

* Fri Nov 02 2007 Gavin Weight <gweight@gmail.com> 4.18.0-75
- Remove previous change, applied to wrong package.  [SME: 3512]

* Fri Nov 02 2007 Gavin Weight <gweight@gmail.com> 4.18.0-74
- Add WPAD feature for DHCP (Thanks Hector Perez).  [SME: 3512]

* Tue Oct 16 2007 Gavin Weight <gweight@gmail.com> 4.18.0-73
- Make non-Removable pseudonyms point to admin when reassigned.  [SME: 2214]

* Sun Oct 14 2007 Gavin Weight <gweight@gmail.com> 4.18.0-72
- Adjust success text when changing admin password. [SME: 2442]

* Thu Oct 11 2007 Charlie Brady <charlie_brady@mitel.com> 4.18.0-71
- Fix comparison of expected to actual SSL cert data. Also change
  truncation point for email address from 40 chars to 64. [SME: 1736].
  [Note that -70 was inadvertently skipped.]

* Tue Sep 11 2007 Gavin Weight <gweight@gmail.com> 4.18.0-69
- Move httpd logrotate.d directory to e-smith-apache. [SME: 3380]

* Tue Sep 11 2007 Gavin Weight <gweight@gmail.com> 4.18.0-68
- Rename in logrotate.d directory apache to httpd. [SME: 3380]

* Fri Sep 07 2007 Charlie Brady <charlie_brady@mitel.com> 4.18.0-67
- Fix pod in groups.pm file. [SME: 3379]

* Wed Aug 22 2007 Charlie Brady <charlie_brady@mitel.com> 4.18.0-66
- Relax restrictions on restore devices, to allow CDR and DVDR.
  [SME: 3126]

* Fri Aug 03 2007 Charlie Brady <charlie_brady@mitel.com> 4.18.0-65
- Ensure that depmod is run for all installed kernels. [SME: 3235]

* Wed Jul 04 2007 Charlie Brady <charlie_brady@mitel.com> 4.18.0-64
- Really really clear devices variable [SME: 3116]

* Sun Jul 1 2007 Shad L. Lords <slords@mail.com> 4.18.0-63
- Really clear devices variable [SME: 3116]

* Sun Jul 1 2007 Shad L. Lords <slords@mail.com> 4.18.0-62
- Clean up loop var and mount point for backup/restore [SME: 3116]

* Thu Jun 28 2007 Shad L. Lords <slords@mail.com> 4.18.0-61
- Improve usb backup error reporting [SME: 2772]

* Tue Jun 26 2007 Gavin Weight <gweight@gmail.com> 4.18.0-60
- Move the pam.d ftp/proftpd templates to e-smith-proftpd.
  [SME: 2762]

* Tue Jun 19 2007 Charlie Brady <charlie_brady@mitel.com> 4.18.0-59
- Have nonetworkdrivers script exit silently if kmodule bin not found.
  [SME: 2549]

* Mon Jun 11 2007 Shad L. Lords <slords@mail.com> 4.18.0-58
- Start messagebus/haldaemon so restore works [SME: 3058]

* Sun Jun 10 2007 Stephen Noble <support@dungog.net> 4.18.0-57
- expand /etc/pam.d/login [SME: 2831]

* Wed Jun 06 2007 Charlie Brady <charlie_brady@mitel.com> 4.18.0-56
- Prevent backout from console config during initial setup.
  [SME: 2540]

* Sun Jun 3 2007 Shad L. Lords <slords@mail.com> 4.18.0-55
- Clean up some more newlines [SME: 3035]
- Make raid failures more verbose [SME: 3032]
- Fix add_drive_to_raid and partition issues [SME: 2155, 2232]

* Wed May 30 2007 Gavin Weight <gweight@gmail.com> 4.18.0-54
- Update noraid text and add newline after text. [SME: 3035]

* Thu May 24 2007 Shad L. Lords <slords@mail.com> 4.18.0-53
- Don't use cracklib in system-auth [SME: 2686]

* Fri May 18 2007 Shad L. Lords <slords@mail.com> 4.18.0-52
- Use correct lib for modules

* Thu May 17 2007 Shad L. Lords <slords@mail.com> 4.18.0-51
- Updates to support xenU instance

* Wed May 9 2007 Shad L. Lords <slords@mail.com> 4.18.0-50
- Updates to support SME Server 8

* Sat May 05 2007 Gavin Weight <gweight@gmail.com> 4.18.0-49
- Fix service match RE in /sbin/e-smith/service. [SME: 2959]

* Sun Apr 29 2007 Shad L. Lords <slords@mail.com>
- Clean up spec so package can be built by koji/plague

* Sun Apr 29 2007 Shad L. Lords <slords@mail.com> 4.18.0-48
- Change to dist for tagging release
- Only include apmd for i386 platforms

* Fri Apr 27 2007 Charlie Brady <charlie_brady@mitel.com> 4.18.0-47
- Validate GatewayIP address more carefully. [SME: 2928]

* Sat Apr 14 2007 Stephen Noble <support@dungog.net> 4.18.0-46
- Field to change ssh port [SME: 2382]

* Sat Apr 14 2007 Stephen Noble <support@dungog.net> 4.18.0-45
- Change fm to self in remoteaccess.pm [SME: 2382]

* Fri Apr 13 2007 Shad L. Lords <slords@mail.com> 4.18.0-44
- Make configuration dbs config(noreplace) [SME: 2527]

* Fri Apr 13 2007 Shad L. Lords <slords@mail.com> 4.18.0-43
- Adjust perm for dhcpd.conf again [SME: 2715]

* Thu Apr 12 2007 Shad L. Lords <slords@mail.com> 4.18.0-42
- Put usbback patch back in. [SME: 2483]

* Thu Apr 12 2007 Stephen Noble <support@dungog.net> 4.18.0-41
- Remove enable slocate patch [SME: 102]

* Thu Apr 12 2007 Stephen Noble <support@dungog.net> 4.18.0-40
- Change Try Again to gettext(Back) in perform backup [SME: 2483]

* Thu Apr 12 2007 Stephen Noble <support@dungog.net> 4.18.0-39
- Enable slocate in /etc/updatedb.conf [SME: 102]

* Wed Apr 11 2007 Stephen Noble <support@dungog.net> 4.18.0-38
- Make console text consistent 'Please stand by' [SME: 2493]

* Wed Apr 11 2007 Stephen Noble <support@dungog.net> 4.18.0-37
- Fix missing en-au & en-nz language noise. [SME: 2093]

* Wed Apr 11 2007 Stephen Noble <support@dungog.net> 4.18.0-36
- Fix missing list items for console [SME: 2642]

* Mon Apr 09 2007 Shad L. Lords <slords@mail.com> 4.18.0-35
- Don't attempt to add_raid_device if no raid [SME: 2484]

* Fri Apr 06 2007 Shad L. Lords <slords@mail.com> 4.18.0-34
- Add fix for perms on dhcpd.conf file [SME: 2715]

* Fri Apr 06 2007 Shad L. Lords <slords@mail.com> 4.18.0-33
- Remove fix for ftpusers.  Belongs in e-smith-proftpd. [SME: 2841]

* Fri Apr 06 2007 Shad L. Lords <slords@mail.com> 4.18.0-32
- Fix permissions on ftpusers file [SME: 2841]
- Fix permissions on pwauth file [SME: 2842]

* Thu Apr 05 2007 Shad L. Lords <slords@mail.com> 4.18.0-31
- Simplify depmod call in conf-modules [SME: 2554]

* Wed Apr 04 2007 Charlie Brady <charlie_brady@mitel.com> 4.18.0-30
- Fix login pam configuration file. TODO - expand the template
  during bootstrap-console-save. [SME: 2831]

* Mon Mar 26 2007 Charlie Brady <charlie_brady@mitel.com> 4.18.0-29
- Add rotate_timestamped_logfiles action, split from
  generic_template_expand. [SME: 2795]

* Thu Mar 22 2007 Shad L. Lords <slords@mail.com> 4.18.0-28
- Fix rc.e-smith to work with el4 and el5 [SME: 2510]

* Mon Mar 19 2007 Shad L. Lords <slords@mail.com> 4.18.0-27
- Add missing elements in prior pam updates [SME: 2551]

* Mon Mar 19 2007 Shad L. Lords <slords@mail.com> 4.18.0-26
- Update pam_stack to new include for el5 [SME: 2551]

* Thu Mar 08 2007 Gavin Weight <gweight@gmail.com> 4.18.0-25
- Fix missing en-gb language noise. [SME: 2633]

* Thu Mar 08 2007 Shad L. Lords <slords@mail.com> 4.18.0-24
- Call cropLeft function correctly in crt expansion [SME: 1689]

* Wed Mar 07 2007 Shad L. Lords <slords@mail.com> 4.18.0-23
- Make elinks display correctly with xterm display [SME: 444]

* Wed Mar 07 2007 Shad L. Lords <slords@mail.com> 4.18.0-22
- Add db override for crt common name [SME: 1689]

* Wed Mar 07 2007 Shad L. Lords <slords@mail.com> 4.18.0-21
- Default adding drive to raid to no [SME: 2644]

* Tue Mar 06 2007 Shad L. Lords <slords@mail.com> 4.18.0-20
- Allow nics to swap if different LAN chosen [SME: 2612]

* Tue Mar 06 2007 Shad L. Lords <slords@mail.com> 4.18.0-19
- Default WAN NIC to the *other* NIC than the one selected for LAN [SME: 2612]

* Tue Mar 06 2007 Charlie Brady <charlie_brady@mitel.com> 4.18.0-18
- Combine two similar loops in selectEthernet and break overly
  long string constant. [SME: 2612]

* Tue Mar 06 2007 Shad L. Lords <slords@mail.com> 4.18.0-17
- Fix network selection dialog to include all drivers. [SME: 2612]

* Thu Mar 01 2007 Charlie Brady <charlie_brady@mitel.com> 4.18.0-16
- Fix run.static file in wan service directory. [SME: 2580]

* Fri Feb 23 2007 Shad L. Lords <slords@mail.com> 4.18.0-15
- Fix glob for selecting backup devices. [SME: 2521]

* Fri Feb 23 2007 Shad L. Lords <slords@mail.com> 4.18.0-14
- User new console infobox for console backup. [SME: 2533]

* Thu Feb 22 2007 Charlie Brady <charlie_brady@mitel.com> 4.18.0-13
- Use new esmith::console::infobox widget in console. [SME: 2533]

* Fri Feb 16 2007 Shad L. Lords <slords@mail.com> 4.18.0-12
- Change runsvctrl to sv to support runit v1.7.x

* Fri Feb 16 2007 Charlie Brady <charlie_brady@mitel.com> 4.18.0-11
- Restate microcode_ctl/irqbalance/cpuspeed dependencies. [SME: 2490]

* Sun Feb 11 2007 Shad L. Lords <slords@mail.com> 4.18.0-10
- Set db value for external ip before expanding templates [SME: 1977]

* Sun Feb 11 2007 Shad L. Lords <slords@mail.com> 4.18.0-9
- Do better detection of possible devices for backup/restore [SME: 2317]

* Sun Feb 11 2007 Shad L. Lords <slords@mail.com> 4.18.0-8
- Set ENV{HOME} so mysql dump works for backup [SME: 2412]

* Wed Feb 07 2007 Charlie Brady <charlieb@e-smith.com> 4.18.0-7
- Remove unused remnant dhcpcd templates. [SME: 2445]

* Wed Feb 07 2007 Charlie Brady <charlieb@e-smith.com> 4.18.0-6
- Configure elinks to obey cache control directives. I have
  no idea why that would not be the default! [SME: 2443]

* Tue Jan 30 2007 Shad L. Lords <slords@mail.com> 4.18.0-5
- Ensure gateway dev is correct for server-only [SME: 2404]

* Mon Jan 29 2007 Shad L. Lords <slords@mail.com> 4.18.0-4
- Add cancel button to backup/restore panels [SME: 2393]

* Mon Jan 29 2007 Shad L. Lords <slords@mail.com> 4.18.0-3
- Add console backup to USB [SME: 2317]

* Sun Jan 28 2007 Shad L. Lords <slords@mail.com> 4.18.0-2
- Fix backtitle for saving changes [SME: 2328]

* Fri Jan 26 2007 Shad L. Lords <slords@mail.com> 4.18.0-1
- Roll stable stream. [SME: 2328]

* Tue Jan 23 2007 Charlie Brady <charlieb@e-smith.com> 4.17.2-8
- Remove unused ifcfg-log:0 templates. [SME: 2368]

* Tue Jan 23 2007 Charlie Brady <charlieb@e-smith.com> 4.17.2-7
- Add template fragments to allow forcing of ethernet negotiation
  parameters [SME: 2362]

* Tue Jan 23 2007 Charlie Brady <charlieb@e-smith.com> 4.17.2-6
- Remove unused pam and abl templates (remnants of some stuff I
  was prototyping).

* Fri Jan 19 2007 Shad L. Lords <slords@mail.com> 4.17.2-5
- [Forward-ported from 4.17.0]
- Refactor console code considerably, and add restore from CDROM/USB
  backup capability to console.
- Remove deprecated %conf use in console. [SME: 1856]

* Fri Jan 19 2007 Shad L. Lords <slords@mail.com> 4.17.2-4
- [Ported from e-smith-base+ldap]
- Add support for use of pam_tally and/or pam_abl modules. Both
  are disabled by default.
- Update /etc/pam.d/{ftp,passwd} templates.
- Add template for /etc/pam.d/system-auth.

* Fri Jan 19 2007 Shad L. Lords <slords@mail.com> 4.17.2-3
- [Forward-ported from 4.17.0]
- Move masq fragments to e-smith-packetfilter rpm.

* Fri Jan 19 2007 Shad L. Lords <slords@mail.com> 4.17.2-2
- [Forward-ported from 4.17.0]
- Remove server-manager templates and scripts - move to e-smith-manager.
  [SME: 2023]

* Fri Jan 19 2007 Shad L. Lords <slords@mail.com> 4.17.2-1
- [Forward-ported from 4.17.0]
- Combine dhcp client, pppoe, dialup and static WAN connections into
  "wan" service. [SME 1795]

* Fri Jan 19 2007 Shad L. Lords <slords@mail.com> 4.17.2-0
- Make new development stream. Based from 4.16.0-39.

* Sun Jan 14 2007 Shad L. Lords <slords@mail.com> 4.16.0-39
- [Back-port from 4.17.0-23]
- Add admin email forwarding to modify user panel [SME: 827]

* Sat Jan 13 2007 Shad L. Lords <slords@mail.com> 4.16.0-38
- [Back-port from 4.17.0-22]
- Fix last patch so that data is pulled correctly [SME: 1034]

* Sat Jan 13 2007 Shad L. Lords <slords@mail.com> 4.16.0-37
- [Back-port from 4.17.0-21]
- Make purge-old-logs configurable via db [SME: 1034]

* Wed Jan 10 2007 Shad L. Lords <slords@mail.com> 4.16.0-36
- [Back-port from 4.17.0-20]
- Don't regenerate key and only regenerate crt when expired. [SME: 2035]

* Tue Dec 26 2006 Gordon Rowell <gordonr@gormand.com.au> 4.16.0-35
- [Back-port from 4.17.0-19]
- And mark admin_raidreport as only available for local mail [SME: 2139]

* Tue Dec 26 2006 Gordon Rowell <gordonr@gormand.com.au> 4.16.0-34
- [Back-port from 4.17.0-17, 4.17.0-18]
- Send raidmonitor output to admin_raidreport pseudonym [SME: 2139]
- And mark admin_raidreport as non-Removable [SME: 2139]

* Sat Dec 23 2006 Shad L. Lords <slords@mail.com> 4.16.0-33
- Disable raid based on /proc/partitions (which is dynamic) instead 
  of grub/device.map (which is static) [SME: 2131]

* Fri Dec 22 2006 Shad L. Lords <slords@mail.com> 4.16.0-32
- Check device size after calculating space needed. [SME: 2131]

* Fri Dec 08 2006 Shad L. Lords <slords@mail.com> 4.16.0-31
- Create partitions in order of size.  This makes sure boot is first and
  / is last.  Also last partitions fills all available space making resizing
  easier. [SME: 2131]

* Thu Dec 07 2006 Shad L. Lords <slords@mail.com>
- Update to new release naming.  No functional changes.
- Make Packager generic

* Tue Dec 05 2006 Shad L. Lords <slords@mail.com> 4.16.0-30
- Update manage raid console functions to handle all raid types [SME: 2131]

* Tue Nov 21 2006 Charlie Brady <charlie_brady@mitel.com> 4.16.0-29
- Fix warning from dhclient.conf template expansion.

* Wed Aug 30 2006 Charlie Brady <charlie_brady@mitel.com> 4.16.0-28
- Add missing LocalModule for mod_proxy_http to admin apache conf.
  [SME: 1853]

* Fri Jul 14 2006 Charlie Brady <charlie_brady@mitel.com> 4.16.0-27
- Prevent daily regeneration of SSL cert if City/Company/Department are
  empty. [SME: 1602]

* Wed Jun 28 2006 Gavin Weight <gweight@gmail.com> 4.16.0-26
- Menu text in console is incorrect for RAID5 installs. [SME: 404] 

* Wed Jun 14 2006 Gavin Weight <gweight@gmail.com> 4.16.0-25
- Modify user create page to show henry:miller not henry_miller. [SME: 531] 

* Fri Jun 9 2006 Gavin Weight <gweight@gmail.com> 4.16.0-24
- Remove lines for creating symlink to statusreport from spec file. [SME: 450] 

* Mon Jun 6 2006 Gordon Rowell <gordonr@gormand.com.au> 4.16.0-23
- Allow for admin account when locking null passwords, and perform
  check in post-upgrade so that the password screen will be presented
  after the reboot [SME: 1529]

* Mon Jun 6 2006 Gordon Rowell <gordonr@gormand.com.au> 4.16.0-22
- Correct argument ordering in last change [SME: 790, SME: 1541]

* Sun May 28 2006 Charlie Brady <charlie_brady@mitel.com> 4.16.0-21
- Increase cert serial number when new certificate is generated. [SME: 790]

* Sun May 28 2006 Charlie Brady <charlie_brady@mitel.com> 4.16.0-20
- Change ssl.crt template so that cert is regenerated if issuer information
  has changed. [SME: 1484]

* Thu Apr 27 2006 Gavin Weight <gweight@gmail.com> 4.16.0-19
- Change default shutdown value from shutdown to reboot. [SME: 1320] 

* Sun Apr 23 2006 Charlie Brady <charlie_brady@mitel.com> 4.16.0-18
- Fix syntax error introduced in last change (and reuse $rc and $choice in
  raidManage.pl). [SME: 1285,1300] 

* Fri Apr 21 2006 Gordon Rowell <gordonr@gormand.com.au> 4.16.0-17
- Force masq service to enabled for servergateway modes, but
  leave at current setting for serveronly. Revises -09 change [SME: 1209]

* Wed Apr 19 2006 Charlie Brady <charlie_brady@mitel.com> 4.16.0-16
- Add big warning about wiping disk to raid management screen. 
  [SME: 1285] 

* Tue Apr 18 2006 Charlie Brady <charlie_brady@mitel.com> 4.16.0-15
- Ensure that rmmod-bonding doesn't return error status if
  bonding is not enabled (e.g. during upgrade) [SME: 935]

* Tue Apr 18 2006 Charlie Brady <charlie_brady@mitel.com> 4.16.0-14
- Avoid warning from NICBondingOptions migrate fragment. [SME: 1271]

* Tue Apr 18 2006 Gordon Rowell <gordonr@gormand.com.au> 4.16.0-13
- Always save ssh property changes, even if sshd is disabled [SME: 1210]

* Thu Apr 13 2006 Charlie Brady <charlie_brady@mitel.com> 4.16.0-12
- Don't run kudzu at every bootup. [SME: 727]

* Tue Apr 11 2006 Charlie Brady <charlie_brady@mitel.com> 4.16.0-11
- More fixes to dhclient configuration (courtesy of Richard Schiffelers).
  [SME: 881]

* Mon Apr 10 2006 Charlie Brady <charlie_brady@mitel.com> 4.16.0-10
- Fixes to dhclient configuration (courtesy of Richard Schiffelers).
  [SME: 881]

* Thu Apr 6 2006 Gordon Rowell <gordonr@gormand.com.au> 4.16.0-09
- Enable the masq service to ensure that installs and upgrades
  are consistent. If someone really wants to disable it, they can 
  add a force fragment [SME: 1209]

* Thu Apr 6 2006 Gordon Rowell <gordonr@gormand.com.au> 4.16.0-08
- Lock accounts with bad SMB passwords [SME: 1193]

* Thu Apr 6 2006 Gordon Rowell <gordonr@gormand.com.au> 4.16.0-07
- Revert password length restriction changes [SME: 1193]

* Thu Apr 6 2006 Gordon Rowell <gordonr@gormand.com.au> 4.16.0-06
- Adjust plural in page title in last patch [SME: 1193]

* Thu Apr 6 2006 Gordon Rowell <gordonr@gormand.com.au> 4.16.0-05
- Adjust console logic for 14 character password restriction [SME: 1193]

* Wed Apr 5 2006 Gordon Rowell <gordonr@gormand.com.au> 4.16.0-04
- Only process 'network' entries in route-eth0 template [SME: 1182]

* Wed Apr 5 2006 Gordon Rowell <gordonr@gormand.com.au> 4.16.0-03
- Restrict passwords to 14 characters [SME: 1193]

* Tue Mar 14 2006 Gordon Rowell <gordonr@gormand.com.au> 4.16.0-02
- Rename anaconda logs, but leave a symlink. Do nothing if the log
  is already a symlink or missing [SME: 808]

* Tue Mar 14 2006 Charlie Brady <charlie_brady@mitel.com> 4.16.0-01
- Roll stable stream version. [SME: 1016]

* Tue Mar 14 2006 Gordon Rowell <gordonr@gormand.com.au> 4.15.9-20
- Ensure that each user has a Shell property in post-upgrade. 
  If they didn't have one before, set it to the current value in
  /etc/passwd. [SME: 859]

* Tue Mar 14 2006 Gordon Rowell <gordonr@gormand.com.au> 4.15.9-19
- Copy anaconda logs instead of renaming them in post-upgrade [SME: 808]
- Adjust timestamp of copied logs to logfiles2timestamp format [SME: 808]

* Mon Mar 13 2006 Gordon Rowell <gordonr@gormand.com.au> 4.15.9-18
- Change modSSL to be private in Private Server and Gateway mode [SME: 328]

* Mon Mar 13 2006 Gordon Rowell <gordonr@gormand.com.au> 4.15.9-17
- And remove now redundant calls to wherenext [SME: 986]

* Fri Mar 10 2006 Charlie Brady <charlie_brady@mitel.com> 4.15.9-16
- Fix FM page name (FirstPage => First) in a few places. [SME: 986]

* Tue Mar  7 2006 Gordon Rowell <gordonr@gormand.com.au> 4.15.9-15
- Correct typo in -13 change which hid message [SME: 964]

* Tue Mar  7 2006 Gordon Rowell <gordonr@gormand.com.au> 4.15.9-14
- Display a message for single disk installs which catches that
  case and tells people that they can add a second disk and produce
  a mirrored pair [SME: 958]

* Tue Mar  7 2006 Gordon Rowell <gordonr@gormand.com.au> 4.15.9-13
- Display a nicer message when a spare disk is available to be
  added to the pair [SME: 964]
- Blank line for consistency with other messages [SME: 964]

* Tue Mar  7 2006 Gordon Rowell <gordonr@gormand.com.au> 4.15.9-12
- Check whether a resync is in progress so we don't state that
  intervention is required when it is not [SME: 958]

* Tue Mar  7 2006 Gordon Rowell <gordonr@gormand.com.au> 4.15.9-11
- Check whether destination drive of add_mirror is already part
  of a RAID device. If so, complain and exit [SME: 870]
- Also ensure that /sbin is in the PATH

* Sun Mar  5 2006 Charlie Brady <charlie_brady@mitel.com> 4.15.9-10
- Fixes to dhclient configuration. [SME: 881]

* Fri Mar 03 2006 Mark Knox <mark_knox@mitel.com> 4.15.9-09
- Added NIC Bonding options screen in console [SME: 935]
- Migrate old NICBondingOptions to new defaults, and added new default
  options [SME: 935]
- rmmod bonding.ko in bootstrap-console-save so new options work
  without extra reboot [SME: 935]
  
* Wed Mar 01 2006 Mark Knox <mark_knox@mitel.com> 4.15.9-08
- Allow NICBondingOptions in 10bonding template fragment [SME: 918]

* Wed Mar 01 2006 Charlie Brady <charlie_brady@mitel.com> 4.15.9-07
- Bump pppoe run script mlimit from 10M to 25M. [SME: 907]

* Fri Feb 24 2006 Gordon Rowell <gordonr@gormand.com.au> 4.15.9-06
- Re-do -04 change as a patch so it sticks [SME: 863]

* Thu Feb 23 2006 Charlie Brady <charlieb@e-smith.com> 4.15.9-05
- Add templates for dhclient configuration file. [SME: 881]

* Wed Feb 22 2006 Charlie Brady <charlieb@e-smith.com> 4.15.9-04
- Remove default fragment for AdminEmail [SME: 863]

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
%patch1 -p1
%patch2 -p1
%if "%{?rhel}" == "5"
%patch3 -p1
%endif
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

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
mkdir -p root/home/e-smith/files/{users,server-resources}
mkdir -p root/home/e-smith/files/users/admin/home
mkdir -p root/home/e-smith/Maildir/{cur,new,tmp}
mkdir -p root/root/.ssh
mkdir -p root/var/log/wan

%if "%_build_arch" == "i386"
echo "enabled" >  root/etc/e-smith/db/configuration/defaults/apmd/status
%else
echo "disabled" >  root/etc/e-smith/db/configuration/defaults/apmd/status
%endif

LEXICONS=$(find root/etc/e-smith/web/{functions,panels/password/cgi-bin} \
    -type f | grep -v CVS)

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

mkdir -p root/usr/share/locale/en_US/LC_MESSAGES
xgettext -o root/usr/share/locale/en_US/LC_MESSAGES/server-console.po root/sbin/e-smith/console

mkdir -p root/etc/e-smith/locale
# Make the fr-ca link in %pre to ease upgrades
# ln -s fr root/etc/e-smith/locale/fr-ca
ln -s fr root/etc/e-smith/locale/fr-fr 
ln -s en-us root/etc/e-smith/locale/en
ln -s en-us root/etc/e-smith/locale/en-au
ln -s en-us root/etc/e-smith/locale/en-gb
ln -s en-us root/etc/e-smith/locale/en-nz

mkdir -p root/etc/e-smith/templates/etc/dhcpc/dhcpcd.exe
ln -s /etc/e-smith/templates-default/template-begin-shell \
      root/etc/e-smith/templates/etc/dhcpc/dhcpcd.exe/template-begin

for file in imap login passwd pwauth system-auth
do
    mkdir -p root/etc/e-smith/templates/etc/pam.d/$file
    ln -s /etc/e-smith/templates-default/template-begin-pam \
      root/etc/e-smith/templates/etc/pam.d/$file/template-begin
done

mkdir -p root/service
mkdir -p root/etc/rc.d/init.d/supervise

for service in dhcpd wan ippp syslog klogd
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
touch root/var/service/wan/down

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
    --dir /var/service/wan 'attr(1755,root,root)' \
    --file /var/service/wan/down 'attr(0644,root,root)' \
    --file /var/service/wan/run 'attr(0750,root,root)' \
    --file /var/service/wan/run.dhclient 'attr(0750,root,root)' \
    --file /var/service/wan/run.pppoe 'attr(0750,root,root)' \
    --file /var/service/wan/run.static 'attr(0750,root,root)' \
    --file /var/service/wan/run.dialup 'attr(0750,root,root)' \
    --file /var/service/wan/run.disabled 'attr(0750,root,root)' \
    --dir /var/service/wan/supervise 'attr(0700,root,root)' \
    --dir /var/service/wan/log 'attr(1755,root,root)' \
    --file /var/service/wan/log/run 'attr(0750,root,root)' \
    --dir /var/service/wan/log/supervise 'attr(0700,root,root)' \
    --dir /var/log/wan 'attr(2750,smelog,smelog)' \
    --dir /var/service/ippp 'attr(1755,root,root)' \
    --file /var/service/ippp/down 'attr(0644,root,root)' \
    --file /var/service/ippp/run 'attr(0750,root,root)' \
    --dir /var/service/ippp/supervise 'attr(0700,root,root)' \
    --dir /var/service/ippp/log 'attr(1755,root,root)' \
    --file /var/service/ippp/log/run 'attr(0750,root,root)' \
    --dir /var/service/ippp/log/supervise 'attr(0700,root,root)' \
    --dir /var/log/ippp 'attr(2750,smelog,smelog)' \
    --dir /etc/e-smith/skel/user/.ssh 'attr(0700,root,root)' \
    > %{name}-%{version}-%{release}-filelist

mkdir -p $RPM_BUILD_ROOT/home/e-smith/db
for file in %{dbfiles}
do
    # Create ghost file for rpm
    touch $RPM_BUILD_ROOT/home/e-smith/db/$file
    echo "%config(noreplace) %attr(0640,root,admin) /home/e-smith/db/$file" \
        >> %{name}-%{version}-%{release}-filelist
done
echo "%doc COPYING"          >> %{name}-%{version}-%{release}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
