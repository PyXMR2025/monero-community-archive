---
title: 'ld: symbol(s) not found for architecture x86_64'
source_url: https://github.com/monero-project/monero-gui/issues/1735
author: CokeBear666
assignees: []
labels:
- resolved
created_at: '2018-11-12T08:01:18+00:00'
updated_at: '2018-12-27T15:18:31+00:00'
type: issue
status: closed
closed_at: '2018-12-27T15:18:31+00:00'
---

# Original Description
on Mac OS 10.14 
boost 1.68
![image](https://user-images.githubusercontent.com/6119459/48333947-17952a00-e694-11e8-8f17-ccebc3d44269.png)


# Discussion History
## sanderfoobar | 2018-11-18T16:55:19+00:00
Stuff I was able to find:

https://qiita.com/misho/items/0c0b3ca25bb8f62aa681
https://stackoverflow.com/a/28119190
https://github.com/litecoin-project/litecoin/issues/170
https://github.com/bitcoin/bitcoin/issues/3228

Solution probably is to reinstall boost.

## BigslimVdub | 2018-11-29T04:39:41+00:00
I just compiled monero with git checkout v0.13.0.4 today on 10.13.6 no issues. I do however get this issue compiling Aeon. 

You can reinstall all dependencies with 

```
brew reinstall gcc boost --c++11 openssl pkgconfig cmake zeromq libsodium libusb unbound libunwind-headers xz ldns pcsc-lite miniupnpc readline expat libgtest doxygen graphviz hidapi qt5
```

Also after that, don't forget to clean up old installs with:

```
brew cleanup
```

Latest QT on osx is 5.11.2_1

Don't forget to link QT with this (if installed via brew)

```
export PATH=$PATH:$/usr/local/Cellar/qt/5.11.2_1
```

let me know if this works for you on mojave 10.14. I have held off upgrading since there were many brew issues about mojave. 

EDIT: 
Also depending on your hardware setup, run more threads:

```
./brew.sh -j 3
```

## dEBRUYNE-1 | 2018-12-17T08:01:05+00:00
@CokeBear - Did you manage to resolve this particular issue? 

## dEBRUYNE-1 | 2018-12-27T15:09:08+00:00
Author has not responded and therefore I am going to close this issue. 

## dEBRUYNE-1 | 2018-12-27T15:09:12+00:00
+resolved

# Action History
- Created by: CokeBear666 | 2018-11-12T08:01:18+00:00
- Closed at: 2018-12-27T15:18:31+00:00
