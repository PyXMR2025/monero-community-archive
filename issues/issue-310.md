---
title: '[Discussion] Reaching consensus on wallet nomenclature'
source_url: https://github.com/monero-project/meta/issues/310
author: SamsungGalaxyPlayer
assignees: []
labels: []
created_at: '2019-03-06T00:28:27+00:00'
updated_at: '2019-03-21T22:55:09+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This is a discussion we've needed to have in the community for a long time. How do we name the different types of Monero wallets?

The following was taken from the Monero website FAQ:

![image](https://user-images.githubusercontent.com/12520755/53846070-25d3c280-3f71-11e9-8813-526e5ceea9bf.png)

This definition doesn't really do a great job covering the nuances of different wallet types. Below are a list of some common Monero wallets and how they function:

**Official CLI and GUI**: these wallets can operate with local full nodes or connect to remote nodes. The view key and private key are kept on the device. They are not given to the remote node.

**Monerujo, Cake Wallet, X Wallet**: these wallets connects to a specified remote node. The view key never leaves the device.

**MyMonero, Edge Wallet**: the view key is given to the MyMonero server for efficiency. There is privacy degradation. MyMonero offers for users to specify a different remote server, which could be the user's own remote MyMonero-style server.

In my opinion, there are two distinguishing traits of wallets:

1. What happens to the keys

2. How the wallet connect to nodes

There are three main ways wallets can handle keys. 1) they can keep the view key and spend key on the device and never give them to anyone. This is bad for efficiency, but it's good for privacy. 2) they can hand over the view key, either temporarily or permanently. This is good for efficiency but bad for privacy. 3) they can hand over the spend key (and the view key). This is bad for privacy and security; it's a custodial wallet.

For these different processes, I recommend using the terminology: 1) full / non-custodial, 2) efficient, 3) custodial. 

There are likewise several ways of connecting to nodes to send transactions and receive network data. 1) wallets can connect to a local full node, as recommended in the official CLI/GUI. 2) wallets can connect to remote nodes or MyMonero-style servers over the clearnet. 3) wallets can connect to remote nodes or MyMonero-style servers over an anonymizing network, such as Tor or i2p. 2 and 3 are interesting since it's technically possible for someone to manually configure this; I believe that the wallet should be identified by the way the user is currently using it.

For these, I propose the terms 1) direct, 2) remote, and 3) remote hidden (perhaps simplify to *hidden*?)

We can thus identify these common Monero wallets as follows:

* **Official GUI/CLI**: *full direct*, *full remote*, or (eventually) *full remote hidden*

* **Monerujo, Cake Wallet, X Wallet**: *full remote*

* **MyMonero, Edge Wallet**: *efficient remote*. If the MyMonero app used Tor connections by default, it would be *efficient remote hidden*

* **Kraken**: *custodial remote* or *custodial*

---

Almutasim from Monero Outreach proposed a different set in a recent unpublished article. They refer to wallets that use remote services as "privacy-enhancing" (for remote node connection) or "efficiency-enhancing" (for MyMonero-style connection). I believe that "privacy-enhancing" is misleading; users lose privacy when connecting to remote nodes compared to running a full node. Users of the GUI/CLI that use remote nodes are not running it in "privacy-enhancing" mode.

I think it's important to stay away from terms like "privacy-degrading," since there are many use-cases where privacy is not reduced. Users can set up their own MyMonero-style server and entrust it with their view key. This does not degrade their privacy if they trust themselves. Users can likewise connect to their own remote node (eg: at home) for efficiency without losing privacy.

---

I just came up with my proposed terminology today, so it's likely other people can come up with better names. I'm asking for help identifying 1) a label for wallets that don't maintain their own full nodes, and 2) labels for the two types that don't: those that a) share the view key with the server and b) those that don't share the view key.

I believe that using these two identifying characteristics (what happens to the keys and how to connect to nodes) is the best I've thought of yet at getting into these nuances. I'm awaiting the day that Monerujo can ask if users want to run their wallets in "hidden mode!" Identifying these wallet types can help us better communicate the pros and cons of the different types to Monero users.

# Discussion History
## dginovker | 2019-03-06T00:40:23+00:00
Like you, I am _against_ the notion of calling wallets "Privacy degrading" - this approach could end up deterring users into using more unsafe options that sugarcoat the wording more. For this reason I support Almutasim's definition of "Privacy enhancing wallet", simply because it provides the opposite effect, and gives more insight and clarity to the end-user about what's going on. I really don't think "Full remote hidden" or "custodial wallet" mean anything to normal people at all.

