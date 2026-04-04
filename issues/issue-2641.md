---
title: 'Deterministic/Reproducible builds '
source_url: https://github.com/monero-project/monero/issues/2641
author: cedricwalter
assignees: []
labels:
- proposal
created_at: '2017-10-12T14:06:57+00:00'
updated_at: '2019-06-28T06:49:38+00:00'
type: issue
status: closed
closed_at: '2019-06-28T06:49:38+00:00'
---

# Original Description
It seems that builds of Monero are non deterministic. Since this is a difficult goal and there is many way to achieve it, I want first to open the discussion here before opening a new PR

I've checked how Bitcoin and Tor is doing it, they use Gitian. I would recommend doing something similar... 

> Gitian is a thin wrapper around the Ubuntu virtualization tools written in a combination of Ruby and bash. It was originally developed by Bitcoin developers to ensure the build security and integrity of the Bitcoin software.
> Gitian uses Ubuntu's python-vmbuilder to create a qcow2 base image for an Ubuntu version and architecture combination and a set of git and tarball inputs that you specify in a 'descriptor', and then proceeds to run a shell script that you provide to build a component inside that controlled environment. This build process produces an output set that includes the compiled result and another "output descriptor" that captures the versions and hashes of all packages present on the machine during compilation.
> Gitian requires either Intel VT support (for qemu-kvm), or LXC support, and currently only supports launching Ubuntu build environments from Ubuntu itself.

## Bitcoin 
* https://github.com/bitcoin-core/docs/blob/master/gitian-building.md
* https://github.com/bitcoin/bitcoin/blob/master/doc/release-process.md#setup-and-perform-gitian-builds

## TorBrowser
* https://blog.torproject.org/deterministic-builds-part-two-technical-details
* first part https://blog.torproject.org/deterministic-builds-part-one-cyberwar-and-global-compromise

# Code base
I want through the source code and checked already that Non-determinism is not originating from the code base itself:
* File paths: direct or indirect embedding of non-deterministic source file paths in the final binary; for example use of C/C++ macro __FILE__ with the use of absolute file paths instead of relative file paths.
* File content references; for example use of C/C++ macro __LINE__, __COUNTER__.
Timestamps: for example, use of C/C++ macros __DATE__, __TIME__, __TIMESTAMP__, embedding the compilation time in the binary, etc. If the gyp define DONT_EMBED_BUILD_METADATA is set, these won't be embedded.
* Source control metadata: checkout revision number embedded in the binary. That fact the SCM reference changed doesn't mean the content changed and as such shouldn't affect the final binary, except extraneous metadata.

I'm open to any ideas or solutions, lets have a good discussion!

# Discussion History
## moneromooo-monero | 2017-10-12T14:24:16+00:00
Why is `__LINE__` non deterministic ?

## moneromooo-monero | 2017-10-12T17:40:01+00:00
Anyway, pigeons was looking at that, and will find his old notes about it so it can be done. Or at least some more work done towards it.

## cedricwalter | 2017-11-05T15:47:18+00:00
i could help if needed pigeons, he should just PM me

## cedricwalter | 2017-11-05T15:52:24+00:00
__LINE__ is not deterministic according to the chromium project (https://www.chromium.org/developers/testing/isolated-testing/deterministic-builds), all these macro are implemented differently on each platform (windows, linux, macos) and each compiler. Example for __FILE__ see http://blog.mindfab.net/2013/12/on-way-to-deterministic-binariy-gcc.html

it is a huge topic that will need more than one person to complete: it took debian lots of time but we should be able to profit from their experience https://wiki.debian.org/ReproducibleBuilds

## danrmiller | 2017-11-05T16:38:34+00:00
Thanks @cedricwalter are you on freenode?

## cedricwalter | 2017-11-05T19:21:40+00:00
@danrmiller not yet, but on which channel monero-dev?

## moneromooo-monero | 2017-11-06T00:20:34+00:00
The link doesn't give any info, but OK. We can cross that bridge if and when we end up needing to.

#monero-dev is a good channel for discussing this, yes.

## jonathancross | 2017-11-06T22:25:15+00:00
@TheCharlatan Also mentioned an interest in helping out with deterministic builds.

## sedited | 2017-11-06T22:40:28+00:00
The version control metadata should not be a problem, if the build is done similar to bitcoin's gitian. Gitian checks out the source tree for every build for every platform in the same way. 
The following is required for a clean Gitian build:

- Localized, statically compiled dependencies, similar to the depends system in bitcoin. Since depends uses autotools, it would probably be easier to use something like mxe: https://github.com/mxe/mxe , which has support for cmake already, but does not contain installer scripts for all the monero dependencies yet. 
- A script that is executed for every build iteration, using lxc with predefined configurations. 

## moneromooo-monero | 2017-11-19T12:36:48+00:00
For the record, I tried compiling simplewallet.cpp twice, and I got identical object files (after stripping debug info), so it's looking like we're in a good starting position :)

