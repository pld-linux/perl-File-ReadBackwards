#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	ReadBackwards
Summary:	File::ReadBackwards - read a file backwards by lines
Summary(pl):	File::ReadBackwards - czytanie pliku od koñca, linia po linii
Name:		perl-File-ReadBackwards
Version:	1.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	48166c04fd3c0c2843a098c6bb289dec
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::ReadBackwards reads a file backwards line by line. It is simple
to use, memory efficient and fast.  It supports both an object and a
tied handle interface.

%description -l pl
File::ReadBackwards czyta plik od koñca, linia po linii. Jest prosty
w u¿yciu, wydajny pod wzglêdem zajêto¶ci pamiêci i szybki. Obs³uguje
zarówno interfejs obiektowy, jak i dowi±zane (przez tie()) uchwyty.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
