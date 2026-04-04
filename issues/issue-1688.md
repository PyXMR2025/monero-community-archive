---
title: make debug-test, behaves differently after, make clean
source_url: https://github.com/monero-project/monero/issues/1688
author: tdprime
assignees: []
labels: []
created_at: '2017-02-05T23:32:45+00:00'
updated_at: '2017-02-12T21:20:02+00:00'
type: issue
status: closed
closed_at: '2017-02-12T21:20:02+00:00'
---

# Original Description
Doing the following experiment,
```
make clean; make debug-test 2>&1 | tee make1.log
make debug-test 2>&1 | tee make2.log
diff make[12].log | head -22
```
yields this result,
```
< -- Building internal libraries with position independent code
---
> -- Building internal libraries as static
```

Having the build behave differently creates many problems.  Requiring all builds to be done after `make clean`.

# Discussion History
## ghost | 2017-02-06T00:32:17+00:00
What platform/processor?

## tdprime | 2017-02-06T00:41:39+00:00
Linux primacy 4.4.0-59-generic #80-Ubuntu SMP Fri Jan 6 17:47:47 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux


## tdprime | 2017-02-06T01:38:45+00:00
`BUILD_SHARED_LIBS` is being changed inside `tests/gtest/CMakeLists.txt`

## ghost | 2017-02-06T08:02:53+00:00
Your issue seems to be coming from different build flags each time you run `make debug-test` as a result of lines `189-199` in `CmakeLists.txt`. 

Your system first executes `set(BUILD_SHARED_LIBS ON)`, building shared libs with -fPIC, but this is then changed back to `OFF` by the time it reaches `/tests/gtest/CMakeLists.txt`, so the second time you run `make debug-test` they're built as static.

What is the expected behaviour? Static or with position-independent-code? There are a couple of solutions depending on which.

## tdprime | 2017-02-06T12:53:52+00:00
Me?  I am new to this project.  I was just trying to get a working build.  Encountered issue #1660 and have been trying to fix things.  Since the build isn't repeatable, that has been made 10x more difficult.

## ghost | 2017-02-06T21:26:57+00:00
Just build without debug for now - `make release`

@moneromooo-monero should this be static or -fPIC? What if we remove `option(BUILD_SHARED_LIBS "Build shared libraries (DLLs)." OFF)` from `/tests/gtest/CMakeLists.txt`?

## moneromooo-monero | 2017-02-06T21:51:25+00:00
I'm not the right guy to ask about cmake to be honest. I know close to nothing about it. But it does indeed seem wrong. However, I've been making incrementally for ages without apparent trouble (though with a custom target, but based on the existing ones).

## ghost | 2017-02-07T17:33:17+00:00
@moneromooo-monero @tdprime I think we should remove `option(BUILD_SHARED_LIBS "Build shared libraries (DLLs)." OFF) from /tests/gtest/CMakeLists.txt` and let the master shared vs. static option override here. 

Unless you can see a reason why this might not be desirable (e.g. always wanting shared libraries ON) then let me know.

## hyc | 2017-02-07T18:26:17+00:00
(1) Why are we building shared libraries, ever? Security-sensitive binaries like these should only use static libraries.
(2) Shared libraries suck for test environments. They require you to use LD_LIBRARY_PATH or equivalent to find the correct shared libs. 

## tdprime | 2017-02-07T19:23:14+00:00
> On Feb 7, 2017, at 1:26 PM, hyc <notifications@github.com> wrote:
> 
> (1) Why are we building shared libraries, ever? Security-sensitive binaries like these should only use static libraries.
> 
Please clarify your concern.  All of the security code I know of is in a shared library: libcryto.so libssl.so, ...
> (2) Shared libraries suck for test environments. They require you to use LD_LIBRARY_PATH or equivalent to find the correct shared libs.
> 
I mostly work on Linux and FreeBSD.  On Linux, it’s not so bad.  One can differentiate between the build location and the install location easily enough with -rpath.

I don’t know what motivated this particular build choice.  I speculate this could have more to do with the build cycle at the time one is actively debugging a problem.  Under such conditions, there will be rapid code churn in a localized portion of the code.  If most is unchanged and it those are in shared libraries, the linking phase will be quicker.  Perhaps the time saving is 10-60s per iteration.  As I said, this is just a guess.

