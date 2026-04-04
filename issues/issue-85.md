---
title: Project licensing
source_url: https://github.com/monero-project/meta/issues/85
author: hyc
assignees: []
labels: []
created_at: '2017-07-02T19:48:44+00:00'
updated_at: '2018-01-31T13:03:14+00:00'
type: issue
status: closed
closed_at: '2018-01-31T13:03:14+00:00'
---

# Original Description
I recently announced that LMDB 1.0 is moving to a dual-use license, instead of the BSD-style license on LMDB 0.9. The new license is essentially a clone of the dual-use license originally used by Sleepycat on BerkeleyDB (before Oracle changed things). It allows free use of LMDB in any open source project, and any proprietary projects who do not wish to release their source code as specified can contact Symas for a proprietary license.

Only a few members of the Core Team were online at the time but there was a lengthy discussion about license conflicts, copyleft vs non-copyleft, etc... Some open questions:

* Should the Monero Project, which is currently under a liberal license, continue to use software which is not liberally licensed?
* Should the Monero Project itself change to a dual-use license?


# Discussion History
## hyc | 2017-07-02T19:52:11+00:00
I have a personal archive of old BerkeleyDB releases. The BDB license before Oracle changed it is here https://github.com/hyc/BerkeleyDB/blob/d88162518f939bbf70aa3b6765b4c2d2bd08650a/LICENSE

The new LMDB license is here http://highlandsun.com/hyc/SymasLicense.txt

## Gingeropolous | 2017-07-05T01:00:03+00:00
>     Should the Monero Project, which is currently under a liberal license, continue to use software which is not liberally licensed?
> Should the Monero Project itself change to a dual-use license?

What are the benefits and drawbacks of each choice? 

## hyc | 2017-07-05T01:52:46+00:00
Backing up a step to answer that question - LMDB is being relicensed basically to require everyone who benefits from it to contribute back. In an open source context everyone is contributing, so that's all cool. But proprietary projects are currently freeloaders, and we want that to stop: if you benefit from an open source resource, you have an obligation to contribute back to it.

To answer your actual question - if the Monero Project decides that it will only use liberally licensed code in its dependencies, then it will have to stick to the currently released LMDB 0.9 code, or switch to some other DB with an acceptable liberal license. At the moment, the only DB I'm aware of that would fit the bill is SQLite, which is 100% public domain. (Note that this isn't even a perfect solution; there are many countries where "public domain" isn't a legal status.) LMDB 0.9 is now end-of-life'd and will not receive any new features. It will still receive critical bugfixes if needed. (But, as far as I can see, LMDB 0.9 is totally solid and doesn't need any bugfixes.)

Some work in LMDB 1.0 is occurring specifically because of Monero - i.e., we've added encryption support to LMDB 1.0 specifically to use it in a future version of the Monero wallet. If the Monero Project decides not to continue to use LMDB due to these license issues, in some ways that's wasted work, but the encryption work in LMDB will still benefit other open source projects (such as OpenLDAP) that use LMDB.

On the second question, whether the Monero Project itself should change to a dual-license - I think the benefits are much the same as for LMDB: people who use Monero code and benefit from it will be obligated to pay back in one way or another. If people develop new open source projects around the Monero code, the entire Monero community benefits. If people develop new closed source projects around the Monero code, with the current license, only those particular people will benefit.

Obviously I'm strongly biased but IMO, anyone who benefits from open source software development owes some kind of payback to the open source developers. That payback isn't necessarily monetary - it can be in the form of contributions of documentation, bug reports, bug fixes, and various other forms. All of these help improve the code and strengthen the community. But closed source projects tend to be black holes - they suck in everyone else's contributions and give nothing back. Switching to a dual-use license, which requires proprietary projects to pay for use of the code, is a way to make sure that everyone contributes fairly.

## fireice-uk | 2017-07-10T00:23:01+00:00
Just out of curiosity, what's the rationale for choosing Sleepycat and not GPL as the copyleft license? (I'm thinking Qt here)

## MoroccanMalinois | 2017-07-10T01:24:32+00:00
IIUC, If monero continues with lmdb 1.0, **any company that wants to accept payments in monero** and doesn't want to open-source their solution (exchanges, mymonero, xmr.to ... ) will need to contact Symas for a proprietary license ? at conditions that are not pre-defined ?

