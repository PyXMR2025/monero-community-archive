---
title: Building on macOS Mojave 10.14 produces non-working monero-wallet-gui.app
source_url: https://github.com/monero-project/monero-gui/issues/1672
author: teutat3s
assignees: []
labels:
- resolved
created_at: '2018-10-16T20:52:11+00:00'
updated_at: '2018-12-27T15:09:28+00:00'
type: issue
status: closed
closed_at: '2018-12-27T15:09:28+00:00'
---

# Original Description
Dear Devs,

I cloned a fresh copy of the git repo, installed all required dependencies, and despite `./build.sh` running through the whole build process seemingly without errors, the produced `monero-wallet-gui.app` is just 28.4MB in size instead of the 301.9MB of the downloaded release of v13.0.3. 

When I start the GUI, no error messages appear, but in Mission Control it looks like an empty window. The GUI is not visible.

Looking inside the .app I can see from comparison that the following is missing:

`Frameworks` folder
`PlugIns` folder
in `MacOS` folder there are only two binaries: `monero-wallet-gui` and `monerod`

This is on macOS Mojave (10.14).

GUI Log file:

[monero-wallet-gui.log](https://github.com/monero-project/monero-gui/files/2484862/monero-wallet-gui.log)



How do I proceed to help finding the culprit here? 

# Discussion History
## sanderfoobar | 2018-10-18T10:52:08+00:00
We've seen problems with others that compiled using Qt 5.11.2 on Windows, so it might be worth to try Qt 5.11.1. I also must note that the GUI is made specifically for Qt 5.7.*, so it is even better to use this version if you can. Our official releases for OSX use this version.

In addition, providing the output of `./build.sh` is helpful. Lastly, make sure to use the latest `release-v0.13` branch: `git checkout release-v0.13 && git pull origin release-v0.13`

## sanderfoobar | 2018-10-18T11:10:05+00:00
One more thing:

https://github.com/monero-project/monero-gui/blob/2ca48fb6bc80922c9db506f74a756dc0a6070b0a/get_libwallet_api.sh#L20

Set this to `git -C $MONERO_DIR checkout v0.13.0.3`

## pazos | 2018-10-20T00:41:46+00:00
@Teutone 

```
cd build
make deploy
```

This will copy qt frameworks and required libraries to the application bundle. There is a PR opened to automate this action #1360  but got no atention so far.

## jacobmort | 2018-10-30T18:46:05+00:00
> ```
> cd build
> make deploy
> ```

When I do this then run the binary I get this error and it crashes
```
objc[65256]: Class QMacAutoReleasePoolTracker is implemented in both /usr/local/opt/qt/lib/QtCore.framework/Versions/5/QtCore (0x104976fa8) and /Users/jacob/Projects/monero-gui/build/release/bin/monero-wallet-gui.app/Contents/Frameworks/QtCore.framework/Versions/5/QtCore (0x1085bffa8). One of the two will be used. Which one is undefined.
objc[65256]: Class QT_ROOT_LEVEL_POOL__THESE_OBJECTS_WILL_BE_RELEASED_WHEN_QAPP_GOES_OUT_OF_SCOPE is implemented in both /usr/local/opt/qt/lib/QtCore.framework/Versions/5/QtCore (0x104977020) and /Users/jacob/Projects/monero-gui/build/release/bin/monero-wallet-gui.app/Contents/Frameworks/QtCore.framework/Versions/5/QtCore (0x1085c0020). One of the two will be used. Which one is undefined.
objc[65256]: Class RunLoopModeTracker is implemented in both /usr/local/opt/qt/lib/QtCore.framework/Versions/5/QtCore (0x104977048) and /Users/jacob/Projects/monero-gui/build/release/bin/monero-wallet-gui.app/Contents/Frameworks/QtCore.framework/Versions/5/QtCore (0x1085c0048). One of the two will be used. Which one is undefined.
QObject::moveToThread: Current thread (0x7fcae1e01340) is not the object's thread (0x7fcae1f0d590).
Cannot move to target thread (0x7fcae1e01340)

You might be loading two sets of Qt binaries into the same process. Check that all plugins are compiled against the right Qt binaries. Export DYLD_PRINT_LIBRARIES=1 and check that only one set of binaries are being loaded.
qt.qpa.plugin: Could not load the Qt platform plugin "cocoa" in "" even though it was found.
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

Available platform plugins are: cocoa.

[1]    65256 abort      build/release/bin/monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui
```

## pazos | 2018-10-31T18:35:21+00:00
@ubien: Something is wrong with your setup. Could you please use `otool -L /path/to/monero-gui.app/Contents/MacOS/monero-wallet-gui` and post here the output. Also please download one of the releases and do the same.

Did you install qt by yourself or using brew? Which qt version? is in your PATH?


## pazos | 2018-10-31T18:38:21+00:00
If everything is on path I would expect that calling the binary (under app bundle -> Contents -> MacOs) with the arguments `-platform cocoa` works.

## jacobmort | 2018-11-01T18:35:53+00:00
> Did you install qt by yourself or using brew? 

brew
> Which qt version? 

5.11.2
> is in your PATH?

```/usr/local/opt/qt5/bin:/usr/local/Cellar/qt/5.11.2/bin/``` is

Compiled 13.0.4:
```
build/release/bin/monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui:
	/usr/local/opt/boost/lib/libboost_serialization.dylib (compatibility version 0.0.0, current version 0.0.0)
	/usr/local/opt/hidapi/lib/libhidapi.0.dylib (compatibility version 1.0.0, current version 1.0.0)
	/usr/local/opt/boost/lib/libboost_thread-mt.dylib (compatibility version 0.0.0, current version 0.0.0)
	/usr/local/opt/boost/lib/libboost_system.dylib (compatibility version 0.0.0, current version 0.0.0)
	/usr/local/opt/boost/lib/libboost_date_time.dylib (compatibility version 0.0.0, current version 0.0.0)
	/usr/local/opt/boost/lib/libboost_filesystem.dylib (compatibility version 0.0.0, current version 0.0.0)
	/usr/local/opt/boost/lib/libboost_regex.dylib (compatibility version 0.0.0, current version 0.0.0)
	/usr/local/opt/boost/lib/libboost_chrono.dylib (compatibility version 0.0.0, current version 0.0.0)
	/usr/local/opt/boost/lib/libboost_program_options.dylib (compatibility version 0.0.0, current version 0.0.0)
	/usr/local/opt/openssl/lib/libssl.1.0.0.dylib (compatibility version 1.0.0, current version 1.0.0)
	/usr/local/opt/libsodium/lib/libsodium.23.dylib (compatibility version 25.0.0, current version 25.0.0)
	/usr/local/opt/openssl/lib/libcrypto.1.0.0.dylib (compatibility version 1.0.0, current version 1.0.0)
	/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1252.200.5)
	/System/Library/Frameworks/PCSC.framework/Versions/A/PCSC (compatibility version 1.0.0, current version 1.0.0)
	/usr/local/opt/qt/lib/QtQuick.framework/Versions/5/QtQuick (compatibility version 5.11.0, current version 5.11.2)
	/usr/local/opt/qt/lib/QtGui.framework/Versions/5/QtGui (compatibility version 5.11.0, current version 5.11.2)
	/usr/local/opt/qt/lib/QtCore.framework/Versions/5/QtCore (compatibility version 5.11.0, current version 5.11.2)
	/System/Library/Frameworks/DiskArbitration.framework/Versions/A/DiskArbitration (compatibility version 1.0.0, current version 1.0.0)
	/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)
	/usr/local/opt/qt/lib/QtQml.framework/Versions/5/QtQml (compatibility version 5.11.0, current version 5.11.2)
	/usr/local/opt/qt/lib/QtNetwork.framework/Versions/5/QtNetwork (compatibility version 5.11.0, current version 5.11.2)
	/usr/local/opt/qt/lib/QtWidgets.framework/Versions/5/QtWidgets (compatibility version 5.11.0, current version 5.11.2)
	/System/Library/Frameworks/OpenGL.framework/Versions/A/OpenGL (compatibility version 1.0.0, current version 1.0.0)
	/System/Library/Frameworks/AGL.framework/Versions/A/AGL (compatibility version 1.0.0, current version 1.0.0)
	/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 400.9.4)```
```
[Downloaded 13.0.4](https://downloads.getmonero.org/gui/monero-gui-mac-x64-v0.13.0.4.tar.bz2) (runs fine):
```
	@executable_path/../Frameworks/libboost_serialization.dylib (compatibility version 0.0.0, current version 0.0.0)
	@executable_path/../Frameworks/libhidapi.0.dylib (compatibility version 1.0.0, current version 1.0.0)
	@executable_path/../Frameworks/libboost_thread-mt.dylib (compatibility version 0.0.0, current version 0.0.0)
	@executable_path/../Frameworks/libboost_system.dylib (compatibility version 0.0.0, current version 0.0.0)
	@executable_path/../Frameworks/libboost_date_time.dylib (compatibility version 0.0.0, current version 0.0.0)
	@executable_path/../Frameworks/libboost_filesystem.dylib (compatibility version 0.0.0, current version 0.0.0)
	@executable_path/../Frameworks/libboost_regex.dylib (compatibility version 0.0.0, current version 0.0.0)
	@executable_path/../Frameworks/libboost_chrono.dylib (compatibility version 0.0.0, current version 0.0.0)
	@executable_path/../Frameworks/libboost_program_options.dylib (compatibility version 0.0.0, current version 0.0.0)
	@executable_path/../Frameworks/libssl.1.0.0.dylib (compatibility version 1.0.0, current version 1.0.0)
	@executable_path/../Frameworks/libsodium.23.dylib (compatibility version 25.0.0, current version 25.0.0)
	@executable_path/../Frameworks/libcrypto.1.0.0.dylib (compatibility version 1.0.0, current version 1.0.0)
	/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1238.0.0)
	/System/Library/Frameworks/PCSC.framework/Versions/A/PCSC (compatibility version 1.0.0, current version 1.0.0)
	@rpath/QtQuick.framework/Versions/5/QtQuick (compatibility version 5.7.0, current version 5.7.0)
	@rpath/QtQml.framework/Versions/5/QtQml (compatibility version 5.7.0, current version 5.7.0)
	@rpath/QtNetwork.framework/Versions/5/QtNetwork (compatibility version 5.7.0, current version 5.7.0)
	@rpath/QtCore.framework/Versions/5/QtCore (compatibility version 5.7.0, current version 5.7.0)
	/System/Library/Frameworks/DiskArbitration.framework/Versions/A/DiskArbitration (compatibility version 1.0.0, current version 1.0.0)
	/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)
	@rpath/QtGui.framework/Versions/5/QtGui (compatibility version 5.7.0, current version 5.7.0)
	@rpath/QtWidgets.framework/Versions/5/QtWidgets (compatibility version 5.7.0, current version 5.7.0)
	/System/Library/Frameworks/OpenGL.framework/Versions/A/OpenGL (compatibility version 1.0.0, current version 1.0.0)
	/System/Library/Frameworks/AGL.framework/Versions/A/AGL (compatibility version 1.0.0, current version 1.0.0)
	/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 307.4.0)
