---
title: Package Monero for Debian so it can eventually also be added to projects like
  Tails
source_url: https://github.com/monero-project/monero/issues/2395
author: scottAnselmo
assignees: []
labels:
- enhancement
created_at: '2017-09-03T20:46:42+00:00'
updated_at: '2022-09-30T18:06:45+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Currently Monero isn't packaged for Debian which is a [roadblock to Monero being adopted by Tails.](https://labs.riseup.net/code/issues/14390).

At time of writing [it looks like there are no packages being tested or otherwise being worked on](https://packages.debian.org/search?keywords=monero&searchon=names&suite=stable&section=all) for Debian.

# Discussion History
## dEBRUYNE-1 | 2017-09-03T20:49:20+00:00
+enhancement 

## privacycat | 2017-09-07T01:52:39+00:00
+enhancement
Agree. Monero is much more private and anonymous than Bitcoin. It's a no-brainer to package it for Debial so that ic could be adopted by Tails.

## anonimal | 2017-09-07T02:08:36+00:00
A debian package would be nice, we do have [snap](https://snapcraft.io/) ready to go though.

Note: re: tails, I don't see how running monero nodes *at large* over Tor would be a good thing for the monero network. This is why we have kovri. I'm assuming the demand is more for monero wallet + a remote node onion service?

## joeldejesus1 | 2017-09-07T06:27:07+00:00
If a debian package is created, is it possible to make sure that there is a monero-dev and libmonero package created as well?  This way, other people can use the c++ funtions in external programs.  I have just tried to use Monero as a library, but the examples only show how to work with static libs compiled with cmake.

## hyc | 2017-09-07T10:54:40+00:00
What exactly does "packaging for Debian" (or any other distro) actually mean? Do we have to actually provide scripts for their build system to build Monero binaries from source? Or are we simply providing the official getmonero.org binaries in a dpkg archive as opposed to a tar archive?

I assume the latter, because having large numbers of non-official binaries out there sounds like a security risk.

## joeldejesus1 | 2017-09-07T11:17:14+00:00
Speaking humbly, for debian packaging, you start with a source package.  Given a source package, someone would be able to type `apt-get source -b monero` and get several debian packages with compiled binaries as a result.  The /bin scripts would get put into a monero-cli kind of package, the libraries (-fPIC flag?) would get put into a libxmr0 package, and etcetera.  Having dynamically linked libraries would be nice to have available in a package.

## diederikdehaas | 2017-10-25T21:21:51+00:00
> What exactly does "packaging for Debian" (or any other distro) actually mean? Do we have to actually provide scripts for their build system to build Monero binaries from source? Or are we simply providing the official getmonero.org binaries in a dpkg archive as opposed to a tar archive?
> I assume the latter, because having large numbers of non-official binaries out there sounds like a security risk.

It is certainly **not** the latter. Debian will **never** distribute a binary that isn't build from source on their infrastructure.
It comes down to populating a `debian` directory which instructs the build system how to produce the package (so in a way the former). Then you'd have to file an `ITP` (Intention to Package) bug and find a sponsor (someone who's already a Debian Developer) to sponsor your package and when ready (s)he will upload it to the NEW queue after which an FTP master reviews the package (again) and if it meets the requirements accepts it into the archive.

Further reading:
- https://www.debian.org/doc/manuals/maint-guide/index.en.html
- https://wiki.debian.org/PackagingWithGit
- https://honk.sigxcpu.org/piki/projects/git-buildpackage/

But it's probably best to (first) contact [Debian Bitcoin Packaging Team](https://lists.alioth.debian.org/cgi-bin/mailman/listinfo/pkg-bitcoin-devel) if someone intends to do that.
(Yes, I know monero != bitcoin, but wrt packaging it may be useful to put it under 1 umbrella team)

## joeldejesus1 | 2017-10-26T16:05:56+00:00
If someone can add a configuration in Cmake to make dynamically linked libs (soname=x.y.z, etc), then I could set up the git-buildpackage items to make it easy to compile debian packages in one command (pbuilder).  You can see my work on [the picocoin debian package](https://github.com/favioflamingo/picocoin) as an example, though picocoin works with autotools as opposed to Cmake.  I am trying to get picocoin into Debian repos at the moment as well.

## dma | 2017-11-13T23:37:42+00:00
Hey all,

I've made a stab at packaging monerod and monero GUI wallet for @Subgraph OS. By default, all traffic exiting from Subgraph OS is over Tor, in case you weren't aware -- unless the user is using the sandboxed clearnet browser. So Monero users on SGOS would do so over Tor.

I just put downloadable packages on our website for testing, if all goes well, we'll drop them into our repo so users can apt-get install monero & they're good to go.  

Download links / instructions for testing before we drop them into our repo:

https://subgraph.com/sgos/documentation/monero/

The commits of the packaging metadata:

Monero:

https://github.com/subgraph/monero/commit/8ef7d55475780e6b844a5d2376bf6809a4de986e

Monero Core:

https://github.com/subgraph/monero-core/commit/b63ac3aad2ad06b43b56945dd0a3114a76904262


## dma | 2017-11-21T13:21:33+00:00
As the above was really a first try mostly to re-implement "build.sh" as debian build rules, I've removed the old repos, and we're now re-doing the packages to build with pbuilder (as we do our other packages). On-going work is here in the "debian" branch of the below forked repos:

https://github.com/subgraph/monero
https://github.com/subgraph/monero-gui

Monero packages have been added to our master packages repo, but it's not building in travis-ci yet:

https://github.com/subgraph/subgraph-debian-packages

I'll update this thread when we have a final packaging we like. Almost there..

## CameronRuggles | 2018-01-04T02:28:30+00:00
How is this progressing? Getting it added to TAILS is an exceedingly important project.
What currently needs to be done for Monero GUI to be added to the Debian packages? 

## dma | 2018-01-04T02:44:10+00:00
Oh, I packaged it in a nice way several weeks ago, but didn't want to release it or announce it until had binary reproducibility (who would want to use a wallet packaged by a third party that isn't?). 

I'd say I got almost there, but ran into some linker weirdness and then had to stop to work on something else. Also, not many people seemed to care and I had other priorities. 

I'd recommend Subgraph over Tails for storing and using XMR, but that's just me :)

I'll be back on it soon and return to this thread when I have achieved byte-for-byte matches on the final .debs.

If you want to try our packages in Tails, you're welcome to:

https://subgraph.com/sgos/documentation/monero/

Those date from when monero-gui was still monero-core, I'll build some new ones and update the page sometime in the next few days.

## scottAnselmo | 2018-01-04T04:41:44+00:00
Cool, keep us updated! I'll test it out on Tails and Subgraph when you put out the new builds and send some pizza/beer money your way from Tails or Subgraph. Will probably advertise it on the various Monero forums as well so you can get more people to test Monero (and Subgraph by proxy). Subgraph will probably be my live usb OS of choice when it comes out of alpha. Honored to have the president working on part of this issue! :)

Edit: Or I can hold off on announcing on any Monero forums you yourself don't announce on until you've got binary reproducibility (not sure if the next build would accomplish that?)
  

## dma | 2018-01-04T05:20:44+00:00
I'll return to it in the next week or so. I'll update this thread when I have a new version. I don't *think* I'm far from a fully reproducible build, which will be pretty awesome.

FWIW, Monero is the only Cryptocurrency project (besides BTC) that interests me at the moment because of its utility and active development/innovation.

## CameronRuggles | 2018-01-04T20:44:56+00:00
>Also, not many people seemed to care

Probably most people don't realize the impact it will have. Getting Monero
in TAILS would be a huge deal. Especially now with multisig and
subaddresses in the next release. It would have an obvious and big impact
on the DNMs, and over all adoption/usage of Monero. Plus, I'd love to just
have it easy to install on my Debian machines.



On Jan 3, 2018 10:20 PM, "David Mirza Ahmad" <notifications@github.com>
wrote:

> I'll return to it in the next week or so. I'll update this thread when I
> have a new version. I don't *think* I'm far from a fully reproducible
> build, which will be pretty awesome.
>
> FWIW, Monero is the only Cryptocurrency project (besides BTC) that
> interests me at the moment because of its utility and active
> development/innovation.
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/2395#issuecomment-355201463>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/ABTRGQhALEfqCi0MSQXyCPJLYVsusBn2ks5tHF-3gaJpZM4PLTFr>
> .
>


## dma | 2018-01-04T20:52:26+00:00
Yeah, obviously *I* realize that, it is implied by the earlier remark about the current tangible utility of XMR vs other "privacy" coins, most of which are quite problematic to varying degrees. 

Additionally, with the lack of a hardware wallet so far I would think exploit mitigation / system hardening in @subgraph OS would be something users want on hosts where they use a software wallet? But nobody replied here. We got no feedback at all - zero.

Anyways, as I said, I'll continue working on it and we'll make put it into our repo when our .deb can be reproducibly built. 

## scottAnselmo | 2018-01-04T21:26:02+00:00
Yep with the lack of a hardware wallet it would be awesome to use Monero on a more security focused OS! 

Apologies for the lack of testing feedback. 

- What in particular are you looking for feedback, anything beyond reporting issues per the existing doc? 
 - A simple 'instructions worked for me and were clear' from those who install it and system specs (e.g. CPU) so you know some amount of people tested it and what it works on? 
- Would feedback of the 'old' builds still be useful at this point to you or should I hold on asking other community members to test until the new builds? 
- What would be the best way to pass along feedback? Would you prefer comments in this thread or through Subgraph's 'Contact Us'? Open and close an issue for feedback (after official release) on https://github.com/subgraph/subgraph-debian-packages/issues?

I can pass along your requests in the open of the [community meeting in two days](https://github.com/monero-project/meta/issues/155) depending on what you would like. In that way it'd reach the more active members who engage in the meeting or read the logs that get posted, but the community at large likely wouldn't be aware of it and use it until you post your release announcement on r/Monero, etc.

## dma | 2018-01-04T21:30:42+00:00
I dunno, nothing elaborate, maybe just: "I tried it, didn't work", or "I tried it, works". 

Note that one doesn't need SGOS, any Debian derivative would do I think, including Tails.

Not grumbling or anything, I just juggle lots of priority things. This seemed important to some people, and was a longstanding dormant feature request, I picked it up & reported progress, but nobody seemed to care so I put it on backburner (also: holidays). I'll get back on it shortly!

## dEBRUYNE-1 | 2018-01-04T21:42:04+00:00
>I dunno, nothing elaborate, maybe just: "I tried it, didn't work", or "I tried it, works".

Note that this ticket is kind of "buried" and therefore not easily visible for potential testers. I'd recommend, once you finalize the new package(s), to put out a post on Reddit (r/monero) which calls for testers. I am sure you'll find a few interested people. 

  >This seemed important to some people, and was a longstanding dormant feature request,

It is :) Please don't let the current lack of testing let you think otherwise. 

## dma | 2018-01-04T21:44:05+00:00
Obviously, that's why I tweeted about it though to our 7000+ project followers and it was even retweeted by fluffypony. I am not sure even one person tried the .debs. Shrug.

## Gingeropolous | 2018-01-04T22:19:25+00:00
where do i find the .debs?

i dont tweet
  
edited to add - I found it, im a genius. Tried using the .deb on Ubuntu 16. 

And of course it looks like I need to have boost installed. 

```

[sudo] password for user: 
Selecting previously unselected package monero-core.
(Reading database ... 284426 files and directories currently installed.)
Preparing to unpack monero-core_0.11.1.0-1_amd64.deb ...
Unpacking monero-core (0.11.1.0-1) ...
dpkg: dependency problems prevent configuration of monero-core:
 monero-core depends on libboost-chrono1.62.0; however:
  Package libboost-chrono1.62.0 is not installed.
 monero-core depends on libboost-date-time1.62.0; however:
  Package libboost-date-time1.62.0 is not installed.
 monero-core depends on libboost-filesystem1.62.0; however:
  Package libboost-filesystem1.62.0 is not installed.
 monero-core depends on libboost-program-options1.62.0; however:
  Package libboost-program-options1.62.0 is not installed.
 monero-core depends on libboost-regex1.62.0; however:
  Package libboost-regex1.62.0 is not installed.
 monero-core depends on libboost-serialization1.62.0; however:
  Package libboost-serialization1.62.0 is not installed.
 monero-core depends on libboost-system1.62.0; however:
  Package libboost-system1.62.0 is not installed.
 monero-core depends on libboost-thread1.62.0; however:
  Package libboost-thread1.62.0 is not installed.
 monero-core depends on libqt5core5a (>= 5.7.0); however:
  Version of li
dpkg: error processing package monero-core (--install):
 dependency problems - leaving unconfigured
Errors were encountered while processing:
 monero-core
user@user-VirtualBox:~$ 

```

oh boost. 

edited again to add, it seems ubuntu is on boost 1.58 . 

## dma | 2018-01-04T22:46:16+00:00
Ah, I see. I should have clarified, Debian stretch derived distro. Thanks for the feedback. Try forcing an install maybe? If it works, we can relax the dependency.

Those debs are a bit out of date. I'm building new packages now & will put them online later. We can move this discussion to avoid adding a lot of noise in here.

## Gingeropolous | 2018-01-05T00:08:14+00:00
indeed, I tend to get vociferous. I'm usually hanging out on freenode #monero 

## dEBRUYNE-1 | 2018-01-05T19:43:37+00:00
@dma Can you confirm that you updated the binaries / packages here?

https://subgraph.com/sgos/documentation/monero/
  

## dma | 2018-01-06T01:15:44+00:00
I have now. I just uploaded some packages I built today.

## Coded-Dude | 2018-01-06T06:30:55+00:00
I tried building it for deb with the ubuntu dependencies, but it failed.  I opened an issue before seeing this.  you can close it if you like.....

## dma | 2018-01-21T01:04:31+00:00
Progress update: I've got monero and monero-gui debs building reproducibly! ~~Monero-gui next, and then we're done~~. Next steps are to add a .desktop file and icons and stuff.

**Monerod client**

Build 1 (AWS/Debian 9):

admin@ip-10-0-0-240:~/dev/subgraph-debian-packages$ sha256sum /tmp/build-area/monero_0.11.0.0-2_amd64.deb 
62ad9fb50bb7dc92f6298fccba6a4601a4c7d40fa175396115d1abd16ab90436  /tmp/build-area/monero_0.11.0.0-2_amd64.deb

Build 2 (dedicated box/Debian 9):

dma@spirit:~/dev/subgraph-debian-packages$ sha256sum /tmp/build-area/monero_0.11.0.0-2_amd64.deb 
62ad9fb50bb7dc92f6298fccba6a4601a4c7d40fa175396115d1abd16ab90436  /tmp/build-area/monero_0.11.0.0-2_amd64.deb

Build 3 (local workstation/Subgraph OS):

user@subgraph:~/dev/subgraph-debian-packages$ sha256sum /tmp/build-area/monero_0.11.0.0-2_amd64.deb 
62ad9fb50bb7dc92f6298fccba6a4601a4c7d40fa175396115d1abd16ab90436  /tmp/build-area/monero_0.11.0.0-2_amd64.deb

**Monero GUI wallet**

Build 1 (local workstation/Subgraph OS)

user@subgraph:~/dev/subgraph-debian-packages$ sha256sum /tmp/build-area/monero-gui_0.11.1.0-1_amd64.deb 
d5b0295d55f9951a6995e2ecc1516898799b22686ed81ca07b05b493175f2f66  /tmp/build-area/monero-gui_0.11.1.0-1_amd64.deb

Build 2 (AWS/Debian 9)

admin@ip-10-0-0-240:~/dev/subgraph-debian-packages$ sha256sum /tmp/build-area/monero-gui_0.11.1.0-1_amd64.deb 
d5b0295d55f9951a6995e2ecc1516898799b22686ed81ca07b05b493175f2f66  /tmp/build-area/monero-gui_0.11.1.0-1_amd64.deb

There some decisions to make for us, like: where does the blockchain data go? Do we start the daemon with systemd by default (feeling like no, as it can be started in GUI)? Appreciate thoughts on this. 

I'll look at fixing this for Ubuntu later.


## scottAnselmo | 2018-01-22T00:45:12+00:00
@fluffypony Can you provide some thoughts or ping one of the core 'stewards' about daemon and blockchain path suggestions?

@dma I've also paged the Monero dev channel as well to provide thoughts per your comment. Just FYI I haven't abandoned testing and I'm still trying to deal with Linux Mint dependencies issues as unfortunately the commands provided in the [GUI readme](https://github.com/monero-project/monero-gui) do not get the necessary 1.62 boost libraries as as mentioned latest packages for Ubuntu is 1.58, I'll see what efforts are being made with regards to packaging libboost 1.62:

`
sudo apt install build-essential cmake libboost-all-dev miniupnpc libunbound-dev graphviz doxygen libunwind8-dev pkg-config libssl-dev libzmq3-dev`
and
`sudo apt install qml-module-qt-labs-settings qml-module-qtgraphicaleffects`

> 
> Unpacking monero (0.11.0.0-1) ...
> dpkg: dependency problems prevent configuration of monero:
>  monero depends on libboost-chrono1.62.0; however:
>   Package libboost-chrono1.62.0 is not installed.
>  monero depends on libboost-date-time1.62.0; however:
>   Package libboost-date-time1.62.0 is not installed.
>  monero depends on libboost-filesystem1.62.0; however:
>   Package libboost-filesystem1.62.0 is not installed.
>  monero depends on libboost-program-options1.62.0; however:
>   Package libboost-program-options1.62.0 is not installed.
>  monero depends on libboost-regex1.62.0; however:
>   Package libboost-regex1.62.0 is not installed.
>  monero depends on libboost-serialization1.62.0; however:
>   Package libboost-serialization1.62.0 is not installed.
>  monero depends on libboost-system1.62.0; however:
>   Package libboost-system1.62.0 is not installed.
>  monero depends on libboost-thread1.62.0; however:
>   Package libboost-thread1.62.0 is not installed.
>  monero depends on libssl1.1 (>= 1.1.0); however:
>   Package libssl1.1 is not installed.

@Gingeropolous Can you provide any suggestions as to getting the needed libboost dependencies sorted out? Haven't really dealt with boost before and have tried sifting through various forums, but struggled to come up with a solution. I imagine if you got it to work on Ubuntu by now the same solution should work for my Mint box.


## diederikdehaas | 2018-01-22T03:46:51+00:00
On maandag 22 januari 2018 01:45:30 CET Scott Anecito wrote:
> libssl-dev

Check whether libssl-dev points to version 1.0 or 1.1 of libssl; that could be 
relevant.
You can also try to use 'aptitude' instead of 'apt' as its dependency resolver 
is more powerful and therefor may find a solution to your dependency issue.



## scottAnselmo | 2018-01-22T04:33:28+00:00
Tried aptitude, but latest package in Synaptic package manager for libssl is 1.0.2g-1ubuntu4.10

> libboost-all-dev is already installed at the requested version (1.58.0.1ubuntu1)
> libboost-all-dev is already installed at the requested version (1.58.0.1ubuntu1)
> No packages will be installed, upgraded, or removed.
> 0 packages upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
> Need to get 0 B of archives. After unpacking 0 B will be used.
>                                          
> libssl-dev is already installed at the requested version (1.0.2g-1ubuntu4.10)
> libssl-dev is already installed at the requested version (1.0.2g-1ubuntu4.10)
> No packages will be installed, upgraded, or removed.
> 0 packages upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
> Need to get 0 B of archives. After unpacking 0 B will be used.

Currently exploring using the[ libboost 1.62 package from Debian](https://packages.debian.org/stretch/amd64/libboost-all-dev/download) and getting past the Error:Dependency is not satisfiable: libboost-fiber-dev issue

Edit: @dma Stupid question, but what directory is the Monero package expecting libboost in? I've tried bootstrapping libboost into /usr/ and /usr/local

## diederikdehaas | 2018-01-22T05:42:49+00:00
On maandag 22 januari 2018 05:33:37 CET Scott Anecito wrote:
> Tried aptitude, but latest package in Synaptic package manager for libssl is
> 1.0.2g-1ubuntu4.10

On my Debian Stable system, I have both libssl-dev (for ssl 1.1) and 
libssl1.0-dev (for ssl 1.0). They're not co-installable though.
I don't know what/how Mint/Ubuntu has done, but there may be a similar 
situation.


## hyc | 2018-01-28T17:16:20+00:00
> There some decisions to make for us, like: where does the blockchain data go? Do we start the daemon with systemd by default (feeling like no, as it can be started in GUI)? Appreciate thoughts on this.

If you start it from systemd, it should probably have its own uid and a home directory in /var/spool/xxx or something, for storing the blockchain. But it's a good point that it can be started in the GUI. Might be best to leave it at that, thus running under the user's uid and in the user's home directory.

## danrmiller | 2018-01-28T17:24:40+00:00
@dma Can you point me to your debian control files like the buildinfo file?

## radfish | 2018-01-28T17:27:20+00:00
Thanks for packaging!

You can take a look at how it's done in the Arch package:
https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=monero-git
https://aur.archlinux.org/cgit/aur.git/tree/monero.install?h=monero-git

Blockchain data dir is /var/lib/monero which is also the home dir of a dedicated user with that name. It is best for security to have a dedicated user for security isolation purpose, since monerod is internet-facing. Config file is in /etc/monero.conf. Log could go into syslog or /var/log/monero.

Systemd service  exists in the repo. It should be installed, but not sarted automatically, although I think some packages on Debian do start services automatically (not a fan at all, since user should have a chance to edit the config before starting the service).

This setup works fine with the GUI wallet running under the normal user. See monero-wallet-qt package: https://aur.archlinux.org/packages/monero-wallet-qt

I would vote against starting the daemon from the GUI wallet. Having it as a standard systemd service is simple and least surprize to users.


## dma | 2018-01-29T14:50:12+00:00
@radfish @hyc I generally agree with all you're saying, and that's how I did it.

I have a reproducibly built .deb now with .desktop and icons. 

Going to make an apparmor policy for monerod and then call it done as we aren't sandboxing the daemon in Subgraph OS. I believe the packages, which build in Debian 9, should work in Tails. Will update this ticket later on this (cc @danrmiller).

## CameronRuggles | 2018-02-12T13:49:27+00:00
Any updates? Anything I can do to help as a fairly non-technical person?

Super excited for this. 

## agx | 2018-02-21T09:32:53+00:00
I have filed a RFP (Request for packaging) in the Debian bug tracker (https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=890974). 

## dma | 2018-02-21T12:03:45+00:00
Hey all, sorry for lack of updates, it's basically done for Subgraph OS. I'm happy with the packages. They build reproducibly, and I added icons, the desktop file, apparmor profile for monerod.. I'll update my last changes to our repo and then we'll write a blog post about it today or tomorrow. They can be built in Debian, though I imagine a maintainer might want to do some things differently.

## h01ger | 2018-02-21T15:11:19+00:00
@dma: where are your source packages? https://subgraph.com/sgos/documentation/monero/ only links to binary packages and both https://github.com/subgraph/monero and https://github.com/subgraph/monero-gui lack a debian/ subdirectory (needed to build source packages)

## dma | 2018-02-21T15:18:30+00:00
@h01ger Check the debian branch of both repositories. That documentation page is out of date, need to update it. I have some commits to the debian branches I haven't pushed yet. Just haven't had time to close this out.

## h01ger | 2018-02-21T15:25:47+00:00
 @dma: thanks for the quick reply! and TBH, I was stupid/tired, I looked for branches with "git branch" instead of "git branch -av"... looking forward to your unpushed changes too!


## dma | 2018-02-21T15:28:45+00:00
@h01ger I'm happy with it. I hope Debian/Tails can benefit from it without much extra work. Our build environment pulls packages from the subgraph repo, but there are no subgraph dependencies for building monero and monero-gui (obviously), so those can be removed for a pristine Debian pbuilder build that's reproducible. I'll push the apparmor policy I made for monerod and whatever else is still not online & then I think we're (I'm) done..

## h01ger | 2018-02-21T15:31:49+00:00
@dma: the debian packaging looks very nice, kudos! (and many thanks too)

I just saw one instance of subgraphos specific changes, the systemd service requires the subgraph_metaproxy.service - so now I wonder how you would deal if I'd uploaded that package to Debian proper, without that requirement...

(and do take your time, I wont really do something within the next 24h anyway. but then, very probably!)

## h01ger | 2018-02-21T15:33:23+00:00
only monero/external/ seems a bit scary...

## dma | 2018-02-21T15:58:23+00:00
@h01ger yeah, right, in the systemd file is a subgraph dependency, which you won't want (I may even remove that - I just wanted to make sure monerod doesn't start connecting to the Internet until transparent tor-ification is up), forgot about that. If Debian packages Monero/Monero GUI, I imagine we'll drop ours and use Debian's. If we need to overload the systemd unit file, we can do that separately.

## scottAnselmo | 2018-04-23T21:41:02+00:00
Hey folks, wishing to follow up on the great work you're doing packaging Monero for Debian. Has Monero v0.12 been packaged for Debian by chance given the documentation references v0.11 still? It's not much unfortunately, but I did send some Moneroj to SubGraph as thanks for prior work.

## scottAnselmo | 2018-06-09T21:22:47+00:00
Just generic status update: Conversation earlier today in IRC on #monero-dev with @moneromooo-monero ... "Apparenly the person who did a debian package [ @dma ] is waiting for reproducible builds, which are on the way,."

Glad to see progress is still being made for users to easily have Monero on security/privacy focused OSes like Subgraph and Tails! Thanks for your continued work!

## jonassmedegaard | 2018-06-20T19:10:12+00:00
Monero entered Debian unstable earlier today. Health of the packaging can be monitored at <https://tracker.debian.org/pkg/monero>

## spth | 2018-08-24T21:15:41+00:00
Any news on progress getting a GUI into Debian?

Philipp


## scottAnselmo | 2019-01-08T18:13:47+00:00
@spth The best point of contact is probably going to be @rehrar as he is the point person between Monero and Purism's for the librem5 integration efforts. If you're unfamiliar with librem5 it's basically a phone that will run PureOS (Debian based) by default and is launching April 2019, so there is interest from those outside the Monero community in contributing to this issue.. It looks like currently we now have a test package for Debian unstable/sid: https://packages.debian.org/search?keywords=monero

I'll ask around if anyone knows of any taskboards, etc to better track how close we are to a non-test package.

## jonassmedegaard | 2019-01-08T19:14:29+00:00
Quoting Scott Anecito (2019-01-08 19:14:04)
> @spth The best point of contact is probably going to be @rehrar as he is the point person between Monero and Purism's for the librem5 integration efforts. If you're unfamiliar with librem5 it's basically a phone that will run PureOS (Debian based) by default and is launching April 2019, so there is interest from those outside the Monero community in contributing to this issue.. It looks like currently we now have a test package for Debian unstable/sid: https://packages.debian.org/search?keywords=monero
> 
> I'll ask around if anyone knows of any taskboards, etc to better track how close we are to a non-test package.

I guess you want this: https://tracker.debian.org/pkg/monero

Also, I maintain the monero package officially in debian, and I work for 
Purism with one of my tasks being point person towards Monero.

Feel free to reach out to me at either jonas.smedegaard@puri.sm or 
dr@jones.dk as needed :-)

 - Jonas

-- 
 * Jonas Smedegaard - idealist & Internet-arkitekt
 * Tlf.: +45 40843136  Website: http://dr.jones.dk/

 [x] quote me freely  [ ] ask before reusing  [ ] keep private


## jonassmedegaard | 2019-01-08T19:16:38+00:00
> Any news on progress getting a GUI into Debian?

No progress on packaging the GUI part of Monero yet, unfortunately.

## moneromooo-monero | 2019-01-08T19:29:14+00:00
If purism needs changes/fixes to monero itself to make their lives easier, feel free to ask, I'll be happy to help (as long as the changes aren't too idiosyncratic).

