---
title: 'Problem building on Trisquel: "ISO C++ forbids declaration of ‘Q_ENUM’..."'
source_url: https://github.com/monero-project/monero-gui/issues/819
author: Riiume
assignees: []
labels: []
created_at: '2017-08-14T06:43:33+00:00'
updated_at: '2017-10-12T07:03:27+00:00'
type: issue
status: closed
closed_at: '2017-10-12T07:03:27+00:00'
---

# Original Description
Hi all, after (seemingly) installing all the dependencies via apt-get, I get the following error when running ./build.sh:

`../src/libwalletqt/PendingTransaction.h:29:18: error: ISO C++ forbids declaration of ‘Q_ENUM’ with no type [-fpermissive]
     Q_ENUM(Status)`

My Linux distro information:
`Linux version 3.13.0-123-generic (pbuilder@devel.trisquel.info) (gcc version 4.8.4 (Ubuntu 4.8.4-2ubuntu1~14.04.3) ) #172+7.0trisquel2 SMP Thu Jun 29 20:03:33 UTC 2017
`

Here's the full output from ./build.sh
[BuildOutput.txt](https://github.com/monero-project/monero-core/files/1221415/BuildOutput.txt)

Here's a list of all libraries I have installed via apt-get:
[AptList.txt](https://github.com/monero-project/monero-core/files/1221416/AptList.txt)

In particular, have all of the QT5 packages installed, but it seems that in Trisquel the qml-module-* packages are named differently. Here are the qml related packages I have installed:

```
libqt5qml-graphicaleffects/belenos,now 5.2.1-1 amd64 [installed]
libqt5qml5/belenos-updates,now 5.2.1-3ubuntu15.1 amd64 [installed]
qtquick1-qml-plugins/belenos,now 5.2.1-1ubuntu1 amd64 [installed]
qtquick1-qmltooling-plugins/belenos,now 5.2.1-1ubuntu1 amd64 [installed]
```



# Discussion History
## Jaqueeee | 2017-08-14T08:45:09+00:00
hi @Riiume 
Was the original issue solved by updating boost? If not, my suggestion is upgrading Qt. I think you'll need 5.5 at lowest. But I'd recommend 5.8.

## Riiume | 2017-08-14T09:39:57+00:00
I have Qt5 and Boost5.8 (which is now working), but I'm still receiving the Qt errors. I will check if perhaps I have an older minor version of Qt5.

[BuildErrors.txt](https://github.com/monero-project/monero-core/files/1221801/BuildErrors.txt)
```
../src/libwalletqt/PendingTransaction.h:29:18: error: ISO C++ forbids declaration of ‘Q_ENUM’ with no type [-fpermissive]
     Q_ENUM(Status)
                  ^
../src/libwalletqt/PendingTransaction.h:29:18: error: expected ‘;’ at end of member declaration
../src/libwalletqt/PendingTransaction.h:36:20: error: ISO C++ forbids declaration of ‘Q_ENUM’ with no type [-fpermissive]
     Q_ENUM(Priority)
                    ^
(etc.)

```

## Jaqueeee | 2017-08-14T10:59:29+00:00
Ok. Qt5 could mean anything between 5.0 - 5.9. `qmake -v` should tell you which version you have installed. 

## Riiume | 2017-08-16T08:08:42+00:00
Okay, I installed Qt 5.9.1 and updated `/usr/lib/x86_64-linux-gnu/qtchooser/default.conf` to point to it, so now I have:

```
needle@Davinlu-Linvega:~/monero-core$ qmake -v
QMake version 3.1
Using Qt version 5.9.1 in /opt/Qt/5.9.1/gcc_64/lib
```

This seems to have fixed the Q_ENUM error.

However, now it's encountering a new error and I'm not sure what exactly to make of it:

```
/home/needle/monero-core/monero/lib/libwallet_merged.a(wallet2.cpp.o): In function `tools::wallet2::load(std::string const&, std::string const&)':
wallet2.cpp:(.text+0x193c1): undefined reference to `boost::filesystem::detail::copy_file(boost::filesystem::path const&, boost::filesystem::path const&, boost::filesystem::detail::copy_option, boost::system::error_code*)'
wallet2.cpp:(.text+0x19923): undefined reference to `boost::filesystem::detail::copy_file(boost::filesystem::path const&, boost::filesystem::path const&, boost::filesystem::detail::copy_option, boost::system::error_code*)'
collect2: error: ld returned 1 exit status
make: *** [release/bin/monero-wallet-gui] Error 1
```


This is odd because it's able to find Boost when it's compiling monero-cli and monerod, it's just during the GUI compilation phase that it's encountering this Boost-related error.

Full build.sh output: 
[BuildOutput20170816.txt](https://github.com/monero-project/monero-core/files/1227464/BuildOutput20170816.txt)


[This](https://stackoverflow.com/a/7972366) seems germane: "You have to link with `-lboost_filesystem -lboost_system`. Boost filesystem is not a header-only library; rather, it depends on compiled components." Which makes me think the issue is that I am using a manually installed version of boost that I had to reconfigure my environment variables to point to, rather than the apt-get version of Boost (which was too old of a version).

FYI here's how I configured my Boost environment variables:

```
export BOOST_ROOT=/usr/local; 
export BOOST_INCLUDEDIR=/usr/local/include/boost; 
export BOOST_LIBRARYDIR=/usr/local/lib
```

## Jaqueeee | 2017-08-16T09:46:24+00:00
Have you checked if those boost env vars are correct? i.e do you have the libboost_*.a files in `/usr/local/lib` and the *.hpp files in` /usr/local/include/boost`?

the `BOOST_INCLUDEDIR` seems wrong. Usually it is `/usr/local/include` (without the boost folder at the end) 

For the specific error above you should make sure that boost_filesystem is installed. Make sure you have` /usr/local/include/boost/filesystem.hpp` and `/usr/local/include/libboost_filesystem.a`


# Action History
- Created by: Riiume | 2017-08-14T06:43:33+00:00
- Closed at: 2017-10-12T07:03:27+00:00
