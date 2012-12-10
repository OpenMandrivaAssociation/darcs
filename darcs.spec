#% global debug_package %{nil}
%define _cabal_setup Setup.lhs
%define _no_haddock 1
%define module darcs
Name:           %{module}
Version:        2.8.3
Release:        1
Summary:        a distributed, interactive, smart revision control system
Group:          Development/Other
License:        GPLv2+
URL:            http://hackage.haskell.org/package/%{module}
Source0:        http://hackage.haskell.org/packages/archive/%{module}/%{version}/%{module}-%{version}.tar.gz

BuildRequires:  ghc < 7.6
buildrequires:  ghc-devel < 7.6
buildrequires:  haskell-macros
buildrequires:  cabal-install
buildrequires:  pkgconfig(libcurl)
buildrequires:  pkgconfig(ncurses)

%description
Darcs is a free, open source revision control system. It is:
* Distributed: Every user has access to the full command set, removing
boundaries between server and client or committer and non-committers.
* Interactive: Darcs is easy to learn and efficient to use because it asks you
questions in response to simple commands, giving you choices in your work flow.
You can choose to record one change in a file, while ignoring another. As you
update from upstream, you can review each patch name, even the full "diff" for
interesting patches.
* Smart: Originally developed by physicist David Roundy, darcs is based on a
unique algebra of patches.
This smartness lets you respond to changing demands in ways that would
otherwise not be possible. Learn more about spontaneous branches with darcs.

%prep
%setup -q -n %{module}-%{version}

%build
cabal update
cabal install
cabal configure --prefix=%{_prefix} --libdir=%{_libdir} --disable-executable-stripping
cabal build
%_cabal_genscripts

%install
%_cabal_install
%_cabal_rpm_gen_deps
%_cabal_scriptlets

%files
%defattr(-,root,root,-)
%{_docdir}/%{module}-%{version}
%{_libdir}/%{module}-%{version}
%_cabal_rpm_deps_dir
%_cabal_haddoc_files
%{_bindir}/%{module}
%attr(644,root,root) %{_mandir}/man1/*


