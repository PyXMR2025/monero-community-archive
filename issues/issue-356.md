---
title: Discussion about how to specifically phase out long payment IDs
source_url: https://github.com/monero-project/meta/issues/356
author: dEBRUYNE-1
assignees: []
labels: []
created_at: '2019-06-07T13:07:18+00:00'
updated_at: '2020-06-05T15:27:35+00:00'
type: issue
status: closed
closed_at: '2020-06-05T15:27:35+00:00'
---

# Original Description
As per the mailing list message, long payment IDs will be phased out this year:

https://lists.getmonero.org/hyperkitty/list/monero-announce@lists.getmonero.org/thread/NQCMZHCW557QG4QX752ZTBETRWLF2P63/

However, no consensus has yet been reached on how to phase them out. There are essentially two options:

(i) Phase them out by removing all support from the official software. 

(ii) Ban them (for a certain period) on the consensus level. 

The risk of the first option is that a third-party wallet provider may retain long payment ID support, thereby potentially providing exchanges and services an excuse to not switch to either integrated addresses or subaddresses. 

The second option implies parsing `tx_extra` for each transaction, which is deemed inelegant by some. That being said, it does not have to be used indefinitely, as utilizing it for one hard fork period (6 months at the time of writing) should be sufficient to make exchanges and services switch.

Please leave your opinion on the matter as well as a 'vote' for the preferred method. 

# Discussion History
## SarangNoether | 2019-06-07T13:22:19+00:00
Provided there is adequate time between the final decision and the implementation, and provided that there is substantial communication to the ecosystem, I favor both options together. A temporary consensus rule discourages third-party wallet support for unencrypted pIDs, and removing support entirely from the default wallet tools provides a better and safer user experience overall (and complies with the consensus rule).

## SamsungGalaxyPlayer | 2019-06-07T13:23:25+00:00
I vote 2. We should commit to a consensus ban for at least one upgrade cycle to force services to upgrade.

## dEBRUYNE-1 | 2019-06-07T13:24:18+00:00
@SarangNoether - I should perhaps have added that option (ii) essentially includes option (i). 

## sethforprivacy | 2019-06-07T14:11:30+00:00
I definitely vote for option 2.

Other options have been around for long enough. As long as we are very careful and send out plenty of comms about the switch, we should ban them on the consensus layer to force the switch.

## scottAnselmo | 2019-06-07T14:21:36+00:00
/me votes for option ii,  long pid need to go and any more delays caused by users getting around the intentions of i is not ideal towards making Monero easier to use.

## ArticMine | 2019-06-07T15:44:58+00:00
I am in favor of a phased approach. We implement (i) first. If it does not work then we move to (ii); however in that case we should be looking at a permanent as opposed to temporary consensus change.  As a rule of thumb I am opposed to "temporary" consensus changes, since they go against decentralization at a very fundamental level. The implication is centralized control  that will reverse the "temporary" change at a later date. The most famous example being the 1 MB block size limit in BItcoin that was introduced in 2010 as a "temporary" anti spam measure. 

## SamsungGalaxyPlayer | 2019-06-07T16:06:40+00:00
@ArticMine a few key points of note and differences.

1. We already are doing a form of 1. It's disabled by default in the GUI and CLI. While it can be completely removed, most services have still not upgraded despite repeated warnings and difficult to work around defaults.

2. If this stays as a consensus change forever, good. No one should ever be using long payment IDs. The possible reversion back would occur if services have already upgraded and if moneromooo and others feel that it's best not to parse tx_extra. Comparing this to the concern of Bitcoin block sizes, especially when you advocate for a permanent change anyway, seems like an inaccurate comparison to me. Monero sets "temporary" fixed ringsizes with the expectation that they will eventually be increased.

## ArticMine | 2019-06-07T16:20:28+00:00
I am not opposed to implementing (ii) as a permanent consensus change now if the consensus is that (i) has already failed or to it being changed back if at a later date it is found to be unnecessary. What I am opposed to is the promise that the consensus change is temporary. 

A consensus change by its very nature is permanent. It may be changed in the future, but there are absolutely no guarantees that such a change will occur. That is the very important lesson of the Bitcoin 1 MB block size limit.   

## binaryFate | 2019-06-07T17:21:44+00:00
I follow ArticMine on this.

I understand we are asked to vote on (i) and/or (ii).
However if (ii) is phrased as it is, by saying _temporary_ it basically means "we are planning to do this and then planning to do that later". As such it could set a dangerous precedent for the project. This could have impacts for the community dynamics in the future, but mostly I am concerned it would endanger the way the Monero project can be considered under various jurisdictions as well as the legal status of its various contributors.

Because of this I can only vote only for (i) unless the "temporary" gets out of the discussion.


**EDIT:** I was asked in private to clarify why (ii) is different from usual consensus changes that we do regularly, here are my (not-a-lawyer, out-of-my-ass) thoughts.

The project has been constantly changing the software since inception, in a reasonably decentralized way. That's how we move forward and everyone is fine with this.
But saying we will change something *later* is taking power over whoever will constitute the community by then (by contrast to them just inheriting a software), so I see a difference in centralization.

I understand that sounds a bit extra paranoid, but I consider it's the core team role to lean on the cautious side.

## scoobybejesus | 2019-06-07T19:19:12+00:00
> (ii) Ban them (for a certain period) on the consensus level.

Perhaps there can be some clarity provided regarding the purpose of the consensus ban being temporary. 

We're talking about `monerod` parsing `tx-extra` and rejecting transactions that use `tx-extra` (for long PIDs), right?  To be clear, is the idea arguing that banning those transactions at the network level will force the ecosystem to adapt?  And, therefore, there will come a time in the near future where there is no need to ban the transactions outright because long PIDs by then will no longer be supported by anyone in the ecosystem?

