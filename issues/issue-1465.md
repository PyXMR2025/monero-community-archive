---
title: Make the GUI plug-and-play by default and limit the resources used by the integrated
  daemon (monerod)
source_url: https://github.com/monero-project/monero-gui/issues/1465
author: dEBRUYNE-1
assignees: []
labels:
- proposal
created_at: '2018-06-17T14:06:53+00:00'
updated_at: '2019-07-04T06:33:24+00:00'
type: issue
status: closed
closed_at: '2019-07-04T06:33:24+00:00'
---

# Original Description
The recent crypto bubble^tm has caused a great influx of new users, who are arguably relatively less tech-savvy. Currently, by default, the GUI requires a new user to perform a full blockchain sync from scratch before they are able to properly use the wallet. This initial blockchain sync can be a long and tedious process, especially if one is syncing to an HDD. In addition, the feedback received by the user is fairly inferior and the resources required by `monerod` can cause the user's system to become laggy (or, alternatively, the user is unable to use other processes properly). Combining these aspects with the short attention span of contemporary people, an environment is created where the user is, in my opinion, easily agitated by the wallet and thus has a negative user experience. The long initial blockchain sync is also the main culprit of the "missing transaction" issues. Basically, the user will send a transaction to his wallet and subsequently think it's missing because he is unable to see it in the wallet (caused by the blockchain not being fully synced yet). This, arguably, causes even more annoyance. In sum, I feel like the current default setup of the GUI is not properly tailored to the current and potential user base. 

I, therefore, propose to make the GUI plug-and-play by default via the bootstrap node option. This basically allows the user, by (temporarily) utilizing a remote node, to immediately use the wallet (and also see payments sent to it) whilst his local node syncs in the background. The wallet will switch to the local node once it is fully synced. The advantages of this setup are as follows. First, users will generally have a more positive user experience, which furthermore may cause a positive feedback loop (e.g. telling their friends about the positive experience). Second, users will incur less issues and require less support. This ensures less time is "wasted" in the ecosystem on supporting users. Third, eventually it will result in more users running their own (local) node. In addition, it will result in an increase in full nodes. Lastly, increased userbase and usage, which ultimately strengthens the Monero network and ecosystem. The salient drawback of this proposal is that, by default, users temporarily have to incur the trade-offs of using a remote node. However, I think this temporary sacrifice is worth the long-term benefits. 

Now, you might wonder how I envision this practically. I think we can mitigate the salient drawback by letting the core-team host a few remote nodes, which are then hardcoded and used by default. These nodes, ideally, should have large resources to ensure high uptime and great connectivity. Furthermore, a disclaimer page should be added to the wizard of the GUI that allows the user to opt-out and use custom node settings. Also, to prevent the local daemon from causing the system to lag or interfere with other processes, I propose to add `--max-concurrency 2` as default startup flag for the local daemon. This flag basically limits the amount of CPU resources the integrated daemon (`monerod`) is able to utilize.

Monero's greatest weakness is arguably its usability. This proposal, however, has the potential to significantly improve that. Moreover, whilst third-party wallets will eventually improve Monero's usability, it's important that the official wallets are quite user friendly too.

# Discussion History
## dEBRUYNE-1 | 2018-06-17T14:07:01+00:00
+proposal 

## erciccione | 2018-06-17T14:56:22+00:00
I already discussed with @dEBRUYNE-1 this proposal on `#monero-gui`, but i think my opinion can be summarized in

> I tend to agree on everything. Not enthusiast about centralize the bootstrap node on the core team, but seems like the best compromise.

## endorxmr | 2018-06-17T16:27:40+00:00
I like the idea of initially using a remote node per se, but I think it would be a bad *default* behaviour. People's short attention span should not be an excuse to be sloppy, nor the minimum common denominator.  
I think it would be better to have a simple dialog that asks the user how he would like to sync his chain/wallet, with the default option being the standard sync, and the "hybrid" sync available (with a big red warning sign listing the pros and cons of such choice).

