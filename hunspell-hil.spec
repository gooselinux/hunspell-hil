Name: hunspell-hil
Summary: Hiligaynon hunspell dictionaries
Epoch: 1
Version: 0.13
Release: 1%{?dist}
Group: Applications/Text
Source: http://borel.slu.edu/obair/%{name}-%{version}.oxt
URL: http://extensions.services.openoffice.org/project/hunspell-hil
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv3+
BuildArch: noarch

Requires: hunspell

%description
Hiligaynon hunspell dictionaries.

%prep
%setup -q -c

%build
for i in dictionaries/README_hil_PH.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/hil_PH.* $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSES-en.txt dictionaries/README_hil_PH.txt
%{_datadir}/myspell/*

%changelog
* Thu Aug 20 2009 Caolan McNamara <caolanm@redhat.com> - 1:0.13-1
- latest version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20050406-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Caolan McNamara <caolanm@redhat.com> - 0.20050406-3
- tidy spec

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20050406-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Nov 07 2008 Caolan McNamara <caolanm@redhat.com> - 0.20050406-1
- initial version
