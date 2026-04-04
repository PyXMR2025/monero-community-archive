---
title: I can't build monero-gui on gentoo linux.
source_url: https://github.com/monero-project/monero-gui/issues/3182
author: crocket
assignees: []
labels: []
created_at: '2020-10-19T13:46:23+00:00'
updated_at: '2021-06-29T22:51:43+00:00'
type: issue
status: closed
closed_at: '2021-06-29T03:02:28+00:00'
---

# Original Description
This is the ebuild file used to build monero-gui-0.17.1.1.

```
# Copyright 1999-2020 Gentoo Authors
# Distributed under the terms of the GNU General Public License v2

EAPI=7

inherit xdg

DESCRIPTION="A Qt GUI wallet for monero"
HOMEPAGE="https://github.com/monero-project/monero-gui"
SRC_URI="https://github.com/monero-project/${PN}/archive/v${PV}.tar.gz"
LISENCE="BSD"

SLOT="0"
KEYWORDS="~amd64"
IUSE="test"

BDEPEND="app-arch/xz-utils
	app-doc/doxygen
	dev-util/cmake
	test? ( dev-cpp/gtest )"
DEPEND="dev-libs/boost
	dev-libs/expat
	dev-libs/openssl
	net-libs/ldns
	net-libs/miniupnpc
	net-libs/zeromq
	sys-libs/libunwind
	dev-libs/libsodium
	dev-libs/hidapi
	dev-libs/libgcrypt
	net-dns/unbound
	dev-qt/qtcore:5
	dev-qt/qtdeclarative:5
	dev-qt/qtquickcontrols:5
	dev-qt/qtquickcontrols2:5
	dev-qt/qtgraphicaleffects:5"
RDEPEND="media-gfx/graphviz
	${DEPEND}"
DOCS="README.md"

src_compile() {
	emake release
}

src_install() {
	emake DESTIDR="${D}" install
	einstalldocs
	insinto /usr/share/applications
	doins ${FILESIDR}/${PN}.desktop
}
```

This is the error I see.

```
CMake Error at CMakeLists.txt:425 (add_c_flag_if_supported):
  Unknown CMake command "add_c_flag_if_supported".
```

# Discussion History
## 00-matt | 2020-10-19T14:06:16+00:00
You should use the CMake eclass and call CMake directly, instead of using Monero's Makefile.

