Summary:	The XEmacs editor
Summary(pl):	XEmacs -- Edytor
Name:		xemacs
version:	20.4
Release:	8
Copyright:	GPL
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Source0:	ftp://ftp.xemacs.org/pub/xemacs/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.xemacs.org/pub/xemacs/%{name}-%{version}/%{name}-%{version}-info.tar.gz
Source4:	xemacs.wmconfig
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
chmod u+wXr * -R
%setup -q -T -D -b 1 -n xemacs-%{version}
chmod u+wXr * -R
%patch0 -p1
chmod u+wXr * -R
%patch1 -p0

%ifarch alpha
%patch2 -p1
%endif

%build

# Delete the originals for the patched files
find . -name "*.orig" -exec rm {} \;

CFLAGS="$RPM_OPT_FLAGS" CPPFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{buildarch}-unknown-`echo %{buildos} | tr A-Z a-z` \
	--prefix=/usr \
	--infodir=/usr/info \
	--with-dialogs=athena \
	--with-sound=nas \
	--cflags="$RPM_OPT_FLAGS" \
	--error-checking=none \
	--debug=no \
	--with-xpm \
	--lockdir=/var/lock/xemacs \
	--with-session=yes \
	--with-gpm=yes \
	--with-png=yes
make dist

# xemacs generation
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/X11/wmconfig,var/lock/xemacs} \
	$RPM_BUILD_ROOT/usr/{man/{ja/man1,man1},X11R6/lib/X11/{ja/app-defaults,app-defaults}}

make install-arch-dep install-arch-indep gzip-el \
	prefix=$RPM_BUILD_ROOT/usr \
	infodir=$RPM_BUILD_ROOT/usr/info

gzip -9nf $RPM_BUILD_ROOT/usr/info/*info*
find $RPM_BUILD_ROOT/usr/lib/%{name}-%{version}/etc/auctex/style/ -name \*.el | xargs gzip -9

cp $RPM_SOURCE_DIR/xemacs.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/xemacs

find $RPM_BUILD_ROOT/usr/bin -type f |xargs  file |grep stripped|  awk -F: '{print $1}' | xargs strip 
find $RPM_BUILD_ROOT/usr/lib/*/* -type f |xargs  file |grep stripped|  awk -F: '{print $1}' | xargs strip 

mv $RPM_BUILD_ROOT/usr/lib/%{name}-%{version}/etc/Emacs.ad \
	$RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults/Emacs
mv $RPM_BUILD_ROOT/usr/lib/%{name}-%{version}/etc/app-defaults/ja/Emacs \
	$RPM_BUILD_ROOT/usr/X11R6/lib/X11/ja/app-defaults/Emacs
mv $RPM_BUILD_ROOT/usr/lib/%{name}-%{version}/etc/xemacs-ja.1 \
	$RPM_BUILD_ROOT/usr/man/ja/man1/xemacs.1

mv -f $RPM_BUILD_ROOT/usr/bin/xemacs-%{version} \
	$RPM_BUILD_ROOT/usr/bin/xemacs

