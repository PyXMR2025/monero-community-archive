---
title: Homebrew (macOS) based package install broken on release v0.12"
source_url: https://github.com/monero-project/monero/issues/3786
author: Zarkoob
assignees: []
labels: []
created_at: '2018-05-09T05:51:32+00:00'
updated_at: '2019-06-17T00:39:41+00:00'
type: issue
status: closed
closed_at: '2018-05-27T06:36:21+00:00'
---

# Original Description
Trying to build 12.0 on OSX 10.13.4 with homebrew gives the following error:


==> Downloading https://github.com/monero-project/monero/pull/3667.patch?full_index=1
==> Downloading from https://patch-diff.githubusercontent.com/raw/monero-project/monero/pull/3667.patch?full_index=1

curl: (22) The requested URL returned error: 404 Not Found
Error: Failed to download resource "monero--patch"
Download failed: https://github.com/monero-project/monero/pull/3667.patch?full_index=1

If I try to go to the page directly I get "Sorry, this diff is unavailable."

This is from following step by step on the Monero homepage. 

# Discussion History
## moneromooo-monero | 2018-05-09T08:21:20+00:00
Where are those instructions exactly ?

## jtgrassie | 2018-05-09T14:19:12+00:00
I _think_ he's doing an install via Homebrew (as detailed in the readme):
```
  brew tap sammy007/cryptonight
  brew install monero --build-from-source
```

@Zarkoob please confirm.


## moneromooo-monero | 2018-05-09T14:37:13+00:00
Then I guess it's downloading something sammy007 maintains, and needs to update. I have no idea how that works.

## jtgrassie | 2018-05-09T14:47:25+00:00
> I have no idea how that works.

Me neither!

Side note, I not particularly fond of third party patches to the core being applied when we link out to a third party maintained build from the repository readme. The malicious third party could add malicious code that appears trusted because they were directed to that build from the main project readme. ?


## moneromooo-monero | 2018-05-09T16:52:14+00:00
Yes, a warning would be warranted I guess if that's what it's doing.

## Zarkoob | 2018-05-09T17:46:11+00:00
The instructions for this are right on the main monero git page. Under MacOS. I'm just trying to build it like they say. 

https://github.com/monero-project/monero 

## jtgrassie | 2018-05-09T19:12:42+00:00
@Zarkoob there are various ways to build detailed. Which one are you doing? 

## Zarkoob | 2018-05-09T19:20:36+00:00
I'm saying again **MacOS**

(From my original post) **Trying to build 12.0 on OSX 10.13.4 with homebrew gives the following error**:

 - It's right there, the homebrew options:

OS X via Homebrew
brew tap sammy007/cryptonight
  brew install monero --build-from-source


@jtgrassie  I don't see any other OS X options, are there?

## jtgrassie | 2018-05-09T19:30:43+00:00
It's on the same page further down. You followed 'Installing from package'. Look further down and you'll see:
```
Compiling from Source
...
On Linux and OS X
```
Anyway, that package install is a third party maintained package that looks to have not been updated. So thanks for flagging.

@moneromooo-monero any idea who maintains that? We really need this addressed (or removed).


## moneromooo-monero | 2018-05-09T19:37:34+00:00
sammy007

## jtgrassie | 2018-05-09T19:44:59+00:00
@Zarkoob did you previously install monero using that command? Reason I ask is I had a look at the tap repository and it doesn't try to patch a PR. Maybe try to update via brew updating command (https://docs.brew.sh/How-to-Create-and-Maintain-a-Tap):

"**Updating**
Once your tap is installed, Homebrew will update it each time a user runs `brew update`. Outdated formulae will be upgraded when a user runs `brew upgrade`, like core formulae."

And then running `brew install monero --build-from-source`.


## Zarkoob | 2018-05-09T20:32:14+00:00
That's the exact command that causes the error: 

"brew install monero --build-from-source"

## jtgrassie | 2018-05-09T20:37:58+00:00
Yes but did you run `brew update` or `brew upgrade` first?

## Zarkoob | 2018-05-09T20:42:58+00:00
No, I did it as the website suggests.  Should I try one of the options you gave just now first?