This also applies to a simple e-commerce site that would use [prestashop's integration](https://forum.getmonero.org/9/work-in-progress/87734/monero-integrations-with-web-apps) ?


## fluffypony | 2017-07-10T07:29:24+00:00
I'm strongly against relicensing Monero. Having gone through the process with Electrum, I can tell you that it is extremely painful and time-consuming. You have to get hold of EVERY contributor that has EVER contributed, and if a contributor decides they don't agree you have to get someone to rewrite their contribution (this thankfully only happened with a single Electrum contributor, but it was painful).

A multi-month relicense effort is way too resource intensive right now, and I don't see much benefit as altcoins forked from Monero will just ignore the license anyway. I also fear that a dual-license will be problematic for binaries in app stores, which is like 90% of the reason we switched to a liberal license in the first place.

@hyc if I understand correctly, we can run with 0.9 for the foreseeable future, and the only major feature we'd lack (right now) is encryption?

## hyc | 2017-07-10T09:31:30+00:00
@fireice-uk we used it because Sleepycat used it successfully with BerkeleyDB. The rationale being, anywhere BerkeleyDB has gone before, we can go too. Choosing the GPL would make that less certain.

@MoroccanMalinois actually no. This is one of the reasons Oracle switched BerkeleyDB to Affero GPLv3 though. I.e., under the Sleepycat license, if you develop code for your own use that you never distribute to anyone else, you have no obligation to distribute source code. Under the Affero license, you would be obligated regardless of whether you distribute it or not. Also, under the Sleepycat license, if your project only uses the Monero source code, and doesn't call LMDB directly (and thus LMDB is not a direct dependency), then you're considered to be using open source, and you don't need a proprietary license.

@fluffypony As I understood it, app stores require a proprietary license already, so this would actually be an improvement, no? But agreed, relicensing such a large project would be a pain. And yes, Monero can run LMDB 0.9 indefinitely.

## moneromooo-monero | 2017-07-10T10:19:52+00:00
This change is interesting, because I don't think there needs to be a relicencing of past contributions: these were made under the BSD style monero licence, which continues to be available. A company which uses a hypothetical LMDB 1.0 using Monero can still abide by this licence. So nothing changes from the point of view of Monero. The only difference would be a company decided to use LMDB directly, and this has nothing to do with Monero code, which keeps the same licence as it has now.

This assumes that hyc's direct vs indirect use understanding of the sleepycat licence is unambiguously conveyed in its wording, however, and I think this is not there yet.


## fluffypony | 2017-07-10T10:28:21+00:00
@hyc the App Store issue isn't about proprietary vs. non-proprietary, it's that licenses like the GPL have a clause that disallow any additional restrictions. Most app stores have some sort of certificate / signing mechanism to prevent you from just grabbing the package and installing it on another device, or even running the binary on another device. This is an additional restriction, and thus breaks the GPL. Using a permissive license, as we do, allows the app stores to add these additional restrictions without contravening the license. So a dual-license isn't an improvement, it's largely just keeping the status quo from that perspective.

@moneromooo-monero if we change the licensing on the Monero project, in any way, we'd need to contact the original contributors. Dual-licensing is still a change, unfortunately.

I'm not sure if LMDB 1.0's dual license would actually require us to relicense, since we are FOSS and thus the proprietary license doesn't apply to us or even to apps we put in an app store. I'd need to chat to our general counsel (the [SFLC](https://softwarefreedom.org)) to find out.

## fireice-uk | 2017-07-10T11:29:54+00:00
@moneromooo-monero You can usually take a more permissive licence and re-release the code under more restrictive licence (see this flowchart https://www.dwheeler.com/essays/floss-license-slide.html ). You (or for that matter anybody else) can take the whole or part of Monero and release it under a copyleft licence. 

That said I don't think the change would be retroactive. There are no provisions for taking back MIT licence, so somebody will always be able to claim that he was using the pre-change code ever since as long as it doesn't contain post-change features.

## hyc | 2017-07-10T13:13:30+00:00
IMO this change to LMDB has absolutely zero impact on the Monero Project itself. It doesn't in any way trigger a need to relicense the Monero code - AFAICS that was simply brought up in our IRC discussion since we were on the topic of licenses anyway.

As an example, the OpenLDAP Project has been using BerkeleyDB since 1999, despite OpenLDAP's use of its OpenLDAP Public License and BerkeleyDB's use of the Sleepycat license. There is clearly no license incompatibility issue there. (But note that there *is* an incompatibility between LDAP and the Affero GPLv3, which is why we don't support any BerkeleyDB newer than 6.0.20 and are removing BerkeleyDB support from future OpenLDAP releases.)

The only potential issue is if someone makes a proprietary project from the Monero codebase, *and* they either modify the Monero code that uses the LMDB APIs, or they write new code that uses the LMDB APIs. In either of those situations, if they distribute binaries, they're obligated to either open source their modifications, or obtain a proprietary license.

## SamsungGalaxyPlayer | 2017-09-22T16:47:17+00:00
Relevant conversation in `#monero-dev`:

**\<moneromooo>** Did we get to an agreement about the licence change btw ? IIRC smooth didn't like the idea of lmdb 1.0 due to this...
**\<i2p-relay>** {-guzzi} the fact that i cannot uprade the machine without dependency hell made the decision final
**\<hyc>** afaik, nobody has made an official statement
**\<hyc>** maybe LMDB wallet just becomes a forked project of its own
**\<moneromooo>** How would that work ? If it forks, the original code's still the same licence.
**\<hyc>** I don't think there's anything in LMDB 1.0 that the existing code needs or could be improved with, really
**\<moneromooo>** Though smooth probably doesn't have much code in the wallet.
**\<i2p-relay>** {-guzzi} i saw no issues with the license. basically says don't fuck off with my code and create your own shit.
**\<i2p-relay>** {-guzzi} these decisions are always difficult to make because humans have a tendancy to just say No.
**\<i2p-relay>** {-guzzi} afk
**\<moneromooo>** Nah.
**\<hyc>** yeah, there's no license incompatibility. afaik smooth just objects to forcing a dependency on the main project, to a copyleft'd module
**\<hyc>** so, doing the work in a forked project means the main project continues on its merry way
**\<i2p-relay>** {-guzzi} copyleft'd
**\<i2p-relay>** {-guzzi} lol
**\<i2p-relay>** {-guzzi} i think it captures the true intent of open source.
**\<i2p-relay>** {-guzzi} it actually formalizes what monero and opensource is tryhing to accomplish.
**\<i2p-relay>** {-guzzi} rather than a depenency i see it as a formalization of the current intentions
**\<hyc>** I agree. I don't think anyone was philosophically opposed to it. the only objection is changing the requirements on an active project
**\<hyc>** anyway, smooth can speak for himself but that's how I interpret what's been stated so far
**\<i2p-relay>** {-guzzi} understood
**\<i2p-relay>** {-guzzi} we would need concensus for sure.
**\<hyc>** nothing has happened on that ticket https://github.com/monero-project/meta/issues/85
**\<hyc>** I suppose we need some way to force a vote, to resolve it.
**\<moneromooo>** Given there is no legal impediment, maybe we can do a core team vote. I think it'd go the right way ^_^

**\<luigi1111>** Which way is that? 
**\<moneromooo>** Using lmdb 1.0 of course 
**\<luigi1111>** What if that's the wrong way?
**\<moneromooo>** I'll act as the spokesperson.
**\<moneromooo>** But yes, maybe we can do test runs first until we're sure it "works" ^_^
**\<hyc>** test runs of wallet? that code doesn't really exist now
**\<moneromooo>** Test runs of the vote 
**\<hyc>** ahhhh
**\<moneromooo>** It just seems like a terrible waste to not update given there's no change in the licence as far as monero is concerned.
**\<scoobybejesus>** I recall there being an "implementation" friction - that all prior code donors would have to sign off on the new license, yada yada
**\<hyc>** no, that's a separate question scoobybejesus
**\<hyc>** about relicensing monero itself. pretty sure it's unanimous that that's a bad idea
**\<sgp>** Interesting read, everyone. @hyc to clarify, Monero can use LMDB 1.0 without a proprietary license as long as Monero stays open-source, correct? And furthermore, other people/companies can use Monero in closed-source projects as long as they don't modify the LMDB implementation, correct?
**\<scoobybejesus>** *goes back to lurking, but thanks hyc for clarification..*
**\<hyc>** correct
**\<hyc>** sgp ^
**\<Element>** hy
**\<sgp>** @hyc will they reasonably need to change the LMDB part? What projects on Monero do you imagine would change this?
**\<hyc>** I can't imagine any reason to, no
**\<hyc>** I suppose if someone wants to add new commands to search the blockchain by some other feature, they might add a new index table
**\<sgp>** So if they want a new index or something, they would have to add it to Monero's code and then use that, correct?
**\<hyc>** in practice, e.g. with OpenLDAP - people just embedded OpenLDAP into their proprietary widgets, and used it as-is.
**\<hyc>** sgp correct
**\<hyc>** sgp: they would have to add it to the public Monero code.
**\<sgp>** Understood

## anonimal | 2017-09-22T22:42:13+00:00
@sgp will you consider editing that post to instead give a TL;DR? It's hard to pickup anything concise from all the chatter (i.e., opinion vs. fact vs. intent).

## iamsmooth | 2017-09-24T23:35:51+00:00
I am strongly opposed to the dual license approach as I feel it is bad for the project, and for the currency.

1. Monero itself can not and should not use a dual license. A dual license (as used here) implies there is some licensing agent with whom you can contract to obtain access to the second license. There is no such entity. The "Monero Project" exists only as an informal collaboration of contributors. If such an entity did exist it would be point of centralization which could be attacked to exert influence over the currency.

2. As a BSD-licensed project, the code is available for all to use in whatever manner they desire, including proprietary code, integrating with hardware, etc. (excepting of course that the copyright and list of conditions must be retained). I am strongly opposed to incorporating some 'asterisk' which says that the code can be used, but isn't actually freely usable without additional conditions (because an essential, tightly-integrated, and arguably consensus-critical component has less permissive license terms) and points people to a particular corporation to obtain other usage rights. 

There have been previous cases where we rejected incorporating useful code because it did not follow the existing license of the project. In my view, contributing to an existing project means doing so under the terms of its existing license. As such, whoever proposes (hypothetically) to make a contribution (aka pull request) which incorporates this new dual-license LMDB (or anything else significantly different from the existing permissive open source license terms) is out of line, as it conflicts with the existing license at least in practice/spirit, and such a proposal/PR should be rejected. A proposal to relicense Monero to allow the same would not be out of line in the same sense, it would be valid community discussion, though I am still personally against it.

As I have said elsewhere, I will be resigning in protest if the new version of LMDB with these less permissive terms is integrated with Monero, or if Monero adopts a copyleft. I joined an open source project with a permissive open source license (permissive not only in theory, but also fully in practice) and I'm not interested in having it change out from under me (nor its existing users).





## ArticMine | 2017-09-25T04:52:57+00:00
I will respond to the second of @hyc's points first 

> Should the Monero Project itself change to a dual-use license?

There are strong arguments against certain implementations of this where our existing license is not part of the dual license that the were expressed by @fluffypony  and @iamsmooth above. A good example would be combining a strong copyleft say GPL v3 with a proprietary license, with the intent of monetizing the latter.  The primary issue is that either one has great trouble changing the license in the future as @fluffypony  points out in 
> I'm strongly against relicensing Monero. Having gone through the process with Electrum, I can tell you that it is extremely painful and time-consuming. You have to get hold of EVERY contributor that has EVER contributed, and if a contributor decides they don't agree you have to get someone to rewrite their contribution (this thankfully only happened with a single Electrum contributor, but it was painful).

The above is the Linux model or one needs a centralized entity to hold the copyrights (this is needed for a dual license, involving a proprietary license if one wishes to monetize the proprietary license) as @iamsmooth points out in 

> Monero itself can not and should not use a dual license. A dual license (as used here) implies there is some licensing agent with whom you can contract to obtain access to the second license. There is no such entity. The "Monero Project" exists only as an informal collaboration of contributors. If such an entity did exist it would be point of centralization which could be attacked to exert influence over the currency.

The latter is the GNU model where the copyrights are held by a centralized entity namely the Free Software Foundation.  

It is important to understand that going from a permissive license to another permissive license, a copyleft license or even a proprietary license does not require the permission of the existing copyright holders, provided the new license is compatible with the existing license.  This is after all the whole point of a permissive FLOSS license. So for example one can go from our current license, 3 clause BSD, to Sleepycat to GPLv3 without getting permission. It is going in the opposite direction that requires the permission of the copyright holders, or where the are license incompatibilities for example going from GPL 2 to GPL 3, the Linux situation. Dual licensing by adding a compatible FLOSS license such as GPL v3 to 3 clause BSD is also a non issue. In effect this is what we are doing with the GUI binaries.  Dual licensing the 3 clause BSD with a proprietary license to for example include our code in the Apple store would also work although in that case a centralized entity is needed because of Apple. 

The controversial issue here is re licensing our base 3 clause BSD license to a copyleft such as for example GPL v3+. There are significant benefits to this in that certain attacks can be prevented or at least mitigated. One example would be the wide spread distribution of a proprietary Monero daemon that  includes tracking spyware and DRM. It would actually be illegal in many jurisdictions to even attempt to figure out what this daemon was doing. This is not a theoretical attack. Consider for example the attack that Lenovo launched against online  fiat banking with Superfish. https://en.wikipedia.org/wiki/Superfish The motivation was to break https in order to place "personalized" ads, but the impact was far worse from a privacy and security point of view. The threat of surveillance capitalism is very real. 

I am actually neutral at this point on re licensing to a strong copyleft such as GPL v3+, I see both sides of the argument.

At this point I will consider the first of @hyc 's points, 

> Should the Monero Project, which is currently under a liberal license, continue to use software which is not liberally licensed?

I actually strongly support this, provided:
a) The software is GPLv3 compatible,. 
b) The software does not involve AGPL code.
c) The software can be replaced on one or more nodes without affecting consensus, even if it may take some work.
d) The software provides a proprietary compatibility licensing option. 
The LMDB software meets all of the above. This is not re licensing our code. 
I support this because:
1) This was done by the Monero project in 2015 with the use of Berkeley db for 32 bit. It did not require any permission from copyright holders and was perfectly reversible. One simply keeps our existing 3 clause BSD license as part of any dual license for our code. This avoids any needs to get permissions to revert etc. This can be reversed in the future just as it was reversed in the past. 
2) It does not impact a proprietary wallet client accessing the Monero network via a node. For example a wallet on an iPhone, all proprietary, could access my Monero node running on Trisquel, 100% Free Libre GNU Linux. Of course the client and node can be run by the same person or related persons. For this reason there is no issue for app store wallets that use a remote node, POS systems connecting to a node, web services, exchanges etc using both FLOSS and proprietary software etc. One should note that in order to trigger the copyleft in LMDB 1.0 one needs both use and accompaniment.  Use alone is not enough. 
3) There are very significant benefits in the future to the users of Monero in particular encryption, with version 1.0 of LMDB.
4) Users who insist on running a proprietary node can still do this either by licensing LMDB or replacing it. There is no imposition here. What we are saying is that if they wish to run a proprietary node they have to play by proprietary rules, and accept the costs of running proprietary software.
5) I have yet to see a legitimate use case where this is an issue,
6)  We get most of the benefits of deterring the attack I mentioned above, without the re-licensing downsides. A handful of proprietary nodes is not an issue, but a large number is.  

