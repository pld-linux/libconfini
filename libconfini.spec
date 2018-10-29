Summary:	simple INI parsing library
Summary(pl.UTF-8):	prosta biblioteka analizy plików INI
Name:		libconfini
Version:	1.8.0
Release:	1
License:	GPL v3
Group:		Libraries
Source0:	https://github.com/madmurphy/libconfini/archive/%{version}.tar.gz
# Source0-md5:	fa19287c403cf760d4a2f945e520fa14
URL:		https://madmurphy.github.io/libconfini/html/index.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libconfini is the ultimate and most consistent INI file parser library
written in C. It focuses on standardization and parsing exactness and
is at ease with almost every type of file containing key/value pairs.

The library is fast and suitable for embedded systems. Its algorithms
are written from scratch and do not depend on any external library,
except for the C standard headers stdio.h, stdlib.h and stdint.h.

Rather than storing the parsed data, libconfini gives the developer
the freedom to choose what to do with them through a custom callback
invoked for each INI node read. The API has been designed to be
powerful, flexible and simple to use.

With libconfini you will find in INI files the same serialization
power you would normally find in other heavily structured formats
(such as JXON, YAML, TOML), but with the advantage of using the most
human-readable configuration format ever invented (thanks to their
informal status, INI files are indeed more fluid and human-readable
than formats explicitly designed with this purpose, such as YAML and
TOML).

%description -l pl.UTF-8
libconfini to najlepsza i najbardziej spójna biblioteka analizatorów
plików INI napisana w języku C. Skupia się ona na standaryzacji i
analizie dokładności i jest łatwa w prawie każdym typie pliku
zawierającego pary klucz / wartość.

Biblioteka jest szybka i odpowiednia dla systemów wbudowanych. Jego
algorytmy są napisane od podstaw i nie zależą od żadnej zewnętrznej
biblioteki, z wyjątkiem standardowych nagłówków C stdio.h, stdlib.h i
stdint.h.

Zamiast przechowywać przeanalizowane dane, libconfini daje
programistom swobodę wyboru, co z nimi zrobić za pomocą
niestandardowego wywołania zwrotnego wywoływanego dla każdego
czytanego węzła INI. Interfejs API został zaprojektowany tak, aby był
wydajny, elastyczny i prosty w użyciu.

Z libconfini znajdziesz w plikach INI tę samą moc serializacji, jaką
zwykle można znaleźć w innych silnie ustrukturyzowanych formatach
(takich jak JXON, YAML, TOML), ale z zaletą użycia najbardziej
czytelnego formatu konfiguracji, jaki kiedykolwiek wymyślono (dzięki
ich status nieformalny, pliki INI są rzeczywiście bardziej płynne i
czytelne dla człowieka niż formaty wyraźnie zaprojektowane w tym celu,
takie jak YAML i TOML).

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%package static
Summary:	Static %{name} library
Summary(pl.UTF-8):	Statyczna biblioteka %{name}
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static %{name} library.

%description static -l pl.UTF-8
Statyczna biblioteka %{name}.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog* MANUAL.md NEWS RATIONALE.md README* examples/ docs/html docs/manual.html
%attr(755,root,root) %{_libdir}/%{name}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/%{name}.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}.so
%{_mandir}/man3/IniDispatch.3*
%{_mandir}/man3/IniFormat.3*
%{_mandir}/man3/IniStatistics.3*
%{_mandir}/man3/confini.h.3*
%{_mandir}/man3/libconfini.3*
%{_libdir}/libconfini.la
%{_includedir}/confini.h
%{_pkgconfigdir}/libconfini-1.8.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/%{name}.a
