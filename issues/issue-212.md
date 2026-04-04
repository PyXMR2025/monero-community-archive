---
title: Use qt5 from brew for OSX
source_url: https://github.com/monero-project/monero-gui/issues/212
author: sammy007
assignees: []
labels:
- resolved
created_at: '2016-11-26T16:18:34+00:00'
updated_at: '2019-04-04T00:54:31+00:00'
type: issue
status: closed
closed_at: '2019-04-04T00:54:31+00:00'
---

# Original Description
Currently brew qt5 formula contains qt5 `5.7.0`. Can be installed with `brew install qt5`.
It's keg-only so bins are not in `PATH` by default. Can be linked with `brew link qt5 --force` but it seems a bit dirty. There is a hint in formula info:

```
Qt 5 conflicts Qt 4
Generally there are no consequences of this for you. If you build your
own software and it requires this formula, you'll need to add to your
build variables:

LDFLAGS:  -L/usr/local/opt/qt5/lib
CPPFLAGS: -I/usr/local/opt/qt5/include
PKG_CONFIG_PATH: /usr/local/opt/qt5/lib/pkgconfig
```

I believe it's way better to follow this instructions instead of installing Qt5 using official installer from qt.io.

# Discussion History
## sammy007 | 2016-11-26T19:24:38+00:00
Also, I added brew formula to my tap https://github.com/sammy007/homebrew-cryptonight

```
brew install monero-core --HEAD
brew linkapps monero-core
```

Feel free to add to readme.

## Jaqueeee | 2016-11-27T13:50:51+00:00
agree. Haven't tested myself but if qt5 from homebrew works it's easier to use that. 

## sammy007 | 2016-11-27T16:21:33+00:00
Also I found that `brew install boost --c++11` is not mandatory, you can use stock bottled boost `brew install boost` without compiling it.

## ghost | 2016-11-28T15:06:48+00:00
I can confirm that the `brew` Qt 5 build also works on my MacOS 10.11.6:

```
brew install qt5
brew link qt5 --force
```

## Jaqueeee | 2016-12-01T22:23:49+00:00
Deployment is broken on current homebrew qt. https://github.com/Homebrew/homebrew-core/issues/3219

Until that issue is solved upstream we should stick to official qt binaries. 


## sammy007 | 2016-12-01T22:29:57+00:00
Deployment? You don't need deployment if you compile it for yourself.

https://github.com/sammy007/homebrew-cryptonight#monero-core-qt-gui

## Jaqueeee | 2016-12-01T22:37:53+00:00
I think some users would expect it to run on machines without Qt installed. Even when they compile themselves. We could have brew method in instructions + a note that official binaries are needed for deployment. 

## sammy007 | 2016-12-01T22:38:49+00:00
They can expect everything, whole homebrew does not work this way.

## sammy007 | 2016-12-02T09:32:18+00:00
Just in case you don't completely understand my point, everything in homebrew is dynamically linked, it's like a gentoo, you can't redistribute binary bundles, only bottles, bottles requires all dependencies to be installed via brew also, can help to avoid compilation of formulas with common options. If someone want to do "deployments" (play coredev role) they must not use homebrew or perform extra steps to make that possible.

## Jaqueeee | 2016-12-04T16:45:45+00:00
@sammy007 Got it! You're welcome to PR that readme update ofc. 

## jonathancross | 2017-06-03T21:51:45+00:00
Thanks @sammy007, this is great that we have a way to install monero-core via Homebrew.

> You're welcome to PR that readme update ofc.

@Jaqueeee I'm happy to help out with this.  Is the idea to just add the brew tap/ install commands to the monero-core README?

While we are on the subject, would it make sense to create a monero-specific a fork under `monero-project/...` ?
I suspect users would prefer to add a tap from `monero-project/brew-tap` so they can be sure it is the correct tap.

Thoughts?

## sammy007 | 2017-06-04T16:56:55+00:00
If only it still works, can't check ATM.

## Jaqueeee | 2017-06-06T08:17:23+00:00
@jonathancross, yes, I think it would be best to add the brew taps to official github project before updating Readme. We need someone in the core team to help us with this. ping @fluffypony @luigi1111

Edit: official github project, not repo. 

## BigslimVdub | 2018-09-12T18:41:26+00:00
Hello? 
Brew installing qt 5.11 now but doesn’t like compiling on high Sierra. Have you updated brew? 
I added all 5 variables as brew suggested post install but still no dice. 

## selsta | 2019-04-04T00:47:10+00:00
The instructions recommend using brew.

+resolved

# Action History
- Created by: sammy007 | 2016-11-26T16:18:34+00:00
- Closed at: 2019-04-04T00:54:31+00:00