This way, people who are wary about their privacy and security have nothing to worry about, and those who are lazy/in a hurry still have the option nicely presented to them. If they're so lazy that they don't even read that screen, it's entirely on them.  
I get it, UX is a big deal and we should strive to improve it as much as we can, but we have to remember that people's money (and potentially safety) are at stake.

TL;DR: make hybrid sync opt-in, rather than opt-out.

## dEBRUYNE-1 | 2018-06-17T17:03:02+00:00
@endorxmr - We have to ask ourselves what the majority of our current and potential user base would prefer and subsequently tailor the GUI default settings to that. 

>This way, people who are wary about their privacy and security have nothing to worry about

Shouldn't those who are particularly worried about privacy and security at least read a disclaimer that allows them to opt-out? I'd deem them fairly foolish if they wouldn't. In addition, don't you think that these kind of users would rather use the CLI? 

## dginovker | 2018-06-18T01:27:48+00:00
I think the real problem isn't that you have to sync the full blockchain - It's that Monero is inherently complicated to set up for beginners.

Consider a beautiful wallet for another Cryptocurrency: You open it, it's seamless. You type in a password, it's instant. It displays your balance, it's beautiful.

Monero lacks this.
Official wallets download the full blockchain and frequently have troubles.
New users are left wondering why their Minecraft game no longer runs.
Intermediate users still have difficulty troubleshooting the problems.


Monero needs a new wallet - A simple wallet that beginners all see first. And it needs to come from the Monero Project itself, where it will receive proper attention from the beginners and can have a link hosted on GetMonero.org.

Keep the GUI how it is. Keep the CLI how it is. Lets not mend the symptoms, lets fix the problem.

## MoneroChan | 2018-06-18T02:09:52+00:00
"How about both? "
No one default solution will suit everyone, 
Why not add a configuration screen on startup to let users decide easily.

EXAMPLE:

**Welcome to Monero:**
Configuration options:

**Q1: Whose blockchain do you want to use?**
 -   Start with Remote node: "Use someone elses's blockchain, Less secure, Faster Initial start"
 -   Use Local node "Download the blockchain, More Secure, Long time to initial start"

**Q2: How much computer resources do you want this program to use?**
 -   CPU: [____ cores/threads]
 -   Bandwidth Download: [____kbps]
 -   Bandwidth Upload: [____kbps]

**Save Settings**
etc... etc...



