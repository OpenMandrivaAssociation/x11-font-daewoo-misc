Name: x11-font-daewoo-misc
Version: 1.0.4
Release: 1
Summary: Xorg X11 font daewoo-misc
Group: Development/X11
URL: https://xorg.freedesktop.org
Source0: https://xorg.freedesktop.org/releases/individual/font/font-daewoo-misc-%{version}.tar.xz
# See #38627 for licensing
License: MIT
BuildArch: noarch
BuildRequires: fontconfig
BuildRequires: pkgconfig(fontutil) >= 1.0.1
BuildRequires: pkgconfig(xorg-macros) >= 1.1.5
Requires(post,postun): mkfontscale

%description
Xorg X11 font daewoo-misc.

%prep
%autosetup -p1 -n font-daewoo-misc-%{version}

%build
%configure --with-fontdir=%{_datadir}/fonts/misc
%make_build

%install
%make_install
rm -f %{buildroot}%{_datadir}/fonts/misc/fonts.scale
rm -f %{buildroot}%{_datadir}/fonts/misc/fonts.dir

%post
mkfontscale %{_datadir}/fonts/misc
mkfontdir %{_datadir}/fonts/misc

%postun
mkfontscale %{_datadir}/fonts/misc
mkfontdir %{_datadir}/fonts/misc

%files
%doc COPYING
%{_datadir}/fonts/misc/hangl*.pcf.gz
