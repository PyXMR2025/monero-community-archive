---
title: '[Packaging] Provide official flatpak package of "monero-gui" on FlatHub'
source_url: https://github.com/monero-project/monero-gui/issues/2806
author: Nokia808
assignees: []
labels: []
created_at: '2020-03-13T20:07:58+00:00'
updated_at: '2022-04-23T16:56:50+00:00'
type: issue
status: closed
closed_at: '2022-04-23T16:56:24+00:00'
---

# Original Description
Hi.
Dears why you do not make your official GUI wallet available officially (packaged by you) as flatpak package on FlatHub ?
If you provide it as flatpak on FlatHub, then it will be available in secure trusted way for nearly all Linux users, because flatpak is a universal Linux package .....

There is someone who tried this but failed .... So it is better to be packaged by you (the official developer of monero-gui wallet).

Best.

# Discussion History
## selsta | 2020-03-14T19:21:31+00:00
Contributors who maintain a flatpak package are welcome.

## ralyodio | 2020-04-15T05:36:11+00:00
This would be great.

## Nokia808 | 2020-04-15T06:35:01+00:00
I'm already asked "Verge" project for adding their wallets to FlatHub & they responded positively & added their full node wallet - see:
https://github.com/vergecurrency/verge/issues/1028
https://github.com/flathub/flathub/pull/1420
https://github.com/flathub/org.vergecurrency.verge-qt
https://www.flathub.org/apps/details/org.vergecurrency.verge-qt
& as you read, they will add their light wallet in near future ....

Also, I asked BEAM project, & they respond positively, but they suffer from problem that they are currently working to solve before adding their wallet - see:
https://github.com/BeamMW/beam/issues/854

I wish that this comment from me will encourage the official developers of monero-gui to package & ship their wallet officially as flatpak package to be available on FlatHub

Best. 

## Nokia808 | 2020-05-28T15:46:42+00:00
Today Electrum dash wallet added to FlatHub:
https://github.com/flathub/flathub/pull/1536
https://github.com/flathub/org.dash.electrum.electrum_dash

And before that groestlcoin wallet (both full node & electrum) joined FlatHub:
https://github.com/flathub/org.groestlcoin.groestlcoin-qt
https://github.com/flathub/org.groestlcoin.electrum-grs

Hopping we will see monero-gui on FlatHub ....

## selsta | 2020-05-28T17:05:11+00:00
It’s easy for Bitcoin Core / Electrum clones to add Flatpak support, it’s simply copy paste. Monero-GUI is its own codebase, it is significantly more work for us. We are currently working on cmake support, then we might be able to look into it.

## Nokia808 | 2020-05-28T19:57:30+00:00
@selsta 
But flatpak is UNIVERSAL Linux package so that it will cover almost all Linux distros & users. 

Why you do not discontinue the current portable binaries that existing on your download page & concentrate your efforts on flatpak only? This will be better to users. Security by default, sandbox by default + automatic update in convenient easy update mechanism & from trusted repository (FlatHub) when all flatpak packages are signed by OpenPGP & open source project are built as reproducible flatpak packages ...

## q7nm | 2021-01-08T10:13:52+00:00
Can I add a flatpak package? I already managed to write a manifest to build it

## scottAnselmo | 2021-01-27T09:52:36+00:00
@BigmenPixel0 There is nothing technically stopping you from submitting the manifest to Flathub. I'm not a a part of the Monero 'Core' team, but I'd highly recommend you do so as I know this is something that would definitely improve adoption.

Flathub submission guide can be found here: https://github.com/flathub/flathub/wiki/App-Submission

## Nokia808 | 2021-01-30T18:34:51+00:00
@BigmenPixel0 
You can start PR to FlatHub, & during process they will ask for joining official developers to join repository. Here your role will come to invite them. Just one of them if accept your invitation this will give some degree of officialism to the flatpak package. Then after, when they have more time & when they see your package working, they will take the hand from you gradually ......... Just start the 1st step.  

## scottAnselmo | 2021-02-20T19:20:25+00:00
Was going to do the PR this weekend using BigmenPixel0's manifest and attribute them given it's been three weeks, but it looks like they put in a PR yesterday to FlatHub! Thanks! https://github.com/flathub/flathub/pull/2124