Also, wouldn't this be a potential security threat? Taking a patch from 1 source like this?

edit: Tried and it does the same thing, as others have stated it looks like it's coming from something sammy007 is maintaining. 

## jtgrassie | 2018-05-09T21:11:16+00:00
@Zarkoob did you see my previous comment?

https://github.com/monero-project/monero/issues/3786#issuecomment-387853495

If you previously installed monero using brew, you probably need to update the tap. Which I presume is `brew update`. I'm sorry I don't use Homebrew so don't know the specifics.

> Also, wouldn't this be a potential security threat? Taking a patch from 1 source like this?

To some degree. It just needs a disclaimer on our project page as without a disclaimer, it appears a monero team supported / developed / reviewed option. Only compiling form source (detailed further down the page) is the officially supported / maintained build option - not package builds.


## jtgrassie | 2018-05-09T21:12:19+00:00
> edit: Tried and it does the same thing, as others have stated it looks like it's coming from something sammy007 is maintaining.

Yes and you should see I have already raised an issue on that repository for you (and it shows linked in this thread on github).

## sammy007 | 2018-05-09T21:42:57+00:00
The patch is in original homebrew formula (added recently to brew mainline) https://github.com/Homebrew/homebrew-core/blob/master/Formula/monero.rb it's not from my tap.

## jtgrassie | 2018-05-09T21:46:21+00:00
Are the readme instructions wrong then? 

## sammy007 | 2018-05-09T21:56:35+00:00
They are not wrong, they are just outdated because brew added a formula for monero and you should install my tap explicitly. I don't like the style how brew handled recent hard fork, they have been hosting outdated v0.11 release for irresponsible long time.

I propose the change how we can handle this issue:

* Fork https://github.com/sammy007/homebrew-monero and keep it under monero project
* All further updates to formula must go via pull-requests, in other words to take over ownership of this tap (solves any security concerns as well)
* Update README to highlight that this formula is alternative method
* Advice to compile via git clone & make

It currently seems broken again, always a mess to keep it up to date with a rolling release style of brew.

Another option:

* Maintain brew stock formula, bit it's a PITA, because brew maintainer seems does not understand how it's necessary to keep formula up to date.


## jtgrassie | 2018-05-10T00:07:21+00:00
@sammy007 thanks for chiming in. Is there a way to force install from your formula rather than the other? Your proposed changes make sense (the first bullets). Can you make a PR based on those?

The other packages have similar issues, I was thinking of updating the readme with a loud disclaimer and demoting the package installs to later in the readme (after source build and install from repo), but I guess there's a lot of users that use package installs. Really novice (not the right term I know) users will use pre-built binaries, next will use packages, next will build from source. Security wise the best option is anything directly under the repository, whether that be packages, source or prebuilt, as at least they are vetted / peer reviewed.

## sammy007 | 2018-05-10T01:01:56+00:00
@jtgrassie check out https://github.com/sammy007/homebrew-monero/blob/master/README.md (brew tap-pin). But it likely broken, I can't dedicate time to fix it, I am running old OSX version, etc.

I can't do a PR, I proposed to transfer membership, it requires core to accept it. I can't commit to monero repositories because I am 3rd party, not a member of development team.

For now I propose to just download binaries from release tab or just clone repo and `make` it, without brew.

## Zarkoob | 2018-05-10T01:26:16+00:00
@sammy007 When I try to issue the make command it stops with errors:

Undefined symbols for architecture x86_64:
  "_rl_copy_text", referenced from:
      _main in CheckFunctionExists.c.o
ld: symbol(s) not found for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)

## jtgrassie | 2018-05-10T01:33:27+00:00
@sammy007 fair enough. I'll make changes to the readme then, which apply to the other packages also anyway. Do you agree we should possibly even remove the brew instruction now it's effectively unmaintained / broken?

@Zarkoob have you installed all the dependencies? 

## sammy007 | 2018-05-10T01:54:08+00:00
@jtgrassie I am sure I have fixed it, need to perform moar tests. Hard to compile such heavy stuff on 2011 mac.

Need to change readme to at least:

```
brew tap sammy007/monero
brew tap-pin sammy007/monero
brew install monero
```

