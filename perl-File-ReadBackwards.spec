#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	ReadBackwards
Summary:	File::ReadBackwards -- Read a file backwards by lines
Summary(pl):	File::ReadBackwards -- Czytaj plik od ko�ca, linia po linii
Name:		perl-File-ReadBackwards
Version:	0.99
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	697b21b397a4a37e5c1d0b4abcadc1e4
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::ReadBackwards reads a file backwards line by line. It is simple
to use, memory efficient and fast. It supports both an object and a tied
handle interface.

%description -l pl
File::ReadBackwards czyta plik od ko�ca, linia po linii.  Jest prosty
w u�yciu, wydajny pod wzgl�dem zaj�to�ci pami�ci i szybki.  Obs�uguje
zar�wno interfejs obiektowy, jak i dowi�zane (przez tie()) uchwyty.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
