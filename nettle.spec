Summary:	Nettle - a cryptographic library
Summary(pl.UTF-8):   Nettle - biblioteka kryptograficzna
Name:		nettle
Version:	1.14
Release:	2
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.lysator.liu.se/pub/security/lsh/%{name}-%{version}.tar.gz
# Source0-md5:	12915b53e751456689e2ec9ec15c74da
Patch0:		%{name}-info.patch
URL:		http://www.lysator.liu.se/~nisse/lsh/
BuildRequires:	gmp-devel
BuildRequires:	m4
BuildRequires:	texinfo-texi2dvi
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nettle is a cryptographic library that is designed to fit easily in
more or less any context: In crypto toolkits for object-oriented
languages (C++, Python, Pike, ...), in applications like LSH or GNUPG,
or even in kernel space. Nettle does only one thing, the low-level
crypto stuff, providing simple but general interface to it. In
particular, Nettle doesn't do algorithm selection. It doesn't do
memory allocation. It doesn't do any I/O. All these is up to
application.

%description -l pl.UTF-8
Nettle to biblioteka kryptograficzna zaprojektowana tak, aby łatwo
dało się jej użyć w prawie każdej sytuacji: w narzędziach
kryptograficznych dla języków zorientowanych obiektowo (C++, Python,
Pike...), w aplikacjach typu LSH czy GNUPG, a nawet w przestrzeni
jądra. Nettle robi tylko jedną rzecz - niskopoziomową kryptografię,
udostępniając do tego prosty, ale ogólny interfejs. Nettle nie
dokonuje żadnego wyboru algorytmu, przydzielania pamięci, czy operacji
we/wy - pozostawia to aplikacji.

%package devel
Summary:	Header files for nettle library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki nettle
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for nettle library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki nettle.

%package static
Summary:	Static nettle library
Summary(pl.UTF-8):   Statyczna biblioteka nettle
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static nettle library.

%description static -l pl.UTF-8
Statyczna biblioteka nettle.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--enable-shared

%{__make} \
	SHLIBLIBS="-lgmp"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/nettle
%{_infodir}/*.info*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
