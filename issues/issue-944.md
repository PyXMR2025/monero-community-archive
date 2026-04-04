---
title: Monero Research Lab Meeting - Wed 13 December 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/944
author: Rucknium
assignees: []
labels: []
created_at: '2023-12-13T15:23:51+00:00'
updated_at: '2023-12-18T04:20:07+00:00'
type: issue
status: closed
closed_at: '2023-12-18T04:20:07+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Discuss: How to confirm security of Monero's multisignature protocol? Do we need mathematical security proofs, and can we get them? Info:
- [Brandon Goodell and Sarang Noether (2018) "Thring Signatures and their Applications to Spender-Ambiguous Digital Currencies"](https://www.getmonero.org/resources/research-lab/pubs/MRL-0009.pdf)
- [Monero multi-signature patch review by Inference](https://community.rino.io/rino-multisig-pr8194-audit-20220627.pdf)
- [Rust alternative implementation](https://github.com/serai-dex/serai/blob/develop/coins/monero/src/wallet/send/multisig.rs) by @kayabaNerve

3. Discuss: [Exploring Trustless zk-SNARKs for Monero's payment protocol](https://github.com/monero-project/research-lab/issues/100). What are the bottlenecks for potential implementation?

4. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

5. Seraphis. ( [UkoeHB's Seraphis Proof of Concept work](https://ccs.getmonero.org/proposals/seraphis-wallet-poc-2.html), [Seraphis repo](https://github.com/UkoeHB/Seraphis) ).

6. MRL Meta: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [MoneroResearch.info repository of Monero-related research papers](https://moneroresearch.info/), [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

7. Any other business

8. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#941 

# Discussion History
## plowsof | 2023-12-17T17:07:02+00:00
Logs 
> __< r​ucknium:monero.social >__ MRL meeting in this room in two hours.     

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/944     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< vtnerd >__ hi     

> __< rbrunner >__ Hello     

> __< t​obtoht:monero.social >__ hi     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< t​obtoht:monero.social >__ Wanted to report that I made some initial progress on my multisig UI/UX work. MMS now speaks JSON instead of XML and I adapted it to connect to a totally bare-bones and (currently) insecure backend that uses FastAPI + Redis. Set up a 2/3 multisig wallet using the CLI and sent a transaction.     

> __< r​ucknium:monero.social >__ me: OSPEAD.     

> __< t​obtoht:monero.social >__ For now I'm going to assume the participants have an out-of-band secure channel (like an encrypted matrix group chat) which a coordinator can use to distribute a shared secret (and channel link) that is used for encrypting the intial setup. All participants must confirm the multisig primary address matches after setup.     

> __< t​obtoht:monero.social >__ The fact that you can only do one transaction signing attempt per multisig info sync is a very easy failure mode to hit and will need to find a clever way to mitigate this as much as possible.     

> __< h​into.janaiyo:matrix.org >__ me: serai+cuprate stuff     

> __< rbrunner >__ tobtoht: Sounds like good progress     

> __< vtnerd >__ me: Im still stuck in subaddress testing in LWS. I think macOS is hitting a stack overflow, as the tests fail intermittently, and address sanitize is complaining loudly about longhash overflowing     

> __< r​ucknium:monero.social >__ 3) Discussion. What do we want to discuss?     

> __< r​ucknium:monero.social >__ People knowledgeable about multisig want to comment on tobtoht 's work?     

> __< rbrunner >__ Sounds good. I think that's a very pragmatic approach how they develop, and that's good. Not becoming victim of the "not invented here" syndrom and starting from scratch also gives hope.     

> __< rbrunner >__ Looking forward to see something like "MMS in GUI" :)     

> __< rbrunner >__ Although you can probably abstract higher and not bother the user with individual messages, at least not during normal workflow     

> __< h​into.janaiyo:matrix.org >__ r​brunner: did you make the decision the use XML? if yes, were there specific reasons?     

> __< t​obtoht:monero.social >__ Yes, I'll start with something like MMS+GUI and slowly work it away to where the user (mostly) doesn't have to interact with it directly.     

> __< rbrunner >__ The API to PyBitmessage is based on XML. I would have opted for JSON, XML for something like this is a bit strange     

> __< h​into.janaiyo:matrix.org >__ ah, that's what i assumed     

> __< rbrunner >__ There once was a time where XML was the future, for everything, according to hype     

> __< rbrunner >__ Anybody remember SOAP ...     

> __< h​into.janaiyo:matrix.org >__ a question i had about seraphis: assuming JSON-RPC remains, how big would the changes be to the daemon interface?     

> __< rbrunner >__ Never thought about that in detail, but I would guess that the daemon doesn't need many changes in its RPC interfaces     

> __< rbrunner >__ Maybe in pool handling details because there are some other things "to know" about Seraphis transactions     

> __< h​into.janaiyo:matrix.org >__ great - i'll probably be responsible for porting the current daemon RPC to cuprate and was wondering if i'd have to rewrite it all when seraphis arrives :)     

> __< rbrunner >__ Ah, I see :)     

> __< r​ucknium:monero.social >__ Does anyone have an estimate for the average time between when a tx is constructed (specifically when `monerod` sends back data to the wallet from a `get_output_distribution` RPC request) and when a mining pool would see it? I am analyzing ring members from the first spendable block after the 10 block lock.     

> __< r​ucknium:monero.social >__ The parts are maybe: 1) Data comes back to wallet 2) Do most wallets ask users to confirm between tx construction and broadcast? 3) Dandelion++ stem phase, then fluff phase.     

