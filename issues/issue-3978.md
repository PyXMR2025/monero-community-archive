---
title: Monerod Building issue
source_url: https://github.com/monero-project/monero/issues/3978
author: WebCodiyapa
assignees: []
labels:
- invalid
created_at: '2018-06-10T03:51:26+00:00'
updated_at: '2018-06-18T20:32:58+00:00'
type: issue
status: closed
closed_at: '2018-06-18T20:32:58+00:00'
---

# Original Description
when I type "make" command to build moneroD, i got issue following:

CMake Error at /usr/share/cmake-2.8/Modules/FindBoost.cmake:1131 (message):
  Unable to find the requested Boost libraries.

  Boost version: 1.55.0

  Boost include path: /usr/include

  Detected version of Boost is too old.  Requested version was 1.58 (or
  newer).
Call Stack (most recent call first):
  CMakeLists.txt:778 (find_package)


CMake Error at CMakeLists.txt:56 (message):
  Could not find Boost libraries, please make sure you have installed
  Boost or libboost-all-dev (1.58) or the equivalent
Call Stack (most recent call first):
  CMakeLists.txt:782 (die)

# Discussion History
## moneroexamples | 2018-06-10T05:01:50+00:00
Monero requires at least boost version 1.58. What OS are you using? You could always try building newer boost yourself.

## WebCodiyapa | 2018-06-10T05:02:55+00:00
now i am using ubuntu


## moneroexamples | 2018-06-10T05:06:41+00:00
Guess its pre ubuntu-16.04 version? 16.04 has already boost in 1.58

## WebCodiyapa | 2018-06-10T05:07:38+00:00
but i can't install boost 1.58 on ubuntu
there is no package

## moneroexamples | 2018-06-10T05:08:58+00:00
Your ubuntu is too old.

## WebCodiyapa | 2018-06-10T05:09:46+00:00
how can i solve?

## moneroexamples | 2018-06-10T05:12:01+00:00
upgrade your ubuntu or compile boost 1.58 on your older version yourself. Either way these are not issues related to monero.

## WebCodiyapa | 2018-06-10T05:12:51+00:00
i should change server?

## homdx | 2018-06-12T10:50:01+00:00
Try manually update boost
```
tar -xvf boost_${BOOST_VERSION}.tar.bz2 
 && cd boost_${BOOST_VERSION} \
    && ./bootstrap.sh \
    && ./b2 
ENV BOOST_ROOT /usr/local/boost_${BOOST_VERSION}
```

## moneromooo-monero | 2018-06-18T20:30:06+00:00
As mentioned above, missing deps, see README.

+invalid

# Action History
- Created by: WebCodiyapa | 2018-06-10T03:51:26+00:00
- Closed at: 2018-06-18T20:32:58+00:00
