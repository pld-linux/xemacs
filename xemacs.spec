Summary:	The XEmacs editor
Summary(pl):	XEmacs -- Edytor
Name:		xemacs
Version:	21.1.8
%define		ver		21.1
%define		basepkgver	1.32
Release:	5
Copyright:	GPL
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Source0:	ftp://ftp.xemacs.org/pub/xemacs/%{name}-%{ver}/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.xemacs.org/pub/xemacs/%{name}-%{ver}/%{name}-%{version}-elc.tar.gz
Source2:	ftp://ftp.xemacs.org/pub/xemacs/packages/xemacs-base-%{basepkgver}-pkg.tar.gz
Source3:	xemacs.desktop
Source4:	xemacs.ad-pl
Patch0:		xemacs-info.patch
Patch1:		xemacs-sitelisp.patch
Patch2:		xemacs-fix_ldflafs.patch
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
Prereq:		/usr/sbin/fix-info-dir
# BuildConflicts: xemacs 
# Yes! I need tu uninstall xemacs-21.1.8-4 to be able to build it!!!!!!!
# I don't understand it 
Buildroot:	/tmp/%{name}-%{version}-root
Provides:	xemacs-base-pkg

%define		_applnkdir	/usr/X11R6/share/applnk

%description
XEmacs is a version of Emacs, compatible with and containing many
improvements over GNU Emacs, written by Richard Stallman of the Free
Software Foundation. It was originally based on an early release of GNU
Emacs version 19, and has tracked subsequent releases of GNU Emacs as they
have become available.
This XEmacs distribution has been splitted in some rpm :

- xemacs:        the main part
- xemacs-extras: files in conflict with emacs

Install xemacs-extras if you do not have emacs installed.

%description -l pl 
XEmacs jest odmian± Emacsa, zgodn± (i zawieraj±c± wiele udogodnieñ) z 
GNU Emacsem tworzonym przez Richard Stallman z Free Software Foundation. 
Wywodzi siê z wczesnych odmian GNU Emacs 19, wprowadza wiele mi³ych 
ulepszeñ nie trac±c jednak wiêzi z oryginaln± wersj±. 

Ta dystrubucja XEmacsa zosta³± podzielona na wiele pakietów binarnych. 
Do pracy niezbêdne s± dwa z nich:

- xemacs:        g³ówny pakiet
- xemacs-extras: pliki wchodz±ce w sk³ad dystrybucji GNU Emacs

Zainstaluj xemacs-extras je¶li nie posiadasz GNU Emacsa. 

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

%package extras
Summary:	files which conflict with GNU Emacs
Summary(pl):	wspólne pliki XEmacsa i GNU Emacsa
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	%{name} = %{version}
Conflicts:	emacs

%description extras
These files are common between GNU Emacs and XEmacs. If you do not 
have GNU Emacs installed, be sure to install this package as well 
when you install XEmacs.

%description extras -l pl
S± to wpólne pliki GNU Emacs i XEmacs. Je¶li nie zainstalowa³e¶ GNU Emacsa,
to koniecznie zainstaluj ten pakiet.

%prep
%setup0 -q -b1 -a2
%patch0 -p1
%patch1 -p1
%patch2 -p1
chmod u+wXr * -R

%ifarch alpha
%patch1 -p1
%endif

%build
autoconf
CFLAGS="$RPM_OPT_FLAGS"
CPPFLAGS="$RPM_OPT_FLAGS"
LDFLAGS="-s -lc"
sitelispdir=%{_libdir}/%{name}/site-lisp
export CFLAGS CPPFLAGS LDFLAGS sitelispdir
./configure %{_target_platform} \
	--prefix=%{_prefix} \
	--infodir=%{_infodir} \
	--mandir=%{_mandir}/man1 \
	--datadir=%{_datadir} \
	--lockdir=/var/lock/xemacs/ \
	--package_path="~/.xemacs::%{_datadir}/%{name}-packages" \
	--with-sound=native \
	--with-x11 \
	--with-jpeg \
	--with-png \
	--without-tiff \
	--with-dialogs=athena \
	--with-database=no \
	--without-dnet \
	--without-ldap \
	--with-xpm \
	--with-ncurses \
	--without-ldap \
	--without-dragndrop \
	--with-site-lisp \
	--without-mule \


