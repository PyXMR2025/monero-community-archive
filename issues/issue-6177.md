---
title: We should have (updated) Debian packages
source_url: https://github.com/monero-project/monero/issues/6177
author: fl4co
assignees: []
labels: []
created_at: '2019-11-24T17:16:53+00:00'
updated_at: '2025-12-19T17:05:05+00:00'
type: issue
status: closed
closed_at: '2025-12-19T17:05:05+00:00'
---

# Original Description
This is going to be a long post. Sorry about that.

Debian (and Ubuntu) are currently shipping v0.14.1.2. These packages won't work anymore in a few days. Unfortunately, my understanding is that they are not likely to be updated soon.

I think that making sure that Linux distributions actively get the latest Monero versions in their repositories is key to increase adoption. Linux servers are the ones that are more likely to be online 24/7, acting as remote nodes.

Currently, if you want to run a node in your Linux server, you have to go to the Monero website, grab the binaries and manually place them in /usr/local/bin or something similar. Then you have to run it under your user name.
This is not the Linux way. This is how you do things in Windows. A Linux server admin expects to find a package in his/her distribution's repository, install it with a single command and have it running with its systemd unit file and under its dedicated user account. He/she doesn't want to check Reddit or the Monero website to know that a new version is out. He/she expects to update the Monero package when the whole system is being updated.

Problem: given the Monero development cycle, it's impossible to have updated in Debian Stable.

This is not really an issue. In fact, having the last version in Sid/Testing only is totally fine because of Debian Backports. The Monero project should aim to have promptly updated packages in Sid and backported to Stable, because who runs a server is very likely to be running the Stable branch: https://backports.debian.org
I run a Tor relay in Debian Stable. I always have the latest version from the Backports. I think that Monero should do the same.
I never packaged software for Debian, I only have experience with Arch packaging which is arguably simpler, but it should be doable with minimal effort: I was able to successfully compile Monero and Monero GUI in Debian Stable, in a VM, only using dependencies from Stable repositories.
Of course, having an updated package in Debian means having an updated package in Ubuntu, and maybe in Tails.

Second best option: create an official repository. Again, Tor is doing it: https://2019.www.torproject.org/docs/debian.html.en. Plex Media Server is doing it. Just package the binaries and put the instructions on the website. A system admin will be able to activate a repository. It's not as convenient as having a package in the official repositories, bit it's still better than having to download the binaries and manually install them every single time. This solution could be temporarely adopted while an official package is prepared for inclusion in Sid/Backports.

If the project decides to prioritize this, these are the components that I think should be included in the package: the binaries (of course), a systemd unit (the official one from GitHub is fine) and a sysusers.d file that creates a dedicated monero user. By just doing that, you make the life easier for Linux server admins, which I guess are the backbone of the p2p network.

This post was about Debian because it's one of the most used server distributions. Of course, after a deb package is provided RPMs for CentOS should probably be the next target. FreeBSD already have reasonably updated ports.

With this post I hope to reach someone with Debian packaging experience and try to make packaging for Linux distros a number one concern for Monero developers. I can host the repository on my server if necessary. I really believe that this can boost adoption and the number of 24/7 online nodes.

# Discussion History
## thomasvaughan | 2019-11-24T22:28:49+00:00
@fl4co You're effectively suggesting that Monero do for Debian users what it currently does for Windows users (since Windows users can choose between an installer .exe and a plain zip archive).

