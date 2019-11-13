Summary:	Extra plugins for Anjuta
Summary(pl.UTF-8):	Dodatkowe wtyczki dla Anjuty
Name:		anjuta-extras
Version:	3.26.0
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/anjuta-extras/3.26/%{name}-%{version}.tar.xz
# Source0-md5:	c08e83b6d24dc735fd54f6c964aec1e2
URL:		http://anjuta.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.10
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gnome-common
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libanjuta-devel >= 1:3.26.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	anjuta >= 1:3.26.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a set of plugins for Anjuta.

The following plugins are included:
- Sample Plugin: Sample Plugin for Anjuta
- Scintilla Editor: An alternate editor based on Scintilla
- Scratchbox: Change build commands to use scratchbox 1 or 2

%description -l pl.UTF-8
Ten pakiet zawiera zestaw wtyczek dla Anjuty. Zawiera następujące
wtyczki:
- Sample Plugin - przykładowa wtyczka
- Scintilla Editor - alternatywny edytor, oparty na Scintilli
- Scratchbox - zmiana poleceń budowania do używania scratchboksa 1 lub
  2

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
%doc AUTHORS NEWS

%attr(755,root,root) %{_libdir}/anjuta/libanjuta-editor.so
%{_libdir}/anjuta/anjuta-editor.plugin
%{_datadir}/anjuta/glade/anjuta-editor-scintilla.ui
%{_datadir}/anjuta/properties
%{_datadir}/anjuta/ui/anjuta-scintilla.xml
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.plugins.scintilla.gschema.xml
%{_pixmapsdir}/anjuta/anjuta-editor-scintilla-plugin-48.png
%{_pixmapsdir}/anjuta/anjuta-editor-scintilla-plugin.svg

%attr(755,root,root) %{_libdir}/anjuta/libanjuta-sample.so
%{_libdir}/anjuta/anjuta-sample.plugin
%{_datadir}/anjuta/ui/anjuta-sample.ui
%{_pixmapsdir}/anjuta/anjuta-sample-plugin-48.png
%{_pixmapsdir}/anjuta/anjuta-sample-plugin.svg

%attr(755,root,root) %{_libdir}/anjuta/libanjuta-scratchbox.so
%{_libdir}/anjuta/anjuta-scratchbox.plugin
%{_datadir}/anjuta/glade/anjuta-scratchbox.ui
%{_datadir}/anjuta/glade/anjuta-scratchbox-panel.png
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.plugins.scratchbox.gschema.xml
%{_pixmapsdir}/anjuta/anjuta-scratchbox-48.png
