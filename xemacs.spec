Summary:	The XEmacs editor
Summary(pl):	XEmacs -- Edytor
Name:		xemacs
Version:	21.1.2
%define		realversion	21.1-p2
%define		pkgdate		1999-07-13
Release:	1
Copyright:	GPL
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Source0:	ftp://ftp.xemacs.org/pub/xemacs/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.xemacs.org/pub/xemacs/packages/%{name}-sumo-%{pkgdate}.tar.gz
Source2:	ftp://ftp.xemacs.org/pub/xemacs/packages/%{name}-mule-sumo-%{pkgdate}.tar.gz
Source3:	xemacs.wmconfig
Patch0:		xemacs-static.patch
Patch1:		xemacs-alpha.patch
Patch2:		xemacs-perl.patch
Patch3:		xemacs-sitelisp.patch
URL:		http://www.xemacs.org/
BuildRequires:	nas-devel
BuildRequires:	XFree86-devel
BuildRequires:	zlib-devel
BuildRequires:	xpm-devel
BuildRequires:	openldap-devel
BuildRequires:	libtiff-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	gpm-devel
BuildRequires:	ncurses-devel
Buildroot:	/tmp/%{name}-%{version}-root

%description
XEmacs is a version of Emacs, compatible with and containing many 
improvements over GNU Emacs, written by Richard Stallman of the 
Free Software Foundation. It was originally based on an early release 
of GNU Emacs version 19, and has tracked subsequent releases of GNU 
Emacs as they have become available.
This XEmacs distribution has been splitted in some rpm :
- xemacs:        the main part
- xemacs-extras: files in conflict with emacs
(Install xemacs-extras if you do not have emacs installed.)
Other are optional. 

%description -l pl 
XEmacs jest odmian± Emacsa, zgodn± (i zawieraj±c± wiele udogodnieñ) z 
GNU Emacsem tworzonym przez Richard Stallman z Free Software Foundation. 
Wywodzi siê z wczesnych odmian GNU Emacs 19, wprowadza wiele mi³ych 
ulepszeñ nie trac±c jednak wiêzi z oryginaln± wersj±. 

Ta dystrubucja XEmacsa zosta³± podzielona na wiele pakietów binarnych. 
Do pracy niezbêdne s± dwa z nich:
- xemacs:        g³ówny pakiet
- xemacs-extras: pliki wchodz±ce w sk³ad dystrybucji GNU Emacs
  (zainstaluj go je¶li nie posiadasz GNU Emacsa), 
oraz innych pakietów (opcjonalnych)

%package el
Summary:	.el source files for XEmacs
Summary(pl):	Pliki ¼ród³owe procedur w eLispie do XEmacsa
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	%{name} = %{version}

%description el
.el source files -- not necessary to run XEmacs

%description el -l pl
Pliki ¼ród³owe procedur w eLispie do XEmacsa.

%package gnats
Summary:	GNU Problem Report Management
Summary(pl):	GNU Problem Report Management
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	%{name} = %{version}

%description gnats
GNU Problem Report Management is a bug-tracking tool designed for use
at a central "Support Site".  Users who experience problems use
electronic mail to communicate these problems to "maintainers" at that
Support Site.  GNATS partially automates the tracking of these "Problem
Reports" ("PR"s). 

%description gnats -l pl
GNU Problem Report Managenment jest systemem informowania o b³êdach opartym o 
centralne repozytorium. 

%package gnats-el
Summary:	.el source files for xemacs-gnats
Summary(pl):	Pliki ¼ród³owe procedur w eLispie do xemacs-gnats
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	%{name} = %{version}

%description gnats-el
.el gnats source files -- not necessary to run XEmacs

%package emulators
Summary:	other editors emulators files for XEmacs
Summary(pl):	emulatory innych edytorów dla XEmacsa
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	%{name} = %{version}

%description emulators
XEmacs-emulators -- other editors emulators files for XEmacs.

%description emulators -l pl 
Emulatory innych edytorów dla XEmacsa.

%package emulators-el
Summary:	.el source files xemacs-emulators
Summary(pl):	Pliki ¼ród³owe dla xemacs-emulators
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	%{name} = %{version}

%description emulators-el
.el source files -- not necessary to run XEmacs.

%description emulators-el -l pl
Pliki ¼ród³owe dla xemacs-emulators.

%package viper
Summary:	Vi emulator for XEmacs
Summary(pl):	emulator Vi dla XEmacsa
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	%{name} = %{version}

%description viper
XEmacs-viper - Vi emulator for XEmacs.

%description viper -l pl 
emulator Vi dla XEmacs.

%package viper-el
Summary:	.el source files for xemacs-viper
Summary(pl):	Pliki ¼ród³owe dla xemacs-viper
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	%{name} = %{version}

%description viper-el
.el source files -- not necessary to run XEmacs.

%description viper-el -l pl
Pliki ¼ród³owe dla xemacs-viper.

%package lisp-programming
Summary:	.el source files for XEmacs
Summary(pl):	Pakiety do programowania w eLisp
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	%{name} = %{version}

%description lisp-programming
Lisp programming XEmacs packages.

%description lisp-programming -l pl 
Pakiety do programowania w eLisp.

%package lisp-programming-el
Summary:	.el source files for xemacs-lisp-programming
Summary(pl):	Pliki ¼ród³owe dla xemacs-lisp-programming
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	%{name} = %{version}

%description lisp-programming-el  
.el source files for xemacs-lisp-programming.

%description lisp-programming-el -l pl 
Pliki ¼ród³owe dla xemacs-lisp-programming.

%package auctex
Summary:	TeX mode for XEmacs
Summary(pl):	tryb TeXowy dla XEmacsa 
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	%{name} = %{version}

%description auctex
XEmacs-auctex - TeX mode for XEmacs.

%description auctex -l pl 
XEmacs-auctex - tryb TeXowy dla XEmacsa.

%package auctex-el
Summary:	.el source files for xemacs-auctex
Summary(pl):	Pliki ¼ród³owe dla xemacs-auctex
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	%{name} = %{version}

%description auctex-el
.el source files -- not necessary to run XEmacs.

%description auctex-el -l pl
Pliki ¼ród³owe dla xemacs-auctex.

%package w3
Summary:	w3 browser for XEmacs
Summary(pl):	przegl±darka W3 dla XEmacsa
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	%{name} = %{version}

%description w3
XEmacs-w3 - w3 browser for XEmacs.

%description w3 -l pl  
XEmacs-w3 - przegl±darka W3 dla XEmacsa.

%package w3-el
Summary:	.el source files for xemacs-w3
Summary(pl):	Pliki ¼ród³owe dla xemacs-w3
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	%{name} = %{version}

%description w3-el
.el source files -- not necessary to run XEmacs.

%description w3-el -l pl 
Pliki ¼ród³owe dla xemacs-w3.

%package modes
Summary:	misc modes for XEmacs
Summary(pl):	inne tryby XEmacsa
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	%{name} = %{version}

%description modes
XEmacs-modes - misc modes for XEmacs.

%description modes -l pl 
Ró¿ne tryby XEmacsa.

%package modes-el
Summary:	.el source files for xemacs-modes
Summary(pl):	Pliki ¼ród³owe dla xemacs-modes
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	%{name} = %{version}

%description modes-el
.el source files -- not necessary to run XEmacs.

%description modes-el -l pl 
Pliki ¼ród³owe dla xemacs-modes.

%package extras
Summary:	files which conflict with GNU Emacs
Summary(pl):	wspólne pliki XEmacsa i GNU Emacsa
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	%{name} = %{version}
Conflicts:   emacs

%description extras
These files are common between GNU Emacs and XEmacs. If you do not 
have GNU Emacs installed, be sure to install this package as well 
when you install XEmacs.

%description extras -l pl
S± to wpólne pliki GNU Emacs i XEmacs. Je¶li nie zainstalowa³e¶ GNU Emacsa,
to koniecznie zainstaluj ten pakiet.

%package psgml
Summary:	pSGML mode for XEmacs 
Summary(pl):	Tryb pSGML dla XEmacsa 
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	%{name} = %{version}

