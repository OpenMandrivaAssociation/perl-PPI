%define upstream_name	 PPI
%define upstream_version 1.215

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Parse, Analyze and Manipulate Perl without perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/PPI/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Clone)
BuildRequires:	perl(File::Remove)
BuildRequires:  perl(IO::String)
BuildRequires:	perl(IO::Stringy)
BuildRequires:	perl(List::Util)       >= 1.200.0
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(Params::Util)
BuildRequires:  perl(Task::Weaken)
BuildRequires:	perl(Test::ClassAPI)
BuildRequires:	perl(Test::More)       >= 0.860.0
BuildRequires:	perl(Test::NoWarnings)
BuildRequires:	perl(Test::SubCalls)
BuildRequires:  perl(Test::Object)
BuildArch:	noarch

%description
PPI is a Perl document parser.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
chmod 644 Changes
find lib -name '*.pm' | xargs chmod 644

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/PPI
%{perl_vendorlib}/PPI.pm
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.215.0-4mdv2012.0
+ Revision: 765603
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1.215.0-2
+ Revision: 676634
- rebuild

* Thu Mar 10 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.215.0-1
+ Revision: 643457
- update to new version 1.215

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.213.0-1mdv2011.0
+ Revision: 552487
- update to 1.213

* Sat Jun 19 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.212.0-1mdv2010.1
+ Revision: 548334
- new version

* Tue Feb 16 2010 Jérôme Quelin <jquelin@mandriva.org> 1.210.0-1mdv2010.1
+ Revision: 506749
- update to 1.210

* Mon Feb 08 2010 Jérôme Quelin <jquelin@mandriva.org> 1.209.0-1mdv2010.1
+ Revision: 502108
- update to 1.209

* Fri Jan 15 2010 Jérôme Quelin <jquelin@mandriva.org> 1.208.0-1mdv2010.1
+ Revision: 491632
- update to 1.208

* Tue Aug 11 2009 Jérôme Quelin <jquelin@mandriva.org> 1.206.0-1mdv2010.0
+ Revision: 414982
- update to 1.206

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 1.205.0-1mdv2010.0
+ Revision: 408829
- adding missing buildrequires:
- adding missing buildrequires:
- update to 1.205, using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.203-2mdv2009.0
+ Revision: 268704
- rebuild early 2009.0 package (before pixel changes)

* Sat May 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.203-1mdv2009.0
+ Revision: 208374
- update to new version 1.203

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Nov 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.201-1mdv2008.1
+ Revision: 104567
- update to new version 1.201


* Wed Nov 15 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.118-1mdv2007.0
+ Revision: 84456
- new version

* Tue Oct 17 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.115-2mdv2007.1
+ Revision: 65731
- Add BuildRequires
- import perl-PPI-1.115-1mdv2007.0

* Wed Aug 30 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.115-1mdv2007.0
- new release

* Thu May 18 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.113-1mdk
- New release 1.113
- spec cleanup
- better source URL
- better buildrequires syntax
- fix directory ownership

* Mon Jan 30 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.110-1mdk
- 1.110

* Fri Dec 16 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.108-1mdk
- 1.108

* Mon Dec 12 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.106-1mdk
- 1.106

* Wed Nov 30 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.104-1mdk
- 1.104

* Tue Oct 18 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.103-1mdk
- 1.103
- Requires perl with recent Storable >= 2.15

* Sat Aug 20 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.003-1mdk
- Initial MDV release.