> __< r​ucknium:monero.social >__ Maybe sech1 would know.     

> __< r​ucknium:monero.social >__ Anything else to discuss?     

> __< h​into.janaiyo:matrix.org >__ yes to 2, default is to ask on cli/gui     

> __< t​obtoht:monero.social >__ I think most (all?) wallets do 2. You would want to show the user the tx fee before broadcast.     

> __< rbrunner >__ Never gave that much attention and just waited     

> __< sech1 >__ Time from tx leaving the wallet until pools see it? It can be 5-40 seconds, depending on Dandelion++ luck     

> __< sech1 >__ The wallet asks for confirmation before sending, and it display the fee to be used, so I guess tx is fully constructed at this point     

> __< r​ucknium:monero.social >__ Thanks, sech1. Maybe I can look at the D++ code and see what the average expected number of hops and delays would be.     

> __< rbrunner >__ "luck" meaning having quick and responsive daemons to pass the tx on for each hop?     

> __< sech1 >__ Yes, and passing through major pool nodes in the stem phase     

> __< r​ucknium:monero.social >__ rbrunner: D++ is a random process. Each node broacasts it to fluff with some probability. And waits to send as a stem phase (if stem phase is randomly chosen) with a random small delay. (AFAIK from the D++ paper).     

> __< r​ucknium:monero.social >__ And if stem fails due to black hole attack or just nodes not broadcasting for some non-malicious reason, the original node eventually broadcasts the tx in fluff phase after a long time     

> __< rbrunner >__ Yes, I start to remember discussions from the implementation phase.     

> __< r​ucknium:monero.social >__ Long = more than a second and less than a minute.     

> __< sech1 >__ I think all nodes in the stem will eventually broadcast with random delays     

> __< sech1 >__ If they don't see it broadcasted     

> __< sech1 >__ D++ covers many different scenarios and tries its best     

> __< h​into.janaiyo:matrix.org >__ `tx-proxy` may need to be accounted for too (unless its statistically irrelevant here, what is the % of tor/i2p txs?)     

> __< rbrunner >__ So maybe it won't be exactly easy to come up with a good average     

> __< r​ucknium:monero.social >__ If someone has a good argument for why tor/i2p txs would be more than 5%, please say it. IIRC tor/i2p txs do not use D++, so they may be faster.     

> __< r​ucknium:monero.social >__ If those are less than 10%, I could ignore them in a rough calculation.     

> __< r​ucknium:monero.social >__ This isn't the only way to try to measure this, by the way. wallet2 has a uniform distribution added to the recent spend window. At the end of the recent spend window, the probability mass drops like a cliff to just the gamma distribution. So you can see if the cliff is aligned where it should be.     

> __< r​ucknium:monero.social >__ But more information and ways to check this is always better.     

> __< plowsof >__ If the node being used has "disable_noise" then d++ wont be used to broadcast tor/i2p tx's      

> __< h​into.janaiyo:matrix.org >__ anecdotal but, tor is almost always slower by a order of magnitude than clearnet for me     

> __< plowsof >__ Will be faster than clrarnet^     

> __< r​ucknium:monero.social >__ You can see the cliff in the probability distribution in the plot in the last page here: https://www.overleaf.com/read/ndbtkwrbrdjq     

> __< r​ucknium:monero.social >__ Anecdote and theory contradict each other 😅     

> __< r​ucknium:monero.social >__ hinto: Do you know if you disable_noise?     

> __< r​ucknium:monero.social >__ Is this a remote connection through Tor, or a local node that broadcasts txs through Tor?     

> __< h​into.janaiyo:matrix.org >__ no, disable_noise is not enabled, so i guess tor + d++     

> __< h​into.janaiyo:matrix.org >__ both remote/local are slower     

> __< plowsof >__ Selsta / ofrnxmr put me onto the advantages of disable_noise for broadcasting anon tx's     

> __< h​into.janaiyo:matrix.org >__ i'm maybe outting my tx's here :)     

> __< h​into.janaiyo:matrix.org >__ maybe i'm hitting some insane world-hopping tor circuit every single time     

> __< r​ucknium:monero.social >__ Thanks. Anything more to discuss?     

> __< h​into.janaiyo:matrix.org >__ me/boog would appreciate some discussion on the more trivial parts of cuprate, e.g https://github.com/Cuprate/cuprate/issues/46 (closes a nearing 2 year monero issue)     

> __< h​into.janaiyo:matrix.org >__ the actual binary name of the application is up for debate as well, current options are `cuprate` and `cuprated`     

> __< v​tnerd:monero.social >__ Rucknium: tor/i2p still uses d++ amon the remote hidden service side     

> __< r​ucknium:monero.social >__ We can end the meeting here. Thanks everyone.     


Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: Rucknium | 2023-12-13T15:23:51+00:00
- Closed at: 2023-12-18T04:20:07+00:00