Does the Debian packaging system accommodate packages constructed from pre-existing binaries? Since Monero now supports reproducible builds for Linux, a “packaged-from-binary” .deb download might make more sense than having a Debian-specific build, for reasons of security as well as packager-workload. (By way of analogy, the pkgsrc packaging system sometimes has both binary _and_ pkgsrc-compiled packages, *e.g.* compare [this libreoffice package](http://cdn.netbsd.org/pub/pkgsrc/current/pkgsrc/misc/libreoffice6-bin/README.html) with [this one](http://cdn.netbsd.org/pub/pkgsrc/current/pkgsrc/misc/libreoffice/README.html) — one has compiled Linux rpm files in its [distinfo](http://cdn.netbsd.org/pub/pkgsrc/current/pkgsrc/misc/libreoffice6-bin/distinfo), while the other has source tar.gz files it its [distinfo](http://cdn.netbsd.org/pub/pkgsrc/current/pkgsrc/misc/libreoffice/distinfo).)

## moneromooo-monero | 2019-11-24T22:49:27+00:00
I've made https://github.com/moneromooo-monero/monero-update which is meant to download/verify the current monero binaries. This program should stay current longer than 6 months, so is more suitable for inclusion in distros.

## fl4co | 2019-11-26T11:14:52+00:00
> @fl4co You're effectively suggesting that Monero do for Debian users what it currently does for Windows users (since Windows users can choose between an installer .exe and a plain zip archive).
> 
> Does the Debian packaging system accommodate packages constructed from pre-existing binaries? Since Monero now supports reproducible builds for Linux, a “packaged-from-binary” .deb download might make more sense than having a Debian-specific build, for reasons of security as well as packager-workload. (By way of analogy, the pkgsrc packaging system sometimes has both binary _and_ pkgsrc-compiled packages, _e.g._ compare [this libreoffice package](http://cdn.netbsd.org/pub/pkgsrc/current/pkgsrc/misc/libreoffice6-bin/README.html) with [this one](http://cdn.netbsd.org/pub/pkgsrc/current/pkgsrc/misc/libreoffice/README.html) — one has compiled Linux rpm files in its [distinfo](http://cdn.netbsd.org/pub/pkgsrc/current/pkgsrc/misc/libreoffice6-bin/distinfo), while the other has source tar.gz files it its [distinfo](http://cdn.netbsd.org/pub/pkgsrc/current/pkgsrc/misc/libreoffice/distinfo).)

You can certainly build packages from binaries, but to be included in the Debian archive the package must be built from source.
A .deb download from the website is an option, but then again it's better to setup a third party repo serving the package-from-binaries because packages are gpg signed and the package manager automatically checks the signature at install time. Of course, with the repo you also have updates without having to download anything again from the website (so better convenience and less security risks).
I don't think that reproducible build are viable in Debian because if I'm not mistaken that requires Ubuntu.
Regarding you're libreoffice example, yes, in Arch for example many packages are published to the AUR by the users in both source-and-compile and in binary form, but Debian is a lot more strict in this regard. You have to build from source to be included in the official repositories.


> I've made https://github.com/moneromooo-monero/monero-update which is meant to download/verify the current monero binaries. This program should stay current longer than 6 months, so is more suitable for inclusion in distros.

While this option is nice, I believe you still need to manually run it to check for updates (ok, you can Cron it, but its not "apt update && apt upgrade" at system level).

It reminds me of https://packages.debian.org/unstable/torbrowser-launcher, are you planning any distro packaging?

## Gingeropolous | 2019-11-26T11:28:50+00:00
@fl4co , you may want to comment on #2395 or see if you can help hack it out. 


## fl4co | 2019-11-26T11:49:46+00:00
I am currently testing a locally created APT repository that should work with any Debian and Ubuntu based distribution, serving .deb packages created from the officially released binaries (so checksums match). I can easily create packages for the ARMs too because there's no compiling involved.
Installation of the repository is like described by the examples in the OP: add a line to the sources.list file to include the repo and import the GPG signing key to the APT keyring. After that, you just `sudo apt install monero` and then you get updates anytime you update your system.

At this moment, I am packaging the CLI utilities for headless servers. At installation time:

- binaries go to /usr/bin;
- the default systemd file provided by the Monero project goes to /usr/lib/systemd/system and can easily enabled or disabled for boot time startup;
- A systemwide /etc/monero.conf configuration file is used as suggested by the systemd unit.
- A dedicated monero user without login rights is created by putting a file to /usr/lib/sysusers.d, leveraging systemd system user creation.
- LICENSE file goes to /usr/share/doc/monero. I'm not sure that's the correct way to do this in Debian though.

I also tested packaging the GUI. This way, a launcher for the application can be created and users don't have to start the GUI from the console, as I believe it's the case right now.

I'm of course open to suggestions. I am currently naming the GUI package `monero-gui`, but I'm not sure if the CLI package should be called `monero` or `monero-cli`.

In the next days, when all packages will be up, I'd like to open testing to others, if anyone is interested.

## moneromooo-monero | 2019-11-26T13:37:15+00:00
> It reminds me of https://packages.debian.org/unstable/torbrowser-launcher, are you planning any distro packaging?

Hopefully packagers for various distros decide to. This way the root of trust becomes the (likely very much monitored) distro's package repository. The only changes that'd be needed are trusted pubkeys so not much maintenance work is likely.


## jonassmedegaard | 2019-12-02T15:36:09+00:00
Would be helpful if not only binary builds were signed but also source release: That could be integrated into official Debian build routines.

## jonassmedegaard | 2019-12-02T15:39:09+00:00
Uhm, correction: Would be useful if release tarballs was signed at all - like it is done for RandomX (where it is done for binaries - better if done for sources too)

## moneromooo-monero | 2019-12-02T15:54:39+00:00
It's done in a kinda roundabout way: the SHA256 hash of the source tarball is contained in a file (https://getmonero.org/downloads/hashes.txt) which is GPG signed.

## moneromooo-monero | 2019-12-02T15:55:36+00:00
Oh, ignore me. The source one isn't in the list for some reason, though it is in the DNS set...

## jonassmedegaard | 2019-12-02T16:06:54+00:00
I have created #6210 to not hijack this issue with that related but separate issue about tarball signing.

## selsta | 2025-12-19T17:04:55+00:00
https://packages.debian.org/en/sid/monero

Appears to be mostly up to date.

# Action History
- Created by: fl4co | 2019-11-24T17:16:53+00:00
- Closed at: 2025-12-19T17:05:05+00:00
