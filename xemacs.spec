Summary:	The XEmacs editor
Summary(pl):	XEmacs -- Edytor
Name:		xemacs
version:	20.4
Release:	8
Copyright:	GPL
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Source0:	ftp://ftp.xemacs.org/pub/xemacs/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:	xemacs.wmconfig
Patch0:		xemacs-static.patch
Patch1:		xemacs-perl.patch
Patch2:		xemacs-alpha.patch
URL:		http://www.xemacs.org/
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
Wywodzi siê z wczesnych odmian GNU Emacs 19, dodaje wiele mi³ych 
udogodnieñ  nie trac±c jednak wiêzi z oryginaln± wersj±. 

Ta dystrubucja XEmacsa zosta³± podzielona na wiele pakietów binarnych. 
Do pracy niezbêdne s± dwa z nich:
- xemacs:        g³ówny pakiet
- xemacs-extras: pliki chodz±ce w sk³ad dystrybucji GNU Emacs
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
Summary(pl):	Pliki ¼ród³owe dla xemacs-programming
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	%{name} = %{version}

%description lisp-programming-el  
.el source files for xemacs-lisp-programming.

%description lisp-programming-el -l pl 
Pliki ¼ród³owe dla xemacs-programming.

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
S± to wpólne pliki GNU Emacs and XEmacs. Je¶li nie zainstalowa³e¶ GNU EMacsa
zainstaluj koniecznie ten pakiet.

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
Summary(pl):	The XEmacs editor
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
Summary(pl):	The XEmacs editor
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	%{name} = %{version}, %{name}-mail

%description gnus
Xemacs -- gnus mode for XEmacs.

%description gnus -l pl 
Xemacs -- poczta i UseNet News w XEmacsie.

%package gnus-el
Summary:	.el source files for xemacs-mail
Summary(pl):	Pliki ¼ród³owe dla xemacs-gnus
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	%{name} = %{version}, 

%description gnus-el
.el gnus source files -- not necessary to run XEmacs.

%description gnus-el -l pl 
Pliki ¼ród³owe dla xemacs-gnus.

%prep
%setup -q -T -b 0 -n xemacs-%{version}
%patch0 -p1
chmod u+wXr * -R
%patch1 -p0

%ifarch alpha
%patch2 -p1
%endif

%build
CFLAGS="$RPM_OPT_FLAGS" CPPFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s -lc" \
./configure %{_target_platform} \
	--prefix=/usr \
	--infodir=%{_infodir} \
	--with-dialogs=athena \
	--with-sound=nas \
	--cflags="$RPM_OPT_FLAGS" \
	--error-checking=none \
	--debug=no \
	--with-xpm \
	--with-ncurses \
	--lockdir=/var/lock/xemacs \
	--with-session=yes \
	--with-gpm=yes \
	--with-png=yes \
	%{buildarch}-pld-`echo %{buildos} | tr A-Z a-z`

make dist
# xemacs generation
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/X11/wmconfig,var/lock/xemacs} \
	$RPM_BUILD_ROOT/usr/{man/{ja/man1,man1},X11R6/lib/X11/{ja/app-defaults,app-defaults}}

make install-arch-dep install-arch-indep gzip-el \
	prefix=$RPM_BUILD_ROOT/usr \
	infodir=$RPM_BUILD_ROOT%{_infodir}

gzip -9nf $RPM_BUILD_ROOT%{_infodir}/*info*
find $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/etc/auctex/style/ -name \*.el | xargs gzip -9

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/xemacs

find $RPM_BUILD_ROOT%{_bindir} -type f |xargs  file |grep stripped|  awk -F: '{print $1}' | xargs strip 
find $RPM_BUILD_ROOT%{_libdir}/*/* -type f |xargs  file |grep stripped|  awk -F: '{print $1}' | xargs strip 

mv $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/etc/Emacs.ad \
	$RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults/Emacs
mv $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/etc/app-defaults/ja/Emacs \
	$RPM_BUILD_ROOT/usr/X11R6/lib/X11/ja/app-defaults/Emacs
mv $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/etc/xemacs-ja.1 \
	$RPM_BUILD_ROOT%{_mandir}/ja/man1/xemacs.1

