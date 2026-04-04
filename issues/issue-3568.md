---
title: '"Choose your hardware device" dropdown empty as non-root'
source_url: https://github.com/monero-project/monero-gui/issues/3568
author: Josef37
assignees: []
labels: []
created_at: '2021-06-16T21:22:54+00:00'
updated_at: '2021-12-17T16:45:03+00:00'
type: issue
status: closed
closed_at: '2021-06-17T23:51:24+00:00'
---

# Original Description
I'm not sure if this is a bug or a misunderstanding on my part (sorry if it is :upside_down_face:).

I tried to create a new hardware wallet using my *Ledger Nano S*.

### Steps to reproduce
I plug in my device and unlock it. 
Then I open the Manjaro GUI and click on "Create a new wallet from hardware". 
Then I try to choose the hardware device with the "Choose your hardware device" dropdown. 
I expect to be able to choose my hardware device, but nothing happens (only the arrow on the right indicates that the dropdown opened).

Repeating these steps as root resolves the issue.

### Notes
I made sure to close Ledger Live (which works fine as a normal user).
I also [added udev rules](https://support.ledger.com/hc/en-us/articles/115005165269-Fix-connection-issues), which were required to get Ledger Live to run.

### System
I'm running the latest version of Monero GUI (0.17.2.2). 
The Ledger Nano S has firmware version 2.0.0. 
My OS is Linux Manjaro KDE with the Linux 5.10.42-1 Kernel (LTS).

# Discussion History
## selsta | 2021-06-16T21:29:02+00:00
Did you install using your package manager? Or did you download the binary from getmonero.org?

If you used your package manager please try the getmonero.org version and report back.

## Josef37 | 2021-06-17T19:54:26+00:00
I did install it through the package manager. Launching the executable from getmonero.org works fine. Thank you! :+1: 

What's the issue with the package manager version, then? :thinking: 

## selsta | 2021-06-17T23:51:24+00:00
I have no idea, please report this to your package manager. This is out of our control.

## Josef37 | 2021-06-18T03:55:00+00:00
Thank you for support :+1: 
There is already an issue on the forums reporting similar: https://bugs.archlinux.org/task/69738

## kpcyrd | 2021-12-17T16:34:41+00:00
hm, I'm the maintainer of the Arch Linux package. Unfortunately I don't have a hardware wallet to test this with (I tweeted that I'm looking for a test device a while ago but didn't get any replies).

This is how the Arch Linux package is compiled:

```
  mkdir -p build && cd build
  cmake -D CMAKE_BUILD_TYPE=Release -D ARCH=default ../
  make
```

https://github.com/archlinux/svntogit-community/blob/fe8294af0aded21fc587eecbedad1827ccda42a3/trunk/PKGBUILD#L56-L58

The full build log looks like this:

<details>

```
+ repro -o /tmp/rebuilderdX9R5ow/out -- /tmp/rebuilderdX9R5ow/inputs/monero-gui-0.17.3.0-2-x86_64.pkg.tar.zst
==> Reusing existing container
==> Updating container
repro 20211205
:: Synchronizing package databases...
 core downloading...
 extra downloading...
 community downloading...
:: Starting full system upgrade...
 there is nothing to do
  -> Preparing packages
Hit cache for /var/lib/rebuilderd-worker/cache/acl-2.3.1-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/archlinux-keyring-20211028-1-any.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/argon2-20190702-3-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/attr-2.5.1-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/audit-3.0.6-5-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/autoconf-2.71-1-any.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/automake-1.16.5-1-any.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/avahi-0.8+22+gfd482a7-3-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/bash-5.1.012-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/binutils-2.36.1-3-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/bison-3.8.2-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/boost-1.76.0-6-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/boost-libs-1.76.0-6-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/brotli-1.0.9-7-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/bzip2-1.0.8-4-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/ca-certificates-20210603-1-any.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/ca-certificates-mozilla-3.73-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/ca-certificates-utils-20210603-1-any.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/cmake-3.22.1-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/coreutils-9.0-2-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/cryptsetup-2.4.2-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/curl-7.80.0-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/db-5.3.28-5-x86_64.pkg.tar.xz
Hit cache for /var/lib/rebuilderd-worker/cache/dbus-1.12.20-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/device-mapper-2.03.14-2-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/diffutils-3.8-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/dnssec-anchors-20190629-3-any.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/double-conversion-3.1.6-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/e2fsprogs-1.46.4-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/elfutils-0.186-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/expat-2.4.1-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/fakeroot-1.26-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/file-5.41-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/filesystem-2021.12.07-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/findutils-4.8.0-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/flex-2.6.4-3-x86_64.pkg.tar.xz
Hit cache for /var/lib/rebuilderd-worker/cache/fontconfig-2:2.13.94-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/freetype2-2.11.1-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/fstrm-0.6.1-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/gawk-5.1.1-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/gc-8.2.0-2-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/gcc-11.1.0-3-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/gcc-libs-11.1.0-3-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/gdbm-1.22-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/gettext-0.21-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/git-2.34.1-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/glib2-2.70.2-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/glibc-2.33-5-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/gmp-6.2.1-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/gnupg-2.2.32-2-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/gnutls-3.7.2-2-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/gpgme-1.16.0-3-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/graphite-1:1.3.14-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/grep-3.7-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/groff-1.22.4-6-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/guile-2.2.7-2-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/gzip-1.11-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/harfbuzz-3.2.0-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/hicolor-icon-theme-0.17-2-any.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/hidapi-0.11.0-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/hiredis-1.0.2-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/hwids-20210613-1-any.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/iana-etc-20211025-1-any.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/icu-70.1-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/iptables-1:1.8.7-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/json-c-0.15-2-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/jsoncpp-1.9.4-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/kbd-2.4.0-2-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/keyutils-1.6.3-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/kmod-29-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/krb5-1.19.2-2-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/ldns-1.7.1-2-x86_64.pkg.tar.xz
Hit cache for /var/lib/rebuilderd-worker/cache/less-1:590-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libarchive-3.5.2-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libassuan-2.5.5-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libcap-2.62-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libcap-ng-0.8.2-6-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libcroco-0.6.13-2-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libcups-1:2.4.0-4-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libdaemon-0.14-5-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libdrm-2.4.109-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libedit-20210910_3.1-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libelf-0.186-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libevdev-1.12.0-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libevent-2.1.12-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libffi-3.4.2-4-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libgcrypt-1.9.4-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libglvnd-1.3.4-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libgpg-error-1.43-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libgudev-237-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libice-1.0.10-3-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libidn2-2.3.2-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libinput-1.19.3-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libjpeg-turbo-2.1.2-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libksba-1.6.0-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libldap-2.6.0-2-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libmnl-1.0.4-3-x86_64.pkg.tar.xz
Hit cache for /var/lib/rebuilderd-worker/cache/libmpc-1.2.1-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libnetfilter_conntrack-1.0.8-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libnfnetlink-1.0.1-4-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libnftnl-1.2.1-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libnghttp2-1.46.0-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libnl-3.5.0-3-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libnsl-2.0.0-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libomxil-bellagio-0.9.3-3-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libp11-kit-0.24.0-2-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libpcap-1.10.1-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libpciaccess-0.16-2-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libpgm-5.3.128-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libpng-1.6.37-3-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libproxy-0.4.17-6-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libpsl-0.21.1-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libsasl-2.1.27-3-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libseccomp-2.5.3-3-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libsecret-0.20.4-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libsm-1.2.3-2-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libsodium-1.0.18-2-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libssh2-1.10.0-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libtasn1-4.18.0-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libtiff-4.3.0-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libtirpc-1.3.2-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libtool-2.4.6+42+gb88cebd5-16-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libunistring-0.9.10-3-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libunwind-1.5.0-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libusb-1.0.24-2-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libuv-1.42.0-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libwacom-1.12-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libx11-1.7.3.1-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libxau-1.0.9-3-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libxcb-1.14-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libxcrypt-4.4.26-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libxdamage-1.1.5-3-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libxdmcp-1.1.3-3-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libxext-1.3.4-3-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libxfixes-6.0.0-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libxi-1.8-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libxkbcommon-1.3.1-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libxkbcommon-x11-1.3.1-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libxml2-2.9.12-5-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libxmu-1.1.3-2-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libxrender-0.9.10-4-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libxshmfence-1.3-2-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libxt-1.2.1-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/libxxf86vm-1.1.4-4-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/linux-api-headers-5.12.3-1-any.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/llvm-libs-13.0.0-6-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/lm_sensors-1:3.6.0.r41.g31d1f125-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/lz4-1:1.9.3-2-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/m4-1.4.19-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/make-4.3-3-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/md4c-0.4.8-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/mesa-21.3.1-1-x86_64.pkg.tar.zst
Downloading monero-0.17.3.0-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/mpfr-4.1.0.p13-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/mtdev-1.1.6-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/ncurses-6.3-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/nettle-3.7.3-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/npth-1.6-3-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/openssl-1.1.1.l-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/p11-kit-0.24.0-2-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/pacman-6.0.1-2-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/pacman-mirrorlist-20211212-1-any.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/pam-1.5.2-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/pambase-20211210-1-any.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/patch-2.7.6-8-x86_64.pkg.tar.xz
Hit cache for /var/lib/rebuilderd-worker/cache/pcre-8.45-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/pcre2-10.39-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/pcsclite-1.9.5-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/perl-5.34.0-3-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/perl-error-0.17029-3-any.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/perl-mailtools-2.21-5-any.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/perl-timedate-2.33-3-any.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/pinentry-1.2.0-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/pkgconf-1.8.0-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/popt-1.18-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/protobuf-3.17.3-3-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/protobuf-c-1.4.0-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/python-3.10.1-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/qt5-base-5.15.2+kde+r263-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/qt5-declarative-5.15.2+kde+r41-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/qt5-graphicaleffects-5.15.2-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/qt5-quickcontrols-5.15.2-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/qt5-quickcontrols2-5.15.2+kde+r8-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/qt5-svg-5.15.2+kde+r13-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/qt5-tools-5.15.2+kde+r17-4-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/qt5-xmlpatterns-5.15.2-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/readline-8.1.001-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/rhash-1.4.2-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/sed-4.8-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/shadow-4.8.1-4-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/shared-mime-info-2.0+115+gd74a913-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/sqlite-3.37.0-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/sudo-1.9.8.p2-3-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/systemd-249.7-2-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/systemd-libs-249.7-2-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/tar-1.34-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/texinfo-6.8-2-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/tslib-1.22-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/tzdata-2021e-1-x86_64.pkg.tar.zst
Downloading unbound-1.14.0-2-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/util-linux-2.37.2-4-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/util-linux-libs-2.37.2-4-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/vulkan-icd-loader-1.2.202-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/wayland-1.20.0-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/which-2.21-5-x86_64.pkg.tar.xz
Hit cache for /var/lib/rebuilderd-worker/cache/xcb-proto-1.14.1-5-any.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/xcb-util-0.4.0-3-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/xcb-util-image-0.4.0-3-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/xcb-util-keysyms-0.4.0-3-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/xcb-util-renderutil-0.3.9-3-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/xcb-util-wm-0.4.1-3-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/xdg-utils-1.1.3+19+g9816ebb-1-any.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/xkeyboard-config-2.34-1-any.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/xorg-xprop-1.2.5-1-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/xorg-xset-1.2.4-2-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/xorgproto-2021.5-1-any.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/xz-5.2.5-2-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/zeromq-4.3.4-2-x86_64.pkg.tar.zst
Hit cache for /var/lib/rebuilderd-worker/cache/zlib-1:1.2.11-4-x86_64.pkg.tar.xz
Hit cache for /var/lib/rebuilderd-worker/cache/zstd-1.5.0-1-x86_64.pkg.tar.zst
  -> Finished preparing packages
==> Starting build...
  -> Create snapshot for monero-gui_915964...
  -> Fetching PKGBUILD from ASP...
resolving dependencies...
looking for conflicting packages...

Packages (11) db-5.3.28-5  gdbm-1.22-1  git-2.34.1-1  grep-3.7-1  jq-1.6-4  oniguruma-6.9.7.1-1  perl-5.34.0-3  perl-error-0.17029-3  perl-mailtools-2.21-5  perl-timedate-2.33-3  asp-8-1

Total Installed Size:  101.54 MiB

:: Proceed with installation? [Y/n] 
checking keyring...
checking package integrity...
loading package files...
checking for file conflicts...
checking available disk space...
:: Processing package changes...
installing oniguruma...
installing jq...
installing gdbm...
installing db...
installing perl...
installing perl-error...
installing perl-timedate...
installing perl-mailtools...
installing grep...
installing git...
Optional dependencies for git
    tk: gitk and git gui
    perl-libwww: git svn
    perl-term-readkey: git svn and interactive.singlekey setting
    perl-io-socket-ssl: git send-email TLS support
    perl-authen-sasl: git send-email TLS support
    perl-mediawiki-api: git mediawiki support
    perl-datetime-format-iso8601: git mediawiki support
    perl-lwp-protocol-https: git mediawiki https support
    perl-cgi: gitweb (web interface) support
    python: git svn & git p4
    subversion: git svn
    org.freedesktop.secrets: keyring credential helper
    libsecret: libsecret credential helper [installed]
installing asp...
:: Running post-transaction hooks...
(1/4) Creating system user accounts...
Creating group git with gid 975.
Creating user git (git daemon user) with uid 975 and gid 975.
(2/4) Reloading system manager configuration...
  Skipped: Current root is not booted.
(3/4) Arming ConditionNeedsUpdate...
(4/4) Warn about old perl modules
From https://github.com/archlinux/svntogit-community
 * branch            packages/monero-gui -> FETCH_HEAD
 * [new branch]      packages/monero-gui -> community/packages/monero-gui
Cloning into 'monero-gui'...
done.
/monero-gui /
Note: switching to 'f5d833fa35df483dcfafe7a62f7c4b6a11477be1'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at f5d833f archrelease: copy trunk to community-x86_64
  -> Found archlinux-keyring-20211028-1-any in keyring cache
==> Installing packages
==> Creating install root at /mnt
==> Installing packages to /mnt
warning: database file for 'core' does not exist (use '-Sy' to download)
warning: database file for 'extra' does not exist (use '-Sy' to download)
warning: database file for 'community' does not exist (use '-Sy' to download)
loading packages...
resolving dependencies...
looking for conflicting packages...

Packages (220) acl-2.3.1-1  archlinux-keyring-20211028-1  argon2-20190702-3  attr-2.5.1-1  audit-3.0.6-5  autoconf-2.71-1  automake-1.16.5-1  avahi-0.8+22+gfd482a7-3  bash-5.1.012-1  binutils-2.36.1-3  bison-3.8.2-1  boost-1.76.0-6  boost-libs-1.76.0-6  brotli-1.0.9-7  bzip2-1.0.8-4  ca-certificates-20210603-1  ca-certificates-mozilla-3.73-1  ca-certificates-utils-20210603-1  cmake-3.22.1-1  coreutils-9.0-2  cryptsetup-2.4.2-1  curl-7.80.0-1  db-5.3.28-5  dbus-1.12.20-1  device-mapper-2.03.14-2  diffutils-3.8-1  dnssec-anchors-20190629-3  double-conversion-3.1.6-1  e2fsprogs-1.46.4-1  elfutils-0.186-1  expat-2.4.1-1  fakeroot-1.26-1  file-5.41-1  filesystem-2021.12.07-1  findutils-4.8.0-1  flex-2.6.4-3  fontconfig-2:2.13.94-1  freetype2-2.11.1-1  fstrm-0.6.1-1  gawk-5.1.1-1  gc-8.2.0-2  gcc-11.1.0-3  gcc-libs-11.1.0-3  gdbm-1.22-1  gettext-0.21-1  git-2.34.1-1  glib2-2.70.2-1  glibc-2.33-5  gmp-6.2.1-1  gnupg-2.2.32-2  gnutls-3.7.2-2  gpgme-1.16.0-3  graphite-1:1.3.14-1  grep-3.7-1  groff-1.22.4-6  guile-2.2.7-2  gzip-1.11-1  harfbuzz-3.2.0-1  hicolor-icon-theme-0.17-2  hidapi-0.11.0-1  hiredis-1.0.2-1  hwids-20210613-1  iana-etc-20211025-1  icu-70.1-1  iptables-1:1.8.7-1  json-c-0.15-2  jsoncpp-1.9.4-1  kbd-2.4.0-2  keyutils-1.6.3-1  kmod-29-1  krb5-1.19.2-2  ldns-1.7.1-2  less-1:590-1  libarchive-3.5.2-1  libassuan-2.5.5-1  libcap-2.62-1  libcap-ng-0.8.2-6  libcroco-0.6.13-2  libcups-1:2.4.0-4  libdaemon-0.14-5  libdrm-2.4.109-1  libedit-20210910_3.1-1  libelf-0.186-1  libevdev-1.12.0-1  libevent-2.1.12-1  libffi-3.4.2-4  libgcrypt-1.9.4-1  libglvnd-1.3.4-1  libgpg-error-1.43-1  libgudev-237-1  libice-1.0.10-3  libidn2-2.3.2-1  libinput-1.19.3-1  libjpeg-turbo-2.1.2-1  libksba-1.6.0-1  libldap-2.6.0-2  libmnl-1.0.4-3  libmpc-1.2.1-1  libnetfilter_conntrack-1.0.8-1  libnfnetlink-1.0.1-4  libnftnl-1.2.1-1  libnghttp2-1.46.0-1  libnl-3.5.0-3  libnsl-2.0.0-1  libomxil-bellagio-0.9.3-3  libp11-kit-0.24.0-2  libpcap-1.10.1-1  libpciaccess-0.16-2  libpgm-5.3.128-1  libpng-1.6.37-3  libproxy-0.4.17-6  libpsl-0.21.1-1  libsasl-2.1.27-3  libseccomp-2.5.3-3  libsecret-0.20.4-1  libsm-1.2.3-2  libsodium-1.0.18-2  libssh2-1.10.0-1  libtasn1-4.18.0-1  libtiff-4.3.0-1  libtirpc-1.3.2-1  libtool-2.4.6+42+gb88cebd5-16  libunistring-0.9.10-3  libunwind-1.5.0-1  libusb-1.0.24-2  libuv-1.42.0-1  libwacom-1.12-1  libx11-1.7.3.1-1  libxau-1.0.9-3  libxcb-1.14-1  libxcrypt-4.4.26-1  libxdamage-1.1.5-3  libxdmcp-1.1.3-3  libxext-1.3.4-3  libxfixes-6.0.0-1  libxi-1.8-1  libxkbcommon-1.3.1-1  libxkbcommon-x11-1.3.1-1  libxml2-2.9.12-5  libxmu-1.1.3-2  libxrender-0.9.10-4  libxshmfence-1.3-2  libxt-1.2.1-1  libxxf86vm-1.1.4-4  linux-api-headers-5.12.3-1  llvm-libs-13.0.0-6  lm_sensors-1:3.6.0.r41.g31d1f125-1  lz4-1:1.9.3-2  m4-1.4.19-1  make-4.3-3  md4c-0.4.8-1  mesa-21.3.1-1  monero-0.17.3.0-1  mpfr-4.1.0.p13-1  mtdev-1.1.6-1  ncurses-6.3-1  nettle-3.7.3-1  npth-1.6-3  openssl-1.1.1.l-1  p11-kit-0.24.0-2  pacman-6.0.1-2  pacman-mirrorlist-20211212-1  pam-1.5.2-1  pambase-20211210-1  patch-2.7.6-8  pcre-8.45-1  pcre2-10.39-1  pcsclite-1.9.5-1  perl-5.34.0-3  perl-error-0.17029-3  perl-mailtools-2.21-5  perl-timedate-2.33-3  pinentry-1.2.0-1  pkgconf-1.8.0-1  popt-1.18-1  protobuf-3.17.3-3  protobuf-c-1.4.0-1  python-3.10.1-1  qt5-base-5.15.2+kde+r263-1  qt5-declarative-5.15.2+kde+r41-1  qt5-graphicaleffects-5.15.2-1  qt5-quickcontrols-5.15.2-1  qt5-quickcontrols2-5.15.2+kde+r8-1  qt5-svg-5.15.2+kde+r13-1  qt5-tools-5.15.2+kde+r17-4  qt5-xmlpatterns-5.15.2-1  readline-8.1.001-1  rhash-1.4.2-1  sed-4.8-1  shadow-4.8.1-4  shared-mime-info-2.0+115+gd74a913-1  sqlite-3.37.0-1  sudo-1.9.8.p2-3  systemd-249.7-2  systemd-libs-249.7-2  tar-1.34-1  texinfo-6.8-2  tslib-1.22-1  tzdata-2021e-1  unbound-1.14.0-2  util-linux-2.37.2-4  util-linux-libs-2.37.2-4  vulkan-icd-loader-1.2.202-1  wayland-1.20.0-1  which-2.21-5  xcb-proto-1.14.1-5  xcb-util-0.4.0-3  xcb-util-image-0.4.0-3  xcb-util-keysyms-0.4.0-3  xcb-util-renderutil-0.3.9-3  xcb-util-wm-0.4.1-3  xdg-utils-1.1.3+19+g9816ebb-1  xkeyboard-config-2.34-1  xorg-xprop-1.2.5-1  xorg-xset-1.2.4-2  xorgproto-2021.5-1  xz-5.2.5-2  zeromq-4.3.4-2  zlib-1:1.2.11-4  zstd-1.5.0-1

Total Installed Size:  1639.57 MiB

:: Proceed with installation? [Y/n] 
checking keyring...
checking package integrity...
loading package files...
checking for file conflicts...
warning: dependency cycle detected:
warning: harfbuzz will be installed before its freetype2 dependency
warning: dependency cycle detected:
warning: mesa will be installed before its libglvnd dependency
checking available disk space...
:: Processing package changes...
installing linux-api-headers...
installing tzdata...
installing iana-etc...
installing filesystem...
installing glibc...
Optional dependencies for glibc
    gd: for memusagestat
installing attr...
installing acl...
installing archlinux-keyring...
call to execv failed (No such file or directory)
installing argon2...
installing gcc-libs...
error: command failed to execute correctly
installing ncurses...
Optional dependencies for ncurses
    bash: for ncursesw6-config [pending]
installing readline...
installing bash...
Optional dependencies for bash
    bash-completion: for tab completion
installing util-linux-libs...
installing e2fsprogs...
installing openssl...
Optional dependencies for openssl
    ca-certificates [pending]
    perl [pending]
installing libsasl...
installing libldap...
installing keyutils...
installing krb5...
installing libcap-ng...
installing audit...
installing gmp...
installing mpfr...
installing gawk...
installing m4...
installing diffutils...
installing gdbm...
installing db...
installing libxcrypt...
installing perl...
installing autoconf...
installing automake...
installing expat...
installing libdaemon...
installing zlib...
installing bzip2...
installing pcre...
installing libffi...
installing glib2...
Optional dependencies for glib2
    python: gdbus-codegen, glib-genmarshal, glib-mkenums, gtester-report [pending]
    libelf: gresource inspection tool [pending]
installing libtirpc...
installing pambase...
installing pam...
installing libcap...
installing libgpg-error...
installing libgcrypt...
installing libtasn1...
installing libp11-kit...
installing lz4...
installing xz...
installing zstd...
installing systemd-libs...
installing dbus...
installing avahi...
Optional dependencies for avahi
    gtk3: avahi-discover, avahi-discover-standalone, bshell, bssh, bvnc
    qt5-base: qt5 bindings [pending]
    libevent: libevent bindings [pending]
    nss-mdns: NSS support for mDNS
    python-twisted: avahi-bookmarks
    python-gobject: avahi-bookmarks, avahi-discover
    python-dbus: avahi-bookmarks, avahi-discover
installing coreutils...
installing findutils...
installing p11-kit...
installing ca-certificates-utils...
installing ca-certificates-mozilla...
installing ca-certificates...
installing brotli...
installing libunistring...
installing libidn2...
installing libnghttp2...
installing libpsl...
installing libssh2...
installing curl...
installing libelf...
installing elfutils...
installing binutils...
installing icu...
installing libxml2...
installing libcroco...
installing gettext...
Optional dependencies for gettext
    git: for autopoint infrastructure updates [pending]
installing bison...
installing boost-libs...
Optional dependencies for boost-libs
    openmpi: for mpi support
installing boost...
Optional dependencies for boost
    python: for python bindings [pending]
installing libarchive...
installing hicolor-icon-theme...
installing jsoncpp...
Optional dependencies for jsoncpp
    jsoncpp-doc: documentation
installing libnsl...
installing libuv...
installing rhash...
installing cmake...
Optional dependencies for cmake
    qt6-base: cmake-gui
installing device-mapper...
installing popt...
installing json-c...
installing cryptsetup...
installing dnssec-anchors...
installing double-conversion...
installing sed...
installing shadow...
installing libseccomp...
installing file...
installing util-linux...
Optional dependencies for util-linux
    python: python bindings to libmount [pending]
    words: default dictionary for look
installing fakeroot...
installing flex...
installing libpng...
installing graphite...
installing harfbuzz...
Optional dependencies for harfbuzz
    cairo: hb-view program
    chafa: hb-view program
installing freetype2...
installing fontconfig...
/tmp/alpm_QymSUA/.INSTALL: line 2: vercmp: command not found
/tmp/alpm_QymSUA/.INSTALL: line 2: ((: < 0 : syntax error: operand expected (error token is "< 0 ")
Rebuilding fontconfig cache...
installing libevent...
Optional dependencies for libevent
    python: to use event_rpcgen.py [pending]
installing fstrm...
installing gc...
installing libmpc...
installing gcc...
Optional dependencies for gcc
    lib32-gcc-libs: for generating code for 32-bit ABI
installing perl-error...
installing perl-timedate...
installing perl-mailtools...
installing pcre2...
installing grep...
installing git...
Optional dependencies for git
    tk: gitk and git gui
    perl-libwww: git svn
    perl-term-readkey: git svn and interactive.singlekey setting
    perl-io-socket-ssl: git send-email TLS support
    perl-authen-sasl: git send-email TLS support
    perl-mediawiki-api: git mediawiki support
    perl-datetime-format-iso8601: git mediawiki support
    perl-lwp-protocol-https: git mediawiki https support
    perl-cgi: gitweb (web interface) support
    python: git svn & git p4 [pending]
    subversion: git svn
    org.freedesktop.secrets: keyring credential helper
    libsecret: libsecret credential helper [pending]
installing npth...
installing libksba...
installing libassuan...
installing libsecret...
Optional dependencies for libsecret
    org.freedesktop.secrets: secret storage backend
installing pinentry...
Optional dependencies for pinentry
    gtk2: gtk2 backend
    qt5-base: qt backend [pending]
    gcr: gnome3 backend
installing nettle...
installing gnutls...
Optional dependencies for gnutls
    guile: for use with Guile bindings [pending]
installing sqlite...
installing gnupg...
Optional dependencies for gnupg
    libldap: gpg2keys_ldap [installed]
    libusb-compat: scdaemon
    pcsclite: scdaemon [pending]
installing gpgme...
installing groff...
Optional dependencies for groff
    netpbm: for use together with man -H command interaction in browsers
    psutils: for use together with man -H command interaction in browsers
    libxaw: for gxditview
    perl-file-homedir: for use with glilypond
installing tar...
installing libtool...
installing less...
installing gzip...
installing texinfo...
installing guile...
installing hidapi...
Optional dependencies for hidapi
    libusb: for the libusb backend -- hidapi-libusb.so [pending]
    libudev.so: for the hidraw backend -- hidapi-hidraw.so [installed]
installing hiredis...
installing hwids...
installing libmnl...
installing libnftnl...
installing libnl...
installing libpcap...
installing libnfnetlink...
installing libnetfilter_conntrack...
installing iptables...
installing kbd...
installing kmod...
installing ldns...
Optional dependencies for ldns
    libpcap: ldns-dpa tool [installed]
installing libjpeg-turbo...
Optional dependencies for libjpeg-turbo
    java-runtime>11: for TurboJPEG Java wrapper
installing libtiff...
Optional dependencies for libtiff
    freeglut: for using tiffgt
installing libusb...
installing libcups...
installing libpciaccess...
installing libdrm...
installing libedit...
installing libevdev...
installing xcb-proto...
installing libxdmcp...
installing libxau...
installing libxcb...
installing xorgproto...
installing libx11...
installing libxext...
installing wayland...
installing libxxf86vm...
installing libxfixes...
installing libxdamage...
installing libxshmfence...
installing libomxil-bellagio...
installing libunwind...
installing llvm-libs...
installing lm_sensors...
Optional dependencies for lm_sensors
    rrdtool: for logging with sensord
    perl: for sensor detection and configuration convert [installed]
installing vulkan-icd-loader...
Optional dependencies for vulkan-icd-loader
    vulkan-driver: packaged vulkan driver
installing mesa...
Optional dependencies for mesa
    opengl-man-pages: for the OpenGL API man pages
    mesa-vdpau: for accelerated video playback
    libva-mesa-driver: for accelerated video playback
installing libglvnd...
installing systemd...
Initializing machine ID from random generator.
Creating group sys with gid 3.
Creating group mem with gid 8.
Creating group ftp with gid 11.
Creating group mail with gid 12.
Creating group log with gid 19.
Creating group smmsp with gid 25.
Creating group proc with gid 26.
Creating group games with gid 50.
Creating group lock with gid 54.
Creating group network with gid 90.
Creating group floppy with gid 94.
Creating group scanner with gid 96.
Creating group power with gid 98.
Creating group adm with gid 999.
Creating group wheel with gid 998.
Creating group utmp with gid 997.
Creating group audio with gid 996.
Creating group disk with gid 995.
Creating group input with gid 994.
Creating group kmem with gid 993.
Creating group kvm with gid 992.
Creating group lp with gid 991.
Creating group optical with gid 990.
Creating group render with gid 989.
Creating group sgx with gid 988.
Creating group storage with gid 987.
Creating group tty with gid 5.
Creating group uucp with gid 986.
Creating group video with gid 985.
Creating group users with gid 984.
Creating group systemd-journal with gid 983.
Creating group rfkill with gid 982.
Creating group bin with gid 1.
Creating user bin (n/a) with uid 1 and gid 1.
Creating group daemon with gid 2.
Creating user daemon (n/a) with uid 2 and gid 2.
Creating user mail (n/a) with uid 8 and gid 12.
Creating user ftp (n/a) with uid 14 and gid 11.
Creating group http with gid 33.
Creating user http (n/a) with uid 33 and gid 33.
Creating group avahi with gid 981.
Creating user avahi (Avahi mDNS/DNS-SD daemon) with uid 981 and gid 981.
Creating group nobody with gid 65534.
Creating user nobody (Nobody) with uid 65534 and gid 65534.
Creating group dbus with gid 81.
Creating user dbus (System Message Bus) with uid 81 and gid 81.
Creating group git with gid 980.
Creating user git (git daemon user) with uid 980 and gid 980.
Creating group systemd-journal-remote with gid 979.
Creating user systemd-journal-remote (systemd Journal Remote) with uid 979 and gid 979.
Creating group systemd-network with gid 978.
Creating user systemd-network (systemd Network Management) with uid 978 and gid 978.
Creating group systemd-oom with gid 977.
Creating user systemd-oom (systemd Userspace OOM Killer) with uid 977 and gid 977.
Creating group systemd-resolve with gid 976.
Creating user systemd-resolve (systemd Resolver) with uid 976 and gid 976.
Creating group systemd-timesync with gid 975.
Creating user systemd-timesync (systemd Time Synchronization) with uid 975 and gid 975.
Creating group systemd-coredump with gid 974.
Creating user systemd-coredump (systemd Core Dumper) with uid 974 and gid 974.
Creating group uuidd with gid 68.
Creating user uuidd (n/a) with uid 68 and gid 68.
Created symlink /etc/systemd/system/getty.target.wants/getty@tty1.service → /usr/lib/systemd/system/getty@.service.
Created symlink /etc/systemd/system/multi-user.target.wants/remote-fs.target → /usr/lib/systemd/system/remote-fs.target.
:: Append 'init=/usr/lib/systemd/systemd' to your kernel command line in your
   bootloader to replace sysvinit with systemd, or install systemd-sysvcompat
Optional dependencies for systemd
    libmicrohttpd: remote journald capabilities
    quota-tools: kernel-level quota management
    systemd-sysvcompat: symlink package to provide sysvinit binaries
    polkit: allow administration as unprivileged user
    curl: machinectl pull-tar and pull-raw [installed]
    libfido2: unlocking LUKS2 volumes with FIDO2 token
    tpm2-tss: unlocking LUKS2 volumes with TPM2
installing libgudev...
installing libice...
installing mtdev...
installing libwacom...
installing libinput...
Optional dependencies for libinput
    gtk3: libinput debug-gui
    python-pyudev: libinput measure
    python-libevdev: libinput measure
installing libpgm...
installing libproxy...
Optional dependencies for libproxy
    networkmanager: NetworkManager configuration module
    perl: Perl bindings [installed]
    python: Python 3.x bindings [pending]
    libproxy-webkit: PAC proxy support (via WebKit)
installing libsm...
installing libsodium...
installing libxi...
installing xkeyboard-config...
installing libxkbcommon...
Optional dependencies for libxkbcommon
    libxkbcommon-x11: xkbcli interactive-x11 [pending]
    wayland: xkbcli interactive-wayland [installed]
installing libxkbcommon-x11...
installing libxt...
installing libxmu...
installing libxrender...
installing make...
installing md4c...
installing zeromq...
installing python...
Optional dependencies for python
    python-setuptools
    python-pip
    sqlite [installed]
    mpdecimal: for decimal
    xz: for lzma [installed]
    tk: for tkinter
installing pcsclite...
installing protobuf...
installing monero...
installing pacman-mirrorlist...
installing pacman...
Optional dependencies for pacman
    perl-locale-gettext: translation support in makepkg-template
installing patch...
Optional dependencies for patch
    ed: for patch -e functionality
installing pkgconf...
installing protobuf-c...
installing xcb-util-keysyms...
installing xcb-util-renderutil...
installing which...
installing xorg-xset...
installing xorg-xprop...
installing xdg-utils...
Optional dependencies for xdg-utils
    kde-cli-tools: for KDE Plasma5 support in xdg-open
    exo: for Xfce support in xdg-open
    pcmanfm: for LXDE support in xdg-open
    perl-file-mimeinfo: for generic support in xdg-open
    perl-net-dbus: Perl extension to dbus used in xdg-screensaver
    perl-x11-protocol: Perl X11 protocol used in xdg-screensaver
installing shared-mime-info...
installing xcb-util-wm...
installing xcb-util...
installing xcb-util-image...
installing tslib...
installing qt5-base...
Optional dependencies for qt5-base
    qt5-svg: to use SVG icon themes [pending]
    qt5-wayland: to run Qt applications in a Wayland session
    qt5-translations: for some native UI translations
    postgresql-libs: PostgreSQL driver
    mariadb-libs: MariaDB driver
    unixodbc: ODBC driver
    libfbclient: Firebird/iBase driver
    freetds: MS SQL driver
    gtk3: GTK platform plugin
    perl: for fixqt4headers and syncqt [installed]
installing qt5-declarative...
installing qt5-graphicaleffects...
installing qt5-quickcontrols...
installing qt5-quickcontrols2...
Optional dependencies for qt5-quickcontrols2
    qt5-graphicaleffects: for the Material style [installed]
installing qt5-svg...
installing qt5-tools...
Optional dependencies for qt5-tools
    clang: for qdoc
    qt5-webkit: for Qt Assistant
installing qt5-xmlpatterns...
Optional dependencies for qt5-xmlpatterns
    qt5-declarative: QML bindings [installed]
installing sudo...
installing unbound...
Optional dependencies for unbound
    expat: for unbound-anchor [installed]
    sh: for unbound-control-setup [installed]
    python: for python-bindings [installed]
:: Running post-transaction hooks...
( 1/16) Creating system user accounts...
Creating group monero with gid 973.
Creating user monero (n/a) with uid 973 and gid 973.
Creating group unbound with gid 972.
Creating user unbound (unbound) with uid 972 and gid 972.
( 2/16) Updating journal message catalog...
( 3/16) Reloading system manager configuration...
  Skipped: Running in chroot.
( 4/16) Updating udev hardware database...
( 5/16) Applying kernel sysctl settings...
  Skipped: Running in chroot.
( 6/16) Creating temporary files...
( 7/16) Reloading device manager configuration...
  Skipped: Running in chroot.
( 8/16) Arming ConditionNeedsUpdate...
( 9/16) Updating the MIME type database...
(10/16) Updating fontconfig configuration...
(11/16) Rebuilding certificate stores...
(12/16) Reloading system bus configuration...
  Skipped: Running in chroot.
(13/16) Warn about old perl modules
(14/16) Updating fontconfig cache...
(15/16) Updating the info directory file...
(16/16) Updating trusted-key.key for unbound...
:: Starting full system upgrade...
looking for conflicting packages...

Packages (1) devtools-20210202-3

Total Installed Size:  0.16 MiB

:: Proceed with installation? [Y/n] 
checking keyring...
checking package integrity...
loading package files...
checking for file conflicts...
checking available disk space...
:: Processing package changes...
installing devtools...
Optional dependencies for devtools
    btrfs-progs: btrfs support
:: Running post-transaction hooks...
(1/1) Arming ConditionNeedsUpdate...
'/usr/share/devtools/makepkg-x86_64.conf' -> '/mnt/etc/makepkg.conf'
Generating locales...
  en_US.UTF-8... done
  de_DE.UTF-8... done
Generation complete.
==> Making package: monero-gui 0.17.3.0-2 (Thu 16 Dec 2021 06:33:58 AM UTC)
==> Checking runtime dependencies...
warning: database file for 'core' does not exist (use '-Sy' to download)
warning: database file for 'extra' does not exist (use '-Sy' to download)
warning: database file for 'community' does not exist (use '-Sy' to download)
==> Checking buildtime dependencies...
warning: database file for 'core' does not exist (use '-Sy' to download)
warning: database file for 'extra' does not exist (use '-Sy' to download)
warning: database file for 'community' does not exist (use '-Sy' to download)
==> Retrieving sources...
Cloning into bare repository '/startdir/monero-gui'...
  -> Cloning monero-gui git repo...
  -> Cloning monero git repo...
Cloning into bare repository '/startdir/monero'...
  -> Cloning unbound git repo...
Cloning into bare repository '/startdir/unbound'...
  -> Cloning miniupnp git repo...
Cloning into bare repository '/startdir/miniupnp'...
  -> Cloning rapidjson git repo...
Cloning into bare repository '/startdir/rapidjson'...
  -> Cloning trezor-common git repo...
Cloning into bare repository '/startdir/trezor-common'...
Cloning into bare repository '/startdir/randomx'...
  -> Cloning randomx git repo...
  -> Cloning supercop git repo...
Cloning into bare repository '/startdir/supercop'...
==> WARNING: Skipping verification of source file PGP signatures.
  -> Found monero-gui.desktop
==> Validating source files with sha512sums...
    monero-gui ... Skipped
    monero ... Skipped
    unbound ... Skipped
    miniupnp ... Skipped
    rapidjson ... Skipped
    trezor-common ... Skipped
    randomx ... Skipped
    supercop ... Skipped
    monero-gui.desktop ... Passed
==> Extracting sources...
  -> Creating working copy of monero-gui git repo...
Cloning into 'monero-gui'...
done.
Switched to a new branch 'makepkg'
  -> Creating working copy of monero git repo...
Cloning into 'monero'...
done.
  -> Creating working copy of unbound git repo...
Cloning into 'unbound'...
done.
  -> Creating working copy of miniupnp git repo...
Cloning into 'miniupnp'...
done.
Cloning into 'rapidjson'...
  -> Creating working copy of rapidjson git repo...
done.
Cloning into 'trezor-common'...
  -> Creating working copy of trezor-common git repo...
done.
  -> Creating working copy of randomx git repo...
Cloning into 'randomx'...
done.
  -> Creating working copy of supercop git repo...
Cloning into 'supercop'...
done.
==> Starting prepare()...
Submodule 'external/quirc' (https://github.com/dlbeer/quirc/) registered for path 'external/quirc'
Submodule 'monero' (https://github.com/monero-project/monero) registered for path 'monero'
Cloning into '/build/monero-gui/src/monero-gui/external/quirc'...
Cloning into '/build/monero-gui/src/monero-gui/monero'...
done.
Submodule path 'external/quirc': checked out '7e7ab596e4d0988faf1c12ae89c354b114181c40'
Submodule path 'monero': checked out 'ab18fea3500841fc312630d49ed6840b3aedb34d'
Cloning into '/build/monero-gui/src/monero-gui/monero/external/miniupnp'...
done.
Cloning into '/build/monero-gui/src/monero-gui/monero/external/randomx'...
done.
Cloning into '/build/monero-gui/src/monero-gui/monero/external/rapidjson'...
done.
Cloning into '/build/monero-gui/src/monero-gui/monero/external/supercop'...
done.
Cloning into '/build/monero-gui/src/monero-gui/monero/external/trezor-common'...
done.
Cloning into '/build/monero-gui/src/monero-gui/monero/external/unbound'...
done.
Submodule path 'external/miniupnp': checked out '544e6fcc73c5ad9af48a8985c94f0f1d742ef2e0'
Submodule path 'external/randomx': checked out '9efc398c196ef1c50d8e6f5e1f2c5ac02f1f6ceb'
Submodule path 'external/rapidjson': checked out '129d19ba7f496df5e33658527a7158c79b99c21c'
From /build/monero-gui/src/supercop
 * branch            633500ad8c8759995049ccd022107d1fa8a1bbc9 -> FETCH_HEAD
Submodule path 'external/supercop': checked out '633500ad8c8759995049ccd022107d1fa8a1bbc9'
Submodule path 'external/trezor-common': checked out 'bff7fdfe436c727982cc553bdfb29a9021b423b0'
From /build/monero-gui/src/unbound
 * branch              0f6c0579d66b65f86066e30e7876105ba2775ef4 -> FETCH_HEAD
Submodule path 'external/unbound': checked out '0f6c0579d66b65f86066e30e7876105ba2775ef4'
==> Starting build()...
-- The C compiler identification is GNU 11.1.0
-- The CXX compiler identification is GNU 11.1.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Initiating compile using CMake 3.22.1
-- Found Git: /usr/bin/git (found version "2.34.1") 
-- Checking submodules
-- Submodule 'monero' is up-to-date
-- Found PythonInterp: /usr/bin/python (found version "3.10.1") 
-- CMake version 3.22.1
-- ccache NOT found! Please install it for faster rebuilds.
-- The ASM compiler identification is GNU
-- Found assembler: /usr/bin/cc
-- Looking for -Wl,--no-undefined linker flag
-- Looking for -Wl,--no-undefined linker flag - found
-- Looking for -Wl,-undefined,error linker flag
-- Looking for -Wl,-undefined,error linker flag - found
-- Building without build tag
-- Checking submodules
-- Submodule 'external/miniupnp' is up-to-date
-- Submodule 'external/unbound' is up-to-date
-- Submodule 'external/rapidjson' is up-to-date
-- Submodule 'external/trezor-common' is up-to-date
-- Submodule 'external/randomx' is up-to-date
-- Submodule 'external/supercop' is up-to-date
-- Could not find DEVELOPER_LOCAL_TOOLS in env (not required)
-- BOOST_IGNORE_SYSTEM_PATHS defaults to OFF
-- Could not find DEVELOPER_LIBUNBOUND_OLD in env (not required)
-- Building for a 64-bit system
-- Building internal libraries as static
-- Using LMDB as default DB type
-- Stack trace on exception enabled (using easylogging++)
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Failed
-- Check if compiler accepts -pthread
-- Check if compiler accepts -pthread - yes
-- Found Threads: TRUE  
-- Performing Test _Werror__pthread_c
-- Performing Test _Werror__pthread_c - Success
-- Performing Test _Werror__pthread_cxx
-- Performing Test _Werror__pthread_cxx - Success
-- Found OpenSSL: /usr/lib/libcrypto.so (found version "1.1.1l")  
-- Using OpenSSL include dir at /usr/include
-- Found HIDAPI: /usr/lib/libhidapi-libusb.so  
-- Looking for memset_s in c
-- Looking for memset_s in c - not found
-- Looking for explicit_bzero in c
-- Looking for explicit_bzero in c - found
-- Looking for strptime
-- Looking for strptime - found
CMake Warning (dev) at /usr/share/cmake-3.22/Modules/FindPackageHandleStandardArgs.cmake:438 (message):
  The package name passed to `find_package_handle_standard_args` (MiniUPnPc)
  does not match the name of the calling package (Miniupnpc).  This can lead
  to problems in calling code that expects `find_package` result variables
  (e.g., `_FOUND`) to follow a certain pattern.
Call Stack (most recent call first):
  monero/cmake/FindMiniupnpc.cmake:39 (find_package_handle_standard_args)
  monero/external/CMakeLists.txt:38 (find_package)
This warning is for project developers.  Use -Wno-dev to suppress it.

-- Could NOT find MiniUPnPc (missing: MINIUPNP_INCLUDE_DIR MINIUPNP_LIBRARY) 
-- Using in-tree miniupnpc
-- Looking for libunbound
-- Found libunbound include (unbound.h) in /usr/include
-- Found libunbound shared library
-- Using 64-bit LMDB from source tree
-- Looking for backtrace
-- Looking for backtrace - found
-- backtrace facility detected in default set of libraries
-- Backtrace_LIBRARY: 
-- Found Backtrace: /usr/include  
-- Performing Test _maes_cxx
-- Performing Test _maes_cxx - Success
-- Setting CXX flag -maes
-- Performing Test _maes_c
-- Performing Test _maes_c - Success
-- Setting C flag -maes
-- Performing Test HAVE_SSSE3
-- Performing Test HAVE_SSSE3 - Success
-- Performing Test HAVE_AVX2
-- Performing Test HAVE_AVX2 - Success
-- Performing Test HAVE_CXX_ATOMICS
-- Performing Test HAVE_CXX_ATOMICS - Success
-- Using HIDAPI include dir at /usr/include/hidapi
-- Found Protobuf: /usr/lib/libprotobuf.so;-pthread (found version "3.17.3") 
-- Protobuf lib: /usr/lib/libprotobuf.so, inc: /usr/include, protoc: /usr/bin/protoc
-- Trezor protobuf messages regenerated out: "."
-- Found PkgConfig: /usr/bin/pkg-config (found version "1.8.0") 
-- Checking for module 'libusb-1.0'
--   Found libusb-1.0, version 1.0.24
-- Looking for libusb_get_device_list in /usr/lib/libusb-1.0.so
-- Looking for libusb_get_device_list in /usr/lib/libusb-1.0.so - found
-- Looking for libusb_get_port_numbers in /usr/lib/libusb-1.0.so
-- Looking for libusb_get_port_numbers in /usr/lib/libusb-1.0.so - found
-- LibUSB Compilation test: TRUE
-- Trezor compatible LibUSB found at: /usr/include/libusb-1.0
-- Building on x86_64 for default
-- AES support enabled
-- Performing Test _Werror__Wformat_c
-- Performing Test _Werror__Wformat_c - Success
-- Performing Test _Werror__Wformat_cxx
-- Performing Test _Werror__Wformat_cxx - Success
-- Performing Test _Werror__Wformat_security_c
-- Performing Test _Werror__Wformat_security_c - Failed
-- Performing Test _Werror__Wformat_security_cxx
-- Performing Test _Werror__Wformat_security_cxx - Failed
-- Performing Test _Werror__fstack_protector_c
-- Performing Test _Werror__fstack_protector_c - Success
-- Performing Test _Werror__fstack_protector_cxx
-- Performing Test _Werror__fstack_protector_cxx - Success
-- Performing Test _Werror__fstack_protector_strong_c
-- Performing Test _Werror__fstack_protector_strong_c - Success
-- Performing Test _Werror__fstack_protector_strong_cxx
-- Performing Test _Werror__fstack_protector_strong_cxx - Success
-- Performing Test _Werror__fcf_protection=full_c
-- Performing Test _Werror__fcf_protection=full_c - Success
-- Performing Test _Werror__fcf_protection=full_cxx
-- Performing Test _Werror__fcf_protection=full_cxx - Success
-- Performing Test _Werror__fstack_clash_protection_c
-- Performing Test _Werror__fstack_clash_protection_c - Success
-- Performing Test _Werror__fstack_clash_protection_cxx
-- Performing Test _Werror__fstack_clash_protection_cxx - Success
-- Looking for -pie linker flag
-- Looking for -pie linker flag - found
-- Looking for -Wl,-z,relro linker flag
-- Looking for -Wl,-z,relro linker flag - found
-- Looking for -Wl,-z,now linker flag
-- Looking for -Wl,-z,now linker flag - found
-- Looking for -Wl,-z,noexecstack linker flag
-- Looking for -Wl,-z,noexecstack linker flag - found
-- Looking for -Wl,-z,noexecheap linker flag
-- Looking for -Wl,-z,noexecheap linker flag - not found
-- Using C security hardening flags:  -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -fstack-protector -fstack-protector-strong -fcf-protection=full -fstack-clash-protection
-- Using C++ security hardening flags:  -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -fstack-protector -fstack-protector-strong -fcf-protection=full -fstack-clash-protection
-- Using linker security hardening flags:  -pie -Wl,-z,relro -Wl,-z,now -Wl,-z,noexecstack
-- Found Boost Version: 107600
-- Looking for rl_copy_text
-- Looking for rl_copy_text - found
-- Looking for rl_filename_completion_function
-- Looking for rl_filename_completion_function - found
-- Found readline library at: /usr
-- Found Git: /usr/bin/git
-- You are currently on commit ab18fea35
-- You are building a tagged release
-- Looking for a ASM-ATT compiler
Wallet crypto is using amd64-64-24k backend
-- Looking for a ASM-ATT compiler - /usr/bin/as
-- Trezor support enabled
Doxygen: graphviz not found - graphs disabled
CMake Warning (dev) at monero/CMakeLists.txt:1126 (option):
  Policy CMP0077 is not set: option() honors normal variables.  Run "cmake
  --help-policy CMP0077" for policy details.  Use the cmake_policy command to
  set the policy and suppress this warning.

  For compatibility with older versions of CMake, option is clearing the
  normal variable 'BUILD_GUI_DEPS'.
This warning is for project developers.  Use -Wno-dev to suppress it.

-- Not building tests
-- Not building debug utilities
-- Could NOT find Doxygen (missing: DOXYGEN_EXECUTABLE) 
-- Found Git: /usr/bin/git
-- You are currently on commit bddb9b005
-- You are building a tagged release
-- /build/monero-gui/src/monero-gui/cmake
-- libsodium: libraries at /usr/lib/libsodium.so
-- Found X11: /usr/include   
-- Looking for XOpenDisplay in /usr/lib/libX11.so;/usr/lib/libXext.so
-- Looking for XOpenDisplay in /usr/lib/libX11.so;/usr/lib/libXext.so - found
-- Looking for gethostbyname
-- Looking for gethostbyname - found
-- Looking for connect
-- Looking for connect - found
-- Looking for remove
-- Looking for remove - found
-- Looking for shmat
-- Looking for shmat - found
-- Looking for IceConnectionNumber in ICE
-- Looking for IceConnectionNumber in ICE - found
-- X11_FOUND = TRUE
-- X11_INCLUDE_DIR = /usr/include
-- X11_LIBRARIES = /usr/lib/libSM.so;/usr/lib/libICE.so;/usr/lib/libX11.so;/usr/lib/libXext.so
-- Checking for modules 'Qt5Core;Qt5Quick;Qt5Gui;Qt5Qml;Qt5Svg;Qt5Xml;Qt5QmlModels;Qt5XmlPatterns'
--   Found Qt5Core, version 5.15.2
--   Found Qt5Quick, version 5.15.2
--   Found Qt5Gui, version 5.15.2
--   Found Qt5Qml, version 5.15.2
--   Found Qt5Svg, version 5.15.2
--   Found Qt5Xml, version 5.15.2
--   Found Qt5QmlModels, version 5.15.2
--   Found Qt5XmlPatterns, version 5.15.2
-- Performing Test _Werror__fno_strict_aliasing_c
-- Performing Test _Werror__fno_strict_aliasing_c - Success
-- Performing Test _Werror__fno_strict_aliasing_cxx
-- Performing Test _Werror__fno_strict_aliasing_cxx - Success
-- Performing Test _Werror__fPIC_c
-- Performing Test _Werror__fPIC_c - Success
-- Performing Test _Werror__fPIC_cxx
-- Performing Test _Werror__fPIC_cxx - Success
-- Using C security hardening flags:  -Wformat -fstack-protector -fstack-protector-strong -fcf-protection=full -fstack-clash-protection -fno-strict-aliasing -fPIC
-- Using C++ security hardening flags:  -Wformat -fstack-protector -fstack-protector-strong -fcf-protection=full -fstack-clash-protection -fno-strict-aliasing -fPIC
-- Using linker security hardening flags:  -pie -Wl,-z,relro -Wl,-z,now -Wl,-z,noexecstack
-- OpenGL: include dir at 
-- OpenGL: libraries at 
-- Configuring done
CMake Warning (dev) at monero/src/CMakeLists.txt:93 (add_library):
  Policy CMP0115 is not set: Source file extensions must be explicit.  Run
  "cmake --help-policy CMP0115" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  File:

    /build/monero-gui/src/monero-gui/monero/src/rpc/instanciations.cpp
Call Stack (most recent call first):
  monero/src/CMakeLists.txt:81 (monero_add_library_with_deps)
  monero/src/rpc/CMakeLists.txt:101 (monero_add_library)
This warning is for project developers.  Use -Wno-dev to suppress it.

-- Generating done
-- Build files have been written to: /build/monero-gui/src/monero-gui/build
[  0%] Built target genversiongui
[  0%] Automatic MOC and UIC for target gui_version
[  0%] Creating directories for 'generate_translations_header'
[  0%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/igd_desc_parse.c.o
[  0%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-shared.dir/igd_desc_parse.c.o
[  1%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-shared.dir/miniupnpc.c.o
[  1%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/minixml.c.o
[  1%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-shared.dir/minixml.c.o
[  2%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/miniupnpc.c.o
[  2%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/minisoap.c.o
[  2%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-shared.dir/minisoap.c.o
[  2%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/testminixml.dir/testminixml.c.o
[  2%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/minixmlvalid.dir/minixmlvalid.c.o
[  2%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/testminiwget.dir/testminiwget.c.o
[  2%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/testaddr_is_reserved.dir/testaddr_is_reserved.c.o
[  2%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/testupnpreplyparse.dir/testupnpreplyparse.c.o
[  2%] Built target gui_version_autogen
[  2%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/testigddescparse.dir/testigddescparse.c.o
[  2%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/minissdpc.c.o
[  3%] Building C object monero/external/db_drivers/liblmdb/CMakeFiles/lmdb.dir/mdb.c.o
[  3%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-shared.dir/minissdpc.c.o
[  3%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-shared.dir/miniwget.c.o
[  3%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/testaddr_is_reserved.dir/addr_is_reserved.c.o
[  4%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/miniwget.c.o
[  4%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/testminixml.dir/minixml.c.o
[  4%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/testminiwget.dir/miniwget.c.o
[  4%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/testupnpreplyparse.dir/minixml.c.o
[  4%] No download step for 'generate_translations_header'
[  5%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/minixmlvalid.dir/minixml.c.o
[  5%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/testigddescparse.dir/igd_desc_parse.c.o
[  5%] Linking C executable testaddr_is_reserved
[  5%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/upnpcommands.c.o
[  5%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-shared.dir/upnpcommands.c.o
[  5%] No update step for 'generate_translations_header'
[  6%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/upnpdev.c.o
[  7%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/testigddescparse.dir/minixml.c.o
[  7%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/testminixml.dir/igd_desc_parse.c.o
[  7%] No patch step for 'generate_translations_header'
[  7%] Built target testaddr_is_reserved
[  8%] Performing configure step for 'generate_translations_header'
[  8%] Linking C executable minixmlvalid
[  8%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/upnpreplyparse.c.o
[  9%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/testupnpreplyparse.dir/upnpreplyparse.c.o
[ 10%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-shared.dir/upnpdev.c.o
[ 10%] Building CXX object monero/external/easylogging++/CMakeFiles/easylogging.dir/easylogging++.cc.o
[ 10%] Linking C executable testminixml
[ 10%] Built target minixmlvalid
[ 10%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/testigddescparse.dir/miniupnpc.c.o
[ 10%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/upnperrors.c.o
-- The C compiler identification is GNU 11.1.0
[ 10%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-shared.dir/upnpreplyparse.c.o
[ 10%] Linking C executable testupnpreplyparse
[ 10%] Building CXX object monero/external/qrcodegen/CMakeFiles/qrcodegen.dir/QrCode.cpp.o
[ 10%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-shared.dir/upnperrors.c.o
[ 10%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/connecthostport.c.o
[ 10%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/portlistingparse.c.o
[ 10%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/testigddescparse.dir/miniwget.c.o
[ 10%] Built target testminixml
[ 10%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/testminiwget.dir/miniupnpc.c.o
[ 11%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/receivedata.c.o
[ 11%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-shared.dir/connecthostport.c.o
[ 11%] Built target testupnpreplyparse
[ 11%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/listdevices.c.o
[ 11%] Built target genversion
[ 11%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-shared.dir/portlistingparse.c.o
[ 11%] Building C object monero/src/crypto/CMakeFiles/obj_cncrypto.dir/aesb.c.o
[ 11%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-static.dir/addr_is_reserved.c.o
[ 12%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-shared.dir/receivedata.c.o
[ 12%] Building CXX object monero/external/randomx/CMakeFiles/randomx.dir/src/aes_hash.cpp.o
[ 12%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-shared.dir/listdevices.c.o
-- The CXX compiler identification is GNU 11.1.0
[ 12%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-shared.dir/addr_is_reserved.c.o
[ 13%] Building C object monero/src/crypto/CMakeFiles/obj_cncrypto.dir/blake256.c.o
-- Detecting C compiler ABI info
[ 13%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/testigddescparse.dir/minissdpc.c.o
[ 13%] Building C object monero/src/crypto/CMakeFiles/obj_cncrypto.dir/chacha.c.o
[ 13%] Linking C static library libminiupnpc.a
[ 13%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/testigddescparse.dir/upnpcommands.c.o
[ 15%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/testigddescparse.dir/upnpreplyparse.c.o
[ 15%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/testigddescparse.dir/minisoap.c.o
[ 15%] Linking C shared library libminiupnpc.so
[ 15%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/testminiwget.dir/minisoap.c.o
[ 15%] Building C object monero/src/crypto/CMakeFiles/obj_cncrypto.dir/crypto-ops-data.c.o
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
[ 15%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/testigddescparse.dir/connecthostport.c.o
[ 15%] Building C object monero/src/crypto/CMakeFiles/obj_cncrypto.dir/crypto-ops.c.o
[ 15%] Built target libminiupnpc-static
[ 15%] Building CXX object monero/src/crypto/CMakeFiles/obj_cncrypto.dir/crypto.cpp.o
[ 15%] Built target libminiupnpc-shared
[ 15%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/testigddescparse.dir/portlistingparse.c.o
Scanning dependencies of target monero-crypto-amd64-64-24k
[ 15%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/testigddescparse.dir/receivedata.c.o
[ 16%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/testminiwget.dir/upnpcommands.c.o
[ 16%] Building C object monero/monero_crypto_src/amd64/CMakeFiles/monero-crypto-amd64-64-24k.dir/amd64-64-24k.c.o
[ 17%] Building CXX object monero/src/ringct/CMakeFiles/obj_ringct_basic.dir/rctOps.cpp.o
[ 17%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/testigddescparse.dir/addr_is_reserved.c.o
[ 17%] Building C object monero/src/crypto/CMakeFiles/obj_cncrypto.dir/groestl.c.o
-- Detecting CXX compiler ABI info - done
[ 18%] Building C object monero/src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-blake.c.o
In file included from /build/monero-gui/src/monero-gui/monero/external/supercop/src/amd64/../../crypto_sign/ed25519/amd64-64-24k/ge25519.h:5,
                 from /build/monero-gui/src/monero-gui/monero/external/supercop/src/amd64/amd64-64-24k.c:38:
/build/monero-gui/src/monero-gui/monero/external/supercop/src/amd64/amd64.c.inc: In function ‘scalarmult_p1p1’:
/build/monero-gui/src/monero-gui/monero/external/supercop/src/amd64/../../crypto_sign/ed25519/amd64-64-24k/sc25519.h:18:34: warning: ‘crypto_sign_ed25519_amd64_64_sc25519_window4’ accessing 85 bytes in a region of size 64 [-Wstringop-overflow=]
   18 | #define sc25519_window4          crypto_sign_ed25519_amd64_64_sc25519_window4
/build/monero-gui/src/monero-gui/monero/external/supercop/src/amd64/../../crypto_sign/ed25519/amd64-64-24k/sc25519.h:18:34: note: in definition of macro ‘sc25519_window4’
   18 | #define sc25519_window4          crypto_sign_ed25519_amd64_64_sc25519_window4
      |                                  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/build/monero-gui/src/monero-gui/monero/external/supercop/src/amd64/../../crypto_sign/ed25519/amd64-64-24k/sc25519.h:18:34: note: referencing argument 1 of type ‘signed char *’
   18 | #define sc25519_window4          crypto_sign_ed25519_amd64_64_sc25519_window4
/build/monero-gui/src/monero-gui/monero/external/supercop/src/amd64/../../crypto_sign/ed25519/amd64-64-24k/sc25519.h:18:34: note: in definition of macro ‘sc25519_window4’
   18 | #define sc25519_window4          crypto_sign_ed25519_amd64_64_sc25519_window4
      |                                  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/build/monero-gui/src/monero-gui/monero/external/supercop/src/amd64/../../crypto_sign/ed25519/amd64-64-24k/sc25519.h:18:34: note: in a call to function ‘crypto_sign_ed25519_amd64_64_sc25519_window4’
   18 | #define sc25519_window4          crypto_sign_ed25519_amd64_64_sc25519_window4
      |                                  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/build/monero-gui/src/monero-gui/monero/external/supercop/src/amd64/../../crypto_sign/ed25519/amd64-64-24k/sc25519.h:18:34: note: in definition of macro ‘sc25519_window4’
   18 | #define sc25519_window4          crypto_sign_ed25519_amd64_64_sc25519_window4
      |                                  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- Check for working CXX compiler: /usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
[ 18%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/testminiwget.dir/minissdpc.c.o
lrelease version 5.15.2
-- Configuring done
[ 18%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/testminiwget.dir/upnpreplyparse.c.o
[ 18%] Building C object monero/external/randomx/CMakeFiles/randomx.dir/src/argon2_ref.c.o
[ 18%] Building C object monero/src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-groestl.c.o
-- Generating done
-- Build files have been written to: /build/monero-gui/src/monero-gui/build/monero/translations
[ 18%] Building ASM object monero/monero_crypto_src/amd64/CMakeFiles/monero-crypto-amd64-64-24k.dir/amd64-64-24k-choose_tp.s.o
[ 19%] Building ASM object monero/monero_crypto_src/amd64/CMakeFiles/monero-crypto-amd64-64-24k.dir/__/__/crypto_sign/ed25519/amd64-64-24k/choose_t.s.o
[ 19%] Performing build step for 'generate_translations_header'
[ 19%] Building C object monero/src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-jh.c.o
[ 19%] Building C object monero/monero_crypto_src/amd64/CMakeFiles/monero-crypto-amd64-64-24k.dir/__/__/crypto_sign/ed25519/amd64-64-24k/consts.s.o
[ 20%] Linking C executable testigddescparse
[ 20%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/testminiwget.dir/minixml.c.o
[ 20%] Building C object monero/monero_crypto_src/amd64/CMakeFiles/monero-crypto-amd64-64-24k.dir/__/__/crypto_sign/ed25519/amd64-64-24k/fe25519_getparity.c.o
[ 20%] Building C object monero/src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-skein.c.o
[ 50%] Building C object CMakeFiles/generate_translations_header.dir/generate_translations_header.c.o
[ 20%] Built target testigddescparse
[ 20%] Building ASM object monero/monero_crypto_src/amd64/CMakeFiles/monero-crypto-amd64-64-24k.dir/__/__/crypto_sign/ed25519/amd64-64-24k/fe25519_freeze.s.o
[ 20%] Building C object monero/src/crypto/CMakeFiles/obj_cncrypto.dir/hash.c.o
[ 20%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/testminiwget.dir/igd_desc_parse.c.o
[100%] Linking C executable generate_translations_header
[ 21%] Building C object monero/monero_crypto_src/amd64/CMakeFiles/monero-crypto-amd64-64-24k.dir/__/__/crypto_sign/ed25519/amd64-64-24k/fe25519_invert.c.o
[ 21%] Building CXX object monero/src/ringct/CMakeFiles/obj_ringct.dir/rctSigs.cpp.o
[ 21%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/testminiwget.dir/connecthostport.c.o
Updating 'monero.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 1148 untranslated source text(s)
[ 22%] Building C object monero/src/crypto/CMakeFiles/obj_cncrypto.dir/hmac-keccak.c.o
Updating 'monero_ar.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 1148 untranslated source text(s)
[ 23%] Building C object monero/monero_crypto_src/amd64/CMakeFiles/monero-crypto-amd64-64-24k.dir/__/__/crypto_sign/ed25519/amd64-64-24k/fe25519_iseq.c.o
[ 23%] Building C object monero/src/crypto/CMakeFiles/obj_cncrypto.dir/jh.c.o
Updating 'monero_bg.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 1148 untranslated source text(s)
[ 23%] Building C object monero/external/randomx/CMakeFiles/randomx.dir/src/argon2_ssse3.c.o
[ 23%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/testminiwget.dir/portlistingparse.c.o
Updating 'monero_bn.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 1148 untranslated source text(s)
[ 23%] Building ASM object monero/monero_crypto_src/amd64/CMakeFiles/monero-crypto-amd64-64-24k.dir/__/__/crypto_sign/ed25519/amd64-64-24k/fe25519_mul.s.o
Updating 'monero_cat.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 1148 untranslated source text(s)
[ 23%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/testminiwget.dir/receivedata.c.o
[ 23%] Building C object monero/monero_crypto_src/amd64/CMakeFiles/monero-crypto-amd64-64-24k.dir/__/__/crypto_sign/ed25519/amd64-64-24k/fe25519_neg.c.o
Updating 'monero_cs.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 1148 untranslated source text(s)
Updating 'monero_da.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 1148 untranslated source text(s)
[ 23%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/testminiwget.dir/addr_is_reserved.c.o
[ 23%] Building C object monero/src/crypto/CMakeFiles/obj_cncrypto.dir/keccak.c.o
Updating 'monero_de.qm'...
    Generated 393 translation(s) (373 finished and 20 unfinished)
    Ignored 755 untranslated source text(s)
[ 23%] Building C object monero/monero_crypto_src/amd64/CMakeFiles/monero-crypto-amd64-64-24k.dir/__/__/crypto_sign/ed25519/amd64-64-24k/fe25519_pack.c.o
Updating 'monero_el.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 1148 untranslated source text(s)
[ 23%] Building C object monero/monero_crypto_src/amd64/CMakeFiles/monero-crypto-amd64-64-24k.dir/__/__/crypto_sign/ed25519/amd64-64-24k/fe25519_pow2523.c.o
[ 23%] Building C object monero/src/crypto/CMakeFiles/obj_cncrypto.dir/oaes_lib.c.o
[ 23%] Linking C executable testminiwget
Updating 'monero_eo.qm'...
[ 23%] Building C object monero/monero_crypto_src/amd64/CMakeFiles/monero-crypto-amd64-64-24k.dir/__/__/crypto_sign/ed25519/amd64-64-24k/fe25519_setint.c.o
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 1148 untranslated source text(s)
Updating 'monero_es.qm'...
    Generated 135 translation(s) (97 finished and 38 unfinished)
    Ignored 1013 untranslated source text(s)
/build/monero-gui/src/monero-gui/monero/src/crypto/oaes_lib.c: In function ‘oaes_get_seed’:
/build/monero-gui/src/monero-gui/monero/src/crypto/oaes_lib.c:515:9: warning: ‘ftime’ is deprecated: Use gettimeofday or clock_gettime instead [-Wdeprecated-declarations]
  515 |         ftime (&timer);
      |         ^~~~~
In file included from /build/monero-gui/src/monero-gui/monero/src/crypto/oaes_lib.c:45:
/usr/include/sys/timeb.h:29:12: note: declared here
   29 | extern int ftime (struct timeb *__timebuf)
      |            ^~~~~
[ 24%] Building ASM object monero/monero_crypto_src/amd64/CMakeFiles/monero-crypto-amd64-64-24k.dir/__/__/crypto_sign/ed25519/amd64-64-24k/fe25519_square.s.o
[ 24%] Building C object monero/monero_crypto_src/amd64/CMakeFiles/monero-crypto-amd64-64-24k.dir/__/__/crypto_sign/ed25519/amd64-64-24k/fe25519_unpack.c.o
Updating 'monero_fa.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 1148 untranslated source text(s)
Updating 'monero_fi.qm'...
[ 24%] Building C object monero/monero_crypto_src/amd64/CMakeFiles/monero-crypto-amd64-64-24k.dir/__/__/crypto_sign/ed25519/amd64-64-24k/ge25519_add.c.o
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 1148 untranslated source text(s)
[ 24%] Built target testminiwget
[ 24%] Building ASM object monero/monero_crypto_src/amd64/CMakeFiles/monero-crypto-amd64-64-24k.dir/__/__/crypto_sign/ed25519/amd64-64-24k/ge25519_add_p1p1.s.o
Updating 'monero_fr.qm'...
    Generated 1023 translation(s) (1023 finished and 0 unfinished)
    Ignored 125 untranslated source text(s)
[ 24%] Building C object monero/src/crypto/CMakeFiles/obj_cncrypto.dir/random.c.o
Updating 'monero_ga.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 1148 untranslated source text(s)
Updating 'monero_he.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 1148 untranslated source text(s)
[ 24%] Building CXX object monero/src/device/CMakeFiles/obj_device.dir/device.cpp.o
Updating 'monero_hi.qm'...
    Generated 158 translation(s) (119 finished and 39 unfinished)
    Ignored 990 untranslated source text(s)
[ 24%] Building ASM object monero/monero_crypto_src/amd64/CMakeFiles/monero-crypto-amd64-64-24k.dir/__/__/crypto_sign/ed25519/amd64-64-24k/ge25519_dbl_p1p1.s.o
Updating 'monero_hr.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 1148 untranslated source text(s)
[ 25%] Building C object monero/monero_crypto_src/amd64/CMakeFiles/monero-crypto-amd64-64-24k.dir/__/__/crypto_sign/ed25519/amd64-64-24k/ge25519_double.c.o
Updating 'monero_hu.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 1148 untranslated source text(s)
[ 25%] Building ASM object monero/monero_crypto_src/amd64/CMakeFiles/monero-crypto-amd64-64-24k.dir/__/__/crypto_sign/ed25519/amd64-64-24k/ge25519_nielsadd_p1p1.s.o
Updating 'monero_id.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 1148 untranslated source text(s)
Updating 'monero_is.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 1148 untranslated source text(s)
[ 25%] Building ASM object monero/monero_crypto_src/amd64/CMakeFiles/monero-crypto-amd64-64-24k.dir/__/__/crypto_sign/ed25519/amd64-64-24k/ge25519_nielsadd2.s.o
Updating 'monero_it.qm'...
[ 25%] Building C object monero/src/crypto/CMakeFiles/obj_cncrypto.dir/skein.c.o
    Generated 797 translation(s) (794 finished and 3 unfinished)
    Ignored 351 untranslated source text(s)
[ 26%] Building C object monero/src/crypto/CMakeFiles/obj_cncrypto.dir/slow-hash.c.o
Updating 'monero_ja.qm'...
    Generated 311 translation(s) (285 finished and 26 unfinished)
    Ignored 837 untranslated source text(s)
[ 26%] Building C object monero/external/randomx/CMakeFiles/randomx.dir/src/argon2_avx2.c.o
Updating 'monero_kmr.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 1148 untranslated source text(s)
[ 26%] Building C object monero/monero_crypto_src/amd64/CMakeFiles/monero-crypto-amd64-64-24k.dir/__/__/crypto_sign/ed25519/amd64-64-24k/ge25519_pack.c.o
Updating 'monero_ko.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 1148 untranslated source text(s)
[ 26%] Building ASM object monero/monero_crypto_src/amd64/CMakeFiles/monero-crypto-amd64-64-24k.dir/__/__/crypto_sign/ed25519/amd64-64-24k/ge25519_p1p1_to_p2.s.o
Updating 'monero_lt.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 1148 untranslated source text(s)
[ 27%] Building ASM object monero/monero_crypto_src/amd64/CMakeFiles/monero-crypto-amd64-64-24k.dir/__/__/crypto_sign/ed25519/amd64-64-24k/ge25519_p1p1_to_p3.s.o
Updating 'monero_nb_NO.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 1148 untranslated source text(s)
[ 27%] Building ASM object monero/monero_crypto_src/amd64/CMakeFiles/monero-crypto-amd64-64-24k.dir/__/__/crypto_sign/ed25519/amd64-64-24k/ge25519_pnielsadd_p1p1.s.o
Updating 'monero_ne.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 1148 untranslated source text(s)
[ 27%] Building C object monero/src/crypto/CMakeFiles/obj_cncrypto.dir/rx-slow-hash.c.o
Updating 'monero_nl.qm'...
    Generated 76 translation(s) (47 finished and 29 unfinished)
    Ignored 1072 untranslated source text(s)
[ 27%] Building C object monero/monero_crypto_src/amd64/CMakeFiles/monero-crypto-amd64-64-24k.dir/__/__/crypto_sign/ed25519/amd64-64-24k/ge25519_scalarmult_base.c.o
Updating 'monero_pl.qm'...
    Generated 13 translation(s) (6 finished and 7 unfinished)
    Ignored 1135 untranslated source text(s)
Updating 'monero_prt.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 1148 untranslated source text(s)
In file included from /build/monero-gui/src/monero-gui/monero/external/supercop/crypto_sign/ed25519/amd64-64-24k/ge25519_scalarmult_base.c:2:
/build/monero-gui/src/monero-gui/monero/external/supercop/crypto_sign/ed25519/amd64-64-24k/ge25519_scalarmult_base.c: In function ‘crypto_sign_ed25519_amd64_64_scalarmult_base’:
/build/monero-gui/src/monero-gui/monero/external/supercop/crypto_sign/ed25519/amd64-64-24k/sc25519.h:18:34: warning: ‘crypto_sign_ed25519_amd64_64_sc25519_window4’ accessing 85 bytes in a region of size 64 [-Wstringop-overflow=]
   18 | #define sc25519_window4          crypto_sign_ed25519_amd64_64_sc25519_window4
/build/monero-gui/src/monero-gui/monero/external/supercop/crypto_sign/ed25519/amd64-64-24k/sc25519.h:18:34: note: in definition of macro ‘sc25519_window4’
   18 | #define sc25519_window4          crypto_sign_ed25519_amd64_64_sc25519_window4
      |                                  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/build/monero-gui/src/monero-gui/monero/external/supercop/crypto_sign/ed25519/amd64-64-24k/sc25519.h:18:34: note: referencing argument 1 of type ‘signed char *’
   18 | #define sc25519_window4          crypto_sign_ed25519_amd64_64_sc25519_window4
/build/monero-gui/src/monero-gui/monero/external/supercop/crypto_sign/ed25519/amd64-64-24k/sc25519.h:18:34: note: in definition of macro ‘sc25519_window4’
   18 | #define sc25519_window4          crypto_sign_ed25519_amd64_64_sc25519_window4
      |                                  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/build/monero-gui/src/monero-gui/monero/external/supercop/crypto_sign/ed25519/amd64-64-24k/sc25519.h:18:34: note: in a call to function ‘crypto_sign_ed25519_amd64_64_sc25519_window4’
   18 | #define sc25519_window4          crypto_sign_ed25519_amd64_64_sc25519_window4
      |                                  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/build/monero-gui/src/monero-gui/monero/external/supercop/crypto_sign/ed25519/amd64-64-24k/sc25519.h:18:34: note: in definition of macro ‘sc25519_window4’
   18 | #define sc25519_window4          crypto_sign_ed25519_amd64_64_sc25519_window4
      |                                  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Updating 'monero_pt-br.qm'...
    Generated 4 translation(s) (2 finished and 2 unfinished)
    Ignored 1144 untranslated source text(s)
Updating 'monero_pt-pt.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 1148 untranslated source text(s)
[ 27%] Building C object monero/monero_crypto_src/amd64/CMakeFiles/monero-crypto-amd64-64-24k.dir/__/__/crypto_sign/ed25519/amd64-64-24k/ge25519_unpackneg.c.o
Updating 'monero_ro.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 1148 untranslated source text(s)
Updating 'monero_ru.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 1148 untranslated source text(s)
[ 27%] Building C object monero/monero_crypto_src/amd64/CMakeFiles/monero-crypto-amd64-64-24k.dir/__/__/crypto_sign/ed25519/amd64-64-24k/sc25519_from32bytes.c.o
Updating 'monero_sk.qm'...
    Generated 3 translation(s) (2 finished and 1 unfinished)
    Ignored 1145 untranslated source text(s)
Updating 'monero_sl.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 1148 untranslated source text(s)
[ 27%] Building C object monero/src/crypto/CMakeFiles/obj_cncrypto.dir/CryptonightR_JIT.c.o
Updating 'monero_sr.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 1148 untranslated source text(s)
Updating 'monero_sv.qm'...
    Generated 604 translation(s) (604 finished and 0 unfinished)
    Ignored 544 untranslated source text(s)
[ 29%] Building CXX object monero/external/randomx/CMakeFiles/randomx.dir/src/bytecode_machine.cpp.o
Updating 'monero_tr.qm'...
    Generated 2 translation(s) (1 finished and 1 unfinished)
    Ignored 1146 untranslated source text(s)
[ 29%] Building C object monero/monero_crypto_src/amd64/CMakeFiles/monero-crypto-amd64-64-24k.dir/__/__/crypto_sign/ed25519/amd64-64-24k/sc25519_window4.c.o
/build/monero-gui/src/monero-gui/monero/external/supercop/crypto_sign/ed25519/amd64-64-24k/sc25519_window4.c:3:34: warning: argument 1 of type ‘signed char[64]’ with mismatched bound [-Warray-parameter=]
    3 | void sc25519_window4(signed char r[64], const sc25519 *s)
      |                      ~~~~~~~~~~~~^~~~~
In file included from /build/monero-gui/src/monero-gui/monero/external/supercop/crypto_sign/ed25519/amd64-64-24k/sc25519_window4.c:1:
/build/monero-gui/src/monero-gui/monero/external/supercop/crypto_sign/ed25519/amd64-64-24k/sc25519.h:58:34: note: previously declared as ‘signed char[85]’
   58 | void sc25519_window4(signed char r[85], const sc25519 *s);
      |                      ~~~~~~~~~~~~^~~~~
Updating 'monero_uk.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 1148 untranslated source text(s)
Updating 'monero_ur.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 1148 untranslated source text(s)
Updating 'monero_zh-cn.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 1148 untranslated source text(s)
Updating 'monero_zh-tw.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 1148 untranslated source text(s)
[ 30%] Building ASM object monero/monero_crypto_src/amd64/CMakeFiles/monero-crypto-amd64-64-24k.dir/__/__/crypto_sign/ed25519/amd64-64-24k/fe25519_add.s.o
Updating 'monero_zu.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 1148 untranslated source text(s)
[ 30%] Building C object monero/src/crypto/CMakeFiles/obj_cncrypto.dir/tree-hash.c.o
Updating 'monero_zu.qm.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 1148 untranslated source text(s)
[ 30%] Building ASM object monero/monero_crypto_src/amd64/CMakeFiles/monero-crypto-amd64-64-24k.dir/__/__/crypto_sign/ed25519/amd64-64-24k/fe25519_sub.s.o
Generating embedded translations header
[ 30%] Building CXX object monero/src/device/CMakeFiles/obj_device.dir/device_default.cpp.o
[ 30%] Building C object monero/src/crypto/CMakeFiles/obj_cncrypto.dir/CryptonightR_template.S.o
[ 30%] Built target monero-crypto-amd64-64-24k
[ 30%] Generating generated_testnet_blocks.c
[ 30%] Building CXX object monero/src/cryptonote_basic/CMakeFiles/obj_cryptonote_format_utils_basic.dir/cryptonote_format_utils_basic.cpp.o
[ 30%] Building CXX object monero/external/randomx/CMakeFiles/randomx.dir/src/cpu.cpp.o
[ 30%] Generating generated_checkpoints.c
[100%] Built target generate_translations_header
[ 30%] Building CXX object monero/external/randomx/CMakeFiles/randomx.dir/src/dataset.cpp.o
[ 30%] Performing install step for 'generate_translations_header'

[ 30%] Completed 'generate_translations_header'
[ 30%] Generating generated_stagenet_blocks.c
[ 30%] Building CXX object monero/external/randomx/CMakeFiles/randomx.dir/src/soft_aes.cpp.o
[ 30%] Built target generate_translations_header
[ 30%] Building CXX object monero/src/checkpoints/CMakeFiles/obj_checkpoints.dir/checkpoints.cpp.o
[ 31%] Building CXX object monero/src/blocks/CMakeFiles/blocks.dir/blocks.cpp.o
[ 31%] Building C object monero/src/blocks/CMakeFiles/blocks.dir/generated_checkpoints.c.o
[ 31%] Linking CXX static library libqrcodegen.a
[ 31%] Built target qrcodegen
[ 31%] Building CXX object monero/src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/account.cpp.o
[ 31%] Building C object monero/external/db_drivers/liblmdb/CMakeFiles/lmdb.dir/midl.c.o
[ 31%] Building CXX object monero/external/randomx/CMakeFiles/randomx.dir/src/virtual_memory.cpp.o
[ 32%] Building CXX object monero/external/randomx/CMakeFiles/randomx.dir/src/vm_interpreted.cpp.o
[ 32%] Linking C static library liblmdb.a
[ 32%] Building CXX object monero/external/randomx/CMakeFiles/randomx.dir/src/allocator.cpp.o
[ 32%] Built target lmdb
[ 32%] Building CXX object monero/src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/blockchain.cpp.o
[ 32%] Building C object monero/src/blocks/CMakeFiles/blocks.dir/generated_testnet_blocks.c.o
[ 32%] Building CXX object monero/external/randomx/CMakeFiles/randomx.dir/src/assembly_generator_x86.cpp.o
[ 32%] Building C object monero/src/blocks/CMakeFiles/blocks.dir/generated_stagenet_blocks.c.o
[ 32%] Linking CXX static library libblocks.a
[ 32%] Building CXX object monero/external/randomx/CMakeFiles/randomx.dir/src/instruction.cpp.o
[ 32%] Built target blocks
[ 32%] Building CXX object monero/external/randomx/CMakeFiles/randomx.dir/src/randomx.cpp.o
[ 32%] Building CXX object monero/src/multisig/CMakeFiles/obj_multisig.dir/multisig.cpp.o
[ 32%] Built target obj_cncrypto
[ 33%] Building CXX object monero/external/randomx/CMakeFiles/randomx.dir/src/superscalar.cpp.o
[ 33%] Building CXX object monero/src/hardforks/CMakeFiles/obj_hardforks.dir/hardforks.cpp.o
[ 33%] Built target obj_hardforks
[ 33%] Building CXX object monero/src/blockchain_db/CMakeFiles/obj_blockchain_db.dir/blockchain_db.cpp.o
[ 33%] Building CXX object monero/external/randomx/CMakeFiles/randomx.dir/src/vm_compiled.cpp.o
[ 33%] Building CXX object monero/external/randomx/CMakeFiles/randomx.dir/src/vm_interpreted_light.cpp.o
[ 33%] Building C object monero/external/randomx/CMakeFiles/randomx.dir/src/argon2_core.c.o
[ 33%] Building CXX object monero/external/randomx/CMakeFiles/randomx.dir/src/blake2_generator.cpp.o
[ 33%] Building CXX object monero/external/randomx/CMakeFiles/randomx.dir/src/instructions_portable.cpp.o
[ 34%] Building C object monero/external/randomx/CMakeFiles/randomx.dir/src/reciprocal.c.o
[ 34%] Building CXX object monero/external/randomx/CMakeFiles/randomx.dir/src/virtual_machine.cpp.o
[ 34%] Building CXX object monero/external/randomx/CMakeFiles/randomx.dir/src/vm_compiled_light.cpp.o
[ 34%] Building C object monero/external/randomx/CMakeFiles/randomx.dir/src/blake2/blake2b.c.o
[ 34%] Building CXX object monero/external/randomx/CMakeFiles/randomx.dir/src/jit_compiler_x86.cpp.o
[ 35%] Building C object monero/external/randomx/CMakeFiles/randomx.dir/src/jit_compiler_x86_static.S.o
[ 35%] Building CXX object monero/src/blockchain_db/CMakeFiles/obj_blockchain_db.dir/lmdb/db_lmdb.cpp.o
[ 35%] Building CXX object monero/src/lmdb/CMakeFiles/obj_lmdb_lib.dir/database.cpp.o
[ 35%] Building CXX object monero/src/net/CMakeFiles/obj_net.dir/dandelionpp.cpp.o
[ 35%] Building CXX object monero/src/mnemonics/CMakeFiles/obj_mnemonics.dir/electrum-words.cpp.o
[ 35%] Linking CXX static library librandomx.a
[ 35%] Built target randomx
[ 35%] Building CXX object monero/src/rpc/CMakeFiles/obj_rpc_base.dir/rpc_args.cpp.o
[ 36%] Building CXX object monero/src/lmdb/CMakeFiles/obj_lmdb_lib.dir/error.cpp.o
[ 36%] Building CXX object monero/src/lmdb/CMakeFiles/obj_lmdb_lib.dir/table.cpp.o
[ 36%] Building CXX object monero/src/lmdb/CMakeFiles/obj_lmdb_lib.dir/value_stream.cpp.o
[ 37%] Building CXX object monero/src/device/CMakeFiles/obj_device.dir/log.cpp.o
[ 37%] Built target obj_lmdb_lib
[ 38%] Building CXX object monero/src/rpc/CMakeFiles/obj_rpc.dir/bootstrap_daemon.cpp.o
[ 39%] Building CXX object monero/src/net/CMakeFiles/obj_net.dir/error.cpp.o
[ 39%] Linking CXX static library libeasylogging.a
[ 39%] Building CXX object monero/src/net/CMakeFiles/obj_net.dir/http.cpp.o
[ 39%] Built target easylogging
[ 39%] Building CXX object monero/src/p2p/CMakeFiles/obj_p2p.dir/net_node.cpp.o
/build/monero-gui/src/monero-gui/monero/src/blockchain_db/blockchain_db.cpp: In member function ‘virtual uint64_t cryptonote::BlockchainDB::add_block(const std::pair<cryptonote::block, std::__cxx11::basic_string<char> >&, size_t, uint64_t, const difficulty_type&, const uint64_t&, const std::vector<std::pair<cryptonote::transaction, std::__cxx11::basic_string<char> > >&)’:
/build/monero-gui/src/monero-gui/monero/src/blockchain_db/blockchain_db.cpp:290:52: warning: loop variable ‘tx’ of type ‘const std::pair<cryptonote::transaction, boost::basic_string_ref<char, std::char_traits<char> > >&’ binds to a temporary constructed from type ‘const std::pair<cryptonote::transaction, std::__cxx11::basic_string<char> >’ [-Wrange-loop-construct]
  290 |   for (const std::pair<transaction, blobdata_ref>& tx : txs)
      |                                                    ^~
/build/monero-gui/src/monero-gui/monero/src/blockchain_db/blockchain_db.cpp:290:52: note: use non-reference type ‘const std::pair<cryptonote::transaction, boost::basic_string_ref<char, std::char_traits<char> > >’ to make the copy explicit or ‘const std::pair<cryptonote::transaction, std::__cxx11::basic_string<char> >&’ to prevent copying
[ 39%] Building CXX object monero/src/ringct/CMakeFiles/obj_ringct_basic.dir/rctTypes.cpp.o
[ 39%] Built target obj_cryptonote_format_utils_basic
[ 40%] Building CXX object monero/src/cryptonote_protocol/CMakeFiles/obj_cryptonote_protocol.dir/block_queue.cpp.o
[ 40%] Building CXX object monero/src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/connection_context.cpp.o
[ 40%] Building CXX object monero/src/device/CMakeFiles/obj_device.dir/device_ledger.cpp.o
[ 40%] Built target obj_multisig
[ 40%] Building CXX object monero/src/rpc/CMakeFiles/obj_rpc_pub.dir/zmq_pub.cpp.o
[ 40%] Building C object monero/src/ringct/CMakeFiles/obj_ringct_basic.dir/rctCryptoOps.c.o
[ 40%] Building CXX object monero/src/ringct/CMakeFiles/obj_ringct_basic.dir/multiexp.cc.o
[ 40%] Built target obj_mnemonics
[ 40%] Building CXX object monero/src/serialization/CMakeFiles/obj_serialization.dir/json_object.cpp.o
[ 40%] Building CXX object monero/src/device/CMakeFiles/obj_device.dir/device_io_hid.cpp.o
/build/monero-gui/src/monero-gui/monero/src/cryptonote_core/blockchain.cpp: In member function ‘std::pair<bool, long unsigned int> cryptonote::Blockchain::check_difficulty_checkpoints() const’:
/build/monero-gui/src/monero-gui/monero/src/cryptonote_core/blockchain.cpp:976:52: warning: loop variable ‘i’ of type ‘const std::pair<long unsigned int, boost::multiprecision::number<boost::multiprecision::backends::cpp_int_backend<128, 128, boost::multiprecision::unsigned_magnitude, boost::multiprecision::unchecked, void> > >&’ binds to a temporary constructed from type ‘const std::pair<const long unsigned int, boost::multiprecision::number<boost::multiprecision::backends::cpp_int_backend<128, 128, boost::multiprecision::unsigned_magnitude, boost::multiprecision::unchecked, void> > >’ [-Wrange-loop-construct]
  976 |   for (const std::pair<uint64_t, difficulty_type>& i : m_checkpoints.get_difficulty_points())
      |                                                    ^
/build/monero-gui/src/monero-gui/monero/src/cryptonote_core/blockchain.cpp:976:52: note: use non-reference type ‘const std::pair<long unsigned int, boost::multiprecision::number<boost::multiprecision::backends::cpp_int_backend<128, 128, boost::multiprecision::unsigned_magnitude, boost::multiprecision::unchecked, void> > >’ to make the copy explicit or ‘const std::pair<const long unsigned int, boost::multiprecision::number<boost::multiprecision::backends::cpp_int_backend<128, 128, boost::multiprecision::unsigned_magnitude, boost::multiprecision::unchecked, void> > >&’ to prevent copying
[ 40%] Building CXX object monero/src/rpc/CMakeFiles/obj_rpc_base.dir/rpc_payment_signature.cpp.o
[ 40%] Building CXX object monero/src/rpc/CMakeFiles/obj_rpc_base.dir/rpc_handler.cpp.o
[ 40%] Built target obj_ringct
[ 40%] Building CXX object monero/src/rpc/CMakeFiles/obj_daemon_messages.dir/message.cpp.o
[ 40%] Building CXX object monero/src/rpc/CMakeFiles/obj_daemon_messages.dir/daemon_messages.cpp.o
[ 40%] Building CXX object monero/src/ringct/CMakeFiles/obj_ringct_basic.dir/bulletproofs.cc.o
[ 40%] Building CXX object monero/src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/cryptonote_basic_impl.cpp.o
[ 40%] Building CXX object monero/src/cryptonote_protocol/CMakeFiles/obj_cryptonote_protocol.dir/cryptonote_protocol_handler-base.cpp.o
[ 40%] Building CXX object monero/src/cryptonote_protocol/CMakeFiles/obj_cryptonote_protocol.dir/levin_notify.cpp.o
[ 40%] Built target obj_device
[ 40%] Building CXX object monero/src/rpc/CMakeFiles/obj_daemon_rpc_server.dir/daemon_handler.cpp.o
[ 40%] Built target obj_rpc_pub
[ 40%] Building CXX object monero/src/wallet/CMakeFiles/obj_wallet.dir/wallet2.cpp.o
[ 40%] Building CXX object monero/src/device_trezor/CMakeFiles/obj_device_trezor.dir/trezor/messages_map.cpp.o
[ 40%] Built target obj_ringct_basic
[ 40%] Building CXX object monero/src/daemonizer/CMakeFiles/obj_daemonizer.dir/posix_fork.cpp.o
[ 40%] Built target obj_daemonizer
[ 40%] Building CXX object monero/src/wallet/api/CMakeFiles/obj_wallet_api.dir/wallet.cpp.o
In file included from /build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/messages_map.cpp:32:
/build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/messages/messages-common.pb.h:751:5: warning: ‘hw::trezor::messages::common::ButtonRequest_ButtonRequestType__Deprecated_ButtonRequest_PassphraseType’ is deprecated [-Wdeprecated-declarations]
  751 |     ButtonRequest_ButtonRequestType__Deprecated_ButtonRequest_PassphraseType;
      |     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/messages/messages-common.pb.h:169:3: note: declared here
  169 |   ButtonRequest_ButtonRequestType__Deprecated_ButtonRequest_PassphraseType PROTOBUF_DEPRECATED_ENUM = 14,
      |   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/messages_map.cpp: In static member function ‘static google::protobuf::Message* hw::trezor::MessageMapper::get_message(const string&)’:
/build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/messages_map.cpp:83:23: warning: loop variable ‘text’ of type ‘const string&’ {aka ‘const std::__cxx11::basic_string<char>&’} binds to a temporary constructed from type ‘const char*’ [-Wrange-loop-construct]
   83 |     for(const string &text : PACKAGES){
      |                       ^~~~
/build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/messages_map.cpp:83:23: note: use non-reference type ‘const string’ {aka ‘const std::__cxx11::basic_string<char>’} to make the copy explicit or ‘const char* const&’ to prevent copying
[ 40%] Building CXX object monero/src/device_trezor/CMakeFiles/obj_device_trezor.dir/trezor/protocol.cpp.o
[ 41%] Building CXX object monero/src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/cryptonote_format_utils.cpp.o
[ 41%] Building CXX object monero/src/net/CMakeFiles/obj_net.dir/i2p_address.cpp.o
[ 41%] Built target obj_serialization
[ 41%] Building C object external/CMakeFiles/quirc.dir/quirc/lib/decode.c.o
[ 41%] Building C object external/CMakeFiles/quirc.dir/quirc/lib/identify.c.o
[ 41%] Built target obj_daemon_messages
[ 41%] Automatic MOC and UIC for target translations
[ 41%] Built target translations_autogen
[ 43%] Automatic MOC and UIC for target zxcvbn
[ 43%] Built target zxcvbn_autogen
[ 44%] Automatic MOC and UIC for target openpgp
[ 44%] Built target openpgp_autogen
[ 44%] Automatic MOC and UIC for target obj_gui_version
[ 44%] Built target obj_gui_version_autogen
[ 44%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/upnpc-static.dir/upnpc.c.o
[ 44%] Built target obj_checkpoints
[ 44%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/upnpc-shared.dir/upnpc.c.o
[ 44%] Linking C executable upnpc-static
[ 44%] Building CXX object monero/src/p2p/CMakeFiles/obj_p2p.dir/net_peerlist.cpp.o
[ 44%] Built target upnpc-static
[ 44%] Building C object monero/external/miniupnp/miniupnpc/CMakeFiles/listdevices.dir/listdevices.c.o
/build/monero-gui/src/monero-gui/monero/external/miniupnp/miniupnpc/listdevices.c: In function ‘add_device’:
/build/monero-gui/src/monero-gui/monero/external/miniupnp/miniupnpc/listdevices.c:60:24: warning: implicit declaration of function ‘strdup’; did you mean ‘strcmp’? [-Wimplicit-function-declaration]
   60 |         elt->descURL = strdup(dev->descURL);
      |                        ^~~~~~
      |                        strcmp
/build/monero-gui/src/monero-gui/monero/external/miniupnp/miniupnpc/listdevices.c:60:22: warning: assignment to ‘char *’ from ‘int’ makes pointer from integer without a cast [-Wint-conversion]
   60 |         elt->descURL = strdup(dev->descURL);
      |                      ^
[ 44%] Linking C executable listdevices
[ 44%] Built target listdevices
[ 44%] Built target obj_rpc_base
[ 44%] Building CXX object monero/contrib/epee/src/CMakeFiles/epee.dir/byte_slice.cpp.o
[ 44%] Building CXX object monero/contrib/epee/src/CMakeFiles/epee_readline.dir/readline_buffer.cpp.o
[ 44%] Linking C executable upnpc-shared
[ 44%] Built target upnpc-shared
[ 45%] Building CXX object monero/src/CMakeFiles/obj_version.dir/__/__/version.cpp.o
[ 45%] Built target obj_version
[ 46%] Building CXX object monero/src/common/CMakeFiles/obj_common.dir/base58.cpp.o
[ 46%] Built target obj_blockchain_db
[ 46%] Generating translations.qrc
[ 46%] Generating monero-core.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core.qm'...
    Generated 4 translation(s) (4 finished and 0 unfinished)
    Ignored 763 untranslated source text(s)
[ 46%] Generating monero-core_af.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_af.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_af.qm'...
    Generated 26 translation(s) (26 finished and 0 unfinished)
    Ignored 693 untranslated source text(s)
[ 47%] Generating monero-core_ar.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_ar.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_ar.qm'...
    Generated 336 translation(s) (336 finished and 0 unfinished)
    Ignored 411 untranslated source text(s)
[ 47%] Generating monero-core_az.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_az.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_az.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 767 untranslated source text(s)
[ 47%] Generating monero-core_bg.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_bg.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_bg.qm'...
    Generated 451 translation(s) (451 finished and 0 unfinished)
    Ignored 290 untranslated source text(s)
[ 47%] Generating monero-core_bn.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_bn.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_bn.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 767 untranslated source text(s)
[ 47%] Generating monero-core_cat.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_cat.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_cat.qm'...
    Generated 525 translation(s) (525 finished and 0 unfinished)
    Ignored 194 untranslated source text(s)
[ 48%] Generating monero-core_cs.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_cs.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_cs.qm'...
    Generated 413 translation(s) (413 finished and 0 unfinished)
    Ignored 315 untranslated source text(s)
[ 48%] Generating monero-core_da.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_da.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_da.qm'...
    Generated 399 translation(s) (399 finished and 0 unfinished)
    Ignored 297 untranslated source text(s)
[ 48%] Generating monero-core_de.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_de.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_de.qm'...
    Generated 660 translation(s) (660 finished and 0 unfinished)
    Ignored 51 untranslated source text(s)
[ 48%] Generating monero-core_el.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_el.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_el.qm'...
    Generated 685 translation(s) (685 finished and 0 unfinished)
    Ignored 52 untranslated source text(s)
[ 48%] Generating monero-core_eo.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_eo.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_eo.qm'...
    Generated 469 translation(s) (469 finished and 0 unfinished)
    Ignored 267 untranslated source text(s)
[ 49%] Generating monero-core_es.qm
[ 50%] Building CXX object monero/contrib/epee/src/CMakeFiles/epee.dir/byte_stream.cpp.o
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_es.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_es.qm'...
    Generated 673 translation(s) (673 finished and 0 unfinished)
    Ignored 54 untranslated source text(s)
[ 50%] Generating monero-core_fa.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_fa.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_fa.qm'...
    Generated 88 translation(s) (88 finished and 0 unfinished)
    Ignored 659 untranslated source text(s)
[ 50%] Generating monero-core_fi.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_fi.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_fi.qm'...
    Generated 516 translation(s) (516 finished and 0 unfinished)
    Ignored 206 untranslated source text(s)
[ 50%] Generating monero-core_fr.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_fr.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_fr.qm'...
    Generated 647 translation(s) (647 finished and 0 unfinished)
    Ignored 54 untranslated source text(s)
[ 50%] Generating monero-core_ga.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_ga.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_ga.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 767 untranslated source text(s)
[ 50%] Generating monero-core_he.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_he.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_he.qm'...
    Generated 281 translation(s) (281 finished and 0 unfinished)
    Ignored 446 untranslated source text(s)
[ 51%] Generating monero-core_hi.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_hi.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_hi.qm'...
    Generated 440 translation(s) (440 finished and 0 unfinished)
    Ignored 297 untranslated source text(s)
[ 51%] Generating monero-core_hr.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_hr.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_hr.qm'...
    Generated 310 translation(s) (310 finished and 0 unfinished)
    Ignored 412 untranslated source text(s)
[ 51%] Generating monero-core_hu.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_hu.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_hu.qm'...
    Generated 506 translation(s) (506 finished and 0 unfinished)
    Ignored 188 untranslated source text(s)
[ 51%] Generating monero-core_id.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_id.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_id.qm'...
    Generated 305 translation(s) (305 finished and 0 unfinished)
    Ignored 428 untranslated source text(s)
[ 51%] Generating monero-core_is.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_is.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_is.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 767 untranslated source text(s)
[ 52%] Generating monero-core_it.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_it.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_it.qm'...
    Generated 599 translation(s) (599 finished and 0 unfinished)
    Ignored 109 untranslated source text(s)
[ 52%] Generating monero-core_ja.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_ja.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_ja.qm'...
    Generated 571 translation(s) (571 finished and 0 unfinished)
    Ignored 129 untranslated source text(s)
[ 52%] Generating monero-core_kmr.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_kmr.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_kmr.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 767 untranslated source text(s)
[ 52%] Generating monero-core_ko.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_ko.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_ko.qm'...
    Generated 185 translation(s) (185 finished and 0 unfinished)
    Ignored 553 untranslated source text(s)
[ 52%] Generating monero-core_lt.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_lt.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_lt.qm'...
    Generated 373 translation(s) (373 finished and 0 unfinished)
    Ignored 356 untranslated source text(s)
[ 52%] Generating monero-core_nb.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_nb.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_nb.qm'...
    Generated 538 translation(s) (538 finished and 0 unfinished)
    Ignored 175 untranslated source text(s)
[ 53%] Generating monero-core_ne.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_ne.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_ne.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 767 untranslated source text(s)
[ 53%] Generating monero-core_nl.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_nl.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_nl.qm'...
    Generated 550 translation(s) (550 finished and 0 unfinished)
    Ignored 92 untranslated source text(s)
[ 53%] Generating monero-core_pl.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_pl.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_pl.qm'...
    Generated 674 translation(s) (674 finished and 0 unfinished)
    Ignored 52 untranslated source text(s)
[ 53%] Generating monero-core_pt-br.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_pt-br.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_pt-br.qm'...
    Generated 744 translation(s) (744 finished and 0 unfinished)
[ 53%] Generating monero-core_pt-pt.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_pt-pt.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_pt-pt.qm'...
    Generated 542 translation(s) (542 finished and 0 unfinished)
    Ignored 173 untranslated source text(s)
[ 54%] Generating monero-core_ro.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_ro.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_ro.qm'...
    Generated 588 translation(s) (588 finished and 0 unfinished)
    Ignored 103 untranslated source text(s)
[ 54%] Generating monero-core_ru.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_ru.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_ru.qm'...
    Generated 759 translation(s) (759 finished and 0 unfinished)
[ 54%] Generating monero-core_sk.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_sk.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_sk.qm'...
    Generated 445 translation(s) (445 finished and 0 unfinished)
    Ignored 280 untranslated source text(s)
[ 54%] Generating monero-core_sl.qm
[ 54%] Building C object external/CMakeFiles/quirc.dir/quirc/lib/quirc.c.o
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_sl.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_sl.qm'...
    Generated 490 translation(s) (490 finished and 0 unfinished)
    Ignored 230 untranslated source text(s)
[ 54%] Generating monero-core_sr.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_sr.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_sr.qm'...
    Generated 499 translation(s) (499 finished and 0 unfinished)
    Ignored 222 untranslated source text(s)
[ 55%] Generating monero-core_sv.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_sv.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_sv.qm'...
    Generated 476 translation(s) (476 finished and 0 unfinished)
    Ignored 235 untranslated source text(s)
[ 55%] Generating monero-core_ta.qm
[ 56%] Building C object external/CMakeFiles/quirc.dir/quirc/lib/version_db.c.o
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_ta.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_ta.qm'...
    Generated 685 translation(s) (685 finished and 0 unfinished)
    Ignored 53 untranslated source text(s)
[ 56%] Generating monero-core_tr.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_tr.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_tr.qm'...
    Generated 504 translation(s) (504 finished and 0 unfinished)
    Ignored 223 untranslated source text(s)
[ 56%] Generating monero-core_uk.qm
[ 56%] Linking C static library libquirc.a
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_uk.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_uk.qm'...
    Generated 547 translation(s) (547 finished and 0 unfinished)
    Ignored 184 untranslated source text(s)
[ 56%] Generating monero-core_ur.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_ur.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_ur.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 767 untranslated source text(s)
[ 56%] Generating monero-core_vi.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_vi.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_vi.qm'...
    Generated 173 translation(s) (173 finished and 0 unfinished)
    Ignored 525 untranslated source text(s)
[ 58%] Generating monero-core_zh-cn.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_zh-cn.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_zh-cn.qm'...
    Generated 588 translation(s) (588 finished and 0 unfinished)
    Ignored 140 untranslated source text(s)
[ 58%] Generating monero-core_zh-tw.qm
[ 58%] Building CXX object monero/contrib/epee/src/CMakeFiles/epee.dir/hex.cpp.o
[ 58%] Building CXX object monero/src/common/CMakeFiles/obj_common.dir/command_line.cpp.o
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_zh-tw.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_zh-tw.qm'...
[ 58%] Built target quirc
    Generated 680 translation(s) (680 finished and 0 unfinished)
    Ignored 54 untranslated source text(s)
[ 58%] Generating monero-core_zu.qm
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_zu.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_zu.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 767 untranslated source text(s)
[ 58%] Generating qrc_translations.cpp
[ 58%] Building CXX object src/zxcvbn-c/CMakeFiles/zxcvbn.dir/zxcvbn_autogen/mocs_compilation.cpp.o
[ 58%] Building C object src/zxcvbn-c/CMakeFiles/zxcvbn.dir/zxcvbn.c.o
[ 58%] Building CXX object translations/CMakeFiles/translations.dir/translations_autogen/mocs_compilation.cpp.o
[ 58%] Building CXX object translations/CMakeFiles/translations.dir/qrc_translations.cpp.o
In file included from /build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/transport.hpp:52,
                 from /build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor.hpp:36,
                 from /build/monero-gui/src/monero-gui/monero/src/device_trezor/device_trezor.hpp:33,
                 from /build/monero-gui/src/monero-gui/monero/src/wallet/wallet2.cpp:85:
/build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/messages/messages-common.pb.h:751:5: warning: ‘hw::trezor::messages::common::ButtonRequest_ButtonRequestType__Deprecated_ButtonRequest_PassphraseType’ is deprecated [-Wdeprecated-declarations]
  751 |     ButtonRequest_ButtonRequestType__Deprecated_ButtonRequest_PassphraseType;
      |     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/messages/messages-common.pb.h:169:3: note: declared here
  169 |   ButtonRequest_ButtonRequestType__Deprecated_ButtonRequest_PassphraseType PROTOBUF_DEPRECATED_ENUM = 14,
      |   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[ 58%] Linking CXX static library libepee_readline.a
[ 58%] Built target epee_readline
[ 58%] Automatic MOC and UIC for target qrdecoder
[ 58%] Built target qrdecoder_autogen
[ 58%] Building CXX object monero/contrib/epee/src/CMakeFiles/epee.dir/abstract_http_client.cpp.o
[ 58%] Building CXX object src/openpgp/CMakeFiles/openpgp.dir/openpgp_autogen/mocs_compilation.cpp.o
[ 58%] Building CXX object src/openpgp/CMakeFiles/openpgp.dir/openpgp.cpp.o
[ 58%] Linking CXX static library libzxcvbn.a
[ 58%] Built target zxcvbn
[ 58%] Building CXX object CMakeFiles/obj_gui_version.dir/obj_gui_version_autogen/mocs_compilation.cpp.o
[ 58%] Built target obj_gui_version
[ 59%] Linking CXX static library libversion.a
/build/monero-gui/src/monero-gui/monero/src/wallet/wallet2.cpp: In member function ‘void tools::wallet2::refresh(bool, uint64_t, uint64_t&, bool&, bool)’:
/build/monero-gui/src/monero-gui/monero/src/wallet/wallet2.cpp:3375:8: warning: variable ‘refreshed’ set but not used [-Wunused-but-set-variable]
 3375 |   bool refreshed = false;
      |        ^~~~~~~~~
[ 59%] Built target version
[ 59%] Building CXX object src/QR-Code-scanner/CMakeFiles/qrdecoder.dir/qrdecoder_autogen/mocs_compilation.cpp.o
[ 59%] Building CXX object monero/src/common/CMakeFiles/obj_common.dir/dns_utils.cpp.o
[ 59%] Building CXX object src/QR-Code-scanner/CMakeFiles/qrdecoder.dir/Decoder.cpp.o
[ 60%] Linking CXX static library libtranslations.a
[ 60%] Built target translations
[ 61%] Building CXX object CMakeFiles/gui_version.dir/gui_version_autogen/mocs_compilation.cpp.o
[ 61%] Linking CXX static library libgui_version.a
[ 61%] Built target gui_version
[ 61%] Linking CXX static library libhardforks.a
[ 61%] Built target hardforks
[ 61%] Building CXX object monero/src/common/CMakeFiles/obj_common.dir/download.cpp.o
[ 61%] Linking CXX static library libopenpgp.a
[ 61%] Built target openpgp
[ 61%] Building CXX object monero/src/common/CMakeFiles/obj_common.dir/error.cpp.o
[ 62%] Building CXX object monero/src/common/CMakeFiles/obj_common.dir/expect.cpp.o
[ 63%] Linking CXX static library libqrdecoder.a
[ 63%] Built target qrdecoder
[ 63%] Building CXX object monero/src/common/CMakeFiles/obj_common.dir/util.cpp.o
[ 63%] Building CXX object monero/src/common/CMakeFiles/obj_common.dir/i18n.cpp.o
[ 63%] Building CXX object monero/src/common/CMakeFiles/obj_common.dir/notify.cpp.o
In file included from /build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/transport.hpp:52,
                 from /build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/protocol.hpp:36,
                 from /build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/protocol.cpp:31:
/build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/messages/messages-common.pb.h:751:5: warning: ‘hw::trezor::messages::common::ButtonRequest_ButtonRequestType__Deprecated_ButtonRequest_PassphraseType’ is deprecated [-Wdeprecated-declarations]
  751 |     ButtonRequest_ButtonRequestType__Deprecated_ButtonRequest_PassphraseType;
      |     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/messages/messages-common.pb.h:169:3: note: declared here
  169 |   ButtonRequest_ButtonRequestType__Deprecated_ButtonRequest_PassphraseType PROTOBUF_DEPRECATED_ENUM = 14,
      |   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[ 63%] Building CXX object monero/src/common/CMakeFiles/obj_common.dir/password.cpp.o
[ 63%] Building CXX object monero/src/common/CMakeFiles/obj_common.dir/perf_timer.cpp.o
[ 64%] Building CXX object monero/src/common/CMakeFiles/obj_common.dir/pruning.cpp.o
[ 65%] Building CXX object monero/src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/cryptonote_core.cpp.o
[ 65%] Building CXX object monero/src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/difficulty.cpp.o
[ 65%] Building CXX object monero/src/common/CMakeFiles/obj_common.dir/spawn.cpp.o
[ 65%] Building CXX object monero/src/common/CMakeFiles/obj_common.dir/threadpool.cpp.o
[ 65%] Built target obj_p2p
[ 65%] Building CXX object monero/src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/tx_pool.cpp.o
[ 65%] Building CXX object monero/src/common/CMakeFiles/obj_common.dir/updates.cpp.o
[ 65%] Building C object monero/src/common/CMakeFiles/obj_common.dir/aligned.c.o
[ 66%] Building CXX object monero/src/common/CMakeFiles/obj_common.dir/timings.cc.o
[ 66%] Built target obj_cryptonote_protocol
[ 66%] Building CXX object monero/src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/tx_sanity_check.cpp.o
[ 67%] Building CXX object monero/src/rpc/CMakeFiles/obj_daemon_rpc_server.dir/zmq_pub.cpp.o
[ 67%] Building CXX object monero/src/common/CMakeFiles/obj_common.dir/combinator.cpp.o
[ 67%] Building CXX object monero/src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/hardfork.cpp.o
[ 67%] Building CXX object monero/src/common/CMakeFiles/obj_common.dir/stack_trace.cpp.o
[ 67%] Building CXX object monero/contrib/epee/src/CMakeFiles/epee.dir/http_auth.cpp.o
[ 67%] Building CXX object monero/src/rpc/CMakeFiles/obj_rpc.dir/bootstrap_node_selector.cpp.o
[ 67%] Building CXX object monero/src/net/CMakeFiles/obj_net.dir/parse.cpp.o
[ 67%] Building CXX object monero/contrib/epee/src/CMakeFiles/epee.dir/mlog.cpp.o
[ 67%] Building CXX object monero/contrib/epee/src/CMakeFiles/epee.dir/net_helper.cpp.o
[ 67%] Building CXX object monero/src/net/CMakeFiles/obj_net.dir/socks.cpp.o
/build/monero-gui/src/monero-gui/monero/src/cryptonote_core/cryptonote_core.cpp: In member function ‘void cryptonote::core::init(const boost::program_options::variables_map&, const cryptonote::test_options*, const GetCheckpointsCallback&, bool)::hash_notify::operator()(uint64_t, epee::span<const cryptonote::block>) const’:
/build/monero-gui/src/monero-gui/monero/src/cryptonote_core/cryptonote_core.cpp:635:30: warning: loop variable ‘bl’ creates a copy from type ‘const cryptonote::block’ [-Wrange-loop-construct]
  635 |             for (const block bl : blocks)
      |                              ^~
/build/monero-gui/src/monero-gui/monero/src/cryptonote_core/cryptonote_core.cpp:635:30: note: use reference type to prevent copying
  635 |             for (const block bl : blocks)
      |                              ^~
      |                              &
[ 68%] Building CXX object monero/src/net/CMakeFiles/obj_net.dir/socks_connect.cpp.o
[ 69%] Building CXX object monero/contrib/epee/src/CMakeFiles/epee.dir/net_utils_base.cpp.o
[ 69%] Building CXX object monero/src/net/CMakeFiles/obj_net.dir/tor_address.cpp.o
[ 69%] Building CXX object monero/src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/miner.cpp.o
[ 69%] Building CXX object monero/src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/cryptonote_tx_utils.cpp.o
[ 69%] Building CXX object monero/src/wallet/api/CMakeFiles/obj_wallet_api.dir/wallet_manager.cpp.o
[ 69%] Building CXX object monero/src/rpc/CMakeFiles/obj_daemon_rpc_server.dir/zmq_server.cpp.o
[ 69%] Building CXX object monero/src/rpc/CMakeFiles/obj_rpc.dir/core_rpc_server.cpp.o
[ 69%] Building CXX object monero/contrib/epee/src/CMakeFiles/epee.dir/string_tools.cpp.o
[ 69%] Building CXX object monero/src/device_trezor/CMakeFiles/obj_device_trezor.dir/trezor/transport.cpp.o
[ 69%] Building CXX object monero/src/rpc/CMakeFiles/obj_rpc.dir/rpc_payment.cpp.o
[ 69%] Building CXX object monero/contrib/epee/src/CMakeFiles/epee.dir/wipeable_string.cpp.o
[ 69%] Built target obj_common
[ 69%] Building CXX object monero/contrib/epee/src/CMakeFiles/epee.dir/levin_base.cpp.o
[ 69%] Building C object monero/contrib/epee/src/CMakeFiles/epee.dir/memwipe.c.o
[ 70%] Building CXX object monero/contrib/epee/src/CMakeFiles/epee.dir/connection_basic.cpp.o
[ 70%] Building CXX object monero/contrib/epee/src/CMakeFiles/epee.dir/network_throttle.cpp.o
[ 70%] Building CXX object monero/contrib/epee/src/CMakeFiles/epee.dir/network_throttle-detail.cpp.o
[ 70%] Building CXX object monero/src/net/CMakeFiles/obj_net.dir/zmq.cpp.o
[ 70%] Building CXX object monero/contrib/epee/src/CMakeFiles/epee.dir/mlocker.cpp.o
[ 70%] Building CXX object monero/src/rpc/CMakeFiles/obj_rpc.dir/rpc_version_str.cpp.o
[ 72%] Building CXX object monero/src/rpc/CMakeFiles/obj_rpc.dir/instanciations.cpp.o
[ 72%] Built target obj_daemon_rpc_server
[ 72%] Building CXX object monero/contrib/epee/src/CMakeFiles/epee.dir/buffer.cpp.o
[ 72%] Building CXX object monero/contrib/epee/src/CMakeFiles/epee.dir/net_ssl.cpp.o
In file included from /build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/transport.hpp:52,
                 from /build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/transport.cpp:42:
/build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/messages/messages-common.pb.h:751:5: warning: ‘hw::trezor::messages::common::ButtonRequest_ButtonRequestType__Deprecated_ButtonRequest_PassphraseType’ is deprecated [-Wdeprecated-declarations]
  751 |     ButtonRequest_ButtonRequestType__Deprecated_ButtonRequest_PassphraseType;
      |     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/messages/messages-common.pb.h:169:3: note: declared here
  169 |   ButtonRequest_ButtonRequestType__Deprecated_ButtonRequest_PassphraseType PROTOBUF_DEPRECATED_ENUM = 14,
      |   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[ 73%] Building CXX object monero/contrib/epee/src/CMakeFiles/epee.dir/int-util.cpp.o
/build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/transport.cpp: In function ‘size_t hw::trezor::message_size(const google::protobuf::Message&)’:
/build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/transport.cpp:159:44: warning: ‘int google::protobuf::MessageLite::ByteSize() const’ is deprecated: Please use ByteSizeLong() instead [-Wdeprecated-declarations]
  159 |     return static_cast<size_t>(req.ByteSize());
      |                                ~~~~~~~~~~~~^~
In file included from /usr/include/google/protobuf/any.h:38,
                 from /usr/include/google/protobuf/generated_message_util.h:49,
                 from /build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/messages_map.hpp:41,
                 from /build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/transport.hpp:49,
                 from /build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/transport.cpp:42:
/usr/include/google/protobuf/message_lite.h:433:7: note: declared here
  433 |   int ByteSize() const { return internal::ToIntSize(ByteSizeLong()); }
      |       ^~~~~~~~
[ 74%] Building CXX object monero/src/device_trezor/CMakeFiles/obj_device_trezor.dir/device_trezor_base.cpp.o
[ 74%] Building CXX object monero/src/wallet/api/CMakeFiles/obj_wallet_api.dir/transaction_info.cpp.o
[ 75%] Building CXX object monero/src/wallet/api/CMakeFiles/obj_wallet_api.dir/transaction_history.cpp.o
[ 75%] Building CXX object monero/src/wallet/api/CMakeFiles/obj_wallet_api.dir/pending_transaction.cpp.o
[ 75%] Building CXX object monero/src/wallet/CMakeFiles/obj_wallet.dir/wallet_args.cpp.o
[ 75%] Building CXX object monero/src/wallet/api/CMakeFiles/obj_wallet_api.dir/utils.cpp.o
[ 75%] Building CXX object monero/src/wallet/api/CMakeFiles/obj_wallet_api.dir/address_book.cpp.o
[ 75%] Built target obj_cryptonote_core
[ 75%] Building CXX object monero/src/wallet/CMakeFiles/obj_wallet.dir/ringdb.cpp.o
[ 75%] Building CXX object monero/src/wallet/api/CMakeFiles/obj_wallet_api.dir/subaddress.cpp.o
[ 75%] Built target obj_net
[ 76%] Building CXX object monero/src/wallet/api/CMakeFiles/obj_wallet_api.dir/subaddress_account.cpp.o
[ 76%] Linking CXX static library libepee.a
[ 76%] Built target epee
[ 77%] Linking CXX static library libcncrypto.a
[ 77%] Built target cncrypto
[ 77%] Linking CXX static library libmnemonics.a
[ 77%] Built target mnemonics
[ 77%] Linking CXX static library libcommon.a
[ 77%] Built target common
[ 77%] Linking CXX static library libwallet-crypto.a
[ 77%] Built target wallet-crypto
[ 77%] Linking CXX static library libringct_basic.a
[ 77%] Built target ringct_basic
[ 77%] Linking CXX static library libcryptonote_format_utils_basic.a
[ 77%] Built target cryptonote_format_utils_basic
[ 77%] Linking CXX static library libcheckpoints.a
[ 77%] Built target checkpoints
[ 77%] Linking CXX static library liblmdb_lib.a
[ 77%] Built target lmdb_lib
[ 78%] Linking CXX static library libnet.a
[ 78%] Built target net
[ 78%] Linking CXX static library librpc_base.a
[ 78%] Built target rpc_base
[ 78%] Linking CXX static library libdaemonizer.a
[ 78%] Built target daemonizer
[ 78%] Building CXX object monero/src/gen_ssl_cert/CMakeFiles/gen_ssl_cert.dir/gen_ssl_cert.cpp.o
[ 78%] Building CXX object monero/src/wallet/CMakeFiles/obj_wallet.dir/node_rpc_proxy.cpp.o
[ 78%] Building CXX object monero/src/wallet/api/CMakeFiles/obj_wallet_api.dir/unsigned_transaction.cpp.o
In file included from /build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/transport.hpp:52,
                 from /build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor.hpp:36,
                 from /build/monero-gui/src/monero-gui/monero/src/device_trezor/device_trezor_base.hpp:43,
                 from /build/monero-gui/src/monero-gui/monero/src/device_trezor/device_trezor_base.cpp:30:
/build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/messages/messages-common.pb.h:751:5: warning: ‘hw::trezor::messages::common::ButtonRequest_ButtonRequestType__Deprecated_ButtonRequest_PassphraseType’ is deprecated [-Wdeprecated-declarations]
  751 |     ButtonRequest_ButtonRequestType__Deprecated_ButtonRequest_PassphraseType;
      |     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/messages/messages-common.pb.h:169:3: note: declared here
  169 |   ButtonRequest_ButtonRequestType__Deprecated_ButtonRequest_PassphraseType PROTOBUF_DEPRECATED_ENUM = 14,
      |   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/build/monero-gui/src/monero-gui/monero/src/device_trezor/device_trezor_base.cpp: In member function ‘bool hw::trezor::device_trezor_base::message_handler(hw::trezor::GenericMessage&)’:
/build/monero-gui/src/monero-gui/monero/src/device_trezor/device_trezor_base.cpp:296:24: warning: ‘hw::trezor::messages::MessageType_Deprecated_PassphraseStateRequest’ is deprecated [-Wdeprecated-declarations]
  296 |         case messages::MessageType_Deprecated_PassphraseStateRequest:
      |                        ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from /build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/messages_map.hpp:47,
                 from /build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/transport.hpp:49,
                 from /build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor.hpp:36,
                 from /build/monero-gui/src/monero-gui/monero/src/device_trezor/device_trezor_base.hpp:43,
                 from /build/monero-gui/src/monero-gui/monero/src/device_trezor/device_trezor_base.cpp:30:
/build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/messages/messages.pb.h:100:3: note: declared here
  100 |   MessageType_Deprecated_PassphraseStateRequest PROTOBUF_DEPRECATED_ENUM = 77,
      |   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/build/monero-gui/src/monero-gui/monero/src/device_trezor/device_trezor_base.cpp: In member function ‘void hw::trezor::device_trezor_base::on_passphrase_request(hw::trezor::GenericMessage&, const hw::trezor::messages::common::PassphraseRequest*)’:
/build/monero-gui/src/monero-gui/monero/src/device_trezor/device_trezor_base.cpp:472:30: warning: ‘bool hw::trezor::messages::common::PassphraseRequest::has__on_device() const’ is deprecated [-Wdeprecated-declarations]
  472 |       if (msg->has__on_device() && msg->_on_device()){
      |           ~~~~~~~~~~~~~~~~~~~^~
In file included from /build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/transport.hpp:52,
                 from /build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor.hpp:36,
                 from /build/monero-gui/src/monero-gui/monero/src/device_trezor/device_trezor_base.hpp:43,
                 from /build/monero-gui/src/monero-gui/monero/src/device_trezor/device_trezor_base.cpp:30:
/build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/messages/messages-common.pb.h:2469:13: note: declared here
 2469 | inline bool PassphraseRequest::has__on_device() const {
      |             ^~~~~~~~~~~~~~~~~
/build/monero-gui/src/monero-gui/monero/src/device_trezor/device_trezor_base.cpp:472:51: warning: ‘bool hw::trezor::messages::common::PassphraseRequest::_on_device() const’ is deprecated [-Wdeprecated-declarations]
  472 |       if (msg->has__on_device() && msg->_on_device()){
      |                                    ~~~~~~~~~~~~~~~^~
In file included from /build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/transport.hpp:52,
                 from /build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor.hpp:36,
                 from /build/monero-gui/src/monero-gui/monero/src/device_trezor/device_trezor_base.hpp:43,
                 from /build/monero-gui/src/monero-gui/monero/src/device_trezor/device_trezor_base.cpp:30:
/build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/messages/messages-common.pb.h:2479:13: note: declared here
 2479 | inline bool PassphraseRequest::_on_device() const {
      |             ^~~~~~~~~~~~~~~~~
/build/monero-gui/src/monero-gui/monero/src/device_trezor/device_trezor_base.cpp:479:30: warning: ‘bool hw::trezor::messages::common::PassphraseRequest::has__on_device() const’ is deprecated [-Wdeprecated-declarations]
  479 |       if (msg->has__on_device() && !msg->_on_device()){
      |           ~~~~~~~~~~~~~~~~~~~^~
In file included from /build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/transport.hpp:52,
                 from /build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor.hpp:36,
                 from /build/monero-gui/src/monero-gui/monero/src/device_trezor/device_trezor_base.hpp:43,
                 from /build/monero-gui/src/monero-gui/monero/src/device_trezor/device_trezor_base.cpp:30:
/build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/messages/messages-common.pb.h:2469:13: note: declared here
 2469 | inline bool PassphraseRequest::has__on_device() const {
      |             ^~~~~~~~~~~~~~~~~
/build/monero-gui/src/monero-gui/monero/src/device_trezor/device_trezor_base.cpp:479:52: warning: ‘bool hw::trezor::messages::common::PassphraseRequest::_on_device() const’ is deprecated [-Wdeprecated-declarations]
  479 |       if (msg->has__on_device() && !msg->_on_device()){
      |                                     ~~~~~~~~~~~~~~~^~
In file included from /build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/transport.hpp:52,
                 from /build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor.hpp:36,
                 from /build/monero-gui/src/monero-gui/monero/src/device_trezor/device_trezor_base.hpp:43,
                 from /build/monero-gui/src/monero-gui/monero/src/device_trezor/device_trezor_base.cpp:30:
/build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/messages/messages-common.pb.h:2479:13: note: declared here
 2479 | inline bool PassphraseRequest::_on_device() const {
      |             ^~~~~~~~~~~~~~~~~
[ 79%] Building CXX object monero/src/wallet/CMakeFiles/obj_wallet.dir/message_store.cpp.o
[ 79%] Linking CXX executable ../../../bin/monero-gen-ssl-cert
[ 79%] Built target gen_ssl_cert
[ 80%] Linking CXX static library libdevice.a
[ 80%] Built target device
[ 80%] Building CXX object monero/src/wallet/CMakeFiles/obj_wallet.dir/message_transporter.cpp.o
[ 80%] Building CXX object monero/src/device_trezor/CMakeFiles/obj_device_trezor.dir/device_trezor.cpp.o
[ 80%] Building CXX object monero/src/device_trezor/CMakeFiles/obj_device_trezor.dir/trezor/messages/messages.pb.cc.o
[ 80%] Building CXX object monero/src/device_trezor/CMakeFiles/obj_device_trezor.dir/trezor/messages/messages-common.pb.cc.o
[ 80%] Built target obj_cryptonote_basic
[ 80%] Linking CXX static library libcryptonote_basic.a
[ 80%] Built target cryptonote_basic
[ 80%] Linking CXX static library libringct.a
[ 80%] Built target ringct
[ 80%] Linking CXX static library libmultisig.a
[ 80%] Built target multisig
[ 80%] Linking CXX static library libblockchain_db.a
[ 80%] Built target blockchain_db
[ 80%] Linking CXX static library libcryptonote_core.a
[ 80%] Built target cryptonote_core
[ 80%] Linking CXX static library libp2p.a
[ 80%] Built target p2p
In file included from /build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/messages/messages-common.pb.cc:4:
/build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/messages/messages-common.pb.h:751:5: warning: ‘hw::trezor::messages::common::ButtonRequest_ButtonRequestType__Deprecated_ButtonRequest_PassphraseType’ is deprecated [-Wdeprecated-declarations]
  751 |     ButtonRequest_ButtonRequestType__Deprecated_ButtonRequest_PassphraseType;
      |     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/messages/messages-common.pb.h:169:3: note: declared here
  169 |   ButtonRequest_ButtonRequestType__Deprecated_ButtonRequest_PassphraseType PROTOBUF_DEPRECATED_ENUM = 14,
      |   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[ 80%] Building CXX object monero/src/blockchain_utilities/CMakeFiles/blockchain_import.dir/blockchain_import.cpp.o
[ 80%] Building CXX object monero/src/blockchain_utilities/CMakeFiles/blockchain_import.dir/bootstrap_file.cpp.o
[ 80%] Building CXX object monero/src/device_trezor/CMakeFiles/obj_device_trezor.dir/trezor/messages/messages-management.pb.cc.o
[ 81%] Building CXX object monero/src/device_trezor/CMakeFiles/obj_device_trezor.dir/trezor/messages/messages-monero.pb.cc.o
[ 81%] Building CXX object monero/src/blockchain_utilities/CMakeFiles/blockchain_import.dir/blocksdat_file.cpp.o
[ 81%] Building CXX object monero/src/blockchain_utilities/CMakeFiles/blockchain_export.dir/blockchain_export.cpp.o
In file included from /build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/transport.hpp:52,
                 from /build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor.hpp:36,
                 from /build/monero-gui/src/monero-gui/monero/src/device_trezor/device_trezor.hpp:33,
                 from /build/monero-gui/src/monero-gui/monero/src/device_trezor/device_trezor.cpp:30:
/build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/messages/messages-common.pb.h:751:5: warning: ‘hw::trezor::messages::common::ButtonRequest_ButtonRequestType__Deprecated_ButtonRequest_PassphraseType’ is deprecated [-Wdeprecated-declarations]
  751 |     ButtonRequest_ButtonRequestType__Deprecated_ButtonRequest_PassphraseType;
      |     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/build/monero-gui/src/monero-gui/monero/src/device_trezor/trezor/messages/messages-common.pb.h:169:3: note: declared here
  169 |   ButtonRequest_ButtonRequestType__Deprecated_ButtonRequest_PassphraseType PROTOBUF_DEPRECATED_ENUM = 14,
      |   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[ 82%] Building CXX object monero/src/blockchain_utilities/CMakeFiles/blockchain_usage.dir/blockchain_usage.cpp.o
[ 82%] Building CXX object monero/src/blockchain_utilities/CMakeFiles/blockchain_ancestry.dir/blockchain_ancestry.cpp.o
[ 83%] Building CXX object monero/src/blockchain_utilities/CMakeFiles/blockchain_depth.dir/blockchain_depth.cpp.o
[ 83%] Built target obj_wallet_api
[ 83%] Building CXX object monero/src/blockchain_utilities/CMakeFiles/blockchain_stats.dir/blockchain_stats.cpp.o
[ 83%] Building CXX object monero/src/blockchain_utilities/CMakeFiles/blockchain_prune_known_spent_data.dir/blockchain_prune_known_spent_data.cpp.o
[ 83%] Building CXX object monero/src/wallet/CMakeFiles/obj_wallet.dir/wallet_rpc_payments.cpp.o
[ 83%] Building CXX object monero/src/blockchain_utilities/CMakeFiles/blockchain_prune.dir/blockchain_prune.cpp.o
[ 83%] Building CXX object monero/src/blockchain_utilities/CMakeFiles/blockchain_export.dir/bootstrap_file.cpp.o
[ 83%] Building CXX object monero/src/blockchain_utilities/CMakeFiles/blockchain_export.dir/blocksdat_file.cpp.o
/build/monero-gui/src/monero-gui/monero/src/blockchain_utilities/blockchain_ancestry.cpp: In instantiation of ‘void ancestry_state_t::serialize(t_archive&, unsigned int) [with t_archive = boost::archive::portable_binary_iarchive]’:
/usr/include/boost/serialization/access.hpp:116:20:   required from ‘static void boost::serialization::access::serialize(Archive&, T&, unsigned int) [with Archive = boost::archive::portable_binary_iarchive; T = ancestry_state_t]’
/usr/include/boost/serialization/serialization.hpp:59:22:   required from ‘void boost::serialization::serialize(Archive&, T&, unsigned int) [with Archive = boost::archive::portable_binary_iarchive; T = ancestry_state_t]’
/usr/include/boost/serialization/serialization.hpp:109:14:   required from ‘void boost::serialization::serialize_adl(Archive&, T&, unsigned int) [with Archive = boost::archive::portable_binary_iarchive; T = ancestry_state_t]’
/usr/include/boost/archive/detail/iserializer.hpp:187:40:   required from ‘void boost::archive::detail::iserializer<Archive, T>::load_object_data(boost::archive::detail::basic_iarchive&, void*, unsigned int) const [with Archive = boost::archive::portable_binary_iarchive; T = ancestry_state_t]’
/usr/include/boost/archive/detail/iserializer.hpp:409:27:   required from ‘static void boost::archive::detail::load_non_pointer_type<Archive>::load_standard::invoke(Archive&, const T&) [with T = ancestry_state_t; Archive = boost::archive::portable_binary_iarchive]’
/usr/include/boost/archive/detail/iserializer.hpp:461:22:   required from ‘static void boost::archive::detail::load_non_pointer_type<Archive>::invoke(Archive&, T&) [with T = ancestry_state_t; Archive = boost::archive::portable_binary_iarchive]’
/usr/include/boost/archive/detail/iserializer.hpp:624:18:   required from ‘void boost::archive::load(Archive&, T&) [with Archive = boost::archive::portable_binary_iarchive; T = ancestry_state_t]’
/usr/include/boost/archive/detail/common_iarchive.hpp:67:22:   required from ‘void boost::archive::detail::common_iarchive<Archive>::load_override(T&) [with T = ancestry_state_t; Archive = boost::archive::portable_binary_iarchive]’
/build/monero-gui/src/monero-gui/monero/external/boost/archive/portable_binary_iarchive.hpp:160:52:   required from ‘void boost::archive::portable_binary_iarchive::load_override(T&) [with T = ancestry_state_t]’
/usr/include/boost/archive/detail/interface_iarchive.hpp:68:36:   required from ‘Archive& boost::archive::detail::interface_iarchive<Archive>::operator>>(T&) [with T = ancestry_state_t; Archive = boost::archive::portable_binary_iarchive]’
/build/monero-gui/src/monero-gui/monero/src/blockchain_utilities/blockchain_ancestry.cpp:492:12:   required from here
/build/monero-gui/src/monero-gui/monero/src/blockchain_utilities/blockchain_ancestry.cpp:152:23: warning: loop variable ‘i’ creates a copy from type ‘const std::pair<const crypto::hash, cryptonote::transaction>’ [-Wrange-loop-construct]
  152 |       for (const auto i: old_tx_cache)
      |                       ^
/build/monero-gui/src/monero-gui/monero/src/blockchain_utilities/blockchain_ancestry.cpp:152:23: note: use reference type to prevent copying
  152 |       for (const auto i: old_tx_cache)
      |                       ^
      |                       &
/build/monero-gui/src/monero-gui/monero/src/blockchain_utilities/blockchain_ancestry.cpp:164:23: warning: loop variable ‘i’ creates a copy from type ‘const std::pair<const long unsigned int, cryptonote::block>’ [-Wrange-loop-construct]
  164 |       for (const auto i: old_block_cache)
      |                       ^
/build/monero-gui/src/monero-gui/monero/src/blockchain_utilities/blockchain_ancestry.cpp:164:23: note: use reference type to prevent copying
  164 |       for (const auto i: old_block_cache)
      |                       ^
      |                       &
/build/monero-gui/src/monero-gui/monero/src/blockchain_utilities/blockchain_ancestry.cpp: In instantiation of ‘void ancestry_state_t::serialize(t_archive&, unsigned int) [with t_archive = boost::archive::portable_binary_oarchive]’:
/usr/include/boost/serialization/access.hpp:116:20:   required from ‘static void boost::serialization::access::serialize(Archive&, T&, unsigned int) [with Archive = boost::archive::portable_binary_oarchive; T = ancestry_state_t]’
/usr/include/boost/serialization/serialization.hpp:59:22:   required from ‘void boost::serialization::serialize(Archive&, T&, unsigned int) [with Archive = boost::archive::portable_binary_oarchive; T = ancestry_state_t]’
/usr/include/boost/serialization/serialization.hpp:109:14:   required from ‘void boost::serialization::serialize_adl(Archive&, T&, unsigned int) [with Archive = boost::archive::portable_binary_oarchive; T = ancestry_state_t]’
/usr/include/boost/archive/detail/oserializer.hpp:153:40:   required from ‘void boost::archive::detail::oserializer<Archive, T>::save_object_data(boost::archive::detail::basic_oarchive&, const void*) const [with Archive = boost::archive::portable_binary_oarchive; T = ancestry_state_t]’
/usr/include/boost/archive/detail/oserializer.hpp:258:27:   required from ‘static void boost::archive::detail::save_non_pointer_type<Archive>::save_standard::invoke(Archive&, const T&) [with T = ancestry_state_t; Archive = boost::archive::portable_binary_oarchive]’
/usr/include/boost/archive/detail/oserializer.hpp:315:22:   required from ‘static void boost::archive::detail::save_non_pointer_type<Archive>::invoke(Archive&, const T&) [with T = ancestry_state_t; Archive = boost::archive::portable_binary_oarchive]’
/usr/include/boost/archive/detail/oserializer.hpp:539:18:   required from ‘void boost::archive::save(Archive&, T&) [with Archive = boost::archive::portable_binary_oarchive; T = const ancestry_state_t]’
/usr/include/boost/archive/detail/common_oarchive.hpp:71:22:   required from ‘void boost::archive::detail::common_oarchive<Archive>::save_override(T&) [with T = const ancestry_state_t; Archive = boost::archive::portable_binary_oarchive]’
/build/monero-gui/src/monero-gui/monero/external/boost/archive/portable_binary_oarchive.hpp:145:52:   required from ‘void boost::archive::portable_binary_oarchive::save_override(T&) [with T = const ancestry_state_t]’
/usr/include/boost/archive/detail/interface_oarchive.hpp:70:36:   required from ‘Archive& boost::archive::detail::interface_oarchive<Archive>::operator<<(const T&) [with T = ancestry_state_t; Archive = boost::archive::portable_binary_oarchive]’
/build/monero-gui/src/monero-gui/monero/src/blockchain_utilities/blockchain_ancestry.cpp:611:14:   required from here
/build/monero-gui/src/monero-gui/monero/src/blockchain_utilities/blockchain_ancestry.cpp:152:23: warning: loop variable ‘i’ creates a copy from type ‘const std::pair<const crypto::hash, cryptonote::transaction>’ [-Wrange-loop-construct]
  152 |       for (const auto i: old_tx_cache)
      |                       ^
/build/monero-gui/src/monero-gui/monero/src/blockchain_utilities/blockchain_ancestry.cpp:152:23: note: use reference type to prevent copying
  152 |       for (const auto i: old_tx_cache)
      |                       ^
      |                       &
/build/monero-gui/src/monero-gui/monero/src/blockchain_utilities/blockchain_ancestry.cpp:164:23: warning: loop variable ‘i’ creates a copy from type ‘const std::pair<const long unsigned int, cryptonote::block>’ [-Wrange-loop-construct]
  164 |       for (const auto i: old_block_cache)
      |                       ^
/build/monero-gui/src/monero-gui/monero/src/blockchain_utilities/blockchain_ancestry.cpp:164:23: note: use reference type to prevent copying
  164 |       for (const auto i: old_block_cache)
      |                       ^
      |                       &
[ 83%] Linking CXX executable ../../../bin/monero-blockchain-usage
[ 83%] Built target blockchain_usage
[ 84%] Linking CXX static library libcryptonote_protocol.a
[ 84%] Built target cryptonote_protocol
[ 84%] Linking CXX static library libserialization.a
[ 84%] Built target serialization
[ 84%] Linking CXX static library librpc_pub.a
[ 84%] Linking CXX static library libdaemon_messages.a
[ 84%] Built target rpc_pub
[ 84%] Built target daemon_messages
[ 84%] Linking CXX executable ../../../bin/monero-blockchain-import
[ 84%] Built target blockchain_import
[ 84%] Built target obj_device_trezor
[ 84%] Linking CXX static library libdevice_trezor.a
[ 84%] Linking CXX executable ../../../bin/monero-blockchain-depth
[ 84%] Built target device_trezor
[ 84%] Built target blockchain_depth
[ 84%] Linking CXX executable ../../../bin/monero-blockchain-stats
[ 84%] Built target blockchain_stats
[ 84%] Linking CXX executable ../../../bin/monero-blockchain-prune-known-spent-data
[ 86%] Linking CXX executable ../../../bin/monero-blockchain-export
[ 86%] Built target blockchain_prune_known_spent_data
[ 86%] Built target blockchain_export
[ 87%] Linking CXX executable ../../../bin/monero-blockchain-prune
[ 87%] Built target blockchain_prune
[ 87%] Linking CXX executable ../../../bin/monero-blockchain-ancestry
[ 87%] Built target blockchain_ancestry
/build/monero-gui/src/monero-gui/monero/src/rpc/core_rpc_server.cpp: In member function ‘bool cryptonote::core_rpc_server::on_rpc_access_data(const request&, cryptonote::COMMAND_RPC_ACCESS_DATA::response&, epee::json_rpc::error&, const connection_context*)’:
/build/monero-gui/src/monero-gui/monero/src/rpc/core_rpc_server.cpp:3375:14: warning: ‘r’ may be used uninitialized in this function [-Wmaybe-uninitialized]
 3375 |       return r;
      |              ^
/build/monero-gui/src/monero-gui/monero/src/rpc/core_rpc_server.cpp: In member function ‘bool cryptonote::core_rpc_server::on_get_limit(const request&, cryptonote::COMMAND_RPC_GET_LIMIT::response&, const connection_context*)’:
/build/monero-gui/src/monero-gui/monero/src/rpc/core_rpc_server.cpp:2772:14: warning: ‘r’ may be used uninitialized in this function [-Wmaybe-uninitialized]
 2772 |       return r;
      |              ^
/build/monero-gui/src/monero-gui/monero/src/rpc/core_rpc_server.cpp: In member function ‘bool cryptonote::core_rpc_server::on_get_version(const request&, cryptonote::COMMAND_RPC_GET_VERSION::response&, epee::json_rpc::error&, const connection_context*)’:
/build/monero-gui/src/monero-gui/monero/src/rpc/core_rpc_server.cpp:2695:14: warning: ‘r’ may be used uninitialized in this function [-Wmaybe-uninitialized]
 2695 |       return r;
      |              ^
/build/monero-gui/src/monero-gui/monero/src/rpc/core_rpc_server.cpp: In member function ‘bool cryptonote::core_rpc_server::on_get_height(const request&, cryptonote::COMMAND_RPC_GET_HEIGHT::response&, const connection_context*)’:
/build/monero-gui/src/monero-gui/monero/src/rpc/core_rpc_server.cpp:428:14: warning: ‘r’ may be used uninitialized in this function [-Wmaybe-uninitialized]
  428 |       return r;
      |              ^
[ 87%] Built target obj_wallet
[ 87%] Linking CXX static library ../../../lib/libwallet.a
[ 87%] Linking CXX static library ../../../lib/libwallet_merged.a
[ 87%] Built target wallet
[ 88%] Building CXX object monero/src/wallet/CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o
[ 88%] Building CXX object monero/src/gen_multisig/CMakeFiles/gen_multisig.dir/gen_multisig.cpp.o
[ 88%] Building CXX object monero/src/simplewallet/CMakeFiles/simplewallet.dir/simplewallet.cpp.o
[ 88%] Building CXX object monero/src/blockchain_utilities/CMakeFiles/blockchain_blackball.dir/blockchain_blackball.cpp.o
[ 88%] Linking CXX static library ../../../../lib/libwallet_api.a
[ 88%] Built target wallet_api
[ 88%] Automatic MOC and UIC for target monero-wallet-gui
[ 88%] Built target wallet_merged
[ 88%] Built target obj_rpc
[ 89%] Linking CXX static library librpc.a
[ 89%] Built target rpc
[ 89%] Linking CXX static library libdaemon_rpc_server.a
[ 89%] Built target daemon_rpc_server
[ 89%] Building CXX object monero/src/daemon/CMakeFiles/daemon.dir/command_parser_executor.cpp.o
[ 89%] Building CXX object monero/src/daemon/CMakeFiles/daemon.dir/command_server.cpp.o
[ 89%] Building CXX object monero/src/daemon/CMakeFiles/daemon.dir/daemon.cpp.o
[ 89%] Building CXX object monero/src/daemon/CMakeFiles/daemon.dir/executor.cpp.o
[ 89%] Building CXX object monero/src/daemon/CMakeFiles/daemon.dir/main.cpp.o
[ 90%] Building CXX object monero/src/daemon/CMakeFiles/daemon.dir/rpc_command_executor.cpp.o
[ 90%] Built target monero-wallet-gui_autogen
/build/monero-gui/src/monero-gui/monero/src/wallet/wallet_rpc_server.cpp: In member function ‘bool tools::wallet_rpc_server::on_get_account_tags(const request&, tools::wallet_rpc::COMMAND_RPC_GET_ACCOUNT_TAGS::response&, epee::json_rpc::error&, const connection_context*)’:
/build/monero-gui/src/monero-gui/monero/src/wallet/wallet_rpc_server.cpp:690:53: warning: loop variable ‘p’ of type ‘const std::pair<std::__cxx11::basic_string<char>, std::__cxx11::basic_string<char> >&’ binds to a temporary constructed from type ‘const std::pair<const std::__cxx11::basic_string<char>, std::__cxx11::basic_string<char> >’ [-Wrange-loop-construct]
  690 |     for (const std::pair<std::string, std::string>& p : account_tags.first)
      |                                                     ^
/build/monero-gui/src/monero-gui/monero/src/wallet/wallet_rpc_server.cpp:690:53: note: use non-reference type ‘const std::pair<std::__cxx11::basic_string<char>, std::__cxx11::basic_string<char> >’ to make the copy explicit or ‘const std::pair<const std::__cxx11::basic_string<char>, std::__cxx11::basic_string<char> >&’ to prevent copying
/build/monero-gui/src/monero-gui/monero/src/simplewallet/simplewallet.cpp: In member function ‘void cryptonote::simple_wallet::print_accounts()’:
/build/monero-gui/src/monero-gui/monero/src/simplewallet/simplewallet.cpp:9443:51: warning: loop variable ‘p’ of type ‘const std::pair<std::__cxx11::basic_string<char>, std::__cxx11::basic_string<char> >&’ binds to a temporary constructed from type ‘const std::pair<const std::__cxx11::basic_string<char>, std::__cxx11::basic_string<char> >’ [-Wrange-loop-construct]
 9443 |   for (const std::pair<std::string, std::string>& p : account_tags.first)
      |                                                   ^
/build/monero-gui/src/monero-gui/monero/src/simplewallet/simplewallet.cpp:9443:51: note: use non-reference type ‘const std::pair<std::__cxx11::basic_string<char>, std::__cxx11::basic_string<char> >’ to make the copy explicit or ‘const std::pair<const std::__cxx11::basic_string<char>, std::__cxx11::basic_string<char> >&’ to prevent copying
[ 91%] Linking CXX executable ../../../bin/monero-gen-trusted-multisig
[ 91%] Built target gen_multisig
[ 91%] Linking CXX executable ../../../bin/monero-blockchain-mark-spent-outputs
[ 91%] Built target blockchain_blackball
[ 91%] Linking CXX executable ../../../bin/monerod
[ 91%] Built target daemon
[ 91%] Generating qrc_qml.cpp
[ 92%] Building CXX object src/CMakeFiles/monero-wallet-gui.dir/libwalletqt/PassphraseHelper.cpp.o
[ 92%] Building CXX object src/CMakeFiles/monero-wallet-gui.dir/libwalletqt/PendingTransaction.cpp.o
[ 92%] Building CXX object src/CMakeFiles/monero-wallet-gui.dir/libwalletqt/TransactionHistory.cpp.o
[ 93%] Building CXX object src/CMakeFiles/monero-wallet-gui.dir/libwalletqt/TransactionInfo.cpp.o
[ 93%] Building CXX object src/CMakeFiles/monero-wallet-gui.dir/daemon/DaemonManager.cpp.o
[ 93%] Building CXX object src/CMakeFiles/monero-wallet-gui.dir/libwalletqt/UnsignedTransaction.cpp.o
[ 93%] Building CXX object src/CMakeFiles/monero-wallet-gui.dir/libwalletqt/AddressBook.cpp.o
[ 93%] Building CXX object src/CMakeFiles/monero-wallet-gui.dir/libwalletqt/Subaddress.cpp.o
[ 93%] Building CXX object src/CMakeFiles/monero-wallet-gui.dir/libwalletqt/QRCodeImageProvider.cpp.o
[ 93%] Building CXX object src/CMakeFiles/monero-wallet-gui.dir/TranslationManager.cpp.o
[ 93%] Building CXX object src/CMakeFiles/monero-wallet-gui.dir/libwalletqt/Wallet.cpp.o
[ 93%] Building CXX object src/CMakeFiles/monero-wallet-gui.dir/libwalletqt/SubaddressAccount.cpp.o
[ 93%] Building CXX object src/CMakeFiles/monero-wallet-gui.dir/monero-wallet-gui_autogen/mocs_compilation.cpp.o
[ 94%] Building CXX object src/CMakeFiles/monero-wallet-gui.dir/libwalletqt/WalletListenerImpl.cpp.o
[ 94%] Building CXX object src/CMakeFiles/monero-wallet-gui.dir/libwalletqt/WalletManager.cpp.o
[ 94%] Building CXX object src/CMakeFiles/monero-wallet-gui.dir/main/Logger.cpp.o
[ 94%] Building CXX object src/CMakeFiles/monero-wallet-gui.dir/main/MainApp.cpp.o
[ 95%] Building CXX object src/CMakeFiles/monero-wallet-gui.dir/main/filter.cpp.o
[ 95%] Building CXX object src/CMakeFiles/monero-wallet-gui.dir/main/clipboardAdapter.cpp.o
[ 95%] Building CXX object src/CMakeFiles/monero-wallet-gui.dir/main/main.cpp.o
[ 95%] Building CXX object src/CMakeFiles/monero-wallet-gui.dir/main/oscursor.cpp.o
[ 95%] Building CXX object src/CMakeFiles/monero-wallet-gui.dir/main/oshelper.cpp.o
[ 95%] Building CXX object src/CMakeFiles/monero-wallet-gui.dir/model/AddressBookModel.cpp.o
[ 95%] Building CXX object src/CMakeFiles/monero-wallet-gui.dir/model/SubaddressAccountModel.cpp.o
[ 96%] Building CXX object src/CMakeFiles/monero-wallet-gui.dir/model/SubaddressModel.cpp.o
[ 96%] Building CXX object src/CMakeFiles/monero-wallet-gui.dir/model/TransactionHistoryModel.cpp.o
[ 96%] Building CXX object src/CMakeFiles/monero-wallet-gui.dir/model/TransactionHistorySortFilterModel.cpp.o
[ 96%] Building CXX object src/CMakeFiles/monero-wallet-gui.dir/qt/FutureScheduler.cpp.o
[ 96%] Building CXX object src/CMakeFiles/monero-wallet-gui.dir/qt/KeysFiles.cpp.o
[ 97%] Building CXX object src/CMakeFiles/monero-wallet-gui.dir/qt/MoneroSettings.cpp.o
[ 97%] Building CXX object src/CMakeFiles/monero-wallet-gui.dir/qt/TailsOS.cpp.o
[ 97%] Building CXX object src/CMakeFiles/monero-wallet-gui.dir/qt/downloader.cpp.o
[ 97%] Building CXX object src/CMakeFiles/monero-wallet-gui.dir/qt/ipc.cpp.o
[ 97%] Building CXX object src/CMakeFiles/monero-wallet-gui.dir/qt/network.cpp.o
[ 97%] Building CXX object src/CMakeFiles/monero-wallet-gui.dir/qt/updater.cpp.o
[ 98%] Building CXX object src/CMakeFiles/monero-wallet-gui.dir/qt/utils.cpp.o
[ 98%] Building CXX object src/CMakeFiles/monero-wallet-gui.dir/qrc_qml.cpp.o
[100%] Linking CXX executable ../../../bin/monero-wallet-cli
[100%] Built target simplewallet
[100%] Linking CXX executable ../bin/monero-wallet-gui
[100%] Built target monero-wallet-gui
[100%] Linking CXX executable ../../../bin/monero-wallet-rpc
[100%] Built target wallet_rpc_server
==> Entering fakeroot environment...
==> Starting package()...
==> Tidying install...
  -> Removing libtool files...
  -> Purging unwanted files...
  -> Removing static library files...
  -> Stripping unneeded symbols from binaries and libraries...
  -> Compressing man and info pages...
==> Checking for packaging issues...
==> WARNING: Package contains reference to $srcdir
usr/bin/monero-wallet-gui
==> Creating package "monero-gui"...
  -> Generating .PKGINFO file...
==> WARNING: Library listed in 'depends' is not required by any files: libudev.so
  -> Generating .BUILDINFO file...
warning: database file for 'core' does not exist (use '-Sy' to download)
warning: database file for 'extra' does not exist (use '-Sy' to download)
warning: database file for 'community' does not exist (use '-Sy' to download)
  -> Generating .MTREE file...
  -> Compressing package...
==> Leaving fakeroot environment.
==> Finished making: monero-gui 0.17.3.0-2 (Thu 16 Dec 2021 06:44:31 AM UTC)
==> Cleaning up...
  -> Delete snapshot for monero-gui_915964...
==> Comparing hashes...
==> Package is reproducible!
```

</details>

Any hints what might be missing? Is there a compile time check that might disable hardware wallet support? Some users in the Arch bugtracker reported running the official binary works for them, and running the Arch binary as root works too (if I'm reading this right, which is confusing).

## selsta | 2021-12-17T16:44:24+00:00
> Any hints what might be missing?

If I had to guess it's related to how Qt is compiled / installed on Arch, and not monero-gui itself.

> This is how the Arch Linux package is compiled 

There is no compile time option missing here.

# Action History
- Created by: Josef37 | 2021-06-16T21:22:54+00:00
- Closed at: 2021-06-17T23:51:24+00:00