In conclusion using LMDB 1.0 in the future will provide us a host of benefits and no downsides, so I must support it. It is also a very good compromise. 


## iamsmooth | 2017-09-25T08:21:10+00:00
I want to follow up to acknowledge that @ArticMine makes a good point about less permissive free software licenses potentially mitigating some attacks on software with very permissive licenses, mostly surrounding DRM (and perhaps other related concerns).

To me that is worthy of community discussion, and in the case where there were sufficient community discussion and consensus built around a license change over a sufficient period of time and with input from all interested parties, I would consider supporting it. 

What I oppose and will not be a part of is an abrupt change that alters the license out from under existing contributors and users in either a direct _or de facto_ way (and I do consider incorporation of LMDB 1.0 to be such a de facto change because in the present state of the project, it renders the software non-functional without the component carrying more restrictive terms, particularly if the wallet libraries are also altered to to use it, which seems to be the major motivation for wanting to upgrade in the first place).

BTW, I opposed integrating BDB given its license as well, but I didn't consider it a critical issue nor oppose it strongly because it was used only as a backup that was barely functional (with extremely poor performance and questionable reliability) and only used minimally-supported (32 bit) systems, and at the time we the plan was to replace it (which was in fact done).

I believe strongly that we would not have pursued using LMDB if it had originally had a copyleft license, just as we have passed on other useful libraries for the same reason. I likewise see no reason to accept one now and push it onto our users just because such a license is bundled with an update. As discussed above we can continue to use the existing version for the time being while exploring alternatives that don't impose restrictions, or possibly, as part of a careful deliberative process appropriate for the seriousness of such a change, consider changing the project license.

