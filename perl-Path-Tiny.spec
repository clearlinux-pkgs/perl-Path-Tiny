#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Path-Tiny
Version  : 0.106
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Path-Tiny-0.106.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Path-Tiny-0.106.tar.gz
Summary  : 'File path utility'
Group    : Development/Tools
License  : Apache-2.0
Requires: perl-Path-Tiny-license
Requires: perl-Path-Tiny-man
BuildRequires : buildreq-cpan

%description
NAME
Path::Tiny - File path utility
VERSION
version 0.106
SYNOPSIS
use Path::Tiny;

%package license
Summary: license components for the perl-Path-Tiny package.
Group: Default

%description license
license components for the perl-Path-Tiny package.


%package man
Summary: man components for the perl-Path-Tiny package.
Group: Default

%description man
man components for the perl-Path-Tiny package.


%prep
%setup -q -n Path-Tiny-0.106

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/perl-Path-Tiny
cp LICENSE %{buildroot}/usr/share/doc/perl-Path-Tiny/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/Path/Tiny.pm

%files license
%defattr(-,root,root,-)
/usr/share/doc/perl-Path-Tiny/LICENSE

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/Path::Tiny.3