mv -f $RPM_BUILD_ROOT%{_bindir}/xemacs-%{version} \
	$RPM_BUILD_ROOT%{_bindir}/xemacs

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/{ja/man1/*,man1/*}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info %{_infodir}/cc-mode.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* CC mode: (ccmode).    The GNU Emacs mode for editing C, C++, Objective-C and Java code."
/sbin/install-info %{_infodir}/cl.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* CL: (cl).             Partial Common Lisp support for Emacs Lisp."
/sbin/install-info %{_infodir}/forms.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* Forms: (forms).       Emacs package for editing data bases by filling in forms."
/sbin/install-info %{_infodir}/xemacs.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* Emacs: (emacs).       The extensible self-documenting text editor."
/sbin/install-info %{_infodir}/ilisp.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* ilisp: (ilisp).       ILISP manual"
/sbin/install-info %{_infodir}/lispref.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* lispref: (lispref).   GNU Emacs Lisp Reference Manual"
/sbin/install-info %{_infodir}/custom.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* custom: (custom).     The Customization Library"
/sbin/install-info %{_infodir}/efs.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* efs: (efs).           Transparent remote file access via FTP"
/sbin/install-info %{_infodir}/external-widget.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* external-widget: (external-widget).External Client Widget"
/sbin/install-info %{_infodir}/internals.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* internals: (internals).internals"
/sbin/install-info %{_infodir}/new-users-guide.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* new-users-guide: (new-users-guide). introduction to the XEmacs editor"
/sbin/install-info %{_infodir}/ph.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* ph: (ph).             E-Lisp client interface to the CCSO white pages directory system also known as PH/QI"
/sbin/install-info %{_infodir}/send-pr.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* send-pr: (send-pr).   Reporting problems--using send-pr"
/sbin/install-info %{_infodir}/term.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* term: (term).         Terminal emulator mode"
/sbin/install-info %{_infodir}/vhdl-mode.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* vhdl-mode: (vhdl-mode). vhdl-mode"
/sbin/install-info %{_infodir}/widget.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* widget: (widget).     The Emacs Widget Library"
/sbin/install-info %{_infodir}/xemacs-faq.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* xemacs-faq: (xemacs-faq). The Xemacs FAQ"

%preun
if [ "$1" = 0 ]; then
	/sbin/install-info --delete %{_infodir}/cc-mode.info.gz /etc/info-dir
	/sbin/install-info --delete %{_infodir}/cl.info.gz /etc/info-dir
	/sbin/install-info --delete %{_infodir}/forms.info.gz /etc/info-dir
	/sbin/install-info --delete %{_infodir}/xemacs.info.gz /etc/info-dir
	/sbin/install-info --delete %{_infodir}/ilisp.info.gz /etc/info-dir
	/sbin/install-info --delete %{_infodir}/lispref.info.gz /etc/info-dir
	/sbin/install-info --delete %{_infodir}/pcl-cvs.info.gz /etc/info-dir
	/sbin/install-info --delete %{_infodir}/custom.info.gz /etc/info-dir
	/sbin/install-info --delete %{_infodir}/efs.info.gz /etc/info-dir
	/sbin/install-info --delete %{_infodir}/external-widget.info.gz /etc/info-dir
	/sbin/install-info --delete %{_infodir}/internals.info.gz /etc/info-dir
	/sbin/install-info --delete %{_infodir}/new-users-guide.info.gz /etc/info-dir
	/sbin/install-info --delete %{_infodir}/ph.info.gz /etc/info-dir
	/sbin/install-info --delete %{_infodir}/send-pr.info.gz /etc/info-dir
	/sbin/install-info --delete %{_infodir}/term.info.gz /etc/info-dir
	/sbin/install-info --delete %{_infodir}/vhdl-mode.info.gz /etc/info-dir
	/sbin/install-info --delete %{_infodir}/widget.info.gz /etc/info-dir
	/sbin/install-info --delete %{_infodir}/xemacs-faq.info.gz /etc/info-dir
fi

%post gnats
/sbin/install-info %{_infodir}/gnats.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* gnats: (gnats).       GNU Problem Report Management System"

%preun gnats
if [ "$1" = $1 ]; then
	/sbin/install-info --delete %{_infodir}/gnats.info.gz /etc/info-dir
fi

%post viper
/sbin/install-info %{_infodir}/viper.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* VIPER: (viper).       The new VI-emulation mode in Emacs-19.29."

%preun viper
if [ "$1" = $1 ]; then
	/sbin/install-info --delete %{_infodir}/viper.info.gz /etc/info-dir
fi

%post auctex
/sbin/install-info %{_infodir}/auctex.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* auctex: (auctex).     TeX mode"
/sbin/install-info %{_infodir}/reftex.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* reftex: (reftex).     RefTeX, a package to do labels, references and citations for LaTeX documents with Emacs"

%preun auctex
if [ "$1" = $1 ]; then
	/sbin/install-info --delete %{_infodir}/auctex.info.gz /etc/info-dir
	/sbin/install-info --delete %{_infodir}/reftex.info.gz /etc/info-dir
fi


%post w3
/sbin/install-info %{_infodir}/w3-faq.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* w3-faq: (w3-faq).     FAQ for Emacs/W3 World Wide Web browser"
/sbin/install-info %{_infodir}/w3.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* w3: (w3).             Emacs/W3 World Wide Web browser"

%preun w3
if [ "$1" = $1 ]; then
	/sbin/install-info --delete %{_infodir}/w3-faq.info.gz /etc/info-dir
	/sbin/install-info --delete %{_infodir}/w3.info.gz /etc/info-dir
fi

%preun modes
if [ "$1" = $1 ]; then
	/sbin/install-info %{_infodir}/pcl-cvs.info.gz /etc/info-dir
fi

%post modes
/sbin/install-info %{_infodir}/pcl-cvs.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* pcl-cvs: (pcl-cvs).   front-end to CVS"

%post psgml
/sbin/install-info %{_infodir}/psgml-api.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* psgml-api: (psgml-api). PSGML, the API documentation"
/sbin/install-info %{_infodir}/psgml.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* psgml: (psgml).       PSGML, a major mode for SGML"
/sbin/install-info %{_infodir}/hm--html-mode.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* hm--html-mode-xemacs: (hm--html-mode). hm--html-menus"

%preun psgml
if [ "$1" = $1 ]; then
	/sbin/install-info --delete %{_infodir}/psgml-api.info.gz /etc/info-dir
	/sbin/install-info --delete %{_infodir}/psgml.info.gz /etc/info-dir
	/sbin/install-info --delete %{_infodir}/hm--html-mode.info.gz /etc/info-dir
fi

%post mail 
/sbin/install-info %{_infodir}/mh-e.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* MH-E: (mh-e).         Emacs interface to the MH mail system."
/sbin/install-info %{_infodir}/supercite.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* SC: (sc).             Supercite lets you cite parts of messages you're replying to, in flexible ways."
/sbin/install-info %{_infodir}/rmail.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* rmail: (rmail).       Rmail mail reader"
/sbin/install-info %{_infodir}/tm-edit-en.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* tm-en: (tm-en).       tm-edit 7.100 Reference Manual"
/sbin/install-info %{_infodir}/tm-mh-e-en.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* tm-mh-e-en: (tm-mh-e-en). tm-mh-e 7.71 Reference Manual"
/sbin/install-info %{_infodir}/tm-view-en.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* tm-view-en: (tm-view-en). tm-view, a MIME Viewer for GNU Emacs"
/sbin/install-info %{_infodir}/tm-vm-en.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* tm-vm-en: (tm-vm-en). tm-vm is an interface between tm and the VM mail user agent"
/sbin/install-info %{_infodir}/vm.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* vm: (vm).             VM mail reader"

%preun mail 
if [ "$1" = $1 ]; then
	/sbin/install-info --delete %{_infodir}/mh-e.info.gz /etc/info-dir
	/sbin/install-info --delete %{_infodir}/supercite.info.gz /etc/info-dir
	/sbin/install-info --delete %{_infodir}/rmail.info.gz /etc/info-dir
	/sbin/install-info --delete %{_infodir}/tm-edit-en.info.gz /etc/info-dir
	/sbin/install-info --delete %{_infodir}/tm-mh-e-en.info.gz /etc/info-dir
	/sbin/install-info --delete %{_infodir}/tm-view-en.info.gz /etc/info-dir
	/sbin/install-info --delete %{_infodir}/tm-vm-en.info.gz /etc/info-dir
	/sbin/install-info --delete %{_infodir}/vm.info.gz /etc/info-dir
fi

%post gnus 
/sbin/install-info %{_infodir}/message.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* Message: (message).   Mail and news composition mode that goes with Gnus."
/sbin/install-info %{_infodir}/gnus.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* Gnus: (gnus).         The news reader Gnus."
/sbin/install-info %{_infodir}/gnus-mime-en.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* gnus-mime-en: (gnus-mime-en) gnus-mime 0.10 reference manual"

%preun gnus 
if [ "$1" = $1 ]; then
	/sbin/install-info --delete %{_infodir}/message.info.gz /etc/info-dir
	/sbin/install-info --delete %{_infodir}/gnus.info.gz /etc/info-dir
	/sbin/install-info --delete %{_infodir}/gnus-mime-en.info.gz
fi

%files
%defattr(644,root,root,755)
%config /etc/X11/wmconfig/xemacs
%attr(2755,root,mail) %{_libdir}/*/*/movemail
%attr(755,root,root) %{_bindir}/xemacs
%attr(755,root,root) %{_bindir}/gnuclient
%attr(755,root,root) %{_libdir}/*/*/cvtmail
%attr(755,root,root) %{_libdir}/*/*/digest-doc
%attr(755,root,root) %{_libdir}/*/*/fakemail
%attr(755,root,root) %{_libdir}/*/*/gnuserv
%attr(755,root,root) %{_libdir}/*/*/hexl
%attr(755,root,root) %{_libdir}/*/*/make-docfile
%attr(755,root,root) %{_libdir}/*/*/make-path
%attr(755,root,root) %{_libdir}/*/*/mmencode
%attr(755,root,root) %{_libdir}/*/*/profile
%attr(755,root,root) %{_libdir}/*/*/sorted-doc
%attr(755,root,root) %{_libdir}/*/*/yow
%attr(755,root,root) %{_bindir}/gnuattach
%attr(755,root,root) %{_bindir}/gnudoit
%attr(755,root,root) %{_bindir}/install-sid
%attr(755,root,root) %{_bindir}/pstogif
%attr(755,root,root) %{_bindir}/send-pr
%attr(755,root,root) %{_libdir}/*/*/add-big-package.sh
%attr(755,root,root) %{_libdir}/*/*/add-little-package.sh
%attr(755,root,root) %{_libdir}/*/*/gzip-el.sh
%attr(755,root,root) %{_libdir}/*/*/install-sid
%attr(755,root,root) %{_libdir}/*/*/rcs2log
%attr(755,root,root) %{_libdir}/*/*/send-pr
%attr(755,root,root) %{_libdir}/*/*/vcdiff
%attr(755,root,root) %{_libdir}/*/*/wakeup
%doc %lang(de) %{_libdir}/*/etc/TUTORIAL.de
%doc %lang(fr) %{_libdir}/*/etc/TUTORIAL.fr
%doc %lang(hr) %{_libdir}/*/etc/TUTORIAL.hr
%doc %lang(ja) %{_libdir}/*/etc/TUTORIAL.ja
%doc %lang(ko) %{_libdir}/*/etc/TUTORIAL.ko
%doc %lang(no) %{_libdir}/*/etc/TUTORIAL.no
%doc %lang(pl) %{_libdir}/*/etc/TUTORIAL.pl
%doc %lang(th) %{_libdir}/*/etc/TUTORIAL.th
%doc %{_libdir}/*/*/DOC
%doc %{_libdir}/*/etc/*.doc
%doc %{_libdir}/*/etc/README.HYPERBOLE
%doc %{_libdir}/*/etc/README.OO-BROWSER
%doc %{_libdir}/*/etc/e/README
%doc %{_libdir}/*/etc/gnuserv.README
%doc %{_libdir}/*/etc/hypb-mouse.txt
%doc %{_libdir}/*/etc/refcard.ps
%doc %{_libdir}/*/etc/refcard.tex
%doc %{_libdir}/*/etc/refcard3.ps
%doc %{_libdir}/*/etc/sample.Xdefaults
%doc %{_libdir}/*/etc/sample.emacs
%doc %{_libdir}/*/lisp/ChangeLog
%doc %{_libdir}/*/lisp/README
%doc %{_libdir}/*/lisp/apel/ChangeLog*
%doc %{_libdir}/*/lisp/ediff/README
%doc %{_libdir}/*/lisp/efs/README
%doc %{_libdir}/*/lisp/eterm/ChangeLog
%doc %{_libdir}/*/lisp/eterm/QUESTIONS
%doc %{_libdir}/*/lisp/eterm/README.term
%doc %{_libdir}/*/lisp/eterm/TODO.term
%doc %{_libdir}/*/lisp/mel/ChangeLog
%doc %{_libdir}/*/lisp/term/README
%{_mandir}/man1/gnuattach.1.gz
%{_mandir}/man1/gnuclient.1.gz
%{_mandir}/man1/gnudoit.1.gz
%{_mandir}/man1/gnuserv.1.gz
%{_mandir}/man1/xemacs.1.gz
%lang(ja) %{_mandir}/ja/man1/xemacs.1.gz
%doc README GETTING.GNU.SOFTWARE PROBLEMS 
%doc etc/NEWS etc/MAILINGLISTS BUGS 
%{_libdir}/*/*/config.values
%{_libdir}/*/etc/*.xbm
%{_infodir}/cc-mode.info*gz
%{_infodir}/custom.info*gz
%{_infodir}/efs.info*gz
%{_infodir}/external-widget.info*gz
%{_infodir}/forms.info*gz
%{_infodir}/internals.info*gz
%{_infodir}/message.info*gz
%{_infodir}/new-users-guide.info*gz
%{_infodir}/ph.info*gz
%{_infodir}/reftex.info*gz
%{_infodir}/send-pr.info*gz
%{_infodir}/term.info*gz
%{_infodir}/vhdl-mode.info*gz
%{_infodir}/widget.info*gz
%{_infodir}/xemacs-faq.info*gz
%{_infodir}/xemacs.info*gz
%{_libdir}/*/etc/*.xpm
%{_libdir}/*/etc/*.xpm.Z
%{_libdir}/*/etc/categories
%{_libdir}/*/etc/cbx.gif
%{_libdir}/*/etc/custom/*
%{_libdir}/*/etc/eos/*
%{_libdir}/*/etc/frame-icon/*
%{_libdir}/*/etc/idd/*
%{_libdir}/*/etc/message/*
%{_libdir}/*/etc/mine/*
%{_libdir}/*/etc/ms-kermit
%{_libdir}/*/etc/ms-kermit-7bit
%{_libdir}/*/etc/smilies/*
%{_libdir}/*/etc/sounds/*
%{_libdir}/*/etc/sparcworks/*
%{_libdir}/*/etc/spook.lines
%{_libdir}/*/etc/time/*
%{_libdir}/*/etc/toolbar/*
%{_libdir}/*/etc/xemacs-fe.sh
%{_libdir}/*/etc/yow.lines
%{_libdir}/*/lisp/*.el
%{_libdir}/*/lisp/apel/*.el
%{_libdir}/*/lisp/apel/*.elc
%{_libdir}/*/lisp/calendar/*.elc
%{_libdir}/*/lisp/cc-mode/*.elc
%{_libdir}/*/lisp/comint/*.elc
%{_libdir}/*/lisp/custom/*.elc
%{_libdir}/*/lisp/ediff/*.elc
%{_libdir}/*/lisp/ediff/Makefile
%{_libdir}/*/lisp/efs/*.el
%{_libdir}/*/lisp/efs/*.elc
%{_libdir}/*/lisp/efs/Makefile
%{_libdir}/*/lisp/electric/*.elc
%{_libdir}/*/lisp/eos/*.el
%{_libdir}/*/lisp/eos/*.elc
%{_libdir}/*/lisp/eos/Makefile
%{_libdir}/*/lisp/eterm/*.elc
%{_libdir}/*/lisp/games/*.elc
%{_libdir}/*/lisp/iso/*.elc
%{_libdir}/*/lisp/mel/*.elc
%{_libdir}/*/lisp/mu/*.el
%{_libdir}/*/lisp/mu/*.elc
%{_libdir}/*/lisp/packages/*.elc
%{_libdir}/*/lisp/prim/*.el
%{_libdir}/*/lisp/prim/*.elc
%{_libdir}/*/lisp/sunpro/*.elc
%{_libdir}/*/lisp/term/*.elc
%{_libdir}/*/lisp/tl/*.el
%{_libdir}/*/lisp/tl/*.elc
%{_libdir}/*/lisp/tooltalk/*.elc
%{_libdir}/*/lisp/tooltalk/Makefile
%{_libdir}/*/lisp/utils/*.elc
%{_libdir}/*/lisp/utils/forms-d2.dat
%{_libdir}/*/lisp/vc/*.elc
%{_libdir}/*/lisp/x11/*.elc
/usr/X11R6/lib/X11/ja/app-defaults/Emacs
/usr/X11R6/lib/X11/app-defaults/Emacs
/var/lock/xemacs

%files el 
%defattr(644,root,root,755)
%{_libdir}/*/lisp/apel/*.el.gz
%{_libdir}/*/lisp/calendar/*.el.gz
%{_libdir}/*/lisp/cc-mode/*.el.gz
%{_libdir}/*/lisp/comint/*.el.gz
%{_libdir}/*/lisp/custom/*.el.gz
%{_libdir}/*/lisp/ediff/*.el.gz
%{_libdir}/*/lisp/efs/*.el.gz
%{_libdir}/*/lisp/electric/*.el.gz
%{_libdir}/*/lisp/eos/*.el.gz
%{_libdir}/*/lisp/eterm/*.el.gz
%{_libdir}/*/lisp/games/*.el.gz
%{_libdir}/*/lisp/iso/*.el.gz
%{_libdir}/*/lisp/mel/*.el.gz
%{_libdir}/*/lisp/mu/*.el.gz
%{_libdir}/*/lisp/packages/*.el.gz
%{_libdir}/*/lisp/prim/*.el.gz
%{_libdir}/*/lisp/sunpro/*.el.gz
%{_libdir}/*/lisp/term/*.el.gz
%{_libdir}/*/lisp/tl/*.el.gz
%{_libdir}/*/lisp/tooltalk/*.el.gz
%{_libdir}/*/lisp/utils/*.el.gz
%{_libdir}/*/lisp/vc/*.el.gz
%{_libdir}/*/lisp/x11/*.el.gz

%files emulators 
%defattr(644,root,root,755)
%{_libdir}/*/lisp/emulators/*.elc
%{_libdir}/*/lisp/emulators/tpu-edt.xmodmap

%files gnats
%defattr(644,root,root,755)
%{_infodir}/gnats.info*gz
%{_libdir}/*/etc/gnats/*
%{_libdir}/*/lisp/gnats/*.elc
%{_libdir}/*/lisp/gnats/*.el.gz

%files emulators-el
%defattr(644,root,root,755)
%{_libdir}/*/lisp/emulators/*.el.gz

%files viper 
%defattr(644,root,root,755)
%doc %{_libdir}/*/etc/viperCard.tex
%{_infodir}/viper.info*gz
%{_libdir}/*/lisp/viper/*.elc
%doc %{_libdir}/*/lisp/viper/README

%files viper-el
%defattr(644,root,root,755)
%{_libdir}/*/lisp/viper/*.el.gz
%{_libdir}/*/lisp/viper/Makefile

%files lisp-programming
%defattr(644,root,root,755)
%{_infodir}/cl.info*gz
%{_infodir}/ilisp.info*gz
%{_infodir}/lispref.info*gz
%doc %{_libdir}/*/lisp/edebug/README
%doc %{_libdir}/*/lisp/ilisp/ACKNOWLEDGMENTS
%doc %{_libdir}/*/lisp/ilisp/COPYING
%doc %{_libdir}/*/lisp/ilisp/GETTING-ILISP
%doc %{_libdir}/*/lisp/ilisp/HISTORY
#%doc %{_libdir}/*/lisp/ilisp/INSTALLATION
%doc %{_libdir}/*/lisp/ilisp/README
%doc %{_libdir}/*/lisp/ilisp/Welcome
%{_libdir}/*/lisp/bytecomp/*.elc
%{_libdir}/*/lisp/cl/*.elc
%{_libdir}/*/lisp/edebug/*.el
%{_libdir}/*/lisp/edebug/*.elc
%{_libdir}/*/lisp/edebug/Makefile
%{_libdir}/*/lisp/edebug/edebug-history
%{_libdir}/*/lisp/ilisp/*.el
%{_libdir}/*/lisp/ilisp/*.elc
%{_libdir}/*/lisp/ilisp/*.lisp
%{_libdir}/*/lisp/ilisp/ild.mail
%{_libdir}/*/lisp/ilisp/ilisp.emacs
%{_libdir}/*/lisp/ilisp/scheme2c.mail

%files lisp-programming-el
%defattr(644,root,root,755)
%{_libdir}/*/lisp/ilisp/*.el.gz
%{_libdir}/*/lisp/edebug/*.el.gz
%{_libdir}/*/lisp/bytecomp/*.el.gz
%{_libdir}/*/lisp/cl/*.el.gz
%{_libdir}/*/lisp/ilisp/Makefile

%files auctex
%defattr(644,root,root,755)
%{_infodir}/auctex.info*gz
%doc %{_libdir}/*/lisp/auctex/CHANGES
%doc %{_libdir}/*/lisp/auctex/ChangeLog
%doc %{_libdir}/*/lisp/auctex/README
%{_libdir}/*/etc/auctex/style/*.elc
%{_libdir}/*/lisp/auctex/*.el
%{_libdir}/*/lisp/auctex/*.elc
#%{_libdir}/*/lisp/auctex/INSTALLATION
%doc %{_libdir}/*/lisp/auctex/PROBLEMS

%files auctex-el
%defattr(644,root,root,755)
%{_libdir}/*/lisp/auctex/Makefile
%{_libdir}/*/lisp/auctex/*.el.gz
%{_libdir}/*/etc/auctex/style/*.el.gz

%files w3 
%defattr(644,root,root,755)
%{_infodir}/w3-faq.info*gz
%{_infodir}/w3.info*gz
%{_libdir}/*/lisp/w3/*.el
%{_libdir}/*/lisp/w3/*.elc
%doc %{_libdir}/*/lisp/w3/ChangeLog
%{_libdir}/*/lisp/w3/descrip.mms
%{_libdir}/*/etc/w3/*

%files w3-el
%defattr(644,root,root,755)
%{_libdir}/*/lisp/w3/*.el.gz
%{_libdir}/*/lisp/w3/Makefile

%files psgml 
%defattr(644,root,root,755)
%{_infodir}/hm--html-mode.info*gz
%{_infodir}/psgml-api.info*gz
%{_infodir}/psgml.info*gz
%doc %{_libdir}/*/lisp/hm--html-menus/ANNOUNCEMENT
%doc %{_libdir}/*/lisp/hm--html-menus/NEWS
%doc %{_libdir}/*/lisp/hm--html-menus/README
%doc %{_libdir}/*/lisp/psgml/ChangeLog
%doc %{_libdir}/*/lisp/psgml/README.psgml
%{_libdir}/*/etc/sgml/*
%{_libdir}/*/lisp/hm--html-menus/*.elc
%{_libdir}/*/lisp/hm--html-menus/command-description.html.tmpl
%{_libdir}/*/lisp/hm--html-menus/frame.html.tmpl
%{_libdir}/*/lisp/hm--html-menus/templates.doc
%{_libdir}/*/lisp/psgml/*.elc
%{_libdir}/*/lisp/psgml/psgml-style.fs

%files psgml-el
%defattr(644,root,root,755)
%{_libdir}/*/lisp/psgml/*.el.gz
%{_libdir}/*/lisp/hm--html-menus/*.el.gz

%files modes 
%defattr(644,root,root,755)
%{_infodir}/pcl-cvs.info*gz
%doc %{_libdir}/*/lisp/pcl-cvs/ChangeLog
%doc %{_libdir}/*/lisp/pcl-cvs/README
%{_libdir}/*/lisp/modes/*.elc
%{_libdir}/*/lisp/pcl-cvs/*.elc
#%{_libdir}/*/lisp/pcl-cvs/INSTALL
%doc %{_libdir}/*/lisp/pcl-cvs/NEWS

%files modes-el
%defattr(644,root,root,755)
%{_libdir}/*/lisp/pcl-cvs/*.el.gz
%{_libdir}/*/lisp/modes/*.el.gz

%files extras
%attr(755,root,root) %{_bindir}/b2m
%attr(755,root,root) %{_bindir}/rcs-checkin

%files mail
%defattr(644,root,root,755)
%doc %{_libdir}/*/etc/MH-E-NEWS
%{_infodir}/mailcrypt.info*gz
%{_infodir}/mh-e.info*gz
%{_infodir}/rmail.info*gz
%{_infodir}/supercite.info*gz
%{_infodir}/tm-edit-en.info*gz
%{_infodir}/tm-en.info*gz
%{_infodir}/tm-mh-e-en.info*gz
%{_infodir}/tm-view-en.info*gz
%{_infodir}/tm-vm-en.info*gz
%{_infodir}/vm.info*gz
%doc %{_libdir}/*/lisp/mailcrypt/ChangeLog
%doc %{_libdir}/*/lisp/mailcrypt/NEWS
%doc %{_libdir}/*/lisp/mailcrypt/ONEWS
%doc %{_libdir}/*/lisp/mailcrypt/README
%doc %{_libdir}/*/lisp/rmail/README
%doc %{_libdir}/*/lisp/vm/README
%attr(755,root,root) %{_libdir}/*/%{buildarch}*/tm*
%{_libdir}/*/etc/vm/*
%{_libdir}/*/lisp/mailcrypt/*.elc
%{_libdir}/*/lisp/mh-e/*.elc
%{_libdir}/*/lisp/rmail/*.elc
%{_libdir}/*/lisp/tm/*.elc
%{_libdir}/*/lisp/vm/*.el
%{_libdir}/*/lisp/vm/*.elc
%{_libdir}/*/lisp/vm/.autoload
%{_libdir}/*/lisp/vm/Makefile
%{_libdir}/*/lisp/vm/make-autoloads

%files mail-el
%defattr(644,root,root,755)
%{_libdir}/*/lisp/tm/*.el.gz
%{_libdir}/*/lisp/vm/*.el.gz
%{_libdir}/*/lisp/mh-e/*.el.gz
%{_libdir}/*/lisp/mailcrypt/*.el.gz
%{_libdir}/*/lisp/rmail/*.el.gz

%files gnus
%defattr(644,root,root,755)
%{_libdir}/*/lisp/gnus/*.elc
%doc %{_libdir}/*/etc/gnusrefcard/*
%doc %{_infodir}/gnus-mime-en.info*gz
%doc %{_infodir}/gnus.info*gz

%files gnus-el
%defattr(644,root,root,755)
%{_libdir}/*/lisp/gnus/*.el.gz
%{_libdir}/*/lisp/gnus/Makefile

%changelog
* Sat Dec 19 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [20.4-8]
- removed {un}registering info.info.gz,
- many modyfications in %description and Summary,
- changed --with-gpm to yes.

* Thu Dec 10 1998 Ziemek Borowski <ziembor@faq-bot.ziembor.waw.pl>
- added --with-xpm and --with-png=yes for ./configure parameters,
- replaced mailnews subpackage by two separated mail and gnus,
- added directory /usr/lib/xemacs/site-lisp (for local xemacs macros)

* Fri Dec  6 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [20.4-7]
- added gziping man pages,
- fixed %files gnats (missing %defattr),
- removed termcap.info* files,
- removed /usr/lib/xemacs-20.4/etc/XKeysymDB,
- removed /usr/lib/xemacs-20.4/etc/tests
- added full url to Source{0,1},
- all info pages moved to %{_infodir}/,
- /usr/lib/xemacs-20.4/etc/xemacs-ja.1.gz
- added Group(pl),
- simplifications in all %files,
- added /var/lock/xemacs direcrory to main.

* Fri Sep 14 1998 Ziemek Borowski <ziembor@faq-bot.ziembor.waw.pl> 
  [20.4-5]
- added pl translation
- based on xemacs-20.4.spec by Henrik Seidel
  <seidel@mpimg-berlin-dahlem.mpg.de> and xemacs-20.4-3.spec
  by Stig Bjorlykke <stigb@tihlde.hist.no>
- moved file list into spec (for Polish Linux Distribution standards) 
- moved %changelog to end of file 
- %defattr instead %attr (in most cases)
- removed file list script 
- new split to subpackages: 
 + xemacs-auctex
 + xemacs-auctex-el
 + xemacs-el
 + xemacs-emulators
 + xemacs-emulators-el
 + xemacs-extras
 + xemacs-info
 + xemacs-lisp-programming
 + xemacs-lisp-programming-el
 + xemacs-mailnews
 + xemacs-mailnews-el
 + xemacs-modes
 + xemacs-modes-el
 + xemacs-psgml
 + xemacs-psgml-el
 + xemacs-viper
 + xemacs-viper-el
 + xemacs-w3
 + xemacs-w3-el

* Fri Aug 21 1998 Henrik Seidel <seidel@mpimg-berlin-dahlem.mpg.de>
  [20.4-4]
- from redhat-contrib 
- some of the *.el files are not compiled and therefore the
  corresponding *.elc files are missing in the base RPM. Now all those
  *.el files are included in the base RPM in an uncompressed format. All
  *.el files that have a compiled elc file are in a compressed format in
  xemacs-el.
- Gzipped all info-files.

* Tue Aug 18 1998 Henrik Seidel <seidel@mpimg-berlin-dahlem.mpg.de> 
- in 20.4-2 there was a bug in the SPEC file - I did not compress the
  *.el files. As a consequence, the *.el files were contained in the
  base xemacs RPM, and xemacs-el was empty.

* Tue Aug 04 1998 Henrik Seidel <seidel@mpimg-berlin-dahlem.mpg.de> 
- the 20.4-1 package was linked against 'libpng.so.0', and the libpng
  that comes with redhat 5.1 is 'libpng.so.2'. Furthermore, the SPEC
  contained the 'Description:' tag that is no longer valid.

* Sun May 31 1998 Stig Bjorlykke <stigb@tihlde.hist.no>
  [20.4-3] 
- from ftp.xemacs.org and mirrors
- Fixed some small errors, should now build on RedHat 5.1.

* Wed Mar 4 1998 Stig Bjorlykke <stigb@tihlde.hist.no>
- Build for alpha.
- Initially by Stig Bjørlykke <stigb@tihlde.hist.no> for i386 
  and modified for sparc by Frederic Poncin <fp@info.ucl.ac.be>
  Then modified for alpha by stigb.