## fluffypony | 2017-09-25T08:56:35+00:00
As an option, since this is primarily a DB concern right now, what if we got the generic blockchain_db class back to its former glory, and then offered multiple DB backends as drop-in binary plugins via 0MQ IPC?

We could have one of the LevelDB forks as the default plugin that is packaged with the code, and @hyc can maintain and ship an LMDB plugin out-of-band.

## iamsmooth | 2017-09-25T10:04:14+00:00
1. Its a lot of work to effectively abstract DB and a questionable idea anyway, at least outside of some special uses (see 3 below for more discussion on this)
2. Does not address the issue of the wallet, which seems to be the primary motivation here anyway
3. DB can be consensus critical and multiple DB backends introduces an increased risk of consensus failure of not done very, very carefully (so even more work). Yes we had multiple DB back ends before. That was a bad idea (though not horribly bad in practice as BDB was only used in a very limited role and likely not on any important nodes ever). There is some discussion on this recent twitter thread about the difficulty of DB abstraction in a consensus context: https://twitter.com/petertoddbtc/status/908368951138275328

At least in the case of the wallet, if we supported multiple db storage engines it would not be a consensus issue. And that fits reasonable well with there currently being GUI (under Qt copyleft license) and CLI (under BSD permissive license) wallets using the same underlying wallet library (under BSD permissive license).

