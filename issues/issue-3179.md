---
title: No successful Windows builds on master?
source_url: https://github.com/monero-project/monero/issues/3179
author: warmbeach
assignees: []
labels:
- invalid
created_at: '2018-01-24T21:32:35+00:00'
updated_at: '2018-03-07T11:56:38+00:00'
type: issue
status: closed
closed_at: '2018-03-07T11:56:38+00:00'
---

# Original Description
I am new here, thinking about contributing after mining for a bit.  I was surprised to look at the build status and see what looks like changes coming into master that don't compile on all platforms and Windows builds that have been failing since at least before January?  Am I looking in the wrong place? I hope I am because this is not confidence inspiring in software that will be handling what I hope to someday be lots of money.

I am looking at the build status at https://github.com/monero-project/monero, and then following that to https://build.getmonero.org/builders/monero-static-win64.

Are Windows builds currently compiling and passing tests, and if so, where can I see that?

Thanks

# Discussion History
## danrmiller | 2018-01-24T21:56:59+00:00
No, windows builds will not compile until #3155 is merged. You can make that change easily in your local branch to build for now. The master branch is the development HEAD and not where stable release tags are built from.

## mrtass | 2018-01-25T06:57:51+00:00
it worked but needed latest boost1.66 as well

## warmbeach | 2018-01-25T16:26:50+00:00
OK, I was confused because of this line in CONTRINUTING.md:

A patch MUST compile cleanly and pass project self-tests on at least the principle target platform.

Does this mean Windows (AMD64) is not a principle target platform?  What are defined as the principle target platform(s)?

It seems like changes have been taken in and pushed out despite the fact that code is not compiling and running tests on Windows and a few of the other platforms.  Is this an accurate statement or am I not seeing something more obvious here?

Thanks


## mrtass | 2018-01-25T16:31:54+00:00
im using windows 2012 64bit. 

## mrtass | 2018-01-26T12:02:22+00:00
Can anyone confirm [ #3155 ](https://github.com/monero-project/monero/pull/3155) will not break Ubuntu builds and other OS ?

## moneromooo-monero | 2018-01-26T12:30:41+00:00
I don't remember writing this, and I wrote this file. It got added by someone else I guess. I don't have a windows system, and I have no wish to get one, so if stuff doesn't build on windows, I'm fine fixing it after the fact, or even before if someone tells me so. Or if it's complex, a Windows coder can do it.

## danrmiller | 2018-01-26T15:25:27+00:00
@mrtass Yes #3155 did not break ubuntu or other builds. The include removed in that PR is no longer needed since a while and removing it was overlooked until now.

## warmbeach | 2018-01-26T16:32:50+00:00
I certainly understand the sentiment to want to work on the OS you like and are most comfortable with.  And in an open source project you should be free to contribute how and when you want.  

I guess what I am missing is why pull requests are accepted when they are known to fail on certain OS's?  For example, here is what the builds look like right now:

![image](https://user-images.githubusercontent.com/18182630/35449503-0df0894c-0272-11e8-8797-3be248355663.png)

It seems like you would want to reject any pull request that does not compile and pass tests until it has been fixed right?  With C++ going from C++11 to C++14 to C++17 and the fact that the compilers are completely different on the various operating systems the opportunity to write code that works fine on one platform but has a terrible security vulnerability on another is not low.  Maybe it does not matter because you have download numbers that show that 99% of the users of your wallets and miners are running Linux and not Android wallets or Windows machines?  By only fixing a defect right before you branch to release you don't get as many eyeballs on the code as may be necessary to find critical vulnerabilities.

Anyway, I will stop here, no reason for me to continue to badger people working hard on an open source project when I have not contributed a single line to it :)

Thanks



## moneromooo-monero | 2018-01-26T16:45:39+00:00
You're certainly welcome to point out when something is broken, and it will get fixed if it reasonably can.
I've started ignoring the build machine pings ages ago because it constantly pinged me for hours about irrelevant stuff, but theoretically it should work that way...

## moneromooo-monero | 2018-03-07T11:43:09+00:00
+invalid

# Action History
- Created by: warmbeach | 2018-01-24T21:32:35+00:00
- Closed at: 2018-03-07T11:56:38+00:00
