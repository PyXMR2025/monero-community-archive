---
title: CCS Wallet Incident
source_url: https://github.com/monero-project/meta/issues/916
author: luigi1111
assignees: []
labels: []
created_at: '2023-11-02T15:57:53+00:00'
updated_at: '2026-04-17T02:53:42+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The CCS Wallet was drained of 2,675.73 XMR (the entire balance) on September 1, 2023, just before midnight. A second, hot wallet, used for payments to contributors, is untouched; its balance is ~244 XMR. We have thus far not been able to ascertain the source of the breach.

Timeline

- April 12, 2020: New CCS wallet is created by fluffypony (on a dedicated wallet laptop, a Purism Librem 14, running Qubes) and the seed shared with Luigi, half via the Wire app, and half via GPG-encrypted email -- fluffypony and Luigi are the only parties with known access to the CCS seed.
- 2020-2023: (Luigi's side) a single use Ubuntu system is set up to run a Monero node and CCS wallet; the hot wallet is on a Windows 10 Pro desktop where it has been since 2017; Luigi makes payments from the hot wallet and tops it up from the CCS Wallet (via SSH), occasionally as needed.
- August 3, 2021: shortly after fluffypony's arrest, most of the CCS wallet was swept by Luigi to the hot wallet as a short-term measure pending more information about the nature of the arrest
- (a few weeks/months later) fluffypony's arrest is determined not crypto-related; reverted to previous behavior of large CCS balance, small hot wallet balance
- May 10, 2023: last transfer was made by Luigi from CCS wallet to hot wallet
- September 1 11:58pm - September 2 12:07am, 2023: CCS wallet was swept in 9 transactions, IDs:
ffc82e64dde43d3939354ca1445d41278aef0b80a7d16d7ca12ab9a88f5bc56a
08487d5dbf53dfb60008f6783d2784bc4c3b33e1a7db43356a0f61fb27ab90cc
4b73bd9731f6e188c6fcebed91cc1eb25d2a96d183037c3e4b46e83dbf1868a9
8a5ed5483b5746bd0fa0bc4b7c4605dda1a3643e8bb9144c3f37eb13d46c1441
56dd063f42775600adf03ae1e7d7376813d9640c65f08916e3802dbfee489e2c
e2ab762927637fe0255246f8795a02bd7bb99f905ae7afc21284e6ff9e7f73db
9bf312ed09da1e7dfce281a76ae2fc5b7b9edc35d31c9eb46b21d38500716b6b
837de977651136c18b0018269626be7155d477cc731c5ca907608a2db57ff6a8
9c278d1496788aee6c7f26556a3f6f2cbb7e109cd20400e0b2381f6c2d4e29f4
(wallet was then empty)
- September 2023: donations come in for Lovera CCS (the only proposal that was in Funding Required)
- September 28, 2023: Luigi logs into CCS wallet to top up hot wallet, finding (after syncing from May 10th as expected) a balance of ~4.6 XMR, representing September donations for Lovera; no additional transfers occurred after September 2
- September 28, 2023 (a few hours later): Luigi has call with binaryFate on what has been discovered; General Fund is confirmed to be intact. Shortly after, Luigi, binaryFate, and fluffypony have a call discussing the situation.
- September 28 - now: Core Team discusses internally; Luigi and fluffypony forensic efforts -- unfortunately, to date, no evidence of breach has been identified

Open questions:

- How do we achieve CCS continuity for existing contributors? Core team is in favor of covering existing liabilities from the General Fund.
- How do we structure the CCS going forward?
- How did the breach occur?

# Discussion History
## fluffypony | 2023-11-02T17:17:04+00:00
Just to add to this, it's entirely possible that it's related to the ongoing attacks that we've seen since April, as they include a variety of compromised keys (including Bitcoin wallet.dats, seeds generated with all manner of hardware and software, Ethereum pre-sale wallets, etc.) and include XMR that's been swept. See [tayvano's thread here](https://twitter.com/tayvano_/status/1696222660013998407). That hack recently started seeing some more sweeps happen (and they can tell that it's from the same hack since the surveillance-chain sweeps go to the same cluster of addresses).

It's entirely possible that other wallets are at risk, which is why luigi1111 and binaryfate have taken additional precautions. I no longer have access to any of these wallets (although I do have large corp / treasury wallets on that laptop that pre-date Monero hardware wallet support and remain untouched), but I've taken similar precautions.

## fluffypony | 2023-11-02T17:22:23+00:00
It's also possible that the attacker isn't aware of what they've stolen, in which case I'd ask them to consider that they have stolen funds that are donated by individuals against specific things that Monero contributors are working on. This attack is unconscionable, as they've taken funds that a contributor might be relying on to pay their rent or buy food. I'd urge them to take action to make this right if they become aware of this😞

## detherminal | 2023-11-02T17:43:49+00:00
Shit, thats hard. We've stumbled upon one of the few bad things about crypto that it is irreversible. I can't think of anything other than replacing from the general fund. Also we should use open source hardware wallets like MoneroSigner from now on imo.

## lazios | 2023-11-02T17:50:00+00:00
"Luigi makes payments from the hot wallet and tops it up from the CCS Wallet (via SSH), occasionally as needed." Does this mean that the private keys for the CSS wallet were on an online Ubuntu server? If yes, thats where the compromise happened imo.


## johnalanwoods | 2023-11-02T17:54:51+00:00
What’s the balance of the general fund, will replenishing the CCS impact protocol development?

## jeffro256 | 2023-11-02T17:57:34+00:00
Thank you for the transparency and closure about this issue.

> shortly after fluffypony's arrest, most of the CCS wallet was swept by Luigi to the hot wallet as a short-term measure pending more information about the nature of the arrest

So to clarify, @fluffypony never had access to the private keys to the hot wallet, but did have the private keys to the main CCS wallet post-arrest?

Would the public be able to get transaction proofs (with addresses) to all nine of those transactions? If the hack was non-targeted, there's a good chance that the receive address gets re-used in someone else's hack, which would help us find the perpetrator.

Going forward, I think that this scenario is an excellent exhibit on why the CCS should use multisig (at least for the main wallet).




## serhack | 2023-11-02T18:06:41+00:00
So sad to learn about this, please let me know if you need any help for the forensic part. 

## fluffypony | 2023-11-02T18:25:55+00:00
> So to clarify, @fluffypony never had access to the private keys to the hot wallet, but did have the private keys to the main CCS wallet post-arrest?

Yes, as well as keys to the Bitcoin donation wallet, previous Monero GF wallet, etc. Post my release I nuked everything that could potentially be problematic as I was unsure as to what might happen next, and didn't want to put anything at risk.

> Would the public be able to get transaction proofs (with addresses) to all nine of those transactions? If the hack was non-targeted, there's a good chance that the receive address gets re-used in someone else's hack, which would help us find the perpetrator.

I'm sure @luigi1111 can do that.

> Going forward, I think that this scenario is an excellent exhibit on why the CCS should use multisig (at least for the main wallet).

Yes definitely; multisig was not ready for this prior, but now it is.

## selsta | 2023-11-02T18:26:12+00:00
@johnalanwoods  General fund is around 8k.

> will replenishing the CCS impact protocol development?

No, the general fund isn't usually used for funding active development but more for emergencies like this and other unexpected expenses.

## SamsungGalaxyPlayer | 2023-11-02T18:29:15+00:00
![picture](https://github.com/monero-project/meta/assets/12520755/190058e3-10da-45aa-b58f-29bef4c31a0d)

There's a clear suspect: https://xmrchain.net/tx/bb77d03cae08942f43cccd759ade505a1c9435470a4a2cabfa5e26d2c93d1a58

## ridolfox | 2023-11-02T18:43:34+00:00
> Just to add to this, it's entirely possible that it's related to the ongoing attacks that we've seen since April, as they include a variety of compromised keys (including Bitcoin wallet.dats, seeds generated with all manner of hardware and software, Ethereum pre-sale wallets, etc.) and include XMR that's been swept. See [tayvano's thread here](https://twitter.com/tayvano_/status/1696222660013998407). That hack recently started seeing some more sweeps happen (and they can tell that it's from the same hack since the surveillance-chain sweeps go to the same cluster of addresses).
> 
> It's entirely possible that other wallets are at risk, which is why luigi1111 and binaryfate have taken additional precautions. I no longer have access to any of these wallets (although I do have large corp / treasury wallets on that laptop that pre-date Monero hardware wallet support and remain untouched), but I've taken similar precautions.

The hacks you mentioned @fluffypony were determined to be related to LastPass. This seems to be something different... 



## fluffypony | 2023-11-02T18:50:00+00:00
> The hacks you mentioned @fluffypony were determined to be related to LastPass. This seems to be something different...

A large number of them were, but there are a whole screed of sweeps from users that have never even downloaded LastPass.

## scottAnselmo | 2023-11-02T18:53:28+00:00
"The CCS Wallet was drained of 2,675.73 XMR (the entire balance) on September 1, 2023, just before midnight." Is this midnight UTC or another timezone? If UTC we can assign it low probability to be the same attacker referenced in tayvano's thread:

> Primary theft txns are almost always between 10am–4pm UTC

I'm guessing Core is already looking into hiring professional digital forensics specialists, but this could help with prioritizing what data to collect now that might still be around: https://owasp.org/www-pdf-archive//NetSecurity-RespondingToTheDigitalCrimeScene-GatheringVolatileData-TechnoForensics-102908.pdf

## jeffro256 | 2023-11-02T19:06:10+00:00
Maybe I'm not understanding correctly, but aren't both of @luigi1111 wallets, Ubuntu and Windows, "hot" wallets? Both reside on machines connected to the internet with no hardware devices. Both had their respective spendkeys on them, yeah?

> Luigi makes payments from the hot wallet and tops it up from the CCS Wallet (via SSH), occasionally as needed

How was this performed? Did the Windows computer SSH into the Ubuntu computer, or vice versa? 

Was the node that the Ubuntu wallet ran on a pruned node or full node?

## hinto-janai | 2023-11-02T19:08:54+00:00
### CCS Wallet Opsec 2.0

- Seed should be generated on the "offline" device
- Only the wallets view key is given to "hot" devices - such that they can generate & broadcast transactions but not sign them
- Wallets are password-protected and/or machines are at-rest encrypted for physical security
- Seed is shared only in encrypted form, and this wallet setup **must** replicated by whomever holds a copy of the spend key
- Key images and outputs are transferred in the same way as transactions

<img src="https://github.com/monero-project/meta/assets/101352116/895da54c-ea5a-4f34-94ae-38808be6fca3" width="40%"/>

---

The offline computer could be a scrappy $200 notebook, what's important is that it is offline forever.

There is a burden when moving funds like this, but then again - this is a large amount of community funds.

Having more "hot" buffers would spread out risk as well, and would speed up the payout latency for contributors, e.g, @plowsof could be given enough funds to pay out soon-to-be-finished CCS's (assuming he doesn't vanish)

> Core team is in favor of covering existing liabilities from the General Fund

Now that this is disclosed, current contributors who have been waiting for payment should be paid ASAP :)