%description psgml
XEmacs-psgml - SGML mode for XEmacs.

%description psgml -l pl
XEmacs-psgml - Tryb SGML dla XEmacsa.

%package psgml-el
Summary:	.el source files for xemacs-psgml
Summary(pl):	Pliki ¼ród³owe dla xemacs-psgml
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	%{name} = %{version}

%description psgml-el
.el source files -- not necessary to run XEmacs.

%description psgml-el -l pl
Pliki ¼ród³owe dla xemacs-psgml.

%package mail
Summary:	mail & news modes for XEmacs
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	%{name} = %{version}

%description mail
XEmacs-mail - mail & news modes for XEmacs: 
* vm 
* Tools for MIME 
* rmail 

%description mail -l pl 
XEmacs-mail - poczta i UseNet News w XEmacsie:
* vm 
* Tools for MIME 
* rmail 

%package mail-el
Summary:	.el source files for xemacs-mail
Summary(pl):	Pliki ¼ród³owe dla xemacs-mail
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	%{name} = %{version}

%description mail-el
.el mail source files -- not necessary to run XEmacs.

%description mail-el -l pl 
Pliki ¼ród³owe dla xemacs-mail.

%package gnus
Summary:	gnus mode for XEmacs
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	%{name} = %{version}, %{name}-mail

%description gnus
Xemacs -- gnus mode for XEmacs.

%description gnus -l pl 
Xemacs -- poczta i UseNet News w XEmacsie.

%package gnus-el
Summary:	.el source files for xemacs-gnus
Summary(pl):	Pliki ¼ród³owe dla xemacs-gnus
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	%{name} = %{version}

%description gnus-el
.el gnus source files -- not necessary to run XEmacs.

%description gnus-el -l pl 
Pliki ¼ród³owe dla xemacs-gnus.

%package zenirc
Summary:	ZenIRC for XEmacs
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	%{name} = %{version}

%description zenirc
Xemacs -- ZenIRC.

%package zenirc-el
Summary:	.el source files for xemacs-zenirc
Summary(pl):	Pliki ¼ród³owe dla xemacs-zenirc
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	%{name} = %{version} 

%description zenirc-el
.el zenirc source files -- not necessary to run XEmacs.

%package bbdb
Summary:	Insidious Big Brother Database for XEmacs
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	%{name} = %{version}

%description bbdb
Xemacs -- Insidious Big Brother Database.

%package bbdb-el
Summary:	.el source files for xemacs-bbdb
Summary(pl):	Pliki ¼ród³owe dla xemacs-bbdb
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	%{name} = %{version}

%description bbdb-el
.el Insidious Big Brother Database source files -- not necessary to run XEmacs.

%package calc
Summary:	Calculator for XEmacs
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	%{name} = %{version}

%description calc
Xemacs -- Calculator for XEmacs.

%package calc-el
Summary:	.el source files for xemacs-calc
Summary(pl):	Pliki ¼ród³owe dla xemacs-calc
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	%{name} = %{version}, 

%description calc-el
.el calc source files -- not necessary to run XEmacs.

%package mule
Summary:	Multi-lingual support for XEmacs
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	%{name} = %{version}

%description mule
Xemacs -- Multi-lingual support for XEmacs.

%package mule-el
Summary:	.el source files for xemacs-mule
Summary(pl):	Pliki ¼ród³owe dla xemacs-mule
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	%{name} = %{version}

%description mule-el
.el mule source files -- not necessary to run XEmacs.

%package jde
Summary:	Java Development Environment for XEmacs
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	%{name} = %{version}

%description jde
Xemacs -- Calculator for XEmacs.

%package jde-el
Summary:	.el source files for xemacs-jde
Summary(pl):	Pliki ¼ród³owe dla xemacs-jde
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	%{name} = %{version}

%description jde-el
.el jde source files -- not necessary to run XEmacs.

%prep
%setup -q -a1 -a2 -T -b 0 -n xemacs-%{version}
%patch0 -p1
#%patch2 -p1
%patch3 -p1
chmod u+wXr * -R

%ifarch alpha
%patch1 -p1
%endif

cp -a mule-packages/* ./ && rm -rf mule-packages
cp -a xemacs-packages/* ./ && rm -rf xemacs-packages

%build
autoconf
CFLAGS="$RPM_OPT_FLAGS" CPPFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s -lc" \
sitelispdir=%{_datadir}/%{name}/site-lisp \
./configure %{_target_platform} \
	--prefix=%{_prefix} \
	--infodir=%{_infodir} \
	--mandir=%{_mandir}/man1 \
	--datadir=%{_datadir} \
	--package_path=%{_datadir}/%{name} \
	--lispdir=%{_datadir}/%{name}/lisp \
	--pkgdir=%{_datadir}/%{name}/lisp \
	--etcdir=%{_datadir}/%{name}/etc \
	--with-dialogs=athena \
	--with-sound=nas \
	--cflags="$RPM_OPT_FLAGS" \
	--error-checking=none \
	--debug=no \
	--with-xpm \
	--with-ncurses \
	--lockdir=/var/lock/xemacs/ \
	--with-session=yes \
	--with-gpm=yes \
	--with-png=yes \


#	--with-mule

sitelispdir=%{_datadir}/%{name}/site-lisp \
make dist
# xemacs generation
sitelispdir=%{_datadir}/%{name}/site-lisp \
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/X11/wmconfig,var/lock/xemacs} \
	$RPM_BUILD_ROOT{%{_mandir}/{ja/man1,man1},/usr/X11R6/lib/X11/{{ja,de,fr,ro}/app-defaults,app-defaults}}

make install-arch-dep install-arch-indep gzip-el \
	prefix=$RPM_BUILD_ROOT/usr \
	infodir=$RPM_BUILD_ROOT%{_infodir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}/man1 \
	datadir=$RPM_BUILD_ROOT%{_datadir} \
	package_path=$RPM_BUILD_ROOT%{_datadir}/%{name} \
	lispdir=$RPM_BUILD_ROOT%{_datadir}/%{name}/lisp \
	pkgdir=$RPM_BUILD_ROOT%{_datadir}/%{name}/lisp \
	sitelispdir=$RPM_BUILD_ROOT%{_datadir}/%{name}/site-lisp \
	etcdir=$RPM_BUILD_ROOT%{_datadir}/%{name}/etc

gzip -9nf $RPM_BUILD_ROOT%{_infodir}/*info*
find $RPM_BUILD_ROOT%{_datadir}/%{name}/etc/auctex/style/ -name \*.el | xargs gzip -9

install %{SOURCE3} $RPM_BUILD_ROOT/etc/X11/wmconfig/xemacs

install lib-src/{install-sid,send-pr} $RPM_BUILD_ROOT%{_libdir}/%{name}-%{realversion}/*/
install lib-src/tm* $RPM_BUILD_ROOT%{_libdir}/%{name}-%{realversion}/*/

[ -d $RPM_BUILD_ROOT%{_datadir}/%{name}/site-lisp ] || \
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/site-lisp

ln -s %{name}-%{realversion} $RPM_BUILD_ROOT%{_libdir}/%{name}

find $RPM_BUILD_ROOT%{_bindir} -type f |xargs  file |grep stripped|  awk -F: '{print $1}' | xargs strip 
find $RPM_BUILD_ROOT%{_libdir}/*/* -type f |xargs  file |grep stripped|  awk -F: '{print $1}' | xargs strip 

mv $RPM_BUILD_ROOT%{_datadir}/%{name}/etc/Emacs.ad \
	$RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults/Emacs

for i in de fr ja ro ; do
	mv $RPM_BUILD_ROOT%{_datadir}/%{name}/etc/app-defaults/$i/Emacs \
		$RPM_BUILD_ROOT/usr/X11R6/lib/X11/$i/app-defaults/Emacs
done

mv $RPM_BUILD_ROOT%{_datadir}/%{name}/etc/xemacs-ja.1 \
	$RPM_BUILD_ROOT%{_mandir}/ja/man1/xemacs.1

