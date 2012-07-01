#
# Conditional build:
%bcond_without	pdump		# portable dumper
%bcond_with	postgresql	# enable PostgreSQL support
%bcond_with	gtk		# GTK+ enabled version
#
%define		ver		21.5
%define		sver		31
%define		xver		%{ver}-b%{sver}
%define		basepkgver	2.27
Summary:	The XEmacs -- Emacs: The Next Generation
Summary(es.UTF-8):	El editor XEmacs
Summary(ja.UTF-8):	XEmacs エディタ
Summary(pl.UTF-8):	XEmacs -- Emacs następnej generacji
Summary(pt_BR.UTF-8):	Editor XEmacs
Summary(ru.UTF-8):	Версия GNU Emacs для X Window System
Summary(uk.UTF-8):	Версія GNU Emacs для X Window System
Name:		xemacs
Version:	%{ver}.%{sver}
Release:	3
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	http://ftp.xemacs.org/xemacs/xemacs-%{ver}/%{name}-%{version}.tar.gz
# Source0-md5:	0185fe905d0b8d8d094d9b60cf262d4a
Source2:	http://ftp.xemacs.org/xemacs/packages/%{name}-base-%{basepkgver}-pkg.tar.gz
# Source2-md5:	2ec18d0faf31e2d343f558c730474a63
Source3:	%{name}.desktop
Source4:	%{name}.ad-pl
Source5:	%{name}-default.el
Source6:	%{name}-ogony-mule.el
Source7:	%{name}-ogony-nomule.el
Source8:	%{name}.png
Patch0:		%{name}-info.patch
Patch1:		%{name}-fix_ldflafs.patch
Patch3:		%{name}-no-memory-warnings.patch
Patch5:		%{name}-destdir.patch
Patch6:		%{name}-do-not-create-backups-in-temp-directories.patch
Patch7:		%{name}-level3.patch
Patch8:		%{name}-ptmx.patch
Patch9:		%{name}-set-locale-to-c-when-not-supported-by-x.patch
URL:		http://www.xemacs.org/
# for X11/bitmaps/gray
BuildRequires:	automake
BuildRequires:	gpm-devel
%{?with_gtk:BuildRequires:	gtk+-devel >= 1.2.10}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	motif-devel
BuildRequires:	ncurses-devel >= 5.0
%{?with_postgresql:BuildRequires:	postgresql-devel >= 7.1}
BuildRequires:	sed >= 4.0
BuildRequires:	texinfo
BuildRequires:	xorg-data-xbitmaps
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	zlib-devel
# If xemacs is already installed build fails:
# Load file misc: not found
# Fatal error during load, aborting
# because src/temacs opens files from /usr/../xemacs*
BuildConflicts:	xemacs
BuildConflicts:	xemacs-common
Requires:	%{name}-common = %{version}-%{release}
Requires:	ctags
Requires:	xorg-lib-libXt >= 1.0
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
XEmacs binary with TTY support only

%description -l ja.UTF-8
XEmacs は Free Software Foundation の Richard Stallman によって
書かれた GNU Emacs との互換性を維持しつつ数多くの改良が施された
派生バージョンです． 元々 Emacs 19 を元に開発され，Emacs
の後続リリースに追加された 機能と同期が取られています．

%description -l es.UTF-8
XEmacs es una versión de Emacs, compatible con GNU Emacs y conteniendo
muchas mejoras. Fue basado originalmente en una versión anterior de
GNU Emacs, y ha seguido las versiones subsecuentes.

%description -l pl.UTF-8
XEmacs jest odmianą Emacsa, zgodną (i zawierającą wiele udogodnień) z
GNU Emacsem tworzonym przez Richarda Stallmana z Free Software
Foundation. Wywodzi się z wczesnych odmian GNU Emacs 19, wprowadza
wiele miłych ulepszeń nie tracąc jednak więzi z oryginalną wersją.

Ta dystrybucja XEmacsa została podzielona na wiele pakietów binarnych:

xemacs-common - pakiet zawierający pliki współdzielone przez pakiety
xemacs i xemacs-nox xemacs - XEmacs skompilowany ze wsparciem dla X11
i konsoli xemacs-nox - XEmacs skompilowany bez wsparcia dla X11
(pracuje tylko na konsoli tekstowej)

Do pracy niezbędne są xemacs-common oraz xemacs bądź xemacs-nox.

%description -l pt_BR.UTF-8
XEmacs é uma versão do Emacs, compatível com o GNU Emacs, contendo
muitos adicionais. Foi baseado numa versão anterior do GNU Emacs, e
seguiu as versões subseqüentes.

%description -l ru.UTF-8
XEmacs (равно как и оригинальный GNU Emacs) - это
самодокументированный, настраиваемый, расширяемый редактор с
отображением в реальном времени. XEmacs самодокументирован потому что
в любое время вы можете нажать control-h для подсказки о возможных
опциях или о том, что делает команда. XEmacs настраиваем потому что вы
можете изменить определения его команд на все, что вам угодно. XEmacs
расширяем потому что вы можете написать совершенно новые
команды-программы на языке Lisp, которые будут исполняться встроенным
интерпретатором Lisp. XEmacs включает отображение в реальном времени,
что значит что редактируемый текст видим на экране и обновляется очень
часто (обычно после каждого символа или пары символов) по мере набора
текста.