## rehrar | 2023-11-02T19:13:43+00:00
> Now that this is disclosed, current contributors who have been waiting for payment should be paid ASAP :)

Core and their helpers have often been trying to pay things out over the years. But a combination of some people being unreachable, refusing payment, or other such circumstances means that funds often sit there. Many times for years. It may be wise to institute a form of expiration policy where unclaimed funds (x months or years after funding/project completion) go into a special "Fund other CCS projects" wallet or something. All of this Monero sitting there years after funding are a liability.

## luigi1111 | 2023-11-02T19:19:45+00:00
> Maybe I'm not understanding correctly, but aren't both of @luigi1111 wallets, Ubuntu and Windows, "hot" wallets? Both reside on machines connected to the internet with no hardware devices. Both had their respective spendkeys on them, yeah?
> 
> > Luigi makes payments from the hot wallet and tops it up from the CCS Wallet (via SSH), occasionally as needed
> 
> How was this performed? Did the Windows computer SSH into the Ubuntu computer, or vice versa?
> 
> Was the node that the Ubuntu wallet ran on a pruned node or full node?

Windows -> Ubuntu, once every 3 months or so. Full node.

## marcovelon | 2023-11-02T19:30:00+00:00
> Windows -> Ubuntu, once every 3 months or so. Full node.

> "Luigi makes payments from the hot wallet and tops it up from the CCS Wallet (via SSH), occasionally as needed." Does this mean that the private keys for the CSS wallet were on an online Ubuntu server? If yes, thats where the compromise happened imo.

I am of the same opinion. All Tayvano's "OG" friends were also Windows users and considering the amount of well done and undetectable malware existing for that OS, I wouldn't be surprised if Luigi's Windows machine was already part of some undetected botnet and its operators performed this attack via SSH session details on that machine (by either stealing the SSH key or live using trojan's remote desktop control capability while the victim was unaware). Compromised developers Windows machines resulting into big corporate breaches is not something uncommon.

A first step to investigate this is to log that machine's network traffic on the router that connects it to the Internet. A log time should be at least 48 hours (but more = better) with any software using network switched off to maximize the log's quality by reducing the noise to the possible minimum. Backdoors existing today are capable of being very low profile in terms of networking and detecting them isn't easy, therefore it will require some time and patience.

This is the only possible realistic attack vector in this case, given that the timeline provided in the OP doesn't omit some more important information.

P.S. beware that chances to discover the malware are 50/50, given that the attacker may track all the public communications related to this event including reading this thread, who could decide to detach/deactivate the backdoor to clear the evidence and avoid its disclosure. So consider making a full disk dump of that machine as well.

P.P.S. stop using Windows for such projects.

