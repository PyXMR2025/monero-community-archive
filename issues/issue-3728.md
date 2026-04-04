---
title: Static builds fail on Ubuntu 16.04
source_url: https://github.com/monero-project/monero/issues/3728
author: TheQuantumPhysicist
assignees: []
labels: []
created_at: '2018-04-29T16:00:09+00:00'
updated_at: '2018-04-30T08:10:39+00:00'
type: issue
status: closed
closed_at: '2018-04-29T20:44:26+00:00'
---

# Original Description
This recipe fails:

```
git clone --recursive https://github.com/monero-project/monero
cd monero && git submodule init && git submodule update
make debug-static-all # fails, says it requires -fPIC flag
rm -r build
make release-static # fails, also wants -fPIC
```

While you guys verify this issue, can you please tell me why you're not using CI on github? I see CI flags on github's readme.md, but most of them fail. I tried to contribute to monero and tried to build it in Qt Creator (which supports cmake out of the box)... and it was mission impossible. I always got undefined reference to `libblockchain` when compiling in debug mode. Apparently, this dependency path is not specified in reference to build directory... I don't know... I'm guessing here because Qt Creator uses shadow directories (directories at the same level) for building. Can someone try this and verify too?


# Discussion History
## moneromooo-monero | 2018-04-29T18:43:49+00:00
Then build whatever it's telling you about with -fPIC. We can't do that for you.


## moneromooo-monero | 2018-04-29T18:52:49+00:00
Or build shared (which is the default). Shared libraries are always built with -fPIC so you don't have to rely on your distribution to be nice.

## TheQuantumPhysicist | 2018-04-29T19:19:41+00:00
@moneromooo-monero
Thanks for the response. You can add the necessary flags to cmake for static mode and make it part of the master branch. I'm not unable to add this for my own copy, but if you add it then it'll work out of the box for everyone, unless there's a reason not to. Is there a reason to avoid adding that flag to all static builds?

Shared libs are not always suitable. Sometimes portable code is needed. As a dev for a privacy oriented coin you definitely know what the reasons may be ;-)

Also what about CI? You haven't commented on that. Why does Monero ignore CI recently? Is it just that you guys are busy with other things or is there another reason?

## moneromooo-monero | 2018-04-29T19:24:19+00:00
You're missing the point. monero builds with -fPIC. It just needs its deps to also be built with -fPIC (like, say, boost, openssl, etc).

We use CI as far as I know. I stopped looking at the reports because it was a massive waste of time as I got pinged many times a day for irrelevant stuff. Unfortunate.


## TheQuantumPhysicist | 2018-04-29T20:44:26+00:00
> You're missing the point. monero builds with -fPIC. It just needs its deps to also be built with -fPIC (like, say, boost, openssl, etc).

I guess you're right. There's nothing to be done from your side. Apologies for the incorrect report.

About CI. I understand the reports are overwhelming. But maybe just look whether it passed or not, and if doesn't pass, then maybe something is wrong. Just a friendly suggestion :-)

Cheers!

## moneromooo-monero | 2018-04-29T21:44:00+00:00
Yes, you're correct, but there are so many false positives at some point you just want to strangle that thing till it shuts up :P

## TheQuantumPhysicist | 2018-04-30T08:10:38+00:00
This probably means that many contexts are mixed together. I don't know if this is the case for Monero, just guessing here. For example, I believe that mixing unit-tests with build tests is a bad idea exactly for this reason. It gets overwhelming very quickly. 

# Action History
- Created by: TheQuantumPhysicist | 2018-04-29T16:00:09+00:00
- Closed at: 2018-04-29T20:44:26+00:00
