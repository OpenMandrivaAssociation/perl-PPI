%define upstream_name	 PPI
%define upstream_version 1.205

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Parse, Analyze and Manipulate Perl without perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/PPI/%{upstream_name}-%{upstream_version}.tar.gz

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
BuildRoot:	    %{_tmppath}/%{name}-%{version}-%{release}

%description
PPI is a Perl document parser.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
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
