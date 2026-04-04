---
title: M1 binaries
source_url: https://github.com/monero-project/monero/issues/8291
author: sweeden-ttu
assignees: []
labels: []
created_at: '2022-04-25T23:10:03+00:00'
updated_at: '2022-04-27T23:52:55+00:00'
type: issue
status: closed
closed_at: '2022-04-27T23:47:17+00:00'
---

# Original Description
I will provide you with the Xcode flags for cross compiling.   When you compile with Homebrew I used the Hardening flags for tor and nginx.   --without-mail and --without-realip

# Discussion History
## selsta | 2022-04-25T23:16:43+00:00
I didn't accuse you of tempering with the binaries. It's fine if you want to provide 3rd party binaries for M1, but the bug tracker is not the place for this, especially when they are incorrectly tagged as "official".

We have a specific process for building release binaries and if that process isn't followed they aren't "official" binaries.

## sweeden-ttu | 2022-04-25T23:26:14+00:00
Well your release is no more official than mine if it doesn't work so let's test it you pass some amount to me I'll pass everything along to Jeff. 

Or whoever you working with I don't know you I'm not running your binary on my machine. 

I do know monero that's why I want to contribute.  I can't compile bitcoin I can't compile Ethereum I don't trust those.

So if you want to test it just tell me what parameters you want to me to run on my machine through an email I will pass everything along to Jeff then we can all know that version 17_3 is working on main_net.

If it's not working on Main_net then don't tell people to download it on the Debian 17.2 release.



## sweeden-ttu | 2022-04-26T00:02:55+00:00
> I didn't accuse you of tempering with the binaries. It's fine if you want to provide 3rd party binaries for M1, but the bug tracker is not the place for this, especially when they are incorrectly tagged as "official".
> 
> 
> 
> We have a specific process for building release binaries and if that process isn't followed they aren't "official" binaries.

If you're going to provide binaries then warn people about the hardcoded DNS servers.

I'm providing these binaries unaltered.  I don't recommend anybody run them because they have those hardcoded DNS servers in there and it will work just fine if you go and change those DNS servers.  

Put your money where your mouth is and put my binaries with yours.  I run my node anonymously and if you don't like it tough titties

## jeffro256 | 2022-04-26T04:17:31+00:00
@web-sharp : @selsta is legit and part of the core dev team, funded through the [CCS](https://ccs.getmonero.org/proposals/selsta-4.html). They're not trying to trick you, but there is a process which binaries must go through (gitian). It's good that you're contributing, but advertising your binaries as "official" is misleading and dangerous since we can't guaranteed that your binaries are not malicious. 

If you want "official" Apple Silicon binaries, then create a PR for the gitian build process. I'm not an expert, but @hyc or @mj-xmr are much more familiar with that process.

## mj-xmr | 2022-04-26T04:57:58+00:00
We do confirm each other's binaries through Gitian, see ([contrib/gitian](https://github.com/monero-project/monero/tree/master/contrib/gitian) directory and it's README.md). Contributions there are always welcome and will allow reviewers to have a peek.

A thing to note here, is that there's indeed some extra effort to be done in order to use this method, but it solves potential disputes.

## hyc | 2022-04-26T16:13:03+00:00
Currently our MacOS gitian build only produces x86-64 binaries. If you can provide the flags to make Xcode cross-compile on Linux to produce aarch64 binaries using gitian, that'd be great.

## sweeden-ttu | 2022-04-27T22:00:08+00:00
I didn't compile it with Xcode I used gnu C.   I can probably get that to you though

## sweeden-ttu | 2022-04-27T22:05:54+00:00
Does anyone have a coupon code I can use with Mac stadium?  lol.  It's pretty pricy and all my X86_64 Macs run linux

## sweeden-ttu | 2022-04-27T23:47:17+00:00
If @selsta is paid in euros then I suppose I trust them.  I will purchase bare metal x86_64 with Mac stadium and test that I can send 32 Monero to it using from main_net

## selsta | 2022-04-27T23:52:54+00:00
https://github.com/monero-project/monero/tree/master/contrib/gitian

As it was already said before, this is the process we are using for release binaries. Support for M1 Mac has to be added there. We cross compile everything from x86_64 linux.

# Action History
- Created by: sweeden-ttu | 2022-04-25T23:10:03+00:00
- Closed at: 2022-04-27T23:47:17+00:00
