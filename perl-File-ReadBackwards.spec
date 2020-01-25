#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	File
%define		pnam	ReadBackwards
Summary:	File::ReadBackwards - read a file backwards by lines
Summary(pl.UTF-8):	File::ReadBackwards - czytanie pliku od końca, linia po linii
Name:		perl-File-ReadBackwards
Version:	1.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/File/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	613d9d02de6c1d86d5fa5b8816a6b214
URL:		http://search.cpan.org/dist/File-ReadBackwards/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::ReadBackwards reads a file backwards line by line. It is simple
to use, memory efficient and fast. It supports both an object and a
tied handle interface.

%description -l pl.UTF-8
File::ReadBackwards czyta plik od końca, linia po linii. Jest prosty w
użyciu, wydajny pod względem zajętości pamięci i szybki. Obsługuje
zarówno interfejs obiektowy, jak i dowiązane (przez tie()) uchwyty.

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
%{perl_vendorlib}/File/ReadBackwards.pm
%{_mandir}/man3/File::ReadBackwards.3pm*
