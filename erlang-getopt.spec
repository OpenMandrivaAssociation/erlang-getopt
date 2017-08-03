%global realname getopt
%global upstream jcomellas
# Technically, we're noarch; but erlang whose directories we install into is not.
%global debug_package %{nil}


Name:		erlang-%{realname}
Version:	0.8.2
Release:	1
Summary:	Erlang module to parse command line arguments using the GNU getopt syntax
Group:		Development/Erlang
License:	BSD
URL:		http://github.com/%{upstream}/%{realname}
Source0:	https://github.com/%{upstream}/%{realname}/archive/v%{version}/%{realname}-%{version}.tar.gz
Patch1:		getopt-0001-Fix-edoc-compilation.patch
BuildRequires:	erlang-rebar
Requires:	erlang-erts%{?_isa} >= R13B
Requires:	erlang-stdlib%{?_isa} >= R13B


%description
Command-line parsing module that uses a syntax similar to that of GNU getopt.


%prep
%setup -q -n %{realname}-%{version}
chmod 0644 examples/*.escript
%patch1 -p1 -b .fix_edoc


%build
%{erlang_compile}


%install
%{erlang_install}


%check
# BEWARE rebar needs bootstrapped getopt in case of an API change
%{erlang_test}


%files
%license LICENSE.txt
%doc README.md examples/
%{erlang_appdir}/



%changelog
* Tue Jun 28 2016 pterjan <pterjan> 0.8.2-6.mga6
+ Revision: 1038024
- Rebuild to fix non-bootstrap rebar

* Thu Jun 16 2016 tv <tv> 0.8.2-5.mga6
+ Revision: 1021684
- use %%license
- use erlan macros

* Fri May 06 2016 neoclust <neoclust> 0.8.2-4.mga6
+ Revision: 1009755
- Rebuild post boostrap
- imported package erlang-getopt

