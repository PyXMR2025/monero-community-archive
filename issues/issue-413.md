---
title: 'Emergency Response Process and Compromised Binaries Post-Mortem Meeting: 22
  November 2019 23:00 UTC'
source_url: https://github.com/monero-project/meta/issues/413
author: SamsungGalaxyPlayer
assignees: []
labels: []
created_at: '2019-11-19T18:14:55+00:00'
updated_at: '2019-12-06T19:57:40+00:00'
type: issue
status: closed
closed_at: '2019-12-06T19:57:40+00:00'
---

# Original Description
**Location**

[Freenode](https://kiwiirc.com/nextclient/#irc://irc.freenode.net/#monero-community) | [Mattermost](https://mattermost.getmonero.org/monero/channels/monero-community) | [Slack](https://monero.slack.com/) | Irc2P

Please test the relays shortly before using. If there are any issues, please use Freenode IRC directly.

Please PM [SGP on Reddit](https://www.reddit.com/message/compose/?to=SamsungGalaxyPlayer&subject=Monero%20Slack%20invite%20(from%20GitHub)&message=Hello%20please%20send%20a%20Monero%20Slack%20invite%20to%20the%20following%20email:) with your email for a Slack invite if desired.

 - `#monero-community`

**Time**

23:00 UTC
17:00 CST (Chicago)

[Use this timezone calculator to convert UTC to your time zone](https://www.timeanddate.com/worldclock/converter.html?iso=20191122T230000&p1=tz_et&p2=28&p3=111&p4=49&p5=179&p6=70&p7=224&p8=48&p9=136).

**Proposed Meeting Items**

This meeting will collect introductory thoughts regarding #412 and will discuss the recent website issue with compromised binaries.

0. Introduction
1. Greetings
2. Website compromised facts and review
3. Introduction of emergency procedure
  a. safe verification of the emergency
  b. classification of the severity
  c. communication (internal and public)
  d. incident response
  e. regular tests/audits
  f. responsible roles, including alternates
  g. missed topics and frameworks
4. Action items
5. Conclusion

# Discussion History
## scottAnselmo | 2019-11-19T21:24:33+00:00
Also worth highlighting that https://github.com/monero-project/monero/issues/6151 contains some of the publicly available information concerning this issue worth looking at before the meeting for anyone planning on attending

## scottAnselmo | 2019-11-26T07:00:36+00:00
In an effort to provide a living doc-like SparkNotes version of what happened in identification and the user communications chain I'm creating this post:

[2019/11/18 09:21 MST](https://github.com/monero-project/monero/issues/6151) - nikitasius reports binary hash mismatch on GitHub
2019/11/18 ??:?? MST - Within 30 minutes of being disabled, File Integreity Monitor is re-enabled, switched to download server backup
[2019/11/18 21:51 MST](https://www.reddit.com/r/Monero/comments/dyfozs/security_warning_cli_binaries_available_on/) - binaryFate posts Reddit warning of bin's probalby being compromised
[2019/11/19 10:10 MST](https://repo.getmonero.org/monero-project/monero-site/commit/bad2fc789da9e2d5d8d1289318fba29994e38489) - erciccione authors banner + blog post
[2019/11/19 10:21 MST](https://repo.getmonero.org/monero-project/monero-site/merge_requests/1154#note_7656) - erciccione makes initial pull request
[2019/11/19 11:14 MST](https://repo.getmonero.org/monero-project/monero-site/merge_requests/1154#note_7676) - erciccione makes final adjustments to PR
[2019/11/19 11:35 MST](https://repo.getmonero.org/monero-project/monero-site/merge_requests/1154#note_7678) - luigi1111 approves PR

## scottAnselmo | 2019-11-26T07:45:49+00:00
Log from meeting. Note that some special characters aren't handled properly in the Discord bridge/client, will fix later. 

```
[23:00] <sgp_> 0. Introduction
[23:00] <needmonero90> Hi diego
[23:00] <sgp_> Welcome to the Emergency Response Process and Compromised Binaries Post-Mortem Meeting. Today, we shall discuss the information we know so far about the compromised binaries and introduce ideas to better respond to emergencies in the future.
[23:00] <sgp_> Itâ€™️s later than most of our meetings, so thank you for coming at this unusual time.
[23:00] <sgp_> 1. Greetings
[23:00] <needmonero90> Hello!
[23:00] <M5M400> Servus!
[23:00] <binaryFate> hi
[23:01] <pizzaburger> Good day!
[23:01] <anhdres2> hola!
[23:01]  <intj440> Hello
[23:01] <mrpublic> top o the mornin'
[23:02] <sgp_> Welcome everyone! There is a lot to cover, so let's move methodically so that we can respect those staying up late
[23:02] <el00ruobuob_[m]> Hi
[23:02] <ArticMine> hi
[23:02] <sgp_> long set of text incoming describing the situation, including new information
[23:02] <almutasim> Hello.
[23:03] <sgp_> Here is a short timeline of the events that unfolded earlier this week:
[23:03] <sgp_> The CLI binaries were compromised for approximately 35 minutes on Monday
[23:03] <sgp_> The attackers did not modify the hashes on the website
[23:03] <needmonero90> Is that time frame known for certain?
[23:03] <sgp_> Core team member binaryFate created a Reddit post and messaged me about it on IRC. He shared it on his personal Twitter account
[23:04] <sgp_> Reddit link: https://www.reddit.com/r/Monero/comments/dyfozs/security_warning_cli_binaries_available_on/
[23:04] <needmonero90> waits patiently 
[23:04] <monerobux> [REDDIT] Security Warning: CLI binaries available on getmonero.org may have been compromised at some point during the last 24h. (self.Monero) | 270 points (98.0%) 
[23:04] <sgp_> I found it likely that this was true given binaryFate’s position and that it was shared on three different mediums. Thus, I immediately sent Blockfolio, CoinGecko, and Delta notifications. I created a tweet from the Monero Twitter account
[23:04] <sgp_> Note that although I have partial access to the Monero Twitter account, I am not the primary owner or maintainer of it, and the tweet I created was an exception for the circumstances
[23:04] <sgp_> I also contacted the other moderators of r/CryptoCurrency, who agreed to allow an announcement about the situation in r/CryptoCurrency
[23:04] <sgp_> ErCiccione authored an announcement on the website about 14 hours after the incident was initially reported. An email to the Monero-announce mailing list went out around the same time.
[23:04] <sgp_> Approximately 12 hours after the sending the Blockfolio notification, it had 14,673 impressions and 259 clicks. Today, it has 25,308 impressions and 326 clicks. I don't have numbers for the other portfolio platforms.
[23:05] <sgp_> The Reddit thread has nearly 300 upvotes and nearly 300 comments.
[23:05] <sgp_> Twitter reports that the initial tweet has 100,918 impressions and 1,455 engagements.
[23:05] <sgp_> Major and minor news sites picked up on the story, including Naked Security, Crypto Briefing, The Next Web, Ars Technica, ZDNet, CoinGeek, Fossbytes, CoinTelegraph, Bleeping Computer, AMBCrypto, Bitcoinist, Coingape, Finder, and Decrypt.
[23:05] <sgp_> There are a few writeups on the content of the malware:
[23:05] <sgp_> Bartblaze: https://bartblaze.blogspot.com/2019/11/monero-project-compromised.html
[23:06] <sgp_> Now, on to the website information.
[23:06] <sgp_> I can answer a few more questions than I could before, but I can’t answer everything yet, including how the website was compromised. I have no insider info there
[23:06] <sgp_> The downloads are served by two sources: the CDN and the source. The CDN binaries were not affected, which are the preferred sources. The source is fallback.
[23:06] <sgp_> After the hack, the security admins temporarily turned logging on with the DR download box (which was switched to) in case someone was trying to hack it. A benefit of this is that we learned there are typically fewer than 10 wallet downloads per hour from the direct source.
[23:07] <sgp_> Full timeline:
[23:07] <sgp_> The FIM’s last log entry was at 16:04 UTC (10:04 CST) - malicious binaries were not served before this point
[23:07] <sgp_> A Github issue was created at 16:21 UTC
[23:07] <sgp_> A community member privately informed site admins at 16:30 UTC
[23:07] <sgp_> fluffypony switched to the failover at 16:40 UTC
[23:08] <sgp_> The maximum compromised time was between 16:04 UTC and 16:40 UTC Monday November 18
[23:08] <sgp_> Since they were served for only 35 minutes, it’s highly likely that fewer than 10 malicious downloads were served. Among these, some were presumably updating their nodes, not running wallets.
[23:08] <sgp_> Does anyone have questions or comments on what happened? I won’t be able to answer some of them unfortunately but I’ll do my best.
[23:08] <M5M400> one question comes to mind: HOW?
[23:09] <needmonero90> The security researchers are dealing with the box atm
[23:09] <needmonero90> We'll probably only know after their analysis
[23:09] <sgp_> M5M400: that's an important question that I don't really have the answer to
[23:09] <sgp_> But I am certain that a dedicated team is digging through the boxes
[23:10] <M5M400> disaster recovery
[23:10] <DarkDotFail> "it’s highly likely that fewer than 10 malicious downloads were served" - I assume this is based on logs? How confident are you in this count?
[23:11] <sgp_> I find it remarkable that two independent community members reported on the issue within 30 minutes
[23:11] <M5M400> when did fluffy upload the original files? ie, how long did it take them from upload to replacment?
[23:11] <Supportoi> Sio
[23:11] <sgp_> DarkDotFail: unless there was a significant anomaly (3+ sd downloads over that period), then I am very confident. So I'd say >95% confident
[23:12] <Supportoi> Any news?
[23:12] <HungryForAvo420> Are there any plans to periodically check sha256 hashes?
[23:12] <sgp_> There are almost never more than 10 downloads/hr. And it was compromised for 35 minutes
[23:12] <DarkDotFail> Who has server access, and what is the process for giving someone server access?
[23:12] <Supportoi> I read about hacking this is Russian hackers
[23:12] <sgp_> Supportoi: there is no evidence I know of that suggests this
[23:12] <anhdres> is it my non-techie impression or we got very lucky here? I mean we only realized it because someone that downloaded the CLI checked the hashes AND they didn't change the hashes accordingly
[23:13] <Supportoi> I downloaded this fkng cli
[23:13] <Supportoi> I'm not infected?
[23:13] <Supportoi> My money not stolen
[23:13] <Supportoi> But I worry about my PC
[23:13] <sgp_> Supportoi: when did you download the cli exactly?
[23:13] <anhdres> needmonero90, ok
[23:13] <Supportoi> 18th
[23:13] <sgp_> DarkDotFail: I do not have a full list
[23:14] <sgp_> Supportoi: what time and what time zone?
[23:14] <DarkDotFail> and regarding the process of granting access, how is it determined who should have access?
[23:14] <needmonero90> As few people as is realistically possible
[23:14] <Supportoi> SHA is eq to SHA of infected files
[23:14] <almutasim> It's really good that changing the hashes requires hacking a second box.
[23:14] <rehrar> DarkDotFail Tari or Globee hosts the getmonero infrastructure
[23:14] <xmrscott[m]> Supportoi: Verify your hashes, that will conclusively tell you if it's the nalicious binary
[23:14] <rehrar> the details would have to be asked of them
[23:14] <anhdres> is there a way to have a bot somewhere else doing just what the human user did by chance? I mean downlaoding the files regularly and checking the hashes to see they match, and if they don't issue an alarm?
[23:15] <DarkDotFail> anhdres: I am working on precisely that :)
[23:15] <sgp_> anhdres: while technically possible, this service would probably be blocked as a DoS attack
[23:15] <needmonero90> That would be a tiny DOS on the server, and if done with a consistent IP, it's possible to serve uninfected binaries to the pollers
[23:15] <Supportoi> Fkng Russian hackers
[23:15] <anhdres> mmmm...
[23:15] <sgp_> there are a stupid number of people who constantly are trying to download the 55GB blockchain.raw
[23:15] <M5M400> when did fluffy upload the original files? ie, how long did it take them from original upload to replacment with compromised bins?
[23:15] <needmonero90> Supportoi: please keep on topic, speculation on who did this is unwarranted at the moment.
[23:16] <needmonero90> We will know more after the post mortem
[23:16] <Supportoi> I reading news and founded article about some hacking russian forum
[23:16] <DarkDotFail> sgp_: Is there any indication yet that the server was compromised, and how?
[23:16] <sgp_> M5M400: are you referring to the time between the 0.15 safe binary uploads and them being compromised?
[23:16] <M5M400> sgp_: yes
[23:16] <Supportoi> Where they have article about monero hacking
[23:16] <binaryFate> M5M400 the malicious binaires were compiled from sources, they are not obtained based on the original ones. So it's indepedendant from original upload time.
[23:16] <Supportoi> Russian hackerssssssss omg
[23:16] <sgp_> DarkDotFail: yes, I can state that the website WAS compromised, though I do not yet have details on how
[23:16] <anhdres> good thing it wasn't the GUI, because those would have been less technical users and therefore less probable they checked the hashes. We need a fool-proof official tutorial to teach how to check them.
[23:16] <needmonero90> Supportoi: last warning.
[23:16] <DarkDotFail> sgp_: Has law enforcement been notified about this breach?
[23:17] <pizzaburger> Is there a possibility that the attackers were after something else and we just haven't noticed their ulterior motives?
[23:17] <PewPewPewPew> ^^
[23:17] <M5M400> binaryFate: trying to gauge how premeditated this attack was... ie if they had everything ready and possibly already access to the box for a while, just waiting for new bins to be uploaded and then quickly replacing them...
[23:17] <sgp_> DarkDotFail: no, and we have not yet found a strong reason to. I will make a recommendation that the security researchers do (in addition to their own assessments) if there's a clear reason to. I do not have knowledge on the state of the investigation to make a recommendation
[23:18] <HungryForAvo420> What is the decommission schedule for source box? CDN was not impacted, but am wondering what the maintanance is like for Source.
[23:18] <needmonero90> I would like to point out that the attack felt rushed/incomplete, from reports I'm hearing. There were many things that could have been done that weren't (infecting the GUI dls for example)
[23:19] <sgp_> pizzaburger: while we can never know for sure what their motivations were, we know the security researchers only found a relatively primitive coin stealer included in the wallet software
[23:19] <Supportoi> I'm worry about my privacy.  I'm not programmer but I know some in programming and security. My antivirus not detected danger, I runned this file.
[23:19] <DarkDotFail> How long has FIM been installed, and has it ever detected other anomalies?
[23:19] <Supportoi> And I readed about this forum. This forum contains information about CLI replace
[23:19] <sgp_> DarkDotFail: I do not know for how long, but FIM was disabled by the attacker
[23:19] <Supportoi> Somebody know some about this?
[23:19] <DarkDotFail> Has FIM ever detected other anomalies?
[23:20] <needmonero90> Supportoi: this has nothing to do with the issue at hand. Please stay in topic for the meeting.
[23:20] <PlasmaPower> I know you don't know how it was compromised yet, but what were the potential avenues of attack for the box other than an insider threat? The web server, maybe SSH, maybe a cloud provider?
[23:20] <M5M400> needmonero90: that's my gut feeling aswell. that's why I was asking how long it took them to replace the bins after initial upload... but I don't seem to get an answer :)
[23:20] <sgp_> DarkDotFail: I do not know about the test environment in which it was tested, but I know there were no other anomalies on the live version of the site
[23:20] <DarkDotFail> Thank you. that's very good.
[23:20] <Supportoi> I payed 50$ in xmr to body from comments and they gived me screenshot
[23:21] <sgp_> M5M400: I don't know when the original 0.15 binaries were uploaded, but that's something we can check on I suppose
[23:22] <sgp_> Any other questions? Sorry to not have juicy details yet on how this happened
[23:22] <binaryFate> this reddit post suggest the 9th: https://www.reddit.com/r/Monero/comments/dtt2j3/cli_v01500_carbon_chamaeleon_released/
[23:22] <monerobux> [REDDIT] CLI v0.15.0.0 'Carbon Chamaeleon' released! (self.Monero) | 158 points (100.0%) | 64 comments | Posted by dEBRUYNE_1 | Created at 2019-11-09 - 07:55:00
[23:22] <DarkDotFail> I want to quickly commend Justin and team for the quick response. My complaint is that the public website took over 14 hours to update after the breach, and I suggest we get a quicker "post an alert to the website" process in place. Going AFK for now, but be safe everyone.
[23:23] <M5M400> binaryFate: that would speak for the less premeditated "uh, new release. let's try to hack that box and replace with our coinstealer" theory
[23:24] <rehrar> honestly, the timing of this seems too good for it to not be premeditated
[23:24] <xmrscott[m]> binaryFate: Also semi-verified going off of WebArchive for getmonero
[23:24] <needmonero90> Processes are being put in place to expedite updates of the public site in the event of a security event. 14 hours was excessive, but we can do better.
[23:24] <ZaiRoX> Strange of them not waiting for the GUI release though
[23:24] <M5M400> rehrar: why wait 5 days then?
[23:24] <rehrar> honestly, who updates CLI early? Exchanges. Services.
[23:24] <rehrar> I think they were hoping for big fish.
[23:24] <binaryFate> Agree website update has the largest room for improvement.
[23:24] <M5M400> rehrar: agreed.
[23:24] <anhdres> would a stupid but useful security measure to suggest to newbie users for them to wait a few hours before running a downloaded binary and see if there's any warning on an official channel?
[23:25] <needmonero90> Hash checking should be sufficient
[23:25] <needmonero90> And signature ofc
[23:25] <sarang> With signature verification you know the file is what it is expected to be
[23:25] <rehrar> M5M400 you asked why wait 5 days after the new CLI was released?
[23:25] <needmonero90> I think prioritizing teaching people how to verify signatures is infinitely better than having them wait for a few hours and hope someone notices
[23:25] <rehrar> because if you release ASAP, everyone is downloading and testing. They will catch it right away.
[23:25] <needmonero90> That's just me tho
[23:26] <sgp_> they also compromised the website at a relatively convenient time
[23:26] <M5M400> rehrar: makes sense
[23:26] <sgp_> time of day
[23:26] <PlasmaPower> frankly, even Monero's "beginner" guide to signature verification on Windows is way too long
[23:26] <anhdres> ok, and based on that "hacking" the hash to match the compromised binary would be too difficult to pull of, right?
[23:26] <M5M400> rehrar: good thing the "big fish" are usually the laziest in updating, I guess...
[23:26] <rehrar> PlasmaPower I just spoke about this with another individual that does website stuff.
[23:26] <sgp_> anhdres: it's more realistic to check the hashes haven't changed
[23:26] <rehrar> We need to separate verification user guides into three. Linux, Mac, and Windows.
[23:26] <rehrar> They won't be so long or scary then.
[23:27] <sgp_> rehrar: good, that's a specific action item
[23:27] <rehrar> I was literally helping a person on Telegram and told him to verify hashes and he got scared by how big the page was and how much CLI commands there were
[23:27] <anhdres> sgp_, needmonero90 : got it thanks
[23:27] <pizzaburger> Thank you for the information and hard work. Best of luck to the Monero team, bye!
[23:27] <PlasmaPower> rehrar: the Windows specific guide is still long, though not scary except the small part that requires command prompt
[23:27] <xmrscott[m]> FWIW with respect to timing, domain was bought 11/14. Arguments could be made that a purchase so close to delivering the attack means it wasn't pre-meditated, but best to wait for the official report
[23:28] <M5M400> xmrscott[m]: ah, I forgot about that domain info. makes perfectly sense
[23:28] <justalurk3r> sgp_: I, too, have downloaded the compromised binaries. If my browser history is right, then it must have happened at 12:24 CET
[23:28] <anhdres> would it be too cumbersome to develop a little monero-branded, hash-checking program for windows that required no installation so a very noob could use it practically guide-less?
[23:28] <M5M400> sgp_: any info which hosting company the infected box belongs to?
[23:29] <sgp_> M5M400: I don't know that
[23:29] <PlasmaPower> anhdres: I thought about that too, but then what if that binary gets compromised :P
[23:29] <needmonero90> Andrhes: and if they compromise that?
[23:29] <needmonero90> Jinx
[23:29] <anhdres> well, it needs to be in a third box
[23:29] <sgp_> the malicious software would just say "I'm totally safe"
[23:29] <needmonero90> :thinking:
[23:29] <cbster> Yeah, were it too simple I think they'd just change that program too
[23:30] <anhdres> if screwing with the hash is "safe" we could do the same with the app
[23:30] <sarang> The only guarantee is a full hash and signature check
[23:30] <needmonero90> ^
[23:30] <sarang> Only doing hash checks is potentially vulnerable
[23:30] <cbster> Agreed, a lot of people leave off the signature check
[23:30] <sarang> It's annoying but important
[23:31] <tevador> one positive aspect of this incident is that people are more likely to verify the hashes from now on
[23:31] <M5M400> sgp_: is there any intersection in the groups of people who research the breach and the group who had access to the box?
[23:31] <rehrar> honestly, the entire cryptography space is long overdue for a good UX GUI for hash checking and verification
[23:31] <rehrar> one that could be used for all of the programs ever
[23:31] <needmonero90> Pgp is pretty good
[23:31] <anhdres> rehrar: yes, please
[23:31] <needmonero90> ...not
[23:31] <sarang> However if you're confident that externally hosted trusted hash lists have not been modified, then a hash check is ok
[23:31] <PlasmaPower> Are GitHub release assets generally deemed safer than the website downloads? I don't think they're GPG signed (though the tags themselves can be).
[23:32] <sgp_> PlasmaPower: it's simpler to hack a Github account probably
[23:32] <HungryForAvo420> Any consideration in using GitLab? have seen MS owned github drop some repos in some countries
[23:33] <pca> Just arrived.  How was the box compromised, or does anybody know that information yet?
[23:33] <tevador> are we signing git tags?
[23:33] <sgp_> HungryForAvo420: Monero already partially uses Gitlab, but this is mostly irrelevant for the conversation at hand
[23:33] <M5M400> pca: not yet
[23:33] <sgp_> For the sake of time, I'm going to warp up this section soon. Most of these questions have been answered in Reddit
[23:33] <rehrar> kthanksbai
[23:33] <PlasmaPower> tevador: I just checked, yes at least the latest tag was signed and most commits seem to be signed too.
[23:34] <needmonero90> Thanks for hosting sgp_
[23:34] <sgp_> just this section lol
[23:34] <sgp_> still have a few more
[23:34] <needmonero90> Oh rip
[23:34] <sgp_> that was just the update and clarification portion
[23:34] <xmrscott[m]> I was going to, still plenty left to discuss nm90 ;)
[23:34] <sgp_> now time to do actual work
[23:34] <needmonero90> nods sheepishly
[23:34] <sgp_> 3. Introduction of emergency procedure
[23:35] <M5M400> ah, the big red button
[23:35] <sgp_> I would like to introduce a project to draft more formalized emergency procedures. This procedure will help the community understand what to do if another emergency occurs.
[23:35] <anhdres2> haha everybody was "ok good one see ya" and Justin still had the cake untouched
[23:35] <sgp_> https://github.com/monero-project/meta/issues/412
[23:35] <sgp_> We can pull from existing resources, including the Monero Vulnerability Response Process and the Monero Malware Response Workgroup.
[23:35] <sgp_> I know that the Monero community has significant concerns about centralization, and these are justified and should be considered carefully. Nevertheless, there are many was that this process can help organize a proper response without having many centralization advantages. And to be clear, it’s not like we can force people to follow a set procedure anyway. All participants’ involvement is entirely voluntary
[23:35] <sgp_> and subject to their own best judgments.
[23:35] <sgp_> I'm currently breaking the procedure into main topic areas: a) safe verification of the emergency, b) classification of the severity, c) communication, d) incident response, e) regular tests/audits, and f) responsible roles, including alternates in case of inactivity.
[23:36] <sgp_> Let’s open discussion on the 6 points that I have above, one at a time. We can talk about what processes (even if informal) we already have, and what you think is a good idea to help with these. If you feel there are any missed topics (likely), please reserve them for later.
[23:36] <sgp_> a. safe verification of the emergency
[23:36] <sgp_> in this case, we didn't have signed messages saying "this was compromised." We simply relied on several trusted accounts. What are our thoughts on this?
[23:37] <sgp_> also related: if people want to contact someone about an emergency, is there a clear disclosure process?
[23:37] <needmonero90> The people who would verify signatures of warnings would verify signatures of their binaries
[23:37] <PlasmaPower> you mean from the perspective of the user verifying the emergency, not the Monero team verifying the emergency?
[23:37] <needmonero90> Trust-y auth is fine here.
[23:37] <M5M400> I'm less worried about "fake news" as about response time, so I guess reputable community members breaking the news is fine
[23:38] <anhdres2> agree
[23:38] <cbster> I agree, even were there a false alarm I can't foresee harm from it
[23:38] <sgp_> needmonero90: is there a certain threshold where you would personally say "hold on a minute, I need some extra verification"?
[23:38] <sgp_> false alerts are unprofessional and also harm the project potentially
[23:38] <ArticMine> Provided one relies on decentralization for alarm security
[23:38] <needmonero90> If the person was in my web of trust, no. If they were not, I would manually verify sigs
[23:38] <xmrscott[m]> Wouldn't hurt to have public keys of core members on getmonero
[23:39] <needmonero90> Personal webs of trust are fine here, theyre probably just as effective (and faster) than signatures
[23:39] <sgp_> they're definitely faster
[23:39] <needmonero90> And that's what should be prioritized imo
[23:39]  <cff97476> hello to everyone
[23:40] <needmonero90> If there's questions, the warning can say it's a question mark
[23:40] <sgp_> I received binaryFate's RC PM and was sending out notifications 2 minutes later
[23:40]  <cff97476> any news?
[23:40] <needmonero90> I had a post stickied on the sub a minute after I got your ping
[23:40] <sgp_> cff97476: scroll up and find section 2
[23:41] <sgp_> ok, so we are all ok with relatively basic identity checks here
[23:41] <M5M400> +1
[23:41] <sgp_> no need to require something that would delay the process
[23:41] <cbster> +
[23:42] <sgp_> ok, so the second question
[23:42] <needmonero90> False positives are better than delayed warnings
[23:42] <ArticMine> yes there is enough redundancy
[23:42] <sgp_> do we have a clear disclosure process? who should people contact?
[23:42] <sgp_> how does the discoverer know how to initiate the process of raising the alarm?
[23:43] <binaryFate> I don't think we can assume much from people finding out something is wrong. It's not like programmers finding bugs who are technical and educated about response.
[23:43] <sgp_> surely long-time Monero members would probably contact people by DM and have personal relationships
[23:43] <cbster> My first thought would be to turn to Reddit, but not everyone knows the site
[23:43] <sgp_> but the first person to raise the alarm in this case did so through a Github issue
[23:44] <anhdres2> I would have used Reddit but I'm not technical
[23:44] <needmonero90> I suspect regardless of where it was posted (irc, github, gitlab, reddit), it would have percolate quickly
[23:44] <needmonero90> We have lots of lurkers
[23:44] <needmonero90> Percolated*
[23:44] <cbster> There could be a section added to the site clarifying what to do in an emergency
[23:44] <binaryFate> I think everyone's first thought will be different, and they are not going to dig for information to know how to disclose. Most people would think they are doing something wrong rather than recognize there is an actual issue
[23:45] <cbster> Perhaps detailing the subreddit, the GitHub and a few handles of core members
[23:45] <sgp_> something in the github readme may be appropriate imo
[23:45] <cbster> Although that could also lead to false alarms, not everyone understands emergencies
[23:45] <sgp_> I'm sure many users will report false alarms
[23:45] <PlasmaPower> I think that might send too much "spam" (users who think they have an emergency but don't) their way
[23:45] <PlasmaPower> yeah
[23:46] <ArticMine> across multiple platforms for redundancy
[23:46] <almutasim> False alarms have a price, too.
[23:46] <M5M400> binaryFate: agreed.
[23:46] <binaryFate> I find it more important to have an "internal" response process so that however this is disclosed, it then quickly gets put on the right rails by community members
[23:46] <M5M400> +1
[23:46] <ArticMine> +1
[23:46] <OWLHACKATHON> hello world
[23:46] <PewPewPewPew> is it safe to assume if someone found a problem like this again they would be technical enough to know about git and irc
[23:46] <sgp_> should we just point people who are new to #monero or something?
[23:46] <M5M400> PewPewPewPew: no
[23:46] <needmonero90> Don't we already?
[23:46] <cbster> I think it's wise to assume
[23:46] <cbster> Unwise*
[23:47] <needmonero90> Getting people to use IRC is like pulling teeth
[23:47] <sgp_> needmonero90: just something that clearly says to go to #monero in the case of an emergency
[23:47] <needmonero90> Ah I see
[23:47] <needmonero90> That could work
[23:47] <sgp_> eg: what if it's an exchange or mining pool who never talks to anyone
[23:47] <needmonero90> Oops
[23:47] <OWLHACKATHON> go to #churchofmonero ;)
[23:47] <binaryFate> Harmless but still a lot of people never used IRC whatsoever
[23:48] <cbster> It's always an option, we could offer multiple channels of reporting
[23:48] <cbster> I think IRC is a good start
[23:48] <needmonero90> binaryFate: linking to kiwiirc would work
[23:48] <sgp_> agreed, this is just something I think people should think about since not all the people who will notice major anomalies are always active
[23:48] <needmonero90> Webirc portal
[23:48] <needmonero90> No downloads, no logins
[23:48] <XeN> love IRC =)
[23:48] <binaryFate> It's fine to give them suggestions, but we should not assume they will follow nicely
[23:49] <sgp_> binaryFate: of course not, we just want to make it easier for people to know what they're supposed to do
[23:49] <sgp_> Anything else on a)?
[23:49] <PlasmaPower> There's a good amount of posts on r/Monero about people who lost funds because of something that was their fault like a fake web wallet, so I don't think telling people to DM the Monero team for emergencies is a good idea. A public location like IRC is probably the best idea.
[23:50] <cbster> Good point
[23:50] <sgp_> b. classification of the severity
[23:50] <sgp_> should we use low - medium - high, and how? who determines?
[23:50] <fluffyunicorn> ALL YOUR BASE ARE BELONG TO OWL
[23:50] <fluffyunicorn> >)>
[23:51] <fluffyunicorn> WEEEEEEE
[23:51] <needmonero90> Er
[23:51] <needmonero90> Can you not? This is a meeting
[23:51] <fluffyunicorn> IM HERE TO HACK STUFF
[23:51] <xmrscott[m]> (Sorry didn't look up in advance, re: A it may be good to look at Tails/Qubes escaltion process)
[23:51] <needmonero90> I'll remove after the meeting.
[23:51] <sgp_> xmrscott[m]: yes, it's important to look at what other people are doing too
[23:52] <sgp_> these classifications are common in projects and in the industry
[23:52] <cbster> I think low, high and critical give more emphasis
[23:52] <sgp_> we use it for HackerOne
[23:52] <sgp_> is there anyone who thinks this classification is unnecessary?
[23:53] <binaryFate> what is the purpose? Public disclosure later? Internal while we work on issue?
[23:53] <sgp_> binaryFate: depends on how it's used. could be either or both
[23:53] <sgp_> how do you envision it being used?
[23:54] <anhdres2> do the classifications change how / which channels are used ? or are they only informative?
[23:54] <cbster> I think they'd stay standard across platforms
[23:54] <binaryFate> I don't find it very useful for either, simply because these incidents are so rare
[23:55] <sgp_> anhdres2: they could
[23:55] <anhdres2> for example only critical are pushed to all channels and low ones only stick in reddit
[23:55] <cbster> Mind you, as Monero grows, they may not stay so rare
[23:55] <sgp_> indeed, these should happen rarely / never
[23:55] <xmrscott[m]> If they are used for escalation though the user may not know what the proper flag is, etc
[23:56] <PlasmaPower> Does anyone have an example of a low severity emergency? I'm thinking that things that send out a notification, like delta direct, shouldn't be used for those.
[23:56] <anhdres2> exactly
[23:56] <PlasmaPower> but I'm not quite sure what a low severity emergency would be, assuming that we aren't including 3rd party services
[23:56] <anhdres2> yellow warnings are usability or network related
[23:57] <anhdres2> red warnings are those when funds might be in danger and therefore are  not reversible
[23:57] <anhdres2> for example
[23:58] <sgp_> maybe something low would be like after RingCT was first added, where blocks were super full
[23:58] <sgp_> no attack necessarily, but degraded network experience
[23:59] <anhdres2> something like that yes
[23:59] <binaryFate> wasn't really about an emergency response
[23:59] <sgp_> unless there are other topics on this, we can move on from b)
[23:59] <ArticMine> It was a good cover for an emergency response
[00:00] <sgp_> c. communication (internal and public)
[00:00] <sgp_> this is communication standards and processes
[00:00] <sgp_> eg: do we all need to be available on a specific platform (mattermost users can't DM IRC users)
[00:01] <sgp_> also, using services like Twitter, Reddit, Blockfolio
[00:01] <needmonero90> I'm generally available. My ringer is generally on even when I'm asleep, so I can resoond when stuff happens
[00:01] <needmonero90> should consider getting paid for this availability
[00:01] <sgp_> we took too long this time to get the website notification up and the monero-announce mailing list email out
[00:01] <M5M400> yes, the website should be a priority
[00:02] <asymptotically> !tip needmonero90 0.001
[00:02] <tippero> asymptotically has tipped needmonero90 1 millinero (0.001 Monero)
[00:02] <binaryFate> internal communication between community members to deal with issue was very efficient I found
[00:02] <sgp_> are there other platforms we forgot about this time? ones we felt were mostly a hassle and not very beneficial?
[00:02] <xmrscott[m]> Where was the roadblock though in getting the site annoucement up
[00:02] <M5M400> it's traditionally generally slacking, but in this case updates need to be of high priority
[00:02] <needmonero90> Your generosity will not be forgotten
[00:03] <xmrscott[m]> Was it in getting approval after erc drafted it?
[00:03] <xmrscott[m]> etc
[00:04] <binaryFate> we'd need a website specific timeline of events
[00:04] <xmrscott[m]> Exactly
[00:04] <sgp_> can we build in notification systems with Cake Wallet, Monerujo, etc?
[00:04] <xmrscott[m]> (Which may be best done after the meeting)
[00:05] <needmonero90> I think we just blanked on updating the site
[00:05] <needmonero90> It was an oversight
[00:06] <needmonero90> Once we were clued in it was updated fairly quickly
[00:06] <sgp_> indeed, which is why the process is important. it gives us a checklist to help us remember
[00:06] <asymptotically> sgp_: bitcoin-qt used to have a built in notification system, but it kind of sucked and got removed
[00:06] <M5M400> sgp_: like a emergency broadcast system that pushes out to multiple outlets with minimal effort?
[00:06] <anhdres2> sgp_ I don't see how unless it adds a centralized element.
[00:06] <cbster> I think built-in notification systems would be smart, but their use would be limited as those affected are probably not using them (they downloaded the core wallet)
[00:07] <xmrscott[m]> Built in notifications introduce a point of attack
[00:07] <M5M400> yeah. super amplified FUD
[00:07] <cbster> If the binaries are comprised for that, I'd be unsure of its reliability to relay notifications
[00:07] <PlasmaPower> Bitcoin's now retired system: https://en.bitcoin.it/wiki/Alert_system
Alert system
[00:07] <sgp_> PlasmaPower: thanks for the reference
[00:07] <xmrscott[m]> Hey, wallet is compromised, download at this new (malicious) website
[00:08] <PlasmaPower> cbster: yeah, though for e.g. an active linking attack it could be helpful
[00:08] <cbster> I think you're right, could prove more troublesome than what it solves
[00:09] <sgp_> ok, no additional platforms coming up. keep thinking about better ways to reach people
[00:09] <sgp_> *coming to mind
[00:10] <sgp_> d. incident response
[00:10] <M5M400> I'd like to throw the mailinglist in the ring. who's got access to post there besides the big fluff?
[00:10] <sgp_> M5M400: good q> I don't know
[00:10] <binaryFate> everyone can post, but emails are approved on a case basis (pigeon and maybe fluffy too)
[00:11] <M5M400> maybe take a note for later. I think it is a good medium, but worthless when notifications get sent out a day or two late
[00:11] <binaryFate> in this case there was a misunderstanding between fluffy and myself. He thought I would send email, I thought he would
[00:11] <binaryFate> (I did not have access to my PGP key in time)
[00:12] <M5M400> fair enough
[00:12] <sgp_> an example of the communication process helping in that case could be specifically assigning tasks to people
[00:12] <PlasmaPower> is there any generally applicable "incident response" besides communication?
[00:13] <sgp_> PlasmaPower: nice segway, thanks
[00:13] <sgp_> an example of an incident response process, though extreme, could be something like getting the opinion and help of an independent firm
[00:14] <M5M400> sgp_: that's not extreme. it's common practice to have security incidents assessed by independent parties to minimize the risk of compromized entities being part of the investigation
[00:15] <sgp_> right, so how do we do that without writing a $10m check to Deloitte?
[00:15] <M5M400> hence my question earlier if the people disecting the box also had access at the time of breach
[00:15] <asymptotically> write me a $9m check instead
[00:16] <needmonero90> I'll do it for $8m
[00:16] <M5M400> sgp_: that's the $8m question
[00:07] <cbster> If the binaries are comprised for that, I'd be unsure of its reliability to relay notifications
[00:07] <PlasmaPower> Bitcoin's now retired system: https://en.bitcoin.it/wiki/Alert_system
Alert system
[00:07] <sgp_> PlasmaPower: thanks for the reference
[00:07] <xmrscott[m]> Hey, wallet is compromised, download at this new (malicious) website
[00:08] <PlasmaPower> cbster: yeah, though for e.g. an active linking attack it could be helpful
[00:08] <cbster> I think you're right, could prove more troublesome than what it solves
[00:09] <sgp_> ok, no additional platforms coming up. keep thinking about better ways to reach people
[00:09] <sgp_> *coming to mind
[00:10] <sgp_> d. incident response
[00:10] <M5M400> I'd like to throw the mailinglist in the ring. who's got access to post there besides the big fluff?
[00:10] <sgp_> M5M400: good q> I don't know
[00:10] <binaryFate> everyone can post, but emails are approved on a case basis (pigeon and maybe fluffy too)
[00:11] <M5M400> maybe take a note for later. I think it is a good medium, but worthless when notifications get sent out a day or two late
[00:11] <binaryFate> in this case there was a misunderstanding between fluffy and myself. He thought I would send email, I thought he would
[00:11] <binaryFate> (I did not have access to my PGP key in time)
[00:12] <M5M400> fair enough
[00:12] <sgp_> an example of the communication process helping in that case could be specifically assigning tasks to people
[00:12] <PlasmaPower> is there any generally applicable "incident response" besides communication?
[00:13] <sgp_> PlasmaPower: nice segway, thanks
[00:13] <sgp_> an example of an incident response process, though extreme, could be something like getting the opinion and help of an independent firm
[00:14] <M5M400> sgp_: that's not extreme. it's common practice to have security incidents assessed by independent parties to minimize the risk of compromized entities being part of the investigation
[00:15] <sgp_> right, so how do we do that without writing a $10m check to Deloitte?
[00:15] <M5M400> hence my question earlier if the people disecting the box also had access at the time of breach
[00:15] <asymptotically> write me a $9m check instead
[00:16] <needmonero90> I'll do it for $8m
[00:16] <M5M400> sgp_: that's the $8m question
[00:16] <PlasmaPower> I definitely agree that's a good step when a server is compromised. Would it also be applicable to e.g. an RCE in the protocol? I'm not sure how useful an investigation would be there, besides a git blame.
[00:16] <needmonero90> And by do it I mean delegate
[00:16] <binaryFate> I don't see that as possible or useful in an emergency situation. Maybe for investigations later. No firm will be hired (with what funds?), get to the case and help us in a couple hours
[00:16] <PlasmaPower> true
[00:16] <sgp_> binaryFate: right, which is why I'm looking for realistic procedures
[00:17] <binaryFate> Since we are not a company and we do not have people around the clock 24/7, I think we should realistically focus on procedures indeed. Not even assigned them strictly so we do not have bottleneck if someone is afk
[00:17] <M5M400> sgp_: community internal segregation of duties would be a start
[00:18] <sgp_> M5M400: can you elaborate a bit more?
[00:19] <M5M400> seperate publishing teams and forensic teams
[00:20] <binaryFate> Maping the current capabilities (mostly website update) would be good too. What processes are required for each steps and who has the permissions currently to do them?
[00:20] <sgp_> binaryFate: good one
[00:20] <sgp_> basic access control stuff
[00:20] <PlasmaPower> though probably keep that documentation internal
[00:20] <M5M400> not sure how it's organized right now, so can't elaborate in detail. but from previous conversations it seems that it's not even totally clear who even had access to the comped box. (probably multiple people)
[00:20] <PlasmaPower> you don't want to provide attackers with a guide of who to attack
[00:21] <M5M400> PlasmaPower: internal is a pretty fuzzy thing... where do you draw the line in the circle of trust an opensource project?
[00:21] <M5M400> anyone in here could be a potential attacker
[00:21] <sgp_> M5M400: I agree in this case it's pretty industry-standard to have some discussions like this kept in the dl
[00:22] <PlasmaPower> M5M400: it's going to be somewhat arbitrary of course, and IDK how the Monero team is currently organized, but whoever has access to the GitHub is a good place to start.
[00:23] <sgp_> any other incident response comments? we will need to revisit this much more later
[00:24] <sgp_> e. regular tests/audits
[00:24] <sgp_> ideally, we will assess the existing processes and suggest improvements. then we can test them to see how effective these processes are
[00:24] <sgp_> that's why schools have fire drills
[00:25] <binaryFate> I want to highlight that people that trust each other getting on an IRC channel to discuss the situation at hand remains by far the most efficient decision process. I find it more important to remove potential bottlenecks in terms of who can do what, than to try to guide too much said decision process.
[00:25] <binaryFate> Have to go now, thanks everyone, thanks sgp_ for meeting
[00:25] <sgp_> binaryFate: thanks for coming
[00:26] <M5M400> +1 on the removing bottlenecks thing
[00:26] <M5M400> cu
[00:26] <sgp_> ideally this would be its own workgroup, but I also don't know how realistic this is
[00:27] <sgp_> ok, people are pretty quiet on this one. we can keep going
[00:27] <sgp_> f. responsible roles, including alternates
[00:28] <sgp_> it's an open-source project without people getting paid for things, so people will be asleep, on vacation, etc
[00:28] <M5M400> regarding fire drills... we could regularly publish emergency broadcast test posts on the outlets and have people go to a website, click on a button or something to assess message reception depth
[00:28] <sgp_> it's important imo to have a list of primary and secondary contacts
[00:28] <M5M400> sorry, I'm slow. it's late.
[00:28] <needmonero90> One solution is to create a hired role for this.
[00:28] <needmonero90> puts his name into the hat
[00:28] <sgp_> needmonero90: I'll give you $1
[00:29] <needmonero90> :thinking:
[00:30] <needmonero90> I can do a writeup of role requirements later
[00:30] <sgp_> that would be very beneficial
[00:30] <sgp_> eg: Justin is the primary for Blockfolio, secondary for Twitter, etc
[00:31] <sgp_> any other ideas? we're getting close to finishing this long meeting
[00:31] <M5M400> would those roles be published somewhere?
[00:32] <sgp_> M5M400: I recommend they're only given to trusted people
[00:32] <sgp_> give people only what they need to see
[00:33] <sgp_> g. missed topics and frameworks
[00:33] <sgp_> If you have any topics you feel were not covered or some other better framework to consider going forward, please mention these now for discussion.
[00:33] <M5M400> <void>
[00:33] <ArticMine> I would raise the question of post incident hardening
[00:33] <M5M400> good one
[00:34] <asymptotically> is there a post mortem of how the bad wallet binary actually ended up on the site? or is that not known yet
[00:34] <M5M400> but probably needs the forensics to complete first
[00:34] <asymptotically> ok nvm that answered my question :p
[00:35] <M5M400> though it begs the question what makes the DR host more secure than the comped box at this point in time
[00:35] <needmonero90> Nothing left on my end
[00:35] <ArticMine> Yes that is the case, but for example hardening the the binary verification process
[00:36] <ArticMine> Such as rehrar suggested but going further
[00:37] <ArticMine> binary verification for android
[00:37] <ArticMine> Free BSD etc
[00:39] <M5M400> still awake - but I can't contribute to this
[00:40] <sgp_> ArticMine: I don't have anything to add here, but I'll note the process
[00:40] <sgp_> Any final thoughts?
[00:41] <sgp_> 4. Action items
[00:41] <sgp_> I will compile the recommendations in 3 into a document and share the initial draft version
[00:41] <sgp_> Once shared, please comment on the draft
[00:41] <sgp_> Please think about specific roles you would feel comfortable filling, even in a backup role
[00:42] <sgp_> rehrar named an action item 1000 years ago when the meeting started but I forget what it was
[00:42] <sgp_> then there's the action item of identifying who has access to what parts of the server (or making sure the core team has that info already)
[00:42] <sgp_> Anything else?
[00:42] <ArticMine> It was about improving the guides for binary verification
[00:43] <ArticMine> Making them easier to understand for users
[00:43]  <rehrar> Goodness! This is still going?
[00:43] <sgp_> ok, add that :)
[00:43] <sgp_> very nearly done rehrar, we were very productive
[00:43] <xmrscott[m]> Write up website notification timeline to figure out what the major contributors were ro thevdelay
[00:43] <asymptotically> maybe openbsd signify would be easier than a pgp signed shasums file?
[00:43] <sgp_> xmrscott[m]: good, have a timeline so we can see what took the longest
[00:44] <sgp_> last chance to say something
[00:44] <sgp_> 5. Conclusion
[00:45] <sgp_> Thank you for participating in this extremely important discussion for Monero
[00:45] <almutasim> Thank you.
[00:45] <M5M400> thx
[00:45] <sgp_> I was extremely pleased at the dedication for this emergency response, and with some organization, I think we can set a gold standard for other projects to follow
[00:45] <sgp_> See you all later :)
```

## fluffypony | 2019-11-26T08:51:53+00:00
@sanecito here's my log, times are SAST (UTC +2) -

- FIM was killed around 6:06pm. Technically, it’s last log entry was 6:06pm, so it may have only been killed a few mins thereafter.
-  GitHub issue was 6:21pm
- selsta reported it to me out-of-band at 6:30pm (I hadn't seen the GitHub issue)
- Failover to the DR box was at 6:40pm, when the downloads box was disconnected from the internet and isolated for auditing

## nikitasius | 2019-12-05T13:55:58+00:00
@sanecito sadly, 20 minutes folks speak about the hack and the rest about hash verification and alerts.

1st step to understand whats happened is to check if you was up to date and which versions you had on your server (for all services).

# Action History
- Created by: SamsungGalaxyPlayer | 2019-11-19T18:14:55+00:00
- Closed at: 2019-12-06T19:57:40+00:00
