# _with_postgresql	- postgresql support
# _with_gtk		- gtk enabled version
%define		ver		21.4
%define		basepkgver 	1.55
Summary:	The XEmacs -- Emacs: The Next Generation
Summary(pl):	XEmacs -- Emacs nastêpnej generacji
Name:		xemacs
Version:	%{ver}.4
Release:	2
License:	GPL
Group:		Applications/Editors/Emacs
Group(de):	Applikationen/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Source0:	ftp://ftp.xemacs.org/%{name}-%{ver}/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.xemacs.org/%{name}-%{ver}/%{name}-%{version}-elc.tar.gz
Source2:	ftp://ftp.xemacs.org/packages/%{name}-base-%{basepkgver}-pkg.tar.gz
Source3:	%{name}.desktop
Source4:	%{name}.ad-pl
Source5:	%{name}-default.el
Source6:	%{name}-ogony-mule.el
Source7:	%{name}-ogony-nomule.el
Source8:	%{name}.png
Patch0:		%{name}-info.patch
Patch1:		%{name}-archlibdir.patch
Patch2:		%{name}-fix_ldflafs.patch
URL:		http://www.xemacs.org/
BuildRequires:	XFree86-devel
BuildRequires:	motif-devel
BuildRequires:	zlib-devel
BuildRequires:	libtiff-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng >= 1.0.8
%{?_with_postgresql:BuildRequires:	postgresql-devel >= 7.1}
BuildRequires:	gpm-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	gpm-devel
%if %{?_with_gtk:1}%{!?_with_gtk:0}
BuildRequires:	gtk+-devel >= 1.2.10
BuildRequires:	glib-devel
%endif
Requires:	ctags
Requires:	%{name}-common = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XEmacs is a highly customizable open source text editor and
application development system. XEmacs is a version of Emacs,
compatible with and containing many improvements over GNU Emacs,
written by Richard Stallman of the Free Software Foundation. It was
originally based on an early release of GNU Emacs version 19, and has
tracked subsequent releases of GNU Emacs as they have become
available. This XEmacs distribution has been splitted in some rpm:

xemacs-common - common files needed by xemacs and xemacs-nox packages
xemacs - XEmacs binary with both X11 and TTY support xemacs-nox -
XEmacs binary with TTY support only xemacs-extras - files in conflict
with emacs

Install xemacs-extras if you haven't emacs installed.

%description -l pl 
XEmacs jest odmian± Emacsa, zgodn± (i zawieraj±c± wiele udogodnieñ) z
GNU Emacsem tworzonym przez Richarda Stallmana z Free Software
Foundation. Wywodzi siê z wczesnych odmian GNU Emacs 19, wprowadza
wiele mi³ych ulepszeñ nie trac±c jednak wiêzi z oryginaln± wersj±.

Ta dystrubucja XEmacsa zosta³± podzielona na wiele pakietów binarnych:

xemacs-common - pakiet zawieraj±cy pliki wspó³dzielone przez pakiety
xemacs i xemacs-nox xemacs - XEmacs skompilowany ze wsparciem dla X11
i konsoli xemacs-nox - XEmacs skompilowany bez wsparcia dla X11
(pracuje tylko na konsoli tekstowej) xemacs-extras - pliki wchodz±ce w
sk³ad dystrybucji GNU Emacs

Do pracy niezbêdne s± xemacs-common oraz xemacs b±d¼ xemacs-nox.
Zainstaluj tak¿e xemacs-extras je¶li nie posiadasz GNU Emacsa.

%package common
Summary:	Common part of XEmacs distribution
Group:		Applications/Editors/Emacs
Group(de):	Applikationen/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Provides:	xemacs-base-pkg

%description common
Common files of XEmacs distribution. This package does not contain
XEmacs editor binary, you must install xemacs or xemacs-nox package to
use XEmacs -- Emacs: The Next Generation editor.

%package nox
Summary:	XEmacs binary compiled without X11 support
Group:		Applications/Editors/Emacs
Group(de):	Applikationen/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	%{name}-common = %{version}
Provides:	%{name} = %{version}

%description nox
XEmacs binary compiled with TTY support only, without X11 support.

%description nox -l pl
XEmacs skompilowany bez wsparcia dla X11 (pracuje tylko na konsoli lub
w okienku xterma).

%package extras
Summary:	files which conflict with GNU Emacs
Summary(pl):	wspólne pliki XEmacsa i GNU Emacsa
Group:		Applications/Editors/Emacs
Group(de):	Applikationen/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	%{name} = %{version}
Conflicts:	emacs

%description extras
These files are common between GNU Emacs and XEmacs. If you do not
have GNU Emacs installed, be sure to install this package as well when
you install XEmacs.

