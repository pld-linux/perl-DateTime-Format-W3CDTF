#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DateTime
%define	pnam	Format-W3CDTF
Summary:	DateTime::Format::W3CDTF - Parse and format W3CDTF datetime strings
Summary(pl.UTF-8):	DateTime::Format::W3CDTF - analizowanie i formatowanie łańcuchów dat W3CDTF
Name:		perl-DateTime-Format-W3CDTF
Version:	0.06
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DateTime/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7eb2a90b78e7e2232eddbd6dd6758a23
URL:		http://search.cpan.org/dist/DateTime-Format-W3CDTF/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-DateTime
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module understands the W3CDTF date/time format, an ISO 8601
profile, defined at <http://www.w3.org/TR/NOTE-datetime>. This format
as the native date format of RSS 1.0.

It can be used to parse these formats in order to create the
appropriate objects.

%description -l pl.UTF-8
Ten moduł rozumie format daty/czasu W3CDTF w profilu ISO 8601,
zdefiniowany w <http://www.w3.org/TR/NOTE-datetime>. Jest to natywny
format daty w RSS 1.0.

Moduł można wykorzystać do analizy tych formatów w celu utworzenia
odpowiednich obiektów.

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
%doc Changes README
%{perl_vendorlib}/DateTime/Format/*.pm
%{_mandir}/man3/*