## tdprime | 2017-02-07T20:53:35+00:00
I was able to learn one more thing, installing libgtest*.a into /usr/lib/ works around this issue.

## ghost | 2017-02-07T22:16:39+00:00
Where were they before?

@hyc @moneromooo-monero So default should always be static unless there's a good reason otherwise? Can you think which of the `Makefile` builds should be built with shared libs, otherwise I can go through and make this stuff explicit where necessary to prevent this happening to anyone else.

## tdprime | 2017-02-07T22:24:15+00:00
I did some research today.  Came across this, https://crascit.com/2015/07/25/cmake-gtest/ <https://crascit.com/2015/07/25/cmake-gtest/>

I was going to look into adapting this method for the monero project.  This will keep tests/gtest/CMakeLists.txt from polluting the build environment for others.

As for the history of things, here is when things changed: https://github.com/monero-project/monero/commit/06bb6923c3068637af729dd7e7500ce1a6c888b9 <https://github.com/monero-project/monero/commit/06bb6923c3068637af729dd7e7500ce1a6c888b9>


> On Feb 7, 2017, at 5:16 PM, Nano Akron <notifications@github.com> wrote:
> 
> Where were they before?
> 
> @hyc <https://github.com/hyc> @moneromooo-monero <https://github.com/moneromooo-monero> @fluffypony <https://github.com/fluffypony> So two ways through this really - default should always be static unless there's a good reason otherwise. Can you think which of the Makefile builds should be built with shared libs? Otherwise I'll go through and make this stuff explicit where necessary.
> 
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub <https://github.com/monero-project/monero/issues/1688#issuecomment-278159987>, or mute the thread <https://github.com/notifications/unsubscribe-auth/AYMjtsvNDKLUdW1Lhtp6ldsUeW_JXfSuks5raO1KgaJpZM4L3qz6>.
> 



## hyc | 2017-02-07T22:37:43+00:00
tdprime wrote:
>> On Feb 7, 2017, at 1:26 PM, hyc <notifications@github.com> wrote:
>>
>> (1) Why are we building shared libraries, ever? Security-sensitive binaries
> like these should only use static libraries.
>>
> Please clarify your concern. All of the security code I know of is in a shared
> library: libcryto.so libssl.so, ...

We statically link libssl.a and libcrypto.a on the official binaries. 
Different Linux distros ship wildly varying versions of these things, you 
can't depend on the right version of the shared library to be present.

-- 
   -- Howard Chu
   CTO, Symas Corp.           http://www.symas.com
   Director, Highland Sun     http://highlandsun.com/hyc/
   Chief Architect, OpenLDAP  http://www.openldap.org/project/


## ghost | 2017-02-08T10:51:38+00:00
@hyc Do those two libraries get included when one clones the repo from GitHub?

## hyc | 2017-02-08T11:20:09+00:00
@NanoAkron no. they still come from the build machine.

## ghost | 2017-02-08T15:22:46+00:00
@tdprime The steps described in that link would seem to ensure that we always build against the latest google test libraries, which is nice (so long as we have an internet connection at build time)

But this issue does raise an important point as noticed by @hyc - do we always build static _except_ for a few cases (as yet undefined) where we want shared libs. If so, we need to define the times when it is acceptable or necessary to build against shared libs.

Otherwise we just go in to `Makefile` and add `-D STATIC=ON` to every option, and amend those corresponding lines we've identified in `CmakeLists.txt`. Trivial.

@vtnerd, @moneromooo-monero, @fluffypony Opinions on static vs shared libs?

## moneromooo-monero | 2017-02-08T17:22:40+00:00
I don't like stuff that pulls from the internet when I build and will veto something that does this (though some script does it in the GUI, but it's easy to avoid it). This is a good way to get pwned.

As for the gtest stuff overriding shared libs setting, is this something that can be done locally (ie, save CFLAGS, let it do its thing, reset CFLAGS) ? I don't really care for shared libs either to be honest, though it's nice for not having to relink the world when debugging.


