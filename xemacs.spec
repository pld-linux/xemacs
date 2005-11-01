#
# Conditional build:
%bcond_without	pdump		# portable dumper
%bcond_with	postgresql	# enable PostgreSQL support
%bcond_with	gtk		# GTK+ enabled version
#
%define		ver		21.5
%define		sver		23
%define		xver		%{ver}-b%{sver}
%define		basepkgver	1.97
Summary:	The XEmacs -- Emacs: The Next Generation
Summary(es):	El editor XEmacs
Summary(ja):	XEmacs ¥¨¥Ç¥£¥¿
Summary(pl):	XEmacs -- Emacs nastêpnej generacji
Summary(pt_BR):	Editor XEmacs
Summary(ru):	÷ÅÒÓÉÑ GNU Emacs ÄÌÑ X Window System
Summary(uk):	÷ÅÒÓ¦Ñ GNU Emacs ÄÌÑ X Window System
Name:		xemacs
Version:	%{ver}.%{sver}
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	ftp://ftp.xemacs.org/xemacs/%{name}-%{ver}/%{name}-%{version}.tar.gz
# Source0-md5:	3a8111472fa7ae47d74374f85f1d0aae
Source2:	ftp://ftp.xemacs.org/xemacs/packages/%{name}-base-%{basepkgver}-pkg.tar.gz
# Source2-md5:	d51d8afe507a0bb17f08ef211f9f6f5a
Source3:	%{name}.desktop
Source4:	%{name}.ad-pl
Source5:	%{name}-default.el
Source6:	%{name}-ogony-mule.el
Source7:	%{name}-ogony-nomule.el
Source8:	%{name}.png
Patch0:		%{name}-info.patch
Patch1:		%{name}-fix_ldflafs.patch
Patch3:		%{name}-no-memory-warnings.patch
Patch4:		%{name}-dump-paths-lispdir.patch
Patch5:		%{name}-destdir.patch
Patch6:		%{name}-do-not-create-backups-in-temp-directories.patch
Patch7:		%{name}-level3.patch
Patch8:		%{name}-ptmx.patch
Patch9:		%{name}-set-locale-to-c-when-not-supported-by-x.patch
Patch10:	%{name}-vendor.patch
URL:		http://www.xemacs.org/
# for X11/bitmaps/gray
BuildRequires:	XFree86
BuildRequires:	XFree86-devel
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	gpm-devel
%{?with_gtk:BuildRequires:	gtk+-devel >= 1.2.10}
BuildRequires:	motif-devel
BuildRequires:	ncurses-devel >= 5.0
%{?with_postgresql:BuildRequires:	postgresql-devel >= 7.1}
BuildRequires:	sed >= 4.0
BuildRequires:	texinfo
BuildRequires:	zlib-devel
Requires:	ctags
Requires:	%{name}-common = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ulibdir	/usr/lib
%define		_appdefsdir	/usr/X11R6/lib/X11/app-defaults

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

%description -l ja
XEmacs ¤Ï Free Software Foundation ¤Î Richard Stallman ¤Ë¤è¤Ã¤Æ
½ñ¤«¤ì¤¿ GNU Emacs ¤È¤Î¸ß´¹À­¤ò°Ý»ý¤·¤Ä¤Ä¿ôÂ¿¤¯¤Î²þÎÉ¤¬»Ü¤µ¤ì¤¿
ÇÉÀ¸¥Ð¡¼¥¸¥ç¥ó¤Ç¤¹¡¥ ¸µ¡¹ Emacs 19 ¤ò¸µ¤Ë³«È¯¤µ¤ì¡¤Emacs
¤Î¸åÂ³¥ê¥ê¡¼¥¹¤ËÄÉ²Ã¤µ¤ì¤¿ µ¡Ç½¤ÈÆ±´ü¤¬¼è¤é¤ì¤Æ¤¤¤Þ¤¹¡¥

%description -l es
XEmacs es una versión de Emacs, compatible con GNU Emacs y conteniendo
muchas mejoras. Fue basado originalmente en una versión anterior de
GNU Emacs, y ha seguido las versiones subsecuentes.

