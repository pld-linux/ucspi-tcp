#
# Conditional build:
%bcond_without	mysql		# build without mysql support
#
Summary:	Transport Control Protocol Superserver
Summary(pl):	Superserwer Transport Control Protocol
Name:		ucspi-tcp
Version:	0.88
Release:	5.2
Group:		Networking/Daemons
License:	DJB http://cr.yp.to/distributors.html
Source0:	http://cr.yp.to/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	39b619147db54687c4a583a7a94c9163
Source1:	ftp://ftp.innominate.org/pub/pape/djb/%{name}-%{version}-man.tar.gz
# Source1-md5:	693be34da89cd5244cef8ae30b4dc6a4
Patch0:		%{name}-%{version}-mysql.patch.pld
Patch1:		%{name}-glibc.patch
URL:		http://cr.yp.to/ucspi-tcp.html
%{?with_mysql:BuildRequires:	mysql-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UNIX Client/Server Program Interface - something like inetd with
add-ons.

%description -l pl
UNIX Client/Server Program Interface - co¶ w rodzaju superserwera
inetd z ma³ymi dodatkami.

%prep
%setup -q
%{?with_mysql:%patch0}
%patch1
echo %{__cc} %{rpmcflags} "-I/usr/include/mysql" >conf-cc
echo /usr >conf-home

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

tar zxf %{SOURCE1}

install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_mandir}/man{1,3,5}}

install	addcr				$RPM_BUILD_ROOT%{_bindir}
install	argv0				$RPM_BUILD_ROOT%{_bindir}
install	auto-str			$RPM_BUILD_ROOT%{_bindir}
install	date@				$RPM_BUILD_ROOT%{_bindir}
install	delcr				$RPM_BUILD_ROOT%{_bindir}
install	finger@				$RPM_BUILD_ROOT%{_bindir}
install	fixcrio				$RPM_BUILD_ROOT%{_bindir}
install	http@				$RPM_BUILD_ROOT%{_bindir}
install	mconnect			$RPM_BUILD_ROOT%{_bindir}
install	mconnect-io			$RPM_BUILD_ROOT%{_bindir}
install rblsmtpd			$RPM_BUILD_ROOT%{_bindir}
install	recordio			$RPM_BUILD_ROOT%{_bindir}
install	rts				$RPM_BUILD_ROOT%{_bindir}
install	tcpcat				$RPM_BUILD_ROOT%{_bindir}
install	tcpclient			$RPM_BUILD_ROOT%{_bindir}
install	tcprules			$RPM_BUILD_ROOT%{_bindir}
install	tcprulescheck			$RPM_BUILD_ROOT%{_bindir}
install	tcpserver			$RPM_BUILD_ROOT%{_bindir}
install	who@				$RPM_BUILD_ROOT%{_bindir}

install	./%{name}-%{version}-man/*.1		$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CHANGES,README,SYSDEPS,TARGETS,TODO,VERSION}
%{_mandir}/man1/*
%attr(755,root,root) %{_bindir}/*