## endorxmr | 2018-06-18T06:27:26+00:00
@dEBRUYNE-1 while I agree that privacy-savy people would definitely not overlook such an important configuration step (and that they'd rather use the CLI), I can't help but feel uneasy promoting a bad security practice as a default behaviour...

I like @MoneroChan 's suggestion: simple, flexible, gives users the choice without making things complicated. I think it's the best course of action for Monero's official wallet.  
*Then*, if someone really doesn't want the whole package, we could have a separate download for the gui wallet alone (without the extra binaries for monerod & co.) and skip that config step, directly asking for a remote node to choose.

## pazos | 2018-06-18T16:23:11+00:00
My two cents:

1. AFAIK the Monero Project is a software project that has the goal of writing the reference implementation of both the backbone of the monero p2p network and the API to interact with that network. This includes user interfaces at some extent.

2. AFAIK the Monero GUI is part of the Monero Project, and should follow the same rules of other user interfaces (like the cli or the rpc wallets)

3. It should be a goal of The Monero Project to write good software, promote safe user behaviour (which requires non-opt privacy) and promote a truly decentralized network.  The fact than the Monero Project have a few people in the core team and even few core contributors doesn't mean anything bad to me as long they care to enforce the above goals, and enforce those policies JUST via the reference software repo.

4. If the user interface is easy (or not) to use never was a primary goal of the Monero Project. It is a good thing to have but not at the expense of decentralization/privacy loses.

5. Creating more apealing user interface is (at some extent) work to be done by the ecosystem created around the core project, but not by the core project itself.

6. Educating users about what happens, (ie: why I need to download the whole blockchain?, why I can't see my balance during syncing?, why my "SPV" wallet need to download hundreds of MB to sync the wallet? should be part of the project goals, and not expected to be done by 3rd party software.

So, to resume:

I am perfectly happy to use 3rd party software (or infrastructure) like Monerujo or Mymonero. They can give whatever they want because they have skin in the game, and I, as a user, can choose if I'm ok with their pros (like instant, easy use) vs their cons (3rd party trust).

I won't be happy if the gui (or the cli or the rpc) wallet gives me some sort of "randomly selected" node and at the same time tries to educate me about "some" privacy issues that would came derived for using it.

My english is awful, I know :cry: 

## philkode | 2018-06-18T17:56:12+00:00
I wholeheartedly agree with this as default behaviour for all the reasons outlined by @dEBRUYNE-1, but I also see merit in @MoneroChan's points. I do, however, think that most non-tech-savvy people would have no idea what to enter into fields asking about cpu cores and bandwidth.

I think a good compromise may be to have a fairly basic initial setup wizard that has bootstrap node enabled with sensible cpu/bandwidth settings as default (and hidden from the user), with a button or clickable text for "Advanced options", which will then allow users to manually set core usage, bandwidth, node settings etc.

## clearwater-trust | 2018-06-18T21:48:19+00:00
@pazos - I see the temptation to leave 'good UI' to 3rd parties.

> AFAIK the Monero Project is a software project that has the goal of writing the reference implementation of both the backbone of the monero p2p network

The goal of a working GUI should be included in the 'reference implementation'

> It should be a goal of The Monero Project to write good software, promote safe user behaviour (which requires non-opt privacy) and promote a truly decentralized network.

A working GUI should be considered a good, safe, and decentralized part of the 'reference implementation'

> If the user interface is easy (or not) to use never was a primary goal of the Monero Project. It is a good thing to have but not at the expense of decentralization/privacy loses.

Is a functional GUI too expensive to include in the 'reference implementation'?

I think providing a functional GUI should be considered part of the 'reference implementation' 

Your English is better than mine... and it's the only language I know how to speak!




## pazos | 2018-06-19T01:00:36+00:00
@clearwater-trust: a working GUI is a matter of fixing bugs, not a matter of incentive new users to use a non trusted source to verify their own transactions. Those new users won't get a better experience for connecting to a remote peer while downloading the blockchain because:

1. Verify monero's blockchain is CPU intensive. You can reduce that at the expense of "downloading" waaaay slower
2. Remote hosts can be unreliable because they are sending blocks to you (and to a bunch of other people) and providing rpc acess at the same time (again to a bunch of people).
3. You'll need to scan the blockchain with your private keys to see your transactions, which is - again, cpu intensive.

I think that most users would get a better experience if they download the blockchain themselves, and while this happens they can try to connect to a remote node (better on other device, and maybe even with another soft like monerujo or cake wallet) or use a 3rd party service like mymonero/openmonero.

At the end of the day you will get what you are willing to give. If a lot of new users connect to a remote node the connection will be poor, the experience will be bad, users that are willing to run a node to serve other peers will see their expenses growing and when/if they need to switch to a remote node they will find that most of them are bloated.

AFAICT there are two ways of doing that. One is educating people about what a p2p network is and the other is myetherwallet, because did you try to run an ethereum node? LOL


## clearwater-trust | 2018-06-19T01:20:01+00:00
@pazos - I agree.

**What's really happening.**

The core devs are clearly sabotaging the GUI in favor of their own commercial wallet offerings.
[https://np.reddit.com/r/Monero/comments/8rkwyt/unofficial_release_of_gui_wallet_version_0122/](https://np.reddit.com/r/Monero/comments/8rkwyt/unofficial_release_of_gui_wallet_version_0122/)

Why fix the GUI when you can steer all users to MyMonero, Cakewallet and who knows whatever else 3rd party solution that throws a monero party.

This is what happens when your key signer runs the largest wallet on the network. 

I love @fluffypony - but we need a working GUI, already. 

## stoffu | 2018-06-19T03:02:18+00:00
@pazos 

> 4. If the user interface is easy (or not) to use never was a primary goal of the Monero Project. It is a good thing to have but not at the expense of decentralization/privacy loses.

In my view, ease of use must be part of the primary goals of the Monero Project, because the easier to use the software is, the more users there will be, hence better privacy. Achieving ease of use without compromising security and privacy should be the holy grail of the project.

I think the suggested idea of hosting a set of remote nodes operated by trusted community members for new users syncing their local nodes using the bootstrap mode is quite practical. This approach would be especially effective when combined with a micropayment mechanism where public node operators are incentivized by receiving low difficulty shares from connected wallet users. I've worked on that idea recently (https://github.com/stoffu/monero/tree/pow-quota) without knowing that @moneromooo-monero has already worked on it too with much more engineering (https://github.com/moneromooo-monero/bitmonero/tree/share-rpc), and overall the idea seems quite workable. If this scheme is deployed, new users will naturally be motivated to NOT use remote nodes because the service isn't free (they need to keep paying with CPU power).

@clearwater-trust 

Your criticism against @fluffypony is quite baseless and disrespectful. Your voice doesn't carry much weight because you've done no contributions to Monero so far.


## clearwater-trust | 2018-06-19T03:08:39+00:00
I agree. Most of my ramblings are baseless. I mean no disrespect.

Now, let's get a working GUI together.

**If I see another plea for funding while the GUI remains broken, I'm going to scream!** 

## krtschmr | 2018-06-20T10:35:01+00:00
fluffy gone and we go directly less privacy by default. yay :>

+1

## fluffypony | 2018-06-20T10:37:54+00:00
@krtschmr I’ve gone nowhere.

@clearwater-trust the GUI has always been a challenge in terms of making sure it works across the board. In hindsight, maybe QtQuick wasn’t a good idea, but given the security issues that have plagued Electron it was a reasonable design decision when we first started on it in 2014.

@debruyne-1 what if there was a dialog asking if they want to start in full node mode, or quick start mode, with a note that it “may take a day or two” for full node mode to sync?

## kieranc | 2018-06-20T13:01:16+00:00
"May take a day or two" seems vague, what if it tested downloading some blocks to get a semi-accurate idea of how long a full sync will take? Then the user can make a more informed decision. 

## pazos | 2018-06-21T00:17:02+00:00
@kieranc: it is pretty difficult to get an ETA cause we are downloading & verifying blocks with dynamic sizes and the first hundreds of thousand of blocks seems almost empty :P

not sure about how to know when the blockchain is downloaded in the gui without asking the daemon again and again. In fact this seems the root cause for unresponsive behaviour in the gui (and more workload to monerod).

We're starting monerod process detached from the gui, so we can't get info directly. If we start the process without detaching then we can do something like

```
    connect(p, &QProcess::readyReadStandardOutput, []() {
            auto feed = p->readAllStandardOutput();
            emit updateLog(feed);
            if (feed.contains("Loading blockchain"))
                emit updateStatus(tr("Loading blockchain & checkpoints, this might take some time"));
            if (feed.contains("daemon will start synchronizing"))
                emit updateStatus(tr("Daemon will start synchronizing"));
            else if(feed.contains("You may now start monero-wallet-cli"))
                emit updateStatus(tr("You are now synchronized with the network"));
            else if(feed.contains("Synced"))
                emit updateStatus(feed, true);
    });

```

This can give the user more feedback during monerod initialization (ie: in the splashscreen), and it signal when the blockchain is ready for switch to a local node.

The code is for another project, and some things don't apply here, but you'll get the idea


At the same time, starting monerod this way will allow us to use p->write(command) instead of using another instance of monerod to communicate via rpc (which will block the ui  waiting for finished)

## dEBRUYNE-1 | 2019-07-04T06:33:24+00:00
This idea has been implemented with the addition of the simple modes (as well as concurrency limiting for `Simple mode (bootstrap)`).

# Action History
- Created by: dEBRUYNE-1 | 2018-06-17T14:06:53+00:00
- Closed at: 2019-07-04T06:33:24+00:00