## SamsungGalaxyPlayer | 2023-11-02T19:47:36+00:00
![picture](https://github.com/monero-project/meta/assets/12520755/60b7c63d-79d4-4fe9-9931-322b3be0c12b)

The attacker likely consolidated the funds again in these two transactions. Exchanges and services should check to see if they received these XMR deposits.

https://xmrchain.net/tx/2c5b45bf398dcae482019a46fb2d06d334bf4260484dc4857fc35db3689ad5ec

https://xmrchain.net/tx/06550272cdfa1eea98d288b2d57c272b5c52a2b195b4f808c8c03422a58ca47b

## MrCyjaneK | 2023-11-02T20:16:36+00:00
I think that nobody asked that before, @luigi1111 I have few questions about the Ubuntu server
 - Was it running at your place (i.e. phisical device you had access to that was being turned on when needed (especially: was offline during the 'Incident'))
 - If not, was it a dedicated cloud server or a KVM/OpenVZ/other VPS (if possible, tell us who was the cloud provider)?
 - Which version of Ubuntu was it running at the time of Incident?
 - Was the Ubuntu server accessed via SSH password authentication or key?
 - Lastly, not a question - but if you have logs of any kinds (maybe logs in backups), try securing them, if it was a cloud server download oldest possible backup(s), and grab copy of all server logs. 


p.s. @SamsungGalaxyPlayer are you tracking monero 😕?

## luigi1111 | 2023-11-02T21:26:11+00:00
> I think that nobody asked that before, @luigi1111 I have few questions about the Ubuntu server
> 
> * Was it running at your place (i.e. phisical device you had access to that was being turned on when needed (especially: was offline during the 'Incident'))
> * If not, was it a dedicated cloud server or a KVM/OpenVZ/other VPS (if possible, tell us who was the cloud provider)?
> * Which version of Ubuntu was it running at the time of Incident?
> * Was the Ubuntu server accessed via SSH password authentication or key?
> * Lastly, not a question - but if you have logs of any kinds (maybe logs in backups), try securing them, if it was a cloud server download oldest possible backup(s), and grab copy of all server logs.
> 
> p.s. @SamsungGalaxyPlayer are you tracking monero 😕?

- It was running at my place.
- n/a
- 20.04
- Password

## tuxpizza | 2023-11-02T21:54:04+00:00
> P.P.S. stop using Windows for such projects.

If you are truly concerned about malware, simply switching to Linux isn't a great answer. Default Linux installations are not that great for security and not very hardened. You need a hardened system, preferably an immutable OS that has the root partition as read-only, IE Fedora Silverblue or any other OSTree based systems. Use https://cisofy.com/lynis/ to see any potential unnecessary security issues and things that weren't being used that can be turned off. Setup automatic updates. Only use Wayland, as X11 is easy to keylog. Use keys for SSH, not passwords. Or better yet SSH turned off. If you need to access it do it physically.

Same thing goes for the CCS node/wallet server. Using UEFI Secure Boot, LUKS encrypted main, root, and GRUB partition. Wanna get crazy you can do coreboot with heads on some specific systems that support it. Don't use LTS kernels, use the latest one with grsecurity patches. Just suggestions.

Also a given, these two devices should be VLAN'd from the rest of the network if not already.

@hinto-janai 's model would already greatly improve what already exists, offline signing would take so many potential attack vectors away.


Also secure the network if not already. Run an OPNSense firewall to VLAN and make sure no unnecessary ports are open. Use an OpenWRT router if you need wireless. Countless shitty consumer routers don't get updated ever, and many of them have severe vulnerabilities that don't get patched for a really long time.

## marcovelon | 2023-11-02T22:12:22+00:00
> > P.P.S. stop using Windows for such projects.
> 
> If you are truly concerned about malware, simply switching to Linux isn't a great answer. Default Linux installations are not that great for security and not very hardened. 

I didn't say one should use a default Linux installation. What you said should be already obvious to people with such responsibilities. What's surprising is that this is being explained to people from Monero team.

## MrCyjaneK | 2023-11-02T22:16:48+00:00
> I didn't say one should use a default Linux installation. What you said should be already obvious to people with such responsibility.

Fluffy's setup was much better..

@luigi1111
> It was running at my place.
Was it exposed to the public internet in any way, other than your laptop or only available via LAN?

I think that this may be the most likely cause of the incident, I doubt someone 'guessed' the seed right.



## marcovelon | 2023-11-02T22:30:18+00:00
> Fluffy's setup was much better..

Yeah it corresponds to the industry standard where the threat agent is LE. 

## tuxpizza | 2023-11-02T22:32:57+00:00
 > I didn't say one should use a default Linux installation. What you said should be already obvious to people with such responsibilities.

Given that Windows was being used these things probably aren't obvious. Most people are not very knowledgeable on the inherent security issues with desktop operating systems, or basic hardening.

## tayvano | 2023-11-02T23:38:24+00:00
I'm not 100% caught up on this thread yet (just getting back home) but here's some more specific details on the threat actors ive been chasing for a good while now:

typically operate 1200 utc - 2300 utc, though all hours have been observed. least amt of activity 300-1000 utc

observations we have on them for the time period mentioneed by op:

2023-Aug-30 21:50
2023-Aug-31 13:09
2023-Aug-31 18:29
2023-Aug-31 18:31
2023-Aug-31 20:13
2023-Sep-03 12:31
2023-Sep-03 12:32
2023-Sep-03 12:35

for those above timestamps, all activity was via

2a00:1650:0:3:45::1

2001:ac8:23:3c:2d4::1

Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36

These are either HideMe VPN or residential proxies (5socks etc), as is usual for these actors.

Victims have all sorts of devices. The only real thruline is the age of keys (created prior to 2022, some keys date back as far as 2012) and everyone we have talked to has used lastpass, most have confirmed the specific keys/seeds that were compromised were in lastpass, usually a secure note, at some point. most are longtime lastpass users but a few only used last past for a short period of time. those users confirmed the specific compromised keys were in lastpass.

fwiw, these actors even push stolen XMR to BTC—we have observed them consolidating a victim's eth, btc, xmr to a btc address before pushing to wasabi/sinbad/cryptomixer/coinomize/etc. they use instaswappers to do so e.g. fixedfloat, simpleswap, sideshift, etc. The size of this theft should make the funds easily findable in the outgoing transactions from the hot wallets of those instaswappers on BTC **if it is in fact these same threat actors.**

The first thing I would ask is if anyone who's ever had access to the keys that were compromised here has had other wallets drained in the last ~year. **Even if the amt stolen from those wallets was small / dust.** That will help determine source of compromise faster than anything else tbh.

## BawdyAnarchist | 2023-11-03T00:52:26+00:00
I can't understand why on Earth you would use less secure system (the Windows hot wallet) to SSH into the what is supposed to be the more secure system (Ubuntu). With a password no less.

Neither do I understand why you would choose Windows or Ubuntu for either operation in the first place. If you're not an expert at sysadmin and security, then you should be using Qubes for this amount of funds, and/or offline key storage.

## elibroftw | 2023-11-03T01:56:04+00:00
> I am of the same opinion. All Tayvano's "OG" friends were also Windows users 

@marcovelon You know, I'd really like to see some citations in a thread about cybersecurity when even Tayvano said all sorts of devices. 

My questions for Luigi and Fluffy Pony are:

- Where all has the CCS seed been stored (who, device, app, file format)? e.g. Windows/ubuntu, Password managers, text files, etc.
    - Also, If the Ubuntu server storage got shot one day, how would you restore the CCS wallet?
    - Does fluffypony have the means to restore the wallet himself (as in could a hack on him lead to wallet drain)?

## luigi1111 | 2023-11-03T02:04:21+00:00
> > I am of the same opinion. All Tayvano's "OG" friends were also Windows users
> 
> @marcovelon You know, I'd really like to see some citations in a thread about cybersecurity when even Tayvano said all sorts of devices.
> 
> My questions for Luigi and Fluffy Pony are:
> 
> * Where all has the CCS seed been stored (device, app, file format)? e.g. Windows/ubuntu, Password managers, text files, etc.
>   
>   * Also, If the Ubuntu server storage got shot one day, how would you restore the CCS wallet?

Seed was only on paper on my end.

## Monero-HackerIndustrial | 2023-11-03T03:52:38+00:00
>Windows -> Ubuntu, once every 3 months or so. Full node.
I think the most plausible route for an attacker is to compromise the windows machine then move laterally to the ubuntu host. With an installed agent on windows an attacker can proxy the traffic and piggy back an existing ssh session or just open one in the background using the compromised password. (You don't even need a kelogger but should be able to dump creds from mem). Once on the host either steal the keys or install an agent on the ubuntu host since it has internet connectivity. (Once keys are stolen the agent is just there for persistence) 

>P.S. beware that chances to discover the malware are 50/50, given that the attacker may track all the public communications related to this event including reading this thread, who could decide to detach/deactivate the backdoor to clear the evidence and avoid its disclosure. So consider making a full disk dump of that machine as well.

There is in memory only malware for windows too. I suggest DD the Ubuntu host and also imaging the windows one if possible. You can dump the memory on it but that was a long time ago so the best bet is on some persistence. 

For the windows host I would hope to examine what network traffic it is connecting to. With remote agents you usually want to make them look like http traffic. So if all programs are down examine what connections are being made to ips or domain names on that box. Keep in mind attackers can domain front trusted cloud domains or use known services such as gsuite, dropbox, slack etc for evading traffic. 


- For the ubuntu box, after imaging a copy with DD (or other imaging software) we can start to examine logs. 
    - SSH logs for auth, any of the system logs for user auth. Check the .ssh/authorized_keys for any backdoored ssh keys. 
- Check to see if any users where added
- Check crontab for any existing tasks that were added. 
- Your bash history is easy to wipe so don't trust it.
- Dump all running processes using ps aux. 


I do have some other questions for the setup:

- Did you use putty or the built in ssh in windows?
- Was the windows machine used for other activities or was it single use as the "hot wallet" 

@tuxpizza has some good recommendations. The network telemetry at a router level would have helped to detect intrusion and the completely airgapped model would have really made it harder for an attacker to steal funds.   I think that using a more "paranoid" model should be followed moving forward. There are a number of very sophisticated threat actors who target crypto teams/groups. They have really good malware and you have to assume they have some browser based 0days at their disposal. 


I really doubt it was some compromise at the initial setup. Many of the crypto focused threat groups target specific high value wallets. There are also the existing botnet operators who can run modules to pillage for crypto/find juicy targets. 




## Monero-HackerIndustrial | 2023-11-03T03:59:44+00:00
@tayvano The actor that you have been following was the same one as the atomic wallet hack right? I know there was a lot more publicity on the eth wallets being drained and there are some reports of btc and other coins, but how common was the compromise of xmr wallets? (From my understanding most of xmr stolen by that group was from atomic wallet). 

I don't know if that actor had any examples of any lateral movement? They appeared to mostly be a group who consolidates stolen keys and is just systematically draining them during those operating times. I don't want to count it out but I don't think it would be the same actor. Unless that actor has moved on to attacking xmr wallets. Which would surprise me in this scenario since while it is a big amount is not a huge wallet compared to other targets in the space. 

## Monero-HackerIndustrial | 2023-11-03T04:03:08+00:00
One last thought. Is there a on going IR process being followed? If you need any help with some basic forensics (outside of the memory dumps) I should be able to help. I am usually on the offensive but have dealt with enough defensive teams to be bale to walk through most of the process. I really think the windows box for sure got popped with malware and the ubuntu box might have some too. 

## BastardiNonCarborundum | 2023-11-03T04:13:22+00:00
Events like this never exist in a vacuum.  Context is everything.  But what is the context?

1 - Cui bono? FluffyPony and luigi1111 will be watched for the rest of their lives by people looking for evidence of extraordinary riches (the impulse to spend rises exponentially as one gets older, except for Nakamoto). I am personally convinced that neither of them are that stupid or ethically compromised. On the other hand, there are two generic parties that stand to gain a lot from a Monero breach - especially a breach of the "heart" of Monero (which shouldn't exist IMO, for this and other reasons) - ie, large corporate or state actors. Which coin is the only one with a public reward by the IRS? That should be your primary focus.

2 - Some have talked about signing offline. They are correct. Some have admonished those same people about the OS and even the physical platform they're signing on. They are also correct. One espoused confidence in UEFI. The first thing I did when I bought an ultrabook with cash at my local retailer in 2013 was disable UEFI. The reason for that is beyond the scope of this post, just do a search.

3 - Paper/stainless steel passwords are ok up to a point, but they're physical (and all that it connotes). Rote learning a 50+ character key, signed off line, is not that difficult. I guess it depends on how serious one takes their responsibility. And of course there is the physical setup - use a TAILS instance (the machine doesn't matter if you have UEFI disabled, at least as far as I know), and sign transactions with your key from memory - the same way Edward Snowden did - with his jacket covering his head and computer. He was NSA. If you think that is comical, you don't belong here.

4 - It's just money. Relax.


## Final-Phoenix | 2023-11-03T08:11:18+00:00
> ### CCS Wallet Opsec 2.0
> * Seed should be generated on the "offline" device
> * Only the wallets view key is given to "hot" devices - such that they can generate & broadcast transactions but not sign them
> * Wallets are password-protected and/or machines are at-rest encrypted for physical security
> * Seed is shared only in encrypted form, and this wallet setup **must** replicated by whomever holds a copy of the spend key
> * Key images and outputs are transferred in the same way as transactions
> 
> <img alt="" width="40%" src="https://user-images.githubusercontent.com/101352116/280089902-895da54c-ea5a-4f34-94ae-38808be6fca3.png">
> The offline computer could be a scrappy $200 notebook, what's important is that it is offline forever.
> 
> There is a burden when moving funds like this, but then again - this is a large amount of community funds.
> 
> Having more "hot" buffers would spread out risk as well, and would speed up the payout latency for contributors, e.g, @plowsof could be given enough funds to pay out soon-to-be-finished CCS's (assuming he doesn't vanish)
> 
> > Core team is in favor of covering existing liabilities from the General Fund
> 
> Now that this is disclosed, current contributors who have been waiting for payment should be paid ASAP :)

Definitely should have always been doing this in the first place, but it still wouldn't change anything if it was an inside job. 

We should figure out a way to decentralize the process and for the community to directly fund these projects, or at the *very least* have some sort of multisig setup.

## erciccione | 2023-11-03T08:19:43+00:00
I see there is a lot of speculation going on, but as long as there are no more details, better wait until we know more. My thoughts on the first two of luigi's questions:

>  How do we achieve CCS continuity for existing contributors? Core team is in favour of covering existing liabilities from the General Fund.

The general fund should be definitely used to cover the payment of ongoing ccs and already approved ccs. This is the "rainy day" kind of situation the general fund exist for.

> How do we structure the CCS going forward?

Every wallet with substantial amount of money managed by the core team should be a multisig wallet. The possibility for single individuals to make transactions from such big wallet will always be a huge vulnerability and in case of breaches, like what we are seeing now, it's inevitable that some in the community will be suspicious of the core team members who had the possibility to transact from that wallet.

This situation seriously impacts short and long term trust in the Monero project and the core team who stewards it, especially since there seems to have been big oversights in the way funds are stored and secured. The sooner things are clarified the better.

We can take advantage of this situation to reconsider the way funds are managed inside the Monero project, which is based on almost complete trust in the core team.

So i throw there another question i think it's very important to answer to:

- How can we improve the way funds are managed so that trust in the "treasurers" is minimized?

## ghost | 2023-11-03T11:10:30+00:00
@SamsungGalaxyPlayer How you were able to track monero?

