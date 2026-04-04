---
title: 'lrelease: could not find a Qt installation of '''''
source_url: https://github.com/monero-project/monero/issues/3053
author: danrmiller
assignees: []
labels: []
created_at: '2018-01-03T16:31:37+00:00'
updated_at: '2018-01-03T17:36:55+00:00'
type: issue
status: closed
closed_at: '2018-01-03T17:36:55+00:00'
---

# Original Description
I think resulting from #2934. I'm not familiar with lrelease and don't have a man page and get the same error just running `lrelease --help`

https://build.getmonero.org/builders/monero-static-ubuntu-amd64/builds/3039/steps/compile/logs/stdio

```
[  0%] Building C object translations/CMakeFiles/generate_translations_header.dir/generate_translations_header.c.o
[  1%] Linking C executable generate_translations_header
lrelease: could not find a Qt installation of ''
make[3]: *** [translations/generate_translations_header] Error 1
translations/CMakeFiles/generate_translations_header.dir/build.make:94: recipe for target 'translations/generate_translations_header' failed
```

# Discussion History
## danrmiller | 2018-01-03T16:41:40+00:00
Is QT Linguist used for the daemon? This would be a new tool dependency I think.
http://doc.qt.io/qt-5/linguist-manager.html

## glv2 | 2018-01-03T17:27:27+00:00
The *lrelease* program from Qt is used to compile the translation files located in *translations/*.

The *translations/CMakeLists.txt* file checks if the *lrelease* program is present, and if it's not, translations are ignored but the build doesn't fail.

In your case it looks like *lrelease* is installed, but not working properly.

Could you try to use it by hand to see if it works?

``` shell
cd translations/
lrelease monero_fr.ts
```

If it works a file named *monero_fr.qm" should be created.


## danrmiller | 2018-01-03T17:29:08+00:00
So this does work on systems where QT is installed and configured:

https://build.getmonero.org/builders/monero-static-ubuntu-i686/builds/2949/steps/compile/logs/stdio
```
make[3]: Entering directory '/home/vagrant/slave/monero-static-ubuntu-i686/build/build/release'
[  0%] Building C object translations/CMakeFiles/generate_translations_header.dir/generate_translations_header.c.o
[  1%] Linking C executable generate_translations_header
Updating 'monero_fr.qm'...
    Generated 485 translation(s) (485 finished and 0 unfinished)
    Ignored 16 untranslated source text(s)
Updating 'monero_it.qm'...
    Generated 497 translation(s) (497 finished and 0 unfinished)
    Ignored 4 untranslated source text(s)
Updating 'monero.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 501 untranslated source text(s)
Generating embedded translations header
make[3]: Leaving directory '/home/vagrant/slave/monero-static-ubuntu-i686/build/build/release'
[  1%] Built target generate_translations_header
```

There seem to be quite a lot of dependencies necessary to get lrelease and qmake configured, that many people are probably not going to want to install to build the daemon. So luckily on systems without lrelease the build doesn't stop, and we get this warning:
```
CMake Warning at translations/CMakeLists.txt:36 (message):
  lrelease program not found, translation files not built
```

I'll close this ticket shortly then, but I am having issues on some platforms with the new `generate_translations_header` binary #2934 adds, particularly cross-compiling. I'll open new issues to deal with those specifically.

# Action History
- Created by: danrmiller | 2018-01-03T16:31:37+00:00
- Closed at: 2018-01-03T17:36:55+00:00
