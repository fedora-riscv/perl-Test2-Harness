Name:           perl-Test2-Harness
Version:        0.001080
Release:        1%{?dist}
Summary:        Test2 Harness designed for the Test2 event system
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Test2-Harness
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Test2-Harness-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.9
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::UUID) >= 1.148
BuildRequires:  perl(Devel::Cover)
# Email::Stuffer 0.016 not used at tests
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path) >= 2.11
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long) >= 2.36
BuildRequires:  perl(goto::file) >= 0.005
# HTTP::Tiny 0.070 not used at tests
BuildRequires:  perl(Importer) >= 0.024
BuildRequires:  perl(IO::Compress::Bzip2)
BuildRequires:  perl(IO::Compress::Gzip)
BuildRequires:  perl(IO::Handle) >= 1.27
BuildRequires:  perl(IO::Uncompress::Bunzip2)
BuildRequires:  perl(IO::Uncompress::Gunzip)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Linux::Inotify2)
BuildRequires:  perl(List::Util) >= 1.45
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(parent)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Term::ANSIColor) >= 4.03
BuildRequires:  perl(Term::Table) >= 0.011
BuildRequires:  perl(Test2::API) >= 1.302133
BuildRequires:  perl(Test2::Event) >= 1.302133
BuildRequires:  perl(Test2::Formatter) >= 1.302133
BuildRequires:  perl(Test2::Hub)
BuildRequires:  perl(Test2::Plugin::Times) >= 0.000105
BuildRequires:  perl(Test2::Util) >= 1.302133
BuildRequires:  perl(Test2::Util::HashBase)
BuildRequires:  perl(Test2::Util::Table)
BuildRequires:  perl(Test2::Util::Term) >= 0.000105
BuildRequires:  perl(Test2::Util::Times)
BuildRequires:  perl(Test::Builder::Formatter) >= 1.302133
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(vars)
# Win32::Console::ANSI not used on Linux
# Tests:
BuildRequires:  perl(ok)
BuildRequires:  perl(Test2::Bundle::Extended) >= 0.000105
BuildRequires:  perl(Test2::Tools::AsyncSubtest) >= 0.000105
BuildRequires:  perl(Test2::Tools::GenTemp)
BuildRequires:  perl(Test2::Tools::Subtest) >= 0.000105
BuildRequires:  perl(Test2::V0) >= 0.000105
BuildRequires:  perl(Test::Builder) >= 1.302133
BuildRequires:  perl(Test::More) >= 1.302133
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(constant)
Suggests:       perl(Cpanel::JSON::XS)
Requires:       perl(Data::Dumper)
Requires:       perl(Data::UUID) >= 1.148
Suggests:       perl(Devel::Cover)
Suggests:       perl(Email::Stuffer) >= 0.016
Requires:       perl(Exporter)
Requires:       perl(File::Find)
Requires:       perl(File::Path) >= 2.11
Suggests:       perl(FindBin)
Requires:       perl(Getopt::Long) >= 2.36
Requires:       perl(goto::file) >= 0.005
Suggests:       perl(HTTP::Tiny) >= 0.070
Requires:       perl(Importer) >= 0.024
Requires:       perl(IO::Compress::Bzip2)
Requires:       perl(IO::Compress::Gzip)
Requires:       perl(IO::Handle) >= 1.27
Requires:       perl(IPC::Cmd)
Suggests:       perl(JSON::MaybeXS)
Requires:       perl(JSON::PP)
Suggests:       perl(Linux::Inotify2)
Requires:       perl(Module::Pluggable)
Suggests:       perl(Term::ANSIColor) >= 4.03
Requires:       perl(Term::Table) >= 0.011
Requires:       perl(Test2::API) >= 1.302133
Requires:       perl(Test2::Event) >= 1.302133
Requires:       perl(Test2::Formatter) >= 1.302133
Requires:       perl(Test2::Hub)
Requires:       perl(Test2::Plugin::Times) >= 0.000105
Requires:       perl(Test2::Util) >= 1.302133
Requires:       perl(Test2::Util::Table)
Requires:       perl(Test2::Util::Term) >= 0.000105
Requires:       perl(Test2::Util::Times)
Requires:       perl(Test::Builder::Formatter) >= 1.302133

# Filter underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Data::UUID|File::Path|Getopt::Long|Importer|IO::Handle|Term::Table|Test2::API|Test2::Formatter|Test2::Util|Test2::Util::Term)\\)$

%description
This is a test harness toolkit for Perl Test2 system. It provides a yath tool,
a command-line tool for executing the tests under the Test2 harness.

%prep
%setup -q -n Test2-Harness-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{_bindir}/yath
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Thu Aug 01 2019 Petr Pisar <ppisar@redhat.com> 0.001080-1
- Specfile autogenerated by cpanspec 1.78.