%description extras -l pl
S± to wpólne pliki GNU Emacs i XEmacs. Je¶li nie zainstalowa³e¶ GNU
Emacsa, to koniecznie zainstaluj ten pakiet.

%prep
%setup0 -q -b1 -a2
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
CFLAGS="-I%{rpmcflags}"
CPPFLAGS="-I%{rpmcflags}"
LDFLAGS="%{rpmldflags} -lc"
sitelispdir=%{_libdir}/%{name}/site-lisp
export CFLAGS CPPFLAGS LDFLAGS sitelispdir

# no X 
./configure %{_target_platform} \
	--prefix=%{_prefix} \
	--infodir=%{_infodir} \
	--mandir=%{_mandir}/man1 \
	--datadir=%{_datadir} \
	--package_path="~/.xemacs::%{_datadir}/%{name}-packages" \
	--with-mule \
	--with-site-lisp \
	--without-postgresql \
	--without-sound \
	--without-x11 \
	--without-jpeg \
	--without-png \
	--without-xpm \
	--with-gpm \
	--with-ncurses \
	--with-database=no \
	--without-tiff \
	--without-dnet \
	--without-ldap \
	--without-dragndrop \
	--without-msw

sitelispdir=%{_libdir}/%{name}/site-lisp \
%{__make}
cp src/xemacs src/xemacs-nox
%{__make} distclean

# X
./configure %{_target_platform} \
	--prefix=%{_prefix} \
	--infodir=%{_infodir} \
	--mandir=%{_mandir}/man1 \
	--datadir=%{_datadir} \
	--package_path="~/.xemacs::%{_datadir}/%{name}-packages" \
	--with-mule \
	--with-site-lisp \
	--with%{?!_with_postgresql:out}-postgresql \
	--without-sound \
	--with-jpeg \
	--with-png \
	--with-xpm \
	--with-gpm \
	--with-ncurses \
	--with%{?!_with_gtk:out}-gtk \
	%{?!_with_gtk:--with-x11 --with-menubars=lucid --with-scrollbars=motif} \
	%{?!_with_gtk:--with-dialogs=motif --with-widgets=motif} \
	--with-database=no \
	--with-gnome=no \
	--without-tiff \
	--without-dnet \
	--without-ldap \
	--without-dragndrop \
	--without-msw

# if you want to xemacs sings and plays sounds add option 
#	--with-sound=native 

#	--lispdir=%{_datadir}/%{name}/lisp \
#	--pkgdir=%{_datadir}/%{name}/lisp \
#	--etcdir=%{_datadir}/%{name}/etc \
#	--cflags="$RPM_OPT_FLAGS" \
#	--error-checking=none \
#	--debug=no \
#	--with-session=yes \

sitelispdir=%{_libdir}/%{name}/site-lisp \
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Development/Editors,%{_pixmapsdir},/var/lock/xemacs} \
	$RPM_BUILD_ROOT{%{_mandir}/{ja/man1,man1},%{_prefix}/X11R6/lib/X11/app-defaults/pl} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/lisp \
	$RPM_BUILD_ROOT%{_libdir}/%{name} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}-packages/{etc,lib-src}

%{__make} install-arch-dep install-arch-indep \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	infodir=$RPM_BUILD_ROOT%{_infodir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}/man1 \
	datadir=$RPM_BUILD_ROOT%{_datadir} \

install %{SOURCE3} $RPM_BUILD_ROOT%{_applnkdir}/Development/Editors/xemacs.desktop

( cd $RPM_BUILD_ROOT%{_datadir}/%{name}-packages; gzip -dc %{SOURCE2} | tar xf - )

install %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/%{name}-packages/lisp/default.el
install %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/%{name}-packages/lisp/ogony-mule.el
install %{SOURCE7} $RPM_BUILD_ROOT%{_datadir}/%{name}-packages/lisp/ogony-nomule.el
install %{SOURCE8} $RPM_BUILD_ROOT%{_pixmapsdir}

#mv $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/%{_target_platform}/config.values $RPM_BUILD_ROOT%{_libdir}/%{name}

[ -d $RPM_BUILD_ROOT%{_datadir}/%{name}/site-lisp ] || \
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/site-lisp
ln -s %{_datadir}/%{name}/site-lisp $RPM_BUILD_ROOT%{_libdir}/%{name}/site-lisp

install $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}%{_sysconfdir}/Emacs.ad \
	$RPM_BUILD_ROOT%{_prefix}/X11R6/lib/X11/app-defaults/Emacs
install $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}%{_sysconfdir}/Emacs.ad \
	$RPM_BUILD_ROOT%{_prefix}/X11R6/lib/X11/app-defaults/pl/Emacs
cat %{SOURCE4} >>$RPM_BUILD_ROOT%{_prefix}/X11R6/lib/X11/app-defaults/pl/Emacs

