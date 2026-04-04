---
title: 'Monero Community Workgroup Meeting: Oct 25th 16:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1286
author: plowsof
assignees: []
labels: []
created_at: '2025-10-25T14:01:21+00:00'
updated_at: '2025-11-05T10:14:37+00:00'
type: issue
status: closed
closed_at: '2025-11-05T10:14:37+00:00'
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
    - XMRig gains RISC-V support - sech1 (full credits in PR comment) https://github.com/xmrig/xmrig/pull/3725
    - https://github.com/P2Pool-Observer/consensus WIP by DataHoarder
    - https://github.com/monero-project/research-lab/issues/151
    - Light Wallet Server (LWS) wallet Skylight beta testing via [sgp_/MAGIC](https://libera.monerologs.net/monero-community/20251024#c601805)
    - "[making a follow](https://xcancel.com/thefuzzstone/status/1982092405211095142) list for Nostr, so we don't lose each other when Twitter/X block us all here" - TheFuzzStone
News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [This Week In Monero](https://cyphergoat.com/blog)
4. [CCS updates](https://ccs.getmonero.org/)    
  a. [MoneroOS Resurrection](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/596)    
  b. [Monero Python Maintenance](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/598)    
  c. [v1docq47 - monero konferenco 2025 voice-over and working on xmr.ru](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/607)    
  d. [acx part-time work on Monfluo 2025Q4](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/616)    
  e. [xmr-support-thorchain](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/619)    
5. Workgroup reports    
  a. Dev workgroup
  b. Localization workgroup
  c. Outreach workgroup
  d. Events workgroup - https://github.com/monero-project/meta/issues/1284
  e. Website workgroup - a new face wanting to push the redisgn along [redsh4de](https://github.com/monero-project/meta/issues/1284)
  f. Policy workgroup
  g. Research workgroup
  h. [Seraphis Migration workgroup](https://github.com/seraphis-migration)
6. Open ideas time    
7. Confirm next meeting date/time    

[Previous meeting including logs](https://github.com/monero-project/meta/issues/1276)    

Meeting logs will be posted here afterwards.    

# Discussion History
## plowsof | 2025-11-05T10:14:14+00:00
Logs 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

## plowsof | 2025-11-05T10:14:27+00:00
Logs 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
> **\<plowsof\>** meeting time     
    
> **\<plowsof\>** greetings, hi https://github.com/monero-project/meta/issues/1286     
    
> **\<parasew:matrix.org\>** <parasew:matrix.org> hi     
    
> **\<sgp_\>** <sgp_> Hello     
    
> **\<hbs:matrix.org\>** <hbs:matrix.org> hello     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> XMRig gains RISC-V support - sech1 (full credits in PR comment) https://github.com/xmrig/xmrig/pull/3725 ⛏️  improvements can be seen in the linked PR https://github.com/xmrig/xmrig/pull/3724     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> from 14 H/s to 33 .. to 100~ for the ORANGE PI RV2      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> to beta test the skywallet (monero LWS wallet) request from sgp with a Play Store account email Skywallet (https://libera.monerologs.net/monero-community/20251024#c601805) , i tried it out briefly earlier, built in tor, connects to any LWS instance.. looks great so far👍️     
    
> **\<elongated:matrix.org\>** <elongated:matrix.org> @plowsof:matrix.org: Any guide to setup lws instance ?     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> do you like Docker? xD     
    
> **\<jack_ma_blabla:matrix.org\>** <jack_ma_blabla:matrix.org> @plowsof:matrix.org: sure, i can try on macos     
    
> **\<sgp_\>** <sgp_> I can definitely use some help for more community lws setup guides. I already made one and probably won't have much time to make others: https://www.privacyguides.org/articles/2025/06/12/monero-server-using-truenas/     
    
> **\<jack_ma_blabla:matrix.org\>** <jack_ma_blabla:matrix.org> @plowsof:matrix.org: they couldnt find a orignal name ? https://play.google.com/store/apps/details?id=com.sky.wallet.tech     
    
> **\<sgp_\>** <sgp_> *Skylight Wallet, https://skylight.magicgrants.org/     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> much better name, Skylight , sorry      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> elongated i need to use https://github.com/MAGICGrants/monero-lws-docker myself so ill let you know how it goes later today      
    
> **\<jack_ma_blabla:matrix.org\>** <jack_ma_blabla:matrix.org> @sgp_: https://mrelay.p2pool.observer/m/matrix.org/RqaAxtwZQedUFKFADLFobNLe.png (image.png)     
    
> **\<jack_ma_blabla:matrix.org\>** <jack_ma_blabla:matrix.org> https://play.google.com/store/apps/details?id=org.magicgrants.skylight      
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> @jack_ma_blabla:matrix.org: You need an invite     
    
> **\<hbs:matrix.org\>** <hbs:matrix.org> @jack_ma_blabla:matrix.org: doesn't seem available in my country     
    
> **\<parasew:matrix.org\>** <parasew:matrix.org> @hbs:matrix.org: also does not work for me     
    
> **\<sgp_\>** <sgp_> I need to add the email first then it'll work. You all are early, before I've even made an actual announcement for it     
    
> **\<sgp_\>** <sgp_> I'll add your Google Play email if you DM me, or email me it (justin⊙mo)     
    
> **\<sgp_\>** <sgp_> The app is in flutter so iOS will work too, shortly after     
    
> **\<sgp_\>** <sgp_> @plowsof:matrix.org: Use this instead: https://github.com/vtnerd/monero-lws/pkgs/container/monero-lws     
    
> **\<sgp_\>** <sgp_> Lee now maintains their own     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> ohh, thanks!     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> a post quantum monero address: https://libera.monerologs.net/monero-research-lounge/20251022#c601238     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> thats a CSIDH-512	, 346 char address from https://github.com/monero-project/research-lab/issues/151      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> fits on a QR and could make open alias great again, great again      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> any other highlights to bring up? https://github.com/P2Pool-Observer/consensus WIP by DataHoarder Monero P2Pool consensus reimplementation     
    
> **\<DataHoarder\>** Main URL is https://git.gammaspectra.live/P2Pool/consensus     
    
> **\<DataHoarder\>** but this is not WiP it's what runs go-p2pool and observer :)     
    
> **\<DataHoarder\>** it also contains many golang utilities to interact with Monero related structures     
    
> **\<DataHoarder\>** it can mine, as well, and it was upgraded to support FCMP++ stressnet (this is the WiP part)     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> something to add under the bare Golang section? @ https://www.getmonero.org/resources/developer-guides/      
    
> **\<DataHoarder\>** feel free! I even have a monero RPC / ZMQ client within the consensus code, view wallet (for carrot and legacy), proof generation, etc.     
    
> **\<DataHoarder\>** for example it gets used on https://blocks.p2pool.observer/ as a general library     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> will make an issue/pr 👍️ i think we can move onto the ccs ideas, jumping into the most recent one as it has seen the most interaction     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> e. xmr-support-thorchain (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/619)     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> nack. they can fund it, and should do more research into monero current and future multisig etc     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> they plan to return: " If no financial support is tendered prior to integration, a second funding request will be made for launch liquidity instead."     
    
> **\<hbs:matrix.org\>** <hbs:matrix.org> funding liquidity????? Is that for real?     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Yes     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> A) pay 250k for integration, and we'll provide liquidity     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> B) pay 250k for liquidity, and we'll do implemtation pro bono     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> tl: we don't need the $, but we want 250k to trade with     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> only 250k for liquidity? we want to see numbers here!     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> 10,000 to cover Q1 2026     
    
> **\<hbs:matrix.org\>** <hbs:matrix.org> AFK writing a liquidity proposal for atomic swaps....     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Anyway, i think this is a bit backwards. As a seemingly very profitable service, they should be donating, not taking donations     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Especially since an xmr integration should benefit them financially     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> more info on the dev fee% as of oct 2025 in this tweet https://xcancel.com/THORChain/status/1973855591513698429      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> 75% of all fees go to "Incentive Pendulum Balances Rewards"  and i do see an "LP" under there, "Liquidity providers" so .. 🤷     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Anyway, i think this is a bit backwards. As a seemingly very profitable service, they should be donating, not taking donations.  Especially since an xmr integration should benefit them financially     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> if i close it after feedback will JP shoot the messenger and throw a tantrum 😬     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> leave it open     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Maybe theyll lower the price to -100xmr as a show of good will     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Also, jp not here to defend himself     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> his twitter handle https://x.com/jpthor      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> moving on, any other feedback for these prev discussed proposals:     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> a. MoneroOS Resurrection (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/596)     
    
> **\<@plowsof:matrix.org\>** <ofrnxmr:xmr.mx> (I just caught the reference) > <@plowsof:matrix.org> if i close it after feedback will JP shoot the messenger and throw a tantrum 😬     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> b. Monero Python Maintenance (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/598)     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> everoddandeven made a dockerfile for this proof of concept(that the library works on another machine) but i had dependency issues he was working through https://github.com/everoddandeven/monero-spammer      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> if the library is proven to actually work by someone or myself, then at least this bounty can be paid out https://bounties.monero.social/posts/171/3-432m-create-python-bindings-for-the-monero-cpp-library and hopefully the ccs merged      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> c. v1docq47 - monero konferenco 2025 voice-over and working on xmr.ru (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/607)     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> i left a comment summarising the last proposal and how it was funded @ https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/607#note_32343 , this looks to not be a blocker but just a note that there is no extra help available if the same happens      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> d. acx part-time work on Monfluo 2025Q4 (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/616)     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> any comments on any proposal mentioned here, feel free to share      
    
> **\<@plowsof:matrix.org\>** <everoddandeven> I can give further support to you and anyone who wants to verify it works 🙏 > <@plowsof:matrix.org> if the library is proven to actually work by someone or myself, then at least this bounty can be paid out https://bounties.monero.social/posts/171/3-432m-create-python-bindings-for-the-monero-cpp-library and hopefully the ccs merged      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> recanmann posted a summary of a recent meeting reg a possible Mokerokon location for 2026 https://github.com/monero-project/meta/issues/1284#issuecomment-3446883779      
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> There is a meeting today for that     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Oh, it overlapped :D lol     
    
> **\<kayabanerve:matrix.org\>** <kayabanerve:matrix.org> Hello, I just popped in and saw a meeting was occurring     
    
> **\<kayabanerve:matrix.org\>** <kayabanerve:matrix.org> I'd note CSIDH-512 is very unlikely compared to 1024 plowsof     
    
> **\<kayabanerve:matrix.org\>** <kayabanerve:matrix.org> @ofrnxmr:xmr.mx: And as users could provide that liquidity. they don't need users to surrender that money so they themselves (JP) provide it.     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> ah i see, looking at the table(s) (https://github.com/monero-project/research-lab/issues/151) , CSIDH-1024 is an extra 103 chars, with barely any tx size difference for an attack time of 4×10^7 years as opposed to 512's 9000 years kayabanerve      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> wallet scan time :(      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> thanks all for joining, an open end     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> #monerokon:matrix.org     
    
> **\<@plowsof:matrix.org\>** <syntheticbird> how did i miss that > <@plowsof:matrix.org> ah i see, looking at the table(s) (https://github.com/monero-project/research-lab/issues/151) , CSIDH-1024 is an extra 103 chars, with barely any tx size difference for an attack time of 4×10^7 years as opposed to 512's 9000 years kayabanerve      
    
> **\<syntheticbird\>** <syntheticbird> tevador cooking hard     
    
> **\<syntheticbird\>** <syntheticbird> lets go     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> the newsletters will continue to increase in numbers until we know everything and morale improves     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> @ofrnxmr:xmr.mx: yep in #monerokon:matrix.org     
    
> **\<plowsof:matrix.org\>** 18:28:39 <br-m> <plowsof:matrix.org> will make an issue/pr 👍     
    
> **\<DataHoarder\>** also, as a note I do pass all the monero crypto tests from https://raw.githubusercontent.com/monero-project/monero/refs/heads/master/tests/crypto/tests.txt, except the three ones about create/check ring signatures which are skipped (I don't handle ring signatures)     
    
> **\<xmrtimes:matrix.org\>** <xmrtimes:matrix.org> hi guys     
    
> **\<xmrtimes:matrix.org\>** <xmrtimes:matrix.org> I'm creating a Monero Journal     
    
> **\<syntheticbird\>** <syntheticbird> @xmrtimes:matrix.org: ngl we have plenty of reputable news source, but hey why not a new one.     
    
> **\<ofrnxmr\>** <ofrnxmr> @syntheticbird: No we dont     
    
> **\<ofrnxmr\>** <ofrnxmr> Theres a civil war going on     
    
> **\<syntheticbird\>** <syntheticbird> @ofrnxmr: monero.observer?     
    
> **\<syntheticbird\>** <syntheticbird> @ofrnxmr: LMFAO     
    
> **\<ofrnxmr\>** <ofrnxmr> @syntheticbird: Didnt you see above? cyphergoat's TWIM has been officially warned     
    
> **\<syntheticbird\>** <syntheticbird> no i didn't     
    
> **\<ofrnxmr\>** <ofrnxmr> That's 2 strikes. One more and revuo uses the samson option     
    
> **\<ofrnxmr\>** <ofrnxmr> https://matrix.to/#/!WzzKmkfUkXPHFERgvm:matrix.org/$Oe7Jnux7kHa4PMWoun8UsxUhQ_44ZuB3T0lhY8mF57o?via=cypherstack.com&via=matrix.org&via=monero.social     
    
> **\<@rottenwheel:unredacted.org\>** <ofrnxmr> ^ > <@rottenwheel:unredacted.org> Now it is this nobody that does nothing but copy and paste prior work, both for his bs copy/paste weekly newsletter, and his "business".     
    
> **\<@rottenwheel:unredacted.org\>** <ofrnxmr> ^ > <@rottenwheel:unredacted.org> Last time I say it, hold back on that response like you did in the copy/paste witch hunt. It is in your best interest.     
    
> **\<@syntheticbird\>** <rottenwheel:unredacted.org> Is journal... a news source? > <@syntheticbird> ngl we have plenty of reputable news source, but hey why not a new one.     
    
> **\<rottenwheel:unredacted.org\>** <rottenwheel:unredacted.org> Maybe in French it might be... 😳     
    
> **\<rottenwheel:unredacted.org\>** <rottenwheel:unredacted.org> @xmrtimes:matrix.org: Pardon him, he's a bit... special, for lack of a better word. Were you saying, lad? What is this journal thing about? Do share.     
    
> **\<rottenwheel:unredacted.org\>** <rottenwheel:unredacted.org> Gottem. https://github.com/xmrtimes     
    
> **\<rottenwheel:unredacted.org\>** <rottenwheel:unredacted.org> https://xmrtimes.github.io/     
    
> **\<rottenwheel:unredacted.org\>** <rottenwheel:unredacted.org> Oh, what a disappointment, it is indeed, yet another XMR news site!     
    
> **\<rottenwheel:unredacted.org\>** <rottenwheel:unredacted.org> Welcome aboard!!! 🥳     
    
> **\<@rottenwheel:unredacted.org\>** <syntheticbird> YES > <@rottenwheel:unredacted.org> Maybe in French it might be... 😳     
    
> **\<syntheticbird\>** <syntheticbird> GOOD JOB     
    
> **\<syntheticbird\>** <syntheticbird> YOU HAVE SUCCESSFULLY DOXXED ME     
    
> **\<rottenwheel:unredacted.org\>** <rottenwheel:unredacted.org> @syntheticbird: It's not like you call me rouuaiuasdipourriette every Sunday out here...     
    
> **\<torir:matrix.org\>** <torir:matrix.org> Even simple low-effort news aggregation is helpful, but it would be nice if TWIM put in enough effort to catch when the MiningPoolStats piechart is clearly broken: https://cyphergoat.com/blog/twim-6     
    
> **\<torir:matrix.org\>** <torir:matrix.org> Ahem: https://cyphergoat.com/blog/twim-6#hashrate-distribution     
    
> **\<plowsof\>** sgp_ how many subaddresses does skylight wallet attempt to generate from monero-lws? for now i just enabled some high limit to stop the warning about exceeding the max      
    
> **\<sgp_\>** <sgp_> It looks for the first unused from account 0     
    
> **\<plowsof\>** ah ok, i must not have set the max subaddresses command, i managed to start a monero-lws instance without needing to read too many docs, but without httpS support and open registration. skylight wallet connects fine, ill try to send/receive some      
    
> **\<plowsof\>** how is the monero-lws admin panel scene? im only aware of https://github.com/CryptoGrampy/monero-lws-admin     
    
> **\<plowsof\>** but npm is scary      
    
> **\<sgp_\>** <sgp_> I personally don't use the admin API at all     
    
> **\<sgp_\>** <sgp_> @elongated:matrix.org @parasew:matrix.org @rbrunner7:monero.social https://github.com/MAGICGrants/skylight-wallet     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> for testing im using docker run --name monero-lws   --network host   ghcr.io/vtnerd/monero-lws:latest   --daemon=tcp://127.0.0.1:18082   --sub=tcp://127.0.0.1:18084 --rest-server http://0.0.0.0:8443 --confirm-external-bind --auto-accept-creation --max-subaddresses 20000     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> with port 8443 open      
    
> **\<sgp_\>** <sgp_> this is why TLS verification doesn't currently work btw https://github.com/MAGICGrants/skylight-wallet/issues/6     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> i promised elongated i would set it up, so i have a slight headache because i had to read "--help" a few times :D      
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> https://mrelay.p2pool.observer/m/matrix.org/TdufzfWAFjfZVYhADfiyWFOF.jpg (1000010543.jpg)     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> Walla try my onion?     
    
> **\<plowsof:matrix.org\>** <plowsof:matrix.org> sgp_ seems to be working, didnt get a notification though (iirc i did allow the popup, but so far working)     
    
> **\<sgp_\>** <sgp_> I'm not 100% confident the notifications work correctly     
    
> **\<sgp_\>** <sgp_> Is there a community LWS matrix channel? Maybe it's time for one     
    
> **\<ofrnxmr:xmr.mx\>** <ofrnxmr:xmr.mx> @sgp_: No     
    
> **\<nioc\>** sgp is there a community LWS IRC channel?      
    
> **\<sgp_\>** <sgp_> Maybe? No idea     
    
> **\<ofrnxmr\>** <ofrnxmr> No     
    
> **\<nioc\>** sgp I was hinting that if a room is set up then don't forget IRC  :)     
    
> **\<plowsof\>** never      

Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: plowsof | 2025-10-25T14:01:21+00:00
- Closed at: 2025-11-05T10:14:37+00:00
