---
title: Gitian build fails trying to find qttranslations-everywhere-src-5.15.1
source_url: https://github.com/monero-project/monero/issues/8599
author: lobster-kerouac
assignees: []
labels: []
created_at: '2022-09-28T03:49:18+00:00'
updated_at: '2022-09-30T14:25:51+00:00'
type: issue
status: closed
closed_at: '2022-09-30T14:25:50+00:00'
---

# Original Description
I am trying to run Gitian build instructions on a VM with Ubuntu 18.04.6 LTS. I am using the `docker` version of the instructions and ran `./gitian-build.py --setup $GH_USER $VERSION` with no issues. When running the main build script however I get the following error (truncated just a bit to ignore some successful downloads of depends sources):

```
$ ./gitian-build.py --docker --no-commit --detach-sign --build $GH_USER $VERSION
HEAD is now at 7cbae6ca9 Merge pull request #8545
make: Entering directory '/home/gitianuser/build/builder/inputs/monero/contrib/depends'
make[1]: Entering directory '/home/gitianuser/build/builder/inputs/monero/contrib/depends'
Fetching qtbase-everywhere-src-5.15.1.tar.xz from https://download.qt.io/official_releases/qt/5.15/5.15.1/submodules
 
## Some download status that times out after 16 seconds

curl: (35) OpenSSL SSL_connect: SSL_ERROR_SYSCALL in connection to mirrors.ocf.berkeley.edu:443 
Fetching qtbase-everywhere-src-5.15.1.tar.xz from https://downloads.getmonero.org/depends-sources

## Download succeeds 

/home/gitianuser/build/builder/inputs/monero/contrib/depends/work/download/qt-5.15.1/qtbase-everywhere-src-5.15.1.tar.xz.temp: OK
Fetching qttranslations-everywhere-src-5.15.1.tar.xz from https://download.qt.io/official_releases/qt/5.15/5.15.1/submodules
  
## Some download status that times out after 16 seconds

curl: (35) OpenSSL SSL_connect: SSL_ERROR_SYSCALL in connection to mirrors.ocf.berkeley.edu:443 
Fetching qttranslations-everywhere-src-5.15.1.tar.xz from https://downloads.getmonero.org/depends-sources

## Download status that fails

curl: (22) The requested URL returned error: 404 Not Found
funcs.mk:264: recipe for target '/home/gitianuser/build/builder/cache/common/download-stamps/.stamp_fetched-qt-qtbase-everywhere-src-5.15.1.tar.xz.hash' failed
make[1]: *** [/home/gitianuser/build/builder/cache/common/download-stamps/.stamp_fetched-qt-qtbase-everywhere-src-5.15.1.tar.xz.hash] Error 22
make[1]: Leaving directory '/home/gitianuser/build/builder/inputs/monero/contrib/depends'
Makefile:221: recipe for target 'download-osx' failed
make: *** [download-osx] Error 2
make: Leaving directory '/home/gitianuser/build/builder/inputs/monero/contrib/depends'
v0.18.1.1

Checking Depends Freshness

Traceback (most recent call last):
  File "./gitian-build.py", line 203, in <module>
    main()
  File "./gitian-build.py", line 193, in main
    build()
  File "./gitian-build.py", line 96, in build
    subprocess.check_call(['make', '-C', 'inputs/monero/contrib/depends', 'download', 'SOURCES_PATH=' + os.getcwd() + '/cache/common'])
  File "/usr/lib/python3.6/subprocess.py", line 311, in check_call
    raise CalledProcessError(retcode, cmd)
subprocess.CalledProcessError: Command '['make', '-C', 'inputs/monero/contrib/depends', 'download', 'SOURCES_PATH=/home/gitianuser/build/builder/cache/common']' returned non-zero exit status 2.
```

This seems like the script simply can't find `qttranslations-everywhere-src-5.15.1` either from the official mirror or the getmonero.org backup. I am missing something really obvious here? Why was `qtbase-everywhere-src-5.15.1` found, but not `qttranslations`?

For the record, the VERSION I am trying to build is `v0.18.1.1`, but I get the same failure when trying `v0.18.1.0`.

Any help is greatly appreciated. Thanks!

# Discussion History
## selsta | 2022-09-28T03:51:21+00:00
Try v0.18.1.2, we removed the Qt package in that version.

## lobster-kerouac | 2022-09-28T04:08:28+00:00
Thanks for the quick reply. I tried v0.18.1.2 and the build has started so it's definitely past the `qt` issue.

So I think this specific issue is technically resolved, but I'm still curious what happened to the `qt` sources for versions less than `v0.18.1.2`. It's not for me to say, but it might still be an issue that past (actually current!) versions can't be built.

## selsta | 2022-09-28T19:29:19+00:00
It's not clear from your logs what exactly is failing.

All these links are online, so I would assume it is an issue with your local setup if you get SSL errors?

- https://download.qt.io/official_releases/qt/5.15/5.15.1/submodules/qttranslations-everywhere-src-5.15.1.tar.xz
- https://download.qt.io/official_releases/qt/5.15/5.15.1/submodules/qttools-everywhere-src-5.15.1.tar.xz
- https://download.qt.io/official_releases/qt/5.15/5.15.1/submodules/qtbase-everywhere-src-5.15.1.tar.xz

Unless the Qt website had issues yesterday and it's fixed now.

## lobster-kerouac | 2022-09-30T14:25:50+00:00
Thanks for the reply. That sent me down a wild maze of rabbit holes, but at the end of the day it was an issue with the VPN on my host machine. Yeesh.

Thanks for your time.

# Action History
- Created by: lobster-kerouac | 2022-09-28T03:49:18+00:00
- Closed at: 2022-09-30T14:25:50+00:00
