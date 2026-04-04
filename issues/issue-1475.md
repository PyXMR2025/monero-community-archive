---
title: error bild win 64
source_url: https://github.com/monero-project/monero-gui/issues/1475
author: laricoins
assignees: []
labels:
- resolved
created_at: '2018-06-25T19:57:32+00:00'
updated_at: '2019-04-23T18:45:42+00:00'
type: issue
status: closed
closed_at: '2019-04-23T18:45:42+00:00'
---

# Original Description
hi.
pls say list  pkg to way bild application on win 64
--------------------------------------------
i'm use  MSYS2
1 step 
pacman -S mingw-w64-x86_64-toolchain make mingw-w64-x86_64-cmake mingw-w64-x86_64-boost mingw-w64-x86_64-openssl mingw-w64-x86_64-zeromq mingw-w64-x86_64-libsodium
2 step
pacman -S mingw-w64-x86_64-qt5
3 step
pacman -S git
4 step
git clone https://github.com/monero-project/monero-gui.git
5 step
cd monero-gui
./build.sh

and give error

pls list version pkg to succes bild from repo (example http://www2.futureware.at/~nickoe/msys2-mirror/mingw/x86_64/)
via
FROM 
pacman -S mingw-w64-x86_64-qt5 
TO 
```
wget -c http://www2.futureware.at/~nickoe/msys2-mirror/mingw/x86_64/mingw-w64-x86_64-qt5-5.8.0-2-any.pkg.tar.xz
pacman -U mingw-w64-x86_64-qt5-5.8.0-2-any.pkg.tar.xz
```

need all pkg list version  to good bild.


**pls 
type
```
cd /var/cache/pacman/pkg
ls
```
and post list file**

Thancks








# Discussion History
## dEBRUYNE-1 | 2019-04-23T18:21:24+00:00
I am doing some housekeeping and closing all old build relates issues, as they are probably not relevant anymore.



## dEBRUYNE-1 | 2019-04-23T18:21:29+00:00
+resolved

# Action History
- Created by: laricoins | 2018-06-25T19:57:32+00:00
- Closed at: 2019-04-23T18:45:42+00:00
