Summary:	Extra plugins for Anjuta
Name:		anjuta-extras
Version:	2.32.0.0
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/anjuta-extras/2.32/%{name}-%{version}.tar.bz2
# Source0-md5:	44e79fb026524897d123bcde5e7861f9
URL:		http://www.anjuta.org/
BuildRequires:	GConf2-devel >= 2.20.0
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	binutils-devel >= 3:2.15.92
BuildRequires:	gettext-devel
BuildRequires:	gnome-common
BuildRequires:	graphviz-devel
BuildRequires:	gtk+2-devel >= 2:2.18.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libanjuta-devel >= 1:2.32.0.0
BuildRequires:	libgnomecanvas-devel >= 2.12.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
Requires(post,preun):	GConf2
Requires:	anjuta >= 1:2.32.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a set of plugins for Anjuta.

The following plugins are included:
- Class Inheritance: A graph painter for the inheritance of the
  classes
- Profiler: Application performance profiler
- Sample Plugin: Sample Plugin for Anjuta
- Scintilla Editor: An alternate editor based on Scintilla
- Scratchbox: Change build commands to use scratchbox 1 or 2
- Valgrind Plugin: Powerful debugging tool

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-schemas-install

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/anjuta/*.{a,la}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install anjuta-editor-scintilla.schemas
%gconf_schema_install anjuta-valgrind.schemas

%preun
%gconf_schema_uninstall anjuta-editor-scintilla.schemas
%gconf_schema_uninstall anjuta-valgrind.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/anjuta/libanjuta-editor.so
%attr(755,root,root) %{_libdir}/anjuta/libanjuta-profiler.so
%attr(755,root,root) %{_libdir}/anjuta/libanjuta-sample.so
%attr(755,root,root) %{_libdir}/anjuta/libanjuta-scratchbox.so
%attr(755,root,root) %{_libdir}/anjuta/libanjuta-valgrind.so
%{_libdir}/anjuta/anjuta-editor.plugin
%{_libdir}/anjuta/profiler.plugin
%{_libdir}/anjuta/anjuta-sample.plugin
%{_libdir}/anjuta/anjuta-scratchbox.plugin
%{_libdir}/anjuta/anjuta-valgrind.plugin
%{_sysconfdir}/gconf/schemas/anjuta-editor-scintilla.schemas
%{_sysconfdir}/gconf/schemas/anjuta-valgrind.schemas
%{_datadir}/anjuta/glade/*.png
%{_datadir}/anjuta/glade/*.ui
%{_datadir}/anjuta/properties
%{_datadir}/anjuta/ui/*.ui
%{_datadir}/anjuta/ui/*.xml
%{_pixmapsdir}/anjuta/*.png
%{_pixmapsdir}/anjuta/*.svg
