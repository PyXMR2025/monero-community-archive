---
title: '[Discussion] Simple mode (for remote node users)'
source_url: https://github.com/monero-project/monero-gui/issues/1846
author: dEBRUYNE-1
assignees: []
labels:
- resolved
created_at: '2018-12-19T15:08:48+00:00'
updated_at: '2019-04-23T18:36:45+00:00'
type: issue
status: closed
closed_at: '2019-04-23T18:36:45+00:00'
---

# Original Description
The community has long stipulated that, in its current form, the GUI is not properly tailored to the less tech-savvy. I personally have acknowledged this particular issue and am therefore proposing to add a simple mode, which would be significantly better curtailed for the less tech-savvy. The goal of this ticket is to describe the layout of the proposed simple mode and to provide an opportunity for the community to post feedback. In a nutshell, the goal for simple mode is to let the GUI automatically connect to a remote node and remove all, arguably, advanced features. 

---------------------

Let's start in the wizard. First, I'd suggest to add the mode selection after the language selection. This ensures a user can easily switch modes. Furthermore, this allows us to remove (disable) features from (in) the wizard (whilst in simple mode) such as the ability to select testnet/stagenet and the number of KDF rounds. 

I thus suggest to remove / disable the following in the wizard (whilst in simple mode).

On [this page](https://github.com/monero-ecosystem/monero-GUI-guide/raw/master/media/wizard_2-options.png):

- Remove number of KDF rounds
- Remove ability to select mainnet, testnet, or stagenet

Additionally, fully remove [this page](https://github.com/monero-ecosystem/monero-GUI-guide/raw/master/media/wizard_5-daemon-settings.png) and ensure the GUI automatically connects to a remote node. Users interested in using a custom remote node (e.g. their own remote node) will be 'delegated' to "Advanced mode", which would basically be similar to the current version of the GUI. 

--------------------------

After the wizard, I'd suggest to I'd suggest to remove / disable the following:

1. On the [`Send` page](https://github.com/monero-ecosystem/monero-GUI-guide/raw/master/media/black_send.png):

- Remove all features under `Advanced options` 

2. On the [`Receive page](https://github.com/monero-ecosystem/monero-GUI-guide/raw/master/media/black_receive.png):

- Remove all features except the ability to generate a new subaddress and perhaps the QR code. 

3.  Fully remove the [`Advanced` page](https://github.com/monero-ecosystem/monero-GUI-guide/blob/master/monero-GUI-guide.md#advanced-features). 

4. On the [`Settings` page - `Wallet` tab](https://github.com/monero-ecosystem/monero-GUI-guide/raw/master/media/black_settings-wallet.png):

- Remove rescan wallet balance feature, as it requires a trusted node. 

5. Fully remove the [`Settings` page - `Node` tab](https://github.com/monero-ecosystem/monero-GUI-guide/raw/master/media/black_settings-node-local_node.png). To reiterate, users interested in using a custom remote node (e.g. their own remote node) will be 'delegated' to "Advanced mode", which would basically be similar to the current version of the GUI. 

6. Fully remove the [`Settings` page - `Log` tab](https://github.com/monero-ecosystem/monero-GUI-guide/raw/master/media/black_settings-log.png).

7. To clarify, I'd like to fully keep the `History` page, `Addressbook` (sub)page,, `Seed & keys` (sub)page, `Settings` page - `Layout` tab, and `Settings` page - `Info` tab.

A few final notes:

- I also have a proposition to add a simple mode (for local node users), which will be posted tomorrow or the day thereafter. 
- The remote node would be randomly chosen from the set of remote nodes under the node aggregator that would, most likely, be set up and hosted by @xmrdsc.
- Perhaps we could let users select their continent to improve performance, because, for instance, an American user will invariably have a better user experience whilst connected to a North-American remote node than whilst connected to an Asian remote node. 
- A checkbox could be added for Tails / Whonix users, that, if checked, ensures the GUI automatically connects to an onion remote node. 
- This particular mode would *not* be the default mode.
- A (brief) warning about the security and privacy detriments of using a remote node should be added. 


















# Discussion History
## Gingeropolous | 2018-12-19T15:17:17+00:00
My only gripe is this: 

> The remote node would be randomly chosen from the set of remote nodes under the node aggregator that would, most likely, be set up and hosted by @xmrdsc.

dsc has already been working on a node-o-matic that the GUI can use, similar to monerujo. I.e., the GUI itself will scan the network and find remote nodes. Creating and maintaining a DNS system for this is apparently not straightforward. Lafudoci figured out a hack to deliver only 5 IP addresses, for instance, to fix the problem that some DNS providers will just not deliver a txt record that contains 20+ addresses. Relying on a centralized service for remote nodes is just not necessary anymore now that m2049r coded up node-o-matic and dsc started porting it (i think). 

## Gingeropolous | 2018-12-19T15:22:16+00:00
second gripe is this

> Additionally, fully remove (page that starts daemon)

IMO, any monero software should *always* attempt to get a local copy of the blockchain. I think this simple mode should get a remote node and use the bootstrap-node flag, so the user gets immediate use and also starts getting a local copy. However, the local node should be super throttled - max-concurrency 1, transfer rates of 400 kb/s or something, max incoming connections set at 8 or something. 

If we leave it as a remote node in simple mode, i bet 95% of people that use the GUI will never get their own copy of the chain.

Ideally, this would occur when moneromooos pruning stuff is ready. so another flag that would be autoloaded is --prune-blockchain

## dEBRUYNE-1 | 2018-12-19T15:25:17+00:00
>IMO, any monero software should always attempt to get a local copy of the blockchain. I think this simple mode should get a remote node and use the bootstrap-node flag, so the user gets immediate use and also starts getting a local copy. However, the local node should be super throttled - max-concurrency 1, transfer rates of 400 kb/s or something, max incoming connections set at 8 or something.

This is basically the goal of simple mode (for local node users), which will be explained in more detail soon:

>I also have a proposition to add a simple mode (for local node users), which will be posted tomorrow or the day thereafter.


## erciccione | 2018-12-19T15:25:55+00:00
I agree on all points, I'm only concerned about the unevitable abuse of remote nodes. i would suggest to make possible for the user to choose between a remote node, and a local node with automatic bootrstap of a remote node. This would make possible for the user to immediatly use the wallet with the bootstrapped remote node, but at the same time syncronize a full one.

Edit: Just read @Gingeropolous 's second post. That's exactly my opinion.

## erciccione | 2018-12-19T15:31:26+00:00
~~@dEBRUYNE-1 So in your model the user would be initially asked to choose between 4 modes (remote node simple, remote node normal-advanced - local node simple, local node normal-advance). Am i correct?~~

Clarified on IRC. Would be "Instead of 3 modes on one page you'd have two modes and another selection of two modes"

## dEBRUYNE-1 | 2018-12-19T15:42:44+00:00
>i would suggest to make possible for the user to choose between a remote node, and a local node with automatic bootrstap of a remote node. 

That's basically simple mode (for remote users) and simple mode (for local node users). 

>So in your model the user would be initially asked to choose between 4 modes (remote node simple, remote node normal-advanced - local node simple, local node normal-advance). Am i correct?

No. There would be three modes:

- Simple mode (for remote node users) - automatically connect to a remote node 
- Simple mode (for local node users) - automatically use a bootstrap (remote) node whilst the local node syncs in the background 
- Advanced / normal mode - current version of the GUI, where the user has to specify everything himself.

## sanderfoobar | 2018-12-19T16:18:17+00:00
@Gingeropolous brings up a fair point. The last few weeks I have been investigating the feasibility of adopting node-o-matic natively inside the GUI. I am, of course, aware of what Monero stands for, tries to achieve and any sign of a centralized service will likely raise a few eyebrows. I respect anyone for questioning this proposition - and I myself would probably be skeptical. Hear me out.

The underlying idea here is that I and others would like to tailor the GUI more towards multiple target audiences. The sporadic, casual user, the technical savvy, the person running on Tails and everything in between. Usability has been a long standing complaint for Monero. As such, I believe there is a place inside our beloved GUI to serve a wide variety of users - as long as one type does not influence the other, that is to say: the GUI should keep it's advanced configuration options if one wishes to have those.

So the complaint here from @Gingeropolous: "We don't have to rely on a centralized remote node aggregator when we have node-o-matic". Let's also note that this proposal only applies to "Simple mode (remote)", i.e: people who have actively chosen for this option.

First lets dive into how node-o-matic works:

1. Ask all Monero seed nodes for a list of peers (ipv4:port)
2. Contact each and ask for more peers
3. Scan (~2000) peers and try to discover an open RPC port
4. Verify that this node is on an acceptable blockheight
    - Achieved by contacting an external API, such as xmrchain.net or implement an algorithm that simply picks the highest reported out of all nodes (afaik. Monerujo does this).
5. Connect to that port

I have 3 complaints on node-o-matic:

1. Not trivial to implement in C++. Not rocket science, however, multi-threading would be required in order to not freeze the UI. Not the end of the world but it would definitely introduce a whole bunch of code which needs to be well written and properly maintained.
2. You're connecting to other users, who may close `monerod` unexpectedly - leaving you in search for another peer.
    - Added complaint here is that you might be connecting to a node that exposed their port by accident.
3. With increased GUI usage, the Monero p2p network would experience something that would resemble an on-going DoS, as each GUI instance is constantly mass-scanning the network for open ports. I don't like the idea of turning the GUI into some kind of Nmap. This is by far my biggest complaint.

As for DNS:

> Creating and maintaining a DNS system for this is apparently not straightforward. Lafudoci figured out a hack to deliver only 5 IP addresses, for instance, to fix the problem that some DNS providers will just not deliver a txt record that contains 20+ addresses.

DNS is one form of transport, this list of aggregated nodes I plan to maintain could be fed in other ways, over http(s) being the most trivial one.

To iterate on my statement that as a developer I know all to well what we're trying to achieve, however, I'd also argue that isn't to say our GUI can't also serve other use cases, albeit with strong warnings and clear descriptions.

## bitlamas | 2018-12-19T17:02:39+00:00
I like this idea very much. Indeed, usability of Monero software has been flagged by the broader community as an issue for a long time and this would certainly help. I have a couple of questions, though:

- Once the user selected the `Simple mode`, will he/she be able to change it back to `Advanced mode` with the same wallet? Where this option would be?
- Maybe this is too off-topic, but how feasible is to add an embedded 1-minute video tutorial of someone demoing the GUI (in both modes)? The average user usually don't have the time nor the discipline to read guides and I think this would improve the experience and reduce the questions/support requests on IRC, reddit, etc. I've been thinking about this idea for a while, but I don't even know if it's feasible to add a video on the GUI.

## dEBRUYNE-1 | 2018-12-19T17:13:40+00:00
>Once the user selected the Simple mode, will he/she be able to change it back to Advanced mode with the same wallet? Where this option would be?

Initially the user would have to close his wallet, select his desired mode in the wizard, and reopen his wallet. In the future we can probably add mode selection to the `Settings` page, but I think initially it would be best and easiest to restrict mode selection to the wizard. 

>Maybe this is too off-topic, but how feasible is to add an embedded 1-minute video tutorial of someone demoing the GUI (in both modes)? The average user usually don't have the time nor the discipline to read guides and I think this would improve the experience and reduce the questions/support requests on IRC, reddit, etc. I've been thinking about this idea for a while, but I don't even know if it's feasible to add a video on the GUI.

This was proposed on IRC as well by gingeropolous. He suggested to make two videos that would explain the difference between modes.

## Gingeropolous | 2018-12-19T17:16:38+00:00
@xmrdsc 

> You're connecting to other users, who may close monerod unexpectedly - leaving you in search for another peer. 

This is true whether you are using node-o-matic or whether you are using a Refined Awesome Curated List of Delectable Remote Nodes listed on a node listing service. 

> With increased GUI usage, the Monero p2p network would experience something that would resemble an on-going DoS, as each GUI instance is constantly mass-scanning the network for open ports.

I fundamentally don't see the problem with this. Is it a denial of service, or is it the exact service that the monero network is providing? I mean, the monero p2p service is kinda doing the same thing. Perhaps node-o-matic should scale back a little (i.e., not do 3000 scans simultaneously, perhaps crawl through the list based on the wallet users IP address... scan IPs in the closest subnet or whatever first). 

> this list of aggregated nodes I plan to maintain could be fed in other ways, over http(s) being the most trivial one.

This is great and all, and I commend you for offering to create and and maintain this service.... but who are you? And who am I? I am also nobody and shouldn't be inherently trusted to offer node listing services, and i've been trying forever to deprecate the node listing service approach and move to a more decentralized model,  and I know you get this and you've stated as much "To iterate on my statement that as a developer I know all to well what we're trying to achieve"... but, can we rely on you? For years? To offer this node listing service? Are you going to share access to the server so others can step in if you go missing or on holiday or whatever? I've tried to make moneroworld as hands off as possible, but im always amazed how many people use node.moneroworld.com and never goto moneroworld.com to actually read it and find alternatives in case the main service is busted. 

I'm sorry, I've had too much coffee. I know this is understood, I just don't understand why we're considering de-facto centralization when we have the tools to do it in a decentralized way. Node listing services were a stopgap for a better solution, and that solution is here. Centralized services are always easier, cheaper, and use less resources. This is monero - we don't do easy, we do whats best. 

I mean, ideally the monero p2p network would itself catalogue remote node servers. Moneromooo was working on this with the share-rpc branch. 

Or should we treat it like the primary monero seed nodes? I mean, thats centralized. And I assume this stuff aint cheap to ensure content delivery everywhere. 

Ultimately though I can't code so its really whatever ends up in the tag i guess :)


## apertamono | 2018-12-19T17:19:55+00:00
Yes, we need a simplified client. Sticking to my expertise, a comment on terminology:
It would be confusing to have both an `Advanced mode` and an `Advanced` page within the advanced mode. Can we brainstorm another name, e.g. `Complete` or `Expert` mode?

> Remove number of KDF rounds

I didn't know we asked users to select that, so it's probably too complicated for me. I don't see it on the screenshot either. Here, I'd also suggest removing the option to restore from keys (which look like weird gibberish to normies). And let's take this opportunity to rename 'mnemonic seeds' (animal, vegetable, mineral???) to 'recovery text'. 

## SamsungGalaxyPlayer | 2018-12-19T17:29:27+00:00
@ProkhorZ I am fine with "simple" and "expert" modes.

## erciccione | 2018-12-19T17:38:32+00:00
> I didn't know we asked users to select that, so it's probably too complicated for me. I don't see it on the screenshot either

This feature was introduced only recently (#1498 ), it's not in the guide yet, but it will be (monero-ecosystem/monero-GUI-guide#101)

## BigslimVdub | 2018-12-19T19:03:47+00:00
The GUI is very simple to work and is powerful for more advanced users if desired. After initial setup (of which I have created 5 visual walk through tutorials) and user should be able to do all basic functions of setup and making/receiving a transaction. 

IMO a separate “Light Wallet” would suffice so that the current wallet stays fully operational. 

## riscphree | 2018-12-19T19:11:20+00:00
Having a nice toggle switch for advanced options is still nice (esp mainnet, testnet, stagenet). 
There are times when I just want a wallet quick and fast, and other times I'm tinkering so having other advanced options still in is also nice without the added secondary wallet software I might end up needing.

## GBKS | 2018-12-20T08:49:10+00:00
I think this could help address some issues where people are confused about the extra options they are seeing. What I don't think it will help with are usability issues related to a lack of understanding of how things work. For that, we would need to explain things better, provide more support when errors happen, split up user flows more (e.g. splitting the send screen into individual ones for amount, address, fee & confirmation, etc). That's something I am hoping to spend time working on in the new year.

The other thing to think about is what other side-effects a mode-switcher will have. In future developments, people will maybe want to customize the simple mode more than just hiding a few things, which will create more code to complexity to manage. Just something to consider.

Probably a bit obvious that I'm not super convinced about this approach. I've been doing UX for quite some time, and I've just found that many issues related to something being "hard for noobs" can be reduced by explaining them better (meaning in a way that makes sense from the users perspective) and providing more support at each step of their actions. So I'd try that first, and then if that fails, look into the harder simple/full feature switch.
 



## medusadigital | 2018-12-20T08:58:51+00:00
personally I am not a fan of software which has the abilities to switch modes.

If there is mode switching it means:

-The target userbase wasnt statisfied by the software, which means we have the wrong targeted userbase or the wrong software.  Since the official GUI always should have been (and nowdays is) a tool for power users, personally i think there was a shift of what the "target user" is and can do. 

-QA becomes nearly impossible since options multiply with each other. having 2 modes of doing things basically means everything needs to be tested twice. 


I definitely tend to belive that its impossible to make a software that fits for everyone. An alternative, separate implementation of such an "easy mode" wallet is therefore the way i would personally prefer to go ( if even necessary, since there is MyMonero Desktop app, but i guess thats another discussion).


A worthy compromise seems to be the extension of the onboarding wizzard and better explanation of the selectable options there. Let the wizzard give non power users certain pre-configurations (like potential remote nodes to use), which he can either keep or change. 

changing the application layout and disable items depending on which mode the user has selected, i would consider complicated and dangerous design.




## selsta | 2018-12-20T12:31:31+00:00
While I liked the idea of a simple mode at first, I’m starting to doubt it. I think the current approach is fine, with advanced options hidden by default. The biggest problem new users have is with a local/remote node.

Maybe someone can design a nice interface which has two easy options (automatically connect to a remote node, local node with remote bootstrapping), while advanced options (custom remote node, no bootstrap) are hidden by default. The wizard should also have simple pre-configurations, like @medusadigital suggested.

Super simple clients are IMO out of scope for the GUI and are better suited for things like MyMonero.

## dEBRUYNE-1 | 2018-12-20T19:10:17+00:00
@Gingeropolous - I think we should not isolate the matter of using a centralized node aggregator. Rather, let us use a dynamic view. That is, whilst a node aggregator is invariably significantly more centralized than a feature such as node-o-matic, it will also invariably provide better performance, which results in a more positive user experience. As a result, there would, most likely, be more people using Monero and thus performing transactions, thereby strengthening the anonymity set of the whole network. Additionally, some simple mode users might eventually switch to running their own local node, thereby improving the strength and decentralization of the Monero network. I guess what I'd like to say is that we should be aware of positive second-order effects that may occur from initially choosing the more centralized option.  

---------------------

@ProkhorZ:

>It would be confusing to have both an Advanced mode and an Advanced page within the advanced mode. Can we brainstorm another name, e.g. Complete or Expert mode?

I concur. I'd personally support using either of those names. 

>Here, I'd also suggest removing the option to restore from keys (which look like weird gibberish to normies).

This feature is typically used for people wanting to migrate from MyMonero (or another service that utilizes 13-word mnemonic seeds). That is, the 13-word mnemonic seed MyMonero uses is incompatible with the GUI and therefore users have to resort to using the private spend key and private view key in order to properly migrate. 

>And let's take this opportunity to rename 'mnemonic seeds' (animal, vegetable, mineral???) to 'recovery text'.

Mnemonic seed is an ubiquitous term in the Monero ecosystem though. Anyone interested in becoming acquainted with the specifics can google "mnemonic seed Monero" and get a variety of decent information, By contrast, "recovery text" would probably not yield any proper information. 

---------------
@riscphree:

>Having a nice toggle switch for advanced options is still nice (esp mainnet, testnet, stagenet).
There are times when I just want a wallet quick and fast, and other times I'm tinkering so having other advanced options still in is also nice without the added secondary wallet software I might end up needing.

Mode switching would still be fairly easy because one can simply close the current wallet, select the desired mode in the wizard, and reopen the wallet. 

---------------

@GBKS:

>For that, we would need to explain things better, provide more support when errors happen, split up user flows more (e.g. splitting the send screen into individual ones for amount, address, fee & confirmation, etc). That's something I am hoping to spend time working on in the new year.

>Probably a bit obvious that I'm not super convinced about this approach. I've been doing UX for quite some time, and I've just found that many issues related to something being "hard for noobs" can be reduced by explaining them better (meaning in a way that makes sense from the users perspective) and providing more support at each step of their actions. So I'd try that first, and then if that fails, look into the harder simple/full feature switch.

In my opinion, the UI should, if the user is not particularly tech-savvy, be self-explanatory. Furthermore, from experience I can tell that users typically do not read instructions. Moreover, I've, for example, rarely encountered people that had issues with using an iPhone. The GUI, at least in simple mode, should be similar to that. 

P.S. The proposed split up of user flows would probably be beneficial though. 

-------------------

@medusadigital:

>-The target userbase wasnt statisfied by the software, which means we have the wrong targeted userbase or the wrong software. Since the official GUI always should have been (and nowdays is) a tool for power users, personally i think there was a shift of what the "target user" is and can do.

First and foremost, I don't think we should restrict the software to a single subset of the userbase, especially since, after the recent cryptocurrency bubble, it has evolved significantly. 

When cryptocurrency was in its infancy, the userbase predominantly consisted of people that were relatively tech-savvy. However, as adoption increases, the percentage of relatively tech-savvy users will invariably decline. As a result, the GUI will, over time, become less and less tailored to the user base. 

>-QA becomes nearly impossible since options multiply with each other. having 2 modes of doing things basically means everything needs to be tested twice.

Somewhat agree here, but I think we can minimize the risk of bugs due to introducing a new mode by keeping the code fairly clean (which I think can be achieved by simply disabling features). 

>An alternative, separate implementation of such an "easy mode" wallet is therefore the way i would personally prefer to go 

Creating a separate official simple GUI wallet will probably be even more difficult to maintain. In addition, fluffypony would, until deterministic builds are properly functioning for the GUI, have to perform builds for both wallets and we are all aware that he only has limited time available currently. 

>A worthy compromise seems to be the extension of the onboarding wizzard and better explanation of the selectable options there. Let the wizzard give non power users certain pre-configurations (like potential remote nodes to use), which he can either keep or change.

I think this would not lead to a significant improvement, as, and to reiterate, from experience I can tell that users typically do not read instructions. Furthermore, having more options might simply cause confusion for the user. 

----------------

@selsta:

>Maybe someone can design a nice interface which has two easy options (automatically connect to a remote node, local node with remote bootstrapping), while advanced options (custom remote node, no bootstrap) are hidden by default

Would we not basically achieve this by creating a simple and advanced mode? 

>The wizard should also have simple pre-configurations, like @medusadigital suggested.

I'd argue using pre-configuration via implementing different modes would be a more elegant and user-friendly solution. Also, the less a less tech-savvy user has to choose, the better his user experience will be in my opinion.

>Super simple clients are IMO out of scope for the GUI and are better suited for things like MyMonero.

Disagree. Imagine being a user new to Monero. You'd probably browse to the website first and download the official GUI, as it can arguably be perceived as the most trustworthy wallet in an ecosystem where wallet options are somewhat scarce. Now, if you are relatively less tech-savvy, you will probably have a negative user experience and you may not look for another wallet that is better suited. Additionally, you may tell your friends about the negative user experience you incurred whilst using the official Monero wallet. Overall this negative user experience may be detrimental to the development of the Monero ecosystem.

--------------------

To conclude, I personally we think we should at least give simple mode a shot for *one* major release. Without actually implementing it we can, for instance, not say with certainty whether:

- New users are content with this particular mode
- The existing community is content by the addition of this particular mode
- Quality assurance is still manageable

If simple mode turns out to have a negative impact, we can simply remove it in the major release thereafter. Sure, dev time would have been wasted, but we could at least with certainty say that the addition turned out to be not beneficial. 

## SBSeed | 2018-12-21T09:47:19+00:00
this is a good idea, streamlining for a very simplified version of the GUI...
i would suggest that this should be used as a kind of learning tools to start with.

this is why i had suggested that all the parts of monero should be combined into a single program...
i would suggest 3 forms of a GUI wallet:
- first would be practice wallet only, everything included within the GUI witch should really be completely offline allowing new users the chance to get to know the very basics...
  = include ability to 'send/receive' fake monero generated via fake mining or something
  = pop-ups and pointers to show what different things do

- second version, a remote node bootstrap like you said that would allow actual usage of real monero
  = buy/sell simplified
  = choice of TRUSTED remote nodes maybe from a list
  = possibly ad a list of exchanges where people can buy/sell safely
  = a list of stores or exchanges for buying amazon stuff etc. using monero

- third version, a more advanced version of the GUI allowing full customization
  = remote/local nodes
  = integrated XMRig as well as the monero pool mining
  = advanced menu/settings
  = paper wallet/possible setup of hardware wallet using schematics
  = USB wallet setup (this should really only hold the set or new address for exchange)
  = how much CPU usage min-max
  = physical/virtual memory usage min-max
  = ibdm file sizes (hopefully)
  = ability to use console commands to set/force other options

i would also suggest using an advanced form of logging/crash dumps...
things this should be able to see/record
- PC time of start/stop of any/all monero activity (depending on level of logging)
- all background programs running at time of crash/freeze (where possible)
- last good download/input hash blockchain data
- any programs that might be blocking/halting monero in any way
- forced idling by the computer (if possible what OS drivers or other might be causing this)
- any glitches/bugs/bad sectors/etc. from hard drives whether its SSD or HDD

(wonder how feasible it would be to create a dedicated core team of maybe 5-10 people, outside of financing, to work on the core and integration of all parts of monero into the GUI)

## Gingeropolous | 2018-12-21T13:48:04+00:00
> Anyone interested in becoming acquainted with the specifics can google "mnemonic seed Monero" and get a variety of decent information, 

a new user shouldn't have to google their way through new software. 

> I guess what I'd like to say is that we should be aware of positive second-order effects that may occur from initially choosing the more centralized option.

I get that, but I guess what I'm trying to say is that we should be aware of first order effects that may occur and be really bad. I mean, this is volunteer effort - this whole side of things. How are we gonna get 100% uptime? Hell, even the more important infrastructure doesn't get 100% uptime ( seed nodes get wonky here and there). And again, who is running this? If the node aggregrator turns on us, you got a whole bunch of noobs that have no idea wtf is going on. 

I just don't get it. This seems like absolutely needless centralization. The automatic node scanning works on a phone. This seems like something a monero clone would do. 


## SBSeed | 2018-12-23T08:41:26+00:00
> > Anyone interested in becoming acquainted with the specifics can google "mnemonic seed Monero" and get a variety of decent information,
> 
> a new user shouldn't have to google their way through new software.
> 
> > I guess what I'd like to say is that we should be aware of positive second-order effects that may occur from initially choosing the more centralized option.
> 
> I get that, but I guess what I'm trying to say is that we should be aware of first order effects that may occur and be really bad. I mean, this is volunteer effort - this whole side of things. How are we gonna get 100% uptime? Hell, even the more important infrastructure doesn't get 100% uptime ( seed nodes get wonky here and there). And again, who is running this? If the node aggregrator turns on us, you got a whole bunch of noobs that have no idea wtf is going on.
> 
> I just don't get it. This seems like absolutely needless centralization. The automatic node scanning works on a phone. This seems like something a monero clone would do.

this is NOT centralization, this is consolidation of the monero GUI not monero the currency...
this is not to control the blockchain, this is to refine the software that access' and mines monero....

its massively important to understand the differences here and use the correct terms.
it is to make it easier to for people who are completely new to monero and specifically the GUI wallet, and the suggestion is to remove or make the learning curve for the software and interactions less painful so that new users of the GUI wallet can be up and running quickly and have a easier time understand and learn in a more instructive/natural way...

new users will be able to setup Monero-GUI wallet within a few minutes, buy/sell monero, and learn the rest of the technical side of digital/cryptocurrency and not feel like they are in the middle of the ocean with nothing to keep them afloat.


as to that, i would like to amend something to my suggestion...
that it would be possible and maybe easier to have all 3 levels of monero-gui-wallet in a single program...
setup> select language > user level - new user/ have used before/ advanced user > creation of wallet
- better pop-up information and explanations with ALL 3 levels of monero-gui-wallet
- create a FAQ page, maybe a page that explains in more detail what specific things do.

## GBKS | 2018-12-23T11:15:09+00:00
Another thing to consider is that the wallet doesn't have to carry the full weight. Before people use the wallet, they come to the website and have to download it. Those are also good opportunities to help users out and explain basic concepts before they are even touching any UI. For example, the download page could feature a prominent intro video on how to set up a wallet ("Watch the tutorial while you're downloading"). I think there's a lot that can be done pre-wallet.

I'd really like to explore all of these approaches with designs mockups in the new year. Having things visualized can make it easier to decide as a group.

## Gingeropolous | 2018-12-23T14:16:13+00:00
> its massively important to understand the differences here and use the correct terms.
it is to make it easier to for people who are completely new to monero and specifically the GUI wallet, and the suggestion is to remove or make the learning curve for the software and interactions less painful so that new users of the GUI wallet can be up and running quickly and have a easier time understand and learn in a more instructive/natural way...

> new users will be able to setup Monero-GUI wallet within a few minutes, buy/sell monero, and learn the rest of the technical side of digital/cryptocurrency and not feel like they are in the middle of the ocean with nothing to keep them afloat.

And this can all be done without a default, behind-the-scenes connection to a single node aggregator.

I'm really lost here.  

## dEBRUYNE-1 | 2018-12-23T16:46:03+00:00
@Gingeropolous:

>a new user shouldn't have to google their way through new software.

You're completely missing my point here. The GUI already explains what a 25 mnemonic seed is and that it's required in order to be able to restore / recreate one's wallet. A user might be interested in "becoming acquainted with the specifics" of the mnemonic seed though. He can then google "mnemonic seed Monero" and get a variety of decent information. By contrast, if the term would be changed to "recovery text", a user would probably not be able to obtain any proper information with a quick google search. 

>and be really bad.

Define really bad? I don't see how using a personal node aggregator is any worse than using any of the current node aggregators. 

>And again, who is running this? 

dsc would mainly be running it, but the intention is to share access credentials with a few other contributors in case he vanishes. 

>If the node aggregrator turns on us, >you got a whole bunch of noobs that have no idea wtf is going on.

How's this any different than any of the current node aggregator operators (which includes you) turning on us? 

>The automatic node scanning works on a phone. 

That doesn't mean it's properly suitable for the GUI yet, as @xmrdsc explained above. 

>And this can all be done without a default, behind-the-scenes connection to a single node aggregator.

Your notion of node-o-matic being the holy grail is becoming preposterous. Both methods have their pros and cons, but it looks like you're not even willing to debate with the other side anymore.

Frankly, I think you're missing the whole point of the proposal, which is ensuring the GUI is better tailored to remote node users. These users are typically already using a centralized node aggregator. Thus, nothing would change in this regard. Furthermore, the centralized aspect would be confined to the simple mode of the GUI and not affect the advanced mode, which, by the way, would still be the default. 

------------------

@GBKS: 

>For example, the download page could feature a prominent intro video on how to set up a wallet ("Watch the tutorial while you're downloading")

Do you honestly envision the majority of users watching such a tutorial? In my opinion, the GUI, at least for simple / less tech-savvy users, should be self-explanatory. 

>I'd really like to explore all of these approaches with designs mockups in the new year. Having things visualized can make it easier to decide as a group.

I do agree, however, that it would probably be a good addition to an *intuitive* design / UI. 

## Edan3blov | 2018-12-23T23:33:05+00:00
why is nobody talking about creating a working version for android(70% of smartphones)

this would help maybe more than simplifying GUI for windows,linux,mac.


## dEBRUYNE-1 | 2018-12-24T06:50:35+00:00
@Edan3blov - That will probably be the next step once these modes are implemented. Having a simple mode makes it easier to create a mobile version of the official GUI. 

## Gingeropolous | 2018-12-24T06:55:25+00:00
i dunno how to define really bad. This just seems like the wrong direction. 

> Frankly, I think you're missing the whole point of the proposal, which is ensuring the GUI is better tailored to remote node users. 

I don't think thats the point. The point of the proposal is to ensure the GUI is better tailored to new users that don't want to fiddle with stuff but just want to access their monero. That just happens to mean they will use a remote node. Tailoring it to remote node users would look slightly different IMO. For instance, there would be stats and stuff about nodes or something, so a user could find *the best* remote node. AFAIU simple mode, its point, click, connected. It's tailored for ease of use, not remote node use.

> Your notion of node-o-matic being the holy grail is becoming preposterous. 

Its not the holy grail, the better version is where the monero network itself flags RPC support. Thats the holy grail.

> How's this any different than any of the current node aggregator operators (which includes you) turning on us?

Exactly, which is why I have always advocated to never have remote node aggregator connection as a default, user-independent thing. Thats why there are drop-down boxes in the current implementation if i remember correctly.

> dsc would mainly be running it, but the intention is to share access credentials with a few other contributors in case he vanishes.

Well thats good. Honestly, I don't trust dsc. He's new. I'm not. You're not. If you were the primary one maintaining and running this node list, that would be a different question. Because its trust. And we shouldn't be having a conversation about trust. 

I mean, why not just do away with the default new node aggregator for simple mode and just have the noobs connect to developer-managed daemons? Thats the logical next step, once we realize that even another node aggregator is just going to aggregate the same nodes that the current aggregators are aggregating. Once we realize that some of the nodes on the new node aggregator list are raspberry pies or core2 duo machines on DSL, the thing that will provide the best onboarding experience is simply servers managed by the developers. 

> Both methods have their pros and cons, but it looks like you're not even willing to debate with the other side anymore

The only cons i've seen so far for node-o-matic are these provided by @xmrdsc 

> Not trivial to implement in C++. Not rocket science, however, multi-threading would be required in order to not freeze the UI. Not the end of the world but it would definitely introduce a whole bunch of code which needs to be well written and properly maintained.

I interpret this as "making decentralized systems is hard". That is true.

> You're connecting to other users, who may close monerod unexpectedly - leaving you in search for another peer. Added complaint here is that you might be connecting to a node that exposed their port by accident.

As pointed out above, this is a [moo point](https://www.youtube.com/watch?v=fLwYpSCrlHU). All nodes sniffed out by an aggregator would do this.

> With increased GUI usage, the Monero p2p network would experience something that would resemble an on-going DoS, as each GUI instance is constantly mass-scanning the network for open ports. I don't like the idea of turning the GUI into some kind of Nmap. This is by far my biggest complaint.

I interpret this as "decentralized systems are inefficient", which is also true. Furthermore, thats not how the current implementation of the user-controlled node scanner (node-o-matic) works. It doesn't constantly mass scan. It does it once. I tried it recently. It took less than 10 seconds. You bookmark a node. I guess if you try and connect to it again later and its not there, you scan again. And if the network can't handle clients looking for service, then wtf.

Furthermore, cats out of the bag. There are 10k downloads of monerujo. 

I haven't seen the pros of a default, user-independent connection to a node aggregator yet. 

I guess here's my point. The node listing service as I cobbled together using bash like 2 years ago was always meant to be exactly what it is - a shitty stop-gap measure to help bootstrap things to get to the next level. Someone took it to the next level - monerujo. That application doesn't need shitty bootstraps anymore. 

Although the service is still somewhat shitty. And thats also the point. Its supposed to be just useable enough, but still shitty enough, that eventually the user will climb the effort wall to run their own node, somehow. This has happened. I've had people email me with complaints of the node service, and I tell them that they should run their own node.... and they do. 

And, again, it just baffles me that a third party app is now more decentralized than a piece of software from the monero repository. 

I feel like I'm railing against the dark in here, or into the wind or however that goes, and I'm sure i'm preaching to the choir, and even those on "the other side" of this argument are actually on the same side, etc. 

All in all, [this is the answer](https://github.com/moneromooo-monero/bitmonero/tree/share-rpc), @moneromooo-monero 's repo that does hash for service, and also includes the rpc flag signaling (i think) so we don't have to scan the network anymore. But yes, i get it, this isn't done, and we're here now, and what we have is currently what works. 

So I guess I'll conclude with one question - what are the pros and cons of using a centralized pool of servers managed by whoever was gonna manage this new aggregator?

Pros - we now know exactly what hardware the nodes run, exactly which software, we know exactly how much uptime the nodes have.

Cons - its centralized ....(?)

Now, for the node aggregator - 

Pros - a new user gets a node selected from it without their knowledge. 

Cons - its the same kind of node aggregation as before (AFAIU - if there are developments to make a better node aggregator, then great! But now we're getting into the whole code maintenance problem again). The aggregated nodes are volunteered, and could be full of core2duo's on DSL that are capable of serving 2 blocks a minute. We can't check which version of the node software the volunteers are running (see recent cache bug). We can't trust that these node operators are actually serving the real blockchain, because our node aggregators only check height. We can't guarantee any kind of uptime. 

If our goal is a smooth user experience for a new user that doesn't want to / can't run a node, the choice is clear. We should just buy a years worth of 3 servers and get a proper load distribution thing setup. 

I mean the thing is that I ultimately agree with you - I want the GUI to be fast for new users coming onto monero. You know this. This solution - a simple mode with a node aggregator connection under the hood thats default with no explanation - just seems like such a push towards centralization that we might as well just provide the goddamned servers ourselves so new user onboarding will be guaranteed functional. Cause I guarantee (unless the new node aggregator has some kind of vetting schemas, algorithms, or tests or something) that new GUI users in simple mode will still have shitty node service. Some rather large percent of new users will click through the 3 windows or whatever its reduced to, and then see status bars that don't move and a thing that says "not connected".

## Edan3blov | 2018-12-24T09:32:33+00:00
i insist that is more important to create a working android version!
anyone has a smartphone now.

put some maths and u'll c that people will adopt much faster because of android 

smartphones are powerful they have big enough data disk even for 49gb that blockchain is.
because of bulletproofs blockchain size wont go very fast.

android gui need very little work because is almost ready.

## SamsungGalaxyPlayer | 2018-12-26T16:24:15+00:00
I agree with @Gingeropolous. There are pros and cons to using a remote node scanning feature and a default configuration to connect to a preset group of servers. However, I am of the opinion that it is best to use a scanning feature natively. If dsc wants to support the network, they can run more nodes with open RPC ports.

There are some usability limitations when connecting to unreliable nodes and other considerations that @dEBRUYNE-1 discussed, but these are often shared with remote node aggregators. Unless all the nodes are maintained well, this will be a small issue that the client needs to deal with. Monerujo helps limit these issues by testing the server ping and block height. There are ways to mitigate these annoyances.

I generally do not think it is a good idea to configure the GUI to push new users to this simple mode that connects them to a list of selected servers automatically. I share the desire for users to not worry about networking, but I have clearly indicated that I am in favor of a solution that scans the network for open nodes in #602.

Monerujo has a good working implementation of this remote node scanner, and it has made using Monerujo a million times more convenient. While I am willing to entertain other arguments in favor of a trusted party running some of these nodes, this is a significant additional expense, we are trusting them with a ton of user network data, and it seems mostly antithesis to decentralization.

We don't need to re-invent the discussion here. We discussed the option of adding a remote node dropdown list in the GUI in [PR 605](https://github.com/monero-project/monero-gui/pull/605).

## moneromooo-monero | 2018-12-26T17:10:44+00:00
> ensure the GUI automatically connects to a remote node

That is sabotage. It means people may not even realize they're made to do the wrong thing, and even those who might to do the right/safe thing won't if they don't realize.


## moneromooo-monero | 2018-12-26T17:41:58+00:00
After a chat with someone, it seems that this will be opt-in, rather than automatic as implied above.
If the risks (you trust the server to be honest) are made clear to the user before a conscious choice, then it'd be OK. Automatic connection to a remote would not be (IMHO).


## BigslimVdub | 2018-12-26T19:23:36+00:00
Moo, I see your point on specific note of “automatic connection”. Although if one were to design a specific separate GUI wallet application with this feature and also inform users upfront about its action, it would not be so misleading. 
Integrating this function to the core gui wallet, IMO, is not the best route as stated before /\. 

## Edan3blov | 2018-12-26T20:21:36+00:00
i agree with moneromooo.

the reason of crypto rise is lack of trust so very dangerous this “automatic connection".

## Gingeropolous | 2018-12-27T15:42:42+00:00
@moneromooo-monero 

> After a chat with someone, it seems that this will be opt-in, rather than automatic as implied above.

It would be great to get clarity on this, because as I understand it (through this post and discussions), the user is presented (via the wizard) to select either simple mode or advanced mode. Simple mode then automatically connects them to a remote node from this new aggregator service. 

## SamsungGalaxyPlayer | 2018-12-27T19:56:40+00:00
@Gingeropolous exactly. "Opt-in" = "user selects simple mode"

## SBSeed | 2018-12-27T23:36:29+00:00
basically...

something else i have thought of that SHOULD be included with this, if it is possible to create the  3-tiered system i have suggested above, there should not only be a list of known good remote node connections to choose from but also a way to add/suggest new remote nodes as well as some way to rate trust of each node potentially....
this would keep the remote nodes in competition and allow the continuation of decentralized remote nodes since you are not automatically joining a single node that you do not know about.

## dEBRUYNE-1 | 2018-12-28T08:56:09+00:00
>the user is presented (via the wizard) to select either simple mode or advanced mode.

Yes, but the mode where the user runs his own (local) node would be selected by default. Thus, a user has to consciously opt-out of this mode and consciously opt-in to (select) the simple mode (for remote node users). 

## Gingeropolous | 2018-12-28T15:35:15+00:00
> Yes, but the mode where the user runs his own (local) node would be selected by default. 

but this is the bootstrap mode, right? which still requires a remote node. 

ok, lets just map this out once and for all.

1) Advanced mode 
2) Simple mode
  a) Remote node only (obviously needs a remote node)
  b) Local node (DEFAULT)... but is this in bootstrap mode?

because a local node without bootstrap won't get the user immediate access to their monero. 



## dEBRUYNE-1 | 2018-12-28T17:17:15+00:00
>but this is the bootstrap mode, right? which still requires a remote node.

Yes. 

>ok, lets just map this out once and for all.

Perhaps this is clearer:

- Simple mode (for remote node users) - A simple user interface where the user automatically connects to a remote node
- Simple mode (for local node users) - A simple user interface where a remote node is used as bootstrap node and where the user syncs his own (local) node in the background. Once the node is fully synced, the GUI will switch from the remote node to the own (local) node. 
- Advanced mode - An advanced interface similar to the current GUI design where nothing is preconfigured. 

In my opinion, it would be best to make `Simple mode (for local node users)` the default as it allows users to immediately use the wallet *and*, eventually, use their own local node. Furthermore, in this mode there is no need to configure anything, which will arguably improve user experience. 

## mmbyday | 2018-12-28T18:59:32+00:00
> * Simple mode (for remote node users) - A simple user interface where the user automatically connects to a remote node
> * Simple mode (for local node users) - A simple user interface where a remote node is used as bootstrap node and where the user syncs his own (local) node in the background. Once the node is fully synced, the GUI will switch from the remote node to the own (local) node.
> * Advanced mode - An advanced interface similar to the current GUI design where nothing is preconfigured.
> 
> In my opinion, it would be best to make `Simple mode (for local node users)` the default as it allows users to immediately use the wallet _and_, eventually, use their own local node. Furthermore, in this mode there is no need to configure anything, which will arguably improve user experience.

Also, we can do a better job using user-friendly terms. Understanding words such as local/remote/bootstrap may be another technical hindrance slowing adoption. Better could be

_ | Wallet Mode | _
------------ | ------------- | -------------
Lightweight | Simple | Advanced
- Lightweight: Quickest way to get started in Monero, with a small privacy trade off.
- Simple: Like lightweight mode initially but will also eventually become a full node.
- Advanced: Use all the features and benefits of Monero. Downloads the blockchain and runs a full node.

My 2 neros.




## Gingeropolous | 2018-12-28T21:03:00+00:00
perhaps amidst these new changes, we should make it so that the wizard automatically checks to see how much free space is on the device. If there is less than 200% of the current size of the blockchain (so, less than 120 GB), then I think the "simple" mode should be greyed out and the only option available is then Lightweight and Advanced.  And if the user hovers over the greyed out Simple mode, it indicates that their device doesn't have enough storage space to keep a local copy of the blockchain, so they will always have to rely on someone elses copy. 





## dEBRUYNE-1 | 2018-12-29T09:40:35+00:00
>Also, we can do a better job using user-friendly terms. Understanding words such as local/remote/bootstrap may be another technical hindrance slowing adoption. Better could be

I agree here. Note that I used the terms merely for convenience purposes. 

@GBKS - Any input on this perhaps? (See @mmbyday's post for reference). 

------------------

@Gingeropolous: Seems like a good idea yeah. @xmrdc / @mmbyday / @selsta / @xiphon:

Any idea about the feasibility of implementing gingeropolous' suggestion? 

## SamsungGalaxyPlayer | 2018-12-29T15:55:41+00:00
We have historically referred to lightweight wallets as MyMonero-style wallets where users hand a service their view key.

## moneromooo-monero | 2018-12-29T18:53:12+00:00
."Lightweight" seems good, so people will select it. You need something like "Degraded privacy", that kind of thing.

## Gingeropolous | 2018-12-29T21:47:40+00:00
Perhaps instead of names for things, they should just be narrative choices:

1. I don't care about network security, privacy, or decentralization. I just want my magic internet money and I want it now. (simple remote only)
2. I care about all the things above, so I will get my own copy of the blockchain and run a node eventually, but I would like to get access to my monero quickly. (simple remote bootstrap)
3. I know what I'm doing. (advanced mode)



## BigslimVdub | 2018-12-30T03:57:37+00:00
```
3. I know what I'm doing. (advanced mode)
```

lol I like this but some people may click this because they have used a crypto wallet before (even though never Monero GUI wallet) and may come up confused for some things as the Monero wallet is more powerful than standard crypto wallets. 

Maybe an 

```
"I've used the Monero GUI before and know what I'm doing."
```
 option?

## Gingeropolous | 2018-12-30T05:36:48+00:00
@BigslimVdub , i figure those users that get cocky can just restart the wizard if they realize advanced mode is over their heads. 

1. I don't care about network security, privacy, or decentralization. I just want my magic internet money and I want it now. (simple remote only)
2. I care about all the things above, so I will get my own copy of the blockchain and run a node eventually, but I would like to get access to my monero quickly. (simple remote bootstrap)
3. I care about all the things above and I have all the patience in the world so I will wait for my node to synchronize to the network like a good p2p citizen. (local node, no bootstrap)
4. I know what I'm doing. (advanced mode)

The key with all of these options is to allow the user to go back once they choose and enter the wallet environment in case they get to the wallet and their like "ooooh i totally wanted the first option because its [MY MONEY AND I NEED IT NOW!"](https://www.youtube.com/watch?v=HX0fIi3H-es)




## sanderfoobar | 2019-01-28T16:55:24+00:00
@Gingeropolous 

> perhaps amidst these new changes, we should make it so that the wizard automatically checks to see how much free space is on the device. If there is less than 200% of the current size of the blockchain (so, less than 120 GB), then I think the "simple" mode should be greyed out......

At this point the user has not selected a blockchain directory yet, so we can't determine if there is enough space. User might hook up an external disk later, while creating or opening a wallet.

## Gingeropolous | 2019-01-29T03:27:25+00:00
well, the software could scan *all* available devices and give a general warning if, say, there's only 20 GB left anywhere on the computer.

Trust me, I've run into plenty of people that were flabbergasted when they learned that monero was creating a 25 gig file in their computer. And yes, that was when monero's blockchain was only 25 gigs. Even though I told them the whooooole concept of cryptocurrency, they didn't get that it would be storing a gigantic database on their computer. 

## sanderfoobar | 2019-01-29T13:13:50+00:00
@Gingeropolous We already have such a warning, but upon looking it up, I think it is currently broken.

https://github.com/monero-project/monero-gui/blob/a6824c68022d0f836e68f372f98f6649248d7264/main.qml#L1156-L1164

Ill fix it...

## dEBRUYNE-1 | 2019-04-23T18:22:05+00:00
This has been implemented in the most recent version of the GUI (v0.14.0.0). I am therefore going to mark it as resolved. 

## dEBRUYNE-1 | 2019-04-23T18:22:10+00:00
+resolved

# Action History
- Created by: dEBRUYNE-1 | 2018-12-19T15:08:48+00:00
- Closed at: 2019-04-23T18:36:45+00:00
