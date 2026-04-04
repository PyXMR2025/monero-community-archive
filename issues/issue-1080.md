---
title: 'Monero Tech Meeting #88 - Monday, 2024-09-23, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1080
author: rbrunner7
assignees: []
labels: []
created_at: '2024-09-20T06:32:02+00:00'
updated_at: '2024-09-23T19:04:52+00:00'
type: issue
status: closed
closed_at: '2024-09-23T19:04:52+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1075).


# Discussion History
## rbrunner7 | 2024-09-23T19:04:52+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1080
<vthor> hi
<S​neurlax> hiya
<j​berman> *waves*
<s​needlewoods> hey
<j​effro256> Howdy
<k​ayabanerve> waves
<r​brunner7> Nice, good attendance. So, what are the reports from the last week?
<s​needlewoods> Working on rbrunners review comments and my own TODOs: https://github.com/monero-project/monero/pull/9464
<j​effro256> me: more auditor shtuff and Carrot coding
<k​ayabanerve> I'm working on making my EC divisors lib constant time.
<sneurlax> working on dart integrations and rust wrappers towards that end.  can elaborate
<r​brunner7> Did that work just offer itself, for a change? I imagine that there are a lot of things on your "to develop" list
<k​ayabanerve> rbrunner7: who is that asking?
<r​brunner7> To you
<k​ayabanerve> Oh. I'd have guessed SNeedlewoods :)
<j​berman> me: made some progress on fcmp++ tx construction, waiting on @kayabaNerve's next batch of fcmp++ work to move forward on that front, thinking I will start on wallet sync (building the local tree) if I get the green light today
<k​ayabanerve> I'm working on cleaning the FCMP prove/verify functions as necessary for expansion to the multi-input case. That requires reworking the data flow, including where we construct divisors. I already built a nice abstraction layer around constructing divisors, yet I didn't finish the work in making it constant time. I'm making it constant time so I can forget about it and use my nice abstraction to finish cleaning the FCMP prove/verify functions.
<sneurlax> on the "no wallet left behind" front, cake, stack, monero-ts, and a few other mobile wallets can all track these FCMP updates in the future by making sure that MrCyjaneK/monero_c, which uses monero-project/monero itself, is updated following kayaba and jberman's work (I may want to rope MrCyjaneK himself into this later if there are any issues
<sneurlax> there)
<j​effro256> Multi-input proofs aren't going to be batched, are they?
<k​ayabanerve> It's undecided if they will be by power of 2 or will be entirely.
<k​ayabanerve> I expect entirely to be the agreeable option.
<k​ayabanerve> sneurlax: I can commit -serai to updating as well for any dependents there :D
<r​brunner7> sneurlax: Dart enter the picture with Flutter, the language these wallets are written in?
<S​neurlax> yes, I'm just trying to make sure that all these packages are Dart packages and do not require Flutter so they can be used on the commandline
<r​brunner7> I guess they will be very grateful for your work ...
<j​effro256> Can two entities create a collaborative FCMP++ 2-input transaction together with batched input proofs and not expose the transaction output's path to the other?
<S​neurlax> others may notice I published many *-serai-mirror crates in order to publish a working monero-rust crate--these will be unpublished/yanked/archived/deprecated after monero-serai, monero-wallet, et al are published
<S​neurlax> way out of left field, recanman's php re-implementation of monero is cool but the size of the review worries me and it worries me that updating it for future FCMP integration will be difficult. I want to see if monero_c can be integrated into PHP like all the other languages.  it's a monstrosity but it actually makes most sense to me because monero-project/monero is our ground sou<clipped message>
<S​neurlax> rce of truth and all the other language integrators just have to concern themselves with respecting it
<S​neurlax> not really worried about PHP, it's just my responsibility as I uploaded the original old monero-integrations/monerophp...
<S​neurlax> unimportant question there but are we wanting to continue developing the monero-integrations org and steward the language-specific integrations there? no need to answer now but within a few quarters
<r​brunner7> You mean treat them (almost) like "core software", in an ideal case?
<S​neurlax> yeah, however official monero-integrations is considered.
<vthor> shouldn't there only be rust /s
<S​neurlax> if we want them to go there, SerHack can fork them over there. not really a big deal to me but that's a convenient way to get a 2nd admin onto some of these things
<k​ayabanerve> Oh! I made a really cool flow chart for this
<k​ayabanerve> Is it in monero-project/monero?
<k​ayabanerve> Yes ..................... No
<k​ayabanerve> It's Official ...... It's unofficial
<s​needlewoods> lol
<S​neurlax> the main concern is FCMPs etc into monero-project/monero and then we can worry about the bike to get those to PHP/Dart/fill in the language
<k​ayabanerve> Hope that helps clarify the status of monero-integrations!
<S​neurlax> the main concern is FCMPs etc into monero-project/monero and then we can worry about the bike(s) to get those to PHP/Dart/fill in the language and their shed
<r​brunner7> Maybe already some better coordination will improve things considerable. *If* people are available, of course
<k​ayabanerve> /s, but I've never heard of this org and assume it's treated as completely third party
<S​neurlax> SerHack ushered me into it long ago for monerophp, monero-nodejs, etc
<S​neurlax> and in all that time since I've wondered how official it is :D or isn't, lol.  aaanyways...
<r​brunner7> Do we have any idea how many users these packages see?
<S​neurlax> and in all that time since I've wondered how official it is :D or isn't, lol.  aaanyways... *notes that it's ofishul*
<r​brunner7> I mean real, actual, live deployments?
<S​neurlax> could be 0, most if not all are out of date. so sorry to distract with this topic.
<r​brunner7> Ok :)
<j​effro256> As someone who works on "official" Monero code, you probably don't want payment processing software to become "official". It comes with a lot of red tape, which is nice to have for one instantiation of the core code for robustness, but it is probably overkill for something which is web integrated and needs constant updating.
<S​neurlax> yeah, monero-integrations is mostly concered with woocommerce, shopify, etc. ... after fcmps it might be good to update them for the ecosystem but it's already out of date and so might be irrelevant currently.  I'll just discuss w SerHack directly if he's going to be updating those to be current to fluorine fermi
<S​neurlax> recanman has been working on that for php at least. so, now everyone knows, yay
<r​brunner7> Alright. Maybe we move on then. jberman: You mentioned possibly obtaining a green light about some follow-up work of yours. Do you want to elaborate?
<vthor> I needed to add 4 methods in wallet2 to integrate UR into monero-gui, and can be that I need to other, still pulling the rope for offline signing and submit tx (although I think this can work with a string). Is there any change that get ever merged? Only to know how much effort I will put in, because I hate to produce code to throw it away afterwards
<r​brunner7> vthor: I think the only way to get to know is actually making the PR and then wait for comments, and hopefully reviews.
<j​berman> UR sounds like something that would be cool for the CLI to also support
<j​berman> for the cold wallet <> hot wallet flow there too
<j​berman> CLI compatible with GUI/other wallets for that is also nice / worth integrating into the core repo
<sneurlax> yeah vthor I will try to support that even if wallet2 doesn't integrate it. might be something for SNeedleWoods' related wallet API PR https://github.com/monero-project/monero/pull/9368 ?
<sneurlax> wallet2 would be the best place to put it for monero_c, which now goes to dart and monero-ts as well, as I mentioned before ... focusing changes on wallet2 until there's such a thing as wallet3 or similar is optimal ... let's get wallet2 updated if possible
<j​berman> @jeffro256 you mentioned the other week interest in picking up wallet sync. thoughts on me taking it this week?
<s​needlewoods> As sneurlax said, if possible add it to the wallet api, then it will become accessible for gui and cli
<r​brunner7> Uh, maybe a little misunderstanding. I see sneurlax opining for putting it directly into wallet2 for the time being. But of course, longterm into the Wallet API
<vthor> In reality it is simply how it had (IMO) should done in the first place and read/write from a string instead from a file, and file handeling should be in cli/gui or whatever code....
<r​brunner7> You mean 10 years ago or more, when the CryptoNote devs laid the foundations of all this :)
<vthor> but it is used and I can not simply change everything in what is my code either, so I splitted the methodes or duplicated, depending how it would IMO create less headache.
<j​berman> I think woodser made a similar change a while back for loading wallet files/keys (update to allow passing in a string instead of reading from file directly)
<r​brunner7> I would say it's certainly worth to at least PR it and try.
<j​effro256> jberman: Yeah that'd be awesome if you picked it up. My offer is still on the table, though. I initially proposed to pick it up after I was done with other things because I was so adamant about it being included, so I thought it fair if I proposed to work on it. NGL, you will probably be able to tackle it faster as you are more familiar with the tree building. I understand though <clipped mess
<j​effro256> if you have a desire to work on different things tho ;)
<vthor> I can not find it in wallet2, so I made this in the wallet-rpc and now the same in wallet2_api for monero-gui
<sneurlax> I may be confusing wallet2 vs wallet2_api terminology.
<sneurlax> you will know better than i the better term in this case.
<j​berman> I was also thinking it would be nice if another dev started to get familiar with tree building to make the fcmp++ review smoother, but at this stage seems most efficient if I just start on it now. I'm definitely cool with taking it
<r​brunner7> .... aaaand sold :)
<vthor> rbunner7, I'm down, and again too much work in something "easy" envolved, so for me is at the moment like if it probably will not get merged I will not put more hours in roboust user feedback how it is born dead, if it is probable that it gets merged I would of course finish ecerything nice (as nice as possible).
<sneurlax> vthor, is it something that can be rolled into https://github.com/monero-project/monero/pull/9368 and we push that when everything is ready? or is it outside the scope of this effort?
<sneurlax> then I can also make sure to support any changes and/or additions to this as well and be ready for it all. anything new for fcmps can go in this as well.
<vthor> :D /s I wanted to do something like that, but it was out of scope, then I lowerded the scope and then if was not rust, I have no expertise.....
<j​effro256> I still plan to review the tree-building at some point before deploying, so hopefully I'll get familiar with it either way
<r​brunner7> For what it's worth, I don't think it's probable that it will get rejected. Don't see right now any obvious reason why it should. And well, if you like, you can just present it as a "do not merge" early work proposal without putting much further work into itand see what people think
<vthor> Sorry, I'm simply fucked and stressed out and feel simply some hostility and in the moment I want only to finish my last milestone to provide some food to my familly. I'm down with my nerves and have strong headache, so it is not my intention to be bitchy
<j​effro256> Will the UR reading introduce new third-party dependencies for wallet2?
<r​brunner7> vthor: Sounds rough. Anyway, you decide of course.
<j​berman> I'd guess @tobtoht would potentially be keen on UR integration into wallet2 / the wallet API also as Feather would use it, worth getting their feedback too
<j​effro256> vthor: that is relatable, wish you the best
<j​effro256> It's easy to get stressed out
<vthor> well, I build a lib, but I was thinking to copying the monero-gui relevant part into src, because then I can delete all the Qt stuff what can not be used in QtQuick
<r​brunner7> This stuff won't run away, even if you finish your project milestones without taking prisoners, and we look at it later.
<r​brunner7> Maybe it really is a bit thorny and need time, who knows.
<vthor> no, it is the last milestone of the XmrSigner I'm working on, but couldn't work after proposing my last CCS because this hostility simply gets me in an angry emotional state, and I want only to finish my ongoing CCS and then evaluate if it even makes sense to try any longer to do here something, because I had not really the impression that it is welcome, more like I would disturb
<j​effro256> This is a pretty fine distinction, but I would be okay with string handling being put into wallet2, but probably not UR scanning libs directly.
<vthor> no the urlibs (bcur, QrCode) goes to monero-gui
<j​effro256> That's good
<vthor> but monero gui, has only a thin wrapper around wallet2 so that I would need to put in monero source
<j​effro256> vthor: are you referring to hostility within this room?
<r​brunner7> Yes, called "Wallet API" most of the time
<j​berman> I think strings in wallet API / wallet2 is reasonable. I'm pretty sure the CLI wallet has some QR code display somewhere already. So at least displaying there may be less controversial (perhaps only added dep to the CLI is bcur?)
<r​brunner7> That wrapper
<vthor> "hat is relatable, wish you the best" <- thank you :)
<vthor> yeah wallet api, I still have some struggles with the things there splattered around... :S
<r​brunner7> I think sometime it's hard to decide how much weight to give to somebody just complaining without much authority and much reason. If somebody proposed something sensible, I rarely saw *true* hostility from people in the know.
<r​brunner7> Doesn't help much maybe, however
<r​brunner7> Ok, any more things to discuss in this very meeting?
<s​needlewoods> To prevent further paralysis by analysis, here are a two things that don't need to be discussed now, but would be great if anyone has a minute to look into during the week:
<vthor>  think strings in wallet API / wallet2 is reasonable. I'm pretty sure the CLI wallet has some QR code display somewhere already. So at least displaying there may be less controversial (perhaps only added dep to the CLI is bcur?) Don't think that should be additional there inside, IMO there is alreay too much, only IMO there should be monero and for all the other stuff like with monero-gui, also monero-cli, monero-rpc etc as repositories to get some 
<vthor> headach away....
<s​needlewoods> - Do we need `wallet2::update_pool_state()`([src](https://github.com/monero-project/monero/blob/a1dc85c5373a30f14aaf7dcfdd95f5a7375d3623/src/wallet/wallet2.cpp#L3684), used in [wallet-rpc](https://github.com/monero-project/monero/blob/a1dc85c5373a30f14aaf7dcfdd95f5a7375d3623/src/wallet/wallet_rpc_server.cpp#L2855) & [wallet-cli](https://github.com/monero-project/monero/blob/a1dc85c5373a30f14aaf7dcfdd95f5a7375d3623/src/simplewallet/simplewallet.cpp#L8586)) & `wallet2::process_pool_state()` in the API? rbrunner opened the discussion with a comment [here](https://github.com/monero-project/monero/pull/9464#discussion_r1747100670).
<s​needlewoods> - I wanted to propose to remove these "accept functions" from the function parameters (as e.g. [here](https://github.com/monero-project/monero/blob/3d890fd0859b8e7992f917ebdfda270af7f16ffd/src/wallet/api/wallet2_api.h#L1354-L1362) used by the wallet-cli [here](https://github.com/monero-project/monero/blob/a1dc85c5373a30f14aaf7dcfdd95f5a7375d3623/src/simplewallet/simplewallet.cpp#L7850)) and "offload" this job to simplewallet as its done [here](https://github.com/monero-project/monero/blob/a1dc85c5373a30f14aaf7dcfdd95f5a7375d3623/src/simplewallet/simplewallet.cpp#L2316-L2335), where the accept function gets applied after the wallet2 call `m_wallet->cold_sign_tx(...)`, but then I realized not all of them are optional in wallet2 (e.g. [here](https://github.com/monero-project/monero/blob/a1dc85c5373a30f14aaf7dcfdd95f5a7375d3623/src/wallet/wallet2.h#L1200-L1201)). Should I still continue with the approach where the parameter is optional, as I did in [this commit](https://github.com/monero-project/monero/pull/9464/commits/4291ce04bda50a95ef71b7aa974423f5fd5f8c1e)? And how to handle the non-optional accept functions?
<s​needlewoods> (that latest commit is a great quick summary of how things are going: remove 2 TODOs and add one TODO, lol)
<r​brunner7> Ok. I think we can wrap up the meeting proper at this point. Thanks for attending, read you again next week at the latest!
<s​needlewoods> thanks everyone
<j​berman> ok, well on using strings for importing/exporting key images/outputs, you could check the function load_wallet_cache as an example for extending wallet2 to support loading strings in place of files. I don't think that would be a controversial change and UR integration into the GUI is something I expect people would want, especially if the integration has compatibility with other w<clipped messag
<j​berman> allets, like Feather
<j​effro256> SNeedlewoods: posted comment https://github.com/monero-project/monero/pull/9464#discussion_r1771934673
<s​needlewoods> thanks
<vthor> what means YAGNI?
<s​needlewoods> https://en.wikipedia.org/wiki/You_aren't_gonna_need_it
<vthor> thank you
````


# Action History
- Created by: rbrunner7 | 2024-09-20T06:32:02+00:00
- Closed at: 2024-09-23T19:04:52+00:00
