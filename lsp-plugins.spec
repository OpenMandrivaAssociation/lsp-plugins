#global debug_package %{nil}
%define _empty_manifest_terminate_build 0

Name:		lsp-plugins
Summary:	A collection of plugins which aim to bring new, non existing plugins to Linux
Version:	1.2.16
Release:	1
License:	GPLv3
Group:		System/Libraries
URL:		https://github.com/sadko4u/lsp-plugins/releases
Source0:	https://github.com/sadko4u/lsp-plugins/releases/download/%{version}/lsp-plugins-src-%{version}.tar.gz

BuildRequires:	ladspa-devel
BuildRequires:	php-cli
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(jack) 
BuildRequires:	pkgconfig(lv2)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:  pkgconfig(opengl)
BuildRequires:	pkgconfig(xrandr)

%description
LSP (Linux Studio Plugins) is a collection of open-source plugins currently
compatible with LADSPA, LV2 and LinuxVST formats.
Standalone plugins for JACK are provided since version 1.0.8.
Experimental support of ARMv7 added since version 1.1.4.

%prep
%autosetup -p1 -n %{name}

%build
make config FEATURES='lv2 vst2 ladspa jack xdg' \
%make_build PREFIX=%{_prefix} LIBDIR=%{_libdir} SHAREDDIR=%{_datadir} BINDIR=%{_bindir}
    BUILD_MODULES='lv2 vst ladspa jack'


%install
#make install DESTDIR=%{buildroot} PREFIX=%{_prefix} LIB_PATH=%{_libdir}

%make_install \
    DESTDIR=%{buildroot} \
	PREFIX=%{_prefix} \
	LIBDIR=%{_libdir} \
	BINDIR=%{_bindir} \
	SHAREDDIR=%{_datadir}

%files
#doc %{_datadir}/doc/lsp-plugins/
%{_bindir}/*
%{_libdir}/vst/lsp-plugins/
%{_libdir}/lsp-plugins/liblsp-plugins-jack-%{version}.so
%{_libdir}/lv2/lsp-plugins.lv2/*
%{_libdir}/liblsp-r3d-glx-lib*
%{_libdir}/ladspa/lsp-plugins-ladspa.so
%{_libdir}/pkgconfig/lsp-r3d-glx-lib.pc
%{_datadir}/applications/in.lsp_plug.lsp_plugins*
%{_datadir}/desktop-directories/lsp-plugins.directory
%{_datadir}/icons/hicolor/*x*/apps/lsp-plugins.png
%{_datadir}/icons/hicolor/scalable/apps/lsp-plugins.svg
%{_sysconfdir}/xdg/menus/applications-merged/%{name}.menu
