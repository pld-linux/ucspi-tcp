#
# Conditional build:
%bcond_without	mysql		# build without mysql support
#
Summary:	Transport Control Protocol Superserver
Summary(pl.UTF-8):	Superserwer Transport Control Protocol
Name:		ucspi-tcp
Version:	0.88
Release:	7
Group:		Networking/Daemons
# http://cr.yp.to/distributors.html
License:	Public Domain
Source0:	http://cr.yp.to/ucspi-tcp/%{name}-%{version}.tar.gz
# Source0-md5:	39b619147db54687c4a583a7a94c9163
Source1:	ftp://ftp.innominate.org/pub/pape/djb/%{name}-%{version}-man.tar.gz
# Source1-md5:	693be34da89cd5244cef8ae30b4dc6a4
Source2:	daemontools-tcprules
Patch0:		%{name}-%{version}-mysql.patch.pld
Patch1:		%{name}-glibc.patch
Patch2:		http://lamer.maexotic.de/maex/creative/software/ucspi-tcp/0.88-recordio/recordio.diff
URL:		http://cr.yp.to/ucspi-tcp.html
%{?with_mysql:BuildRequires:	mysql-devel}
# make and stat from coreutils are for building tcprules
Requires:	coreutils
Requires:	make
Conflicts:	daemontools < 0.76-8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# qmail.spec uses this dir
%define 	tcprules 	/etc/tcprules.d

%description
UNIX Client/Server Program Interface - something like inetd with
add-ons.

%description -l pl.UTF-8
UNIX Client/Server Program Interface - coś w rodzaju superserwera
inetd z małymi dodatkami.

%prep
%setup -q -a1
mv ucspi-tcp-%{version}-man man
%{?with_mysql:%patch0}
%patch1 -p0
%patch2 -p1

%build
echo "%{__cc} %{rpmcflags} %{?with_mysql:-I%{_includedir}/mysql}" > conf-cc
echo "%{_prefix}" > conf-home
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_mandir}/man{1,3,5},%{tcprules}}

install addcr argv0 auto-str date@ delcr finger@ fixcrio \
	http@ mconnect mconnect-io rblsmtpd recordio rts tcpcat \
	tcpclient tcprules tcprulescheck tcpserver who@ \
	$RPM_BUILD_ROOT%{_bindir}

install man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

install %{SOURCE2} $RPM_BUILD_ROOT%{tcprules}/Makefile

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README SYSDEPS TARGETS TODO VERSION
%{tcprules}
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