**edit** Also feel free to contribute to [the Monero overlay :)](https://github.com/gentoo-monero/gentoo-monero)

## xiphon | 2020-10-19T14:08:35+00:00
You have to clone the repo with git. Github ships incomplete tar archives (without submodules).

## crocket | 2020-10-19T14:44:17+00:00
I used `git-r3` eclass to push through the error. But, I see new errors.

```
/usr/include/qt5/QtNetwork/qtnetwork-config.h:6: error: "QT_LINKED_OPENSSL" redefined [-Werror]
    6 | #define QT_LINKED_OPENSSL true
/usr/include/qt5/Gentoo/gentoo-qconfig.h:7: note: this is the location of the previous definition
    7 | #define QT_LINKED_OPENSSL
```

## 00-matt | 2020-10-19T14:54:47+00:00
The `QT_LINKED_OPENSSL` thing is a Gentoo bug. I think the easiest "solution" is to build without `-Werror`/with `-Wno-error=whatever-the-warning-is`.

## bjacquin | 2020-10-19T22:56:17+00:00
I addressed this bug in my overlay with the following patch:

```
iff --git a/CMakeLists.txt b/CMakeLists.txt
index 197e7c301120..a865ec4fa922 100644
--- a/CMakeLists.txt
+++ b/CMakeLists.txt
@@ -422,8 +422,6 @@ if(APPLE)
 endif()
 
 # warnings
-add_c_flag_if_supported(-Werror C_SECURITY_FLAGS)
-add_cxx_flag_if_supported(-Werror CXX_SECURITY_FLAGS)
 add_c_flag_if_supported(-Wformat C_SECURITY_FLAGS)
 add_cxx_flag_if_supported(-Wformat CXX_SECURITY_FLAGS)
 add_c_flag_if_supported(-Wformat-security C_SECURITY_FLAGS)
diff --git a/monero-wallet-gui.pro b/monero-wallet-gui.pro
index 271786236b98..49506e09e9e2 100644
--- a/monero-wallet-gui.pro
+++ b/monero-wallet-gui.pro
@@ -187,8 +187,8 @@ android {
 
 
 
-QMAKE_CXXFLAGS += -Werror -Wformat -Wformat-security
-QMAKE_CFLAGS += -Werror -Wformat -Wformat-security
+QMAKE_CXXFLAGS += -Wformat -Wformat-security
+QMAKE_CFLAGS += -Wformat -Wformat-security
 QMAKE_CXXFLAGS_RELEASE += -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -O2
 QMAKE_CFLAGS_RELEASE += -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -O2
 
```

See: https://git.pants-on.net/gentoo/portage.git/tree/net-p2p/monero/files/monero-gui-0.17.1.1-cmake-remove-Werror.patch

## crocket | 2020-10-20T05:22:10+00:00
After applying the patch, I see this error.

```
 * QA Notice: The following files contain writable and executable sections
 *  Files with such sections will not work properly (or at all!) on some
 *  architectures/operating systems.  A bug should be filed at
 *  https://bugs.gentoo.org/ to make sure the issue is fixed.
 *  For more information, see:
 * 
 *    https://wiki.gentoo.org/wiki/Hardened/GNU_stack_quickstart
 * 
 *  Please include the following list of files in your report:
 *  Note: Bugs should be filed for the respective maintainers
 *  of the package in question and not hardened@gentoo.org.
 * !WX --- --- usr/lib/libwallet_merged.a:CryptonightR_template.S.o

Files matching a file type that is not allowed:
   usr/lib/libeasylogging.so
   usr/lib/liblmdb.so
 * ERROR: gui-apps/monero-gui-0.17.1.1::crocket-overlay failed:
 *   multilib-strict check failed!
```

cmake doesn't put libraries in /usr/lib64, but /usr/lib. Is it possible to specify libdir to cmake?

## bjacquin | 2020-10-20T18:07:40+00:00
The full ebuild is available on https://git.pants-on.net/gentoo/portage.git/tree/net-p2p/monero/monero-0.17.1.1.ebuild. The ebuild itself is particularly awful since monero is unfortunately not packaging friendly due requirement on git, cmake files need to good refactoring, hard dependency of monero-gui to monero source code also implied the code is compiled twice, things I'd like to tackle when time permits

## selsta | 2020-10-20T18:14:40+00:00
Thanks @bjacquin 

I assume this is resolved.

## crocket | 2020-10-21T06:55:11+00:00
Recursive dependency on git submodules is awful. I gave up on compiling monero-gui on gentoo for now.

## 00-matt | 2020-10-21T10:04:24+00:00
> Recursive dependency on git submodules is awful

If you use `git-r3.eclass`, the repository at `EGIT_REPO_URI` will be cloned along with all of its submodules (recursively). Alternatively you can use a script like [`git archive-all`](https://github.com/roehling/git-archive-all) to create a tarball that includes submodules, and host that yourself.

## crocket | 2020-10-21T11:52:11+00:00
git-r3 takes care of recursive git submodules, but cmake files still don't allow me to configure libdir.
I also hope that monero-gui was refactored so that it doesn't use git submodules. It's not elegant.

## 00-matt | 2020-10-21T12:26:16+00:00
Yes, it would be very nice if the main Monero project could install a libwallet library to your system for this GUI (and other wallets) to search for.

## xiphon | 2020-10-22T01:31:49+00:00
Monero doesn't depend on Git anyhow. That's just a way to obtain the source code. It builds just fine without git.

> Recursive dependency on git submodules is awful. 

We don't have recursive dependency. At all. None.

> I also hope that monero-gui was refactored so that it doesn't use git submodules. It's not elegant.

No, Git submodules is perfect instrument. Unless you provide reasonable explanation.

```
time git clone https://github.com/monero-project/monero-gui --depth 1 --recurse-submodules --shallow-submodules

Receiving objects: 100% (492/492), 4.05 MiB | 3.63 MiB/s, done.
Receiving objects: 100% (1426/1426), 8.72 MiB | 3.44 MiB/s, done.
Receiving objects: 100% (326/326), 455.59 KiB | 1.97 MiB/s, done.
Receiving objects: 100% (153/153), 1.68 MiB | 3.35 MiB/s, done.
Receiving objects: 100% (342/342), 1.05 MiB | 3.57 MiB/s, done.
Receiving objects: 100% (118/118), 269.99 KiB | 1.57 MiB/s, done.
Receiving objects: 100% (299/299), 1.28 MiB | 2.78 MiB/s, done.
Receiving objects: 100% (1352/1352), 5.49 MiB | 5.08 MiB/s, done.
Receiving objects: 100% (107/107), 29.05 KiB | 3.23 MiB/s, done.
Receiving objects: 100% (285/285), 977.24 KiB | 1.64 MiB/s, done.
Receiving objects: 100% (347/347), 702.11 KiB | 2.85 MiB/s, done.
Receiving objects: 100% (122/122), 46.69 KiB | 3.33 MiB/s, done.
Receiving objects: 100% (2081/2081), 642.38 KiB | 2.75 MiB/s, done.

real    0m33.236s
user    0m5.147s
sys     0m4.624s
```

33 seconds and 39.19 MB total! That's all you need to get Monero GUI source code.

What's wrong with you guys?

Awful. 

PS: PRs are welcome. Twice as awful.

## crocket | 2020-10-22T07:39:36+00:00
Instead of git submodules, I suggest depending on dynamic libraries. monero-gui can depend on monero's dynamic libraries.

Another problem is that monero-gui builds monero binaries such as monerod and monero-wallet-cli. Monero already has monerod and monero-wallet-cli.

Right now, the blocking issue is that cmake files don't allow me to configure libdir.

## l29ah | 2021-06-01T01:13:41+00:00
I can build monero-gui on gentoo linux! emerge monero-gui::booboo
It's a mess tho.

## selsta | 2021-06-29T03:02:28+00:00
Closing this as it seem possible to build on gentoo according to @l29ah

## crocket | 2021-06-29T22:46:18+00:00
It's possible, but it requires hacks. There should be a new issue for hacks.

## selsta | 2021-06-29T22:47:50+00:00
We are most likely not going to change submodules for a single linux OS. Other operating system don't seem to have any issues and can build without any hacks.

But I'm also not familiar with gentoo :)

## l29ah | 2021-06-29T22:51:43+00:00
I doubt they can build monero-gui w/o building monerod at the same time.

# Action History
- Created by: crocket | 2020-10-19T13:46:23+00:00
- Closed at: 2021-06-29T03:02:28+00:00
