#global debug_package %{nil}
%define _empty_manifest_terminate_build 0

Name:		lsp-plugins
Summary:	A collection of plugins which aim to bring new, non existing plugins to Linux
Version:	1.2.1
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

%description
LSP (Linux Studio Plugins) is a collection of open-source plugins currently
compatible with LADSPA, LV2 and LinuxVST formats.
Standalone plugins for JACK are provided since version 1.0.8.
Experimental support of ARMv7 added since version 1.1.4.

%prep
%autosetup -p1 -n %{name}

%build
make config \
%make PREFIX=%{_prefix} \
    BIN_PATH=%{_bindir} LIB_PATH=%{_libdir} \
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
%{_bindir}/*
#{_libdir}/ladspa/lsp-plugins-ladspa.so
%{_libdir}/lv2/lsp-plugins.lv2/*
#{_libdir}/vst/lsp-plugins-lxvst-%{version}/lsp-plugins*
#{_libdir}/lsp-plugins/lsp-plugins-jack-core-%{version}.so
#{_libdir}/%{name}/%{name}-r3d-glx.so

