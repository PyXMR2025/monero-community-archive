---
title: 'Fails to build on macOs 10.12 '
source_url: https://github.com/monero-project/monero-gui/issues/35
author: dternyak
assignees: []
labels: []
created_at: '2016-10-05T07:34:44+00:00'
updated_at: '2016-10-07T06:17:10+00:00'
type: issue
status: closed
closed_at: '2016-10-07T06:17:10+00:00'
---

# Original Description
I think there is a missing file in the source due to this error and the fact that I can't find the header file (wallet2_api.h) manually: 

`
In file included from ../main.cpp:38:
../src/libwalletqt/WalletManager.h:6:10: fatal error:
      'wallet/wallet2_api.h' file not found
# include <wallet/wallet2_api.h>

`

Full stacktrace below:

```~/desktop/monero-core ~/desktop/monero-core
/Users/danielternyak2/Qt/5.7/clang_64/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_de.ts -qm /Users/danielternyak2/Desktop/monero-core/build/release/bin/monero-core.app/Contents/Resources/translations/monero-core_de.qm
Updating '/Users/danielternyak2/Desktop/monero-core/build/release/bin/monero-core.app/Contents/Resources/translations/monero-core_de.qm'...
Removing translations equal to source text in '/Users/danielternyak2/Desktop/monero-core/build/release/bin/monero-core.app/Contents/Resources/translations/monero-core_de.qm'...
    Generated 125 translation(s) (125 finished and 0 unfinished)
    Ignored 11 untranslated source text(s)
/Users/danielternyak2/Qt/5.7/clang_64/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_zh.ts -qm /Users/danielternyak2/Desktop/monero-core/build/release/bin/monero-core.app/Contents/Resources/translations/monero-core_zh.qm
Updating '/Users/danielternyak2/Desktop/monero-core/build/release/bin/monero-core.app/Contents/Resources/translations/monero-core_zh.qm'...
Removing translations equal to source text in '/Users/danielternyak2/Desktop/monero-core/build/release/bin/monero-core.app/Contents/Resources/translations/monero-core_zh.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 147 untranslated source text(s)
/Users/danielternyak2/Qt/5.7/clang_64/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_ru.ts -qm /Users/danielternyak2/Desktop/monero-core/build/release/bin/monero-core.app/Contents/Resources/translations/monero-core_ru.qm
Updating '/Users/danielternyak2/Desktop/monero-core/build/release/bin/monero-core.app/Contents/Resources/translations/monero-core_ru.qm'...
Removing translations equal to source text in '/Users/danielternyak2/Desktop/monero-core/build/release/bin/monero-core.app/Contents/Resources/translations/monero-core_ru.qm'...
    Generated 4 translation(s) (4 finished and 0 unfinished)
    Ignored 141 untranslated source text(s)
/Users/danielternyak2/Qt/5.7/clang_64/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_it.ts -qm /Users/danielternyak2/Desktop/monero-core/build/release/bin/monero-core.app/Contents/Resources/translations/monero-core_it.qm
Updating '/Users/danielternyak2/Desktop/monero-core/build/release/bin/monero-core.app/Contents/Resources/translations/monero-core_it.qm'...
Removing translations equal to source text in '/Users/danielternyak2/Desktop/monero-core/build/release/bin/monero-core.app/Contents/Resources/translations/monero-core_it.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 147 untranslated source text(s)
/Users/danielternyak2/Qt/5.7/clang_64/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_pl.ts -qm /Users/danielternyak2/Desktop/monero-core/build/release/bin/monero-core.app/Contents/Resources/translations/monero-core_pl.qm
Updating '/Users/danielternyak2/Desktop/monero-core/build/release/bin/monero-core.app/Contents/Resources/translations/monero-core_pl.qm'...
Removing translations equal to source text in '/Users/danielternyak2/Desktop/monero-core/build/release/bin/monero-core.app/Contents/Resources/translations/monero-core_pl.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 147 untranslated source text(s)
/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang++ -c -pipe -stdlib=libc++ -O2 -std=gnu++11 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.12.sdk -mmacosx-version-min=10.8 -Wall -W -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-core -I. -I/Users/danielternyak2/Desktop/monero-core/monero/include -I../src/libwalletqt -I../../../Qt/5.7/clang_64/lib/QtQuick.framework/Headers -I../../../Qt/5.7/clang_64/lib/QtWidgets.framework/Headers -I../../../Qt/5.7/clang_64/lib/QtGui.framework/Headers -I../../../Qt/5.7/clang_64/lib/QtQml.framework/Headers -I../../../Qt/5.7/clang_64/lib/QtNetwork.framework/Headers -I../../../Qt/5.7/clang_64/lib/QtCore.framework/Headers -I. -I/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.12.sdk/System/Library/Frameworks/OpenGL.framework/Headers -I/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.12.sdk/System/Library/Frameworks/AGL.framework/Headers -I../../../Qt/5.7/clang_64/mkspecs/macx-clang -F/Users/danielternyak2/Qt/5.7/clang_64/lib -o main.o ../main.cpp
In file included from ../main.cpp:38:
../src/libwalletqt/WalletManager.h:6:10: fatal error:
      'wallet/wallet2_api.h' file not found
# include <wallet/wallet2_api.h>

```
     ^