#	--lispdir=%{_datadir}/%{name}/lisp \
#	--pkgdir=%{_datadir}/%{name}/lisp \
#	--etcdir=%{_datadir}/%{name}/etc \
#	--cflags="$RPM_OPT_FLAGS" \
#	--error-checking=none \
#	--debug=no \
#	--with-session=yes \
#	--with-gpm=yes \
#	--with-png=yes \

#	--with-mule

sitelispdir=%{_libdir}/%{name}/site-lisp \
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Editors,/var/lock/xemacs} \
	$RPM_BUILD_ROOT{%{_mandir}/{ja/man1,man1},/usr/X11R6/lib/X11/app-defaults}

install -d $RPM_BUILD_ROOT/usr/X11R6/lib/X11/pl/app-defaults

make install-arch-dep install-arch-indep gzip-el \
	prefix=$RPM_BUILD_ROOT/usr \
	infodir=$RPM_BUILD_ROOT%{_infodir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}/man1 \
	datadir=$RPM_BUILD_ROOT%{_datadir} \

#	package_path=$RPM_BUILD_ROOT%{_datadir}/%{name} \
#	lispdir=$RPM_BUILD_ROOT%{_datadir}/%{name}/lisp \
#	pkgdir=$RPM_BUILD_ROOT%{_datadir}/%{name}/lisp \
#	sitelispdir=$RPM_BUILD_ROOT%{_datadir}/%{name}/site-lisp \
#	etcdir=$RPM_BUILD_ROOT%{_datadir}/%{name}/etc

install %{SOURCE3} $RPM_BUILD_ROOT%{_applnkdir}/Editors/xemacs.desktop
install %{SOURCE4} $RPM_BUILD_ROOT/usr/X11R6/lib/X11/pl/app-defaults/Emacs


install -d $RPM_BUILD_ROOT%{_datadir}/%{name}-packages
( cd $RPM_BUILD_ROOT%{_datadir}/%{name}-packages; gzip -dc %{SOURCE2} | tar xf - ; cd lisp/xemacs-base; gzip -9nf *.el)

install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/lisp
install -d $RPM_BUILD_ROOT%{_libdir}/%{name}
mv $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/%{_target_platform}/config.values $RPM_BUILD_ROOT%{_libdir}/%{name}

[ -d $RPM_BUILD_ROOT%{_datadir}/%{name}/site-lisp ] || \
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/site-lisp
ln -s %{_datadir}/%{name}/site-lisp $RPM_BUILD_ROOT%{_libdir}/%{name}/site-lisp

# mv $RPM_BUILD_ROOT%{_datadir}/%{name}/etc/app-defaults/Emacs \
#	$RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults/Emacs

mv $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/etc/xemacs-ja.1 \
	$RPM_BUILD_ROOT%{_mandir}/ja/man1/xemacs.1

