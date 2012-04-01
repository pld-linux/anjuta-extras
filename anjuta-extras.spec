Summary:	Extra plugins for Anjuta
Name:		anjuta-extras
Version:	3.4.0
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/anjuta-extras/3.4/%{name}-%{version}.tar.xz
# Source0-md5:	fa1946725c0f45ffa7ee64b4a2c8f86e
URL:		http://www.anjuta.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gnome-common
BuildRequires:	gnome-doc-utils >= 0.18.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libanjuta-devel >= 1:3.4.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	anjuta >= 1:3.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a set of plugins for Anjuta.

The following plugins are included:
- Sample Plugin: Sample Plugin for Anjuta
- Scintilla Editor: An alternate editor based on Scintilla
- Scratchbox: Change build commands to use scratchbox 1 or 2

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
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/anjuta/*.{a,la}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/anjuta/libanjuta-editor.so
%attr(755,root,root) %{_libdir}/anjuta/libanjuta-sample.so
%attr(755,root,root) %{_libdir}/anjuta/libanjuta-scratchbox.so
%{_libdir}/anjuta/anjuta-editor.plugin
%{_libdir}/anjuta/anjuta-sample.plugin
%{_libdir}/anjuta/anjuta-scratchbox.plugin
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.plugins.scintilla.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.plugins.scratchbox.gschema.xml
%{_datadir}/anjuta/glade/*.png
%{_datadir}/anjuta/glade/*.ui
%{_datadir}/anjuta/properties
%{_datadir}/anjuta/ui/*.ui
%{_datadir}/anjuta/ui/*.xml
%{_pixmapsdir}/anjuta/*.png
%{_pixmapsdir}/anjuta/*.svg
