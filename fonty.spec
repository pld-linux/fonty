Summary:	Fonts on Linux console
Summary(pl):	Fonty na konsoli Linuxa
Name:		fonty
Version:	1.0
Release:	4
License:	GPL
Group:		Applications/Text
Source0:	http://qrczak.ids.net.pl/programy/linux/%{name}/%{name}-%{version}.tar.gz
Source1:	iso02grf.psf.gz
URL:		http://qrczak.ids.net.pl/programy/linux/fonty/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	perl
Requires:	console-tools

%description
The Fonty package contains various fonts for Linux text console and
dynafont - a tool which allows displaying texts containing thousands
of different characters.

%description -l pl
Niniejszy pakiet zawiera ró¿ne czcionki dla konsoli tekstowej Linuxa
oraz dynafont - narzêdzie pozwalaj±ce wy¶wietlaæ teksty zawieraj±ce
tysi±ce ró¿nych znaków.

%prep
%setup -q

%build
OPTFLAGS="%{rpmcflags} %{!?debug:-fomit-frame-pointer}"
OPTFLAGS="$OPTFLAGS -fno-rtti -fno-exceptions"
%{__make} \
	CXXFLAGS="$OPTFLAGS" \
	consoleprefix=%{_prefix} \
	konwertprefix=%{_prefix} \
	perl=%{_bindir}/perl \
	docdir=%{_docdir}/%{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	consoleprefix=$RPM_BUILD_ROOT%{_prefix} \
	konwertprefix=$RPM_BUILD_ROOT%{_prefix} \
	perl=%{_bindir}/perl \
	docdir=$RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/consolefonts

rm -f doc/pl/{DO_ZROBIENIA,ZMIANY}
cp -a doc/en/TODO doc/pl/DO_ZROBIENIA
cp -a doc/en/CHANGES doc/pl/ZMIANY

gzip -9nf doc/en/* doc/pl/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %lang(en) doc/en
%doc %lang(pl) doc/pl
%{_datadir}/consolefonts/*
%attr(755,root,root) %{_libdir}/konwert/aux/dynafont
%attr(755,root,root) %{_datadir}/konwert/filters/dynafont
