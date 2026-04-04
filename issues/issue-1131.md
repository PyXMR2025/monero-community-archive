---
title: 'Monero Tech Meeting #100 - Monday, 2024-12-23, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1131
author: rbrunner7
assignees: []
labels: []
created_at: '2024-12-21T17:43:46+00:00'
updated_at: '2024-12-23T18:36:40+00:00'
type: issue
status: closed
closed_at: '2024-12-23T18:36:40+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1125).


# Discussion History
## rbrunner7 | 2024-12-23T18:36:40+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1131
<j​berman> *waves*
<r​brunner7> Welcome to our 100th meeting :)
<sneedlewoods> +1
<s​yntheticbird> hi
<s​yntheticbird> congrats
<r​brunner7> Anybody had time to develop something last week, beside frantically buying Christmas gifts?
<j​berman> Continued implementing kayabanerve 's faster torsion check in C/C++ to improve sync (tree build) time. It's taking a bit longer to implement than expected because it seems our crypto lib doesn't have as many ops as the rust lib kaya is using has out of the box (e.g. fe_sqrt, fe_pow to name a couple)
<r​brunner7> Funny anyway that such masses of code should make *anything* substantially faster, but well, it's what those lines do that is important
<r​brunner7> Of course
<r​brunner7> I guess a speedup is important so that you already optimize now, and not later?
<j​berman> on my machine, wallet sync is currently 2-2.5x slower because building the tree locally is so much slower than identifying received outputs (the current bottleneck when pointing to a local daemon)
<j​berman> specifically the faster torsion check would speed up building the tree, to be clear
<r​brunner7> Let's hope so :)
<r​brunner7> I saw that so many Monero PRs wait to get merged it might approach a new record. Is anything in there already with any relevance for FCMP++ implementation?
<tobtoht_> Everything in the queue just got merged an hour ago
<r​brunner7> Ah, ok. Nice.
<tobtoht_> Bootstrappable builds got merged, which is a major milestone in preparing the build system for FCMP++.
<jberman> +1
<sneedlewoods> +1
<r​brunner7> What is a "bootstrappable build"?
<tobtoht_> The ability to build from source "all the way down".
<r​brunner7> So including all sub-modules, recursively?
<r​brunner7> Sounds like fun, especially with that coming mix of 2 programming languages :)
<tobtoht_> You start with a tiny heavily annotated binary and work your way up to increasingly complex software. (Simple C compiler -> C++ compiler -> All build dependencies)
<r​brunner7> Hmm. Sounds even more extreme than reproducible builds. And we will need to compile our own C++ compiler for some reason, or at least will profit from doing so? Maybe this will become clear over the next few months.
<tobtoht_> Bootstrappability isn't relevant to FCMP++, however the switch from Gitian to Guix allows us to ship a modern Rust compiler while still targeting older versions of glibc.
<r​brunner7> Really a new land we will be in with that Rust parts.
<tobtoht_> Bootstrapping is optional. Guix has 'substitutes' which are like binary packages for anyone who doesn't want to build the world from source.
<s​yntheticbird> Will musl still be supported ?
<tobtoht_> Not for release builds (as is currently also the case). We could target musl in the future.
<s​yntheticbird> alright (i'm a musl user so im looking forward official support)
<r​brunner7> Because of the Linux distro you are working with, if I remember correctly?
<tobtoht_> Even better, we could produce portable static binaries: https://github.com/monero-project/monero/pull/9207
<s​yntheticbird> rbrunner7, not working with exactly. I just prefer Alpine Linux for isolated services like monerod (for security reasons)
<s​yntheticbird> tobtoht_ that would be ideal
<tobtoht_> These will run on just about any Linux distro.
<r​brunner7> Basically if the kernel is there, it runs.
<tobtoht_> including Android
<tobtoht_> Yes
<r​brunner7> Fascinating. But will we still have some very simple compile available, like today, git clone and make and there you go?
<tobtoht_> Yes, absolutely. This is just a replacement for the Gitian release build process.
<r​brunner7> Splendid. For a moment I was holding my breath :)
<r​brunner7> Just some more dependencies to install, I guess. Like a Rust compiler of course.
<tobtoht_> Right
<r​brunner7> Ok, that sound indeed like an important puzzle piece then.
<r​brunner7> Interesting report, thanks tobtoht!
<r​brunner7> Do we have anything else to discuss today beyond reports?
<tobtoht_> I have some links and go into some of the benefits of guix / bootstrappability on the PR, for anyone interested: https://github.com/monero-project/monero/pull/8929
<r​brunner7> Bookmarked.
<r​brunner7> Things seem to relentlessly move forward so that something like Gitian is already in "maintenance mode" ...
<r​brunner7> Alright, seems we got everything. Wish everybody nice holidays, thanks for attending, and read you again in 1 week!
<tobtoht_> I find the innovation in this space very exciting. I don't think we'll have to move away from Guix any time soon. Perhaps something even better comes around in a decade.
<s​yntheticbird> merry christmas to you all
<tobtoht_> merry xmas!
````


# Action History
- Created by: rbrunner7 | 2024-12-21T17:43:46+00:00
- Closed at: 2024-12-23T18:36:40+00:00