```

## pazos | 2018-11-01T20:16:56+00:00
@ubien: it seems that macdeployqt didn't work. macdeployqt is a binary installed as part of Qt and is the tool used to modify the path for libraries/frameworks to use the ones placed inside the app bundle instead of the system ones (as you can see in the differences between your compiled app and the downloaded one). It uses otool internally.

Your compiled application should work if you're running it with `build/release/bin/monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui -platform cocoa` but is not redistributable because it expects to find the libraries under /usr/local/opt.

You can try to uninstall brew's qt and install an official release from https://download.qt.io/official_releases/qt/5.9/5.9.7, or simply clean the build tree with `rm -rf build/` and build the application again and post the output of `make deploy`

## BigslimVdub | 2018-11-29T04:49:17+00:00
brew install location for QT should be ``/usr/local/Cellar/qt/5.11.2_1``
Check if it is actually in that location then run ``export PATH=$PATH:$/usr/local/Cellar/qt/5.11.2_1``

also, make sure to upgrade all dependencies `` brew upgrade `` and clean up old installs after upgrading with ``brew cleanup``

Make sure all dependencies are installed and do a fresh pull and checkout of the latest v0.13.0.4

## dEBRUYNE-1 | 2018-12-17T08:04:22+00:00
@Teutone - Are you still incurring this particular issue? 

## dEBRUYNE-1 | 2018-12-27T15:08:54+00:00
Author has not responded and therefore I am going to close this issue. 

## dEBRUYNE-1 | 2018-12-27T15:08:59+00:00
+resolved

# Action History
- Created by: teutat3s | 2018-10-16T20:52:11+00:00
- Closed at: 2018-12-27T15:09:28+00:00