mv -f $RPM_BUILD_ROOT%{_bindir}/xemacs-%{realversion} \
	$RPM_BUILD_ROOT%{_bindir}/xemacs

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/{ja/man1/*,man1/*}
find $RPM_BUILD_ROOT%{_datadir}/*/* -type f -name ChangeLog* | xargs gzip -9nf

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info %{_infodir}/cc-mode.info.gz /etc/info-dir
/sbin/install-info %{_infodir}/forms.info.gz /etc/info-dir
/sbin/install-info %{_infodir}/xemacs.info.gz /etc/info-dir
/sbin/install-info %{_infodir}/custom.info.gz /etc/info-dir
/sbin/install-info %{_infodir}/efs.info.gz /etc/info-dir
/sbin/install-info %{_infodir}/external-widget.info.gz /etc/info-dir
/sbin/install-info %{_infodir}/internals.info.gz /etc/info-dir
/sbin/install-info %{_infodir}/new-users-guide.info.gz /etc/info-dir
/sbin/install-info %{_infodir}/send-pr.info.gz /etc/info-dir
/sbin/install-info %{_infodir}/term.info.gz /etc/info-dir
/sbin/install-info %{_infodir}/vhdl-mode.info.gz /etc/info-dir
/sbin/install-info %{_infodir}/widget.info.gz /etc/info-dir
/sbin/install-info %{_infodir}/xemacs-faq.info.gz /etc/info-dir
/sbin/install-info %{_infodir}/ediff.info.gz /etc/info-dir
/sbin/install-info %{_infodir}/eudc.info.gz /etc/info-dir

%preun
if [ "$1" = "0" ]; then
	/sbin/install-info %{_infodir}/cc-mode.info.gz /etc/info-dir
	/sbin/install-info %{_infodir}/forms.info.gz /etc/info-dir
	/sbin/install-info %{_infodir}/xemacs.info.gz /etc/info-dir
	/sbin/install-info %{_infodir}/custom.info.gz /etc/info-dir
	/sbin/install-info %{_infodir}/efs.info.gz /etc/info-dir
	/sbin/install-info %{_infodir}/external-widget.info.gz /etc/info-dir
	/sbin/install-info %{_infodir}/internals.info.gz /etc/info-dir
	/sbin/install-info %{_infodir}/new-users-guide.info.gz /etc/info-dir
	/sbin/install-info %{_infodir}/send-pr.info.gz /etc/info-dir
	/sbin/install-info %{_infodir}/term.info.gz /etc/info-dir
	/sbin/install-info %{_infodir}/vhdl-mode.info.gz /etc/info-dir
	/sbin/install-info %{_infodir}/widget.info.gz /etc/info-dir
	/sbin/install-info %{_infodir}/xemacs-faq.info.gz /etc/info-dir
	/sbin/install-info %{_infodir}/ediff.info.gz /etc/info-dir
	/sbin/install-info %{_infodir}/eudc.info.gz /etc/info-dir
fi

%post gnats
/sbin/install-info %{_infodir}/gnats.info.gz /etc/info-dir

%preun gnats
if [ "$1" = "0" ]; then
	/sbin/install-info %{_infodir}/gnats.info.gz /etc/info-dir
fi

%post viper
/sbin/install-info %{_infodir}/viper.info.gz /etc/info-dir

%preun viper
if [ "$1" = "0" ]; then
	/sbin/install-info %{_infodir}/viper.info.gz /etc/info-dir
fi

%post auctex
/sbin/install-info %{_infodir}/auctex.info.gz /etc/info-dir
/sbin/install-info %{_infodir}/reftex.info.gz /etc/info-dir

%preun auctex
if [ "$1" = "0" ]; then
	/sbin/install-info %{_infodir}/auctex.info.gz /etc/info-dir
	/sbin/install-info %{_infodir}/reftex.info.gz /etc/info-dir
fi


%post w3
/sbin/install-info %{_infodir}/w3-faq.info.gz /etc/info-dir
/sbin/install-info %{_infodir}/w3.info.gz /etc/info-dir

%preun w3
if [ "$1" = "0" ]; then
	/sbin/install-info %{_infodir}/w3-faq.info.gz /etc/info-dir
	/sbin/install-info %{_infodir}/w3.info.gz /etc/info-dir
fi

%post modes
/sbin/install-info %{_infodir}/pcl-cvs.info.gz /etc/info-dir

%preun modes
if [ "$1" = "0" ]; then
	/sbin/install-info %{_infodir}/pcl-cvs.info.gz /etc/info-dir
fi

%post psgml
/sbin/install-info %{_infodir}/psgml-api.info.gz /etc/info-dir
/sbin/install-info %{_infodir}/psgml.info.gz /etc/info-dir
/sbin/install-info %{_infodir}/hm--html-mode.info.gz /etc/info-dir

%preun psgml
if [ "$1" = "0" ]; then
	/sbin/install-info %{_infodir}/psgml-api.info.gz /etc/info-dir
	/sbin/install-info %{_infodir}/psgml.info.gz /etc/info-dir
	/sbin/install-info %{_infodir}/hm--html-mode.info.gz /etc/info-dir
fi

%post mail 
/sbin/install-info %{_infodir}/mh-e.info.gz /etc/info-dir
/sbin/install-info %{_infodir}/supercite.info.gz /etc/info-dir
/sbin/install-info %{_infodir}/rmail.info.gz /etc/info-dir
/sbin/install-info %{_infodir}/tm-edit-en.info.gz /etc/info-dir
/sbin/install-info %{_infodir}/tm-mh-e-en.info.gz /etc/info-dir
/sbin/install-info %{_infodir}/tm-view-en.info.gz /etc/info-dir
/sbin/install-info %{_infodir}/tm-vm-en.info.gz /etc/info-dir
/sbin/install-info %{_infodir}/vm.info.gz /etc/info-dir

%preun mail 
if [ "$1" = "0" ]; then
	/sbin/install-info %{_infodir}/mh-e.info.gz /etc/info-dir
	/sbin/install-info %{_infodir}/supercite.info.gz /etc/info-dir
	/sbin/install-info %{_infodir}/rmail.info.gz /etc/info-dir
	/sbin/install-info %{_infodir}/tm-edit-en.info.gz /etc/info-dir
	/sbin/install-info %{_infodir}/tm-mh-e-en.info.gz /etc/info-dir
	/sbin/install-info %{_infodir}/tm-view-en.info.gz /etc/info-dir
	/sbin/install-info %{_infodir}/tm-vm-en.info.gz /etc/info-dir
	/sbin/install-info %{_infodir}/vm.info.gz /etc/info-dir
fi

%post gnus 
/sbin/install-info %{_infodir}/message.info.gz /etc/info-dir
/sbin/install-info %{_infodir}/gnus.info.gz /etc/info-dir
/sbin/install-info %{_infodir}/gnus-mime-en.info.gz /etc/info-dir

%preun gnus 
if [ "$1" = "0" ]; then
	/sbin/install-info %{_infodir}/message.info.gz /etc/info-dir
	/sbin/install-info %{_infodir}/gnus.info.gz /etc/info-dir
	/sbin/install-info %{_infodir}/gnus-mime-en.info.gz /etc/info-dir
fi

%post zenirc
/sbin/install-info %{_infodir}/zenirc.info.gz /etc/info-dir

%preun zenirc
if [ "$1" = "0" ]; then
	/sbin/install-info %{_infodir}/zenirc.info.gz /etc/info-dir
fi

%post lisp-programming
/sbin/install-info %{_infodir}/ilisp.info.gz /etc/info-dir
/sbin/install-info %{_infodir}/cl.info.gz /etc/info-dir
/sbin/install-info %{_infodir}/lispref.info.gz /etc/info-dir
/sbin/install-info %{_infodir}/elib.info.gz /etc/info-dir

%preun lisp-programming
if [ "$1" = "0" ]; then
	/sbin/install-info %{_infodir}/ilisp.info.gz /etc/info-dir
	/sbin/install-info %{_infodir}/cl.info.gz /etc/info-dir
	/sbin/install-info %{_infodir}/lispref.info.gz /etc/info-dir
	/sbin/install-info %{_infodir}/elib.info.gz /etc/info-dir
fi

#%post bbdb
#/sbin/install-info %{_infodir}/bbdb.info.gz /etc/info-dir

#%preun bbdb
#if [ "$1" = "0" ]; then
#	/sbin/install-info %{_infodir}/bbdb.info.gz /etc/info-dir
#fi

%post calc
/sbin/install-info %{_infodir}/calc.info.gz /etc/info-dir

%preun calc
if [ "$1" = "0" ]; then
	/sbin/install-info %{_infodir}/calc.info.gz /etc/info-dir
fi

%post mule
/sbin/install-info %{_infodir}/skk.info.gz /etc/info-dir

%preun mule
if [ "$1" = "0" ]; then
	/sbin/install-info %{_infodir}/skk.info.gz /etc/info-dir
fi

%files
%defattr(644,root,root,755)
%doc README GETTING.GNU.SOFTWARE PROBLEMS 
%doc etc/NEWS etc/MAILINGLISTS BUGS etc/TERMS etc/SERVICE
%doc %{_datadir}/*/etc/TUTORIAL
%doc %lang(de) %{_datadir}/*/etc/TUTORIAL.de
%doc %lang(fr) %{_datadir}/*/etc/TUTORIAL.fr
%doc %lang(hr) %{_datadir}/*/etc/TUTORIAL.hr
%doc %lang(ja) %{_datadir}/*/etc/TUTORIAL.ja
%doc %lang(ko) %{_datadir}/*/etc/TUTORIAL.ko
%doc %lang(no) %{_datadir}/*/etc/TUTORIAL.no
%doc %lang(pl) %{_datadir}/*/etc/TUTORIAL.pl
%doc %lang(ro) %{_datadir}/*/etc/TUTORIAL.ro
%doc %lang(ru) %{_datadir}/*/etc/TUTORIAL.ru
%doc %lang(th) %{_datadir}/*/etc/TUTORIAL.th
%doc %{_libdir}/%{name}-%{realversion}/*/DOC
%doc %{_datadir}/*/etc/*.doc
%doc %{_datadir}/*/etc/README.HYPERBOLE
%doc %{_datadir}/*/etc/README.OO-BROWSER
%doc %{_datadir}/*/etc/e/README
%doc %{_datadir}/*/etc/gnuserv.README
%doc %{_datadir}/*/etc/refcard.ps.gz
%doc %{_datadir}/*/etc/refcard.tex
%doc %{_datadir}/*/etc/sample.Xdefaults
%doc %{_datadir}/*/etc/sample.emacs
%doc %{_datadir}/*/etc/aliases.ksh
%doc %{_datadir}/*/etc/editclient.sh
%doc %{_datadir}/*/etc/emerge.txt
%doc %{_datadir}/*/etc/photos
%doc %{_datadir}/*/lisp/ChangeLog*
%doc %{_datadir}/*/lisp/README
%doc %{_datadir}/*/lisp/apel/ChangeLog*
%doc %{_datadir}/*/lisp/apel/README.en
%doc %lang(jp) %{_datadir}/*/lisp/apel/README.ja
%doc %{_datadir}/*/lisp/ediff/README
%doc %{_datadir}/*/lisp/ediff/ChangeLog*
%doc %{_datadir}/*/lisp/eterm/ChangeLog*
%doc %{_datadir}/*/lisp/eterm/QUESTIONS
%doc %{_datadir}/*/lisp/eterm/README.term
%doc %{_datadir}/*/lisp/eterm/TODO.term
%doc %{_datadir}/*/lisp/term/README
%doc %{_datadir}/*/lisp/Sun/ChangeLog*
%doc %{_datadir}/*/lisp/efs/ChangeLog*
%doc %{_datadir}/*/lisp/forms/ChangeLog*
%doc %{_datadir}/*/lisp/slider/ChangeLog*
%doc %{_datadir}/*/lisp/games/ChangeLog*
%doc %{_datadir}/*/lisp/misc-games/ChangeLog*
%doc %{_datadir}/*/lisp/mine/ChangeLog*
%doc %{_datadir}/*/lisp/calendar/ChangeLog*
%doc %{_datadir}/*/lisp/cc-mode/ChangeLog*
%doc %{_datadir}/*/lisp/tooltalk/ChangeLog*
%doc %{_datadir}/*/lisp/vc/ChangeLog*
%doc %{_datadir}/*/lisp/cookie/ChangeLog*
%doc %{_datadir}/*/lisp/dired/ChangeLog*
%doc %{_datadir}/*/lisp/edit-utils/ChangeLog*
%doc %{_datadir}/*/lisp/emerge/ChangeLog*
%doc %{_datadir}/*/lisp/eudc/ChangeLog*
%doc %{_datadir}/*/lisp/frame-icon/ChangeLog*
%doc %{_datadir}/*/lisp/fsf-compat/ChangeLog*
%doc %{_datadir}/*/lisp/fsf-compat/README
%doc %{_datadir}/*/lisp/igrep/ChangeLog*
%doc %{_datadir}/*/lisp/ispell/ChangeLog*
%doc %{_datadir}/*/lisp/net-utils/ChangeLog*
%doc %{_datadir}/*/lisp/os-utils/ChangeLog*
%doc %{_datadir}/*/lisp/sounds-au/ChangeLog*
%doc %{_datadir}/*/lisp/sounds-wav/ChangeLog*
%doc %{_datadir}/*/lisp/speedbar/ChangeLog*
%doc %{_datadir}/*/lisp/strokes/ChangeLog*
%doc %{_datadir}/*/lisp/textools/ChangeLog*
%doc %{_datadir}/*/lisp/time/ChangeLog*
%doc %{_datadir}/*/lisp/view-process/ChangeLog*
%doc %{_datadir}/*/lisp/xemacs-base/ChangeLog*
%config /etc/X11/wmconfig/xemacs
%{_libdir}/%{name}
%dir %{_libdir}/%{name}-%{realversion}
%dir %{_libdir}/%{name}-%{realversion}/%{_target_platform}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/etc
%dir %{_datadir}/%{name}/lisp
%dir %{_datadir}/%{name}/site-lisp
%dir %{_datadir}/%{name}/etc/e
%dir %{_datadir}/%{name}/lisp/Sun
%dir %{_datadir}/%{name}/lisp/apel
%dir %{_datadir}/%{name}/lisp/calendar
%dir %{_datadir}/%{name}/lisp/cc-mode
%dir %{_datadir}/%{name}/lisp/cookie
%dir %{_datadir}/%{name}/lisp/dired
%dir %{_datadir}/%{name}/lisp/ediff
%dir %{_datadir}/%{name}/lisp/edit-utils
%dir %{_datadir}/%{name}/lisp/efs
%dir %{_datadir}/%{name}/lisp/emerge
%dir %{_datadir}/%{name}/lisp/eterm
%dir %{_datadir}/%{name}/lisp/eudc
%dir %{_datadir}/%{name}/lisp/forms
%dir %{_datadir}/%{name}/lisp/frame-icon
%dir %{_datadir}/%{name}/lisp/fsf-compat
%dir %{_datadir}/%{name}/lisp/games
%dir %{_datadir}/%{name}/lisp/igrep
%dir %{_datadir}/%{name}/lisp/ispell
%dir %{_datadir}/%{name}/lisp/mine
%dir %{_datadir}/%{name}/lisp/misc-games
%dir %{_datadir}/%{name}/lisp/net-utils
%dir %{_datadir}/%{name}/lisp/pc
%dir %{_datadir}/%{name}/lisp/os-utils
%dir %{_datadir}/%{name}/lisp/slider
%dir %{_datadir}/%{name}/lisp/sounds-au
%dir %{_datadir}/%{name}/lisp/sounds-wav
%dir %{_datadir}/%{name}/lisp/speedbar
%dir %{_datadir}/%{name}/lisp/strokes
%dir %{_datadir}/%{name}/lisp/term
%dir %{_datadir}/%{name}/lisp/textools
%dir %{_datadir}/%{name}/lisp/time
%dir %{_datadir}/%{name}/lisp/tooltalk
%dir %{_datadir}/%{name}/lisp/vc
%dir %{_datadir}/%{name}/lisp/view-process
%dir %{_datadir}/%{name}/lisp/xemacs-base
%attr(755,root,root) %{_bindir}/xemacs
%attr(755,root,root) %{_bindir}/gnuclient
%attr(755,root,root) %{_bindir}/gnuattach
%attr(755,root,root) %{_bindir}/gnudoit
%attr(755,root,root) %{_bindir}/pstogif
%attr(2755,root,mail) %{_libdir}/%{name}-%{realversion}/*/movemail
%attr(755,root,root) %{_libdir}/%{name}-%{realversion}/*/cvtmail
%attr(755,root,root) %{_libdir}/%{name}-%{realversion}/*/digest-doc
%attr(755,root,root) %{_libdir}/%{name}-%{realversion}/*/fakemail
%attr(755,root,root) %{_libdir}/%{name}-%{realversion}/*/gnuserv
%attr(755,root,root) %{_libdir}/%{name}-%{realversion}/*/hexl
%attr(755,root,root) %{_libdir}/%{name}-%{realversion}/*/make-docfile
%attr(755,root,root) %{_libdir}/%{name}-%{realversion}/*/make-path
%attr(755,root,root) %{_libdir}/%{name}-%{realversion}/*/mmencode
%attr(755,root,root) %{_libdir}/%{name}-%{realversion}/*/profile
%attr(755,root,root) %{_libdir}/%{name}-%{realversion}/*/sorted-doc
%attr(755,root,root) %{_libdir}/%{name}-%{realversion}/*/yow
%attr(755,root,root) %{_libdir}/%{name}-%{realversion}/*/add-big-package.sh
%attr(755,root,root) %{_libdir}/%{name}-%{realversion}/*/gzip-el.sh
%attr(755,root,root) %{_libdir}/%{name}-%{realversion}/*/install-sid
%attr(755,root,root) %{_libdir}/%{name}-%{realversion}/*/rcs2log
%attr(755,root,root) %{_libdir}/%{name}-%{realversion}/*/send-pr
%attr(755,root,root) %{_libdir}/%{name}-%{realversion}/*/vcdiff
%attr(755,root,root) %{_libdir}/%{name}-%{realversion}/*/wakeup
%{_libdir}/%{name}-%{realversion}/*/config.values
%{_mandir}/man1/gnuattach.1.gz
%{_mandir}/man1/gnuclient.1.gz
%{_mandir}/man1/gnudoit.1.gz
%{_mandir}/man1/gnuserv.1.gz
%{_mandir}/man1/xemacs.1.gz
%lang(ja) %{_mandir}/ja/man1/xemacs.1.gz
%{_infodir}/cc-mode.info*gz
%{_infodir}/custom.info*gz
%{_infodir}/efs.info*gz
%{_infodir}/external-widget.info*gz
%{_infodir}/eudc.info*gz
%{_infodir}/ediff.info*gz
%{_infodir}/forms.info*gz
%{_infodir}/internals.info*gz
%{_infodir}/message.info*gz
%{_infodir}/new-users-guide.info*gz
%{_infodir}/send-pr.info*gz
%{_infodir}/term.info*gz
%{_infodir}/vhdl-mode.info*gz
%{_infodir}/widget.info*gz
%{_infodir}/xemacs-faq.info*gz
%{_infodir}/xemacs.info*gz
%{_datadir}/*/etc/*.xbm
%{_datadir}/*/etc/*.xpm
%{_datadir}/*/etc/cbx.png
%{_datadir}/*/etc/custom
%{_datadir}/*/etc/e/e*
%{_datadir}/*/etc/ediff
%{_datadir}/*/etc/eos
%{_datadir}/*/etc/frame-icon
%{_datadir}/*/etc/idd
%{_datadir}/*/etc/message
%{_datadir}/*/etc/mine
%{_datadir}/*/etc/ms-kermit
%{_datadir}/*/etc/ms-kermit-7bit
%{_datadir}/*/etc/smilies
%{_datadir}/*/etc/sounds
%{_datadir}/*/etc/sparcworks
%{_datadir}/*/etc/spook.lines
%{_datadir}/*/etc/time
%{_datadir}/*/etc/toolbar
%{_datadir}/*/etc/slider
%{_datadir}/*/etc/xemacs-fe.sh
%{_datadir}/*/etc/yow.lines
%{_datadir}/*/etc/xemacs-enhanced.png
%{_datadir}/*/etc/sokoban.levels
%{_datadir}/*/etc/forms-d2.dat
%{_datadir}/*/lisp/*.el
%{_datadir}/*/lisp/apel/*.elc
%{_datadir}/*/lisp/calendar/*.elc
%{_datadir}/*/lisp/cc-mode/*.elc
%{_datadir}/*/lisp/cus*.elc
%{_datadir}/*/lisp/ediff/*.elc
%{_datadir}/*/lisp/efs/*.elc
%{_datadir}/*/lisp/eterm/*.elc
%{_datadir}/*/lisp/games/*.elc
%{_datadir}/*/lisp/misc-games/*.elc
%{_datadir}/*/lisp/mine/*.elc
%{_datadir}/*/lisp/blessmail*.elc
%{_datadir}/*/lisp/Sun/*.elc
%{_datadir}/*/lisp/term/*.elc
%{_datadir}/*/lisp/tooltalk/*.elc
%{_datadir}/*/lisp/forms/*.elc
%{_datadir}/*/lisp/slider/*.elc
%{_datadir}/*/lisp/vc/*.elc
%{_datadir}/*/lisp/cookie/*.elc
%{_datadir}/*/lisp/dired/*.elc
%{_datadir}/*/lisp/edit-utils/*.elc
%{_datadir}/*/lisp/emerge/*.elc
%{_datadir}/*/lisp/eudc/*.elc
%{_datadir}/*/lisp/frame-icon/*.elc
%{_datadir}/*/lisp/fsf-compat/*.elc
%{_datadir}/*/lisp/igrep/*.elc
%{_datadir}/*/lisp/ispell/*.elc
%{_datadir}/*/lisp/net-utils/*.elc
%{_datadir}/*/lisp/os-utils/*.elc
%{_datadir}/*/lisp/pc/*.elc
%{_datadir}/*/lisp/sounds-au/*.elc
%{_datadir}/*/lisp/sounds-wav/*.elc
%{_datadir}/*/lisp/speedbar/*.elc
%{_datadir}/*/lisp/strokes/*.elc
%{_datadir}/*/lisp/textools/*.elc
%{_datadir}/*/lisp/time/*.elc
%{_datadir}/*/lisp/view-process/*.elc
%{_datadir}/*/lisp/xemacs-base/*.elc
%{_datadir}/*/lisp/a*.elc
%{_datadir}/*/lisp/ba*.elc
%{_datadir}/*/lisp/bu*.elc
%{_datadir}/*/lisp/ca*.elc
%{_datadir}/*/lisp/ch*.elc
%{_datadir}/*/lisp/cm*.elc
%{_datadir}/*/lisp/co*.elc
%{_datadir}/*/lisp/d*.elc
%{_datadir}/*/lisp/e*.elc
%{_datadir}/*/lisp/f*.elc
%{_datadir}/*/lisp/g*.elc
%{_datadir}/*/lisp/h*.elc
%{_datadir}/*/lisp/i*.elc
%{_datadir}/*/lisp/k*.elc
%{_datadir}/*/lisp/l*.elc
%{_datadir}/*/lisp/m*.elc
%{_datadir}/*/lisp/o*.elc
%{_datadir}/*/lisp/p*.elc
%{_datadir}/*/lisp/r*.elc
%{_datadir}/*/lisp/s*.elc
%{_datadir}/*/lisp/t*.elc
%{_datadir}/*/lisp/u*.elc
%{_datadir}/*/lisp/v*.elc
%{_datadir}/*/lisp/wid*.elc
%{_datadir}/*/lisp/window*.elc
%{_datadir}/*/lisp/x-*.elc
%lang(de) /usr/X11R6/lib/X11/de/app-defaults/Emacs
%lang(fr) /usr/X11R6/lib/X11/fr/app-defaults/Emacs
%lang(ja) /usr/X11R6/lib/X11/ja/app-defaults/Emacs
%lang(ro) /usr/X11R6/lib/X11/ro/app-defaults/Emacs
/usr/X11R6/lib/X11/app-defaults/Emacs
/var/lock/xemacs

%files el 
%defattr(644,root,root,755)
%{_datadir}/*/lisp/apel/*.el.gz
%{_datadir}/*/lisp/calendar/*.el.gz
%{_datadir}/*/lisp/cc-mode/*.el.gz
%{_datadir}/*/lisp/cus*.el.gz
%{_datadir}/*/lisp/ediff/*.el.gz
%{_datadir}/*/lisp/efs/*.el.gz
%{_datadir}/*/lisp/eterm/*.el.gz
%{_datadir}/*/lisp/games/*.el.gz
%{_datadir}/*/lisp/misc-games/*.el.gz
%{_datadir}/*/lisp/mine/*.el.gz
%{_datadir}/*/lisp/blessmail*.el.gz
%{_datadir}/*/lisp/Sun/*.el.gz
%{_datadir}/*/lisp/term/*.el.gz
%{_datadir}/*/lisp/tooltalk/*.el.gz
%{_datadir}/*/lisp/forms/*.el.gz
%{_datadir}/*/lisp/slider/*.el.gz
%{_datadir}/*/lisp/vc/*.el.gz
%{_datadir}/*/lisp/cookie/*.el.gz
%{_datadir}/*/lisp/dired/*.el.gz
%{_datadir}/*/lisp/edit-utils/*.el.gz
%{_datadir}/*/lisp/emerge/*.el.gz
%{_datadir}/*/lisp/eudc/*.el.gz
%{_datadir}/*/lisp/frame-icon/*.el.gz
%{_datadir}/*/lisp/fsf-compat/*.el.gz
%{_datadir}/*/lisp/igrep/*.el.gz
%{_datadir}/*/lisp/ispell/*.el.gz
%{_datadir}/*/lisp/net-utils/*.el.gz
%{_datadir}/*/lisp/os-utils/*.el.gz
%{_datadir}/*/lisp/sounds-au/*.el.gz
%{_datadir}/*/lisp/sounds-wav/*.el.gz
%{_datadir}/*/lisp/speedbar/*.el.gz
%{_datadir}/*/lisp/strokes/*.el.gz
%{_datadir}/*/lisp/textools/*.el.gz
%{_datadir}/*/lisp/time/*.el.gz
%{_datadir}/*/lisp/view-process/*.el.gz
%{_datadir}/*/lisp/xemacs-base/*.el.gz
%{_datadir}/*/lisp/a*.el.gz
%{_datadir}/*/lisp/ba*.el.gz
%{_datadir}/*/lisp/bu*.el.gz
%{_datadir}/*/lisp/ca*.el.gz
%{_datadir}/*/lisp/ch*.el.gz
%{_datadir}/*/lisp/cm*.el.gz
%{_datadir}/*/lisp/co*.el.gz
%{_datadir}/*/lisp/d*.el.gz
%{_datadir}/*/lisp/e*.el.gz
%{_datadir}/*/lisp/f*.el.gz
%{_datadir}/*/lisp/g*.el.gz
%{_datadir}/*/lisp/h*.el.gz
%{_datadir}/*/lisp/i*.el.gz
%{_datadir}/*/lisp/k*.el.gz
%{_datadir}/*/lisp/l*.el.gz
%{_datadir}/*/lisp/m*.el.gz
%{_datadir}/*/lisp/o*.el.gz
%{_datadir}/*/lisp/p*.el.gz
%{_datadir}/*/lisp/r*.el.gz
%{_datadir}/*/lisp/s*.el.gz
%{_datadir}/*/lisp/t*.el.gz
%{_datadir}/*/lisp/u*.el.gz
%{_datadir}/*/lisp/v*.el.gz
%{_datadir}/*/lisp/wid*.el.gz
%{_datadir}/*/lisp/window*.el.gz
%{_datadir}/*/lisp/x-*.el.gz

%files emulators 
%defattr(644,root,root,755)
%doc %{_datadir}/*/lisp/crisp/ChangeLog*
%doc %{_datadir}/*/lisp/edt/ChangeLog*
%doc %{_datadir}/*/lisp/tpu/ChangeLog*
%dir %{_datadir}/*/lisp/crisp
%dir %{_datadir}/*/lisp/edt
%dir %{_datadir}/*/lisp/tpu
%{_datadir}/*/lisp/crisp/*.elc
%{_datadir}/*/lisp/edt/*.elc
%{_datadir}/*/lisp/tpu/*.elc
%{_datadir}/*/etc/tpu-edt.xmodmap

%files emulators-el
%defattr(644,root,root,755)
%{_datadir}/*/lisp/crisp/*.el.gz
%{_datadir}/*/lisp/edt/*.el.gz
%{_datadir}/*/lisp/tpu/*.el.gz

%files gnats
%defattr(644,root,root,755)
%{_infodir}/gnats.info*gz
%doc %{_datadir}/*/lisp/gnats/ChangeLog*
%dir %{_datadir}/*/lisp/gnats
%{_datadir}/*/etc/gnats
%{_datadir}/*/lisp/gnats/*.elc

%files gnats-el
%defattr(644,root,root,755)
%{_datadir}/*/lisp/gnats/*.el.gz

%files viper 
%defattr(644,root,root,755)
%doc %{_datadir}/*/etc/viperCard.tex
%{_infodir}/viper.info*gz
%doc %{_datadir}/*/lisp/viper/README
%doc %{_datadir}/*/lisp/viper/ChangeLog*
%dir %{_datadir}/*/lisp/viper
%{_datadir}/*/lisp/viper/*.elc

%files viper-el
%defattr(644,root,root,755)
%{_datadir}/*/lisp/viper/*.el.gz

%files lisp-programming
%defattr(644,root,root,755)
%{_infodir}/cl.info*gz
%{_infodir}/ilisp.info*gz
%{_infodir}/lispref.info*gz
%{_infodir}/elib.info*gz
%doc %{_datadir}/*/lisp/edebug/README
%doc %{_datadir}/*/lisp/edebug/ChangeLog*
%doc %{_datadir}/*/lisp/ilisp/ACKNOWLEDGMENTS
%doc %{_datadir}/*/lisp/ilisp/ChangeLog*
%doc %{_datadir}/*/lisp/ilisp/GETTING-ILISP
%doc %{_datadir}/*/lisp/ilisp/HISTORY
%doc %{_datadir}/*/lisp/ilisp/README
%doc %{_datadir}/*/lisp/ilisp/Welcome
%doc %{_datadir}/*/lisp/elib/ChangeLog*
%doc %{_datadir}/*/lisp/elib/README
%doc %{_datadir}/*/lisp/elib/NEWS
%doc %{_datadir}/*/lisp/xemacs-devel/ChangeLog*
%dir %{_datadir}/*/lisp/edebug
%dir %{_datadir}/*/lisp/elib
%dir %{_datadir}/*/lisp/ilisp
%dir %{_datadir}/*/lisp/xemacs-devel
%{_datadir}/*/lisp/byte*.elc
%{_datadir}/*/lisp/cl*.elc
%{_datadir}/*/lisp/edebug/*.elc
%{_datadir}/*/lisp/elib/*.elc
%{_datadir}/*/lisp/ilisp/*.elc
%{_datadir}/*/lisp/ilisp/*.lisp
%{_datadir}/*/lisp/ilisp/ild.mail
%{_datadir}/*/lisp/ilisp/ilisp.emacs
%{_datadir}/*/lisp/ilisp/scheme2c.mail
%{_datadir}/*/lisp/xemacs-devel/*.elc

%files lisp-programming-el
%defattr(644,root,root,755)
%{_datadir}/*/lisp/elib/*.el.gz
%{_datadir}/*/lisp/ilisp/*.el.gz
%{_datadir}/*/lisp/edebug/*.el.gz
%{_datadir}/*/lisp/xemacs-devel/*.el.gz
%{_datadir}/*/lisp/byte*.el.gz
%{_datadir}/*/lisp/cl*.el.gz

%files auctex
%defattr(644,root,root,755)
%{_infodir}/auctex.info*gz
%{_infodir}/reftex.info*gz
%doc %{_datadir}/*/lisp/auctex/CHANGES
%doc %{_datadir}/*/lisp/auctex/ChangeLog*
%doc %{_datadir}/*/lisp/auctex/README
%doc %{_datadir}/*/lisp/reftex/ChangeLog*
%dir %{_datadir}/*/etc/auctex
%dir %{_datadir}/*/etc/auctex/style
%dir %{_datadir}/*/lisp/auctex
%dir %{_datadir}/*/lisp/reftex
%{_datadir}/*/lisp/reftex/*.elc
%{_datadir}/*/etc/auctex/style/*.elc
%{_datadir}/*/lisp/auctex/*.elc
%doc %{_datadir}/*/lisp/auctex/PROBLEMS

%files auctex-el
%defattr(644,root,root,755)
%{_datadir}/*/lisp/auctex/*.el.gz
%{_datadir}/*/etc/auctex/style/*.el.gz
%{_datadir}/*/lisp/reftex/*.el.gz

%files w3 
%defattr(644,root,root,755)
%{_infodir}/w3-faq.info*gz
%{_infodir}/w3.info*gz
%doc %{_datadir}/*/lisp/w3/ChangeLog*
%doc %{_datadir}/*/lisp/w3/BUGS
%doc %{_datadir}/*/lisp/w3/HOWTO
%doc %{_datadir}/*/lisp/w3/README
%doc %{_datadir}/*/lisp/w3/TODO
%dir %{_datadir}/*/lisp/w3
%{_datadir}/*/etc/w3
%{_datadir}/*/lisp/w3/*.elc

%files w3-el
%defattr(644,root,root,755)
%{_datadir}/*/lisp/w3/*.el.gz

%files psgml 
%defattr(644,root,root,755)
%{_infodir}/hm--html-mode.info*gz
%{_infodir}/psgml-api.info*gz
%{_infodir}/psgml.info*gz
%doc %{_datadir}/*/lisp/psgml/ChangeLog*
%doc %{_datadir}/*/lisp/sgml/ChangeLog*
%doc %{_datadir}/*/lisp/hm--html-menus/ChangeLog*
%dir %{_datadir}/*/lisp/hm--html-menus
%dir %{_datadir}/*/lisp/psgml
%dir %{_datadir}/*/lisp/sgml
%{_datadir}/*/etc/hm--html-menus
%{_datadir}/*/etc/psgml
%{_datadir}/*/lisp/hm--html-menus/*.elc
%{_datadir}/*/lisp/psgml/*.elc
%{_datadir}/*/lisp/sgml/*.elc

%files psgml-el
%defattr(644,root,root,755)
%{_datadir}/*/lisp/psgml/*.el.gz
%{_datadir}/*/lisp/sgml/*.el.gz
%{_datadir}/*/lisp/hm--html-menus/*.el.gz

%files modes 
%defattr(644,root,root,755)
%{_infodir}/pcl-cvs.info*gz
%doc %{_datadir}/*/lisp/pcl-cvs/ChangeLog*
%doc %{_datadir}/*/lisp/ada/ChangeLog*
%doc %{_datadir}/*/lisp/c-support/ChangeLog*
%doc %{_datadir}/*/lisp/debug/ChangeLog*
%doc %{_datadir}/*/lisp/pc/ChangeLog*
%doc %{_datadir}/*/lisp/prog-modes/ChangeLog*
%doc %{_datadir}/*/lisp/scheme/ChangeLog*
%doc %{_datadir}/*/lisp/sh-script/ChangeLog*
%doc %{_datadir}/*/lisp/texinfo/ChangeLog*
%doc %{_datadir}/*/lisp/text-modes/ChangeLog*
%doc %{_datadir}/*/lisp/vhdl/ChangeLog*
%dir %{_datadir}/*/lisp/pcl-cvs
%dir %{_datadir}/*/lisp/ada
%dir %{_datadir}/*/lisp/c-support
%dir %{_datadir}/*/lisp/debug
%dir %{_datadir}/*/lisp/pc
%dir %{_datadir}/*/lisp/prog-modes
%dir %{_datadir}/*/lisp/scheme
%dir %{_datadir}/*/lisp/sh-script
%dir %{_datadir}/*/lisp/texinfo
%dir %{_datadir}/*/lisp/text-modes
%dir %{_datadir}/*/lisp/vhdl
%{_datadir}/*/lisp/pcl-cvs/*.elc
%{_datadir}/*/lisp/ada/*.elc
%{_datadir}/*/lisp/c-support/*.elc
%{_datadir}/*/lisp/debug/*.elc
%{_datadir}/*/lisp/pc/*.elc
%{_datadir}/*/lisp/prog-modes/*.elc
%{_datadir}/*/lisp/scheme/*.elc
%{_datadir}/*/lisp/sh-script/*.elc
%{_datadir}/*/lisp/texinfo/*.elc
%{_datadir}/*/lisp/text-modes/*.elc
%{_datadir}/*/lisp/vhdl/*.elc

%files modes-el
%defattr(644,root,root,755)
%{_datadir}/*/lisp/pcl-cvs/*.el.gz
%{_datadir}/*/lisp/ada/*.el.gz
%{_datadir}/*/lisp/c-support/*.el.gz
%{_datadir}/*/lisp/debug/*.el.gz
%{_datadir}/*/lisp/pc/*.el.gz
%{_datadir}/*/lisp/prog-modes/*.el.gz
%{_datadir}/*/lisp/scheme/*.el.gz
%{_datadir}/*/lisp/sh-script/*.el.gz
%{_datadir}/*/lisp/texinfo/*.el.gz
%{_datadir}/*/lisp/text-modes/*.el.gz
%{_datadir}/*/lisp/vhdl/*.el.gz

%files extras
%attr(755,root,root) %{_bindir}/b2m
%attr(755,root,root) %{_bindir}/rcs-checkin

%files mail
%defattr(644,root,root,755)
%{_infodir}/mailcrypt.info*gz
%{_infodir}/mew.info*gz
%lang(ja) %{_infodir}/mew.jis.info*gz
%{_infodir}/mh-e.info*gz
%{_infodir}/rmail.info*gz
%{_infodir}/supercite.info*gz
%{_infodir}/tm-edit-en.info*gz
%{_infodir}/tm-en.info*gz
%{_infodir}/tm-mh-e-en.info*gz
%{_infodir}/tm-view-en.info*gz
%{_infodir}/tm-vm-en.info*gz
%lang(ja) %{_infodir}/tm*ja*.info.gz
%{_infodir}/vm.info*gz
%doc %{_datadir}/*/lisp/mailcrypt/ChangeLog*
%doc %{_datadir}/*/lisp/mail-lib/ChangeLog*
%doc %{_datadir}/*/lisp/mew/ChangeLog*
%doc %{_datadir}/*/lisp/mh-e/ChangeLog*
%doc %{_datadir}/*/lisp/rmail/ChangeLog*
%doc %{_datadir}/*/lisp/tm/ChangeLog*
%doc %{_datadir}/*/lisp/vm/ChangeLog*
%doc %{_datadir}/*/lisp/footnote/ChangeLog*
%doc %{_datadir}/*/lisp/supercite/ChangeLog*
%attr(755,root,root) %{_libdir}/%{name}-%{realversion}/*/tm*
%dir %{_datadir}/*/lisp/mailcrypt
%dir %{_datadir}/*/lisp/mail-lib
%dir %{_datadir}/*/lisp/mew
%dir %{_datadir}/*/lisp/mh-e
%dir %{_datadir}/*/lisp/rmail
%dir %{_datadir}/*/lisp/tm
%dir %{_datadir}/*/lisp/vm
%dir %{_datadir}/*/lisp/footnote
%dir %{_datadir}/*/lisp/supercite
%{_datadir}/*/etc/vm
%{_datadir}/*/etc/mew
%{_datadir}/*/lisp/mailcrypt/*.elc
%{_datadir}/*/lisp/mail-lib/*.elc
%{_datadir}/*/lisp/mew/*.elc
%{_datadir}/*/lisp/mh-e/*.elc
%{_datadir}/*/lisp/rmail/*.elc
%{_datadir}/*/lisp/tm/*.elc
%{_datadir}/*/lisp/vm/*.elc
%{_datadir}/*/lisp/footnote/*.elc
%{_datadir}/*/lisp/supercite/*.elc

%files mail-el
%defattr(644,root,root,755)
%{_datadir}/*/lisp/tm/*.el.gz
%{_datadir}/*/lisp/mew/*.el.gz
%{_datadir}/*/lisp/mail-lib/*.el.gz
%{_datadir}/*/lisp/vm/*.el.gz
%{_datadir}/*/lisp/mh-e/*.el.gz
%{_datadir}/*/lisp/mailcrypt/*.el.gz
%{_datadir}/*/lisp/rmail/*.el.gz
%{_datadir}/*/lisp/footnote/*.el.gz
%{_datadir}/*/lisp/supercite/*.el.gz

%files gnus
%defattr(644,root,root,755)
%doc %{_datadir}/*/lisp/gnus/ChangeLog*
%doc %{_datadir}/*/etc/gnusrefcard
%doc %{_datadir}/*/etc/gnus-tut.txt
%doc %{_infodir}/gnus-mime-en.info*gz
%doc %{_infodir}/gnus.info*gz
%lang(ja) %doc %{_infodir}/gnus-mime-ja.info*gz
%dir %{_datadir}/*/lisp/gnus
%{_datadir}/*/etc/gnus
%{_datadir}/*/lisp/gnus/*.elc

%files gnus-el
%defattr(644,root,root,755)
%{_datadir}/*/lisp/gnus/*.el.gz

%files zenirc
%defattr(644,root,root,755)
%{_infodir}/zenirc.info*gz
%doc %{_datadir}/*/lisp/zenirc/BUGS
%doc %{_datadir}/*/lisp/zenirc/ChangeLog*
%doc %{_datadir}/*/lisp/zenirc/NEWS
%doc %{_datadir}/*/lisp/zenirc/TODO
%doc %{_datadir}/*/etc/zenirc
%dir %{_datadir}/*/lisp/zenirc
%{_datadir}/*/lisp/zenirc/*.elc

%files zenirc-el
%defattr(644,root,root,755)
%{_datadir}/*/lisp/zenirc/*.el.gz

%files bbdb
%defattr(644,root,root,755)
#%{_infodir}/bbdb.info*gz
%doc %{_datadir}/*/lisp/bbdb/ChangeLog*
%doc %{_datadir}/*/lisp/bbdb/README
#%doc %{_datadir}/*/etc/bbdb/tex
#%attr(755,root,root) %{_datadir}/*/etc/bbdb/*.pl
#%dir %{_datadir}/*/etc/bbdb
%dir %{_datadir}/*/lisp/bbdb
#%{_datadir}/*/etc/bbdb/*.el
%{_datadir}/*/lisp/bbdb/*.elc

%files bbdb-el
%defattr(644,root,root,755)
%{_datadir}/*/lisp/bbdb/*.el.gz

%files calc
%defattr(644,root,root,755)
%{_infodir}/calc.info*gz
%doc %{_datadir}/*/lisp/calc/ChangeLog*
%doc %{_datadir}/*/etc/calccard*
%dir %{_datadir}/*/lisp/calc
%{_datadir}/*/lisp/calc/*.elc

%files calc-el
%defattr(644,root,root,755)
%{_datadir}/*/lisp/calc/*.el.gz

%files mule
%defattr(644,root,root,755)
%{_infodir}/skk.info*gz
%doc %{_datadir}/*/etc/mule/FAQ-Mule
%doc %lang(cn) %{_datadir}/*/etc/mule/*.cn
%doc %lang(ja) %{_datadir}/*/etc/mule/*.ja
%doc %lang(kr) %{_datadir}/*/etc/mule/*.kr
%doc %lang(th) %{_datadir}/*/etc/mule/*.th
%doc %{_datadir}/*/etc/mule/*.1
%doc %{_datadir}/*/etc/mule/*.ps
%doc %{_datadir}/*/etc/mule/*.tex
%doc %{_datadir}/*/etc/mule/*.xbm
%doc %{_datadir}/*/etc/mule/VERSIONS
%doc %lang(th) %{_datadir}/*/etc/mule-doc/Thai
%doc %lang(vt) %{_datadir}/*/etc/mule-doc/viet
%doc %lang(ja) %{_datadir}/*/etc/mule-doc/*.ja
%doc %lang(cn) %{_datadir}/*/etc/mule-doc/*.cn
%doc %{_datadir}/*/etc/mule-doc/ChangeLog*
%doc %{_datadir}/*/etc/mule-doc/NEWFEATURE
%doc %{_datadir}/*/etc/mule-doc/README.Mule
%doc %{_datadir}/*/etc/mule-doc/arabic.txt
%doc %{_datadir}/*/etc/mule-doc/sample.ks
%doc %{_datadir}/*/etc/skk
%lang(fr) %{_datadir}/*/etc/start-files/fr
%lang(ja) %{_datadir}/*/etc/start-files/ja
%lang(ro) %{_datadir}/*/etc/start-files/ro
%doc %{_datadir}/*/lisp/edict/ChangeLog*
%doc %{_datadir}/*/lisp/edict/edictj.demo
%doc %{_datadir}/*/lisp/egg-its/ChangeLog*
%doc %{_datadir}/*/lisp/leim/ChangeLog*
%doc %{_datadir}/*/lisp/locale/ChangeLog*
%doc %{_datadir}/*/lisp/mule-base/ChangeLog*
%doc %{_datadir}/*/lisp/skk/ChangeLog*
%dir %{_datadir}/*/etc/mule
%dir %lang(th) %{_datadir}/*/etc/mule-doc
%dir %{_datadir}/*/lisp/edict
%dir %{_datadir}/*/lisp/egg-its
%dir %{_datadir}/*/lisp/leim
%dir %{_datadir}/*/lisp/leim/quail
%dir %{_datadir}/*/lisp/locale
%dir %{_datadir}/*/lisp/mule
%dir %{_datadir}/*/lisp/mule-base
%dir %{_datadir}/*/lisp/skk
%{_datadir}/*/lisp/edict/*.elc
%{_datadir}/*/lisp/egg-its/eggrc*
%{_datadir}/*/lisp/egg-its/*.elc
%{_datadir}/*/lisp/leim/quail/*.elc
%{_datadir}/*/lisp/leim/*.elc
%{_datadir}/*/lisp/locale/*.elc
#%{_datadir}/*/lisp/mule/*.elc
%{_datadir}/*/lisp/mule-base/*.elc
%{_datadir}/*/lisp/skk/*.elc

%files mule-el
%defattr(644,root,root,755)
%{_datadir}/*/lisp/edict/*.el.gz
%{_datadir}/*/lisp/egg-its/*.el.gz
%{_datadir}/*/lisp/leim/quail/*.el.gz
%{_datadir}/*/lisp/leim/*.el.gz
%{_datadir}/*/lisp/locale/*.el.gz
#%{_datadir}/*/lisp/mule/*.el.gz
%{_datadir}/*/lisp/mule-base/*.el.gz
%{_datadir}/*/lisp/skk/*.el.gz

%files jde
%defattr(644,root,root,755)
%doc %{_datadir}/*/etc/jde/*.gif
%doc %{_datadir}/*/etc/jde/*.htm*
%doc %{_datadir}/*/lisp/jde/ChangeLog*
%dir %{_datadir}/*/etc/jde
%dir %{_datadir}/*/lisp/jde
%{_datadir}/*/etc/jde/java
%{_datadir}/*/lisp/jde/*.elc

%files jde-el
%defattr(644,root,root,755)
%{_datadir}/*/lisp/jde/*.el.gz