## tdprime | 2017-02-08T19:01:17+00:00
Only a moron would suggest we suck in stuff automatically over the internet.

What was suggested and being worked on is a means of protecting the monero build from the gtest build.

Do you have anything constructive to contribute here?

> On Feb 8, 2017, at 12:22 PM, moneromooo-monero <notifications@github.com> wrote:
> 
> I don't like stuff that pulls from the internet when I build and will veto something that does this (though some script does it in the GUI, but it's easy to avoid it). This is a good way to get pwned.
> 
> 



## moneromooo-monero | 2017-02-08T21:39:42+00:00
That's how I interpreted "ensure that we always build against the latest google test libraries, which is nice (so long as we have an internet connection at build time)", maybe this was incorrect. I have not looked at the code in particular.

As for constructive contribution, the two paragraphs in my previous post were. I have nothing to add right now.

## ghost | 2017-02-08T22:50:49+00:00
@tdprime Wow that's a pretty insulting response to both myself and one of our most experienced developers, in place of a simple factual correction. 

Could you please explain why you chose the words and tone that you did?

## tdprime | 2017-02-08T23:19:05+00:00
I will agree that there was an insulting tone taken.  Threatening “veto” is nothing short of a personal attack.  It is childish and it is bullying.

We have people volunteering there time here.  I bring 30 years of experience with me.  I am sure there are others here who bring more.

When I started looking at this project, the stuff did not build.  It took days of analysis and fiddling to learn how the project is organized.  The point is, I put in the effort and have been making real contributions.  I try some changes, and submit them for public review.  Each iteration, things get better and better.

All I heard was knee-jerk shouting.  Fear without understanding.  Anger without compassion.

No advice.  No questions.  Just a whiny child.

When you see a bully, call him out.


> On Feb 8, 2017, at 5:50 PM, Nano Akron <notifications@github.com> wrote:
> 
> @tdprime <https://github.com/tdprime> Wow that's a pretty insulting response to both myself and one of our most experienced developers, in place of a simple factual correction.
> 
> Could you please explain why you chose the words and tone that you did?
> 
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub <https://github.com/monero-project/monero/issues/1688#issuecomment-278488497>, or mute the thread <https://github.com/notifications/unsubscribe-auth/AYMjtuxVQjyhc3097cgU3t_Egj-gMdVEks5rakbMgaJpZM4L3qz6>.
> 



## ghost | 2017-02-09T07:22:13+00:00
A general statement about what warrants a veto != a personal attack, and the fact that you perceived it as such is a potentially concerning indicator.

Then you make the accusation (a generalisation) about 'knee jerk shouting' when none is plain to see.

Finally you parade your 'years of experience' as a medal, in a community of peers who just contribute where they can, no matter how much or how little experience they have. We have no need of such virtue signalling here - the code can speak for itself.

I strongly advise you that humility is a virtue. There are no rewards here, no showers of praise, just an internal drive to see a project improve. Expect that opinions and code will be criticised, and that text will remain an imperfect medium of communication. Your contributions will be accepted on their own merits, and we expect you to criticise the contributions of others as well, albeit in a good-natured manner.

## kenshi84 | 2017-02-09T08:42:00+00:00
Just FYI, my motivation to make PR #1626 was to accomplish debug build on Mac. The reason for the debug build failing turned out to be the fact that the debug build somehow activates the shared lib building and the mutual dependency between libblockchain_db/libringct and libcryptonote_core prevents them from being successfully built due to link errors with missing symbols.

If the shared libs building is to be discouraged in general, that PR may not be able to justify itself very well (although I tend to like the resulting straightened dependency relationship after splitting libcryptonote_core).

## moneromooo-monero | 2017-02-09T09:10:44+00:00
I think you'll find most projects have reviewers. I know a lot of stuff gets merged to Monero which isn't totally ready or could be done nicer, etc, but there's still stuff I won't accept. I'm not sure why you're trying to be insulting over this, but if this starts to go over a sane grief/benefit ratio, it is not going to be helpful.

In short: if you want to help, help without the attitude. Otherwise, plenty of other projects around.

# Action History
- Created by: tdprime | 2017-02-05T23:32:45+00:00
- Closed at: 2017-02-12T21:20:02+00:00
