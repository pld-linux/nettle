#
# Conditional build:
%bcond_without	static_libs	# static libraries

Summary:	Nettle - a cryptographic library
Summary(pl.UTF-8):	Nettle - biblioteka kryptograficzna
Name:		nettle
Version:	3.10.1
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://www.lysator.liu.se/~nisse/archive/%{name}-%{version}.tar.gz
# Source0-md5:	c3dc1729cfa65fcabe2023dfbff60beb
Patch0:		%{name}-info.patch
URL:		http://www.lysator.liu.se/~nisse/nettle/
BuildRequires:	ghostscript
BuildRequires:	gmp-devel >= 6.1
BuildRequires:	m4
BuildRequires:	rpmbuild(macros) >= 1.527
BuildRequires:	tetex-dvips
BuildRequires:	texinfo-texi2dvi
Requires:	gmp >= 6.1
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
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki nettle
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for nettle library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki nettle.

%package static
Summary:	Static nettle library
Summary(pl.UTF-8):	Statyczna biblioteka nettle
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static nettle library.

%description static -l pl.UTF-8
Statyczna biblioteka nettle.

%package progs
Summary:	nettle utility programs
Summary(pl.UTF-8):	Narzędzia wykorzystujące bibliotekę nettle
Group:		Applications/Crypto
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description progs
This package contains utility programs that use nettle library.

%description progs -l pl.UTF-8
Kilka przykładowych narzędzi wykorzystujących bibliotekę
nettle.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--enable-shared \
	%{__enable_disable static_libs static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libhogweed.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libhogweed.so.6
%attr(755,root,root) %{_libdir}/libnettle.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libnettle.so.8

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhogweed.so
%attr(755,root,root) %{_libdir}/libnettle.so
%{_includedir}/nettle
%{_pkgconfigdir}/hogweed.pc
%{_pkgconfigdir}/nettle.pc
%{_infodir}/nettle.info*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libhogweed.a
%{_libdir}/libnettle.a
%endif

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nettle-hash
%attr(755,root,root) %{_bindir}/nettle-lfib-stream
%attr(755,root,root) %{_bindir}/nettle-pbkdf2
%attr(755,root,root) %{_bindir}/pkcs1-conv
%attr(755,root,root) %{_bindir}/sexp-conv
