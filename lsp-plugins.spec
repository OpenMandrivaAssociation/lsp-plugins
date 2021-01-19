%global debug_package %{nil}

Name:		lsp-plugins
Summary:	A collection of plugins which aim to bring new, non existing plugins to Linux
Version:	1.1.29
Release:  1
License:	GPLv3
Group:		System/Libraries
URL:		https://github.com/sadko4u/lsp-plugins/releases
Source0:	https://github.com/sadko4u/%{name}/archive/%{name}-%{version}.tar.gz
#Patch0:         lsp-plugins-1.1.28-plugins.php.patch

BuildRequires:	ladspa-devel
BuildRequires:	php-cli
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(jack) 
BuildRequires:	pkgconfig(lv2)
BuildRequires:	pkgconfig(sndfile)

%description
LSP (Linux Studio Plugins) is a collection of open-source plugins currently
compatible with LADSPA, LV2 and LinuxVST formats.
Standalone plugins for JACK are provided since version 1.0.8.
Experimental support of ARMv7 added since version 1.1.4.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
#ifarch armv7hl
# Force building for armv7 even if hardware/kernel is armv8
#make DESTDIR=%{buildroot} PREFIX=%{_prefix} BUILD_PROFILE=armv7a
#else
make DESTDIR=%{buildroot} PREFIX=%{_prefix}
#endif

%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix} LIB_PATH=%{_libdir}
# We don't need these:
#rm -rf %{buildroot}%{_libdir}/vst/*

%files
%{_bindir}/*
%{_sysconfdir}/xdg/menus/applications-merged/lsp-plugins.menu
%{_libdir}/ladspa/lsp-plugins-ladspa.so
%{_libdir}/lv2/lsp-plugins.lv2/*
%{_libdir}/vst/lsp-plugins-lxvst-%{version}/lsp-plugins*
%{_docdir}/lsp-plugins/*
%{_libdir}/lsp-plugins/lsp-plugins-jack-core-%{version}.so
%{_libdir}/%{name}/%{name}-r3d-glx.so
%{_datadir}/applications/in.lsp_plug.lsp_plugins_*
%{_datadir}/desktop-directories/lsp-plugins.directory
%{_iconsdir}/hicolor/*x*/apps/lsp-plugins.png
%{_iconsdir}/hicolor/scalable/apps/lsp-plugins.svg
