# This rpm is in the SVN
# $Id: darcs.spec 122076 2007-02-17 04:47:41Z nanardon $

%define name darcs
%define version 2.0.0
%define release %mkrel 1

%define withgit 1

%{?_without_git:%define withgit 0}
%{?_with_git:%define withgit 1}

Summary: David's Advanced Revision Control System
Name: %{name}
Version: %version
Release: %release
Source0: http://www.darcs.net/%{name}-%{version}.tar.gz
License: GPL
Group: Development/Other
Url: http://www.darcs.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: ghc
BuildRequires: zlib-devel
BuildRequires: openssl-devel
BuildRequires: ncurses-devel
BuildRequires: latex2html tex4ht hevea
%if %withgit
BuildRequires: git-devel
%endif

%description
Darcs is a revision control system, along the lines of CVS
or arch. That means that it keeps track of various revisions
and branches of your project, allows for changes to
propogate from one branch to another. Darcs is intended to
be an ``advanced'' revision control system. Darcs has two
particularly distinctive features which differ from other
revision control systems: 1) each copy of the source is a
fully functional branch, and 2) underlying darcs is a
consistent and powerful theory of patches.

%package server
Summary: David's advanced revision control system Server
Group: Development/Other
Requires: webserver

%description server
Darcs is a revision control system, along the lines of CVS
or arch. That means that it keeps track of various revisions
and branches of your project, allows for changes to
propogate from one branch to another. Darcs is intended to
be an ``advanced'' revision control system. Darcs has two
particularly distinctive features which differ from other
revision control systems: 1) each copy of the source is a
fully functional branch, and 2) underlying darcs is a
consistent and powerful theory of patches.

This package contains the darcs cgi server program.

%prep
%setup -q

%build
%configure \
    --with-sendmail=%{_sbindir}/sendmail \
%if %withgit
    --enable-git \
    --with-git-includes=-I%{_includedir}/git/
%endif

%make all

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=%{buildroot}  installbin installserver
# yes, it is a hack
mkdir -p $RPM_BUILD_ROOT/%{_localstatedir}/www/
mv -f $RPM_BUILD_ROOT/%{_libdir}/cgi-bin $RPM_BUILD_ROOT/%{_localstatedir}/www/cgi

%check
PATH="$PWD:$PATH" make check

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS doc/manual 
%config(noreplace) %{_sysconfdir}/bash_completion.d/darcs
%{_bindir}/darcs
%{_mandir}/man1/darcs*

%files server
%defattr(-,root,root,-)
%{_localstatedir}/www/cgi/*
%config(noreplace) %{_sysconfdir}/darcs
%{_datadir}/darcs



