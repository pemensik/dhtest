#%%global gittag 3041d10
#%%global snapinfo 20180306git%{gittag}
%global branch master
%global gittag v%{version}

Name:		dhtest
Version:	1.5
Release:	2%{?snapinfo:.%{snapinfo}}%{?dist}
Summary:	A DHCP client simulation on linux

License:	GPLv2
URL:		https://github.com/saravana815/dhtest
Source0:	https://github.com/saravana815/dhtest/archive/%{gittag}/%{name}-%{version}.tar.gz

BuildRequires:	gcc

%description
It can simulate multiple DHCP clients behind a network device.
It can help in testing the DHCP servers or in testing switch/router
by loading the device with multiple DHCP clients.

%prep
%autosetup -n %{name}-%{version}
#sed -e 's,^#!/usr/bin/env python,#!/usr/bin/python,' -i dhscript.py

%build
%make_build CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"


%install
mkdir -p %{buildroot}%{_bindir}
%{__install} -m 0755 dhtest %{buildroot}%{_bindir}/dhtest

%check
# run dhscript.py here once it can run without special setup
# or dhcp server is configured

%files
%doc README.txt
%license LICENSE
%{_bindir}/dhtest

%changelog
* Sun Dec 15 2019 Petr Menšík <pemensik@redhat.com> - 1.5-2
- Add license

* Thu Mar 15 2018 Petr Menšík <pemensik@redhat.com> - 1.5-1
- Initial package