%description -l pl
XEmacs jest odmian± Emacsa, zgodn± (i zawieraj±c± wiele udogodnieñ) z
GNU Emacsem tworzonym przez Richarda Stallmana z Free Software
Foundation. Wywodzi siê z wczesnych odmian GNU Emacs 19, wprowadza
wiele mi³ych ulepszeñ nie trac±c jednak wiêzi z oryginaln± wersj±.

Ta dystrybucja XEmacsa zosta³a podzielona na wiele pakietów binarnych:

xemacs-common - pakiet zawieraj±cy pliki wspó³dzielone przez pakiety
xemacs i xemacs-nox xemacs - XEmacs skompilowany ze wsparciem dla X11
i konsoli xemacs-nox - XEmacs skompilowany bez wsparcia dla X11
(pracuje tylko na konsoli tekstowej) xemacs-extras - pliki wchodz±ce w
sk³ad dystrybucji GNU Emacs

Do pracy niezbêdne s± xemacs-common oraz xemacs b±d¼ xemacs-nox.
Zainstaluj tak¿e xemacs-extras je¶li nie posiadasz GNU Emacsa.

%description -l pt_BR
XEmacs é uma versão do Emacs, compatível com o GNU Emacs, contendo
muitos adicionais. Foi baseado numa versão anterior do GNU Emacs, e
seguiu as versões subseqüentes.

%description -l ru
XEmacs (ÒÁ×ÎÏ ËÁË É ÏÒÉÇÉÎÁÌØÎÙÊ GNU Emacs) - ÜÔÏ
ÓÁÍÏÄÏËÕÍÅÎÔÉÒÏ×ÁÎÎÙÊ, ÎÁÓÔÒÁÉ×ÁÅÍÙÊ, ÒÁÓÛÉÒÑÅÍÙÊ ÒÅÄÁËÔÏÒ Ó
ÏÔÏÂÒÁÖÅÎÉÅÍ × ÒÅÁÌØÎÏÍ ×ÒÅÍÅÎÉ. XEmacs ÓÁÍÏÄÏËÕÍÅÎÔÉÒÏ×ÁÎ ÐÏÔÏÍÕ ÞÔÏ
× ÌÀÂÏÅ ×ÒÅÍÑ ×Ù ÍÏÖÅÔÅ ÎÁÖÁÔØ control-h ÄÌÑ ÐÏÄÓËÁÚËÉ Ï ×ÏÚÍÏÖÎÙÈ
ÏÐÃÉÑÈ ÉÌÉ Ï ÔÏÍ, ÞÔÏ ÄÅÌÁÅÔ ËÏÍÁÎÄÁ. XEmacs ÎÁÓÔÒÁÉ×ÁÅÍ ÐÏÔÏÍÕ ÞÔÏ ×Ù
ÍÏÖÅÔÅ ÉÚÍÅÎÉÔØ ÏÐÒÅÄÅÌÅÎÉÑ ÅÇÏ ËÏÍÁÎÄ ÎÁ ×ÓÅ, ÞÔÏ ×ÁÍ ÕÇÏÄÎÏ. XEmacs
ÒÁÓÛÉÒÑÅÍ ÐÏÔÏÍÕ ÞÔÏ ×Ù ÍÏÖÅÔÅ ÎÁÐÉÓÁÔØ ÓÏ×ÅÒÛÅÎÎÏ ÎÏ×ÙÅ
ËÏÍÁÎÄÙ-ÐÒÏÇÒÁÍÍÙ ÎÁ ÑÚÙËÅ Lisp, ËÏÔÏÒÙÅ ÂÕÄÕÔ ÉÓÐÏÌÎÑÔØÓÑ ×ÓÔÒÏÅÎÎÙÍ
ÉÎÔÅÒÐÒÅÔÁÔÏÒÏÍ Lisp. XEmacs ×ËÌÀÞÁÅÔ ÏÔÏÂÒÁÖÅÎÉÅ × ÒÅÁÌØÎÏÍ ×ÒÅÍÅÎÉ,
ÞÔÏ ÚÎÁÞÉÔ ÞÔÏ ÒÅÄÁËÔÉÒÕÅÍÙÊ ÔÅËÓÔ ×ÉÄÉÍ ÎÁ ÜËÒÁÎÅ É ÏÂÎÏ×ÌÑÅÔÓÑ ÏÞÅÎØ
ÞÁÓÔÏ (ÏÂÙÞÎÏ ÐÏÓÌÅ ËÁÖÄÏÇÏ ÓÉÍ×ÏÌÁ ÉÌÉ ÐÁÒÙ ÓÉÍ×ÏÌÏ×) ÐÏ ÍÅÒÅ ÎÁÂÏÒÁ
ÔÅËÓÔÁ.

