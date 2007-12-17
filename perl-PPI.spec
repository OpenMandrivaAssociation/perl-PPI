%define module	PPI
%define name	perl-%{module}
%define version	1.201
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Parse, Analyze and Manipulate Perl without perl
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/PPI/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
Requires:	perl >= 2:5.8.7-4mdk
BuildRequires:	perl >= 2:5.8.7-4mdk
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:	perl(Clone)
BuildRequires:	perl(IO::Stringy)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(Params::Util)
BuildRequires:	perl(Test::ClassAPI)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(Test::Object)
BuildArch:	    noarch

%description
PPI is a Perl document parser.

%prep
%setup -q -n %{module}-%{version}
chmod 644 Changes
find lib -name '*.pm' | xargs chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/PPI
%{perl_vendorlib}/PPI.pm
%{_mandir}/*/*