%description -l uk.UTF-8
XEmacs (так само як і оригінальний GNU Emacs) - це самодокументований,
настроюваний, розширюваний редактор з відображенням у реальному часі.
XEmacs самодокументований тому що у любий час ви можете натиснути
control-h для підказки про можливі опції або про те, що робить
команда. XEmacs настроюваний тому що ви можете змінити визначення його
команд на все, що вам завгодно. XEmacs розширюваний тому що ви можете
написати абсолютно нові команди-програми на мові Lisp, які будуть
виконуватися вбудованим інтерпретатором Lisp. XEmacs включає
відображення у реальному часі, що означає що редагований текст видно
на екрані і він поновлюється дуже часто (зазвичай після кожного
символу або пари символів) по мірі набору тексту.

%package common
Summary:	Common part of XEmacs distribution
Summary(pl.UTF-8):	Wspólne części XEmacsa
Group:		Applications/Editors/Emacs
Provides:	xemacs-base-pkg
Obsoletes:	xemacs-extras

%description common
Common files of XEmacs distribution. This package does not contain
XEmacs editor binary, you must install xemacs or xemacs-nox package to
use XEmacs -- Emacs: The Next Generation editor.

%description common -l pl.UTF-8
Wspólne pliki XEmacsa. Ten pakiet nie zawiera pliku wykonywalnego
edytora, musisz zainstalować xemacs lub xemacs-nox, aby używać XEmacsa
bądź Emacsa: edytor Następnej Generacji.

%package nox
Summary:	XEmacs binary compiled without X11 support
Summary(pl.UTF-8):	XEmacs skompilowany bez wsparcia dla X11
Group:		Applications/Editors/Emacs
Requires:	%{name}-common = %{version}-%{release}
Provides:	%{name} = %{version}-%{release}

%description nox
XEmacs binary compiled with TTY support only, without X11 support.

%description nox -l pl.UTF-8
XEmacs skompilowany bez wsparcia dla X11 (pracuje tylko na konsoli lub
w okienku xterma).

%prep
%setup -q -a2
%patch0 -p1
%patch1 -p1
%ifarch alpha ia64
# disable memory_warnings() - it doesn't support memory model used on alpha
%patch3 -p1
%endif
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

%if "%{_lib}" == "lib64"
sed -i -e 's#"lib"#"lib64"#g' lisp/find-paths.el lisp/info.el lisp/setup-paths.el
%endif

%build
%{__autoconf}
cp /usr/share/automake/config.sub .
CFLAGS=" %{rpmcflags}"
CPPFLAGS=" %{rpmcflags}"
LDFLAGS=" %{rpmldflags} -lc"
export CFLAGS CPPFLAGS LDFLAGS

# no X
%configure %{_target_platform} \
	--prefix=%{_prefix} \
	--exec-prefix=%{_prefix} \
	--infodir=%{_infodir} \
	--mandir=%{_mandir} \
	--datadir=%{_datadir} \
	--libdir=%{_libdir} \
	--with-prefix=%{_prefix} \
	--with-statedir=%{_libdir} \
	--with-archlibdir=%{_libdir}/%{name}-%{xver}/%{_target_cpu}-pld-linux \
	--with-lispdir=%{_datadir}/%{name}-%{xver}/lisp \
	--with-moduledir=%{_libdir}/%{name}-%{xver}/%{_target_cpu}-pld-linux/modules \
	--with-etcdir=%{_datadir}/%{name}-%{xver}/etc \
	--with-docdir=%{_datadir}/%{name}-%{xver}/etc \
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
	--without-msw \
	--disable-kkcc \
	--with-error-checking=none \
	--with-debug=no


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
	--exec-prefix=%{_prefix} \
	--infodir=%{_infodir} \
	--mandir=%{_mandir}/man1 \
	--datadir=%{_datadir} \
	--libdir=%{_libdir} \
	--with-prefix=%{_prefix} \
	--with-statedir=%{_libdir} \
	--with-archlibdir=%{_libdir}/%{name}-%{xver}/%{_target_cpu}-pld-linux \
	--with-lispdir=%{_datadir}/%{name}-%{xver}/lisp \
	--with-moduledir=%{_libdir}/%{name}-%{xver}/%{_target_cpu}-pld-linux/modules \
	--with-etcdir=%{_datadir}/%{name}-%{xver}/etc \
	--with-docdir=%{_datadir}/%{name}-%{xver}/etc \
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
	--with-xft \
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
	--disable-kkcc \
	--with-error-checking=none \
	--with-debug=no \
%if !%{with pdump}
	--pdump=no
%endif


# if you want to xemacs sings and plays sounds add option
#	--enable-sound=native

#	--cflags="$RPM_OPT_FLAGS" \
#	--with-session=yes \

