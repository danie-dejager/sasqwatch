%define __spec_install_post %{nil}
%define debug_package %{nil}

Summary:   A modern take on the classic watch command for Linux
Name:      sasqwatch
Version:   0.2.6
Release:   1
License:   MIT
URL:       https://github.com/danie-dejager/sasqwatch
Source0:   sasqwatch-%{version}-dist.tar.gz


BuildRequires: golang
BuildRequires: git
BuildRequires: upx
Requires:      procps-ng

%description
Sasqwatch is a modern take on the classic watch command for Linux. It periodically executes a command and displays the output in a clear and concise manner.

%prep
%setup -q -n sasqwatch
go mod vendor

%build
GO111MODULE=on CGO_ENABLED=0 go build \
    -mod=vendor \
    -ldflags="-s -w -X 'github.com/fabio42/sasqwatch/cmd.Version=%{version}'" \
    -o %{name}
strip %{name}
upx %{name}

%install
%{__install} -Dm755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Mon Sep 8 2025 Danie de Jager <danie.dejager@gmail.com> - 0.2.6-1
* Fri Jun 13 2025 Danie de Jager <danie.dejager@gmail.com> - 0.2.5-7
* Fri Dec 20 2024 Danie de Jager <danie.dejager@gmail.com> - 0.2.5-6
* Mon Sep 30 2024 Danie de Jager <danie.dejager@gmail.com> - 0.2.5-5
* Mon Jun 10 2024 Danie de Jager <danie.dejager@gmail.com> - 0.2.5-4
* Fri Jul 28 2023 Danie de Jager <danie.dejager@gmail.com> - 0.2.5-2
- Improved printing of version information
* Tue Jun 20 2023 Danie de Jager <danie.dejager@gmail.com> - 0.2.5-1
- Initial package release
