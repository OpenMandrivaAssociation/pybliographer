%define name pybliographer
%define version 1.2.12
%define release 4
Summary: 	A framework for working with bibliographic databases
Name:           %{name}
Version:        %{version}
Release:        %{release}
License:	GPL
Group:		Office
Url:            http://pybliographer.org/
Source: 	http://prdownloads.sourceforge.net/%name/%{name}-%{version}.tar.gz
Source1:        %{name}-16.png
Source2:        %{name}-32.png
Source3:        %{name}-48.png
Patch: pybliographer-1.2.11-icon.patch
Buildrequires:	pygtk2.0-libglade
Buildrequires:	python-bibtex
Buildrequires:	gnome-python
BuildRequires:	gnome-python-gnomevfs
Buildrequires:	gnome-python-gconf
BuildRequires:	docbook-utils
BuildRequires:  scrollkeeper
BuildRequires:  desktop-file-utils
BuildRequires:  intltool
Requires:	gnome-python
Requires:	gnome-python-gconf
Requires:	gnome-python-gnomevfs
Requires:	pygtk2.0-libglade
Requires:	python-bibtex >= 1.1.93.1
Requires(post): desktop-file-utils scrollkeeper
Requires(postun): desktop-file-utils scrollkeeper
BuildArch:	noarch

%description
Pybliographer is a tool for managing bibliographic databases. It
currently supports the following formats: 

- BibTeX (quite complete) 
- Medline (read-only) 
- Ovid files (from ovid.com) 
- Refer and EndNote (read only)
- SGML DocBook (write only) 

Pybliographer can be used for searching, editing, reformatting, etc.
In fact, it's a simple framework that provides easy to use python
classes and functions, and therefore can be extended to any usage
(generating HTML pages according to bibliographic searches, etc).

In addition to the scripting environment, a graphical GNOME interface
is available. It provides powerful editing capabilities, in addition
to a nice hierarchical search mechanism.

%prep
%setup -q
%patch -p1
rm -f pybliographic.desktop

%build
%configure2_5x
%make


%install
%makeinstall_std
rm -f %{buildroot}%_datadir/applications/mimeinfo.cache
chmod -x %{buildroot}%{_datadir}/pybliographer/*.py

%{find_lang} %{name} --with-gnome --all-name

# menu
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-Office-Publishing" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*


# icon
mkdir -p %{buildroot}%{_miconsdir}
mkdir -p %{buildroot}%{_liconsdir}
install -m 644 %{SOURCE1} %{buildroot}%{_miconsdir}/pybliographic.png
install -m 644 %{SOURCE2} %{buildroot}%{_iconsdir}/pybliographic.png
install -m 644 %{SOURCE3} %{buildroot}%{_liconsdir}/pybliographic.png

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README TODO
%{_bindir}/*
%_datadir/applications/pybliographic.desktop
%{_datadir}/mime-info/*
%{_datadir}/pixmaps/*
%{_datadir}/pybliographer
%{_iconsdir}/pybliographic.png
%{_miconsdir}/pybliographic.png
%{_liconsdir}/pybliographic.png




%changelog
* Tue Sep 15 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.2.12-2mdv2010.0
+ Revision: 441981
- rebuild

* Mon Dec 01 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1.2.12-1mdv2009.1
+ Revision: 308706
- update to new version 1.2.12

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.2.11-4mdv2009.0
+ Revision: 259402
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.2.11-3mdv2009.0
+ Revision: 247256
- rebuild
- drop old menu
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Oct 09 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.2.11-1mdv2008.1
+ Revision: 96318
- fix buildrequires
- fix desktop file
- new version
- drop patch 0


* Sat Jan 20 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.2.10-1mdv2007.0
+ Revision: 110997
- new version

* Wed Nov 01 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.2.9-3mdv2007.1
+ Revision: 74992
- fix buildrequires
- Import pybliographer

* Mon Oct 30 2006 Götz Waschk <waschk@mandriva.org> 1.2.9-2mdv2007.1
- remove xdg build dep

* Fri Jul 14 2006 Götz Waschk <waschk@mandriva.org> 1.2.9-1mdv2007.0
- new macros
- xdg menu
- New release 1.2.9

* Mon Jan 23 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.2.8-1mdk
- New release 1.2.8
- use mkrel

* Fri Oct 14 2005 Götz Waschk <waschk@mandriva.org> 1.2.7-1mdk
- add Xvfb build hack
- New release 1.2.7

* Tue Sep 06 2005 Götz Waschk <waschk@mandriva.org> 1.2.6.2-2mdk
- drop Xvfb build workaround
- fix deps

* Tue Feb 22 2005 GÃ¶tz Waschk <waschk@linux-mandrake.com> 1.2.6.2-1mdk
- New release 1.2.6.2

* Sun Feb 13 2005 GÃ¶tz Waschk <waschk@linux-mandrake.com> 1.2.6.1-1mdk
- New release 1.2.6.1

* Thu Nov 25 2004 Götz Waschk <waschk@linux-mandrake.com> 1.2.5-1mdk
- update mime handling
- New release 1.2.5

* Tue Jul 20 2004 Goetz Waschk <waschk@linux-mandrake.com> 1.2.4-1mdk
- New release 1.2.4

* Thu Mar 11 2004 Götz Waschk <waschk@linux-mandrake.com> 1.2.3-1mdk
- fix menu section
- add new desktop entry
- don't compress the icons
- new version