%{__make} -j1 \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},/var/lock/xemacs} \
	$RPM_BUILD_ROOT{%{_mandir}/{ja/man1,man1},%{_datadir}/X11/{pl,}/app-defaults} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/lisp \
	$RPM_BUILD_ROOT%{_datadir}/%{name}-packages/{etc,lib-src,info,pkginfo}

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


[ -d $RPM_BUILD_ROOT%{_datadir}/%{name}/site-lisp ] || \
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/site-lisp

ln -s %{_datadir}/%{name}/site-lisp $RPM_BUILD_ROOT%{_libdir}/%{name}/site-lisp

install $RPM_BUILD_ROOT%{_datadir}/%{name}-%{xver}%{_sysconfdir}/Emacs.ad \
	$RPM_BUILD_ROOT%{_datadir}/X11/app-defaults/XEmacs
install $RPM_BUILD_ROOT%{_datadir}/%{name}-%{xver}%{_sysconfdir}/Emacs.ad \
	$RPM_BUILD_ROOT%{_datadir}/X11/pl/app-defaults/XEmacs
cat %{SOURCE4} >>$RPM_BUILD_ROOT%{_datadir}/X11/pl/app-defaults/XEmacs

mv -f $RPM_BUILD_ROOT%{_bindir}/xemacs-%{xver} \
	$RPM_BUILD_ROOT%{_bindir}/xemacs

%if %{with pdump}
install src/xemacs.dmp $RPM_BUILD_ROOT%{_bindir}
%endif

find $RPM_BUILD_ROOT%{_datadir}/%{name}-%{xver}/* -type f -name "ChangeLog*" | xargs gzip -9nf

install src/xemacs-nox $RPM_BUILD_ROOT%{_bindir}
%if %{with pdump}
install src/xemacs-nox.dmp $RPM_BUILD_ROOT%{_bindir}
%endif

# hack...
install lib-src/gnuserv-nox $RPM_BUILD_ROOT%{_bindir}
mv -f $RPM_BUILD_ROOT%{_libdir}/%{name}-%{xver}/*-linux*/gnuserv $RPM_BUILD_ROOT%{_bindir}

# remove some .elc files
find $RPM_BUILD_ROOT -name '_pkg.elc' -exec rm "{}" ";"

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done
rm -f $RPM_BUILD_ROOT%{_bindir}/{c,e}tags

# hmm, maybe xemacs-devel is necessary?
rm -rf	$RPM_BUILD_ROOT%{_libdir}/%{name}-%{xver}/*-linux/include \
	$RPM_BUILD_ROOT%{_infodir}/dir* \
	$RPM_BUILD_ROOT%{_infodir}/{info,standards,texinfo}.info*

find $RPM_BUILD_ROOT -regex '.*~$' -exec rm -f {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnuattach
%attr(755,root,root) %{_bindir}/gnuclient
%attr(755,root,root) %{_bindir}/gnudoit
%attr(755,root,root) %{_bindir}/gnuserv
%attr(755,root,root) %{_bindir}/xemacs
%if %{with pdump}
%{_bindir}/xemacs.dmp
%endif
%attr(755,root,root) %{_bindir}/ootags
%attr(755,root,root) %{_bindir}/ellcc
%{_datadir}/%{name}-%{xver}/etc/custom
%{_datadir}/%{name}-%{xver}/etc/eos
%{_datadir}/%{name}-%{xver}/etc/toolbar
%{_datadir}/%{name}-%{xver}/etc/*.png
%{_datadir}/%{name}-%{xver}/etc/*.xbm
%{_datadir}/%{name}-%{xver}/etc/*.xpm
%{_datadir}/X11/app-defaults/XEmacs
%lang(pl) %{_datadir}/X11/pl/app-defaults/XEmacs
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_mandir}/man1/gnuattach.1*
%{_mandir}/man1/gnuclient.1*
%{_mandir}/man1/gnudoit.1*
%{_mandir}/man1/gnuserv.1*

%files common
%defattr(644,root,root,755)
%doc README etc/NEWS
%attr(755,root,root) %{_bindir}/b2m
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
%{_datadir}/%{name}

# do not know it is necessary
%dir %{_libdir}/%{name}-%{xver}
%dir %{_libdir}/%{name}-%{xver}/*-linux*
%{_libdir}/%{name}-%{xver}/*-linux/modules
%attr(755,root,root) %{_libdir}/%{name}-%{xver}/*-linux/[Dacdfghprsvwy]*
%attr(755,root,root) %{_libdir}/%{name}-%{xver}/*-linux/m[am]*
%attr(755,root,root) %{_libdir}/%{name}-%{xver}/*-linux/mov*

%{_datadir}/%{name}-%{xver}/lisp

%dir %{_datadir}/%{name}-packages
%dir %{_datadir}/%{name}-packages/info
%dir %{_datadir}/%{name}-packages/pkginfo
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
%{_bindir}/xemacs-nox.dmp
%endif
%attr(755,root,root) %{_bindir}/gnuserv-nox