Incidentally we should not take lightly the prospect of upgrading the node database library anyway, without clear review and understanding of any functional differences (including bug fixes) between the releases. See second bullet item in the answer here: https://bitcoin.stackexchange.com/questions/42925/why-does-bitcoind-use-a-fork-of-leveldb-for-key-value-storage/42929

## hyc | 2017-09-26T13:35:37+00:00
As an aside, my recent patches to blockchain_db will allow new backend implementations to be plugged in without impacting the rest of the source tree.

I'm unclear on why @iamsmooth is so violently opposed to this change in LMDB, but seems to have no problem with using QT in the GUI, which also has copyleft/commercial dual licensing.

## iamsmooth | 2017-09-26T18:01:04+00:00
> m unclear on why @iamsmooth is so violently opposed to this change in LMDB, but seems to have no problem with using QT in the GUI, which also has copyleft/commercial dual licensing.]

@hyc as I stated above, I do not consider the GUI to be at all in the same category as it is not essential nor does it implement the consensus protocol. That ought to be obvious since for like 3 years we didn't even have a GUI. As far as I'm concerned, that is a different code base, under a different license, which is a _user_ of the core implementation. 

And to be clear I'm not opposed to your licensing generally. What I am opposed to is a fundamental change in the licensing terms under which Monero (the core implementation) is usable. I firmly believe that the core implementation of a decentralized currency should be usable without any meaningful restrictions or legal compliance requirements, and that includes a copyleft. 