## ghost | 2023-11-03T11:34:34+00:00
> ### CCS Wallet Opsec 2.0
> * Seed should be generated on the "offline" device
> * Only the wallets view key is given to "hot" devices - such that they can generate & broadcast transactions but not sign them
> * Wallets are password-protected and/or machines are at-rest encrypted for physical security
> * Seed is shared only in encrypted form, and this wallet setup **must** replicated by whomever holds a copy of the spend key
> * Key images and outputs are transferred in the same way as transactions
> 
> <img alt="" width="40%" src="https://user-images.githubusercontent.com/101352116/280089902-895da54c-ea5a-4f34-94ae-38808be6fca3.png">
> The offline computer could be a scrappy $200 notebook, what's important is that it is offline forever.
> 
> There is a burden when moving funds like this, but then again - this is a large amount of community funds.
> 
> Having more "hot" buffers would spread out risk as well, and would speed up the payout latency for contributors, e.g, @plowsof could be given enough funds to pay out soon-to-be-finished CCS's (assuming he doesn't vanish)
> 
> > Core team is in favor of covering existing liabilities from the General Fund
> 
> Now that this is disclosed, current contributors who have been waiting for payment should be paid ASAP :)

using seed encryption (offset) & a cold storage setup with airgapped transactions would have prevented all of this (assuming it was a hack) 

luckily now we have wallets like ANONERO and (soon) Feather Wallet that will make securing such a setup much easier next time

## TheFuzzStone | 2023-11-03T11:40:16+00:00
> * How can we improve the way funds are managed so that trust in the "treasurers" is minimized?

Multisig.

---

Maybe someone will not like this level of nerdiness, but I see the situation this way.

A multisig wallet is created with for example with 5 cosigners, and 2 cosigners are required to spend.

The number of cosigners - let the Monero community decide, as well as the Core team amongst themselves, as different people are online with different frequency, and if you reduce the number of cosigners too much, you may end up with a situation where the right number of cosigners are unavailable to spend funds from the wallet.

Each of the 5 cosigners must have a GPG key, and sign the necessary public keys from the Multisig wallet (and upload them to Github/-Lab) for future verification of which key was involved in each spend from the main wallet.