mv -f $RPM_BUILD_ROOT%{_bindir}/xemacs-%{version} \
	$RPM_BUILD_ROOT%{_bindir}/xemacs

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/{man1/*,ja/man1/*} \
	$RPM_BUILD_ROOT%{_infodir}/*info*

find $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/* -type f -name "ChangeLog*" | xargs gzip -9nf

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1 

%postun
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1 


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
%doc %{_libdir}/%{name}-%{version}/*/DOC
%doc %{_datadir}/*/etc/*README*
%doc %{_datadir}/*/etc/refcard.ps.gz
%doc %{_datadir}/*/etc/refcard.tex
%doc %{_datadir}/*/etc/sample.Xdefaults
%doc %{_datadir}/*/etc/sample.emacs
%doc %{_datadir}/*/etc/aliases.ksh
%doc %{_datadir}/*/etc/editclient.sh
%doc %{_datadir}/*/lisp/ChangeLog*
%doc %{_datadir}/*/lisp/README
%doc %{_datadir}/*/lisp/term/README
%{_applnkdir}/Editors/xemacs.desktop


%{_libdir}/%{name}
%dir %{_libdir}/%{name}-%{version}
%dir %{_libdir}/%{name}-%{version}/%{_target_platform}

%{_datadir}/%{name}

%dir %{_datadir}/%{name}-%{version}
%dir %{_datadir}/%{name}-%{version}/etc
%{_datadir}/%{name}-%{version}/etc/custom
%{_datadir}/%{name}-%{version}/etc/eos
%{_datadir}/%{name}-%{version}/etc/idd
%{_datadir}/%{name}-%{version}/etc/photos
%{_datadir}/%{name}-%{version}/etc/toolbar
%{_datadir}/%{name}-%{version}/etc/*.xbm
%{_datadir}/%{name}-%{version}/etc/*.xpm
%{_datadir}/%{name}-%{version}/etc/*.png
%{_datadir}/%{name}-%{version}/etc/ms-kermit*

%dir %{_datadir}/%{name}-%{version}/lisp
%{_datadir}/%{name}-%{version}/lisp/*.elc
%dir %{_datadir}/%{name}-%{version}/lisp/term
%{_datadir}/%{name}-%{version}/lisp/term/*.elc

%dir %{_datadir}/%{name}-packages
%dir %{_datadir}/%{name}-packages/lisp
%dir %{_datadir}/%{name}-packages/lisp/xemacs-base
%{_datadir}/%{name}-packages/lisp/xemacs-base/*.elc

%attr(755,root,root) %{_bindir}/ootags
%attr(755,root,root) %{_bindir}/gnu*
%attr(755,root,root) %{_bindir}/pstogif
%attr(755,root,root) %{_bindir}/xemacs


%attr(2755,root,mail) %{_libdir}/%{name}-%{version}/*/movemail
%attr(755,root,root) %{_libdir}/%{name}-%{version}/*/cvtmail
%attr(755,root,root) %{_libdir}/%{name}-%{version}/*/digest-doc
%attr(755,root,root) %{_libdir}/%{name}-%{version}/*/fakemail
%attr(755,root,root) %{_libdir}/%{name}-%{version}/*/gnuserv
%attr(755,root,root) %{_libdir}/%{name}-%{version}/*/hexl
%attr(755,root,root) %{_libdir}/%{name}-%{version}/*/make-docfile
%attr(755,root,root) %{_libdir}/%{name}-%{version}/*/make-path
%attr(755,root,root) %{_libdir}/%{name}-%{version}/*/mmencode
%attr(755,root,root) %{_libdir}/%{name}-%{version}/*/profile
%attr(755,root,root) %{_libdir}/%{name}-%{version}/*/sorted-doc
%attr(755,root,root) %{_libdir}/%{name}-%{version}/*/yow
%attr(755,root,root) %{_libdir}/%{name}-%{version}/*/add-big-package.sh
%attr(755,root,root) %{_libdir}/%{name}-%{version}/*/gzip-el.sh
%attr(755,root,root) %{_libdir}/%{name}-%{version}/*/rcs2log
%attr(755,root,root) %{_libdir}/%{name}-%{version}/*/vcdiff
%attr(755,root,root) %{_libdir}/%{name}-%{version}/*/wakeup

%{_mandir}/man1/gnu*
%{_mandir}/man1/xemacs*
%lang(ja) %{_mandir}/ja/man1/*

%{_infodir}/custom.info*gz
%{_infodir}/external-widget.info*gz
%{_infodir}/internals.info*gz
%{_infodir}/new-users-guide.info*gz
%{_infodir}/term.info*gz
%{_infodir}/widget.info*gz
%{_infodir}/xemacs-faq.info*gz
%{_infodir}/xemacs.info*gz

/var/lock/xemacs

%files el 
%defattr(644,root,root,755)

%{_datadir}/%{name}-%{version}/lisp/*.el.gz
%{_datadir}/%{name}-%{version}/lisp/term/*.el.gz
%{_datadir}/%{name}-packages/lisp/xemacs-base/*.el.gz


%files extras
%attr(755,root,root) %{_bindir}/b2m
%attr(755,root,root) %{_bindir}/rcs-checkin
/usr/X11R6/lib/X11/pl/app-defaults/*