* Also, is there an expectation that `tx-extra` will be used in the future for something other than PIDs?  

I just figure some context around the proposed "temporary" consensus change would be helpful. Without greater context, it does feel a bit like a slippery slope.

## SamsungGalaxyPlayer | 2019-06-07T19:46:15+00:00
If people are getting caught up on the *temporary* wording, then choose between i) wallet removal and ii) consensus banning through tx_extra parsing. It should go without saying that even if many in the community hope that ii) will be temporary, a discussion will need to take place on whether to remove it in the future, regardless of what we speculate may happen now.

## dEBRUYNE-1 | 2019-06-08T06:41:37+00:00
@ArticMine @binaryFate - I don't particularly see a problem if we precommit to removing it during the next scheduled upgrade. That is, precommit to instating a temporary consensus ban in the October 2019 scheduled protocol upgrade that will be removed in the April 2020 upgrade. 

>is taking power over whoever will constitute the community by then

I don't think you can make this argument if we precommit to it *and* there is only a six month difference. Realistically, how much is the community going to change within six months? 

## danrmiller | 2019-06-08T21:50:26+00:00
How long is forbidding them going to add to transaction verification time? Are there ways to create transactions that will take a particularly long time to verify that they don't use a long payment id?

## iamsmooth | 2019-06-09T05:51:26+00:00
@danrmiller If tx_extra needs to be parsed then it could potentially take _some_ time to do so. I don't believe there is currently any limit to its size. Such a consensus change could also limit it to a reasonable size, and maybe this would be a good idea. However, in practice, I doubt that parsing it will take significant time compared to the various cryptographic functions otherwise needed during transaction verification.

I'm against the 'temporary' wording for the reasons stated by others.

I'm against the forced removal of payment ids at all, as discussed elsewhere. However, that seems to be a closed issue. 

Given pID removal, I'm neutral on enforcing it in consensus. The main disadvantage I see is adding permanent complexity (technical debt) to the consensus code for short-term issue (even if the rule is later removed, the code will need to remain to validate the prior chain), and risk of bugs and exploits to the consensus code. Parsers in general are a frequent source of such bugs.

Also, I think the community needs to think more carefully about tx_extra and whether it is a good idea in general to allow such a free-form field in a currency which aims at fungibility when various risks to fungibility from non-cooperative wallet implementations seem inherent in the concept. The question raised by this issue seems to be only a narrow example of a broad category of risks.

## ghost | 2019-06-10T08:45:46+00:00
Smooth's last point is a good one. Unless we can think of use cases which are fundamental to the functioning of a cryptocurrency which can ONLY be achieved through the use of an arbitrarily sized tx_extra field, then we shouldn't have tx_extra at all. It's a massive vulnerability to fingerprinting and fungibility breaking attacks of all sorts. Things like sending arbitrary data and messages through the Monero blockchain are not good enough uses in my opinion as they potentially compromise the fundamental use case which is fungible value transfer.

An arbitrary data field also opens up the network to easily constructed bloat attacks and legal issues of being forced to retain potentially objectionable material on the user's hard drive in order to run a full node.

Edit: To answer the original question, a temporary parsing of tx_extra to stop PID's could be an intermediate step towards dropping the tx_extra field altogether.

## SamsungGalaxyPlayer | 2019-06-12T02:04:05+00:00
While a discussion on tx_extra in general is important, I want to make sure this issue doesn't succumb to scope creep. I recommend reserving broader tx_extra discussion for a different issue. While tx_extra allows for a broad set of risks, only one main one is used in ~33% of transactions right now (standalone payment IDs).

## iamsmooth | 2019-06-12T08:13:04+00:00
@SamsungGalaxyPlayer Considering the role of tx_extra in general is relevant here because the proposed solution of starting to parse inside tx_extra in the consensus code to address payment IDs is well outside the existing use case, and carries its own risks and complications. It isn't scope creep to consider whether the issue might be better addressed in a more comprehensive and potentially cleaner way with less potential for introducing permanent technical debt to deal with current conditions on the network at one point in time.



## ArticMine | 2019-06-12T16:17:16+00:00
After further reviewing this thread and giving this further thought i have to remove my support of banning payment ids at the consensus level by parsing tx_extra. The only proper way I see of banning payment Ids at the consensus level is by removing the tx_extra field entirely. The fundamental issue here is that we start with an arbitrary data field and now we want to introduce censorship for a very specific sting of data.  I see two serious issues with the parsing tx_extra approach:
1) It will not work.  A third party wallet designer wishing to have payment ids could easily use a different data string that would pass the parsing code and provide similar payment id functionality.
2) A significant risk with an arbitrary data field is illegal content on the blockchain. Once we open the door to censorship by attempting to ban payment ids, the question becomes why do we not also ban illegal content? If we add into the mix technically illiterate legislators and / or regulators in positions of power the potential for disaster is very significant. 

One only needs to look at the failed attempts to censor the Internet, by using block lists, in Australia for example or the failed attempts censor "infringing content" from the Internet by big copyright It is actually the same problem. Censoring "undesirable content" from an otherwise open platform. What I have mentioned above is only one of many possible attacks against tx_extra, so unless there is a compelling use case for tx_extra, its removal is the prudent course of action. 

My take is that comprehensibly addressing tx_extra is far more likely to attract consensus than an payment id specific "solution" that would likely fail in any event. 

## SamsungGalaxyPlayer | 2020-03-10T20:41:05+00:00
@dEBRUYNE-1 can you please close this? We can open a new discussion if we want to revisit this for a future upgrade imo.

# Action History
- Created by: dEBRUYNE-1 | 2019-06-07T13:07:18+00:00
- Closed at: 2020-06-05T15:27:35+00:00