## jtgrassie | 2019-03-06T00:45:32+00:00
There is another nuance: public vs private remote node. Using a private remote node (additionally connecting to it over TLS/SSH/Tor/i2p), is really no less secure than using a local node. However, a public remote node can log your IP/usage as could a MITM.

## Mitchellpkt | 2019-03-06T00:46:02+00:00
Agree with above comments, terminology like "efficient" and "privacy enhancing" makes perfect sense to people who already understand different wallet architectures, but has a high chance of causing confusion for general users (who stand to be the main beneficiaries of clearer terminology).

What about jumping straight to the heart of the matter and referring to the owner of the keys. Something like "remote with user-controlled keys" versus "remote with shared keys" or "custodial, no keys". << this is clunky and I am not proposing these as final terms. Just hoping to spark ideas.

## jtgrassie | 2019-03-06T00:51:27+00:00
Also, the topic is wider than just where your keys exists when we're discussing privacy.

## SamsungGalaxyPlayer | 2019-03-06T00:59:23+00:00
I essentially gave up on classifying the node connection types to owned infrastructure or others' infrastructure. This isn't really on the wallet either; the connection *type* is the same no matter what node they connect to. And the wallet doesn't really know if you connect to your node or a friend's node, for example.

I personally believe this should remain out of scope. But it's certainly a privacy consideration.

## jtgrassie | 2019-03-06T01:14:12+00:00
I think it's important owned/others and how you connect. Very quick draft of a breakdown could look like (where "secure" means "SSL/TLS/Tor/i2p"):

|Type|Connection|Strength|
|--|--|--|
|Local full node|localhost|5|
|Private remote node|secure|5|
|Private local network node|secure|5|
|Private local network node|clearnet|4|
|Private remote node|clearnet|4|
|Public remote node|secure|3|
|Public remote node|clearnet|2|
|Private lightwallet server|secure|5|
|Private lightwallet server|clearnet|4|
|Public lightwallet server|secure|2|
|Public lightwallet server|clearnet|1|

It get's confusing but ultimately it's about 3 things - where your keys are, how you connect and who owns. 


## jtgrassie | 2019-03-06T01:17:52+00:00
> I personally believe this should remain out of scope. But it's certainly a privacy consideration.

I'm not so sure. Where keys are is only a fraction of the issue. Education is important IMO.

## knaccc | 2019-03-06T01:24:06+00:00
First, here are the choices, as I'd present them to an end user:

1. Your computer scans the blockchain for incoming transactions (High privacy, but scanning will take some time)
2. Ask a remote server to scan the blockchain for you (Scanning will be near-instant, your privacy depends on their privacy policy).

If they choose option 1, their further choice is:

1a. Download and verify the entire blockchain on your computer, for maximum protection against transaction fraud
1b. Ask a remote server for only the parts of the blockchain you need, and trust the remote server to not be malicious.

So these are three options: 1a, 1b and 2.

To name these in a way that users can still attempt to figure out the meaning without further explanation, this is my most concise attempt so far:

1a. High privacy full blockchain wallet
1b. High privacy, trusted remote blockchain wallet
2. Trusted light-wallet service

To get even more concise:

1a. Full blockchain wallet
1b. Remote blockchain wallet
2. Light-wallet

## jtgrassie | 2019-03-06T01:24:08+00:00
But if you really want to restrict this to "types" of wallets, then really we're talking wallet+local node, wallet+remote node, "openmonero type light wallet" I guess. The last wallet type is not, after all, technically a "monero" wallet (i.e. it's not part of the core Monero codebase). ?

## jtgrassie | 2019-03-06T01:32:06+00:00
I like @knaccc's breakdown if we're only talking wallet types, but still, this can lead to a false sense of security - the public/private remote distinction is missing and how one connects. The moment we start saying "high privacy", these distinctions matter greatly.

## Gingeropolous | 2019-03-06T02:54:58+00:00
I think we should be black and white about it. The most secure wallet is a Full Wallet. The nomenclature is flawed at the next level up, and I don't think we can fix it at this level. These aren't wallets. The blockchain is the thing that actually has your monero. The key to access that monero in the blockchain is... a key. I think if we really want to *fix* this, we call a Full Wallet when you have the blockchain on your computer and the keys on your computer scanning that blockchain. Anything else is a light wallet and should be considered Not As Great. 

It doesn't matter what the mechanism is... remote viewkey scanning, remote node, blah dee blah. If we're talking about the end user, it should be Full Wallet and Light Wallet. Presenting shades of security to end users just complicates things. 

If we're talking about the developer end of things, more nuance is needed. 

