---
title: 'Monero Tech Meeting #94 - Monday, 2024-11-04, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1103
author: rbrunner7
assignees: []
labels: []
created_at: '2024-11-01T20:26:24+00:00'
updated_at: '2024-11-04T18:43:35+00:00'
type: issue
status: closed
closed_at: '2024-11-04T18:43:34+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1099).


# Discussion History
## rbrunner7 | 2024-11-04T18:43:34+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1103
<s​needlewoods> Hey
<0​xfffc> Hi everyone
<s​yntheticbird> Hello
<j​berman> *waves*
<r​brunner7> Alright, let's read your reports from last week
<s​needlewoods> Worked on jeffros review and also played around with this tests framework by jberman https://github.com/monero-project/monero/pull/9547 on a new branch, based on the wallet API
<j​berman> Me: I've implemented wallet2-friendly async tree building (parallel local tree building to identifying receives). I haven't re-tested perf, but on my machine tree build should be around 2-2.5x time to identify receives. With lower level optimizations to tree build, overall wallet2 scan time should *hopefully* remain bottlenecked by time to identify receives, and be unaffected by tree building thanks to this approach
<r​brunner7> So it stays interesting :)
<s​yntheticbird> Continued briefly adding FFI of `OutputBlinds`, `*Blind` and `ScalarDecomposition` to `fcmp_pp_rust` crate: https://github.com/j-berman/monero/pull/15. I'll find the time to finish `Fcmp`, `Branch` and `Path` this week. hopefully.
<r​brunner7> That's something like a bridge between Rust and C++, right?
<s​yntheticbird> Yes. It contains the C FFI function that `monerod` is going to use.
<s​yntheticbird> FFI function of `fullchain_membership_proofs` crate*
<s​yntheticbird> iiuc there is another C++ library aside that is doing the template abstraction over these FFI functions
<r​brunner7> Template abstraction?
<s​yntheticbird> C++ `template` definitions. that are going to be used through at `monero` codebase
<r​brunner7> I guess I will understand it when I see it :)
<syntheticbird> +1
<j​berman> https://github.com/monero-project/monero/pull/9436/files#diff-7d6de001fd2c5c00004e26ca5801d03140ea86cfe14976d8424258f11e562875
<j​berman> This diagram should help, but sounds like @SyntheticBird is referring to the src/fcmp_pp/fcmp_pp_rust/fcmp++.h file
<j​berman> Diagram: https://private-user-images.githubusercontent.com/26468430/357961021-e18bd002-ec3f-4a18-9cd4-aba3be3ef858.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzA3NDQxOTMsIm5iZiI6MTczMDc0Mzg5MywicGF0aCI6Ii8yNjQ2ODQzMC8zNTc5NjEwMjEtZTE4YmQwMDItZWMzZi00YTE4LTljZDQtYWJhM2JlM2VmODU4LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDExMDQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMTA0VDE4MTEzM1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTAzOGU5M2NhYjA3N2E3NTEzYzZiMDZlODkxNmMwM2VkYTBhYzg2Y2MyMzdlYmM3ZGQ1Zjk2M2M4Y2U1MWI1MzImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.gdMXmuO2okE9SLia-36oYTrgRaTvgWwKqBY9uUJwXI8
<s​yntheticbird> Yes i forgot which file was that. Thx for clarifying
<jberman> +1
<r​brunner7> Just curious: If you debug such a C++ plus Rust combo interactively, does that work smoothly? Can you step up and down calls, and the display switches between languages?
<s​yntheticbird> Rust assembly makes you wanna kill yourself. So i hope you wont have to
<vThor> :D
<r​brunner7> I wonder where "assembly" enters the picture. You mean you are thrown down to assember instructions level instead of having the Rust source?
<j​berman> I haven't tried to step through the rust side with a debugger, but dbg/print statements on the rust side come through. dbg statements are nice in rust, they print out a complete object cleanly. Modifying the lower level fcmp++ code to try to debug can be a little annoying since it pulls that code in from a github repo, but you can easily pull the github repo into your local, then point the rust code to that local repo
<j​berman> fwiw almost all the debugging I've had to do while working on the integration is on my side of the C++
<r​brunner7> Ok. Let's see how this will play out in the end.
<r​brunner7> Anything else to discuss in this meeting, beyond reports?
<vThor> Hi, and sorry for the interruption, I hope with my CCS I get the documentation for the lib documented on docs.getmonero.org and I would love to see one central point of documetation for development, libraries and so on. I have not yet a subdomain for clearnet for it, but ofrnxmr gave me a hidden service already: http://nuloxt7g5kyavotgekjkcpb5jwnogre4jjw5n32675rgd4umqjm3csad.onion/sdk/ Does there exist documentation what could be integrated there?
<r​brunner7> No idea, myself. Was never involved.
<r​brunner7> No idea either who could answer with authority there ...
<vThor> Another thing, I will now start finally my long procastinated edit of the PR from the review of SNeedlewoods, I gues there are 100 ways how I can fuck it up and only 1-2 ways do do it right. So, I would edit, then commit, then push in the same branch (can I add a tag?) and what I need to do then in the github web side regarding the correction of the PR?
<s​needlewoods> vthor if you push to your remote branch it should automatically update the PR to the monero repo, no additional steps involved
<vThor> I mean the fcmp++ part is pretty new and so I think it would make sense to document that directly, even before catching up with the current stuff, or?
<s​needlewoods> and don't worry, there are almost as many ways to do it right as there are ways to mess it up :D
<vThor> s​needlewoods: thank you that is comforting :)
<vThor> :D "nd don't worry, there are almost as many ways to do it right" that even more
<s​needlewoods> if I'm unsure a git command could mess something up I do a backup of the branch or my entire local repo, that often was very helpful
<r​brunner7> vThor: Not sure I understand your comment about documenting FCMP++. Is that somehow related with your work right now?
<vThor> :o I got already with git 10 days of work eradicated on trying to reorganize the commits in thr retroperspective, and learned then first try in a play repo before making some new (to me) git magic
<r​brunner7> I have a question about next week's meeting: Does it make sense to skip that, because of Monerotopia? So next meeting in 2 weeks?
<j​berman> good with me
<s​needlewoods> +1
<vThor> "vThor: Not sure I understand your comment about documenting FCMP++. Is that somehow related with your work right now?" <- Nope. Only a think I would like to see. Maybe you remeber my proposal I closed, but still I would like that there exists something like an SDK and thinks are documeted in one place in different depth levels. To easy create something without the full picture and the ability to dive in deeper, without to search the internet for 
<vThor> source
<r​brunner7> vThor: Ah, ok. So nothing that blocks you in a way in the short term.
<vThor> Nope, only documetation ends up in the end when there is a shortage of time always on low priority, but then later it cost 10x the effort to document something. ( I'm guilt of that sin, too)
<r​brunner7> Alright, I think we can close. Read you again in 2 weeks then. Happy Monerotopia to the people who will be there!
<j​berman> Gonna add a bit more color to my wallet2 scanning work
<r​brunner7> And thanks for attending of course
<vThor> So, how I see that there will be a C ABI/FFI for fcmp++ it would be great to document it also on a central place to avoid headache in the future.
<s​needlewoods> thanks everybody
<r​brunner7> PowerPoint slides or it does not exist :)
<vThor> *arg* :D
<j​berman> @vthor imo this PR is probably the best place to get an idea of changes for now: https://github.com/monero-project/monero/pull/9436
<j​berman> I agree it will eventually be nice to have central documentation on the integration implementation once it's complete
````


# Action History
- Created by: rbrunner7 | 2024-11-01T20:26:24+00:00
- Closed at: 2024-11-04T18:43:34+00:00
