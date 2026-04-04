---
title: '[Feature] Bump Qt requirements to 5.12'
source_url: https://github.com/monero-project/monero-gui/issues/1787
author: sanderfoobar
assignees: []
labels: []
created_at: '2018-12-07T07:33:24+00:00'
updated_at: '2019-04-23T13:19:58+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
GUI uses ~~5.7.1~~ 5.7.0 as the base Qt version. This release is from December 2016. 

Using a relatively older version has proven to be useful in terms of compatibility with older distributions.

However.. Newer versions have bugfixes and fancy features. More specifically, 5.12 [which released recently](https://wiki.qt.io/New_Features_in_Qt_5.12) has embedded ECMAScript7 (modern iteration of Javascript) which I'm most excited about.

#### Challenges

- Build systems should get updated
- Find out it's compatibility on older systems
- Compilation will become harder (for casual users that want to compile themselves), as our newly adopted version is not yet in their distro's apt repos.

# Discussion History
## dEBRUYNE-1 | 2018-12-08T07:26:47+00:00
I suggest we bump the QT version for the first 0.14 point release. This ensures a fallback is provided (because the 0.14 major version would be built with the old QT version) in case any issues arise from the QT version upgrade. 

## sanderfoobar | 2018-12-08T10:01:40+00:00
Yep, sounds good.

## pazos | 2018-12-10T14:01:36+00:00
You'll break compatibility with all linux distros with little to no gain.

## xiphon | 2018-12-10T20:11:33+00:00
FYI, just checked MSYS2. Mingw QT 5.12 package is available now.

## dEBRUYNE-1 | 2018-12-10T21:51:32+00:00
@pazos - can you perhaps elaborate? 

## mmbyday | 2018-12-16T02:59:31+00:00
Insightful discussion on QT versions over at the bitcoin issue tracker.

`https://github.com/bitcoin/bitcoin/issues/13478`

tldr;

- QT 5.12 is a LTS release with support good for 3 years or until ~December 2021.  Other versions:

QT Version | Support until
------------ | -------------
5.12 (LTS) | 3 years post release (Likely December 2018).
5.11 | May 2019
5.10 | Dec 2018
5.9 (LTS) | May 31, 2020
5.6 (LTS) | March 16, 2019

- Any other releases older than 5.9 are no longer supported (by Qt).

- These are the officially supported OS platforms for QT 5.12, and if upgraded, by extension, monero-gui.

OS | Version
------------ | -------------
macOS | > 10.12
Windows | 7, 8.1 and 10
Ubuntu | 16.04 and 18.04
RHEL | > 7.4
OpenSUSE | > 43.2
Android | 4.1, 5, 6, 7, 8 (API Level 16)
iOS | 11, 12


## sanderfoobar | 2018-12-16T11:07:30+00:00
Thanks for the info @mmbyday 

So Windows is trivial and should not cause problems. Linux would bump the requirement from Ubuntu 14.04 to 16.04. I guess what matters here is the libc version. If a monero-gui build using Qt5.12 is build statically, it should run on Debian 8, etc.

As for MacOS, it's unfortunate 10.10, 10.11 are not on the 5.12 compatibility list but not the end of the world. I am certain we can ignore these versions because **the added benefit for us developers of being able to use new features and bugfixes outweigh the user's trouble of having to upgrade an OS**. Most (old) Apple hardware support an upgrade to 10.12.

Some key features of Qt5.12 that directly benefit us:
- Improved performance and reduced memory consumption
  - QML/JS engine should be couple factors faster
  - 30-50% (?) reduction in RAM footprint when running monero-gui
- ecmascript7 - allows for OOP JS, meaning, less spaghetti JS intertwined with QML.
- Fixes various DPI scaling issues
- Wayland support
- Ton of other fixes

For opponents: How long do we want to support 10.10 and 10.11? Does it justify the technical debt?

## pazos | 2018-12-17T01:32:56+00:00
>  can you perhaps elaborate?

I will be glad, sorry for the delay @dEBRUYNE-1 @xmrdsc @mmbyday @xiphon.

> GUI uses 5.7.1 as the base Qt version

Not true, [GUI requires 5.7.0 as the minimum version](https://github.com/monero-project/monero-gui/blob/master/monero-wallet-gui.pro#L2-L4). Yes, I guess that the build system is using 5.7.1, but that shouldn't matter for bumping qt requirements.

Qt version was bumped the last time from 5.4 to introduce qtquickcontrols2 and this check was written to warn users because it was possible to build without errors and after that find errors at runtime (qml module isn't found).

> Any other releases older than 5.9 are no longer supported (by Qt).

True. 5.9 would be the next logical bump *if* required. Has good support everywhere, without doing magic repo updates, qtwebkit -discontinued in 5.6- is available as a module on most distributions (and a lot of packages depends on it).

> So Windows is trivial and should not cause problems. Linux would bump the requirement from Ubuntu 14.04 to 16.04. I guess what matters here is the libc version. If a monero-gui build using Qt5.12 is build statically, it should run on Debian 8, etc.

Of course
On windows we deploy qt as dll. Linux (where I believe we static link) shouldn't be a problem even with qt shared libraries since we can deploy them on target and locate them at runtime using LD_LIBRARY_PATH

> I guess what matters here is the libc version. If a monero-gui build using Qt5.12 is build statically, it should run on Debian 8, etc.

Yeah, libc and libstdc++ will be problematic. Buildbot should be run on the oldest linux distro as possible (to avoid unknown symbols). This is today something with gcc4.8 and c+11 support. I'll guess that qt5.12 will run without problems even on 14.04.

> As for MacOS, it's unfortunate 10.10, 10.11 are not on the 5.12 compatibility list but not the end of the world. I am certain we can ignore these versions because the added benefit for us developers of being able to use new features and bugfixes outweigh the user's trouble of having to upgrade an OS. Most (old) Apple hardware support an upgrade to 10.12

We shoudn't have any problems on mac too. Even mojave supports 10.09 as the minimum target. Probably the most realistic minimum is what brew offers. Not officialy supported doesn't mean that shouldn't work, but if you found an upstream bug you're alone unless you can replicate it on a supported os.

> For opponents: How long do we want to support 10.10 and 10.11? Does it justify the technical debt?

I think that your thesis is: lets bump the build system. This is fine and I agree. You can use a recent toolchain and build the application linked to new Qt versions.

My thesis is: do not bump minimum requirements without a reason. If you build something that *requires* a new qt version and it is not trivial to make it compatible with qt5.7/5.9 then bump qt and please update the check to the newer minimum version

### In short
Sorry if my last comment was rude. I just mean that *today* bump qt minimum version, per se, does not make sense. Bump the buildbot to a newer qt version seems a good idea to me, too :dancer: 

BTW, nice work guys, heads up! :+1: 


## ghost | 2019-04-23T10:29:30+00:00
qt.5.9.1 cannot build this am getting this error

../src/libwalletqt/WalletManager.cpp:51:16: error: 'virtual void WalletPassphraseListenerImpl::onDeviceButtonPressed()' marked 'override', but does not override
   virtual void onDeviceButtonPressed() override
                ^
../src/libwalletqt/WalletManager.cpp:56:16: error: 'virtual void WalletPassphraseListenerImpl::onSetWallet(Monero::Wallet*)' marked 'override', but does not override
   virtual void onSetWallet(Monero::Wallet * wallet) override
                ^


## selsta | 2019-04-23T13:19:58+00:00
@claprox Please try to do `rm -r build monero` first and then build again.

# Action History
- Created by: sanderfoobar | 2018-12-07T07:33:24+00:00