## SamsungGalaxyPlayer | 2019-03-06T03:01:02+00:00
Here is the matrix when using three different words to cover these cases. "Hosted" = "infrastructure that you run yourself;" "borrowed" = "infrastructure others run." Same 1-5 (high = good privacy/security) ranking, n/a left blank:

| | Full | Efficient | Custodial |
|---|---|---|---|
| **Direct Hosted** | Full Direct Hosted (5) | Efficient Direct Hosted (5) | |
| **Direct Borrowed** | | | |
| **Remote Hosted** | Full Remote Hosted (4) | Efficient Remote Hosted (4) | |
| **Remote Borrowed** | Full Remote Borrowed (2) | Efficient Remote Borrowed (1) | Custodial Remote Borrowed (0) |
| **Hidden Hosted** | Full Hidden Hosted (5) | Efficient Hidden Hosted (5) | |
| **Hidden Borrowed** | Full Hidden Borrowed (3) | Efficient Hidden Borrowed (2) | Custodial Hidden Borrowed (0) |

Here is the matrix when two three different words to cover these cases. Same 1-5 (high = good privacy/security) ranking, n/a left blank:

| | Full | Efficient | Custodial |
|---|---|---|---|
| **Direct** | Full Direct (5) | Efficient Direct (5) | |
| **Remote** | Full Remote (4 hosted or 2 borrowed) | Efficient Remote (4 hosted or 1 borrowed) | Custodial Remote (0) |
| **Hidden** | Full Hidden (5 hosted or 3 borrowed) | Efficient Hidden (5 hosted or 2 borrowed) | Custodial Hidden (0) |

