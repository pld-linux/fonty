Summary:     Fonts on Linux console
Summary(pl): Fonty na konsoli Linuxa
Name:	     fonty
Version:     1.0
Release:     1
Copyright:   GPL
Group:	     Utilities/Text
Group(pl):   Narzêdzia/Tekst
Source:	     http://qrczak.home.ml.org/programy/linux/%{name}/%{name}-%{version}.tar.gz
URL:	     http://qrczak.home.ml.org/programy/linux/fonty/
Requires:    console-tools
BuildRoot:   /tmp/%{name}-%{version}-root

%description
The Fonty package contains various fonts for Linux text console and
dynafont - a tool which allows displaying texts containing thousands of
different characters.

%description -l pl
Niniejszy pakiet zawiera ró¿ne czcionki dla konsoli tekstowej Linuxa oraz
dynafont - narzêdzie pozwalaj±ce wy¶wietlaæ teksty zawieraj±ce tysi±ce
ró¿nych znaków.

%prep
%setup -q

%build
CXXFLAGS=$RPM_OPT_FLAGS make \
	consoleprefix=/usr \
	konwertprefix=/usr \
	perl=%{_bindir}/perl \
	docdir=/usr/doc/fonty-%{version}

%install
rm -rf $RPM_BUILD_ROOT
make install \
	consoleprefix=$RPM_BUILD_ROOT/usr \
	konwertprefix=$RPM_BUILD_ROOT/usr \
	perl=%{_bindir}/perl \
	docdir=$RPM_BUILD_ROOT/usr/doc/fonty-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %lang(en) doc/en
%doc %lang(pl) doc/pl
%{_datadir}/consolefonts/*
%{_datadir}/consoletrans/*
%attr(755,root,root) %{_libdir}/konwert/aux/dynafont
%attr(755,root,root) %{_datadir}/konwert/filters/dynafont

%changelog
* Tue Jan 26 1999 Micha³ Kuratczyk <kurkens@polbox.com>
- added "Group(pl)"

* Sat Nov 28 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0-1]
- simplification in %files,
- removed "Prereq: perl".

* Fri Sep 20 1998 Marcin 'Qrczak' Kowalczyk <qrczak@knm.org.pl>
- First release in RPM