## Nokia808 | 2021-02-20T19:42:29+00:00
@sanecito 
Yes ! Thank you to him ! But it seem that threre are problems:
1) it seem that the flatpak will not be official from developers of Monero since @BigmenPixel0 dictated in the RP that he "can not contact developers" !!
2) also, it seem that @BigmenPixel0 suffer from difficulties & need help to assist him in this PR. Unfortunately I can not help ...... If you @sanecito can help him by going his PR, then this may be great push forward. 

But the question remain: why he can not contact Monero developers & they all are in this repository ?! It will be much batter if the flatpak package supported officially by developers of Monero themselves & if they help @BigmenPixel0 in his struggle to complete this PR & reach it to be approved, & assist him also in maintaining this flatpak ...... Hopping they will join him & take part in this PR ......

## scottAnselmo | 2021-02-20T20:01:54+00:00
#monero-dev has been reached out just now to see if someone like @moneromooo-monero can voice support of the PR on the PR, so that should address point 1 hopefully. I'll try messing around tomorrow with building using the PR manifest on my system to see if I can replicate the buildbot issues for x86/x64, but hopefully given BigmenPixel0 was able to work out a manifest, they'll be able to make quick work themselves.

## erciccione | 2021-02-21T09:32:49+00:00
Point 1 is moot. Monero is not a company with a hierarchic structure. You don't need anybody's permission or approval to do anything. There are no "official developers". The code is open source and can be distributed by anyone.

## Nokia808 | 2021-02-21T11:17:22+00:00
@erciccione 
Dear I know Monero is not a company & being open source project & know what open source project means.

All point is that I have the following idea (kindly, correct to me if wrong): the founder(s) of project is(are) the USUALLY the best regarding making this project ..... Taking in mind the complexity of Monero code, it will be more useful if developer(s) of Monero take part in packaging flatpak because this will assist in decrease possibilities of errors in the package ....... At least just observation to assist 3rd party packager(s) in same way for flatpak package of Telegram.

By the way, this is the 2nd trail to distribute Monero as flatpak on FlatHub - see:
https://github.com/flathub/flathub/pull/94
As you see, 1st trail end by failure ! We wish the current PR achieve success. Certainly help of Monero developers will give great push forward .....

Best regards.

## roundtheworldman | 2021-04-08T17:49:23+00:00
Hello I have been working on trying to get Monero GUI Wallet app into Flathub.
I'm just a fan trying to help out.
Based on work that BigmenPixel0 already did.

I have no prior experience with Flathub packaging, nor their build system.
The Flathub maintainers there have a preference for builds from source, rather than pre-compiled binaries.

My original PR I have closed.
My current PR is here:
https://github.com/flathub/flathub/pull/2245

The Flathub build system, where I am currently stuck seems to be failing because Monero GUI requires a `git clone` of this repository to do a proper build.

https://flathub.org/builds/#/builders/10/builds/5238

some relevant output from the Flathub build system:
```
-- Found Git: /usr/bin/git
fatal: not a git repository (or any parent up to mount point /run/build)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
CMake Warning at cmake/GitGetVersionTag.cmake:38 (message):
  /run/build/monero-source: cannot determine current commit.  Make sure that
  you are building from a Git working tree
Call Stack (most recent call first):
  cmake/VersionGui.cmake:41 (git_get_version_tag)
  CMakeLists.txt:120 (include)
  ```

**The Flathub build system has minimal network permissions.**
**It seems that git clone is a blocker based on my current tests with their build system.**

The Flathub build system will do a download of a source code release from here. (this monero-gui repo)
But I don't think Flathub Build Bot has permissions to do a `git clone`

Can an @monero-project maintainer comment on why there is a requirement for a `git clone` in order to run `make release` as noted in the README.md file??

I have tested locally recently, and I can confirm:
It seems like downloading the current source code release tar ball file, and then running `make release` is not enough for `make` to be happy.
It complains that there is no `.git` directory.
Then when I run a `git init` in the downloaded, extracted dir, `make` complains that is is a git repo with no commits.

