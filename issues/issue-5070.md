---
title: Integrate with I2P-Java via libsam3
source_url: https://github.com/monero-project/monero/issues/5070
author: knaccc
assignees: []
labels:
- invalid
created_at: '2019-01-13T16:01:41+00:00'
updated_at: '2019-08-27T16:17:55+00:00'
type: issue
status: closed
closed_at: '2019-08-27T16:17:55+00:00'
---

# Original Description
I2P-Java is a relatively mature project with active developers.

A few years ago, it would have been unthinkable to have to ask people to separately install a 200 MB JVM on their machine before being able to run a Monero wallet that wanted to route connections through I2P-Java.

Things have changed since then. Java 9 implemented modularization to allow zero dependency native apps with small footprints. This brings the footprint of an app with a bundled JVM down to as low as 22 MB (11 MB with compression). The end user will have no idea they're running a JVM, and no JVM will be installed. This means no conflicts with any other JVMs they may previously have installed. Even better, we now have the open source (GPLv2) OpenJDK. See https://steveperkins.com/using-java-9-modularization-to-ship-zero-dependency-native-apps/

zab_, one of the I2P developers, has noted in the Monero reddit that we could interface with I2P-Java via the SAM library https://github.com/i2p/libsam3 or via the lower level  I2CP protocol https://geti2p.net/en/docs/protocol/i2cp (zab_'s comment [here](https://www.reddit.com/r/Monero/comments/aeizzp/never_bring_a_knife_to_a_gun_fight_bring_popcorn/edtboid/)).

# Discussion History
## fluffypony | 2019-01-13T16:35:54+00:00
If we're convinced that i2p-java is going to continue then why not. We have a responsibility to maximise the protection that users have available to them.

## knaccc | 2019-01-14T03:13:45+00:00
Here are some first thoughts at how this would work, as a starting point for comment by the Monero and I2P communities:

I2P provides a C library called [libsam3](https://github.com/i2p/libsam3), which makes it easy for the Monero daemon to communicate with a SAMBridge instance via tcp sockets.

SAM stands for Simple Anonymous Messaging. SAMBridge is Java code that will translate between the high level SAM protocol and the lower level I2CP "I2P Client Protocol". Therefore the Monero daemon will open tcp sockets to SAMBridge with libsam3 and communicate using the SAM protocol, and SAMBridge will open a single tcp socket to the I2P router and communicate using the I2CP protocol.

Advanced Monero daemon users should be given the option to connect via SAM to their own full I2P router installation. This will be a useful feature during development, because it means development can begin prior to the existence of an embedded I2P-Java router.

Embedded I2P-Java/SAMBridge instances

The Monero daemon will need to launch a JVM that will run the I2P Java router and a SAMBridge instance. 

A tiny Java project will exist that will bundle the following I2P Java libraries: i2p.jar, router.jar, streaming.jar, mstreaming.jar and jbigi.jar.

This Java project will then have a main Java class that will do something very close to the following code, which was provided at https://geti2p.net/en/docs/applications/embedding

```
	Properties p = new Properties();
	p.addProperty("i2p.dir.base", baseDir);
	p.addProperty("i2p.dir.config", configDir);
	p.addProperty("i2np.inboundKBytesPerSecond", "50");
	p.addProperty("i2np.outboundKBytesPerSecond", "50");
	p.addProperty("router.sharePercentage", "80");
	p.addProperty("foo", "bar");
	Router r = new Router(p);
	r.setKillVMOnEnd(false);
	r.runRouter();
```

In addition, the code will instantiate and run an instance of the Java SAMBridge class. Both the I2P-Java router and the SAMBridge instance will be launched by the same Java code running inside the same JVM process.

The Java project will be built into per-OS executables using the jlink tool. This tool will, for each OS, produce a directory tree that will contain both the compiled Java code and specific JVM executables for each OS. From one build environment OS, executables can be generated for all available OSs by the jlink tool.

The jlink tool will use a module-info.java file to build these executables such that only the necessary parts of the JVM are included. This will ensure the size of the executables is kept to a minimum.

These per-OS joint Embedded I2P-Java/SAMBridge executables will be bundled with Monero builds, and used to send traffic via I2P.

End users will have no idea they are running Java code or using a JVM. The Monero daemon will handle the startup and shutdown of this Embedded I2P-Java/SAMBridge process.

## zlatinb | 2019-01-14T04:14:55+00:00
Hi, zab here.  You pretty much have everything figured out as far as integrating goes.  The only issues I see are that using modules and jlink ties us to Java 9+, and while Java 11 is already out and is LTS, the default download for Windows on www.java.com is still 8, which means Oracle doesn't feel confident enough yet to bump it to 11.

Currently the I2P code is Java 7 compliant.  The nasty bit about modules and jlink is that they are defined in .java files, which means we either force 9+ code compatibility or employ some very creative exclusion filters to make sure our code still builds on 7.

This is based on very preliminary research because I learned about jlink same time as you did :)  So it's more of a strategic decision whether and how to modularise; Monero certainly doesn't need a full I2P distribution (that includes email, torrent client and a kitchen sink).  

To alleviate @fluffypony 's concern Java I2P is healthier than ever and definitely going to continue.  We  even have a paid program to support full-time developers and are currently employing 3 core developers full-time and 2 part-time, in addition to some PR and design folk.

## anonimal | 2019-01-14T09:18:56+00:00
>I2P-Java is a relatively mature project with active developers.

@knaccc s/developers/developer/. And they're still technically in beta; have been for ~15 years.

>If we're convinced that i2p-java is going to continue then why not

@fluffypony because your whole platform **for years**, even before Kovri, was to **not** use Java I2P. In fact, you were the first and only person to shoot down a socket based API; making everyone wait for years as a result. In fact, you were the deciding factor at that time but flaked out; leaving me to clean up your mess. And here you are now, as you conveniently appear to sway opinion on yet another decision that is beyond your technical grasping.