mv $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}%{_sysconfdir}/xemacs-ja.1 \
	$RPM_BUILD_ROOT%{_mandir}/ja/man1/xemacs.1

mv -f $RPM_BUILD_ROOT%{_bindir}/xemacs-%{version} \
	$RPM_BUILD_ROOT%{_bindir}/xemacs

find $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/* -type f -name "ChangeLog*" | xargs gzip -9nf

install -s src/xemacs-nox $RPM_BUILD_ROOT%{_bindir}

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done
rm -f $RPM_BUILD_ROOT%{_bindir}/{c,e}tags
# hmm, maybe xemacs-devel is necessary?
rm -fr $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/%{_target_platform}/include
rm -f $RPM_BUILD_ROOT%{_infodir}/dir*
rm -f $RPM_BUILD_ROOT%{_infodir}/{info,standards,texinfo}.info*

find $RPM_BUILD_ROOT -regex '.*~$' -exec rm -f {} \;

gzip -9nf README GETTING.GNU.SOFTWARE PROBLEMS \
	etc/NEWS etc/MAILINGLISTS BUGS etc/TERMS etc/SERVICE

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1 

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1 

%files
%defattr(644,root,root,755)
%lang(en) %{_prefix}/X11R6/lib/X11/app-defaults/Emacs
%lang(pl) %{_prefix}/X11R6/lib/X11/app-defaults/pl/Emacs
%attr(755,root,root) %{_bindir}/gnu*
%attr(755,root,root) %{_bindir}/xemacs
%attr(755,root,root) %{_bindir}/ootags
%attr(755,root,root) %{_bindir}/ellcc
%attr(755,root,root) %{_bindir}/gnuserv
%{_applnkdir}/Development/Editors/xemacs.desktop
%{_pixmapsdir}/*
%{_mandir}/man1/gnuattach.1*
%{_mandir}/man1/gnuclient.1*
%{_mandir}/man1/gnudoit.1*
%{_mandir}/man1/gnuserv.1*
%{_datadir}/%{name}-%{version}%{_sysconfdir}/custom
%{_datadir}/%{name}-%{version}%{_sysconfdir}/eos
%{_datadir}/%{name}-%{version}%{_sysconfdir}/toolbar
%{_datadir}/%{name}-%{version}%{_sysconfdir}/*.png
%{_datadir}/%{name}-%{version}%{_sysconfdir}/*.xbm
%{_datadir}/%{name}-%{version}%{_sysconfdir}/*.xpm

%files common
%defattr(644,root,root,755)
%doc *.gz etc/*.gz
%doc %{_datadir}/%{name}-%{version}%{_sysconfdir}/TUTORIAL
%doc %lang(de) %{_datadir}/%{name}-%{version}%{_sysconfdir}/TUTORIAL.de
%doc %lang(fr) %{_datadir}/%{name}-%{version}%{_sysconfdir}/TUTORIAL.fr
%doc %lang(hr) %{_datadir}/%{name}-%{version}%{_sysconfdir}/TUTORIAL.hr
%doc %lang(ja) %{_datadir}/%{name}-%{version}%{_sysconfdir}/TUTORIAL.ja
%doc %lang(ko) %{_datadir}/%{name}-%{version}%{_sysconfdir}/TUTORIAL.ko
%doc %lang(no) %{_datadir}/%{name}-%{version}%{_sysconfdir}/TUTORIAL.no
%doc %lang(pl) %{_datadir}/%{name}-%{version}%{_sysconfdir}/TUTORIAL.pl
%doc %lang(ro) %{_datadir}/%{name}-%{version}%{_sysconfdir}/TUTORIAL.ro
%doc %lang(ru) %{_datadir}/%{name}-%{version}%{_sysconfdir}/TUTORIAL.ru
%doc %lang(th) %{_datadir}/%{name}-%{version}%{_sysconfdir}/TUTORIAL.th
%doc %{_datadir}/%{name}-%{version}%{_sysconfdir}/[A-SU-Z]*

%{_libdir}/%{name}
%dir %{_datadidir}/%{name}-%{version}
%attr(755,root,root)  %{_datadir}/%{name}-%{version}/%{_target_platform}

%{_datadir}/%{name}

%dir %{_datadir}/%{name}-%{version}
# do not know it is necessary
%{_datadir}/%{name}-%{version}/%{_target_platform}

%{_datadir}/%{name}-%{version}/lisp/

%dir %{_datadir}/%{name}-packages
%{_datadir}/%{name}-packages/lisp

%{_mandir}/man1/xemacs.1*
%lang(ja) %{_mandir}/ja/man1/*

%{_infodir}/*

/var/lock/xemacs

%files nox
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xemacs-nox

%files extras
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/b2m
%attr(755,root,root) %{_bindir}/rcs-checkin