## who-biz | 2019-02-13T16:48:13+00:00
I began packaging the GUI for Debian.  Will definitely take some more work to get the fine-tuning of everything in order... but the repository at https://github.com/who-biz/monero-gui/tree/debian is a start.  It does build from source cleanly with `dpkg-buildpackage`. (You will need to run that command as root to package -- do so from within a chroot, or a secure environment)

All of the relevant files are contained in the `debian` directory. While it is still a WIP, it builds a functioning .deb package for release v0.13.0.4.

Anyone can feel free to contribute via PR or just appropriate what is there for your own use, as you see fit.  Just trying to get the ball rolling on this, so copy-and-pasting to a different repo, or whatever anybody may want to do, is completely okay by me. 

Edit: `debian` directory has been updated to now function fully with freedesktop menus and launchers. 

## adrelanos | 2019-08-11T13:13:03+00:00
"simply put the pre-build Monero binaries into a deb package": [[IDEA] [PROPOSAL] Monero Debian (deb) packages / Debian package repository deb.getmonero.org (I can do)](https://www.reddit.com/r/Monero/comments/cowjun/idea_proposal_monero_debian_deb_packages_debian/)


## OrvilleRed | 2019-09-29T08:01:59+00:00
The [excuses](https://qa.debian.org/excuses.php?package=monero) for this .deb say it's stuck because we need a clean arm64 build. Bug [939311](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=939311) is open for this problem.

Is anybody actively working that Bug? If not, I'll get an arm64 compute from a random cloud service and try building, I guess...

## bill-mcgonigle | 2020-02-29T03:08:21+00:00
> Is anybody actively working that Bug? If not, I'll get an arm64 compute from a random cloud service and try building, I guess...

@denisgoddard - it looks like [the blocker bug](https://sourceware.org/bugzilla/show_bug.cgi?id=25210) is fixed as of last month; are you on this?


## scottAnselmo | 2020-03-02T17:43:38+00:00
There is now a CCS that would address the heart of this issue of making it easier for users to install the Monero GUI on Debian related distros courtesy of Whonix folk and infrastructure. If people are still interested in taking the path of getting the package onto getmonero.org or Debian infrastructure that would be cool too.

If so, let me know so I can update this issue's scope to package being hosted on getmonero and/or Debian so work can still be tracked, etc.

https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/130?commit_id=b188c28babbaa21f12a3f4993d8ed046b675fcaf

## bill-mcgonigle | 2020-08-14T14:39:51+00:00
OK, sweet, Patrick has done the packaging:
https://gitlab.com/whonix/monero-gui

Not sure if it meets all of Debian's requirements but it's at least that much closer.

## jonassmedegaard | 2020-08-14T18:33:10+00:00
Quoting Bill McGonigle (2020-08-14 16:40:06)
> OK, sweet, Patrick has done the packaging:
> https://gitlab.com/whonix/monero-gui
> 
> Not sure if it meets all of Debian's requirements but it's at least that much closer.

It certainly does not meet Debian's requirements to put the pre-build 
Monero binaries into a deb package - but if acceptable to some then good 
for them!


 - Jonas

-- 
 * Jonas Smedegaard - idealist & Internet-arkitekt
 * Tlf.: +45 40843136  Website: http://dr.jones.dk/

 [x] quote me freely  [ ] ask before reusing  [ ] keep private

## erciccione | 2020-08-15T14:53:17+00:00
Posting this here since it's related:

I recently opened an issue on Tails's repository asking to add Monero. That's not possible at the moment, but they give some good suggestions about getting the GUI on Debian: https://gitlab.tails.boum.org/tails/tails/-/issues/17823

## adrelanos | 2020-08-19T09:22:34+00:00
> OK, sweet, Patrick has done the packaging:
> https://gitlab.com/whonix/monero-gui
> 
> Not sure if it meets all of Debian's requirements but it's at least that much closer.

No, this was explicitly excluded. Quote [CCS proposal](https://ccs.getmonero.org/proposals/adrelanos-debian-package.html):

> `packages.debian.org` is out of scope since Debian does not upgrade often enough to keep up with Monero fork cycle and for other reasons as well.

https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/130

## erciccione | 2021-01-19T13:17:59+00:00
Tails' devs posted a list of requirements needed in order to support Monero on tails: https://gitlab.tails.boum.org/tails/tails/-/issues/17823#note_163991

It's fundamental that the package maintained by the 'Debian Cryptocoin Team' (https://tracker.debian.org/pkg/monero) is fixed and updated to the latest version before Debian Bullseye's soft freeze (February 12th. In less than a month). Recently, an unfixed bug caused the monero package to be removed from 'testing' and that's problematic for a future addition on Tails (and not only that, please see the gitlab issue i linked to at the beginning of this post).

So, to reiterate, the 'monero' package needs to be fixed and updated ASAP. If anybody has contacts with the developers who used to work on this, please contact them and point them to this issue.

## erciccione | 2021-01-30T10:48:33+00:00
The issue i mentioned above is resolved. The latest Monero release is now available on Debian testing.

For details see https://gitlab.tails.boum.org/tails/tails/-/issues/17823#note_164543

## DeeDeeRanged | 2022-09-30T18:06:44+00:00
Any chance to get the monero package updated to the latest version for Debian testing/sid?

# Action History
- Created by: scottAnselmo | 2017-09-03T20:46:42+00:00