And add a note that formula from brew core is not preferred because broken and could be significantly outdated.

I still prefer the idea of transferring membership of my tap to monero project and offering it as convenient (hipster) way of installation. Solves confusion and security issues.

## jtgrassie | 2018-05-10T01:59:20+00:00
@sammy007 Cool, thanks. I just made a PR #3791 removing the Homebrew package (and adding a disclaimer) but if this change can be tested I'll update to add that change in. There's a lot of brew folks out there so hopefully someone can test.

## jtgrassie | 2018-05-10T02:12:32+00:00
@Zarkoob could you update this issue title to something that references the Homebrew package install please so hopefully we get some testers on @sammy007's [comment](https://github.com/monero-project/monero/issues/3786#issuecomment-387927166) above please? 

Something like: "Homebrew based package install broken on release v0.12".

## sammy007 | 2018-05-10T02:26:06+00:00
It works for me already. And I have sent a PR to core brew with a fix.

## Zarkoob | 2018-05-10T02:30:43+00:00
@jtgrassie I changed the topic for you that makes more sense I agree. 

For the new update I’m not home to test. I will as soon as I can for you. Do I just need to update and type what you did post before @sammy007? 

## jtgrassie | 2018-05-10T02:37:05+00:00
Thanks @Zarkoob 

I believe you just need to:

```
brew tap sammy007/monero
brew tap-pin sammy007/monero
brew install monero
```

based on @sammy007's comments.


## sammy007 | 2018-05-10T02:39:33+00:00
Well, hold on for now, this fucking brew seems ignores `tap-pin` for some reason and always install bottle, I will show up later with better guide.

## jtgrassie | 2018-05-10T02:40:23+00:00
@sammy007 
> It works for me already. And I have sent a PR to core brew with a fix.

Nice, thanks. I have updated the readme PR to add your change.

## jtgrassie | 2018-05-10T02:48:13+00:00
@sammy007 ugh ok, just updated the PR again then to remove your last note. Just ping me if you manage to find a fix and I'll update the PR again. I thought there was a single command to install from specific formula w/o needing to add the tap? Something like `brew install sammy007/monero`?

I'm pretty confident @fluffypony would create the repo in this project if asked with an apple.

## Zarkoob | 2018-05-10T03:00:01+00:00
I tried and I get the **same** errors when I download directly from git and try to issue the `make` command (as it's just doing what I'm doing only with "extra" stuff on the end of cmake):

==> `cmake . -DCMAKE_C_FLAGS_RELEASE=-DNDEBUG -DCMAKE_CXX_FLAGS_RELEASE=-DNDEBUG -DCMAKE_INSTALL_PREFIX=/usr/local/Cellar/monero/0.12.0.0 -DCMAKE_BUILD_TYPE=Release -DCMAKE_FIND_FRAMEWORK=LAST -DCMAKE`
Last 15 lines from /Users/daniel/Library/Logs/Homebrew/monero/01.cmake:
-- AES support enabled
-- Found Boost Version: 106700
-- Looking for rl_copy_text
-- Looking for rl_copy_text - not found
-- Looking for rl_filename_completion_function
-- Looking for rl_filename_completion_function - found
-- Could not find GNU readline library so building without readline support
-- Found Git: /usr/local/bin/git
Doxygen: graphviz not found - graphs disabled
-- Could NOT find Doxygen (missing: DOXYGEN_EXECUTABLE)
-- Performing Test HAVE_C11
-- Performing Test HAVE_C11 - Success
-- Configuring incomplete, errors occurred!
See also "/tmp/monero-20180509-20438-1gjoq6w/monero-0.12.0.0/CMakeFiles/CMakeOutput.log".
See also "/tmp/monero-20180509-20438-1gjoq6w/monero-0.12.0.0/CMakeFiles/CMakeError.log".

If reporting this issue please do so at (not Homebrew/brew or Homebrew/core):
https://github.com/sammy007/homebrew-monero/issues


Both issues in CMakeError.log are the same, are these pin issues like @sammy007 wrote or do I miss a dep like @jtgrassie asked?

I'm not sure how much of the CMakeError.log you want? (do I report this on the link it says or is here ok since they're linked? I'm new to github forgive me )