%description -l uk
XEmacs (ÔÁË ÓÁÍÏ ÑË ¦ ÏÒÉÇ¦ÎÁÌØÎÉÊ GNU Emacs) - ÃÅ ÓÁÍÏÄÏËÕÍÅÎÔÏ×ÁÎÉÊ,
ÎÁÓÔÒÏÀ×ÁÎÉÊ, ÒÏÚÛÉÒÀ×ÁÎÉÊ ÒÅÄÁËÔÏÒ Ú ×¦ÄÏÂÒÁÖÅÎÎÑÍ Õ ÒÅÁÌØÎÏÍÕ ÞÁÓ¦.
XEmacs ÓÁÍÏÄÏËÕÍÅÎÔÏ×ÁÎÉÊ ÔÏÍÕ ÝÏ Õ ÌÀÂÉÊ ÞÁÓ ×É ÍÏÖÅÔÅ ÎÁÔÉÓÎÕÔÉ
control-h ÄÌÑ Ð¦ÄËÁÚËÉ ÐÒÏ ÍÏÖÌÉ×¦ ÏÐÃ¦§ ÁÂÏ ÐÒÏ ÔÅ, ÝÏ ÒÏÂÉÔØ
ËÏÍÁÎÄÁ. XEmacs ÎÁÓÔÒÏÀ×ÁÎÉÊ ÔÏÍÕ ÝÏ ×É ÍÏÖÅÔÅ ÚÍ¦ÎÉÔÉ ×ÉÚÎÁÞÅÎÎÑ ÊÏÇÏ
ËÏÍÁÎÄ ÎÁ ×ÓÅ, ÝÏ ×ÁÍ ÚÁ×ÇÏÄÎÏ. XEmacs ÒÏÚÛÉÒÀ×ÁÎÉÊ ÔÏÍÕ ÝÏ ×É ÍÏÖÅÔÅ
ÎÁÐÉÓÁÔÉ ÁÂÓÏÌÀÔÎÏ ÎÏ×¦ ËÏÍÁÎÄÉ-ÐÒÏÇÒÁÍÉ ÎÁ ÍÏ×¦ Lisp, ÑË¦ ÂÕÄÕÔØ
×ÉËÏÎÕ×ÁÔÉÓÑ ×ÂÕÄÏ×ÁÎÉÍ ¦ÎÔÅÒÐÒÅÔÁÔÏÒÏÍ Lisp. XEmacs ×ËÌÀÞÁ¤
×¦ÄÏÂÒÁÖÅÎÎÑ Õ ÒÅÁÌØÎÏÍÕ ÞÁÓ¦, ÝÏ ÏÚÎÁÞÁ¤ ÝÏ ÒÅÄÁÇÏ×ÁÎÉÊ ÔÅËÓÔ ×ÉÄÎÏ
ÎÁ ÅËÒÁÎ¦ ¦ ×¦Î ÐÏÎÏ×ÌÀ¤ÔØÓÑ ÄÕÖÅ ÞÁÓÔÏ (ÚÁÚ×ÉÞÁÊ Ð¦ÓÌÑ ËÏÖÎÏÇÏ
ÓÉÍ×ÏÌÕ ÁÂÏ ÐÁÒÉ ÓÉÍ×ÏÌ¦×) ÐÏ Í¦Ò¦ ÎÁÂÏÒÕ ÔÅËÓÔÕ.

%package common
Summary:	Common part of XEmacs distribution
Summary(pl):	Wspólne czê¶ci XEmacsa
Group:		Applications/Editors/Emacs
Provides:	xemacs-base-pkg
Requires:	emacscommon

%description common
Common files of XEmacs distribution. This package does not contain
XEmacs editor binary, you must install xemacs or xemacs-nox package to
use XEmacs -- Emacs: The Next Generation editor.

%description common -l pl
Wspólne pliki XEmacsa. Ten pakiet nie zawiera pliku wykonywalnego
edytora, musisz zainstalowaæ xemacs lub xemacs-nox, aby u¿ywaæ XEmacsa
b±d¼ Emacsa: edytor Nastêpnej Generacji.

