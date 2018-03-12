#%%global gittag 3041d10
#%%global snapinfo 20180306git%{gittag}
%global branch master

Name:		dhtest
Version:	0
Release:	1%{?snapinfo:.%{snapinfo}}%{?dist}
Summary:	A DHCP client simulation on linux

License:	GPLv2
URL:		https://github.com/saravana815/dhtest
Source0:	https://github.com/saravana815/dhtest/archive/%{branch}.zip

BuildRequires:	gcc

%description
It can simulates multiple DHCP clients behind a network device. It can help in testing the DHCP servers or in testing switch/router by loading the device with multiple DHCP clients.

%prep
%setup -q -n %{name}-%{branch}
#sed -e 's,^#!/usr/bin/env python,#!/usr/bin/python,' -i dhscript.py

%build
%make_build CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"


%install
mkdir -p %{buildroot}%{_bindir}
%{__install} -m 0755 dhtest %{buildroot}%{_bindir}/dhtest
#%{__install} -m 0755 dhscript.py %{buildroot}%{_bindir}/dhtest-script

%files
%doc README.txt
%{_bindir}/dhtest

%changelog
* Tue Mar 06 2018 Petr Menšík <pemensik@redhat.com> - 0-1.20180306git3041d10
- Initial package


