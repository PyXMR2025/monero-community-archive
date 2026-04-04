---
title: Could we update the ARM build instructions, please?
source_url: https://github.com/monero-project/monero-gui/issues/3642
author: bonevays
assignees: []
labels: []
created_at: '2021-07-25T23:32:22+00:00'
updated_at: '2022-01-24T20:19:30+00:00'
type: issue
status: closed
closed_at: '2022-01-24T20:19:30+00:00'
---

# Original Description
I'm on the latest Ubuntu and first tried the "whonix repo method" to get the binary, even though I see the ARM parameter somewhere, it only managed to get me x86 binaries itself.

I also followed the standard Ubuntu recipe with make release, and it broke with the -maes unknown error, which has already been discussed in the RandomX context a long time ago, if not in this repo as well. As -maes simply should be removed for ARM, I looked into the Makefile only to find a release-linux-armv8 target. So I guessed that should do the job, except that it does not behave like make release, has some hardcoded dependency to ../.. for whatever reason. I did try the standard cmake recipe but it breaks almost immediately. 

Finally, I created bin/arm , copied the Makefile there, and now the stars seem to have aligned and the project gets built correctly in monero-gui/bin/arm/bin . Perhaps someone more competent than me knows what to fix here or there to make the build more streamlined.

# Discussion History
## selsta | 2021-07-26T00:27:49+00:00
Did you try `make release-linux-armv8`?

## bonevays | 2021-07-26T11:45:52+00:00
> Did you try `make release-linux-armv8`?

yes, like I said it needs a workaround because it has hardcoded ../.. and that directory in my case is /home, and of course no building can take place there.

## selsta | 2021-08-08T03:08:11+00:00
It's not clear to me what you mean with `../..` hardcoded. I need logs.

## Dendrocalamus64 | 2021-08-31T19:28:50+00:00
I can pick it up here since I'm now at that point.  monero_gui/Makefile has,
>release:
 >       mkdir -p $(builddir)/release && cd $(builddir)/release && cmake -D DEV_MODE=$(or ${DEV_MODE},OFF) -DMANUAL_SUBMODULES=${MANUAL_SUBMODULES} -D ARCH="x86-64" -D CMAKE_BUILD_TYPE=Release $(topdir) && $(MAKE)
>
>release-linux-armv8:
>       mkdir -p $(builddir)/release
>        cd $(builddir)/release
>        cmake -D DEV_MODE=$(or ${DEV_MODE},OFF) -D ARCH="armv8-a" -D BUILD_64=ON -D CMAKE_BUILD_TYPE=Release -D BUILD_TAG="linux-armv8" $(topdir) && $(MAKE)

So it's using `$(topdir)` in either case, and that's set to `../..` earlier in the Makefile.
>topdir := ../..

Then the build fails with,
>cmake -D DEV_MODE=OFF -D ARCH="armv8-a" -D BUILD_64=ON -D CMAKE_BUILD_TYPE=Release -D BUILD_TAG="linux-armv8" ../.. && make
>CMake Error: The source directory "/home/rock/build-area/monero-gui" does not appear to contain CMakeLists.txt.
>Specify --help for usage, or press the help button on the CMake GUI.
>make: *** [Makefile:53: release-linux-armv8] Error 1
>==> ERROR: A failure occurred in build().
>    Aborting...

Changing it to `topdir:= .` allows it to start building.


## Dendrocalamus64 | 2021-08-31T19:33:23+00:00
I think it's because the commands for target `release-linux-armv8:` are split into three lines for readability, while target `release:` is all on one line with `&&`s.  So it's not starting in the anticipated directory.  The 'workaround' causes other problems like clobbering the Makefile with a CMake-generated Makefile.

## Dendrocalamus64 | 2021-08-31T19:43:21+00:00
Yeah, it looks like the proper fix is just to put all the commands for `release-linux-armv8:` onto one line.
>release-linux-armv8:
        mkdir -p $(builddir)/release && cd $(builddir)/release && cmake -D DEV_MODE=$(or ${DEV_MODE},OFF) -D ARCH="armv8-a" -D BUILD_64=ON -D CMAKE_BUILD_TYPE=Release -
D BUILD_TAG="linux-armv8" $(topdir) && $(MAKE)

## selsta | 2021-08-31T19:52:06+00:00
Thanks @Dendrocalamus64 #3680

# Action History
- Created by: bonevays | 2021-07-25T23:32:22+00:00
- Closed at: 2022-01-24T20:19:30+00:00