We have never accepted copyleft code as an essential part of the core implementation and I do not believe we should do so now in order to adopt an 'upgrade' of an upstream library. My position would be the same for any other other upstream library: we should stick with the permissively licensed version, or switch to a non-copyleft alternative. 

Alternately an extensive public discussion and public awareness campaign should occur as to whether this is beneficial change to make for the project and why, so that: 1) existing or prospective users of whatever nature are informed of the upcoming change and able to plan accordingly; and 2) past, current, and prospective contributors can be informed that the terms under which their work is usable are being fundamentally changed and have the opportunity to express whether they want their work to go forward under a less permissive licensing model. (I'm aware that the latter is not necessarily a legal requirement since the previous permissive terms allow adding restrictions, however I consider it to be a reasonable ethical requirement for an existing project to significantly change its open source philosophy from permissive to copyleft, something that not all open source developers support at all or under these particular conditions. While I remain unconvinced by @ArticMine's idea that it is actually a benefit to adopt a copyleft approach for Moenro, I'm open to consider that idea and I believe that having such as discussion on advantages and disadvantages is the right way to make such a decision, as opposed to by default due to an upgrade of an upstream library.)

Regarding the ability to drop in a new backend implementation, in addition to the fact that no such usable implementation exists (and the prospect of developing and maintaining one is likely unrealistic as demonstrated by the BDB example, which was never all that well developed or maintained and promptly abandoned as soon as it was no longer needed for a few platforms), as I have explained above a database back end that stores blocks is consensus critical. To properly support a switchable back end would require essentially a formal verification that it is functionally identical to the primary implementation (there are a few exceptions to this but they are niche use cases out of the scope of this discussion). Again that seems unrealistic to me, and not a good approach to pursue.

## luigi1111 | 2017-09-26T18:49:35+00:00
I don't have anything to add at the moment, but I am in agreement with most of @iamsmooth's points, as below.

> I am strongly opposed to the dual license approach as I feel it is bad for the project, and for the currency.
> 1. Monero itself can not and should not use a dual license. A dual license (as used here) implies there is some licensing agent with whom you can contract to obtain access to the second license. There is no such entity. The "Monero Project" exists only as an informal collaboration of contributors. If such an entity did exist it would be point of centralization which could be attacked to exert influence over the currency.
> 2. As a BSD-licensed project, the code is available for all to use in whatever manner they desire, including proprietary code, integrating with hardware, etc. (excepting of course that the copyright and list of conditions must be retained). I am strongly opposed to incorporating some 'asterisk' which says that the code can be used, but isn't actually freely usable without additional conditions (because an essential, tightly-integrated, and arguably consensus-critical component has less permissive license terms) and points people to a particular corporation to obtain other usage rights.

## ArticMine | 2017-09-27T22:26:40+00:00
> I'm unclear on why @iamsmooth is so violently opposed to this change in LMDB, but seems to have no problem with using QT in the GUI, which also has copyleft/commercial dual licensing.

The key difference I see comes down to using a copyleft (or other non permissive FLOSS license) in consensus vs non consensus code. When it comes to consensus code I agree with most of @iamsmooth's concerns. While I can see some very significant advantages to incorporating a copyleft in consensus code and have some ideas on how it could possibly be done, it would have to be structured extremely carefully. The fundamental issue is how to add a copyleft (or other, non permissive, FLOSS license) to consensus code, while at the same time preserving both decentralization (having the code copyright owned by as large as a group of people as possible) and flexibility (being able to change the copyleft (or other, non permissive, FLOSS) license at a future date). With our current permissive license both decentralization and flexibility are trivial. One point is clear to me: Simply adding a copyleft (or other, non permissive ,FLOSS license) library to consensus code, where the copyleft (or other, non permissive, FLOSS license) library code is controlled by one or more persons is not the way to do this.

When it comes to non consensus code as is for example QT in the GUI, or a copyleft (or other, non permissive, FLOSS license) in one of many wallets then It can and, if technically appropriate, should be done subject to the constraints I mentioned above. As a consequence, the question of my support for LMDB v1.0 vs LMDB v0.9 in the daemon comes down to its impact on consensus or quasi consensus code. 

Edit: The Berkeley DB / Sleepycat license for LMDB 1.0  is not a copyleft nor for that matter is it a permissive license. This is because it does not enforce FLOSS on the use and accompanying software. What it enforces is a form of "Shared Source" which is met by FLOSS but also can be met by proprietary software licenses that are willing to disclose their source even under a non disclosure agreement. 

 

## ghost | 2017-10-01T21:23:21+00:00
Is it not possible for @hyc to make a special concession to Monero for a permissive license to LMDB 1.0, but enforce dual licensing on all other instances/implementations? Essentially using Monero as an advertising vehicle and test-bed for the technology he continues to develop (which I'm fine with BTW).

## erikd | 2017-10-01T22:51:52+00:00
@hyc says:

> I'm unclear on why @iamsmooth is so violently opposed to this change in LMDB, but seems to have no problem with using QT in the GUI, which also has copyleft/commercial dual licensing.

The GUI is optional, LMDB is currently not optional.


## Gingeropolous | 2017-10-21T05:01:14+00:00
came across this, maybe relevant. https://sfconservancy.org/blog/2017/oct/20/additional-permissions/



## mutagenfork | 2018-01-31T12:11:15+00:00
FWIW, I agree with @iamsmooth's arguments.  I also agree with @fluffypony's suggestion to  beef up blockchain_db to allow for multiple db's to be dropped in. 

## hyc | 2018-01-31T13:03:14+00:00
As a result of these discussions and the well-considered reasons put forth by the community we decided not to change LMDB's license. Closing this issue.

# Action History
- Created by: hyc | 2017-07-02T19:48:44+00:00
- Closed at: 2018-01-31T13:03:14+00:00