Can we remove this restriction for git clone?
I think it will help get Monero GUI into Flathub, and thus available to more users without having to manually download every new update.

Thank you for your help and consideration!

## mj-xmr | 2021-04-08T18:32:38+00:00
@roundtheworldman Are you able to feed Flathub's build system with a local clone of the official repo? Then within the build system, with a small `CMakeLists.txt` patch you could redirect the actual cloning from the official repo to the local clone, which will work equally fine.

## selsta | 2021-04-08T18:37:32+00:00
> I have tested locally recently, and I can confirm:
> It seems like downloading the current source code release tar ball file, and then running make release is not enough for make to be happy.
> It complains that there is no .git directory.
Then when I run a git init in the downloaded, extracted dir, make complains that is is a git repo with no commits.


That's because Github source tar ball does not include submodules. We do offer a full tarball, see e.g. https://github.com/monero-project/monero-gui/actions/runs/727690193

## roundtheworldman | 2021-04-08T19:57:03+00:00
> That's because Github source tar ball does not include submodules. We do offer a full tarball, see e.g. https://github.com/monero-project/monero-gui/actions/runs/727690193

Hi @selsta thanks for tip on the archive that includes the submodules!
However, I looked at the page you shared a link to and the relevant code in build.yml
It is not clear to me right now where this "meta-archive" that includes git submodules is actually being uploaded to??
Can you point me in the right direction?
Thanks!


## roundtheworldman | 2021-04-09T10:53:50+00:00
I see the artifacts in the actions workflow page you linked to now.
But I'm running into the dreaded problem of:
"it is easy for graphical web browser to click on above link and wait for the api call that will actually request the tar.zip file"
but
It is a lot harder to download the tar.zip file with `curl` or `wget`.

This describes what I'm running into pretty well:
https://github.com/actions/upload-artifact/issues/89#issuecomment-654217051

