%global _tag v2.1.0
%global _ocfroot /usr/lib/ocf
Name: resource-agents-paf
Version: 2.1.0
Release: 1
Summary: PostgreSQL resource agent for Pacemaker
License: PostgreSQL
Group: Applications/Databases
Url: http://dalibo.github.io/PAF/

Source0: https://github.com/dalibo/PAF/releases/download/%{_tag}/PAF-%{_tag}.tgz
BuildArch: noarch
#BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: resource-agents perl perl-Module-Build
Provides: resource-agents-paf = %{version}

%description
PostgreSQL resource agent for Pacemaker

%prep
%setup -n PAF-%{_tag}

%build
perl Build.PL --destdir "%{buildroot}" --install_path bindoc=%{_mandir}/man1 --install_path libdoc=%{_mandir}/man3
perl Build

%install
./Build install
rm -f "%{buildroot}"/usr/local/lib64/perl5/auto/PAF/.packlist

%files
%defattr(-,root,root,0755)
%doc README.md 
%license LICENSE
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*
%{_ocfroot}/resource.d/heartbeat/pgsqlms
%{_ocfroot}/lib/heartbeat/OCF_ReturnCodes.pm
%{_ocfroot}/lib/heartbeat/OCF_Directories.pm
%{_ocfroot}/lib/heartbeat/OCF_Functions.pm
%{_datadir}/resource-agents/ocft/configs/pgsqlms

%changelog
* Fri Dec 23 2016 Jehan-Guillaume de Rorthais <jgdr@dalibo.com> - 2.1.0-1
- 2.1.0 major release

* Sat Dec 17 2016 Jehan-Guillaume de Rorthais <jgdr@dalibo.com> - 2.1rc2-1
- 2.1_rc2 beta release

* Sun Dec 11 2016 Jehan-Guillaume de Rorthais <jgdr@dalibo.com> - 2.1rc1-1
- 2.1_rc1 beta release

* Sun Dec 04 2016 Jehan-Guillaume de Rorthais <jgdr@dalibo.com> - 2.1beta1-1
- 2.1_beta1 beta release

* Fri Sep 16 2016 Jehan-Guillaume de Rorthais <jgdr@dalibo.com> - 2.0.0-1
- 2.0.0 major release

* Wed Aug 03 2016 Jehan-Guillaume de Rorthais <jgdr@dalibo.com> - 2.0rc1-1
- 2.0_rc1 first release candidate

* Fri Jul 1 2016 Jehan-Guillaume de Rorthais <jgdr@dalibo.com> - 2.0beta2-1
- 2.0_beta2 beta release

* Wed Jun 15 2016 Jehan-Guillaume de Rorthais <jgdr@dalibo.com> - 2.0beta1-1
- 2.0_beta1 beta release

* Wed Apr 27 2016 Jehan-Guillaume de Rorthais <jgdr@dalibo.com> - 1.0.1-1
- 1.0.1 minor release

* Wed Mar 02 2016 Jehan-Guillaume de Rorthais <jgdr@dalibo.com> 1.0.0-1
- Official 1.0.0 release

* Tue Mar 01 2016 Jehan-Guillaume de Rorthais <jgdr@dalibo.com> 0.99.0-1
- Initial version

