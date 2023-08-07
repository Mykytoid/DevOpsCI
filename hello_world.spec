Name:           hello_world
Version:        1.0
Release:        1%{?dist}
Summary:        A simple Python script that prints "Hello, World!"

URL:            https://github.com/Mykytoid/DevOpsCI.git
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

%description
This package contains a simple Python script that prints "Hello, World!" when executed.

%prep
%autosetup -n %{name}-%{version}

%build

%install
mkdir -p %{buildroot}/usr/bin
install -m 755 hello_world.py %{buildroot}/usr/bin/hello_world.py

%files
/usr/bin/hello_world.py