%package nox
Summary:	XEmacs binary compiled without X11 support
Summary(pl):	XEmacs skompilowany bez wsparcia dla X11
Group:		Applications/Editors/Emacs
Requires:	%{name}-common = %{version}-%{release}
Provides:	%{name} = %{version}-%{release}

%description nox
XEmacs binary compiled with TTY support only, without X11 support.

%description nox -l pl
XEmacs skompilowany bez wsparcia dla X11 (pracuje tylko na konsoli lub
w okienku xterma).

%package extras
Summary:	Files which conflict with GNU Emacs
Summary(pl):	Wspólne pliki XEmacsa i GNU Emacsa
Group:		Applications/Editors/Emacs
Provides:	emacscommon
Obsoletes:	emacscommon

%description extras
These files are common between GNU Emacs and XEmacs. If you do not
have GNU Emacs installed, be sure to install this package as well when
you install XEmacs.

%description extras -l pl
S± to wpólne pliki GNU Emacs i XEmacs. Je¶li nie zainstalowa³e¶ GNU
Emacsa, to koniecznie zainstaluj ten pakiet.

%prep
%setup -q -a2
%patch0 -p1
%patch1 -p1
%ifarch alpha ia64
# disable memory_warnings() - it doesn't support memory model used on alpha
%patch3 -p1
%endif
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
rm lisp/startup.elc
sed -i -e "s#@srcdir@#$PWD#" lisp/startup.el

%build
cp /usr/share/automake/config.sub .
CFLAGS=" %{rpmcflags}"
CPPFLAGS=" %{rpmcflags}"
LDFLAGS=" %{rpmldflags} -lc"
sitelispdir=%{_ulibdir}/%{name}/site-lisp
export CFLAGS CPPFLAGS LDFLAGS sitelispdir

# no X
%configure %{_target_platform} \
	--prefix=%{_prefix} \
	--infodir=%{_infodir} \
	--mandir=%{_mandir}/man1 \
	--datadir=%{_datadir} \
	--with-package_path="~/.xemacs::%{_datadir}/%{name}-packages" \
	--enable-mule \
	--with-site-lisp \
%if %{with postgreql}
	--with-postgresql \
%else
	--without-postgresql \
%endif
	--disable-sound \
	--without-x11 \
	--without-jpeg \
	--without-png \
	--without-xpm \
	--with-gpm \
	--with-ncurses \
	--enable-database=no \
%if %{with pdump}
	--enable-pdump=yes \
%else
	--enable-pdump=no \
%endif
	--without-tiff \
	--without-dnet \
	--without-ldap \
	--without-dragndrop \
	--without-msw

sitelispdir=%{_ulibdir}/%{name}/site-lisp \
%{__make} -j1 \
	CC="%{__cc}"
cp src/xemacs src/xemacs-nox
%if %{with pdump}
cp src/xemacs.dmp src/xemacs-nox.dmp
%endif
cp lib-src/gnuserv lib-src/gnuserv-nox
%{__make} -j1 distclean

# X
./configure %{_target_platform} \
	--prefix=%{_prefix} \
	--infodir=%{_infodir} \
	--mandir=%{_mandir}/man1 \
	--datadir=%{_datadir} \
	--with-package_path="~/.xemacs::%{_datadir}/%{name}-packages" \
	--enable-mule \
	--with-site-lisp \
%if %{with postgresql}
	--with-postgresql \
%else
	--without-postgresql \
%endif
	--disable-sound \
	--with-jpeg \
	--with-png \
	--with-xpm \
	--with-gpm \
	--with-ncurses \
%if %{with gtk}
	--with-gtk \
%else
	--without-gtk \
%endif
%if %{undefined gtk}
	--with-x11 --enable-menubars=lucid --enable-scrollbars=motif \
	--enable-dialogs=motif --enable-widgets=motif \
%endif
	--enable-database=no \
	--enable-gnome=no \
	--without-tiff \
	--without-dnet \
	--without-ldap \
	--without-dragndrop \
	--without-msw \
%if %{without pdump}
	--pdump=no
%endif


# if you want to xemacs sings and plays sounds add option
#	--enable-sound=native