But, aside from that, the real reason is because [there is already a better solution than hooking into java I2P directly](https://gitlab.com/sekreta/sekreta/blob/master/README.md) from monero. With that said, Monero is a money project, not an anonymity project, so I don't expect most here to understand what's happening aside from the few devs who have, fortunately, reached-out and made contact. Besides, you'll certainly want "something" "now", so; have at it.

>We have a responsibility to maximise the protection that users have available to them.

@fluffypony "We"? Who do you think you are? You're not an anonymity developer; you're barely technically literate. If you were truly responsible, then [this wouldn't have happened](https://forum.getmonero.org/9/work-in-progress/86967/anonimal-s-kovri-full-time-development-funding-thread?page=&noscroll=1#post-96613). If you were truly responsible, then you would've already engaged our development in `#sekreta-dev`.

Besides; this entire issue has already been deprecated by [Sekreta](https://gitlab.com/sekreta/sekreta/blob/master/README.md). Single-system solutions are a thing of the past. While Monero enjoys the past, other privacy coins will lead the future. I've already pointed out [that danger](https://www.coindesk.com/this-binance-backed-crypto-startup-wants-to-anonymize-everything) in my post.

My only advice now is to not get too attached to this hack of a request (#5070). Also, throw salt on blockchain developers who moonlight as network anonymity developers since the technology involved is not the same.

>To alleviate @fluffypony 's concern Java I2P is healthier than ever and definitely going to continue. We even have a paid program to support full-time developers and are currently employing 3 core developers full-time and 2 part-time, in addition to some PR and design folk.

@zlatinb So, there's reality, which is exposed via monotone's/git's log, and there is what you say, which is more of an illusive reality. Java I2P logs look no different than how they've looked over the years with the exception of Meeh doing some OS X work in 2018 (good to see he's back though, he MIA'd for a long time). Aside from him, there are almost no other authors besides zzz for 2018/2019 (and those other authors have very few commits); and zzz's always been the lead/full-time dev since jrandom left.

## fluffypony | 2019-01-14T12:00:19+00:00
> @fluffypony because your whole platform **for years**, even before Kovri, was to **not** use Java I2P.

Yes, because it would require installing Java, which adds a Java dependency to Monero. See, for instance, [this post of mine from July, 2015](https://bitcointalk.org/index.php?topic=583449.msg11915070#msg11915070). @knaccc is suggesting that the modularisation in Java 9 makes it self-contained, and thus doesn't install Java.

## apxs94 | 2019-01-14T16:16:09+00:00
> Besides; this entire issue has already been deprecated by [Sekreta](https://gitlab.com/sekreta/sekreta/blob/master/README.md). Single-system solutions are a thing of the past. While Monero enjoys the past, other privacy coins will lead the future. I've already pointed out [that danger](https://www.coindesk.com/this-binance-backed-crypto-startup-wants-to-anonymize-everything) in my post.

It's important to remember that currently Monero runs without Kovri/i2p/Sekreta/Tor - it simply runs over clearnet - and this proposal would at least improve the status quo.

> @fluffypony "We"? Who do you think you are? You're not an anonymity developer; you're barely technically literate. If you were truly responsible, then this wouldn't have happened.

@anonimal  No need to resort to ad hominem attacks here. The beauty of a community effort is that we all have strengths and weaknesses.

Let your work speak for itself, and rational people will adopt it. Attacking community members will only distract people from your hard work.

## x1ddos | 2019-01-14T17:53:45+00:00
Why embed anything at all at any point instead of keep communicating over an ipc such as sockets? 

Maybe a better investment would be a monero binary which is ipc-agnostic to kovri, i2p-java, tor or sekreta. Then everyone can run whay they choose without dead dependencies.

Embedding seems like a too tight coupling for unclear benefits compared to ipc.

## knaccc | 2019-01-14T19:35:25+00:00
@zlatinb Thanks for taking the time to comment!

> using modules and jlink ties us to Java 9+

I've figured out how to automatically convert your existing JARs into modules. No code modifications will be necessary to I2P's repository.

> While Java 11 is already out and is LTS, the default download for Windows on [www.java.com](http://www.java.com) is still 8, which means Oracle doesn't feel confident enough yet to bump it to 11.

I know a lot of people that rely heavily on Java 11 in production. so I have a good feeling about it.

> Currently the I2P code is Java 7 compliant. The nasty bit about modules and jlink is that they are defined in .java files, which means we either force 9+ code compatibility or employ some very creative exclusion filters to make sure our code still builds on 7.

As above, you won't have to worry about this. Your Java 7 JARs are easily turned into modules and run perfectly on Java 11.

> To alleviate @fluffypony 's concern Java I2P is healthier than ever and definitely going to continue. We even have a paid program to support full-time developers and are currently employing 3 core developers full-time and 2 part-time, in addition to some PR and design folk.

That's wonderful to hear!

## knaccc | 2019-01-14T19:37:58+00:00
I've just released an embedded I2P Java router with SAM, that would be suitable for embedding into Monero.

The GitHub repo is here: https://github.com/knaccc/embedded-i2p-java-router-with-sam

It works by taking existing I2P JARs and turning them into modules. These are then used with jlink to produce an executable with a minimal JVM.

@zlatinb I'd be very interested in your thoughts, in particular on two things:

1. The way that the I2P router and the SAMBridge are launched here: https://github.com/knaccc/embedded-i2p-java-router-with-sam/blob/master/src/org/getmonero/i2p/embedded/Main.java

2. How you would recommend we go about figuring out what a minimal I2P "base dir" would be to bundle?

Thanks!

## fluffypony | 2019-01-14T19:42:26+00:00
> Why embed anything at all at any point instead of keep communicating over an ipc such as sockets?
> 
> Maybe a better investment would be a monero binary which is ipc-agnostic to kovri, i2p-java, tor or sekreta. Then everyone can run whay they choose without dead dependencies.
> 
> Embedding seems like a too tight coupling for unclear benefits compared to ipc.

Just to be clear, when we say embedding we actually mean bundling, but we've gotten so used to saying "embedding". Comms would absolutely go over RPC via TCP, or over IPC.

## zlatinb | 2019-01-14T19:52:59+00:00
@knaccc I'm impressed, well done!  Your approach to converting jars into modules will come in handy because honestly we can't wait to get rid of our dependency on Java as well.  Now to your questions:

> The way that the I2P router and the SAMBridge are launched here: https://github.com/knaccc/embedded-i2p-java-router-with-sam/blob/master/src/org/getmonero/i2p/embedded/Main.java

Usually the SAM bridge is launched via a "clients.config" file, but it might work the way you've done it too.  What I recommend is you wait until the Router state machine reaches RUNNING state before starting the SAM bridge.  Poke around the code to see exactly how to get a reference to it.

> How you would recommend we go about figuring out what a minimal I2P "base dir" would be to bundle?

Trial and Error :) more specifically write a small Hello World application that uses the SAM library, enable full logging in the router and hammer it until it works.  I *think* you don't really need to bundle anything to get it to bootstrap and join the I2P network.  If you're comfortable with Python here is a nice guide - https://geti2p.net/en/blog/post/2018/10/23/application-development-basics

## knaccc | 2019-01-14T19:58:43+00:00
@zlatinb Thanks, I'll make that update to the code.

Btw, I've tested the executable built with this project by setting up a Node.js client and server to talk to each other via it (using https://github.com/redhog/node-i2p). Everything seems to work great!

## knaccc | 2019-01-14T21:31:05+00:00
Btw the total executable ended up as **36**MB (37281943 bytes).

It was reduced to **19**MB (19764972 bytes) when compressed with `xz`.

## jtgrassie | 2019-01-15T02:26:25+00:00
@knaccc firstly, this is great.

At a high-level, are you envisioning i2p being used just for tx broadcasting (like @vtnerd's Tor PR #4988)?

## Gingeropolous | 2019-01-15T03:45:23+00:00
@jtgrassie , 

> At a high-level, are you envisioning i2p being used just for tx broadcasting 

I think that has been the idea from the start, primarily because the latency of the i2p network and the size of the monero blocks. Though who knows - if our fluffyblocks is smart enough, block relay has effectively the same cost as tx relay. Though knaccc may have a different idea.

In general, does this bundling and modularization and lack of dependencies change the amount of resources used by java i2p? I just checked on my node server and currently java is using 50% cpu resources ... and now 64%... back to 50%... I'm just worried that bundling this with monero, and assuming its an always on situation in order to provide the most privacy, is going to create another case of people not using the monero core software because its resource intensive. 

"What the heck is using 50% of my CPU? My superbloated javascript webpages don't load nearly as fast as they used to! Oh, its the monero software. DELETED."

Because of this resource use (and perhaps independent of it), users will probably start and stop The Monero Software (which now has i2p), and from what I've gathered its best to keep the router running so your tunnels get all interconnected and integrated. 

Of course the flip side of this is that bundling java-i2p is better than nothing, and ultimately if the software is designed for some extreme user apathy or we wait for perfect optimizations, then we'll have a .... i dunno. Best getting in the way of good situation. 

## zlatinb | 2019-01-15T04:19:30+00:00
> does this bundling and modularization and lack of dependencies change the amount of resources used by java i2p?

Not really, you are still running a JVM with it's bells and whistles (JIT, GC, etc.).  

The main source of CPU usage are the crypto operations, which reminds me - @knaccc it is important to add jbigi.jar and the NativeBigInteger libraries to the bundle, otherwise performance will suffer.. a lot!

The number of crypto operations is proportional to the amount of I2P traffic that is routed and that can be limited through configuration, so it's a matter of choosing sane defaults.  

## anonimal | 2019-01-15T11:12:23+00:00
Since no one in this thread has developed I2P technology longer than I, allow me to drop some important information:

Note: for those who don't know; NTCP is the encrypted TCP transport layer for I2P. This discussion was regarding the new 2nd version. This is a mission-critical protocol, a base-layer protocol that ferries your layered messages.

```
#kovri-dev

2018-03-27 19:57:37     +zzz    [16:39:04] anonimal, Java I2P is going to pick up the pace on some long-dormant proposals, starting with NTCP 2 (proposal 111), would you or somebody else in kovri/monero like to
 participate?
2018-03-27 19:57:37     +i2p-relay      [16:44:41] {-oneiric_} zzz: that sounds interesting, i would like to participate
2018-03-27 19:57:37     +i2p-relay      [16:45:46] {-oneiric_} are junior-level developers welcome to join in?
2018-03-27 19:57:37     +zzz    [16:46:04] super, please review the proposal, and the long zzz.i2p thread linked on it
2018-03-27 19:57:37     +i2p-relay      [16:46:24] {-oneiric_} will do :)
2018-03-27 19:57:37     +zzz    [16:46:32] anybody is, of course
2018-03-27 19:57:37     +i2p-relay      [17:42:31] {-anonimal} zzz has anything changed since the currently published 111-ntcp-2.rst ?
2018-03-27 19:57:37     +zzz    [17:51:46] anonimal, yes, see the zzz.i2p thread for followups since then, including a possible rewrite in the Noise framework
2018-03-27 19:57:37     +zzz    [17:52:05] it's unclear if we will do that or not
2018-03-27 19:57:37     +i2p-relay      [17:55:13] {-anonimal} There's not clearnet collaboration? Is everything on zzz.i2p?
2018-03-27 19:57:37     +zzz    [17:55:49] well, there's no activity now
2018-03-27 19:57:37     +zzz    [17:56:06] we could perhaps move it to our new forum
2018-03-27 20:08:41     +i2p-relay      {-oneiric_} To any and all interested: NTCP2 design discussion in #ntcp2 on Irc2P
2018-03-27 20:10:04     &anonimal       If it's not relayed to freenode, if it's not made more public, it's not a serious discussion.
2018-03-27 20:11:14     &anonimal       zzz: monero has brilliant mathematicians but not everyone is going to fire up a router just to check a thread or use IRC.
2018-03-27 20:12:02     +zzz    anonimal, it's serious as a heart attack. If you're not happy with oneiric as your representative, let me know, otherwise we are proceeding
2018-03-27 20:12:47     +zzz    There's two proposals, one from last July (prop 111) and one from November (the Noise one in the zzz.i2p thread). We're working on a new one
2018-03-27 20:13:07     +zzz    nothing's been "fleshed out more" yet. That's what we're doing now.
2018-03-27 20:13:44     +zzz    The results will be made public in the form of updates to proposal 111, starting next week
2018-03-27 20:13:35     &anonimal       Where are the mailing list discussion? Where are the public clearnet discussions?
2018-03-27 20:13:46     +zzz    I invited your project to participate and oneiric is filling that role.
2018-03-27 20:14:21     &anonimal       There are 8+ billion humans on the planet. Must discussions be so limited to such finite channels and groups?
2018-03-27 20:14:40     +zzz    There is no mailing list. There is no clearnet discussion. If that means it is illegitimate in your eyes, I'm sorry you feel that way
2018-03-27 20:14:41     &anonimal       Has this at least made it to the modercrypto mailing list?
2018-03-27 20:15:12     &anonimal       No one said illegitimate.
2018-03-27 20:15:21     +zzz    Not familiar with that mailing list, sorry
2018-03-27 20:15:31     &anonimal       Technology can only evolve so much if it doesn't break from the shells it creates.
2018-03-27 20:16:28     oneiric right, I wasn't aware of being a representative of anything
2018-03-27 20:16:41     oneiric thought I was just participating in the discussion
2018-03-27 20:17:19     +zzz    I assumed you were representing kovri's interests. That's what I asked for, a representative.
2018-03-27 20:17:39     oneiric oh, no, I'm definitely not qualified for that role
2018-03-27 20:22:25     &anonimal       Who are the people working on this proposal, zzz?
2018-03-27 20:22:46     +zzz    me, psi, oneiric
2018-03-27 20:23:05     +zzz    see also summary at end of the NTCP2 thread on zzz.i2p
2018-03-27 20:23:07     &anonimal       What about str4d?
2018-03-27 20:23:45     +zzz    he doesn't have time. But we're using his Noise draft from November as an input
2018-03-27 20:24:36     +zzz    he may participate further, we'll see
2018-03-27 20:25:39     &anonimal       Wow, ok. The proposal needs more eyes and needs to be more public.
2018-03-27 20:25:42     &anonimal       I'll be glad to look at it.
2018-03-27 20:25:45     &anonimal       I'll be glad to contribute.
2018-03-27 20:25:51     &anonimal       I'll be glad to have more people get involved.
2018-03-27 20:26:07     &anonimal       The collaboration can improve with a more public approach though.
2018-03-27 20:26:20     &anonimal       And I only have so much time as I'm balancing a lot of different things on any given day.
2018-03-27 20:26:53     +zzz    latest 111 proposal been up there since july on our website. Noise draft been on zzz.i2p since November. Both public. New draft versions will be posted as updates to 111 on our website
2018-03-27 20:27:36     +zzz    discussions are in #ntcp2 and periodic video calls at least once a week.
2018-03-27 20:28:01     +zzz    we'd like to keep the video calls to one representative from each project
2018-03-27 20:28:13     &anonimal       But where do people submit pull requests / patches?
2018-03-27 20:28:32     +i2p-relay      {-moneromooo} What is the video supposed to show ?
2018-03-27 20:28:45     +zzz    we aren't using a pull/patch process
2018-03-27 20:28:52     &anonimal       Where?
2018-03-27 20:29:15     &anonimal       The tracker that took 2 years for my website doc error requests to be resolved? Or github?
2018-03-27 20:30:06     +zzz    the process is we're having meetings and then I'm making changes to what's on the website. That's the entire process.
2018-03-27 20:30:47     +zzz    there are no pull requests. there are no patches.
2018-03-27 20:31:58     +zzz    the meeting-and-update process we are using is working fine so far, and your maybe-representative hasn't complained about it either.
```

Let me repeat:

```
2018-03-27 20:11:14     &anonimal       zzz: monero has brilliant mathematicians but not everyone is going to fire up a router just to check a thread or use IRC.
2018-03-27 20:14:40     +zzz    There is no mailing list. There is no clearnet discussion. If that means it is illegitimate in your eyes, I'm sorry you feel that way
2018-03-27 20:30:47     +zzz    there are no pull requests. there are no patches.
2018-03-27 20:31:58     +zzz    the meeting-and-update process we are using is working fine so far, and your maybe-representative hasn't complained about it either.
```

Firstly, that's false: he has complained - as have many people over the years about how zzz handles (or doesn't handle) the project. From everything to the above to refusing to use git - and more. There are lots of IRC dumps to prove this. **Project decisions affect code decisions**: don't forget that.

Secondly, and **more importantly**; someone who is opposed to collaborating with the vast majority of scientists and researchers among the global human population (people that only live on clearnet) thinks that this approach is "working fine so far".

...This is Java I2P, folks. This is zzz, the lead and only developer of java I2P, and java I2P contributor for at least 13 years. Things have not changed in this area. This attitude has not changed over the years.

Don't believe me? Feel free to ask other developers such as psi about I2P development. You can find him working on [LokiNet](https://github.com/loki-project/loki-network). psi had been involved with the java I2P project even longer than I (yes, I also contributed to java I2P), so I'm sure he can provide another perspective. Or even ask str4d for that matter, as he is working on [Ire](https://github.com/str4d/ire) among other things. Sidenote: [Sekreta](https://gitlab.com/sekreta/sekreta/blob/master/README.md) will support LokiNet and Ire (see list of all supported networks).

**But, how is this an issue now? How does this affect Monero?**

Now, in January 2019, it's been almost a year later and there's still no audit of NTCP2. No official 3rd party review of *anything* related to NTCP2 outside of Noise (which is a completely separate component, and which received its own audit long ago). In March of 2018, java I2P's budget was around ~4 million USD in cryptocurrency and not a single penny was spent for a formal audit. Wrap that around your head. Either java I2P is still a lost cause of a project or their intentions behind such a lack of responsible development should be considered questionable at best.

This is not an isolated incident. This type of history has only been repeating throughout every aspect of java I2P development - year after year after year after year. And now, a few Monero contributors want to integrate technology that they know very little about - and that's a big problem for Monero.

So, when flakeypony pretends to not know this, despite using the *exact* reasons above (shall I provide logs?) as a catalyst to **not** use java I2P (specifically, zzz), you must question his legitimacy not only as an honest person but as any sort of anonymity consultant; as he has repeatedly proven himself to be lackluster in both of these areas.

In other words, it's time to get with the program. Archaic tools are for archaic problems. It's laughable that #5070 is even a proposal but I can smell the desperation in the air because of the 2018 bear.

Monero is better-off using a SOCKS proxy at this point, at least until Sekreta is integrated. Otherwise, deciding parties will do Monero users a massive disservice by enforcing a single implementation / single-network per-channel solution. At least with a temporary "only SOCKS proxy" solution, you'll have less blood on your hands (everyone can still use any existing I2P implementation or network of their choice so long as the implementation of choice support a SOCKS proxy).

Lastly, allowing anything Java to infiltrate the Monero implementation is literally [the writing on the wall](https://en.wikipedia.org/wiki/Belshazzar%27s_feast) for Monero innovation. I'm so sad to see it end this way; especially since I'm one of the few who have dedicated their lives to building Monero Project since 2015.

## zlatinb | 2019-01-15T11:54:35+00:00
Some fact-checking here:
> no one in this thread has developed I2P technology longer than I

Pull the monotone source and search for "zab" and "zab2".  If you started in 2015 I got you beat by 3 years.

> Feel free to ask other developers such as psi about I2P development

Psi aka Jeff aka https://github.com/majestrate has already made his opinion known here https://i2p.rocks/blog/kovri-and-the-curious-case-of-code-rot-part-2.html and here https://i2p.rocks/blog/kovri-and-the-curious-case-of-code-rot-part-3.html but do ask him.

> allowing anything Java to infiltrate the Monero implementation

If Monero hates Java that much, i2pd supports the SAM protocol as well.  I don't know C++ so I can't vouch for their code, but orignal had no problem collaborating with us on NTCP2.

## knaccc | 2019-01-15T14:39:10+00:00
> At a high-level, are you envisioning i2p being used just for tx broadcasting (like @vtnerd's Tor PR #4988)?

I have no opinion on this. I am also not a C/C++ person, so it'd be completely up to whoever takes on the baton from here to decide how this might work. It'd be nice to be able to give people the option to hide all of their Monero related traffic.

> I just checked on my node server and currently java is using 50% cpu resources ... and now 64%... back to 50%

> it is important to add jbigi.jar and the NativeBigInteger libraries to the bundle, otherwise performance will suffer.. a lot!

I did not include the jbigi.jar for this first iteration, for simplicity. Some of the other CPU drain could be because the node is starting for the first time. As @zlatinb points out, calling the native crypto libraries by including jbigi.jar in the future will result in a big crypto speedup when integrated.

I've read that the RSA/ElGamal crypto is also much slower than the newer EC crypto in NTCP2. Perhaps someone can comment on this.

> Lastly, allowing anything Java to infiltrate the Monero implementation is literally the writing on the wall for Monero innovation

I'm a big proponent of ending up with a well written, small footprint, security audited C/C++ I2P router with multiple collaborators from both within and outside the Monero community.

The only reason I suggested Java-I2P in the meanwhile is because that dream scenario seems to be at least 1-2 years away. 





## knaccc | 2019-01-15T14:53:57+00:00
> it is important to add jbigi.jar and the NativeBigInteger libraries to the bundle, otherwise performance will suffer.. a lot!

@zlatinb I wasn't exactly sure what files to include to make this work, other than the jar file.

Am I correct in thinking that the I2P-Java project is currently only providing native builds of the bigint libraries for Linux, and not for Win/MacOS?

On the topic of the I2P base directory, it looks like it's possible to leave it completely empty. However, there are certificate checking errors, and so it seems like it would be best to include the certificates, hosts, blocklist and geoip content. Do you agree? How necessary do you think each of these are? I was also struggling to figure out where this content was from, since it's not in your Github repository (this data dir content is present in the Ubuntu distribution of I2P-Java).

## zlatinb | 2019-01-15T15:42:19+00:00
> Am I correct in thinking that the I2P-Java project is currently only providing native builds of the bigint libraries for Linux, and not for Win/MacOS?

There are libraries for Linux, Windows, MacOS and FreeBSD.  The full list is here https://github.com/i2p/i2p.i2p/tree/master/installer/lib/jbigi .  The libraries that start with "jbigi" are the actual implementations for platform*CPU architecture.  Those that start with "jcpuid" are used to identify the CPU architecture so that the optimal implementation library can be loaded.  Looking at router and wrapper logs during startup is your best bet for identifying the correct bundling.

* Certificates - you need at least the "certificates/reseed" directory in order to bootstrap into the network, but it won't hurt to include all the certificates from "installer/resources/certificates"
* blocklist - sure nice to have, it's in "installer/resources/blocklist.txt"
* geoip - this is used for identifying "bad" countries where running an I2P router can put one at risk; the router behaves differently if it detects that it's running in a "bad" country.  Look at the top-level build.xml file for how geoip gets packaged.

## knaccc | 2019-01-15T19:39:09+00:00
@Gingeropolous Please could you check your ~/.i2p/wrapper.log file, and see if it contains the lines:

```
INFO: Native CPUID library jcpuid-x86-linux loaded from file
INFO: Locally optimized native BigInteger library loaded from file
```
On my laptop, the I2P Java process is rarely using more than 1-2% CPU, so I'm not sure why this is happening for you. Are you running on the same machine where you installed the Ubuntu I2P package?

It looks like when you run this embedded I2P project, if you run it on the same machine where you installed the Ubuntu I2P package, then it will be using native BigInteger operations.

This is because the NativeBigInteger class that calls the native code is already contained in the i2p.jar file that this project uses, and you'll already have the libjbigi.so native library installed in your /usr/lib/jni directory.


## knaccc | 2019-01-16T08:17:37+00:00
I've just released a new version that runs on Linux, and from Linux will build the Linux, MacOS and Windows zero-dependency distributions. Beware that the scripts will need to download all 3 JDKs, totalling hundreds of megabytes.

Unlike the previous version of this project, you will not need to pre-install Linux packages for Java, the Ant build tool or I2P in order to build the zero-dependency router distributions.

The native BigInteger libraries are now included in distributions for all platforms. You can check if the native libraries are being used by launching the router and checking the contents of the i2p.config/wrapper.log log file.

The final zero-dependency distribution sizes are as follows:

OS | Uncompressed size (MB) | xz Compressed size (MB)
------------ | ------------- | -------------
Linux | 41.6 | 22.5
MacOS | 29.5 | 17.5
Windows | 33.6 | 20.1

## Gingeropolous | 2019-01-16T15:12:13+00:00
yeah, im running the ubuntu i2p package @knaccc , those were the numbers I was talking about. Does the version you are working with end up using less resources? I might try out your version... but then i gotta migrate my tunnel configurations etc... 

## knaccc | 2019-01-16T17:51:03+00:00
This project has been renamed I2P-zero, because it means less typing for me and less confusion when discussing it. 

New github repo URL: https://github.com/knaccc/i2p-zero

## jtgrassie | 2019-01-16T18:03:35+00:00
With a couple of build script tweaks I got this building and running on macos. Uses hardly any resources! Nice work @knaccc.

## zlatinb | 2019-01-16T18:35:34+00:00
Few notes
@knaccc : 
* you should include the licenses for proper license-compliance.  This is a bit tricky because we have the (bad) habit of including library source code inside the projects.  For example, router.jar contains UPnP code from the cybergarage library so you need to include LICENSE-UPnP.txt
* you may want to have the option of checking out a specific tag from git for i2p
* I haven't looked at what launcher scripts get generated, is there an easy way to tune JVM params like -Xmx ?

@jtgrassie It takes quite some time for a new router to start contributing to the network, until that happens it won't be using pretty much any resources.

@Gingeropolous this distribution does not include i2ptunnel.jar, so it will not open any of your tunnels.

## x1ddos | 2019-01-16T19:28:14+00:00
> Just to be clear, when we say embedding we actually mean bundling, but we've gotten so used to saying "embedding". Comms would absolutely go over RPC via TCP, or over IPC.

But what if I don't want and need bundling because I'm already running my own i2p router or tor? I'd just want monero to use what I already have setup and don't bundle stuff I'll never use.

## Gingeropolous | 2019-01-16T19:45:00+00:00
> But what if I don't want and need bundling because I'm already running my own i2p router or tor? I'd just want monero to use what I already have setup and don't bundle stuff I'll never use.

Then there'd probably be a startup flag to tell the daemon to not run the bundled i2p , and compile flags to not bring it in... if i had to guess, and if i have an actual understanding of what bundling means. 

## lessless | 2019-01-16T21:26:49+00:00
Few questions here, but in the first I want to say thank you to @anonimal for being vocal with his concerns. Discussion, which raises awareness  in a such sensitive field as a privacy is always appreciated, at least from the end-user perspective. 

1. Do you guys think that it will be possible to put an i2p-bote in the bundle? That might be of help to the Monero MMS system which is currently using Bitmessage https://www.reddit.com/r/Monero/comments/a90b2b/multisig_and_monero_messaging_system_questions/ecv4rvk/

3. Does it make sense to consider integrating with the loki network which advertise itself as what would I2P look like if it would be made in 2018? It also supposed to have a messaging capabilities that would again help MMS (at least).

5. Are there any other good reasons except emotions/feelings to stay away from Sekreta? 


Peace ✌️

## Gingeropolous | 2019-01-16T21:54:33+00:00
so, I obviously don't speak for anyone but myself, but to address @lessless , 

> Are there any other good reasons except emotions/feelings to stay away from Sekreta?

I think the main thing is that it does not exist yet. 

And I've just heard about loki, but the same probably still applies. It looks like it exists, but how flush is the network?

My take on things,,, if we take the grand view of things perspective - I've always viewed Monero as a tool that uses the best available technology to achieve its ends. For example - ring signatures are not optimal. Surely, we could all dump resources into imagineering something that works better than ring signatures. But then we wouldn't have a functioning fungible cryptocurrency, because we're waiting for something to get developed etc. Hell, blockchains are not optimal. 

Same goes for the broadcast protection layer. Sekreta sounds like it would be great. Loki too. They may be more optimal.

## knaccc | 2019-01-16T22:21:29+00:00
> * you should include the licenses for proper license-compliance. 

I've now included the LICENSE.txt from the main I2P repository in the i2p.base dir in the distribution.

> * you may want to have the option of checking out a specific tag from git for i2p

It's now checking out tags/i2p-0.9.37, and this can be modified in bin/import-packages.sh

> * I haven't looked at what launcher scripts get generated, is there an easy way to tune JVM params like -Xmx ?

Yes, this and other preferences such as bandwidth usage can be tweaked in resources/launch.sh and resources/launch.bat

> But what if I don't want and need bundling because I'm already running my own i2p router?

It would be easy for Monero to detect whether there is an existing I2P router running, and for Monero to use that instead of launching a new one. You would of course have the option to not use I2P at all.

> Does it make sense to consider integrating with the loki network

In one of the Loki network talks, they mentioned that they would want Loki to run on top of I2P. If I understood what they were saying correctly, that means Loki does not duplicate I2P functionality. I don't know a lot about Loki (and I think it's at a very early stage).

> Are there any other good reasons except emotions/feelings to stay away from Sekreta?

This project is not about staying away from Kovri or Sekreta. It's about delivering something now, instead of waiting 1-2 years to see how progress on those projects develop.



## majestrate | 2019-01-16T22:28:43+00:00
I'll just chime in about really quickly

@knaccc 

>I'm a big proponent of ending up with a well written, small footprint, security audited C/C++ I2P router with multiple collaborators from both within and outside the Monero community.

That is what i2pd is effectively but given the past and current relations between monero and i2pd I highly doubt that collaboration will ever come to fruition. I am personally in charge of the SAM subsystem in i2pd and I have neglected that part very much so as of late because of my work with loki. 

>The only reason I suggested Java-I2P in the meanwhile is because that dream scenario seems to be at least 1-2 years away.

Although it would warrant an entirely separate github issue but I think it is worth mentioning that lokinet is functional and the required changes are far far less drastic vs doing i2p via sam, if there are any at all.
 
It may be 1-2 weeks away if you are going to use lokinet as I have already got the fork of monero lokid project uses (lokid) to sync blocks over our toy mixnet with basically no modifications made to the actual daemon, it may or may not need a bit of gluey parts but it should "just work" (at least in theory).

## lessless | 2019-01-16T22:33:52+00:00
thanks for the replies guys, appreciated! 

## knaccc | 2019-01-16T22:34:37+00:00
@majestrate 

> Although it would warrant an entirely separate github issue but I think it is worth mentioning that lokinet is functional and the required changes are far far less drastic vs doing i2p via sam, if there are any at all.

> It may be 1-2 weeks away if you are going to use lokinet as I have already got the fork of monero lokid project uses (lokid) to sync blocks over our toy mixnet with basically no modifications made to the actual daemon, it may or may not need a bit of gluey parts but it should "just work" (at least in theory).

@majestrate could you give us a quick overview of what Loki does please? I watched a Loki talk, where someone said that Loki may want to run on top of I2P. Can you clear up my confusion?




## lessless | 2019-01-16T23:09:19+00:00
@knaccc thanks for pointing that out. Indeed LOKI seems to be a something completely standalone, based on their own protocol 

https://loki-project.github.io/loki-docs/Lokinet/LLARP/

> Loki proposes a new routing protocol called LLARP which is designed as a hybrid between Tor and I2P to provide additional desirable properties versus any existing routing protocol.

https://github.com/loki-project/loki-network/blob/master/docs/high-level.txt

>Working on I2P has been a really big learning experience for everyone involved.
>After much deliberation I have decided to start making a "next generation" onion routing protocol.

## majestrate | 2019-01-17T13:27:45+00:00
@knaccc what @lessless said is correct.

As it is now if you don't want to integrate java into the monero stack to get i2p support, [i2pd](https://github.com/purplei2p/i2pd) is a good fit. I am not sure that will happen because of past tensions between the two projects. As it is now, i2pd has almost been entirely rewritten since kovri forked from it and the code quality is much better albeit still a bit lackluster. That being said it's maintained by people that seem to know how to handle themselves in C++ for the most part. The main part that is still the old jenky code style is the SAM subsystem which I have been maintaining. I have neglected that for some time and probably could be rewritten. That is my fault as I have promised for over a year to rewrite that subsystem but never got it all the way done, but I digress.

The UX of LLARP's onion router is such that you don't really need a glue layer to use it as it just provides an IP tunnel with a DNS server that triggers address mapping, but all that would probably warrant a separate issue.

## knaccc | 2019-01-17T17:16:26+00:00
@majestrate 

>  As it is now, i2pd has almost been entirely rewritten since kovri forked from it and the code quality is much better albeit still a bit lackluster. That being said it's maintained by people that seem to know how to handle themselves in C++ for the most part. The main part that is still the old jenky code style is the SAM subsystem which I have been maintaining. I have neglected that for some time and probably could be rewritten. That is my fault as I have promised for over a year to rewrite that subsystem but never got it all the way done, but I digress.

@majestrate Could you comment please on the funding situation regarding ongoing work on i2pd vs i2p-java, and therefore which of the two would be more likely to be maintained and improved?

Given that you were heavily involved in i2pd and are now working on Loki, does that mean that i2pd is not going to get as much attention in general going forward as i2p-java?

## zlatinb | 2019-01-17T17:29:14+00:00
@knaccc I can shed some light on the funding situation since I'm the "compensation manager" for I2P-Java.

First, i2pd is developed independently from i2p-java.  While the two teams are in close contact, they are not funded from the same pool.  

I2P-java's finances are public and available for review here https://geti2p.net/en/about/hall-of-fame 

Current balance: as of 2018-09-20
General fund: 50790,90 € and 466,822470802 BTC

As you can see we are heavily dependent on the price of Bitcoin; we've had paid full-time developers during 2018 and will continue during at least 1H 2019 regardless of the btc price.  In the worst case scenario where bitcoin goes to zero, I2P-java will go back to operating the way it has been for 14 years prior to 2018.

## x1ddos | 2019-01-17T18:13:27+00:00
>  i2pd vs i2p-java

it seems noone's mentioning kovri anymore. is it to be considered dead now? in the scope of monero project, that is. 

## knaccc | 2019-01-17T19:02:07+00:00
@zlatinb Thanks, so I2P-Java development is funded with about $1.7 million. 

In contrast, i2pd have a donation address on their web site which has received an all-time total of $1600 worth of BTC at today's prices.

Do you happen to know how well funded i2pd is, and if this $1600 figure is misleading?


## zlatinb | 2019-01-17T19:11:35+00:00
> Do you happen to know how well funded i2pd is, and if this $1600 figure is misleading?

No idea, sorry.  Other than @majestrate the following might know: "orignal", "r4sas", "l-n-s"

## paulshapiro | 2019-01-17T19:19:31+00:00
> > i2pd vs i2p-java
> 
> it seems noone's mentioning kovri anymore. is it to be considered dead now? in the scope of monero project, that is.

Definitely not. _oneiric, sean, I, and others have been discussing a modular, minimal rewrite of Kovri. Initial design document here. More progress such as architecture diagram and planning to come. Contributors welcome in #kovri-dev. https://gist.github.com/coneiric/a26ea711ed7abc7279416a7fb38a283e#file-tini2p-design.md

## majestrate | 2019-01-17T19:27:31+00:00
On Thu, Jan 17, 2019 at 07:11:46PM +0000, Zlatin Balevsky wrote:
> > Do you happen to know how well funded i2pd is, and if this $1600 figure is misleading?
> 
> No idea, sorry.  Other than @majestrate the following might know: "orignal", "r4sas", "l-n-s"

If I recall the main contention between monero and i2pd was that there was an unofficial
understanding that i2pd was going to be funded, but it ended up not being funded and was 
instead forked (as kovri).

All that is ancient history and best left as such.

> 
> -- 
> You are receiving this because you were mentioned.
> Reply to this email directly or view it on GitHub:
> https://github.com/monero-project/monero/issues/5070#issuecomment-455294089


## jtgrassie | 2019-01-18T17:28:04+00:00
@majestrate 
> ... but given the past and current relations between monero and i2pd I highly doubt that collaboration will ever come to fruition.

Is this not a bit pessimistic? There seems to be more developers engaging now.

> All that is ancient history and best left as such.

100% agree.

@paulshapiro I'd be interested to hear the pros of the tini2p approach over either using a slimmed down i2pd or using @knaccc's approach of simply packaging up the bare minimal java-i2p based stuff. 


## majestrate | 2019-01-18T18:20:31+00:00
irc logs from `#i2pd-dev`
```
2019-01-18 13:01:19     orignal_        but really I don't understand their point
2019-01-18 13:01:39     orignal_        either decide i2pd is shit and write new one from scratch
2019-01-18 13:02:20     orignal_        or "slimmed down i2pd" than don't call i2pd as "shit"
2019-01-18 13:05:18     orignal_        "Do you happen to know how well funded i2pd is, and if this $1600 figure is misleading?"
2019-01-18 13:05:21     orignal_        )))
2019-01-18 13:06:25     psi_    "i2pd is funded in part by users like you, and by [insert sponsored ads bytes here]"
2019-01-18 13:07:03     orignal_        my point is simplier, it's not his business
2019-01-18 13:07:23     psi_    heh
2019-01-18 13:07:36     psi_    i think they want to know if you'll stiff them like anonimal did
2019-01-18 13:08:32     orignal_        honeslt I don't care what they want to know
2019-01-18 13:08:51     orignal_        they have made a wrong decision in 2015
2019-01-18 13:08:53     psi_    i see, do you mind if that notion is relayed to them?
2019-01-18 13:09:13     orignal_        at the moment when built-in i2pd was ready and worked with ANC
2019-01-18 13:09:25     orignal_        up to you
2019-01-18 13:09:37     orignal_        and Spagni knew about it
2019-01-18 13:10:02     orignal_        I'm wondering if he has shared it with others
2019-01-18 13:10:21     psi_    okay
2019-01-18 13:10:54     orignal_        I suspect he didn't
2019-01-18 13:10:59     R4SAS   say just4lulz that i2pd already works with 2 coins inside i2p space
2019-01-18 13:11:01     R4SAS   )))
2019-01-18 13:11:22     R4SAS   in that topic
2019-01-18 13:11:31     orignal_        and there was anci2pd bundle for a long time
2019-01-18 13:12:04     orignal_        and https://bitbucket.org/orignal/anci2pd
2019-01-18 13:13:10     orignal_        R4SAS if I rememeber we have made anci2pd bundle by the end of 2017
2019-01-18 13:13:22     orignal_        anc + i2pd throughj the SAM
2019-01-18 13:13:30     R4SAS   yup
2019-01-18 13:13:40     orignal_        then SAM has been changed a lot for gostcoin
2019-01-18 13:13:42     psi_    i need to get those sam patches in
2019-01-18 13:13:46     orignal_        because it didn't work well
2019-01-18 13:13:53     R4SAS   it can be found at gh in anc releases
2019-01-18 13:14:05     orignal_        it's in the code
2019-01-18 13:14:19     orignal_        when we started gostcoin we have found some issue with SAM in i2pd
```
the aforementioned SAM patches for i2pd are on a branch that needs to be (non trivially) rebased atop the recent protocol improvements (namely NTCP2 and LS2).

I think that going forward you'll realistically get more done working together with us at loki using lokinet, lots of i2pd people feel really burned by the previous interactions with monero.

## coneiric | 2019-01-18T19:09:50+00:00
> I'd be interested to hear the pros of the tini2p approach over either using a slimmed down i2pd or using @knaccc's approach of simply packaging up the bare minimal java-i2p based stuff

Ideally, Monero should be agnostic to what anonymity router is being used. The more options the better.

The idea behind tini2p is to have a minimal, auditable router. One of the benefits is to implement as little of the home-rolled crypto present in legacy I2P protocols. The HMAC-MD5-128 stuff in SSU makes me cringe everytime I think about it. I would like to continue contributing to advancing I2P, and only implement the protocols with modern crypto.

However, what I'm working on, and hope to collaborate with others, is still a fair bit away from a complete audit, let alone functioning as a router. Monero users should have something that works now, and is flexible enough to support future innovation. Implementing SAM client code is fairly easy from a Monero standpoint, here is a C library: [libsam3](https://github.com/i2p/libsam3).

> Beware that the scripts will need to download all 3 JDKs, totalling hundreds of megabytes.

Yikes! That's one big reason to opt for slimmed down i2pd or tini2p. For users that have already committed to a Java environment, Java-I2P via @knaccc's module project looks awesome.

I don't think any of the routers should be "bundled" or "embedded" into Monero other than a link on the download page, or submodule branch on the repository. Something like "here are the routers Monero is compatible with, pick one (or many)". As long as the routers support SOCKS, IPC, SAM or some other common API.

> I've read that the RSA/ElGamal crypto is also much slower than the newer EC crypto in NTCP2. Perhaps someone can comment on this.

It is, much, much slower. Mostly when it comes to fresh key generation. Correct me if I'm wrong, but LS2 will partly address the need for ElGamal, like @majestrate mentioned. Here is the [LS2 proposal](https://geti2p.net/spec/proposals/123-new-netdb-entries).

[ECIES](https://geti2p.net/spec/proposals/144-ecies-x25519-aead-ratchet) using the new Noise primitives (X25519, ChaChaPoly1305) is also being proposed. It would be great to have a router option that only implemented these more secure options. At first it may come at the cost of performance if most other routers aren't updated, but it also supplies motivation to move to the new tech. Here is a link to the new [crypto proposals](https://geti2p.net/spec/proposals/142-new-crypto-template).

## knaccc | 2019-01-18T21:44:44+00:00
> > Beware that the scripts will need to download all 3 JDKs, totalling hundreds of megabytes.
> 
> Yikes! That's one big reason to opt for slimmed down i2pd or tini2p. For users that have already committed to a Java environment, Java-I2P via @knaccc's module project looks awesome.

Just in case it's not clear, these JDK downloads are only required on the occasions that you want to build a new I2P-zero release. 

Monero devs will not be building I2P-zero releases when they are developing Monero, just like they won't be recompiling Linux when they are developing Monero. Once every few months, when there is a new I2P-Java release, someone trusted will run the I2P-zero script and build a new I2P-zero release, and everyone else will use those slimmed down 30-40MB releases for development and deployment.

> I don't think any of the routers should be "bundled" or "embedded" into Monero other than a link on the download page, or submodule branch on the repository. 

Why would we want to make people jump through hoops to use a network privacy layer?

## knaccc | 2019-01-18T21:54:58+00:00
> 2019-01-18 13:08:32     orignal_        honeslt I don't care what they want to know
> 2019-01-18 13:08:51     orignal_        they have made a wrong decision in 2015

I don't know what happened, and I don't really want to know, but wow there is a lot of bad blood between Monero and i2pd.

Since they're separate teams, I hope this bad blood doesn't extend to the I2P-Java team.

## JustFranz | 2019-01-19T03:15:46+00:00
Hello, a few questions. My knowledge of Tor and networks like it is very very basic and flawed (brace yourself). What is this privacy overlay network supposed to do for Monero?

Hide the originating node for a specific transaction?

Hide the existence of a Monero node?

What parts of the network traffic of a Monero node will go through this network, just the "mempool" additions?

What about wallets communicating with remote nodes? Do wallets communicate with a "hidden service" of sorts? Or do those transactions go over the regular internet? 

If over regular internet, how are those communications encrypted? Are the different packets going between light wallets and full nodes distinguishable or uniform?

Will each full node be a  "hidden service"?

If you have an IP hosting a hidden service also send corresponding traffic over the regular internet, is that good/bad/neutral for the security of this network?

Dandelion protocol, inferior or can it be used in unison with this network to improve security or will it just be not needed?



## SamsungGalaxyPlayer | 2019-01-19T04:01:22+00:00
> Hide the originating node for a specific transaction?

Yes, this is the primary goal.

> Hide the existence of a Monero node?

This is a "reach goal" that most users won't bother with.

> What parts of the network traffic of a Monero node will go through this network, just the "mempool" additions?

Yes, generally the mempool additions will go through I2P unless configured otherwise.

> What about wallets communicating with remote nodes? Do wallets communicate with a "hidden service" of sorts? Or do those transactions go over the regular internet?

It would depend on the configuration. Remote node over I2P is a clear use-case, though it comes with efficiency tradeoffs. Another "nice to have."

> If over regular internet, how are those communications encrypted? Are the different packets going between light wallets and full nodes distinguishable or uniform?

The relevant packets of data communicated here are encrypted iirc, but normal node sync data between nodes is not encrypted.

> Will each full node be a "hidden service"?

It will not be a requirement, but having a network of Monero nodes connected over both clearnet and I2P would substantially increase the resiliency of the network. Monero users benefit from high I2P adoption.

> If you have an IP hosting a hidden service also send corresponding traffic over the regular internet, is that good/bad/neutral for the security of this network?

Mostly neutral. Though it could be "good" in that less data needs to be transferred over the less-efficient I2P network.

> Dandelion protocol, inferior or can it be used in unison with this network to improve security or will it just be not needed?

Dandelion works similarly though to a less-rigorous extent. It's a simpler solution that may be "good enough" for most use-cases. I2P integration should provide more metadata protection than Dandelion, and much better protection against sybil attacks. Dandelion however works more simply with the existing nodes.

## zlatinb | 2019-01-19T04:02:42+00:00
> I hope this bad blood doesn't extend to the I2P-Java team.

I wouldn't be here if that were the case!  There is no bad blood between the **Monero** project as a whole and I2P-java, although our interactions with the **Kovri** team specifically over the years leave a lot to be desired.  But I'm feeling significantly better after reading the comments by @coneiric .

If you choose to go with us we will try to dedicate a full-time resource to the maintenance of libsam3.  

## fluffypony | 2019-01-19T06:11:05+00:00
> I don't think any of the routers should be "bundled" or "embedded" into Monero other than a link on the download page, or submodule branch on the repository. Something like "here are the routers Monero is compatible with, pick one (or many)". As long as the routers support SOCKS, IPC, SAM or some other common API.

This is the same as non-mandatory privacy. I'd support optional Tor support if we're going to bundle i2p, but we *must* bundle something so that it's effortless and on by default, else nobody will use it.

> What parts of the network traffic of a Monero node will go through this network, just the "mempool" additions?

When a node handshakes with another node, over ipv4 or over Tor / i2p, it will specify what it wants on that connection, either blocks or transactions or both. By default, it will ask for transactions only over hidden services, and it will ask for blocks only over ipv4.

> What about wallets communicating with remote nodes? Do wallets communicate with a "hidden service" of sorts? Or do those transactions go over the regular internet?

Absolutely - one of the things that MyMonero wants to add to the open-source light wallet server is the ability to leverage a bundled hidden service, and show a QR code for that service address. You can then scan the QR code with the MyMonero app, and it will use your backend, without you needing to forward ports on your router or do anything like that!

> Dandelion works similarly though to a less-rigorous extent. It's a simpler solution that may be "good enough" for most use-cases. I2P integration should provide more metadata protection than Dandelion, and much better protection against sybil attacks. Dandelion however works more simply with the existing nodes.

In addition, I'm of the opinion that we should implement Dandelion regardless, as it will defeat many of the fingerprinting attacks that try determine whether a machine broadcasting a tx on a hidden service is the same machine broadcasting blocks on a particular ipv4 address.

## JustFranz | 2019-01-19T07:46:08+00:00
Than you for the clear answers, one more question. 

If a light wallet client creates a transaction and sends it to a full node either over ipv4 or i2p/tor, if you are monitoring the outgoing packets of that light wallet, is it an identifiable event? Or is there constant back and forth indistinguishable data transmission where you can't tell?

What I mean is especially if a wallet goes through i2p/tor only to broadcast its transaction. With sufficient surveillance you can tie a wallet (IP, phone, person, entity) to one of the transactions in the block (or mempool addition) after the observed tx broadcasting event over i2p/tor. Knowing that a certain entity just constructed a transaction seems like the best you can hope for, considering the nature of the Monero blockchain. Correct me if I am have misunderstood something.

## x1ddos | 2019-01-19T09:29:13+00:00
> over ipv4

what happened to ipv6? very surprised it's left out.

## lessless | 2019-01-19T09:57:16+00:00
> the aforementioned SAM patches for i2pd are on a branch that needs to be (non trivially) rebased atop the recent protocol improvements (namely NTCP2 and LS2).
> 
> I think that going forward you'll realistically get more done working together with us at loki using lokinet, lots of i2pd people feel really burned by the previous interactions with monero.

@majestrate is it possible to use Loki Network without being bound to the cryptocurrency part? 


## kayront | 2019-01-19T09:58:44+00:00
@anonimal continues to propagate this unsubstantiated claim:

> Besides; this entire issue has already been deprecated by Sekreta. Single-system solutions are a thing of the past. 

Once again, because he failed to reply [on reddit](https://old.reddit.com/r/Monero/comments/aeizzp/never_bring_a_knife_to_a_gun_fight_bring_popcorn/edqdj49/?context=0), and I quote my post in its entirety:

**Repeated frequently in your recent posts is the assumption that a single overlay network is now "deprecated" and "not sound".**

**Please provide evidence supporting this assertion, something other than "I have begun working on something even more complex than the project that has not materialized, and THAT is the solution to all of our problems.**

**I would like to see comments backed by security professionals, tor and i2p developers, where they clearly agree with your assertion.**

**Do you have any such material to share? I will naturally be glad to review my opinion if presented with irrefutable evidence (this message is not adversarial, just straight to the point and I would be happy to learn more if the state of affairs in anonymizing technology truly has changed that much), to the best of my present knowledge no such consensus exists, the first time I heard about Tor or I2P being deprecated when single-handedly relied upon is from your claims, you will surely understand my healthy scepticism on the matter when continued funding depends on the acceptance of the premise that a single overlay network is no longer adequate.**


I must also [reiterate](https://old.reddit.com/r/Monero/comments/acgr0q/anominal_statement_on_secreta_and_kovri/eddcvay/?context=3) that @anonimal continues to exhibit - as clearly seen in this github thread - unwarranted, rude, and aggressive behavior, and continues to speak down to other contributors in a manner that any civilized and reasonable person ought to consider unacceptable.

No one else is distributing insults and belittlements the way @anonimal is doing. This sort of behaviour is hardly acceptable.



## fluffypony | 2019-01-19T10:26:58+00:00
@x1ddos good question! We largely ignore ipv6 as it is not resistant to isolation attacks, which is especially relevant in light of the recent ETC attack (which some suspect was an isolation attack and not a 51% attack). This is because ipv4 addresses are scarce, and thus more expensive. What I’d personally like to see on clearner is some sort of baseline approach where we do like 8 outbound connections on ipv4 for isolation attack resistance, and then anything inbound can be ipv4 or ipv6.

## JustFranz | 2019-01-19T11:03:08+00:00
> @anonimal continues to propagate this unsubstantiated claim:
> 
> > Besides; this entire issue has already been deprecated by Sekreta. Single-system solutions are a thing of the past.
> 
> Once again, because he failed to reply [on reddit](https://old.reddit.com/r/Monero/comments/aeizzp/never_bring_a_knife_to_a_gun_fight_bring_popcorn/edqdj49/?context=0), and I quote my post in its entirety:
> 
> **Repeated frequently in your recent posts is the assumption that a single overlay network is now "deprecated" and "not sound".**
> 

I've had some time to think about sekreta. The readme concentrates on non issues like message confidentiality and integrity which are guaranteed through encryption already.

What tor/i2p are supposed to do is hide you and your activity. Blasting i2p/tor/loki network traffic at the same time is going to reveal you (at the beginning with few users and apps).

Sekreta can not detect a compromised network and route around a spy.

Sekreta will join the different anonymity networks into one for sekreta users and apps. The underlying flaws of each different network remain.

If you use 10 different networks at the same time and 9 of them are perfect while the 10th is flawed and that 10% of usage deanomizes you, you are done. It just does not make sense to use multiple networks simultaneously. You want to use a robust network and blend into the other users of the  network.

Perfect network A and perfect network B with 50K concurrent users for both. For each there are 15K sekreta dual networkers for a total of 15K sekreta users. Those sekreta users are revealing themselves at the ISP level, they are in a pool of 15K instead of the 35K of the remainder of each respective network (+ 15K/2 if the sekreta users divided themselves). Both networks will be monitored and who knows what you can find out about the dual users if you can identify their traffic on both networks.

An API for easy integration with any of the networks currently out there, commendable. Extra encryption safeguards, why not. IMO network switching is bad and simultaneous usage is double-triple bad.

Sekreta might improve security by making the usage and implementation of if easier but it will not enhance any of the networks or synergize multiple for a positive effect for the user.

Sekreta warrants more discussion, thought and planning. 

## x1ddos | 2019-01-19T11:03:38+00:00
This his a bit of a weak argument against ipv6 imho. I personally wouldn't consider resource scarcity being an obstacle to mount such an attack in ipv4 space given the interested party has sufficient funds.

ISPs and hosting providers become more and more desperate due to the same issue of ipv4 scarcity and everyone's switching to ipv6 even though much slower than expected. I know some ISPs deliver new networks to users exclusively over ipv6 stack these days and ipv4 is an exception. To me the lack of ipv6-only support is kind of delaying the inevitable. Relying on ipv4 as some kind of a security measure might as well backfire with slower adoption of monero.

But this is out of scope here. I see there's already #147 although it's closed for some unspecified reason.

## fluffypony | 2019-01-19T11:11:28+00:00
@x1ddos the cost of mounting an attack on ipv6 is like $0, the cost of doing so on ipv4 is not cheap given Monero's node distribution and the usage of anchor connections, class limitations, etc. Some good reading is:

- [This paper describing Monero's p2p system in detail](https://courses.csail.mit.edu/6.857/2018/project/Hu-Macias-Jachymiak-Siabi-Monero.pdf)

- [This paper describing eclipse attacks, and countermeasures against them, some of which Monero has implemented](https://www.usenix.org/system/files/conference/usenixsecurity15/sec15-paper-heilman.pdf)

## orignal | 2019-01-19T11:43:21+00:00
> I don't know what happened, and I don't really want to know, but wow there is a lot of bad blood between Monero and i2pd.
> 
> Since they're separate teams, I hope this bad blood doesn't extend to the I2P-Java team.

Great. Just leave i2pd alone. Especially about "slimmed down i2pd". Go write your own code.

## lessless | 2019-01-19T13:17:56+00:00
@orignal I thought that we all are here to advance privacy in the Internet. What's the problem with using i2pd code? 

## orignal | 2019-01-19T13:24:45+00:00
> @orignal I thought that we all are here to advance privacy in the Internet. What's the problem with using i2pd code?

The is no problem with using i2pd code at all. And we are happy when people use it and help everybody, but kovri, due the theft initiated by Spagni, that affects entire Monero.
And since @knaccc 's position is pretty clear, there is no more room for discussions.

## lessless | 2019-01-19T13:40:06+00:00
Politics will obviously drive this a bit further away from the productive discussion, and I guess all of us have to express gratitude to @knaccc  in the first place for bearing with so many loosely related to the original issue content.

@orignal won't you please mind explaining your concerns to community at [/r/Monero](https://www.reddit.com/r/Monero/), so we will at least be informed about the situation at hand. There are a lot of people out there who are involved in Monero with their hearts, souls and pockets and who will appreciate clearly delivered information.
Thanks.

## majestrate | 2019-01-19T14:48:00+00:00
> > the aforementioned SAM patches for i2pd are on a branch that needs to be (non trivially) rebased atop the recent protocol improvements (namely NTCP2 and LS2).
> > I think that going forward you'll realistically get more done working together with us at loki using lokinet, lots of i2pd people feel really burned by the previous interactions with monero.
> 
> @majestrate is it possible to use Loki Network without being bound to the cryptocurrency part?

yes lokinet can be used without being tied to the loki coin, but it may require a network fork depending on what parts you want to utilize. either way it's totally something we can figure out.

## knaccc | 2019-01-19T14:54:38+00:00
@orignal
> And since @knaccc 's position is pretty clear, there is no more room for discussions.

Not sure what you mean by this. I'm just someone that pointed out that I2P-Java looks like a great project and that it would be easy to bundle it with Monero. It's not my decision, and my enthusiasm for this approach is subject to a healthy debate about the future.


## orignal | 2019-01-19T17:46:53+00:00
@lessless if you, guys, were not away what fluffypony and anonimal did, that's too bad for you.

But based on this statement
> The only reason I suggested Java-I2P in the meanwhile is because that dream scenario seems to be at least 1-2 years away.

The built-in i2pd worked in the Anoncoin network as early as end of 2015. And Spagni knew about it (I can provide a log if necessary). Instead they preferred to shit  on i2pd everywhere and kept doing until recent time. 
Later on we have decided to not use this approach for gostcoin, but bundle i2pd and gostcoin and communicate though the SAM using libsam as suggested in this topic. We have to make some changes to SAM implementation in i2pd and we also changed libsam to support EdDSA signatures and ECIES crypto. Such approach works successfully almost for two year now.

My impression is that Monero remembers about i2pd only when somebody fails. This scenario was with i2pcpp, now kovri, that's not a way we are interested in.
 
@coneiric  mentioned LS2 and ECEIS.
LS2 goes lives next week.
ECIES proposal comes from i2pd. We use ECIES-P256 a lot for a long time, because it's much faster than ElGamal. Everybody can check their netdb for LeaseSets with crypto type 1.



## fluffypony | 2019-01-19T17:53:36+00:00
@orignal Dude, stop. You're embarrassing yourself. Please stop. You literally disappeared and, as far as anyone could tell, abandoned i2pd. After AN ENTIRE MONTH a few people decided to fork the project. I offered them a home at the Monero project. It doesn't matter if it was working with Anoncoin or not, the project was forked and it was up to the new maintainer (@anonimal) to figure out what to do. The fact that you came back later is tangential, because you came back and were immediately hostile to everyone. This fact is evidenced by the terms you use today like "theft" instead of "forked my abandoned code".

I get that there's a language barrier, but even the IRC logs you posted on Reddit last year make you look like you misinterpreted the situation, not like @anonimal and I are evil, conniving tricksters who stole your livelihood. It's better if you just walk away from this with your dignity intact.

## orignal | 2019-01-19T18:01:57+00:00
@fluffypony  you didn't fork, you decided to hijack entire i2pd. Without authorization from anybody.
Proof. https://github.com/PurpleI2P/i2pd/tree/cryptopp  "Remove orignal certificate."
Stop lying like you do all the time. I NEVER ABANDONED or planned to do it. Nobody from your tried to contact me while others was able to contact me without any problem. You was just waiting for an opportunity to hijack i2pd because you failed to pay.
Who has assigned anonimal as "new maintainer"?  You did, didn't you?
You abused the trust granted to you and so was able to get an access to the repository.

Have you shared info about anci2pd project among other Monero people? I doubt.
There is no "language barrier" as you like to repeat this word. There is only your permanent lie, that looks the same in any language.
 





## fluffypony | 2019-01-19T18:17:21+00:00
@orignal Forking is not hijacking, stop being ridiculous. Also, [that commit](https://github.com/PurpleI2P/i2pd/commit/b9e25f2c96bd051cfdc9dc6dfbda1ed44b9ca027) was EinMByte, who was/is a prominent i2p contributor. I have no control over what he did on a repo that I don't have collaborator privileges on.

Failed to pay whom or for what? I literally have no idea what you're talking about.

What repository did I not have access to? The i2pd repo was open, was it not? I don't recall being given special privileges to access anything.

Again, the fact that you came back and were working on i2pd was no secret. anonimal chose to continue with Kovri regardless of whatever i2pd and Anoncoin were doing, and that was his call. There is no conspiracy here, nobody was hiding information that was public in any event. The excess paranoia is not helpful.

This argument isn't pushing the conversation further. I'm going to add you to my ignore list, feel free to continue with your paranoid rants as you wish.

## lessless | 2019-01-19T18:18:42+00:00
@orignal are you the guy who erased git history https://github.com/monero-project/kovri-docs/blob/master/i18n/en/faq.md#what-were-the-turning-points-that-lead-to-forking-from-i2pd-and-why-are-there-two-i2pd-repositories-one-on-bitbucket-and-one-on-github, moved project to https://bitbucket.org/orignal/i2pd/src/master/ and then came back? 

## orignal | 2019-01-19T18:25:02+00:00
> @orignal Forking is not hijacking, stop being ridiculous. Also, [that commit](https://github.com/PurpleI2P/i2pd/commit/b9e25f2c96bd051cfdc9dc6dfbda1ed44b9ca027) was EinMByte, who was/is a prominent i2p contributor.

He has never been an i2pd contributor before. Furthermore he has been declined by me explicitly.

> Failed to pay whom or for what? I literally have no idea what you're talking about.

Let me refresh your memory. When i2pcpp guy has stopped the project, you start buzzing me and  promised to pay on behalf of the Monero. Or you didn't and just wanted to say "hi"?
And I have worked on the code for two years and then suddenly decided to abandon it just for you.
Don't make people idiots.

>I have no control over what he did on a repo that I don't have collaborator privileges on.

Blaming 1M this time?
That's how you "had no privelleges".
https://github.com/PurpleI2P/i2pd/commit/85b1505e511c3ba9da0cf6e8ab140a1a6a9b46b6
 
>anonimal chose to continue with Kovri regardless of whatever i2pd and Anoncoin were doing, and that was his call. 

Answer yes or no if you have shared this info among Monero people.
Or I want to ask others if they have ever heard about anci2pd before.



## orignal | 2019-01-19T18:28:52+00:00
> @orignal are you the guy who erased git history https://github.com/monero-project/kovri-docs/blob/master/i18n/en/faq.md#what-were-the-turning-points-that-lead-to-forking-from-i2pd-and-why-are-there-two-i2pd-repositories-one-on-bitbucket-and-one-on-github, moved project to https://bitbucket.org/orignal/i2pd/src/master/ and then came back?

They have erased the history not me.
See https://github.com/PurpleI2P/i2pd/tree/cryptopp
By moving all files to not show the history before like these files was started from scratch.

I continued on the bitbucket (and I keep maintaining that mirror now) because I was not able to fight with this gang by that time due personal circumstances.

When i2pd got back to github I continued from the original tree to retain the history and moved their stuff to the branch "cryptopp" as evidence of the theft.

## zlatinb | 2019-01-19T20:06:47+00:00
In a probably futile attempt to get this thread back on topic I'd like to point out that it is a good idea to as a lawyer or Oracle themselves whether the BCL applies to the bundles produced by jlink. 

The BCL says the full JRE is subject to export restrictions (Iran, North  Korea, etc) but says nothing about jlink.

## knaccc | 2019-01-19T21:20:12+00:00
Here's a starting point for figuring out license concepts:

Oracle open sourced the JDK under GPLv2 with Classpath Exception. See https://openjdk.java.net/legal/gplv2+ce.html

The classpath exception means that any code that runs inside an OpenJDK JVM is not subject to the GPLv2 and is free to be licensed in any way.

I think the BCL (Binary Code License) that zlatinb is referring to is related to the OracleJDK and not the OpenJDK, as far as I can see.

The OpenJDK is available as packages in most major Linux distributions, so I wonder whether they've already looked into possible export restrictions.


## zlatinb | 2019-01-19T21:55:39+00:00
@knaccc I think it's simpler than that.  How did you find the download links for the different JDKs?  Did you have to click "agree" to any license, or was there text that says something along the lines of "By downloading this software you agree to blah blah"?  If yes, then whatever license that is (most likely BCL) is what applies.

## knaccc | 2019-01-19T22:48:14+00:00
@zlatinb If you download the OracleJDK, you have to agree to license conditions before downloading, because that's the Oracle version.

The OpenJDK however does not require agreement before downloading. The links are here: https://jdk.java.net/11/

You can even build the OpenJDK from source, using instructions here: http://cr.openjdk.java.net/~ihse/demo-new-build-readme/common/doc/building.html

## zlatinb | 2019-01-19T22:51:22+00:00
@knaccc fantastic!  No export restrictions then.  I would have hated to have to configure our download servers to block the people who need i2p most.

## KeeJef | 2019-01-20T10:43:57+00:00
@x1ddos The PR for IPv6 support is here, will soon be merged once a few things are fixed https://github.com/monero-project/monero/pull/4851

## mikalv | 2019-01-20T18:58:56+00:00
Meeh here.

After reading this thread, I can't hold back a comment; omfg so much fucking stupid I've read (aggressive posts, claims, etc). But ok, I'll jump over that and keep the topic.

We decided earlier today I'm gonna maintain the I2P-Java's libsam3 from now on. aka libsam3 helpdesk. So this shouldn't be a problem.

## orignal | 2019-01-20T19:06:31+00:00
@mikalv  correct me if I'm wrong. You use new libsam3 in Anoncoin-gost already

## mikalv | 2019-01-20T19:15:28+00:00
@orignal yes I think you're right

## knaccc | 2019-01-21T03:43:37+00:00
I've got some updated information about the export restrictions on strong crypto in the JDK. I've been told that If things are hosted in the US, then web sites like https://openjdk.java.net/ will cover themselves legally by asking people not to export downloaded content to certain countries. There is actually a ToU on the US hosted OpenJDK site for example https://openjdk.java.net/legal/tou/terms

For this reason, I've been told about an IBM sponsored JDK binary download site here: https://adoptopenjdk.net/releases.html?variant=openjdk11&jvmVariant=hotspot

GNU have a FAQ item about this: https://www.gnu.org/licenses/gpl-faq.en.html#ExportWarranties

The bottom line seems to be that since it's GPLv2 software, what counts is that the country you're downloading it from does not enforce export rules. So no US hosting.

## zlatinb | 2019-01-21T06:42:25+00:00
@knaccc are you sure these export restrictions do not apply only to the unlimited strength JCE?  That is a separate download.  

Also, it is not clear how much of the crypto gets jlink-ed into the final bundle.  

## knaccc | 2019-01-21T06:46:59+00:00
> @knaccc are you sure these export restrictions do not apply only to the unlimited strength JCE? That is a separate download.

In the old days, the unlimited strength crypto policy jar was a separate download. They changed this and unlimited strength is now the default. Either way, it's all GPLv2 now.

## zlatinb | 2019-01-22T18:44:42+00:00
@knaccc two small things:
* 0.9.38 is done and tagged
* if you set LG2=en before invoking ant, it will skip the translations and build much faster

## knaccc | 2019-01-23T06:01:52+00:00
@zlatinb thanks, done and pushed

## knaccc | 2019-01-23T07:05:46+00:00
@jtgrassie Has discovered https://jdk.java.net/jpackage/ https://openjdk.java.net/jeps/343 which will build self-contained msi/exe/deb/rpm/dmg/app files. This is currently scheduled to be available in OpenJDK 13, due for release in September 2019. 

## knaccc | 2019-01-28T20:12:53+00:00
I2P-zero GUI just released. Screenshots at the top of the README here:

https://github.com/knaccc/i2p-zero/blob/master/README.md


## lessless | 2019-01-28T22:02:30+00:00
Fantastic job! 

## zlatinb | 2019-02-06T05:26:26+00:00
@knaccc I did some experimenting with different compression schemes and managed to get all of I2P + a windows JRE (with full I2P dependencies, not just those used by zero) down to 32MB.  To get there, I disabled compression in jlink and in all I2P jars, then compressed the final bundle with lzma.

## moneromooo-monero | 2019-08-27T15:18:47+00:00
Is this still relevant ? I think the GUI uses i2p0 now ?

## selsta | 2019-08-27T15:44:50+00:00
> I think the GUI uses i2p0 now ?

GUI is working on I2P-zero support. I think this can be closed.

## moneromooo-monero | 2019-08-27T15:50:45+00:00
Alright, please reopen if this gets new life as an alternative.

+invalid


# Action History
- Created by: knaccc | 2019-01-13T16:01:41+00:00
- Closed at: 2019-08-27T16:17:55+00:00
