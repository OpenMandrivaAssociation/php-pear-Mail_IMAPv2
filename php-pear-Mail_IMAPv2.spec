%define		_class		Mail
%define		_subclass	IMAPv2
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.2.0
Release:	10
Summary:	Provides a c-client backend for webmail
License:	PHP License
Group:		Development/PHP
URL:		https://pear.php.net/package/Mail_IMAPv2/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires:	php-imap
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
Mail_IMAPv2 provides a simplified backend for working with the
c-client (IMAP) extension. It serves as an OO wrapper for commonly
used c-client functions. It provides structure and header parsing as
well as body retrieval.

Mail_IMAPv2 may be used as a webmail backend or as a component in a
mailing list manager.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml



%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-8mdv2012.0
+ Revision: 742036
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-7
+ Revision: 679389
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-6mdv2011.0
+ Revision: 613704
- the mass rebuild of 2010.1 packages

* Wed Nov 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.0-5mdv2010.1
+ Revision: 470145
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.2.0-4mdv2010.0
+ Revision: 441275
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-3mdv2009.1
+ Revision: 322279
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-2mdv2009.0
+ Revision: 236915
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-1mdv2007.0
+ Revision: 82050
- Import php-pear-Mail_IMAPv2

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-1mdk
- 0.2.0
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-1mdk
- initial Mandriva package (PLD import)

