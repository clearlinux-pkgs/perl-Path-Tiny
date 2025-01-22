#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Path-Tiny
Version  : 0.146
Release  : 45
URL      : https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Path-Tiny-0.146.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Path-Tiny-0.146.tar.gz
Summary  : 'File path utility'
Group    : Development/Tools
License  : Apache-2.0
Requires: perl-Path-Tiny-license = %{version}-%{release}
Requires: perl-Path-Tiny-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Digest::MD5)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
Path::Tiny - File path utility
VERSION
version 0.146
SYNOPSIS
use Path::Tiny;

%package dev
Summary: dev components for the perl-Path-Tiny package.
Group: Development
Provides: perl-Path-Tiny-devel = %{version}-%{release}
Requires: perl-Path-Tiny = %{version}-%{release}

%description dev
dev components for the perl-Path-Tiny package.


%package license
Summary: license components for the perl-Path-Tiny package.
Group: Default

%description license
license components for the perl-Path-Tiny package.


%package perl
Summary: perl components for the perl-Path-Tiny package.
Group: Default
Requires: perl-Path-Tiny = %{version}-%{release}

%description perl
perl components for the perl-Path-Tiny package.


%prep
%setup -q -n Path-Tiny-0.146
cd %{_builddir}/Path-Tiny-0.146
pushd ..
cp -a Path-Tiny-0.146 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Path-Tiny
cp %{_builddir}/Path-Tiny-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Path-Tiny/85e14080c483146fd022a7140831a977f7eeaac8 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Path::Tiny.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Path-Tiny/85e14080c483146fd022a7140831a977f7eeaac8

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