## xiphon | 2021-04-09T11:11:52+00:00
Yeah, we have to add source archive download link or upload source archive to [Monero GUI Github Releases](https://github.com/monero-project/monero-gui/releases) .

Will that be enough for you?

## roundtheworldman | 2021-04-09T14:45:28+00:00
> Yeah, we have to add source archive download link or upload source archive to [Monero GUI Github Releases](https://github.com/monero-project/monero-gui/releases) .
> 
> Will that be enough for you?

Yes, so as I stated before, the current way the source code is published is not enough to build the entire GUI without network access.

Can make it so that there is a tar file artifact URL published publicly, that **includes the git submodules** needed for `make release`??

I think that can work for getting this into Flathub.

```
Submodule path 'external/quirc': checked out '7e7ab596e4d0988faf1c12ae89c354b114181c40'
Submodule path 'monero': checked out 'f6e63ef260e795aacd408c28008398785b84103a'
Submodule 'external/miniupnp' (https://github.com/monero-project/miniupnp) registered for path 'monero/external/miniupnp'
Submodule 'external/randomx' (https://github.com/tevador/RandomX) registered for path 'monero/external/randomx'
Submodule 'external/rapidjson' (https://github.com/Tencent/rapidjson) registered for path 'monero/external/rapidjson'
Submodule 'external/supercop' (https://github.com/monero-project/supercop) registered for path 'monero/external/supercop'
Submodule 'external/trezor-common' (https://github.com/trezor/trezor-common.git) registered for path 'monero/external/trezor-common'
Submodule 'external/unbound' (https://github.com/monero-project/unbound) registered for path 'monero/external/unbound'

...
Finished uploading artifact monero-gui-v0.17.1.9-87-g41fc2772.tar. Reported size is 25779461 bytes.
There were 0 items that failed to upload
Artifact monero-gui-v0.17.1.9-87-g41fc2772.tar has been successfully uploaded!

```

I have been looking at doing an API call with Github3 (https://pypi.org/project/github3.py/)
But I don't think it's doable with the current Flathub Build system, since it has minimal network permissions and packages available to it, as far as I can tell.

But best solution is probably to just publicly publish the true tar.zip file link for what shows up here in the bottom of attached screenshot. (screenshot from the Action Workflow)
![Screenshot from 2021-04-09](https://user-images.githubusercontent.com/19298304/114196459-e7274800-9940-11eb-80bb-e00094c10f5a.png)


## xiphon | 2021-04-09T15:02:20+00:00
> I have been looking at doing an API call with Github3 (https://pypi.org/project/github3.py/)
But I don't think it's doable with the current Flathub Build system, since it has minimal network permissions and packages available to it, as far as I can tell.

Don't do that.

> Yes, so as I stated before, the current way the source code is published is not enough to build the entire GUI without network access.
> 
> Can make it so that there is a tar file artifact URL published publicly, that **includes the git submodules** needed for `make release`??
>
> I think that can work for getting this into Flathub.
>
> But best solution is probably to just publicly publish the true tar.zip file link for what shows up here in the bottom of attached screenshot. (screenshot from the Action Workflow)
Screenshot from 2021-04-09

That's literally what i said.

Just wait for v0.17.2.0 release, we will add source archive download link (or upload it) to [Monero GUI Github Releases](https://github.com/monero-project/monero-gui/releases).

Thanks.

## mj-xmr | 2021-04-10T09:59:20+00:00
Won't the Monero build scripts still complain about a missing version? The tarball in question is not supposed to have the .git dir.

## selsta | 2021-04-11T13:23:39+00:00
https://downloads.getmonero.org/gui/monero-gui-source-v0.17.2.0.tar.bz2

## roundtheworldman | 2021-04-12T10:22:15+00:00
@selsta 

Build failure output from flathub build system here:

```
...
Looking for -pie linker flag
-- Looking for -pie linker flag - found
-- Looking for -Wl,-z,relro linker flag
-- Looking for -Wl,-z,relro linker flag - found
-- Looking for -Wl,-z,now linker flag
-- Looking for -Wl,-z,now linker flag - found
-- Looking for -Wl,-z,noexecstack linker flag
-- Looking for -Wl,-z,noexecstack linker flag - found
-- Looking for -Wl,-z,noexecheap linker flag
-- Looking for -Wl,-z,noexecheap linker flag - not found
-- Using C security hardening flags:  -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -fcf-protection=full -fstack-clash-protection
-- Using C++ security hardening flags:  -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -fcf-protection=full -fstack-clash-protection
-- Using linker security hardening flags:  -pie -Wl,-z,relro -Wl,-z,now -Wl,-z,noexecstack
CMake Error at /usr/share/cmake-3.19/Modules/FindPackageHandleStandardArgs.cmake:218 (message):
  Could NOT find Boost (missing: Boost_INCLUDE_DIR system filesystem thread
  date_time chrono regex serialization program_options locale) (Required is
  at least version "1.58")
Call Stack (most recent call first):
  /usr/share/cmake-3.19/Modules/FindPackageHandleStandardArgs.cmake:582 (_FPHSA_FAILURE_MESSAGE)
  /usr/share/cmake-3.19/Modules/FindBoost.cmake:2208 (find_package_handle_standard_args)
  monero/CMakeLists.txt:886 (find_package)
-- Configuring incomplete, errors occurred!
See also "/run/build/monero-source/build/release/CMakeFiles/CMakeOutput.log".
See also "/run/build/monero-source/build/release/CMakeFiles/CMakeError.log".
make: *** [Makefile:48: release] Error 1
]2;flatpak-builder: Cleanup monero-sourceError: module monero-source: Child process exited with code 2
FB: Unmounting read-only fs: fusermount -uz /srv/buildbot/worker/build-x86_64/build/.flatpak-builder/rofiles/rofiles-JU79rM
```
https://flathub.org/builds/#/builders/48/builds/5248/steps/6/logs/stdio

Boost is a pretty common library for a long time. I have a hard time believing that they do not have this in their build environment. I will have to look to see if there is a way to add this as a build pre-req there before compilation. But if you have any tips, please let me know.

## q7nm | 2021-07-05T09:40:40+00:00
Accepted on flathub :)
https://github.com/flathub/org.getmonero.Monero

## elibroftw | 2022-04-23T16:55:42+00:00
Close this? @selsta 

# Action History
- Created by: Nokia808 | 2020-03-13T20:07:58+00:00
- Closed at: 2022-04-23T16:56:24+00:00