#	--lispdir=%{_datadir}/%{name}/lisp \
#	--pkgdir=%{_datadir}/%{name}/lisp \
#	--etcdir=%{_datadir}/%{name}/etc \
#	--cflags="$RPM_OPT_FLAGS" \
#	--error-checking=none \
#	--debug=no \
#	--with-session=yes \

sitelispdir=%{_ulibdir}/%{name}/site-lisp \
%{__make} -j1 \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},/var/lock/xemacs} \
	$RPM_BUILD_ROOT{%{_mandir}/{ja/man1,man1},%{_appdefsdir}/pl} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/lisp \
	$RPM_BUILD_ROOT%{_ulibdir}/%{name} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}-packages/{etc,lib-src}

%{__make} install-arch-dep install-arch-indep \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix} \
	infodir=%{_infodir} \
	mandir=%{_mandir}/man1 \
	datadir=%{_datadir} \

install %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}

( cd $RPM_BUILD_ROOT%{_datadir}/%{name}-packages; gzip -dc %{SOURCE2} | tar xf - )

install %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/%{name}-packages/lisp/default.el
install %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/%{name}-packages/lisp/ogony-mule.el
install %{SOURCE7} $RPM_BUILD_ROOT%{_datadir}/%{name}-packages/lisp/ogony-nomule.el
install %{SOURCE8} $RPM_BUILD_ROOT%{_pixmapsdir}

#mv $RPM_BUILD_ROOT%{_ulibdir}/%{name}-%{version}/*-linux/config.values $RPM_BUILD_ROOT%{_ulibdir}/%{name}

[ -d $RPM_BUILD_ROOT%{_datadir}/%{name}/site-lisp ] || \
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/site-lisp
ln -s %{_datadir}/%{name}/site-lisp $RPM_BUILD_ROOT%{_ulibdir}/%{name}/site-lisp

install $RPM_BUILD_ROOT%{_datadir}/%{name}-%{xver}%{_sysconfdir}/Emacs.ad \
	$RPM_BUILD_ROOT%{_appdefsdir}/Emacs
install $RPM_BUILD_ROOT%{_datadir}/%{name}-%{xver}%{_sysconfdir}/Emacs.ad \
	$RPM_BUILD_ROOT%{_appdefsdir}/pl/Emacs
cat %{SOURCE4} >>$RPM_BUILD_ROOT%{_appdefsdir}/pl/Emacs

#mv $RPM_BUILD_ROOT%{_datadir}/%{name}-%{xver}%{_sysconfdir}/xemacs-ja.1 \
#	$RPM_BUILD_ROOT%{_mandir}/ja/man1/xemacs.1

mv -f $RPM_BUILD_ROOT%{_bindir}/xemacs-%{xver} \
	$RPM_BUILD_ROOT%{_bindir}/xemacs

%if %{with pdump}
install src/xemacs.dmp $RPM_BUILD_ROOT/%{_bindir}
%endif

find $RPM_BUILD_ROOT%{_datadir}/%{name}-%{xver}/* -type f -name "ChangeLog*" | xargs gzip -9nf

install src/xemacs-nox $RPM_BUILD_ROOT%{_bindir}
%if %{with pdump}
install src/xemacs-nox.dmp $RPM_BUILD_ROOT%{_bindir}
%endif

# hack...
install lib-src/gnuserv-nox $RPM_BUILD_ROOT%{_bindir}
mv -f $RPM_BUILD_ROOT%{_ulibdir}/%{name}-%{xver}/*-linux*/gnuserv $RPM_BUILD_ROOT%{_bindir}