## Zarkoob | 2018-05-10T03:09:27+00:00
@jtgrassie also you asked if I had monero installed before. Only as the download not the package via git / install. NOT with brew. Sorry I didn't answer before.

When I try and do a `brew upgrade monero` I get `Error: monero not installed`

## sammy007 | 2018-05-10T03:21:11+00:00
@jtgrassie go ahead with my last instructions, I finally managed to test it on fresh OS with fresh brew, works for me. Aka

```
brew tap sammy007/monero
brew tap-pin sammy007/monero
brew install monero
```


## Zarkoob | 2018-05-10T04:20:53+00:00
@sammy007 I can't get it to install, it fails where / what error logs should I post? MacOS 10.13.14

## jtgrassie | 2018-05-10T11:48:36+00:00
@Zarkoob have you tried `brew install sammy007/monero`?

## Zarkoob | 2018-05-10T14:13:19+00:00
@jtgrassie yes. I’m sure it’s my machine if Sammy gets it installed but can’t figure out what is not worKing I’m not good with logs 

## Zarkoob | 2018-05-11T03:10:28+00:00
@jtgrassie I've been able to compile monero from source now on macOS 10.13.4 **without** using homebrew. When I try to use homwbrew it errors out.  Since I'm able to get it to work, but sammy the author can... should I just close the issue?

## moneromooo-monero | 2018-05-11T08:46:21+00:00
The actual error's probably earlier in the cmake output.

## ilovezfs | 2018-05-16T14:48:40+00:00
I strongly suggest `brew install monero` and using the prebuilt bottles, not tap-pinning or building from source.

## sammy007 | 2018-05-16T15:13:07+00:00
I strongly suggest using only official binaries from monero-project github built by core team.
The tap pinning is used because `brew install monero` always outdated and broken. It takes 1-2 weeks to convince them to fix it.

https://www.linuxuprising.com/2018/05/malware-found-in-ubuntu-snap-store.html


## ilovezfs | 2018-05-16T15:39:48+00:00
If you want to use the upstream version:

```
brew cask install monero-wallet
```

>The tap pinning is used because brew install monero always outdated and broken. It takes 1-2 weeks to convince them to fix it.

This is insulting and false, and I'm not going to engage with you further about it.

## sammy007 | 2018-05-16T16:07:55+00:00
> This is insulting and false

I agree, your reply is false.

The proof of your outdated and confusing formula https://github.com/Homebrew/homebrew-core/pull/25993


## ilovezfs | 2018-05-16T16:10:13+00:00
Yes, which I finished for you in https://github.com/Homebrew/homebrew-core/pull/25726.

## sammy007 | 2018-05-16T16:33:25+00:00
Wow, **your finished it for me**. If you want to package software learn something about its development process. Keeping outdated versions for a while after mandatory protocol upgrade is harmful for users.

## ilovezfs | 2018-05-16T16:36:49+00:00
@jtgrassie @moneromooo-monero this issue can be closed as there is no problem with the current version in Homebrew/homebrew-core.

## Zarkoob | 2018-05-27T05:35:29+00:00
_Can we have the issue still open? I am not able to build it with the commands listed above using homebrew._ 


