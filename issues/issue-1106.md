---
title: 'Monero Community Workgroup Meeting: November 9th 16:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1106
author: plowsof
assignees: []
labels: []
created_at: '2024-11-07T09:15:57+00:00'
updated_at: '2024-11-20T16:18:03+00:00'
type: issue
status: closed
closed_at: '2024-11-20T16:18:03+00:00'
---

# Original Description
Location: [Libera.chat, #monero-community](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-community:monero.social?via=matrix.org&via=monero.social)

[Instructions for joining the monero.social Matrix server.](https://www.getmonero.org/resources/user-guides/join-monero-matrix.html)

Time
16:00 UTC [Check your timezone](https://www.timeanddate.com/worldclock/converter.html)

Moderator: plowsof

Please reach out in advance of the meeting if you would like to propose an agenda item.

Proposed Meeting Items:

1. Introduction
2. Greetings
3. Community highlights 
    - How to buy Monero (November 2024) [yewtu.be](https://yewtu.be/watch?v=UKOE2DKBmRQ) - Xenu
    - Bounty [Monero point of sale device with 0conf](https://bounties.monero.social/posts/159/5-000m-foss-monero-point-of-sale-android-app)
    - [LocalMonero](https://localmonero.co/) closes down 7th November
    - [RINO.io](https://rino.io) to close down end of November, please withdraw all funds   
News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/)
5. [CCS updates](https://ccs.getmonero.org/)    
  a. [Carrot animated video](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/506)    
  b. [CryptoCheckout WordPress plugin (for WooCommerce) & Shopify app](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/514)    
  c. [Monerotopia 2024 Marketing and Publicity](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/515)    
6. Workgroup reports    
  a. Dev workgroup
  b. Localization workgroup
  c. Outreach workgroup
  d. Events workgroup - [MoneroKon 2025](https://monerokon.org)
  e. Website workgroup
  f. Policy workgroup
  g. Research workgroup
  h. [Seraphis Migration workgroup](https://github.com/seraphis-migration)
7. Open ideas time    
8. Confirm next meeting date/time    

[Previous meeting including logs](https://github.com/monero-project/meta/issues/1095)    

Meeting logs will be posted here afterwards.    


# Discussion History
## plowsof | 2024-11-20T16:17:46+00:00
Logs 
> __< plowsof >__ do we think there is a demand to fund a payment processor that merchants must look in monero gui to verify payments have been made or customers have to enter some txid/key after purchase?      

> __< geonic >__ doesn't seem likely     

> __< plowsof >__ a site that says 2$ / month for unlimited tx's but another page says 10$ a month https://cryptocheckout.co/fees/      

> __< ofrnxmr >__ geonic, imho, proposer has been 100% unable/unwilling to take a different approach. Just resolves threads and doubles down on usinf localmonero's block explorer to verify payments     

> __< b​enraouane:matrix.org >__ ofrnxmr: no, I said the others requires the mnemonic phrase of the wallet, then sync     

> __< ofrnxmr >__ Claiming that "its not his problem if funds are burnt"     

> __< plowsof >__ specifically states no fees per tx but i see a 1% fee hardcoded , but this was from an older version. so the repo is messy and not professional      

> __< plowsof >__ proposer can take an already built solution, today, with proper monero integration      

> __< r​ucknium:monero.social >__ plowsof: "however, this is not feasible in monero as the proofs does not tell us if the outputs are spent.. or burnt etc " I didn't read all the details of the proposal, but if the outputs are owned by the merchant, isn't it irrelevant if they are spent or not, since the merchant now has control (and can spend it as they wish)?     

> __< plowsof >__ for example bitcart.ai and start marketing it to merchants via third party SaaS      

> __< ofrnxmr >__ "no, I said the others requires the mnemonic phrase of the wallet, then sync" << "As I think the monero-wallet-rpc package (I've tried before) does not gives you the real time balance, & does not contain sync function, the sync itself requires a service & a server."     

> __< b​enraouane:matrix.org >__ plowsof @plowsof:matrix.org:  I said not applicable, it requires the mnemonic phrase of theerchant & deploying the app.js     

> __< b​enraouane:matrix.org >__ @plowsof:matrix.org:  I said not applicable, it requires the mnemonic phrase of the merchant & deploying the app.js,     

> __< b​enraouane:matrix.org >__ Even the code exist in back.php     

> __< ofrnxmr >__ In response to the funds burning, you said "That problems does not concern us, what we need is to confirm such amount were sent from such address (buyer) to such another address (merchant), locked or not, already spent or not, burnt or not, does not concern us."     

> __< b​enraouane:matrix.org >__ Even the code exists in back.php     

> __< plowsof >__ the merchant provides only an address, no private view key, we can submit a payment proof that is valid (but we didnt pay for the goods) , is my understanding of....      

> __< plowsof >__ https://github.com/monero-project/monero/issues/8819     

> __< b​enraouane:matrix.org >__ Exaxctly     

> __< ofrnxmr >__ "but if the outputs are owned by the merchant, isn't it irrelevant if they are spent or not, since the merchant now has control (and can spend it as they wish)?" << ruck, the service uses explorer to prove payments instead of a wallet     

> __< plowsof >__ bitcart.ai exists, no need for this      

> __< b​enraouane:matrix.org >__ No, you should pay, then submit your payment proof     

> __< ofrnxmr >__ And the spender has to submit tx proofs to localmonero's explorer (previously rino's)     

> __< b​enraouane:matrix.org >__ plowsof @plowsof:matrix.org:  from what you'll get the payment proof, you don't make a transaction?     

> __< plowsof >__ moneropay, acceptxmr     

> __< plowsof >__ btcpayserver      

> __< ofrnxmr >__ Hotshop, bitrequest     

> __< plowsof >__ all work listed in "Future" can happen, today      

> __< ofrnxmr >__ None of these requires submitting your tx keys to an explorer     

> __< plowsof >__ 2.1 Million merchants can all ping localmoneros block explorer with this SaaS     

> __< b​enraouane:matrix.org >__ They require mnemonic phrase of the merchant, they are not decentralized     

> __< ofrnxmr >__ no they dont.      

> __< r​ucknium:monero.social >__ Do they integrate with Shopify and Woocommerce?     

> __< plowsof >__ https://docs.bitcart.ai/integrations/shopify     

> __< plowsof >__ i can host this for people using this mode https://docs.bitcart.ai/deployment/thirdpartyhosting      

> __< ofrnxmr >__ I think btcpayserver does too. But shopify isnt the issue, its "what is actually being integrated"     

> __< plowsof >__ this is not a monero integration, this is a copy and paste of a generic method used for transparent blockchains     

> __< ofrnxmr >__ And in this proposal, its not payments being integrated, its block explorer payment proofs     

> __< r​ucknium:monero.social >__ plowsof: Wonderful.     

> __< b​enraouane:matrix.org >__ plowsof @plowsof:matrix.org:  bitcart not listed on the Shopify app store     

> __< plowsof >__ solano has different number of atomic units than monero, and the dev of the payment processor does not know this      

> __< ofrnxmr >__ Maybe you could contribute to bitcart to get it listed there?     

> __< b​enraouane:matrix.org >__ It does not follow the standard developer guide of the Shopify, concerning developing payment apps     

> __< plowsof >__ yes, i would look into why not and contact MrNaif about that      

> __< geonic >__ does the proposer have any merged code/prior contributions?     

> __< ofrnxmr >__ no     

> __< geonic >__ I vote no then     

> __< b​enraouane:matrix.org >__ ofrnxmr: it requires a mnemonic phrase, I'm already did since 2022     

> __< ofrnxmr >__ it does not     

> __< ofrnxmr >__ These all use view-only wallets      

> __< r​ecanman:kernal.eu >__ 🤦‍♂️     

> __< ofrnxmr >__ bitcart, btcpayserver, birtequest. None of these use a hot wallet (mnemonic passphrase)     

> __< ofrnxmr >__ https://github.com/BenraouaneSoufiane/cryptocheckout.co/blob/15942c7a676ce23963d06ec664dc323cf4fde46c/site/back.php#L25     

> __< plowsof >__ sloppy      

> __< b​enraouane:matrix.org >__ ofrnxmr: as per the official docentation, it seems they generate a private key for each merchant     

> __< b​enraouane:matrix.org >__ Private key is equivalent to mnemonic phrase     

> __< ofrnxmr >__ and heres the offending line that says that monero has 9 atomic units ..     

> __< plowsof >__ i think we can move on, benraouane can clarify criticisms here at a later time if they wish, its a no from me      

> __< geonic >__ that's worse than misgendering     

> __< vthor >__ what huge difference can three zeros do? /s     

> __< plowsof >__ if wownero was integrated it wouldnt be as bad     

> __< plowsof >__   c. [Monerotopia 2024 Marketing and Publicity](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/515)         

> __< geonic >__ brb putting my preferred atomic units in my email signature     

> __< ofrnxmr >__ lmao     

> __< plowsof >__ a new comment from jeffro on the 'topia marketing proposal      

> __< ofrnxmr >__ My only problem with monerotopia is the time     

> __< geonic >__ yes the time is an issue. based on positive reception to the proposal we've gone ahead. Vik paid them yesterday and they're pushing ahead. we have digital ads running right now     

> __< geonic >__ Vik is absorbing the volatility risk and I guess the risk that people will vote no here     

> __< vthor >__ +1     

> __< ofrnxmr >__ So new proposal is to repay vik for his altruism      

> __< geonic >__ btw jeffro is misinterpreting mbull's comment. this was monerobull's concern 2 weeks ago (before we had a proposal)     

> __< geonic >__ I pitched it to him as him getting his money back, was not a donation     

> __< geonic >__ guess I'm on the hook then     

> __< vthor >__ as I remember geonic stated in the comment from the beginning that he would prefinace it, or?     

> __< ofrnxmr >__ Well i guess we wait for vik to send the invoice after everything is settled?     

> __< geonic >__ doug, sunita and I have met twice with the PR company this week. they know what we want to achieve     

> __< plowsof >__ nice     

> __< geonic >__ yea if approved then that would be provided for payout     

> __< ofrnxmr >__ (if vik is getting change back, paying extra etc)     

> __< geonic >__ he wired $6000 yesterday, which was equivalent to 36.42 xmr at the time     

> __< ofrnxmr >__ i think we can pre-approve it, and wait for invoice to adjust the amount accordingly      

> __< plowsof >__ can i keep the rest     

> __< ofrnxmr >__ yes     

> __< plowsof >__ thanks     

> __< geonic >__ deal     

> __< geonic >__ there was probably a wire fee, will confirm     

> __< plowsof >__ pre approved to cover the entire amount - i suspect the full amount would still be needed to cover % markups     

> __< ofrnxmr >__ Anyway. I vote yes to repay vik his costs, once the confirmed whether the pr company used all/less funds (if there is change etc)     

> __< geonic >__ cool     

> __< plowsof >__ d. Gingeropolous 1TB MRC upgrade     

> __< plowsof >__  https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/516      

> __< r​ucknium:monero.social >__ FWIW, I think this proposal is fine. Will there be a report after the conference about how many local tickets vs international tickets were sold? IIRC, there is a discount on tickets to locals, so it should be easy to compute that data without any privacy issues.     

> __< ofrnxmr >__ They only had like 3 vip tickets left a couple days ago     

> __< plowsof >__ have MRL already shown sentiment for gingers new proposal Rucknium?     

> __< geonic >__ ruck: yes. although the PR co was clear with us that they're not expecting a huge rush of locals in such a short time. we're expecting most of the media coverage to come out after the conference. they promised to bring 20 journalists to the opening day of the conf.     

> __< r​ucknium:monero.social >__ Yes let me get the logs     

> __< plowsof >__ its 20xmr btw     

> __< ofrnxmr >__ for d. I'd say yes in principle, but i don't know that i like chainanysis node running mrl, and gingers unwillingness to share the ips that he was fwding to     

> __< ofrnxmr >__ Yes to proposal, no to proposer is my vote 🤷‍♂️     

> __< r​ucknium:monero.social >__ Discussed at these two MRL meetings: https://github.com/monero-project/meta/issues/1102 https://github.com/monero-project/meta/issues/1098 . Positive sentiment.     

> __< plowsof >__ thanks      

> __< geonic >__ (btw locals don't pay for tickets unless they want to enter the dome, so maybe ticket sales wouldn't be the best metric either)     

> __< r​ucknium:monero.social >__ Ok. If there are media pieces after, I would like to see those.     

> __< geonic >__ yes. media coverage would be my metric     

> __< plowsof >__ where those meetings with sunita open source??? meetings minutes??     

> __< plowsof >__ :D     

> __< geonic >__ :D     

> __< geonic >__ I'm afraid they used a proprietary technology called Zoom     

> __< plowsof >__ : ' (      

> __< plowsof >__ i think we can end it there. is there a monerokon meeting today? thanks all for joining and giving feedback      

> __< r​ucknium:monero.social >__ If the research computing server gets RAM, it would likely save the CCS money in the long term so that the server users do not have to spend time writing more complex code and lengthening the duration of `process --> analyze --> revise --> repeat`.     

> __< plowsof >__ thanks for joining msvb-lab!     

> __< geonic >__ ty     

> __< r​ottenwheel:kernal.eu >__ plowsof mononokon meeting already kicked off haha.     

> __< r​ottenwheel:kernal.eu >__ 5 minutes in.     

> __< plowsof >__ Greetings     

> __< msvb-lab >__ You're welcome, good meeting.     

> __< plowsof >__ benraouane i will ask mrnaif whats going on with bitcart and shopify store. do you have a link? is it an app store?     

> __< r​ucknium:monero.social >__ Maybe I shouldn't speak in the third person: I am one of the server users that has to spend time writing complex code and handling longer iterations.     

> __< b​enraouane:matrix.org >__ Still not built     

> __< plowsof >__ oh     

> __< b​enraouane:matrix.org >__ I propose to built it (& publish it through the app store)     

> __< plowsof >__ ah yes i understand     

> __< b​enraouane:matrix.org >__ @ofrnxmr:monero.social: as per the official documentation, it seems they generate a private key for each merchant     

> __< 0​xfffc:monero.social >__ monero.social account does not show matrix.org accounts messages.     

> __< o​frnxmr:monero.social >__ Uhoh     

> __< o​frnxmr:monero.social >__ the markets room is _totally_ broken     

> __< o​frnxmr:monero.social >__ Monero.social _only_ sees monero.social there     

> __< o​frnxmr:monero.social >__ [@0xfffc:monero.social](https://matrix.to/#/@0xfffc:monero.social)  i can see [@benraouane:matrix.org](https://matrix.to/#/@benraouane:matrix.org) 's messges     

> __< 0​xfffc:monero.social >__ Are you sure? there is a message from Benraouane Soufiane  " as per the official documentation, it seems they generate a private key for each merchant " which I see in IRC, but don't see in Element.     

> __< 0​xfffc:monero.social >__ ofrnxmr     

> __< o​frnxmr:monero.social >__ Ouch     

> __< o​frnxmr:monero.social >__ The server is breaking down     

> __< r​ecanman:kernal.eu >__ Let's write a new protocol that is better!     

> __< r​ecanman:kernal.eu >__ (joking)     

> __< o​frnxmr:monero.social >__ Lets call it "irc"     

> __< o​frnxmr:monero.social >__ Niocat would be so proud     

> __< d​etherminal:monero.social >__ MHMP     

> __< r​ecanman:kernal.eu >__ Hahaha     

> __< d​etherminal:monero.social >__ Monero Hidden Messaging Protocol     

> __< r​ecanman:kernal.eu >__ blockchain messaging!!!     

> __< d​etherminal:monero.social >__ As if it would be secure...     

> __< r​ecanman:kernal.eu >__ Lol     

> __< nioCat >__ ofrnxmr yes irc works even here in the emergency room     

> __< nioCat >__ Not here for me  :)     

> __< nioCat >__ Will catch up later     

> __< o​frnxmr:monero.social >__ Why not catch down?     

> __< m​rnaif:matrix.org >__ That's because to be listed there you need to be fit under many conditions, maintain a legal entity I believe and many more conditions. My friend told me that it took them a year to get approved into shopify store. The hack we use is the best without having any legal entity and in decentralised nature     

> __< plowsof >__ Thank you mrnaif      

> __< b​enraouane:matrix.org >__ Yes, that's true, I forget, it's not about development issue,     

> __< b​enraouane:matrix.org >__ : Even I'll build the app, I'll not submit for listing on the app store     

> __< b​enraouane:matrix.org >__ plowsof @plowsof:matrix.org:  Even I'll build the app, I'll not submit for listing on the app store     

> __< plowsof >__ Ben just fork vitcart      

> __< plowsof >__ Bitcart* it has everything you need :(     

> __< plowsof >__ How to monetize it you may wonder. Selling it as a SaaS, either giving a merchant (power user) access to an account , or, charging for consulting / setting up the integration and maintaining it .. mr aif are there other ways i can become rich from bitcart?     

> __< plowsof >__ mrnaif*     

> __< m​rnaif:matrix.org >__ selling it as saas is something I've been trying for a while, but I still need to get my legal consultation whether I need any licenses to do so. this is the best way to monetize opensource projects. but yeah, it's complicated with mica and other stuff coming soon     

> __< plowsof >__ Great to hear your perspective, thank you again. Perhaps Siren/Stnby of moneropay/digilol have sought advice already about this      


Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: plowsof | 2024-11-07T09:15:57+00:00
- Closed at: 2024-11-20T16:18:03+00:00