# remove some .elc files
find $RPM_BUILD_ROOT -name '_pkg.elc' -exec rm "{}" ";"
find $RPM_BUILD_ROOT -name 'auto-autoloads.elc' -exec rm "{}" ";"

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done
rm -f $RPM_BUILD_ROOT%{_bindir}/{c,e}tags
# hmm, maybe xemacs-devel is necessary?
rm -rf	$RPM_BUILD_ROOT%{_ulibdir}/%{name}-%{xver}/*-linux/include \
	$RPM_BUILD_ROOT%{_infodir}/dir* \
	$RPM_BUILD_ROOT%{_infodir}/{info,standards,texinfo}.info*

find $RPM_BUILD_ROOT -regex '.*~$' -exec rm -f {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnuattach
%attr(755,root,root) %{_bindir}/gnuclient
%attr(755,root,root) %{_bindir}/gnudoit
%attr(755,root,root) %{_bindir}/gnuserv
%attr(755,root,root) %{_bindir}/xemacs
%if %{with pdump}
%attr(644,root,root) %{_bindir}/xemacs.dmp
%endif
%attr(755,root,root) %{_bindir}/ootags
%attr(755,root,root) %{_bindir}/ellcc
%{_datadir}/%{name}-%{xver}/etc/custom
%{_datadir}/%{name}-%{xver}/etc/eos
%{_datadir}/%{name}-%{xver}/etc/toolbar
%{_datadir}/%{name}-%{xver}/etc/*.png
%{_datadir}/%{name}-%{xver}/etc/*.xbm
%{_datadir}/%{name}-%{xver}/etc/*.xpm
%{_appdefsdir}/Emacs
%lang(pl) %{_appdefsdir}/pl/Emacs
%{_desktopdir}/*
%{_pixmapsdir}/*
%{_mandir}/man1/gnuattach.1*
%{_mandir}/man1/gnuclient.1*
%{_mandir}/man1/gnudoit.1*
%{_mandir}/man1/gnuserv.1*

%files common
%defattr(644,root,root,755)
%doc README etc/NEWS
%dir %{_datadir}/%{name}-%{xver}
%dir %{_datadir}/%{name}-%{xver}/etc
%{_datadir}/%{name}-%{xver}/etc/package-index.LATEST.gpg
%doc %{_datadir}/%{name}-%{xver}/etc/TUTORIAL
%doc %lang(de) %{_datadir}/%{name}-%{xver}/etc/TUTORIAL.de
%doc %lang(fr) %{_datadir}/%{name}-%{xver}/etc/TUTORIAL.fr
%doc %lang(hr) %{_datadir}/%{name}-%{xver}/etc/TUTORIAL.hr
%doc %lang(ja) %{_datadir}/%{name}-%{xver}/etc/TUTORIAL.ja
%doc %lang(ko) %{_datadir}/%{name}-%{xver}/etc/TUTORIAL.ko
%doc %lang(nb) %{_datadir}/%{name}-%{xver}/etc/TUTORIAL.no
%doc %lang(pl) %{_datadir}/%{name}-%{xver}/etc/TUTORIAL.pl
%doc %lang(ro) %{_datadir}/%{name}-%{xver}/etc/TUTORIAL.ro
%doc %lang(ru) %{_datadir}/%{name}-%{xver}/etc/TUTORIAL.ru
%doc %lang(th) %{_datadir}/%{name}-%{xver}/etc/TUTORIAL.th
%doc %{_datadir}/%{name}-%{xver}/etc/[A-SU-Z]*
%doc %{_datadir}/%{name}-%{xver}/etc/refcard.ps.gz
%doc %{_datadir}/%{name}-%{xver}/etc/refcard.tex
%doc %{_datadir}/%{name}-%{xver}/etc/sample.*

%{_datadir}/%{name}-%{xver}/etc/unicode

%{_ulibdir}/%{name}

%{_datadir}/%{name}

# do not know it is necessary
%dir %{_ulibdir}/%{name}-%{xver}
%dir %{_ulibdir}/%{name}-%{xver}/*-linux*
%{_ulibdir}/%{name}-%{xver}/*-linux/modules
%attr(755,root,root) %{_ulibdir}/%{name}-%{xver}/*-linux/[Dacdfghprsvwy]*
%attr(755,root,root) %{_ulibdir}/%{name}-%{xver}/*-linux/m[am]*
%attr(755,root,root) %{_ulibdir}/%{name}-%{xver}/*-linux/mov*

%{_datadir}/%{name}-%{xver}/lisp

%dir %{_datadir}/%{name}-packages
%{_datadir}/%{name}-packages/etc
%{_datadir}/%{name}-packages/lisp
%{_datadir}/%{name}-packages/lib-src

%{_mandir}/man1/xemacs.1*
#%lang(ja) %{_mandir}/ja/man1/*

%{_infodir}/*.info*

/var/lock/xemacs

%files nox
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xemacs-nox
%if %{with pdump}
%attr(644,root,root) %{_bindir}/xemacs-nox.dmp
%endif
%attr(755,root,root) %{_bindir}/gnuserv-nox

%files extras
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/b2m
%attr(755,root,root) %{_bindir}/rcs-checkin
