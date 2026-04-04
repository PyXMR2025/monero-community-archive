---
title: Should we Patch the Airgap Vulnerability in Monero CLI/GUI ?
source_url: https://github.com/monero-project/monero/issues/4634
author: MoneroChan
assignees: []
labels: []
created_at: '2018-10-17T03:04:30+00:00'
updated_at: '2018-10-21T14:03:26+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Re: that 'Default Airgap Vulnerability' (most pro-hackers know what i'm talking about)

1) Bulletproofs is coming, so we can finally use bulletproofs to patch the 'Default Airgap Vulnerabilty' in the CLI/GUI and commence mass wallet migration without bloating the blockchain.

2) Can i re-confirm our stance on officially patching and fixing the existing default airgap vulnerability in the monero GUI/CLI? Because that vulnerability has been known to be used by government intelligence agencies for operations elsewhere.

Are we going to deliberately leave it open "so that the intelligence agencies don't bother us?" and leave it up to individual users own counterintelligence OpSec?

3) The instant fix and Workaround guide is already available for the monero GUI, which can be released at anytime, (however, this will require the trouble of the creation of new wallets for most existing holders of monero and transfer of all funds to the new wallet; hence the wait for bulletproofs).

This vulnerability also affects most other coins including bitcoin, and may hinder intelligence agencies globally,  so if we release it, it may have follow on effects outside Monero, 

What is our official stance on countering airgap vulnerabilities used by the intelligence agencies?

Regards,
MC

# Discussion History
## SChernykh | 2018-10-17T08:32:19+00:00
Can you clarify a bit for non "pro-hackers"? What's an airgap vulnerability?

## anonimal | 2018-10-17T08:41:25+00:00
>Reporter doesn't bother to read https://github.com/monero-project/monero#vulnerability-response
>Reporter doesn't bother to send an email and instead posts to github
>No citations
>No links
>FUD or doesn't know any better

@MoneroChan if you see something, say something - responsibly: https://github.com/monero-project/monero#vulnerability-response.

The types of questions you asked here are welcome there as well. When you use the proper channels, you'll also learn if a claim is endemic to monero or simply a well-known crypto-agnostic problem. If not, posts like this end up looking like low quality bait.

## moneromooo-monero | 2018-10-17T09:36:13+00:00
I'm going to be charitable and not close this outright in case there's an actual report somewhere that just needs explaining.

## MoneroChan | 2018-10-17T17:24:22+00:00
Hi @anonimal , yea i read the response guide but I just wanted to check whether we are even willing to patch airgap vulnerabilities before i submit. (hence the last sentence in my OP.)

Easier to ask here then disturb fluffy.
If Yes; i'll take the time to submit details and workaround fix.
If No; i won't waste my time and  @moneromooo-monero can delete this issue.

Cheers,

## moneromooo-monero | 2018-10-17T17:29:52+00:00
This is a bug tracker. You report bugs here. If we don't want to patch it, we close (or we wait till we do). Asking whether we want to fix a bug without telling us what the bug is is useless.

## MoneroChan | 2018-10-18T01:20:21+00:00
Hi @anonimal @moneromooo-monero
@SChernykh : The Airgap vulnerabilities, a.k.a, design flaws in the current user interface that 'allow by default', compromising electronic emissions and therefore, potential theft of keys and seeds from GUI, CLI, MyMonero website, PaperWallets, (even those created on clean computers without any spyware malware.)
This is very different branch from normal vulnerabilities,  
Hence I thought i'd ask if it's our stance to leave this area of security to users individual OpSec? Or if we're willing to Modify the GUI to mitigate?

## moneromooo-monero | 2018-10-18T08:35:15+00:00
It's like everything. It depends on how bad it is, how invasive the patches are, how effective they would be, whether that's under our control, etc.
Side channel defense is really hard, so I wouldn't expect we're able to defend against a lot of those in the first place, but we can certainly harden stuff where the gain/work ratio seems good enough.


## MoneroChan | 2018-10-18T13:56:12+00:00
Re: 
>  “It’s like Everything” @moneromooo-monero
Yes, i guess we have to start somewhere. 
In that case, can we start with patching the wallet creation screen vulnerability as follows: 
( The temporary fix/workaround is available below.)
_______________________

**CURRENT: Vulnerable CLI/GUI/www.MyMonero.com initial wallet creation process**


Step 1. [Create a new wallet] 
Step 2. [Mnemonic Seed Displayed on screen instantly*] 


_*At this point, the wallet and all funds in it are compromised to attackers doing emissions sniffing._

____________________________

**PROPOSED PATCH: Secure CLI/GUI/MyMonero initial wallet creation process**


Step 1. [Create a new wallet] 
Step 2. [Mnemonic Seed Creation options screen]

Display this message onscreen:

	"WARNING:  Mnemonic seeds can be stolen via electronic emissions recording hardware 
	(e.g TempestSDR) and powerline mesh antennas designed to reliably capture and reconstruct 
	computer, keyboard, and monitor cable emissions from a distance, resulting in the theft 
	of your entire wallet, even if your computer is not connected to the internet (air gapped) 
	and is 100% free from viruses and malware."	