gzip -9nf $RPM_BUILD_ROOT/usr/man/{ja/man1/*,man1/*}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info /usr/info/cc-mode.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* CC mode: (ccmode).    The GNU Emacs mode for editing C, C++, Objective-C and Java code."
/sbin/install-info /usr/info/cl.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* CL: (cl).             Partial Common Lisp support for Emacs Lisp."
/sbin/install-info /usr/info/forms.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* Forms: (forms).       Emacs package for editing data bases by filling in forms."
/sbin/install-info /usr/info/xemacs.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* Emacs: (emacs).       The extensible self-documenting text editor."
/sbin/install-info /usr/info/ilisp.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* ilisp: (ilisp).       ILISP manual"
/sbin/install-info /usr/info/lispref.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* lispref: (lispref).   GNU Emacs Lisp Reference Manual"
/sbin/install-info /usr/info/custom.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* custom: (custom).     The Customization Library"
/sbin/install-info /usr/info/efs.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* efs: (efs).           Transparent remote file access via FTP"
/sbin/install-info /usr/info/external-widget.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* external-widget: (external-widget).External Client Widget"
/sbin/install-info /usr/info/internals.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* internals: (internals).internals"
/sbin/install-info /usr/info/new-users-guide.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* new-users-guide: (new-users-guide). introduction to the XEmacs editor"
/sbin/install-info /usr/info/ph.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* ph: (ph).             E-Lisp client interface to the CCSO white pages directory system also known as PH/QI"
/sbin/install-info /usr/info/send-pr.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* send-pr: (send-pr).   Reporting problems--using send-pr"
/sbin/install-info /usr/info/term.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* term: (term).         Terminal emulator mode"
/sbin/install-info /usr/info/vhdl-mode.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* vhdl-mode: (vhdl-mode). vhdl-mode"
/sbin/install-info /usr/info/widget.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* widget: (widget).     The Emacs Widget Library"
/sbin/install-info /usr/info/xemacs-faq.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* xemacs-faq: (xemacs-faq). The Xemacs FAQ"

%preun
if [ "$1" = 0 ]; then
	/sbin/install-info --delete /usr/info/cc-mode.info.gz /etc/info-dir
	/sbin/install-info --delete /usr/info/cl.info.gz /etc/info-dir
	/sbin/install-info --delete /usr/info/forms.info.gz /etc/info-dir
	/sbin/install-info --delete /usr/info/xemacs.info.gz /etc/info-dir
	/sbin/install-info --delete /usr/info/ilisp.info.gz /etc/info-dir
	/sbin/install-info --delete /usr/info/lispref.info.gz /etc/info-dir
	/sbin/install-info --delete /usr/info/pcl-cvs.info.gz /etc/info-dir
	/sbin/install-info --delete /usr/info/custom.info.gz /etc/info-dir
	/sbin/install-info --delete /usr/info/efs.info.gz /etc/info-dir
	/sbin/install-info --delete /usr/info/external-widget.info.gz /etc/info-dir
	/sbin/install-info --delete /usr/info/internals.info.gz /etc/info-dir
	/sbin/install-info --delete /usr/info/new-users-guide.info.gz /etc/info-dir
	/sbin/install-info --delete /usr/info/ph.info.gz /etc/info-dir
	/sbin/install-info --delete /usr/info/send-pr.info.gz /etc/info-dir
	/sbin/install-info --delete /usr/info/term.info.gz /etc/info-dir
	/sbin/install-info --delete /usr/info/vhdl-mode.info.gz /etc/info-dir
	/sbin/install-info --delete /usr/info/widget.info.gz /etc/info-dir
	/sbin/install-info --delete /usr/info/xemacs-faq.info.gz /etc/info-dir
fi

%post gnats
/sbin/install-info /usr/info/gnats.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* gnats: (gnats).       GNU Problem Report Management System"

%preun gnats
if [ "$1" = $1 ]; then
	/sbin/install-info --delete /usr/info/gnats.info.gz /etc/info-dir
fi

%post viper
/sbin/install-info /usr/info/viper.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* VIPER: (viper).       The new VI-emulation mode in Emacs-19.29."

%preun viper
if [ "$1" = $1 ]; then
	/sbin/install-info --delete /usr/info/viper.info.gz /etc/info-dir
fi

%post auctex
/sbin/install-info /usr/info/auctex.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* auctex: (auctex).     TeX mode"
/sbin/install-info /usr/info/reftex.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* reftex: (reftex).     RefTeX, a package to do labels, references and citations for LaTeX documents with Emacs"

%preun auctex
if [ "$1" = $1 ]; then
	/sbin/install-info --delete /usr/info/auctex.info.gz /etc/info-dir
	/sbin/install-info --delete /usr/info/reftex.info.gz /etc/info-dir
fi


%post w3
/sbin/install-info /usr/info/w3-faq.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* w3-faq: (w3-faq).     FAQ for Emacs/W3 World Wide Web browser"
/sbin/install-info /usr/info/w3.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* w3: (w3).             Emacs/W3 World Wide Web browser"

%preun w3
if [ "$1" = $1 ]; then
	/sbin/install-info --delete /usr/info/w3-faq.info.gz /etc/info-dir
	/sbin/install-info --delete /usr/info/w3.info.gz /etc/info-dir
fi

%preun modes
if [ "$1" = $1 ]; then
	/sbin/install-info /usr/info/pcl-cvs.info.gz /etc/info-dir
fi

%post modes
/sbin/install-info /usr/info/pcl-cvs.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* pcl-cvs: (pcl-cvs).   front-end to CVS"

%post psgml
/sbin/install-info /usr/info/psgml-api.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* psgml-api: (psgml-api). PSGML, the API documentation"
/sbin/install-info /usr/info/psgml.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* psgml: (psgml).       PSGML, a major mode for SGML"
/sbin/install-info /usr/info/hm--html-mode.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* hm--html-mode-xemacs: (hm--html-mode). hm--html-menus"

%preun psgml
if [ "$1" = $1 ]; then
	/sbin/install-info --delete /usr/info/psgml-api.info.gz /etc/info-dir
	/sbin/install-info --delete /usr/info/psgml.info.gz /etc/info-dir
	/sbin/install-info --delete /usr/info/hm--html-mode.info.gz /etc/info-dir
fi

%post mail 
/sbin/install-info /usr/info/mh-e.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* MH-E: (mh-e).         Emacs interface to the MH mail system."
/sbin/install-info /usr/info/supercite.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* SC: (sc).             Supercite lets you cite parts of messages you're replying to, in flexible ways."
/sbin/install-info /usr/info/rmail.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* rmail: (rmail).       Rmail mail reader"
/sbin/install-info /usr/info/tm-edit-en.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* tm-en: (tm-en).       tm-edit 7.100 Reference Manual"
/sbin/install-info /usr/info/tm-mh-e-en.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* tm-mh-e-en: (tm-mh-e-en). tm-mh-e 7.71 Reference Manual"
/sbin/install-info /usr/info/tm-view-en.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* tm-view-en: (tm-view-en). tm-view, a MIME Viewer for GNU Emacs"
/sbin/install-info /usr/info/tm-vm-en.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* tm-vm-en: (tm-vm-en). tm-vm is an interface between tm and the VM mail user agent"
/sbin/install-info /usr/info/vm.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* vm: (vm).             VM mail reader"

%preun mail 
if [ "$1" = $1 ]; then
	/sbin/install-info --delete /usr/info/mh-e.info.gz /etc/info-dir
	/sbin/install-info --delete /usr/info/supercite.info.gz /etc/info-dir
	/sbin/install-info --delete /usr/info/rmail.info.gz /etc/info-dir
	/sbin/install-info --delete /usr/info/tm-edit-en.info.gz /etc/info-dir
	/sbin/install-info --delete /usr/info/tm-mh-e-en.info.gz /etc/info-dir
	/sbin/install-info --delete /usr/info/tm-view-en.info.gz /etc/info-dir
	/sbin/install-info --delete /usr/info/tm-vm-en.info.gz /etc/info-dir
	/sbin/install-info --delete /usr/info/vm.info.gz /etc/info-dir
fi

%post gnus 
/sbin/install-info /usr/info/message.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* Message: (message).   Mail and news composition mode that goes with Gnus."
/sbin/install-info /usr/info/gnus.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* Gnus: (gnus).         The news reader Gnus."
/sbin/install-info /usr/info/gnus-mime-en.info.gz /etc/info-dir \
	--section "XEmacs:" --entry \
	"* gnus-mime-en: (gnus-mime-en) gnus-mime 0.10 reference manual"

%preun gnus 
if [ "$1" = $1 ]; then
	/sbin/install-info --delete /usr/info/message.info.gz /etc/info-dir
	/sbin/install-info --delete /usr/info/gnus.info.gz /etc/info-dir
	/sbin/install-info --delete /usr/info/gnus-mime-en.info.gz
fi

%files
%defattr(644, root, root, 755)
%config /etc/X11/wmconfig/xemacs
%attr(2755, root, mail) /usr/lib/*/*/movemail
%attr(755, root, root) /usr/bin/xemacs
%attr(755, root, root) /usr/bin/gnuclient
%attr(755, root, root) /usr/lib/*/*/cvtmail
%attr(755, root, root) /usr/lib/*/*/digest-doc
%attr(755, root, root) /usr/lib/*/*/fakemail
%attr(755, root, root) /usr/lib/*/*/gnuserv
%attr(755, root, root) /usr/lib/*/*/hexl
%attr(755, root, root) /usr/lib/*/*/make-docfile
%attr(755, root, root) /usr/lib/*/*/make-path
%attr(755, root, root) /usr/lib/*/*/mmencode
%attr(755, root, root) /usr/lib/*/*/profile
%attr(755, root, root) /usr/lib/*/*/sorted-doc
%attr(755, root, root) /usr/lib/*/*/yow
%attr(755, root, root) /usr/bin/gnuattach
%attr(755, root, root) /usr/bin/gnudoit
%attr(755, root, root) /usr/bin/install-sid
%attr(755, root, root) /usr/bin/pstogif
%attr(755, root, root) /usr/bin/send-pr
%attr(755, root, root) /usr/lib/*/*/add-big-package.sh
%attr(755, root, root) /usr/lib/*/*/add-little-package.sh
%attr(755, root, root) /usr/lib/*/*/gzip-el.sh
%attr(755, root, root) /usr/lib/*/*/install-sid
%attr(755, root, root) /usr/lib/*/*/rcs2log
%attr(755, root, root) /usr/lib/*/*/send-pr
%attr(755, root, root) /usr/lib/*/*/vcdiff
%attr(755, root, root) /usr/lib/*/*/wakeup
%doc %lang(de) /usr/lib/*/etc/TUTORIAL.de
%doc %lang(fr) /usr/lib/*/etc/TUTORIAL.fr
%doc %lang(hr) /usr/lib/*/etc/TUTORIAL.hr
%doc %lang(ja) /usr/lib/*/etc/TUTORIAL.ja
%doc %lang(ko) /usr/lib/*/etc/TUTORIAL.ko
%doc %lang(no) /usr/lib/*/etc/TUTORIAL.no
%doc %lang(pl) /usr/lib/*/etc/TUTORIAL.pl
%doc %lang(th) /usr/lib/*/etc/TUTORIAL.th
%doc /usr/lib/*/*/DOC
%doc /usr/lib/*/etc/*.doc
%doc /usr/lib/*/etc/README.HYPERBOLE
%doc /usr/lib/*/etc/README.OO-BROWSER
%doc /usr/lib/*/etc/e/README
%doc /usr/lib/*/etc/gnuserv.README
%doc /usr/lib/*/etc/hypb-mouse.txt
%doc /usr/lib/*/etc/refcard.ps
%doc /usr/lib/*/etc/refcard.tex
%doc /usr/lib/*/etc/refcard3.ps
%doc /usr/lib/*/etc/sample.Xdefaults
%doc /usr/lib/*/etc/sample.emacs
%doc /usr/lib/*/lisp/ChangeLog
%doc /usr/lib/*/lisp/README
%doc /usr/lib/*/lisp/apel/ChangeLog*
%doc /usr/lib/*/lisp/ediff/README
%doc /usr/lib/*/lisp/efs/README
%doc /usr/lib/*/lisp/eterm/ChangeLog
%doc /usr/lib/*/lisp/eterm/QUESTIONS
%doc /usr/lib/*/lisp/eterm/README.term
%doc /usr/lib/*/lisp/eterm/TODO.term
%doc /usr/lib/*/lisp/mel/ChangeLog
%doc /usr/lib/*/lisp/term/README
%attr(644, root, man) /usr/man/man1/gnuattach.1.gz
%attr(644, root, man) /usr/man/man1/gnuclient.1.gz
%attr(644, root, man) /usr/man/man1/gnudoit.1.gz
%attr(644, root, man) /usr/man/man1/gnuserv.1.gz
%attr(644, root, man) /usr/man/man1/xemacs.1.gz
%attr(644, root, man) %lang(ja) /usr/man/ja/man1/xemacs.1.gz
%doc README GETTING.GNU.SOFTWARE PROBLEMS 
%doc etc/NEWS etc/MAILINGLISTS BUGS 
/usr/lib/*/*/config.values
/usr/lib/*/etc/*.xbm
/usr/info/cc-mode.info*gz
/usr/info/custom.info*gz
/usr/info/efs.info*gz
/usr/info/external-widget.info*gz
/usr/info/forms.info*gz
/usr/info/internals.info*gz
/usr/info/message.info*gz
/usr/info/new-users-guide.info*gz
/usr/info/ph.info*gz
/usr/info/reftex.info*gz
/usr/info/send-pr.info*gz
/usr/info/term.info*gz
/usr/info/vhdl-mode.info*gz
/usr/info/widget.info*gz
/usr/info/xemacs-faq.info*gz
/usr/info/xemacs.info*gz
/usr/lib/*/etc/*.xpm
/usr/lib/*/etc/*.xpm.Z
/usr/lib/*/etc/categories
/usr/lib/*/etc/cbx.gif
/usr/lib/*/etc/custom/*
/usr/lib/*/etc/eos/*
/usr/lib/*/etc/frame-icon/*
/usr/lib/*/etc/idd/*
/usr/lib/*/etc/message/*
/usr/lib/*/etc/mine/*
/usr/lib/*/etc/ms-kermit
/usr/lib/*/etc/ms-kermit-7bit
/usr/lib/*/etc/smilies/*
/usr/lib/*/etc/sounds/*
/usr/lib/*/etc/sparcworks/*
/usr/lib/*/etc/spook.lines
/usr/lib/*/etc/time/*
/usr/lib/*/etc/toolbar/*
/usr/lib/*/etc/xemacs-fe.sh
/usr/lib/*/etc/yow.lines
/usr/lib/*/lisp/*.el
/usr/lib/*/lisp/apel/*.el
/usr/lib/*/lisp/apel/*.elc
/usr/lib/*/lisp/calendar/*.elc
/usr/lib/*/lisp/cc-mode/*.elc
/usr/lib/*/lisp/comint/*.elc
/usr/lib/*/lisp/custom/*.elc
/usr/lib/*/lisp/ediff/*.elc
/usr/lib/*/lisp/ediff/Makefile
/usr/lib/*/lisp/efs/*.el
/usr/lib/*/lisp/efs/*.elc
/usr/lib/*/lisp/efs/Makefile
/usr/lib/*/lisp/electric/*.elc
/usr/lib/*/lisp/eos/*.el
/usr/lib/*/lisp/eos/*.elc
/usr/lib/*/lisp/eos/Makefile
/usr/lib/*/lisp/eterm/*.elc
/usr/lib/*/lisp/games/*.elc
/usr/lib/*/lisp/iso/*.elc
/usr/lib/*/lisp/mel/*.elc
/usr/lib/*/lisp/mu/*.el
/usr/lib/*/lisp/mu/*.elc
/usr/lib/*/lisp/packages/*.elc
/usr/lib/*/lisp/prim/*.el
/usr/lib/*/lisp/prim/*.elc
/usr/lib/*/lisp/sunpro/*.elc
/usr/lib/*/lisp/term/*.elc
/usr/lib/*/lisp/tl/*.el
/usr/lib/*/lisp/tl/*.elc
/usr/lib/*/lisp/tooltalk/*.elc
/usr/lib/*/lisp/tooltalk/Makefile
/usr/lib/*/lisp/utils/*.elc
/usr/lib/*/lisp/utils/forms-d2.dat
/usr/lib/*/lisp/vc/*.elc
/usr/lib/*/lisp/x11/*.elc
/usr/X11R6/lib/X11/ja/app-defaults/Emacs
/usr/X11R6/lib/X11/app-defaults/Emacs
/var/lock/xemacs

%files el 
%defattr(644, root, root, 755)
/usr/lib/*/lisp/apel/*.el.gz
/usr/lib/*/lisp/calendar/*.el.gz
/usr/lib/*/lisp/cc-mode/*.el.gz
/usr/lib/*/lisp/comint/*.el.gz
/usr/lib/*/lisp/custom/*.el.gz
/usr/lib/*/lisp/ediff/*.el.gz
/usr/lib/*/lisp/efs/*.el.gz
/usr/lib/*/lisp/electric/*.el.gz
/usr/lib/*/lisp/eos/*.el.gz
/usr/lib/*/lisp/eterm/*.el.gz
/usr/lib/*/lisp/games/*.el.gz
/usr/lib/*/lisp/iso/*.el.gz
/usr/lib/*/lisp/mel/*.el.gz
/usr/lib/*/lisp/mu/*.el.gz
/usr/lib/*/lisp/packages/*.el.gz
/usr/lib/*/lisp/prim/*.el.gz
/usr/lib/*/lisp/sunpro/*.el.gz
/usr/lib/*/lisp/term/*.el.gz
/usr/lib/*/lisp/tl/*.el.gz
/usr/lib/*/lisp/tooltalk/*.el.gz
/usr/lib/*/lisp/utils/*.el.gz
/usr/lib/*/lisp/vc/*.el.gz
/usr/lib/*/lisp/x11/*.el.gz

%files emulators 
%defattr(644, root, root, 755)
/usr/lib/*/lisp/emulators/*.elc
/usr/lib/*/lisp/emulators/tpu-edt.xmodmap

%files gnats
%defattr(644, root, root, 755)
/usr/info/gnats.info*gz
/usr/lib/*/etc/gnats/*
/usr/lib/*/lisp/gnats/*.elc
/usr/lib/*/lisp/gnats/*.el.gz

%files emulators-el
%defattr(644, root, root, 755)
/usr/lib/*/lisp/emulators/*.el.gz

%files viper 
%defattr(644, root, root, 755)
%doc /usr/lib/*/etc/viperCard.tex
/usr/info/viper.info*gz
/usr/lib/*/lisp/viper/*.elc
%doc /usr/lib/*/lisp/viper/README

%files viper-el
%defattr(644, root, root, 755)
/usr/lib/*/lisp/viper/*.el.gz
/usr/lib/*/lisp/viper/Makefile

%files lisp-programming
%defattr(644, root, root, 755)
/usr/info/cl.info*gz
/usr/info/ilisp.info*gz
/usr/info/lispref.info*gz
%doc /usr/lib/*/lisp/edebug/README
%doc /usr/lib/*/lisp/ilisp/ACKNOWLEDGMENTS
%doc /usr/lib/*/lisp/ilisp/COPYING
%doc /usr/lib/*/lisp/ilisp/GETTING-ILISP
%doc /usr/lib/*/lisp/ilisp/HISTORY
#%doc /usr/lib/*/lisp/ilisp/INSTALLATION
%doc /usr/lib/*/lisp/ilisp/README
%doc /usr/lib/*/lisp/ilisp/Welcome
/usr/lib/*/lisp/bytecomp/*.elc
/usr/lib/*/lisp/cl/*.elc
/usr/lib/*/lisp/edebug/*.el
/usr/lib/*/lisp/edebug/*.elc
/usr/lib/*/lisp/edebug/Makefile
/usr/lib/*/lisp/edebug/edebug-history
/usr/lib/*/lisp/ilisp/*.el
/usr/lib/*/lisp/ilisp/*.elc
/usr/lib/*/lisp/ilisp/*.lisp
/usr/lib/*/lisp/ilisp/ild.mail
/usr/lib/*/lisp/ilisp/ilisp.emacs
/usr/lib/*/lisp/ilisp/scheme2c.mail

%files lisp-programming-el
%defattr(644, root, root, 755)
/usr/lib/*/lisp/ilisp/*.el.gz
/usr/lib/*/lisp/edebug/*.el.gz
/usr/lib/*/lisp/bytecomp/*.el.gz
/usr/lib/*/lisp/cl/*.el.gz
/usr/lib/*/lisp/ilisp/Makefile

%files auctex
%defattr(644, root, root, 755)
/usr/info/auctex.info*gz
%doc /usr/lib/*/lisp/auctex/CHANGES
%doc /usr/lib/*/lisp/auctex/ChangeLog
%doc /usr/lib/*/lisp/auctex/README
/usr/lib/*/etc/auctex/style/*.elc
/usr/lib/*/lisp/auctex/*.el
/usr/lib/*/lisp/auctex/*.elc
#/usr/lib/*/lisp/auctex/INSTALLATION
%doc /usr/lib/*/lisp/auctex/PROBLEMS

%files auctex-el
%defattr(644, root, root, 755)
/usr/lib/*/lisp/auctex/Makefile
/usr/lib/*/lisp/auctex/*.el.gz
/usr/lib/*/etc/auctex/style/*.el.gz

%files w3 
%defattr(644, root, root, 755)
/usr/info/w3-faq.info*gz
/usr/info/w3.info*gz
/usr/lib/*/lisp/w3/*.el
/usr/lib/*/lisp/w3/*.elc
%doc /usr/lib/*/lisp/w3/ChangeLog
/usr/lib/*/lisp/w3/descrip.mms
/usr/lib/*/etc/w3/*

%files w3-el
%defattr(644, root, root, 755)
/usr/lib/*/lisp/w3/*.el.gz
/usr/lib/*/lisp/w3/Makefile

%files psgml 
%defattr(644, root, root, 755)
/usr/info/hm--html-mode.info*gz
/usr/info/psgml-api.info*gz
/usr/info/psgml.info*gz
%doc /usr/lib/*/lisp/hm--html-menus/ANNOUNCEMENT
%doc /usr/lib/*/lisp/hm--html-menus/NEWS
%doc /usr/lib/*/lisp/hm--html-menus/README
%doc /usr/lib/*/lisp/psgml/ChangeLog
%doc /usr/lib/*/lisp/psgml/README.psgml
/usr/lib/*/etc/sgml/*
/usr/lib/*/lisp/hm--html-menus/*.elc
/usr/lib/*/lisp/hm--html-menus/command-description.html.tmpl
/usr/lib/*/lisp/hm--html-menus/frame.html.tmpl
/usr/lib/*/lisp/hm--html-menus/templates.doc
/usr/lib/*/lisp/psgml/*.elc
/usr/lib/*/lisp/psgml/psgml-style.fs

%files psgml-el
%defattr(644, root, root, 755)
/usr/lib/*/lisp/psgml/*.el.gz
/usr/lib/*/lisp/hm--html-menus/*.el.gz

%files modes 
%defattr(644, root, root, 755)
/usr/info/pcl-cvs.info*gz
%doc /usr/lib/*/lisp/pcl-cvs/ChangeLog
%doc /usr/lib/*/lisp/pcl-cvs/README
/usr/lib/*/lisp/modes/*.elc
/usr/lib/*/lisp/pcl-cvs/*.elc
#/usr/lib/*/lisp/pcl-cvs/INSTALL
%doc /usr/lib/*/lisp/pcl-cvs/NEWS

%files modes-el
%defattr(644, root, root, 755)
/usr/lib/*/lisp/pcl-cvs/*.el.gz
/usr/lib/*/lisp/modes/*.el.gz

%files extras
%attr(755, root, root) /usr/bin/b2m
%attr(755, root, root) /usr/bin/rcs-checkin

%files mail
%defattr(644, root, root, 755)
%doc /usr/lib/*/etc/MH-E-NEWS
/usr/info/mailcrypt.info*gz
/usr/info/mh-e.info*gz
/usr/info/rmail.info*gz
/usr/info/supercite.info*gz
/usr/info/tm-edit-en.info*gz
/usr/info/tm-en.info*gz
/usr/info/tm-mh-e-en.info*gz
/usr/info/tm-view-en.info*gz
/usr/info/tm-vm-en.info*gz
/usr/info/vm.info*gz
%doc /usr/lib/*/lisp/mailcrypt/ChangeLog
%doc /usr/lib/*/lisp/mailcrypt/NEWS
%doc /usr/lib/*/lisp/mailcrypt/ONEWS
%doc /usr/lib/*/lisp/mailcrypt/README
%doc /usr/lib/*/lisp/rmail/README
%doc /usr/lib/*/lisp/vm/README
%attr(755, root, root) /usr/lib/*/%{buildarch}*/tm*
/usr/lib/*/etc/vm/*
/usr/lib/*/lisp/mailcrypt/*.elc
/usr/lib/*/lisp/mh-e/*.elc
/usr/lib/*/lisp/rmail/*.elc
/usr/lib/*/lisp/tm/*.elc
/usr/lib/*/lisp/vm/*.el
/usr/lib/*/lisp/vm/*.elc
/usr/lib/*/lisp/vm/.autoload
/usr/lib/*/lisp/vm/Makefile
/usr/lib/*/lisp/vm/make-autoloads

%files mail-el
%defattr(644, root, root, 755)
/usr/lib/*/lisp/tm/*.el.gz
/usr/lib/*/lisp/vm/*.el.gz
/usr/lib/*/lisp/mh-e/*.el.gz
/usr/lib/*/lisp/mailcrypt/*.el.gz
/usr/lib/*/lisp/rmail/*.el.gz

%files gnus
%defattr(644, root, root, 755)
/usr/lib/*/lisp/gnus/*.elc
%doc /usr/lib/*/etc/gnusrefcard/*
%doc /usr/info/gnus-mime-en.info*gz
%doc /usr/info/gnus.info*gz

%files gnus-el
%defattr(644, root, root, 755)
/usr/lib/*/lisp/gnus/*.el.gz
/usr/lib/*/lisp/gnus/Makefile

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
- all info pages moved to /usr/info/,
- /usr/lib/xemacs-20.4/etc/xemacs-ja.1.gz moved to
  /usr/man/ja/man1/xemacs.1.gz
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