I can build it **with out** homebrew. But not **with** homebrew     @sammy007 @ilovezfs @moneromooo-monero  (I guess technically that's more secure right?)

@jtgrassie I also am able to build https://github.com/fluffypony/monero version now too from source and I'm on 10.13.4 Mac OSx how do I report to @fluffypony that it works on this version of Mac OSx? I don't see any way to comment on that version he has on his forked page of github. (where it says build success and has OS version listed, I don't see mac 10.13.4 etc) Processor is Intel(R) Core(TM) i7-4980HQ CPU @ 2.80GHz

version while running monerod and wallet-cli says:
Monero 'Lithium Luna' (v0.12.1.0-master-45975fd8)


## ilovezfs | 2018-05-27T06:06:40+00:00
@Zarkoob I can try to help you if you post the output of `brew gist-logs monero`. It's going to be a local configuration issue, though, and not a problem with the [Homebrew/homebrew-core formula](https://github.com/Homebrew/homebrew-core/blob/master/Formula/monero.rb) or the Monero project, as Homebrew just had 🍏 CI for `monero` and a new version a couple days ago. See
https://github.com/Homebrew/homebrew-core/pull/28210
https://github.com/Homebrew/homebrew-core/commit/975371a58f9be5c9da684c2934dbb87722d32e80
https://github.com/Homebrew/homebrew-core/commit/fa98922082d8ad32f1aeb25d57fead9bd93fe89f
https://jenkins.brew.sh/job/Homebrew%20Core%20Pull%20Requests/24714/


## Zarkoob | 2018-05-27T06:12:37+00:00
@ilovezfs ok great thank you! 

I think I did this right?   https://gist.github.com/Zarkoob/db6889008807760eb3a5de9e8bde8e16



## ilovezfs | 2018-05-27T06:18:14+00:00
OK, try this please:
```
brew tap-unpin sammy007/monero
brew install monero
```

## Zarkoob | 2018-05-27T06:27:23+00:00
@ilovezfs 



`Pouring monero-0.12.1.0.high_sierra.bottle.tar.gz`
 seems to have worked... 

I did a 
`brew reinstall monero --build-from-source`
 now to test and got 
`/usr/local/Cellar/monero/0.12.1.0: 13 files, 62.6MB, built in 4 minutes 51 seconds`


## ilovezfs | 2018-05-27T06:29:15+00:00
Perfect :)

## Zarkoob | 2018-05-27T06:34:57+00:00
inside the **MONEROD** and **MONERO-WALLET-CLI** program when I do version I get
`Monero 'Lithium Luna' (v0.12.1.0-master-release)`



## Zarkoob | 2018-05-27T06:36:21+00:00
Since homebrew is able to install from source v0.12.1.0-master-release I'm closing the issue.

## Zarkoob | 2018-05-27T07:03:46+00:00
@ilovezfs how do we (or myself) update the main page to show it's working on this build of mac and OS?

## ilovezfs | 2018-05-27T07:54:03+00:00
@Zarkoob I think that reflects Monero's CI, which doesn't appear to be running on macOS at all. It could probably be run on Travis's or CircleCI's macOS offerings, though.

## Zarkoob | 2018-06-02T20:36:01+00:00
@ilovezfs how would we upgrade to the next version out 0.12.2.0? 

## ilovezfs | 2018-06-03T04:20:23+00:00
@Zarkoob https://github.com/Homebrew/homebrew-core/pull/28604 will upgrade the formula to 0.12.2.0. However, https://github.com/monero-project/monero/releases/latest still points to 0.12.1.0 so we cannot ship it yet.

If you're eager you can `brew pull 28604` and then `brew upgrade --build-from-source monero` or just wait for @fluffypony or @moneromooo-monero to actually designate 0.12.2.0 as the latest release.

## Zarkoob | 2018-06-03T06:52:44+00:00
@ilovezfs thank you for the reply... just learning here so I appreciate the baby steps.

while I waited for your reply I did a `brew edit monero` then changed the tag and revisions to be:
tag: `v0.12.2.0`
revision `0d219ccdcda36e1ce620a5a5e7ab820f85cba379`
then I did a `brew upgrade --build-from-source monero` and it made v0.12.2.0 for me.


How did you know to do 28604 on the brew pull? did I do it wrong by editing the 
`brew edit monero`?

## ilovezfs | 2018-06-04T05:30:27+00:00
@Zarkoob you did not do it wrong, no. You'd only know to use `brew pull 28604` by searching the pull requests for monero https://github.com/Homebrew/homebrew-core/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Aopen+monero

## Zarkoob | 2018-10-10T21:29:22+00:00
@ilovezfs I'm trying to reinstall monero and it's failing again. It's triyng to install v0.12.2.0 and I've edited `brew edit monero` but it still does 0.12.2. Is there a way to install fresh with 0.13+?

## Zarkoob | 2019-06-17T00:39:41+00:00
@sammy007 what would be the best way to upgrade to v0.14.1.0 with homebrew? 

# Action History
- Created by: Zarkoob | 2018-05-09T05:51:32+00:00
- Closed at: 2018-05-27T06:36:21+00:00
