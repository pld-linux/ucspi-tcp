Summary:	Transport Control Protocol Superserver
Summary(pl):	Superserwer Transport Control Protocol
Name:		ucspi-tcp
Version:	0.88
Release:	2
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
License:	GPL
URL:		http://cr.yp.to/%{name}.html
Source0:	http://cr.yp.to/%{name}/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.innominate.org/pub/pape/djb/%{name}-%{version}-man.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UNIX Client/Server Program Interface - 
	something like inetd with add-ons.

%description -l pl
UNIX Client/Server Program Interface -
	co¶ w rodzaju superserwera inetd z ma³ymi dodatkami.

%prep
tar zxf %{SOURCE1}

%setup -q
echo %{__cc} %{rpmcflags} >conf-cc
echo /usr >conf-home

%build
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

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

install	../%{name}-%{version}-man/*.1		$RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf {CHANGES,FILES,README,SYSDEPS,TARGETS,TODO,VERSION}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CHANGES,README,SYSDEPS,TARGETS,TODO,VERSION}.gz
%{_mandir}/man1/*
%attr(755,root,root) %{_bindir}/*
