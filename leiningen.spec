Name:           leiningen
Version:        2.9.4
Release:        1%{?dist}
Summary:        Automation for Clojure projects
License:        EPL-1.0
URL:            https://leiningen.org/
Source0:        https://github.com/technomancy/leiningen/releases/download/%{version}/leiningen-%{version}-standalone.zip
# Following files are taken from the upstream repo in the `doc` and `bin` subfolders:
Source1:        lein-pkg
Source2:        bash_completion.bash
Source3:        zsh_completion.zsh
Source4:        lein.1

BuildArch:      noarch

BuildRequires:  fdupes
BuildRequires:  unzip
Requires:       clojure >= 1.10.0
Requires:       java >= 1.8.0

%description
Working on Clojure projects with tools designed for Java can be an
exercise in frustration. With Leiningen, builds can be describe with
Clojure. Leiningen handles fetching dependencies, running tests,
packaging projects and can be extended with a number of plugins.

%prep

%build

%install
mkdir -p %{buildroot}%{_datadir}/java/
install -m 0644 -D %{SOURCE0} %{buildroot}%{_javadir}/%{name}.jar
install -m 0755 -D %{SOURCE1} %{buildroot}%{_bindir}/lein
install -m 0644 -D %{SOURCE2} %{buildroot}%{_datadir}/bash-completion/completions/lein
install -m 0644 -D %{SOURCE3} %{buildroot}%{_sysconfdir}/zsh_completion.d/_lein
install -m 0644 -D %{SOURCE4} %{buildroot}%{_mandir}/man1/lein.1

%fdupes %{buildroot}/%{_prefix}

%check 
LEIN_ROOT=y sh bin/lein-pkg test

%files
%license LICENSE
%{_bindir}/lein
%{_mandir}/man1/lein*
%{_datadir}/bash-completion/completions/lein
%{_sysconfdir}/zsh_completion.d
%{_datadir}/java/leiningen-%{version}-standalone.jar

%changelog
* Tue Sep 15 2020 Breno Brand Fernandes <brandfbb@gmail.com> - 2.9.4-1