```

1 error generated.
make: **\* [main.o] Error 1
macdeployqt /Users/danielternyak2/Desktop/monero-core/build/release/bin/monero-core.app -qmldir=/Users/danielternyak2/Desktop/monero-core
ERROR: Could not find bundle binary for "/Users/danielternyak2/Desktop/monero-core/build/release/bin/monero-core.app"
ERROR: "/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/objdump: '': No such file or directory.\nfatal error: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/otool: internal objdump command failed\n"
ERROR: "/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/objdump: '': No such file or directory.\nfatal error: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/otool: internal objdump command failed\n"
make: **\* [deploy] Segmentation fault: 11
~/desktop/monero-core```


# Discussion History
## ghost | 2016-10-05T07:42:43+00:00
Had the same error few minutes ago on my machine:

```
/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.12.sdk/System/Library/Frameworks/AGL.framework/Headers -I../../../../Qt/5.7/clang_64/mkspecs/macx-clang -F/Users/foo/Qt/5.7/clang_64/lib -o moc_TranslationManager.o moc_TranslationManager.cpp
/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang++ -headerpad_max_install_names -stdlib=libc++ -Wl,-syslibroot,/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.12.sdk -mmacosx-version-min=10.8 -Wl,-rpath,/Users/foo/Qt/5.7/clang_64/lib -o release/bin/monero-core.app/Contents/MacOS/monero-core main.o filter.o clipboardAdapter.o oscursor.o WalletManager.o Wallet.o PendingTransaction.o TransactionHistory.o TransactionInfo.o oshelper.o TranslationManager.o qrc_qml.o moc_filter.o moc_clipboardAdapter.o moc_oscursor.o moc_WalletManager.o moc_Wallet.o moc_PendingTransaction.o moc_TransactionHistory.o moc_TransactionInfo.o moc_oshelper.o moc_TranslationManager.o   -F/Users/foo/Qt/5.7/clang_64/lib -L/Users/foo/Development/crypto/monero-core/monero/lib -lwallet_merged -lunbound -L/usr/local/lib -lboost_serialization -lboost_thread-mt -lboost_system -lboost_date_time -lboost_filesystem -lboost_regex -lboost_chrono -lboost_program_options -lssl -lcrypto -ldl -framework QtQuick -framework QtQml -framework QtNetwork -framework QtCore -framework DiskArbitration -framework IOKit -framework QtGui -framework QtWidgets -framework OpenGL -framework AGL 
ld: library not found for -lssl
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make: *** [release/bin/monero-core.app/Contents/MacOS/monero-core] Error 1
macdeployqt /Users/foo/Development/crypto/monero-core/build/release/bin/monero-core.app -qmldir=/Users/foo/Development/crypto/monero-core
ERROR: Could not find bundle binary for "/Users/foo/Development/crypto/monero-core/build/release/bin/monero-core.app"
ERROR: "/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/objdump: '': No such file or directory.\nfatal error: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/otool: internal objdump command failed\n"
ERROR: "/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/objdump: '': No such file or directory.\nfatal error: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/otool: internal objdump command failed\n"
make: *** [deploy] Segmentation fault: 11
```


## dternyak | 2016-10-05T07:43:51+00:00
@maitscha Similar, but not the same. You're missing a library, I'm missing a file. Try installing that library. 


## Jaqueeee | 2016-10-05T08:17:06+00:00
Looks like the libwallet api library didn't get built. Do you get any errors when running ./get_libwallet_api.sh ? Ensure that you have a monero/lib/libwallet_merged.a after running that script. @dternyak


## dternyak | 2016-10-05T08:18:21+00:00
@Jaqueeee I'm just running `bash build.sh`. I'll try to do some steps manually and see if there's a bug in the script.


## dternyak | 2016-10-05T08:22:57+00:00
@Jaqueeee So manually running `get_libwallet_api.sh` and then build.sh worked. 


## ghost | 2016-10-05T08:33:17+00:00
@dternyak I installed OpenSSL with `brew install openssl`, but the error doesn't go away. What libraries have you installed prior to running `build.sh`?


## Jaqueeee | 2016-10-05T14:25:47+00:00
@dternyak That's good news. I would guess you already had a monero dir from old build?  get_library_api.sh isn't executed in build.sh if that dir already exists. 


## dternyak | 2016-10-05T16:20:36+00:00
@Jaqueeee I doubt it, never built from source before.


# Action History
- Created by: dternyak | 2016-10-05T07:34:44+00:00
- Closed at: 2016-10-07T06:17:10+00:00
