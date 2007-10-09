%define name pybliographer
%define version 1.2.11
%define release %mkrel 1
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
Requires:	gnome-python
Requires:	gnome-python-gconf
Requires:	gnome-python-gnomevfs
Requires:	pygtk2.0-libglade
Requires:	python-bibtex >= 1.1.93.1
Requires(post): desktop-file-utils scrollkeeper
Requires(postun): desktop-file-utils scrollkeeper
BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot
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

%build
%configure2_5x
%make


%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f %buildroot%_datadir/applications/mimeinfo.cache
chmod -x $RPM_BUILD_ROOT%{_datadir}/pybliographer/*.py

%{find_lang} %{name} --with-gnome --all-name

# menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{_bindir}/pybliographic" title="Pybliographic" icon="pybliographic.png" longtitle="A tool for managing bibliographic databases" needs="x11" section="Office/Publishing" mimetypes="text/x-bibtex" startup_notify="true" xdg="true"
EOF
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-Office-Publishing" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*


# icon
mkdir -p $RPM_BUILD_ROOT%{_miconsdir}
mkdir -p $RPM_BUILD_ROOT%{_liconsdir}
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_miconsdir}/pybliographic.png
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_iconsdir}/pybliographic.png
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_liconsdir}/pybliographic.png

%post
%{update_menus}
%update_desktop_database
%update_scrollkeeper

%postun
%{clean_menus}
%clean_desktop_database
%clean_scrollkeeper

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README TODO
%{_bindir}/*
%_datadir/applications/pybliographic.desktop
%{_datadir}/mime-info/*
%{_datadir}/pixmaps/*
%{_datadir}/omf/pybliographer/pybliographer-C.omf
%{_datadir}/pybliographer
%{_menudir}/%{name}
%{_iconsdir}/pybliographic.png
%{_miconsdir}/pybliographic.png
%{_liconsdir}/pybliographic.png