All cosigners (in this example there are 5 of them) should be able to communicate with each other, and definitely not through a proprietary crap like Wire App, where half of the mnemonic phrase has already been covered (I recommend you **NOT** to use this mnemonic phrase anymore). Create a chat room in [SimpleX.chat](https://simplex.chat/) for only `number-of-cosigners` cosigners.

When the need to spend money comes, then 1 of 5 cosigners writes in the chat: "_We need to send n XMR for such and such expenses_", let's say `cosigner_2` will be the initiator (simply because he is more often online than the others, and more monitors the situation within the Monero community), and `cosigner_4` responds to him in this chat, that he is online also, and is ready to sign this spend from his side.

Let me remind you that all this happens in private chat only for the cosigners of this wallet.

Other cosigners (`cosigner_1`, `cosigner_3`, `cosigner_5`) see that `cosigner_2` and `cosigner_4` have everything under control, and if they are satisfied with everything, they can simply ignore and `cosigner_2` and `cosigner_4` will send the right amount of XMR to the right place, and due to the fact that the necessary public keys were signed with their GPG-keys and posted publicly - anyone can check who exactly from cosigners took part in the spending of each transaction from this Multisig wallet.

This is just my idea. It is not necessary to take exactly 5 cosigners and it is not necessary to create a wallet that requires only 2 signatures. There needs to be a balance between convenience/efficiency and security, because in the end it can end badly. 

If you want "democracy"? Create a Multisig wallet with 10 cosigners and where you need 6 signatures to spend. Only question is, how efficient will it be?

## spirobel | 2023-11-03T13:14:13+00:00
lets shut the CCS down and support developers directly. You guys have failed. 
(Or you stole the money. There is no way to tell.)

## shortwavesurfer2009 | 2023-11-03T13:20:56+00:00
I don't actually feel like they stole the money. If they had wanted to do that, there has been plenty of opportunity before now, and that is a lot of Monero that they could have stolen at any time.

Sent from Proton Mail mobile

-------- Original Message --------
On Nov 3, 2023, 9:14 AM, spirobel wrote:

> lets shut the CCS down and support developers directly. You guys have failed.
> (Or you stole the money. There is no way to tell.)
>
> —
> Reply to this email directly, [view it on GitHub](https://github.com/monero-project/meta/issues/916#issuecomment-1792417680), or [unsubscribe](https://github.com/notifications/unsubscribe-auth/A33HFOXS6WBBQQDMR3MRCJLYCTU3HAVCNFSM6AAAAAA63D5YLCVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMYTOOJSGQYTONRYGA).
> You are receiving this because you are subscribed to this thread.Message ID: ***@***.***>

## spirobel | 2023-11-03T13:27:45+00:00
>I don't actually feel like they stole the money. 

There is no way to tell. This system is extremely stupid. Instead of building a relationship of mutual trust between developers and donors, we have a middle man that can just take the money or lose it because of incompetence. 

Also we need to bow to this middle man if we want to make a living. Because this middle man can drag out payments or refuse to merge requests for funding.

## tayvano | 2023-11-03T14:20:56+00:00
@Monero-HackerIndustrial --

> The actor that you have been following was the same one as the atomic wallet hack right? 

No, the actors I'm following are Russian-speaking while Atomic Wallet was hacked by Lazarus aka North Korean state-sponsored actors. Based on the subsequent DPRK hacks like [AlphaPo, Coinspaid, Coinex, and Stake](https://coinspaid.com/company-updates/the-coinspaid-hack-explained/) the Atomic Wallet hack is likely is from some variation of their Operation Dreamjob campaign. Basically they offer mid-tier devops guys who have too much server access a nice, cushy job and drop a malicious PDF or ZIP or something as part of the job application process and escalate from there.

That said, there are major overlaps with the crew that was responsible for [3CX](https://www.sentinelone.com/blog/smoothoperator-ongoing-campaign-trojanizes-3cx-software-in-software-supply-chain-attack/) and [JumpCloud](https://jumpcloud.com/blog/security-update-june-20-incident-details-and-remediation) supply chain attacks so it may be that Atomic Wallet's compromise was more sophisticated than a mal pdf.

While DPRK has sophisticated malware across Mac, Windows, Linux, they rely heavily on social engineering to make initial access and escalate privs. They trick **you** into installing something that ultimately grants them access. Their turnaround time is also pretty dang fast and, as such, even less technically adept victims are usually pretty quick to determine what message / email was the source of compromise once they've been hit (e.g. a malicious email was received on Oct 26 by a victim, their wallets were drained on Oct 30).

If DPRK is responsible for this attack, which is possible but I think unlikely, it's more likely to be from one of campaigns that target [security researchers](https://blog.google/threat-analysis-group/active-north-korean-campaign-targeting-security-researchers/), use Signal/Wire instead of email/Slack, and take advantage of npm/PyPI packages rather than ZIPs/PDFs.

> how common was the compromise of xmr wallets?

The distribution of coins stolen appears similar to the distribution of victim's devices is similar to the distribution of wallets used to generate the compromised keys: it reflects the coins/devices/wallets this specific demographic of people used/held, not what the threat actor targets/prefers. XMR is not the most common coin but its also not rare by any stretch. There have been more XMR thefts than DOGE thefts, for example, lol.

The thing that stands out to me about this hack is the timeline. It appears we're talking about a generally cold wallet that was not accessed or sent from for a decent period of time prior to the theft. In my opinion, it's more likely that this theft was executed by my russian-speaking motherfuckers than by DPRK, but, tbh, it's even more likely to be an individual or group more similar to the one that got [Luke](https://lordx64.medium.com/multiple-linux-backdoors-discovered-targeting-bitcoin-core-developer-technical-analysis-793f8491f561) back in December.

@SamsungGalaxyPlayer -- I've pinged my contacts to see if anyone has a deposit for those consolidations. Thanks for dropping those.

@ everyone insinuating theft or inside job here -- stop being stupid. your anti-social pathologies are unhelpful and harmful  to the situation at hand and the ecosystem in general.

## ghost | 2023-11-03T14:23:49+00:00
It is very ironic that when the wallet of Monero is being hacked devs would trace the hacker's transaction. I think this is a serious issue and could damage Monero's credibility as a privacy coin.

Whether or not hacker is being caught, it will create more damage to the coin for exposing traceability.

@tayvano This is much, much worse than being speculated for inside job. How the earth that the privacy coin could be traced? We should already assume that the ecosystem being killed because of this.

## intr-cx | 2023-11-03T14:28:51+00:00
@kaliubuntu0206 
> It is very ironic that when the wallet of Monero is being hacked devs would trace the hacker's transaction.

The only reason they can do this is because they still have the private keys to the wallet.

## ghost | 2023-11-03T14:33:35+00:00
@intr-cx I don't think so, Like what the consolidation means, hacker already drained the wallet and tried to consolidate it to other wallet which shouldn't be traced at this point.

## intr-cx | 2023-11-03T14:46:22+00:00
@kaliubuntu0206 if you actually look through the chatlogs and the kind of 'tracking' they do, it's primarily probabilistic searches using [Pokkst's decoy scanner](https://github.com/pokkst/monero-decoy-scanner) and some clever guesswork based on some highly unlikely statistics about the transactions. After this they're probably going to contact some CEXes with big puppy eyes about transactions with similar amounts.

Regarding the CCS: Whether this happened out of malice, incompetence, or something beyond their control, it clearly demonstrates that CCS needs a complete reform in the very least. Dropping CCS altogether for a system where no single entity has the final say is even better.

## tayvano | 2023-11-03T17:11:20+00:00
> @tayvano This is much, much worse than being speculated for inside job. How the earth that the privacy coin could be traced? We should already assume that the ecosystem being killed because of this.

LOL honey don't you dare tell me that _talking_ about the well-known and well-documented ways in which monero can be traced and the multitude of ways monero users' privacy can be broken is more harmful than 1) the well-known and well-documented ways in which monero can be traced 2) the multitude of ways monero users' privacy can be broken 3) the theft from good-faith builders who have long served the monero ecosystem.

Like, what, is your plan to simply pretend that monero is always untraceable? Because that doesn't make monero untraceable. In fact, that's what leads to people getting fucked because they made bad assumptions based on incomplete information perpetuated by ignorant people like you.

It's quite easy to watch batches of Monero move through the network, especially given a starting point and a narrow time frame. Monero has more fingerprints than most every other chain which is only amplified by the fact everyone is running their own nodes. Further, given the general lack of liquidity on **every** network rn, anyone with eyeballs can easily find the $200k output for a $200k input _even when_ the threat actor is moving ETH -> BTC or BTC -> ETH via one of the most liquid centralized exchanges. Given that a **far** smaller subset of centralized exchanges support Monero, the fact the there are no decentralized bridges, the fact we're talking about a sum that's far more than $200k, and the fact the hacker has undoubtedly moved to Bitcoin as that is where they can actually get value for their coins (and actually hide in mixers with more liquidity than the monero network on the whole), its a couple hours of manual work to find the output txns to BTC, and less than an hour if you get lucky or have the ability to filter down the withdrawals from multiple CEX hot wallets quickly.

Whether or not the output will be found in this case depends exclusively on whether or not anyone is **sufficiently motivated** to find said output. **As is always the case.** Contrary to popular belief by the paranoid minds that make up the monero ecosystem, most transactions aren't traced because no one gives any fucks about your transactions lol.

If you don't want the above to be true, then you best go understand how Monero **is** traced and then take steps to make it less traceable and especially educate yourself and other individuals on steps they can take to make their specific movements harder to trace. **That** is how you make Monero more private—not by lying to people like iTs sO uNtRaCeAbLe. 🤦‍♀️

## jeffro256 | 2023-11-03T17:38:56+00:00
> Monero has more fingerprints than most every other chain which is only amplified by the fact everyone is running their own nodes.

Would you care to expand on this point, please?

## TheFuzzStone | 2023-11-03T18:25:29+00:00
> is your plan to simply pretend that monero is always untraceable?

Monero is one of the tools to keep your financial privacy. That doesn't mean you can't shoot yourself in the foot.

> Monero has more fingerprints than most every other chain which is only amplified by the fact everyone is running their own nodes. Further, given the general lack of liquidity on every network rn, anyone with eyeballs can easily find the $200k output for a $200k input even when the threat actor is moving ETH -> BTC or BTC -> ETH via one of the most liquid centralized exchanges. Given that a far smaller subset of centralized exchanges support Monero, the fact the there are no decentralized bridges, the fact we're talking about a sum that's far more than $200k, and the fact the hacker has undoubtedly moved to Bitcoin as that is where they can actually get value for their coins (and actually hide in mixers with more liquidity than the monero network on the whole), its a couple hours of manual work to find the output txns to BTC, and less than an hour if you get lucky or have the ability to filter down the withdrawals from multiple CEX hot wallets quickly.

Wow, that's how trackable XMR turns out to be, even better than the mixers in BTC. That's fantastic. Then you should think about writing software to track XMR and sell it to government agencies.

BTW, 200k, 500k, even a few million dollars in XMR, on the OTC market is just a drop in the ocean, which can be turned into cash at a faster than getting 10 confirmations on the BTC network.

>Whether or not the output will be found in this case depends exclusively on whether or not anyone is sufficiently motivated to find said output. 

And if it doesn't, it's only because no one is motivated. Uh-huh. I see. And it's not because the person who stole the XMR knows how to get away with it. Only motivation is the factor here.

>As is always the case. Contrary to popular belief by the paranoid minds that make up the monero ecosystem, most transactions aren't traced because no one gives any fucks about your transactions lol.

Let's write it down, if someone needs privacy, they should go to fully open blockchains like BTC or ETH, because there is more liquidity there.

---

I didn't come to fight with you, I just didn't like the way you responded above.

## likuilin | 2023-11-03T20:13:04+00:00
> I didn't come to fight with you, I just didn't like the way you responded above.

As a random person on the internet, I didn't come here to read an argument about how trackable XMR is. What's with the inflammatory language? 

## ghost | 2023-11-03T22:28:19+00:00
> If you don't want the above to be true, then you best go understand how Monero is traced and then take steps to make it less traceable and especially educate yourself and other individuals on steps they can take to make their specific movements harder to trace. That is how you make Monero more private—not by lying to people like iTs sO uNtRaCeAbLe. 🤦‍♀️

@tayvano I think your words should be widely written on the front page of getmonero.org with big warning banner. Seems like an important disclaimer.

> As a random person on the internet, I didn't come here to read an argument about how trackable XMR is. What's with the inflammatory language?

@likuilin It literally means that Monero isn't a privacy coin anymore but rather we should call it somewhat a low-liquidity version of coinjoin alternative

## termermc | 2023-11-03T22:34:31+00:00
> > If you don't want the above to be true, then you best go understand how Monero is traced and then take steps to make it less traceable and especially educate yourself and other individuals on steps they can take to make their specific movements harder to trace. That is how you make Monero more private—not by lying to people like iTs sO uNtRaCeAbLe. 🤦‍♀️
> 
> @tayvano I think your words should be widely written on the front page of getmonero.org with big warning banner. Seems like an important disclaimer.
> 
> > As a random person on the internet, I didn't come here to read an argument about how trackable XMR is. What's with the inflammatory language?
> 
> @likuilin It literally means that Monero isn't a privacy coin anymore but rather we should call it somewhat a low-liquidity version of coinjoin alternative

It's time for you to stop talking now

## ghost | 2023-11-03T22:37:40+00:00
> It's time for you to stop talking now

@termermc Do you work for feds trying to advertise that monero is untraceable and track those footprints or you hold a stack of them willing not to be damaged by the fact

## termermc | 2023-11-03T22:38:48+00:00
> > It's time for you to stop talking now
> 
> @termermc Do you work for feds trying to advertise that monero is untraceable and track those footprints or you hold a stack of them willing not to be damaged by the fact

No, I just think you're stupid and have nothing to add to this thread

## ghost | 2023-11-03T22:40:09+00:00
> No, I just think you're stupid and have nothing to add to this thread

I don't think so, attempting to keep my mouth shut will only shown as an attempt to keep the lies of untraceable currency

## ghost | 2023-11-03T22:41:33+00:00
If the monero devs believe on the untraceable currency vision they should stop tracking the transaction. It will only damage the reputation of the project.

## elibroftw | 2023-11-03T22:47:48+00:00
Monero community becoming toxic speedrun any %. @kaliubuntu0206, check out breaking monero. The monero community should focus a lot more on tracking tools so that it can figure out monero's weaknesses and promote better education in how to use Monero privately. 

On a serious note @fluffypony, not sure if you got a chance to read my question but I was wondering where all you had the CCS wallet seed stored? And how was the seed created (e.g. monero GUI, cli)? I really don't believe this is a malware issue as Luigi said he unlocked the wallet last time in may and the funds were stolen in early September. 

Also @luigi1111, were your ssh password and CCS wallet passwords the same or different?

## ghost | 2023-11-03T22:53:56+00:00
> Monero community becoming toxic speedrun any %. @kaliubuntu0206, check out breaking monero. The monero community should focus a lot more on tracking tools so that it can figure out monero's weaknesses and promote better education in how to use Monero privately.

This is what I wanted to tell, rather if we want to trace the transaction we need to tell everyone about the truth in a transparent way.

## termermc | 2023-11-03T22:57:46+00:00
> > Monero community becoming toxic speedrun any %. @kaliubuntu0206, check out breaking monero. The monero community should focus a lot more on tracking tools so that it can figure out monero's weaknesses and promote better education in how to use Monero privately.
> 
> This is what I wanted to tell, rather if we want to trace the transaction we need to tell everyone about the truth in a transparent way.

What @elibroftw is referring to is the series called Breaking Monero. The website is [here](https://www.monerooutreach.org/breaking-monero/), and you can watch the first and subsequent videos on [YouTube](https://www.youtube.com/watch?v=WOyC6OB6ezA). Note that it was originally made 4 years ago.

## lazios | 2023-11-03T22:57:56+00:00
> > Monero community becoming toxic speedrun any %. @kaliubuntu0206, check out breaking monero. The monero community should focus a lot more on tracking tools so that it can figure out monero's weaknesses and promote better education in how to use Monero privately.
> 
> This is what I wanted to tell, rather if we want to trace the transaction we need to tell everyone about the truth in a transparent way.

My brother in christ, the fact that ring signatures are the weakest link and that you can follow transactions for 1-2 hops if someone reuses a lot of outputs is nothing new. This "flaw" will be gone with full chain membership proofs which will arrive at some point in the future. Relax, Monero is not broken and nobody made promises about privacy guarantees that are now suddenly broken. Everything is working as intended.

## luigi1111 | 2023-11-03T23:00:00+00:00
> Also @luigi1111, were your ssh password and CCS wallet passwords the same or different?

They were different.

## elibroftw | 2023-11-03T23:06:02+00:00
> > Also @luigi1111, were your ssh password and CCS wallet passwords the same or different?
> 
> They were different.

Thanks for answering. Has the seed generation of Monero library been audited? I really hope this is just a compromised seed and not a bigger issue.

## SamsungGalaxyPlayer | 2023-11-03T23:50:55+00:00
https://moonstoneresearch.com/2023/11/03/Postmortem-of-Monero-CCS-Hack

## ghost | 2023-11-03T23:58:06+00:00
> https://moonstoneresearch.com/2023/11/03/Postmortem-of-Monero-CCS-Hack

@SamsungGalaxyPlayer I think the article explains well about the limitations of tracing monero and how the hacker will likely be identified if those problematic transactions were ever detected on CEXes. Well done.

> Transactions with an atypical number of output enotes occur for a variety of reasons, but these are almost always anchored in some specific use-case. For example, transactions with multiple output enotes might be sent by an exchange to multiple of their customers who wish to withdraw. However, transactions with more than two output enotes are probably not destined as an exchange or instant exchange deposit, since there is only one recipient.

So I think some machine learning and filtering of unlikely output numbers would raise some chance of being traced. And what is more important that AML providers will likely create a map for every CEX deposits to trace those users which could be used for compliance purpose aka surveillance.

Things that should be learned while using monero is that we need to mimic some behavior of what PocketChange does in a random like behavior in order to increase privacy while spending it.



## Hueristic | 2023-11-04T01:57:21+00:00
If I were a suspicious person I would think something like this would be used to leverage devs to work on tracing techniques in finding the culprit thereby doing the chain analysis boys job for them.

## Final-Phoenix | 2023-11-04T13:15:49+00:00
> @ everyone insinuating theft or inside job here -- stop being stupid. your anti-social pathologies are unhelpful and harmful to the situation at hand and the ecosystem in general.

It's not stupid at all. Even though I would like to believe this isn't true there is no way to know for sure. It will always be a possibility. We need to do some method of direct funding or a better way to distribute and minimize trust via multisig.

If not nefarious, this was at the very least irresponsible negligence. That was a lot of money lost that could've done a lot of good for Monero.

## tayvano | 2023-11-04T14:39:52+00:00
Since it seems like this thread has escaped the confines of github, if you're a random uneducated person freaking out bc someone on twitter told you to freak out, plz calm down and educate yourself. then, please harden your emotional response to random statements by random people on the internet.

https://twitter.com/sethforprivacy/status/1720792327579414915

https://twitter.com/DontTraceMeBruh/status/1720730193172590883

## d4f5409d | 2023-11-04T16:08:17+00:00
> > > I am of the same opinion. All Tayvano's "OG" friends were also Windows users
> > 
> > @marcovelon You know, I'd really like to see some citations in a thread about cybersecurity when even Tayvano said all sorts of devices.
> > 
> > My questions for Luigi and Fluffy Pony are:
> > 
> > * Where all has the CCS seed been stored (device, app, file format)? e.g. Windows/ubuntu, Password managers, text files, etc.
> >   
> >   * Also, If the Ubuntu server storage got shot one day, how would you restore the CCS wallet?
> 
> Seed was only on paper on my end.

Who did access the paper, and did you check whether the paper has a unrecognisable fingerprint on it?

## d4f5409d | 2023-11-04T16:10:14+00:00
Also, please ask yourself, why exactly now? 

It would be nice to initiate a dedicated jitsi or jami call to get this solved. Real time communication could make things faster and more efficient. We could also visualize what exactly happened on a timeline for example.

## scottAnselmo | 2023-11-04T18:23:56+00:00
**Threat Modeling**

Returning to the conversation to one of the questions initially proposed:

> - How do we structure the CCS going forward?

If focusing on high level policy and procedures with respect to this event, within a security framework it helps to think of things with respect to Confidentiality, Integrity, and Availability. 

I believe one of the primary focuses should be around integrity. The general threats even if they seem obvious I would highlight that should be taken into account are:

- Preventing unauthorized parties from spending funds
- Preventing authorized parties from accidentally sending the funds to the wrong address
- Preventing an authorized party from running away from funds
- Preventing collusion of multiple parties

On the availability side:

- Ensuring funds can be distributed
- Ensuring funds are distributed in a timely fashion

**Possible Policy/Procedures**

- The person merging the CCS into 'Funding Required' should be different than the person(s) sending the funds upon milestones being hit. Generally businesses split out those who approve expenses, and those who process them
- Distribution of funds from any CCS wallet should require at least two signatures

The first point is relatively straightforward in terms of procedure. The second point I would propose a 2 of 7 Core signatures wallet. This provides general mitigation in terms of wallet integrity. As the number of signatures required gets raised you further impact availability's timely distribution and things like 'Core all on a sinking boat' factor.

**Other**

The above doesn't guarantee this event will never happen again, because root cause hasn't been determined with a high degree of probability. It simply provides a quick, basic threat model and set of simple policy mitigations given the limited resources of any FOSS project like Monero. Others are welcome to identify other threats around Confidentiality, Integrity, and Availability and high level policy to guide mitigation.

## tarris034otheracc | 2023-11-05T09:52:03+00:00
@kaliubuntu0206:
> I think the article explains well about the limitations of tracing monero and how the hacker will likely be identified if those problematic transactions were ever detected on CEXes. Well done.

Wouldn't sending this stolen funds couple times to new Monero wallets using CLI wallet with own full node be enough to never trace this attacker ?

## d4f5409d | 2023-11-05T10:22:25+00:00
> Wouldn't sending this stolen funds couple times to new Monero wallets using CLI wallet with own full node be enough to never trace this attacker ?

We only have metadata to work from which is they presumably will exchange the mass amount of Monero stolen but it's unsure who was exactly

## tarris034otheracc | 2023-11-06T16:54:20+00:00
Due to no conclusions on the attack vector how about we make an offer to the attacker that we stop chasing the stolen funds if he tells us how he did it ? something like those ETH cases where attacker was offered to legally take some percentage if he returns the rest of the stolen money ?


## mckibbinusa | 2023-11-06T20:32:46+00:00
My take on what I am reading is that the incident is an OPSEC problem at the wallet level, and NOT a 'hacking' incident involving the blockchain itself.  If that is true, this should be simple to fix at the team level. I read today that @FluffyPony is recommending that the core developer group be decentralized in some way, which sounds like prudent advice.  For the record, I am relieved to learn this is not a 'hack' of the Monero blockchain security model itself (though I may be wrong). For the record, I have long harbored concerns about OPSEC issues at the developer level at Monero and every other coin out there. I get especially worried when the team considers esoteric innovations that could compromise the Monero security model fundamentally. We are all counting on the developers to exercise the greatest of care with Monero's security.

## luigi1111 | 2023-11-07T01:35:07+00:00
Correct. Whatever happened, there is no reason to suspect anything related to the blockchain security itself.

## Monero-HackerIndustrial | 2023-11-07T04:57:21+00:00
Hey @luigi1111, are you able to provide some logs and config files from the ubuntu host? 
I was curious about any entries in crontab, any extra keys on the known hosts or extra users added. Curious about some potential binaries and scripts that could potentially be scattered in places like /usr/sbin/ 
I can dive deeper into some of the TTP from known actors and the malware they use to help give you a better list of things we can look for. 

@tayvano 
Yeah I agree on Lazarus group leaning on social engineering although like you mentioned there is some precedence to DPRK using malicious packes on pip/npm repos. I have also seen them backdoor known software with a cloned website for specific targets they are after. Attacking a wallet with this small of an amount (compared to the amount in defi accounts) does not make me inclined to attribute it to them (along with the social engineering aspect and goals etc)

The actors that targeted Luke last year make more sense, although that specific initial access was physical access to the server in a data center. That sort of targeting of a monero dev over the stolen amount would surprise me. Seems like that attack was the only one attributed to UNC1142. They list other APTs that use the TINYSHELL based backdoors. 

I knew of the Lazarus group but could use some help listing out other known APT's from similar incidents so I can look up the malware for any potential IOCs that they might have left behind. It would be nice to attribute this. 

## luigi1111 | 2023-11-07T16:57:18+00:00
(update for thread) We are in contact on IRC. Will update if anything is found.

## PidgeyBE | 2023-11-07T19:59:00+00:00
Am I correct to assume that a hack like this is not possible if you have a hardware wallet? (like ledger, trezor, ..)
Because your private keys are never exposed to a network attached computer (ubuntu, windows, ..)?

## tarris034otheracc | 2023-11-07T21:00:29+00:00
> Am I correct to assume that a hack like this is not possible if you have a hardware wallet? (like ledger, trezor, ..) Because your private keys are never exposed to a network attached computer (ubuntu, windows, ..)?

Hardware wallet is just another third-party you have to trust and if we are into trustless money then instead of buying and trusting some company we should invest some time in learning how to use air-gaped machine with it's cold wallet.

This hardware wallets are not to be trusted, there's many attack vectors like people behind the company, hardware and software flaws in their closed applications and so on... 

Recently one of those companies added new "feature" of private key recovery - there goes your "never exposed key" and we all remember the leaked database of clients that shouldn't exist with all the home addresses...

It's safer to be a fish in the ocean (regular hardware) than a shark in a small tank.

## johnalanwoods | 2023-11-07T21:38:32+00:00
> > Am I correct to assume that a hack like this is not possible if you have a hardware wallet? (like ledger, trezor, ..) Because your private keys are never exposed to a network attached computer (ubuntu, windows, ..)?
> 
> 
> 
> Hardware wallet is just another third-party you have to trust and if we are into trustless money then instead of buying and trusting some company we should invest some time in learning how to use air-gaped machine with it's cold wallet.
> 
> 
> 
> This hardware wallets are not to be trusted, there's many attack vectors like people behind the company, hardware and software flaws in their closed applications and so on... 
> 
> 
> 
> Recently one of those companies added new "feature" of private key recovery - there goes your "never exposed key" and we all remember the leaked database of clients that shouldn't exist with all the home addresses...
> 
> 
> 
> It's safer to be a fish in the ocean (regular hardware) than a shark in a small tank.

Where you trust a downloaded Kernel, the CSPRNG, the hardware RDRand or entropy seeding, the /dev/random implementation, the x86 or ARM hardware implementation the OS user space etc etc etc 

Come on man . AVI

## tarris034otheracc | 2023-11-07T22:05:17+00:00
> 
> Where you trust a downloaded Kernel, the CSPRNG, the hardware RDRand or entropy seeding, the /dev/random implementation, the x86 or ARM hardware implementation the OS user space etc etc etc
> 
> Come on man . AVI

I see you didn't get the fish in the ocean analogy, in case of hardware wallets you're being easier to target.

## ghost | 2023-11-08T09:02:33+00:00
> > Am I correct to assume that a hack like this is not possible if you have a hardware wallet? (like ledger, trezor, ..) Because your private keys are never exposed to a network attached computer (ubuntu, windows, ..)?
> 
> Hardware wallet is just another third-party you have to trust and if we are into trustless money then instead of buying and trusting some company we should invest some time in learning how to use air-gaped machine with it's cold wallet.
> 
> This hardware wallets are not to be trusted, there's many attack vectors like people behind the company, hardware and software flaws in their closed applications and so on...
> 
> Recently one of those companies added new "feature" of private key recovery - there goes your "never exposed key" and we all remember the leaked database of clients that shouldn't exist with all the home addresses...
> 
> It's safer to be a fish in the ocean (regular hardware) than a shark in a small tank.

so then make your own DIY HWW using ANONERO or Feather

## tarris034otheracc | 2023-11-08T10:12:52+00:00
> 
> so then make your own DIY HWW using ANONERO or Feather

For a properly air-gaped cold wallet machine you can use whatever, even outdated Windows.
Just be sure whole disk is fully encrypted in case of robbery and have encrypted seed words printed and hidden in many places.

I'm not using anything other than official CLI wallet for my cold wallet, in case of my usage I never had to use other than official wallet and I never use my phone for banking or cryptocurrencies as I don't trust android or custom made firmwares.

But if I had to use other software for the sake of convenience, I would use it only for small change.

## d4f5409d | 2023-11-08T19:14:54+00:00
Have RSA-2048 been used?

## luigi1111 | 2023-11-09T17:17:22+00:00
After Thanksgiving.

## d4f5409d | 2023-11-10T17:04:47+00:00
@luigi1111 may this be possible in your case? https://www.youtube.com/watch?v=3T2Al3jdY38

## d4f5409d | 2023-11-13T21:11:01+00:00
https://arstechnica.com/security/2023/11/hackers-can-steal-ssh-cryptographic-keys-in-new-cutting-edge-attack/

SSH vulnerability

## shortwavesurfer2009 | 2023-11-14T01:09:09+00:00
> https://arstechnica.com/security/2023/11/hackers-can-steal-ssh-cryptographic-keys-in-new-cutting-edge-attack/
> 
> SSH vulnerability

Earlier in the thread it was brought up that an ssh password was used instead of a key. Still an interesting read though. Yet another attack against RSA. Apparently DSA is the way to go.

## d4f5409d | 2023-11-14T07:04:40+00:00
Sorry I didn't have the time yet to browse through all of the thread and do all of the research, but I am here to send here anything that may help

## oblak-be | 2023-11-15T19:08:17+00:00
It is unbelievable that what is referred to as a "cold" wallet, was still a box with network access (SSH). For the most OG blockchain network next to Bitcoin you would think the core maintainers would know the difference between a hot and a cold wallet.

I am still grateful for all the contributors making Monero possible, but I hope that this incident will inspire more developers to take operational security serious.

Why is it so easy to break in into Microsoft? Because of all the Windows.....

## sjatkins | 2023-11-15T23:11:42+00:00
If you have a server that only should be accessed by one machine then firewall should ensure that.   
SSH access by password is way less secure always than by key.   Was the server set up with standard best practices for hardening it against any unwanted access? 
As others mentioned Windows (non-server anyway) is WAY HARD to properly secure even for seasoned pros. 
Why wouldn't a hardware and/or much more cold wallet have been used for vault of significant amount of monero? 

## d4f5409d | 2023-11-16T21:48:20+00:00
Another helpful thing could be: didn't you accidentaly exposed ssh passwords (keys)?

https://arstechnica.com/security/2023/11/developers-cant-seem-to-stop-exposing-credentials-in-publicly-accessible-code/

## twannnnn | 2023-11-17T04:35:30+00:00
Sounds like in house to me so I can say if you work for me block chain it's possible then

## Final-Phoenix | 2023-11-25T08:22:19+00:00
"Rethinking the Monero CCS: A cypherpunk proposal"

https://monero.observer/cypherpunk-transmission-017-rethinking-monero-ccs-cypherpunk-proposal/

## and21togrowon | 2023-12-06T12:05:11+00:00
1 vote for Luigi1111

## twannnnn | 2023-12-06T12:07:01+00:00
Like what

On Wed, Dec 6, 2023, 7:05 AM and21togrowon ***@***.***> wrote:

> 1 vote for Luigi1111
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/meta/issues/916#issuecomment-1842739143>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/BDHMSFSIMDVBW53TJUWC623YIBNQRAVCNFSM6AAAAAA63D5YLCVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMYTQNBSG4ZTSMJUGM>
> .
> You are receiving this because you commented.Message ID:
> ***@***.***>
>


## vampyren | 2023-12-06T22:15:26+00:00
sorry i'm no expert buy why not using a hw wallet? 

## SyntheticBird45 | 2023-12-30T11:55:42+00:00
> P.P.S. stop using Windows for such projects.

> Why is it so easy to break in into Microsoft? Because of all the Windows.....

> I can't understand why on Earth you would use less secure system (the Windows hot wallet)

Operational Security is a security research topic. Blaming Luigi for using Windows with false claims such as Windows being inherently insecure compared to Linux is just annoying for him and the discussion. If you have no practical knowledge on this matter, stop proposing such *insights*.

## SyntheticBird45 | 2023-12-30T12:01:41+00:00
> sorry i'm no expert buy why not using a hw wallet?

- Hardware wallet centralize the hidden seed to a single physical object. This could potentially (as seen a lot before) make the CCS fund holder a target for robbery.
- Hardware wallet security isn't perfect. Even tho it is far more secure than software based security, some parts of the wallet cryptographic operations are handled by specific chips that ensure security through obscurity.
- Some vulnerabilities have already been found in the past [and exploited](https://youtube.com/watch?v=dT9y-KQbqi4).
- Makes it harder for emergency procedures since the holder need to keep the hw with him

## oblak-be | 2023-12-30T16:32:20+00:00
> > P.P.S. stop using Windows for such projects.
> 
> > Why is it so easy to break in into Microsoft? Because of all the Windows.....
> 
> > I can't understand why on Earth you would use less secure system (the Windows hot wallet)
> 
> Operational Security is a security research topic. Blaming Luigi for using Windows with false claims such as Windows being inherently insecure compared to Linux is just annoying for him and the discussion. If you have no practical knowledge on this matter, stop proposing such _insights_.

I admit there was a bit of frustration during the posting, but hey, it's not us who lost half a million in donations. A little bit of frustration was justified. If you can't stand the heat, stay out the kitchen. But ok, we can (and will) be constructive too.

On the topic of Windows, it **is** inherently less safe than a minimal Linux system, for starters because of its closed source nature. The time whining about Windows is time you could be spending some time learning Linux thoroughly. It will greatly help in upping that OPSEC posture.

Some good advice, now we are on it:

- you don't need trezor or ledger, a few simple laptops and some usb sticks are fine. You can find all that for less than 600$.
- use an offline device to keep the private keys and sign transactions. Don't do anything else with that device.
- use a different device to broadcast transactions. Don't do anything else with that device, and keep it in an isolated network.
- use an usb stick to transfer transaction files between the 2 devices
- use another different device for development / work, keep it on a different network.
- use another devices four leisure, like movies and games. Also on a different network.

If multiple holders share the wallet, share the private key physically at inception.

## felipebrunet | 2023-12-31T16:41:55+00:00
Hi, I was checking the monero github donation address (with the secret view key that is published there) and I saw someone deposited 2,696.73 xmr on dec 6 2023. An amount quite close to the extracted 2,675.73 xmr. Are those 2 transfers related? or is it just a coincidence? Be that as it may, that donation may help to recover the CCS fund right? Unless that money was already spent in something else (cause I cannot see the address spendings)
primary address: 44AFFq5kSiGBoZ4NMDwYtN18obc8AemS33DBLWs3H7otXft3XjrpDtQGv7SqSsaBYBb98uNbr2VBBEt7f2wfn3RVGQBEP3A 
TXID: d6f518d8131472aac362f1f22a99da46fc93aed53af8c83baf637f62193c4f11
Secret View Key:  f359631075708155cc3d92a32b75a7d02a5dcf27756707b47a2b31b21c389501
Sub address: 888tNkZrPN6JsEgekjMnABU4TBzc2Dt29EPAvkRxbANsAnjyPbb3iQ1YBRk1UXcdRsiKc9dhwMVgN5S9cQUiyoogDavup3H

## vampyren | 2023-12-31T17:18:03+00:00
> > sorry i'm no expert buy why not using a hw wallet?
> 
> * Hardware wallet centralize the hidden seed to a single physical object. This could potentially (as seen a lot before) make the CCS fund holder a target for robbery.
> * Hardware wallet security isn't perfect. Even tho it is far more secure than software based security, some parts of the wallet cryptographic operations are handled by specific chips that ensure security through obscurity.
> * Some vulnerabilities have already been found in the past [and exploited](https://youtube.com/watch?v=dT9y-KQbqi4).
> * Makes it harder for emergency procedures since the holder need to keep the hw with him

You might not know but Trezor has a hidden wallet behind the visible wallet so the first point is not valid.
Also yes "some" vulnerabilities is 100X better than having it on a software wallet where there are so much more risks involved.
Yes i realizes the comment don't help but then again people need to know and understand that having hw wallet remove so much more risk from the table.  

## Final-Phoenix | 2024-01-06T03:09:37+00:00
> Hi, I was checking the monero github donation address (with the secret view key that is published there) and I saw someone deposited 2,696.73 xmr on dec 6 2023. An amount quite close to the extracted 2,675.73 xmr. Are those 2 transfers related? or is it just a coincidence? Be that as it may, that donation may help to recover the CCS fund right? Unless that money was already spent in something else (cause I cannot see the address spendings) primary address: 44AFFq5kSiGBoZ4NMDwYtN18obc8AemS33DBLWs3H7otXft3XjrpDtQGv7SqSsaBYBb98uNbr2VBBEt7f2wfn3RVGQBEP3A TXID: d6f518d8131472aac362f1f22a99da46fc93aed53af8c83baf637f62193c4f11 Secret View Key: f359631075708155cc3d92a32b75a7d02a5dcf27756707b47a2b31b21c389501 Sub address: 888tNkZrPN6JsEgekjMnABU4TBzc2Dt29EPAvkRxbANsAnjyPbb3iQ1YBRk1UXcdRsiKc9dhwMVgN5S9cQUiyoogDavup3H

Generous whale, remorseful thief, or intentional ruse with the goal of bringing attention to improving the security and structure of the CSS

I don't think anyone knows for sure. Either way it was a fortunate surprise and we shouldn't let this second chance go to waste.

## d4f5409d | 2024-01-06T08:43:11+00:00
> What's the timeline for when host and network logs will be made available? Has the compromised machine been forensically imaged? 
> After Thanksgiving.

Where are the logs? Maybe I am so dumb, but I can't find it in this thread. Is it somewhere else?

## luigi1111 | 2024-01-06T15:57:26+00:00
> Where are the logs? Maybe I am so dumb, but I can't find it in this thread. Is it somewhere else?

https://github.com/monero-project/meta/issues/923

## preland | 2024-01-14T01:01:55+00:00
> Hi, I was checking the monero github donation address (with the secret view key that is published there) and I saw someone deposited 2,696.73 xmr on dec 6 2023. An amount quite close to the extracted 2,675.73 xmr. Are those 2 transfers related? or is it just a coincidence? Be that as it may, that donation may help to recover the CCS fund right? Unless that money was already spent in something else (cause I cannot see the address spendings)
> primary address: 44AFFq5kSiGBoZ4NMDwYtN18obc8AemS33DBLWs3H7otXft3XjrpDtQGv7SqSsaBYBb98uNbr2VBBEt7f2wfn3RVGQBEP3A
> TXID: d6f518d8131472aac362f1f22a99da46fc93aed53af8c83baf637f62193c4f11
> Secret View Key: f359631075708155cc3d92a32b75a7d02a5dcf27756707b47a2b31b21c389501
> Sub address: 888tNkZrPN6JsEgekjMnABU4TBzc2Dt29EPAvkRxbANsAnjyPbb3iQ1YBRk1UXcdRsiKc9dhwMVgN5S9cQUiyoogDavup3H

Something which would give it away: what was the “gas” price for a transaction involving 2,696.73 XMR?

If it was a “generous whale” that had over 2 and a half K in Monero to burn, it would make more sense for them to pay a number equivalent or higher to the amount taken.

However, if it was a “remorseful thief”, the thief likely wouldn’t have extra XMR to use for fees, nor would they feel obligated to do so.

In fact, if this was a case of “remorseful thief”, there could actually be a completely different reasoning behind the sudden return of funds: the thief already had a sizable amount of XMR in their possession, and was afraid that the theft may bring unwanted instability to the project (after all, it doesn’t matter how much XMR you have if the entire chain dies).

Or, they were just bored and gave the money back (considering the prevalence of crypto casinos for a while, having a lack of practical uses for a large amount of crypto can lead to wacky decisions; basically imagine if you won a lottery for 1 million dollars, but it was only payable via gallon jugs of 1% milk)

At the end of the day, those are all just theories, and because of the design of Monero, there won’t (or shouldn’t) ever be a way to determine which one really happened. What’s important is making sure this doesn’t happen again.

## TheCodeingPadawan | 2024-01-25T20:49:18+00:00
I know this may be an unpopular take, as it may be better to keep everything in house. However, would it be worth considering using other solutions in the chain of custody.. Something like Rhino wallet that has 2FA via 1 in 2 multi sig.

From what i understand, it is open source so can be looked over by the team. But if the ecosystem is growing and tools are being made, then it would not be too out-there to start using some of them in house. When you have half a mill in funds, it may be worth it to start thinking more like an org/enterprise.

In the end of the day, a mine for iron may not make there own steal, and most certainly will not make there own equipment for mining it out. They will use the services of CAT, JCB or even an engineering firm to make and design the equipment.

I'm just a Monero user with some technical knowledge on how things work to know it makes sense on the surface, but i have little dev / detailed knowledge to say this would be worth doing or not when deeper details are taken into account. so let me know kindly if this would not be a good idea.

I know that another in house solution would be to have a policy where you hold a limited amount of total funds on a hot wallet, then use Monero's offline transaction feature to top it up periodically. Though I understand the Devs have a valid concern that they may become a target for theft, Should it be known that 1 of them are holding the cold wallet with significant funds.



## HardenedSteel | 2024-05-04T00:50:43+00:00
Related comment: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/444#note_23992

## ghost | 2024-10-14T03:14:39+00:00
Could be an inside job. I mean we are talking about over 350,000 USD.

## nf-works | 2026-02-25T03:20:15+00:00
Any update on where 2,675.73 XMR (!) went?
I feel like funds received from us, the community, are being handled grossly negligent. It appears that another 867 XMR are gone: https://github.com/monero-project/meta/issues/1326

What is the current state of this investigation? What are consequences for the project for this? What are consequences for the people responsible for these funds?

## luigi1111 | 2026-02-25T03:47:35+00:00
There is ~no way to tell with XMR where the funds went. Someone did donate an identical amount to the General Fund a short time after the hack was disclosed, but no one ever claimed it. The 867 XMR is from a time long before and unrelated to this.


The investigation fizzled out as no hack was found. The current state of things is that the CCS wallet is held strictly offline on an airgapped computer.

## geonic1 | 2026-04-14T12:54:23+00:00
It has recently come to light that one of the two people who had access to the drained CCS wallet, @fluffypony, has decided to [appropriate the remaining funds](https://github.com/monero-project/meta/issues/1326#issuecomment-4240654322) in the FFS wallet (the precursor to the CCS). The reasoning appears to be that he believes he is owed that money in exchange for his earlier contributions.

I would also emphasize that only the "cold wallet" in this case was drained while the "hot wallet" remained untouched, suggesting that the perpetrator had access to the keys and this was not a hack. As mentioned in this thread, "fluffypony never had access to the private keys to the hot wallet, but did have the private keys to the main CCS wallet".

edit: It is also worth noting that fluffypony has been accused by a former employer of [committing invoice fraud](https://decrypt.co/77503/fluffypony-monero-cookies-fraud) to the tune of $100,000.

## PPPDUD | 2026-04-16T15:59:55+00:00
Perhaps this is a good time to encourage private entities to start their own funding systems and begin phasing out the centralized CCS fund altogether? That way, the people managing funding will be much higher-profile and can be sued if they defraud their investors, as opposed to the current system where the thief has not been held accountable for their actions and still possesses thousands of XMR stolen from donors.

## nahuhh | 2026-04-16T20:18:53+00:00
> Perhaps this is a good time to encourage private entities to start their own funding systems and begin phasing out the centralized CCS fund altogether? That way, the people managing funding will be much higher-profile and can be sued if they defraud their investors

Never heard of MAGIC?

> as opposed to the current system where the thief has not been held accountable for their actions and still **possesses thousands of XMR stolen from donors.** 

what?

## PPPDUD | 2026-04-16T23:00:47+00:00
> > Perhaps this is a good time to encourage private entities to start their own funding systems and begin phasing out the centralized CCS fund altogether? That way, the people managing funding will be much higher-profile and can be sued if they defraud their investors
> 
> Never heard of MAGIC?
>

No, but I looked it up and it sounds pretty cool! Yet another reason to decommission the CCS wallet.

> > as opposed to the current system where the thief has not been held accountable for their actions and still **possesses thousands of XMR stolen from donors.**
> 
> what?

According to the person who opened this issue (@luigi1111):

> _The CCS Wallet was drained of 2,675.73 XMR (the entire balance) on September 1, 2023, just before midnight._

Unless someone has evidence to the contrary, I believe that the thief still possesses that money to this very day.

## preland | 2026-04-17T00:00:31+00:00
> Unless someone has evidence to the contrary, I believe that the thief still possesses that money to this very day

I think you are going to need to be a _little_ more clear about what you are implying exactly, because the way this is written leaves too much up to interpretation.

## PPPDUD | 2026-04-17T00:02:13+00:00
> > Unless someone has evidence to the contrary, I believe that the thief still possesses that money to this very day
> 
> I think you are going to need to be a _little_ more clear about what you are implying exactly, because the way this is written leaves too much up to interpretation.

What specifically is unclear to you?

## nahuhh | 2026-04-17T00:04:40+00:00
> What specifically is unclear to you?

who you are accusing of being in posession of the stolen funds

> No, but I looked it up and it sounds pretty cool! Yet another reason to decommission the CCS wallet.

being a registered, legal entity, based in USA; MAGIC cannot fund anonymous contributors. It exists as an option for any/all who don't mind going through a KYC process. 

- Monero has many anonymous contributors.
- CCS funds some MAGIC proposals. Example: FCMP audits by veridise.

## PPPDUD | 2026-04-17T00:07:25+00:00
> > What specifically is unclear to you?
> 
> who you are accusing of being in posession of the stolen funds

Someone. I don't know the specifics.

## luigi1111 | 2026-04-17T02:53:42+00:00
It would be expected, unless they subsequently acquired a conscience and forwarded the stolen funds to the General Fund (as there exists an exact match), that the thief is either: A. in possession of; or B. sold the funds.

# Action History
- Created by: luigi1111 | 2023-11-02T15:57:53+00:00