Please select the option suited to your current security arrangements:

	     1. Do Not generate or display a Mnemonic seed.
		(Use password encrypted wallet and keys only)

	     2. Generate Mnemonic Seed directly to a file for permanent offline cold storage. 
		 (For Non-Tempest secure systems, or if visual and emissions espionage is suspected.
		 *export as a JPG image/encrypted/regular txt file. Do not display seed on screen)

	     3. Display Mnemonic Seed on screen.
   		 (Recommended only for low value wallets or on Tempest secured systems)


------------------

**Workaround/Temporary fix for GUI/CLI v11-v13:**
Use taskmgr.exe > Menu bar > 'always on top' function of to obfuscate the seed in the current during wallet creation, so the the mnemonic seed doesn't get emissions leaked, then copy/paste seed out elsewhere, or, discard if desired. Personally i don't keep the seed as it's a liability.

**Fix for compromised wallets:**
Paranoid people can create a new offline cold sign / paper wallet with said workaround and move funds into it with low Tx fee thanks to bulletproofs going live today.

**Wallets Affected:** 
Varies / subjective. This attack has been around long before bitcoin. Arguably most wallets created without Hardware wallet implementations may have be compromised, including bitcoin, ethereum etc... (unlikely, but Monero is the #1 privacy coin for paranoid people.)

Maybe this will help @fluffypony with people complain their funds were stolen from Mymonero.com

If this could be fixed first, we'll go on to the next one.

Thanks for your great work as always. @anonimal  @SChernykh @moneromooo-monero @fluffypony

MC

## moneromooo-monero | 2018-10-18T14:03:58+00:00
You should have said in was about van Eck phreaking from the start :D 
I'd be totally fine not displaying the seed by default. It's a good idea.

## moneromooo-monero | 2018-10-18T14:07:38+00:00
In fact, a "paranoid-display" setting in simplewallet would be nice. People can turn it off if they like.

## MoneroChan | 2018-10-18T14:55:32+00:00
Yes, i use "van eck phreaking" for analog issues , and "tempest/airgap/ELINT" for digital, 
I guess we'll have to wait and see if devs even have time to fix this issue before going further.
I mean, when the seed is compromised at the very beginning, it's practically game over for everything else.  :-/

## moneromooo-monero | 2018-10-18T14:59:43+00:00
You know, why care about this when you're running on a compromised CPU anyway ? I mean, it's game over already before you even run monero, right ?

## hyc | 2018-10-18T15:06:45+00:00
Agreed. Also, simply choosing not to display the seed doesn't protect against such an attack. The radio EMI from your CPU when it's generating a wallet can be picked up and decoded too.

## MoneroChan | 2018-10-18T15:10:15+00:00
and all the compromised the GPU's. nVidia bios fakes on eBay. and dodgy firmware infecting in your MB . Everything is infected. Trust nothing ..... Except the laws of physics and a solid steel box. :)

## moneromooo-monero | 2018-10-18T15:15:15+00:00
You have more trust in steel boxes than you probably should.

## moneromooo-monero | 2018-10-18T15:23:28+00:00
Thanks for letting us know in advance, we're stlil in 2018 here, so it's really GREAT to know that all other easier ways to compromise a monero wallet will be eradicated within a year or so.


## fluffypony | 2018-10-18T15:26:57+00:00
> Maybe this will help @fluffypony with people complain their funds were stolen from Mymonero.com

Literally nobody that gets their funds stolen is getting shoulder-surfed (or pwned via van Eck phreaking or some other side channel) during account creation. They invariably store their seed in plain text in a shared folder on Dropbox, or (far more commonly) they've just logged in to a phishing site.

<img width="865" alt="screenshot 2018-10-18 at 5 22 27 pm" src="https://user-images.githubusercontent.com/1944293/47165746-f5112a80-d2fa-11e8-8be9-99af5a44e7cf.png">

## SamsungGalaxyPlayer | 2018-10-18T15:48:19+00:00
Is there a desire to make a new account in a compromised location? imo, simply telling people sensitive data is about to be displayed is enough.

The default should absolutely encourage backups as well as we can. The MyMonero desktop client does a great job here.

## MoneroChan | 2018-10-18T16:37:41+00:00
@hyc , Hi, Yes we can go way deeper than that

Basically part of this github proposal, is to put a warning message, on one of the first screens a new user sees to give them an example of the risks invovled.  
They can figure the rest based on the initial warning,

 I think the Mnemonic seed makes a good starting point.

Ignoring this entire category of vulnerabilities is one of the outcomes i suspected would happen in my first post, so whether we go further is less concerning to me.  

But this Is Monero, the #1 privacy coin.  I'll let the dev's decide.

## fluffypony | 2018-10-18T16:39:01+00:00
I think a warning that sensitive data is about to be displayed is a good idea.

## moneromooo-monero | 2018-10-21T14:03:26+00:00
Can you rename this to something sensible/intelligible please, like "do not display secret information on screen", etc.

# Action History
- Created by: MoneroChan | 2018-10-17T03:04:30+00:00