Here is a PDF that walks through how these names are derived:
[Monero Wallet Types.pdf](https://github.com/monero-project/meta/files/2934155/Monero.Wallet.Types.pdf)

## SamsungGalaxyPlayer | 2019-03-06T03:05:07+00:00
@Gingeropolous I think this discussion can include different names for technical and average use, but I think technical use is more important in this discussion. Once the technical names are sorted out, people can feel more confident making shorter/easier names for wallets.

Perhaps the simple terms can be *full*, *efficient*, and *custodial* without getting into the nuances of how the connections are made and who runs the infrastructure.

## jprichardson | 2019-03-06T03:08:02+00:00
> It doesn't matter what the mechanism is... remote viewkey scanning, remote node, blah dee blah. If we're talking about the end user, it should be Full Wallet and Light Wallet. Presenting shades of security to end users just complicates things.

The revelation of the view key matters. Privacy is the core value proposition of Monero, not convenience. 

If people aren't aware that the company whose wallet they're using reveals the view key to the server and that company gets subpoenaed, everyone's privacy may have been compromised. People need to know this risk.

## jtgrassie | 2019-03-06T03:21:14+00:00
@jprichardson 
> The revelation of the view key matters. Privacy is the core value proposition of Monero, not convenience.

When we're talking about privacy, more than the view key matters though. Just knowing someone is _using_ Monero can be a serious problem. Even worse if you can pinpoint _when_ they are using it. Hence, remote public (e.g. 3rd-party services), especially when used over clearnet, are huge privacy weaknesses.

@Gingeropolous 
> It doesn't matter what the mechanism is... remote viewkey scanning, remote node, blah dee blah. If we're talking about the end user, it should be Full Wallet and Light Wallet. Presenting shades of security to end users just complicates things.

I disagree. We have to educate users IMO. Anything that hides the complexities and dumbs down the risks, when we are trying to provide the most secure and private cryptocurrency, is a mistake. If we can educate people, no matter their technical skill level, we can help them make balanced decisions depending on their use case. Sometimes they may be happy with a lower privacy level for certain transactions and sometimes they may need a high degree of privacy.

## anhdres | 2019-03-06T03:21:30+00:00
Agree with @Mitchellpkt here, taking the non-technical user in mind (which I am), I think @knaccc 
 was closest. Something like this may work and be clear enough. I think we should focus on the workings of the wallet, and then on its privacy implications:

**Full wallet**
_A wallet with its own node, like the official._

**Remote wallet**
_A wallet that has to connect to a node, like Monerujo._

**Light wallet**
_A wallet like MyMonero that also connect to a node but that process is hidden from the user._

**Web wallet**
_A custodial wallet like an exchange. I know it's not accurate but related to the way most users talk about webmail for example, where you're trusting the provider with everything (in most cases)_

These have the most likely level of adoption because it's close to what it's already been used.
If I'm allowed to go more freestyle I'd go:

**Standalone wallet** - has node
**Tethered or satellite wallet** - connects to a node
**Wallet service** - not even a wallet, custodial

Now, for most users that's what they care first about because it involves what they need to setup and how to make the thing work, which is a daunting task in itself when you're not tech-savvy.
if the conversation or context requires it (or in a formal presentation), I'd just add a trust-related prefix and now we're talking about privacy.

For example, psychologically  Monerujo could be a _trustless remote wallet_ and MyMonero a _trust light wallet_
Or visually, Monerujo could be a _opaque satellite wallet_ and MyMonero a _transparent satellite wallet_

I'll shut up now. Good night.



## paulshapiro | 2019-03-06T03:27:07+00:00
@jprichardson MyMonero is not a US company, its code is not held by a US company, its servers aren't in the US, so we can't get subpoenaed by the US gov nor can they tell us to put something in our code. We've gone to great lengths to ensure this.

@SamsungGalaxyPlayer We still think the term "lightweight wallet" still makes sense. It's contrasted with "full wallet".  It does make sense to have a more fully qualified explanation of what a lightweight wallet means, but the term "lightweight wallet" exists in Bitcoin too, and at such a time as the ability to have a lightweight wallet can be evolved on top of Monero technology such that it can be done without disclosing the view-key to the server, we'd all still call it a lightweight wallet. Everyone would move to that superior technology.

I'd like to mention again that lightweight wallets are not just for MyMonero or even for a third party to whom you must disclose your view key. Everyone can run a lightweight wallet server at any time… The MyMonero team, primarily vtnerd, spent a lot of careful effort to write a high quality C++ server to be a companion alongside the Monero daemon so that people can run this at home easily. The code is ready to review and can actually, as far as I know, have the [do not merge] tag removed. That's here: https://github.com/monero-project/monero/pull/4139

There's also OpenMonero, of course. 

The way that we view these servers is basically like a remote full wallet server – and then the actual client itself is basically a "lightweight" interface into that remote full wallet server.

Not to be a negative nancy but I can also find semantic ambiguities in a lot of the other terms that were proposed here... e.g. "satellite" wallet doesn't really convey anything functionally about what's actually occurring or being disclosed… and I think there's quite a lot to be said for taking a term everyone's already used to using – "lightweight wallet server" and simply educating people about what it really means whenever the term is actually used. The fact it's a server means it's doing something for you – it's serving something – and it's a wallet server, so that means it's got to have some information. But the fact it's a lightweight wallet server for Monero also means that the spend key is never sent to that server – something that none of these terms encapsulate either but which is also absolutely critical to the user's understanding of the custody dynamic. 

## jtgrassie | 2019-03-06T03:28:03+00:00
@anhdres I partly agree on the first-use case but also we have to deal with someone who requires a high degree of privacy (first-use or not). It could be a solution to split these out like: "If you just want to get going quickly and not worry about privacy, then here's a quick overview..." followed by a "But if you require a high degree of privacy, here's a more detailed breakdown of your options..." ??

## paulshapiro | 2019-03-06T03:29:10+00:00
I wonder if introducing the word "scanning" somewhere makes sense. Like a lightweight scanning wallet server. But we'd still end up calling it a lightweight wallet for short. The more fully qualified term could be used when explaining it to people... but the wallet is, of course, still lightweight.

## anhdres | 2019-03-06T03:44:18+00:00
@jtgrassie you're probably right, and it's very useful to have a clear page somewhere with both angles covered in a standarized way, like in a wikipedia table. For normal use, what @paulshapiro implied is the truth, only one word will succeed, specially if it's already in use: Full wallet, light wallet, etc.



## jtgrassie | 2019-03-06T03:52:40+00:00
@anhdres yes but @paulshapiro also rightly points out, even in the case of light wallets, it's not simply a case of 3rd-party as you can run your own light wallet server :) 

The fundamental difference in the wallet types is whether you scan the blockchain yourself or let someone else scan it for you (e.g. where your private view key is and where the blockchain is). Then there are all the differences which relate to public(3rd-party)/private and how you connect. It is complicated!

## jtgrassie | 2019-03-06T04:07:01+00:00
needmoney90 just commented on Reddit using the word Hybrid as a differentiator for wallet types. This strikes a chord for differentiating between core wallets and light (MyMonero type) wallets. The word hybrid maybe encourages the user to further research on the wallet types???

## SamsungGalaxyPlayer | 2019-03-06T04:17:02+00:00
@jtgrassie I don't speak for needmoney90, but perhaps they meant that "hybrid" would be used to explain wallets that support different connection types. That it's meant to state "this wallet can fill several boxes." Not that "hybrid" is a specific type of configuration itself.

## Mitchellpkt | 2019-03-06T04:47:37+00:00
@paulshapiro I like your idea to introduce "scanning" since it is both accurate and intuitive (I think?)

Should we separate the non-technical terminology discussion from the technical terminology discussion? i.e. different GitHub issues. They're both important conversations, and mostly unrelated. 

I would caution against using the term "efficient", which states directly and has a lot of *implied* info... X efficient compared to Y, with respect to Z metric, with W tradeoffs... that will not be apparent to most users. This is mostly relevant in the non-tech vocab discussion, but the note holds for tech talk as well. Everything is more efficient than something. :- P 

## Gingeropolous | 2019-03-06T05:14:43+00:00
so it seems that the term i use was only in my comment, so i'll just add it here how I've thought of these things

I've always presented it in terms of what the wallet is connecting to.

Local node   
Remote node   
Remote viewkey scanning node   

so anything remote could be akin to a service provider. A service provider is something people can generally understand. Whats a common equivalent for self hosting? Local might be it but maybe there's something else. I mean, your average user has no idea what hosting is, in terms of computers. There's some intuition there, as well as the word "server". 

Lets perhaps take the angle of money as opposed to computers. 

A local node could be akin to a safe in your house. Its yours, you know the money is in there, no one can really screw with you. 

A remote node is a safe in some other place. It could be some random dudes house, it could be a company. You still have the keys though. 

And a remote viewkey scanning node is a safe thats somewhere else that someone can look into for you to provide some convenience. 

maybe that helps, i dunno. 

## Jasonhcwong | 2019-03-06T08:28:42+00:00
Is there any mobile wallet that support connecting to a Tor hidden service?

## umma08 | 2019-03-06T10:21:05+00:00
The discussion should, in my opinion, be divided down three important (and not wholly unrelated lines). 

1. who holds the private keys (user, custodian)
 
 2. the method through which information is passed from the network to the wallet. (view/scan, remote node, full node)
 
3. the degree of privacy afforded to the user, with respect to 1 and 2 (plus any gateway/router used to leverage increased privacy)

## hokkjoy | 2019-03-15T20:26:58+00:00
There are exactly two types of Monero clients: **autonomous and inferior**.

Also, except for @Gingeropolous, this thread seems  to be blind to the more significant confusion:

_None of the mentioned tools are wallets!_

Trying to change the word from its original meaning may be possible, but it would take decades and it's a major hurdle to widespread use of cryptocurrency:

"Wallet" is one of the first terms a newbie learns and it immediately leads to dangerous misconceptions. It has people believe that their funds are stored inside the software. This, in turn, enforces ideas like creating coins out of thin air just by hacking the local software. And finally, new users are led to believe that only people with access to their copy of the software can access the funds.

**"Wallet" is basically the single word that explains everything that crypto is not.**

If one were to compare the client software to any previously existing concept, online banking would be a much better fit. Apart from the technical differences, at least it matches the main feature:

*Handling the funds associated with your account*

Thus, to describe the software, we need to use synonyms of those words. Examples include fund manager, account manager, account controller, account handler, Monero handler, Monero console, Monero client, Monero terminal, Monero access tool, Monero portal, …

Only after naming the software itself correctly, we can categorize in more detail, based on its level of information disclosure or otherwise:

* Autonomous clients are: private / concealing / independent / trustable / protective / "chained"
* Inferior clients are: revealing / disclosing / dependant / remote / separated / tunneled / "unchained"
* Even more inferior clients are: public / untrusted / sharing / exposing / also "unchained"

(Note that I abstained from using "trusted", since this word is prone to be confused with "trustworthy". Custody providers such as exchanges are not Monero accounts at all. Words like irresponsible or retained come to mind.)

Trying out these words in descriptive phrases:

"CLI or GUI, with monerod, are autonomous account managers for Monero. You will be connected directly to the blockchain."

"MyMonero is an inferior Monero account manager. It uses a middleman to communicate you with the blockchain. Certain information will have to be revealed to the middleman or third parties."

"CakeWallet is an inferior Monero account manager. You can convert it from inferior to autonomous by configuring it to use your own node."

Monero is about learning from Bitcoin's mistakes, not repeating them. We should abstain from using terms that are blatantly wrong.


## hokkjoy | 2019-03-21T22:54:31+00:00
Giving this some more thought, I come to "**detached**" and "**attached**" as descriptive synonyms for differentiating clients that work directly with the blockchain from those that use intermediaries of any kind.

Combining those terms for connection-type with terms that refer to how the keys are treated, we end up with these combinations:

1. attached-protective
2. attached-revealing
3. detached-protective
4. detached-revealing

The second category may be omitted.

# Action History
- Created by: SamsungGalaxyPlayer | 2019-03-06T00:28:27+00:00
