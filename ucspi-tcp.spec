Summary:     ucspi-tcp
Summary(pl): ucspi-tcp
Name:        ucspi-tcp
Version:     0.84
Release:     1
Group:       Networking/Daemons
Group(pl):   Sieciowe/Serwery
Copyright:   GPL
URL:         http://pobox.com/~djb/ucspi-tcp.html
Source:      %{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UNIX Client/Server Program Interface

%description -l pl
UNIX Client/Server Program Interface

%prep
%setup -q
echo gcc $RPM_OPT_FLAGS >conf-cc
echo /usr >conf-home

%build
make 

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_mandir}/man{1,3,5}}

install	addcr				$RPM_BUILD_ROOT%{_bindir}
install	argv0				$RPM_BUILD_ROOT%{_bindir}
install	auto-str			$RPM_BUILD_ROOT%{_bindir}
install	date@				$RPM_BUILD_ROOT%{_bindir}
install	delcr				$RPM_BUILD_ROOT%{_bindir}
install	finger@				$RPM_BUILD_ROOT%{_bindir}
install	fixcr				$RPM_BUILD_ROOT%{_bindir}
install	http@				$RPM_BUILD_ROOT%{_bindir}
install	mconnect			$RPM_BUILD_ROOT%{_bindir}
install	mconnect-io			$RPM_BUILD_ROOT%{_bindir}
install	recordio			$RPM_BUILD_ROOT%{_bindir}
install	rts				$RPM_BUILD_ROOT%{_bindir}
install	tcpcat				$RPM_BUILD_ROOT%{_bindir}
install	tcpclient			$RPM_BUILD_ROOT%{_bindir}
install	tcprules			$RPM_BUILD_ROOT%{_bindir}
install	tcprulescheck			$RPM_BUILD_ROOT%{_bindir}
install	tcpserver			$RPM_BUILD_ROOT%{_sbindir}
install	who@				$RPM_BUILD_ROOT%{_bindir}

install	*.1				$RPM_BUILD_ROOT%{_mandir}/man1
install	*.3				$RPM_BUILD_ROOT%{_mandir}/man3
install *.5				$RPM_BUILD_ROOT%{_mandir}/man5

gzip -9nf {BLURB,CHANGES,README,SYSDEPS,TARGETS,TCP,THANKS,TODO} \
          {UCSPI,VERSION,$RPM_BUILD_ROOT%{_mandir}/man{1,3,5}/*}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {BLURB,CHANGES,README,SYSDEPS,TARGETS,TCP,THANKS,TODO,UCSPI,VERSION}.gz
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_mandir}/man5/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
