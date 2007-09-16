Summary:	Client for Vattghern mud game
Summary(pl.UTF-8):	Klient dla muda Vattghern
Name:		gMUDvattix
Version:	0.5.3
Release:	1
License:	GPL v2+
Group:		Applications/Games
Source0:	http://www.vattghern.pl/pliki/%{name}-%{version}.tgz
# Source0-md5:	5a3f04080d8001e73e15353a06be5edc
URL:		http://www.vattghern.pl/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is offcial client for Vattghern mud game.

%description -l pl.UTF-8
Jest to oficjalny klient dla gry mudowej Vattghern.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO doc/gmudix.txt
%attr(755,root,root) %{_bindir}/%{name}