## dEBRUYNE-1 | 2018-01-08T12:38:52+00:00
+proposal

## anonimal | 2018-01-08T20:44:59+00:00
This issue should be moved to the [meta repo](https://github.com/monero-project/meta) as it will affect all applicable monero umbrella projects.

## sedited | 2018-02-04T09:48:29+00:00
Some updates: I managed to static compile a linux binary with all important dependencies linked from a modified version of bitcoin's depends system and an additional cmake toolchain file. It might be a good idea to break this into smaller pieces, since I cannot really estimate the time required to get it running on all platforms.  It would be nice to get a minimal set of requirements (e.g. which platforms should be supported, what manual interaction is acceptable) in order to open a pull request for this so more people can start working on it. 
Edit: 
To give a taste on how it works in Bitcoin:
A local script calls the gitian builder who creates a container in which the following is run:
- A depends build for every platform with `make HOST=PLATFORM_TRIPLET` , where platform triplet is for example `x86_64-apple-darwin`, or `x86_64-w64-mingw32`
- A configure script for the source code is then run with `CONFIG.SITE=/path/to/depends/PLATFORM_TRIPLET/share/config.site` prepended (in monero this would be something like `cmake -DCMAKE_TOOLCHAIN_FILE=/path/to/depends/toolchain_file`)
- This is run for every platform, creating deterministic binaries for each triplet
- Once built there are a few options for additional signing (detached sigs, no signing, check sigs)

## moneromooo-monero | 2018-03-07T15:04:10+00:00
Are you still working on this (or planning to) ?

## sedited | 2018-03-08T18:37:21+00:00
Still working on it. The cross compilation is a bit problematic, since the current build system expects vendored sources from external/ to be built. Not quite sure how to properly ship around this while keeping native compilation intact. This is why I will probably focus on getting the deterministic build done now on Linux, and think about the cross compilation again at a later stage. 

## moneromooo-monero | 2018-03-10T09:32:20+00:00
Getting there in steps is certainly fine. Thanks for doing this.

## sedited | 2018-03-18T16:37:27+00:00
I now opened #3430 to get depends on monero. This should at least take care of deterministically getting dependencies for all platforms. 

## garlicgambit | 2018-04-22T21:56:21+00:00
Any status updates on the progress? Need any support with something?

## sedited | 2018-04-22T22:17:45+00:00
The pr is still open, I will continue work on it once it is merged. If you want to move ahead, checkout my depends branch and try to setup a gitian descriptor, probably for a 64bit linux to start out, like here [in bitcoin](https://github.com/bitcoin/bitcoin/blob/master/contrib/gitian-descriptors/gitian-linux.yml).

## h01ger | 2018-08-27T07:36:47+00:00
actually, monero can be (re-)build in a deterministic way, if the same build path is used. see https://tests.reproducible-builds.org/monero (the sun icons on the left...) :-)

## sedited | 2018-09-10T19:32:22+00:00
@h01ger yes, it can and I have achieved reproducibility in the past on linux amd64. The hard thing is to make an easy as possible recipe for all architectures and target hosts (including mac and windows).

## h01ger | 2018-09-10T20:02:24+00:00
right. I guess it would be very nice to have some generic way/toolchain for that, maybe even a tool. and documentation...

## sedited | 2018-09-18T14:48:36+00:00
#3430 has been merged now. This adds a generic toolchain for some targets; mac, windows, linux 64 bit and arm 32 bit. Looking at getting a gitian build script for it going now.

## sedited | 2018-09-26T07:34:10+00:00
Now that the builds are more or less stable https://travis-ci.org/TheCharlatan/monero/builds/433563684 (hooray!) , I'll post a list of issues that still remain and need to be dealt with. Support/input on any of the items is welcome.

- [x]  hid and libusb are not statically linked into the end libraries yet, the dynamic libraries of libusb and hidapi are used. If static hidapi is used, the linker throws a bunch of errors, that libusb needs to be linked correctly
- [x] The linux binaries all still link the system's libc. When compiling on ubuntu 18 for example (which is my current preferred host OS) this means that the binary expects a new libc version on the machine it is running on. Since libc is not backwards compatible, this will result in non-portable binaries. Measures to ensure backwards compatibility should therefore be taken. Bitcoin has already dealt with those, so we can again build on their work: https://github.com/bitcoin/bitcoin/tree/master/src/compat . They also check the back compatibility of the used symbols at the end of every build.
- [x] A full gitian build script needs to be written. This should be similar to: https://github.com/bitcoin/bitcoin/blob/master/contrib/gitian-build.py . Docs on the gitian build process can be found here: https://github.com/bitcoin-core/docs/blob/master/gitian-building.md . 
- [x] Make protobuf cross compile properly when cross compiling to windows with mingw. Currently I get an error: https://github.com/protocolbuffers/protobuf/issues/5358 . Fixed in #4945
- [x] The macOS binaries currently only seem to run on macOS 10.11 (El Capitan). The goal is to make them compatible for all machines running 10.11 and above. Update: A build was now produced that runs on macOS 10.14 with xcode installed, need to verify that it runs without any developer extensions.

Optional, once the above is taken care of:
- [ ] Probably the debug symbols need to be split on Linux. This can be done by passing `--enable-deterministic-archives` for the archiver.
- [ ] Something like autotools' `make dist` for cmake might be useful as well to ensure that no git metadata leaks into the source during compile time. This should be taken care of though, when building in a seperate build director. Just something to keep in mind.

## sedited | 2018-10-03T12:01:42+00:00
Progress on the gitian build script (gitian-build.py) can be tracked here: https://github.com/TheCharlatan/monero/tree/gitian/contrib/gitian . if you want to participate, checkout that branch and submit improvements there. 

## sedited | 2018-10-08T14:17:23+00:00
I now opened #4526 to add a gitian build script to monero.

## sedited | 2018-12-02T17:26:50+00:00
The gitian builds are running stable now and seem to produced reproducible outputs. I also opened https://github.com/monero-project/unbound/pull/12 and https://github.com/monero-project/monero/pull/4929 to ensure that binaries compiled by gitian are portable across linux distributions.

## sedited | 2019-03-19T11:10:13+00:00
Now that docker support has been merged, building has become quite easy. Just run a docker daemon on ubuntu pass an additional `--docker` to the build script. 
Currently there is a compilation problem with macOS (though there is also a runtime problem when initialising openSSL that requires further inspection). 
Next to this, all windows builds and all linux builds safe `x86_64-linux-gnu` are reproducible. I'm investigating the source of non-determinism on the native 64 bit toolchain, my current suspects are some time calling functions and the JIT compilation of the mining code.

## sedited | 2019-06-12T09:37:03+00:00
Thanks to hyc's https://github.com/monero-project/monero/pull/5633 we now have full reproducibility for all compiled binaries. The pull request also seems to have fixed the crashes on macOS. I will close the issue once reproducible builds are used to build a monero release and at least two other participants achieve the same hashes.

## fluffypony | 2019-06-12T12:19:23+00:00
Awesome - thank you for your hard work! I’ll tag today or tomorrow, and then we can build:)

## dEBRUYNE-1 | 2019-06-12T12:38:07+00:00
@fluffypony - Please don't forget to merge #5633 and #5631 for the `release-v0.14` branch. 

## dEBRUYNE-1 | 2019-06-13T10:35:42+00:00
@fluffypony - Those PRs have been merged. When would you be able to create a "prep for v0.14.1" PR (similar to #5170) + tag?

## fluffypony | 2019-06-13T10:41:45+00:00
Already on it, will let you know when it’s done and then we can do some reproducible builds :)

## dEBRUYNE-1 | 2019-06-13T11:02:34+00:00
Thanks!

## sedited | 2019-06-28T01:56:54+00:00
+resolved

## dEBRUYNE-1 | 2019-06-28T06:42:32+00:00
+resolved

# Action History
- Created by: cedricwalter | 2017-10-12T14:06:57+00:00
- Closed at: 2019-06-28T06:49:38+00:00
