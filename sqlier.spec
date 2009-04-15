%define		rel	0.2
Summary:	SQLIer - an SQL Injection vulnerable URL prober
Name:		sqlier
Version:	0.8
Release:	0.b.%{rel}
License:	BSD
Group:		Applications
Source0:	http://bcable.net/archive.php?%{name}-%{version}b.sh
# Source0-md5:	40702eb5397dfd4134ad7761a15a5e88
Patch0:		%{name}-bashism.patch
URL:		http://bcable.net/project.php?sqlier
Requires:	awk
Requires:	python
Requires:	wget
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SQLIer takes an SQL Injection vulnerable URL and attempts to determine
all the necessary information to build and exploit an SQL Injection
hole by itself, requiring no user interaction at all (unless it can't
guess the table/field names correctly). By doing so, SQLIer can build
a UNION SELECT query designed to brute force passwords out of the
database. This script also does not use quotes in the exploit to
operate, meaning it will work for a wider range of sites.

An 8 character password (containing any character from decimal ASCII
code 1-127) takes approximately 1 minute to crack.

%prep
%setup -qcT
cp %{SOURCE0} %{name}.sh
%patch0 -p0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install %{name}.sh $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sqlier
