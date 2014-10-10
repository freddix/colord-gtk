Summary:	GTK helper library for colord
Name:		colord-gtk
Version:	0.1.25
Release:	4
License:	GPL v2+ and LGPL v2+
Group:		Libraries
Source0:	http://www.freedesktop.org/software/colord/releases/%{name}-%{version}.tar.xz
# Source0-md5:	f3ad262c060fc50c10805b744be7479d
URL:		http://www.freedesktop.org/software/colord/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	colord-devel
BuildRequires:	gettext-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+3-devel
BuildRequires:	intltool
BuildRequires:	lcms2-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	vala
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK helper library for colord.

%package devel
Summary:	Header files for colord-gtk library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for colord-gtk library.

%package apidocs
Summary:	colord-gtk API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
colord-gtk API documentation.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--enable-vala		\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
# -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS NEWS README TODO
%attr(755,root,root) %ghost %{_libdir}/libcolord-gtk.so.1
%attr(755,root,root) %{_libdir}/libcolord-gtk.so.*.*.*
%{_libdir}/girepository-1.0/ColordGtk-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcolord-gtk.so
%{_includedir}/colord-1/colord-gtk.h
%{_includedir}/colord-1/colord-gtk
%{_datadir}/gir-1.0/ColordGtk-1.0.gir
%{_datadir}/vala/vapi/colord-gtk.vapi
%{_pkgconfigdir}/colord-gtk.pc

%if 0
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/colord-gtk
%endif

