%define modname	PPI
%define modver 1.291

Summary:	Parse, Analyze and Manipulate Perl without perl
Name:		perl-%{modname}
Version:	%{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://github.com/Perl-Critic/PPI
Source0:	https://cpan.metacpan.org/authors/id/M/MI/MITHALDU/PPI-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Clone)
BuildRequires:	perl(File::Remove)
BuildRequires:	perl(IO::String)
BuildRequires:	perl(IO::Stringy)
BuildRequires:	perl(List::Util)       >= 1.200.0
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(Params::Util)
BuildRequires:	perl(Task::Weaken)
BuildRequires:	perl(Test::ClassAPI)
BuildRequires:	perl(Test::More)       >= 0.860.0
BuildRequires:	perl(Test::NoWarnings)
BuildRequires:	perl(Test::SubCalls)
BuildRequires:	perl(Test::Object)
BuildRequires:	perl(Class::Inspector)

%description
PPI is a Perl document parser.

%prep
%setup -qn %{modname}-%{modver}
chmod 644 Changes
find lib -name '*.pm' | xargs chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/PPI
%{perl_vendorlib}/PPI.pm
%{_mandir}/man3/*
