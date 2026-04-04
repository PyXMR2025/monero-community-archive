---
title: 'Vote: Luigi to continue as CCS escrow'
source_url: https://github.com/monero-project/meta/issues/935
author: plowsof
assignees: []
labels: []
created_at: '2023-11-25T16:01:01+00:00'
updated_at: '2023-12-23T17:02:16+00:00'
type: issue
status: closed
closed_at: '2023-12-23T17:02:16+00:00'
---

# Original Description
Yes / No / Maybe . Further details/caveats to your answer (especially Maybe) is much appreciated.

leaving this open until 2nd December , should be enough time to gather enough opinions.

# Discussion History
## michaesc | 2023-11-25T16:05:54+00:00
Yes, because Luigi has generously offered to do it, is well trusted, did a good job before (despite the theft), and is the least complex option we have.

## umma08 | 2023-11-25T18:19:08+00:00
No. 

The previous setup has been proven to contain an exploitable vulnerability and/or has been directly targeted by an attacker.

As we have no more concrete information, the only way to mitigate the vulnerability is to remove the set-up from the CCS process, including those that were responsible/in control of the set-up (i.e., Luigi and Fluffypony). 

## selsta | 2023-11-25T18:22:54+00:00
I'm in favour of luigi continuing together with changing how the wallets are setup to either a hardware wallet or a proper cold wallet. Also we should make sure that large funds don't accumulate again in the CCS.

## ajs-xmr | 2023-11-26T09:17:56+00:00
No, not because of Luigi, he has been asset to the community and am very grateful for his contributions over the years, but because the CCS escrow system itself is broken. 

The Monero project has grown since the early days of the FFS (the predecessor of the CCS). We need to move away from overly centralized systems and reliance on the core team. Although returning to the status quo would be familiar and easy, we should instead take this opportunity to explore other mechanisms such as direct funding of contributors with well-defined milestones reviewed by the community before moving to the funding required stage on a "per milestone basis" and/or multisig escrow with rotating elected community members as signers.

## erciccione | 2023-11-26T10:09:50+00:00
@plowsof @luigi1111 Could we have some details on this? Seems to me like it's an important vote (assuming voting here has practical weight), so would be good to have more details than a one line request for vote on github.

like:

What does the escrow entail? Is it the same structure of before?
Does this assume the way wallets are managed will be changed? How?

I agree with @selsta, but more transparency and clarity on what is going on is needed. in general i'd prefer a better system, where only the votes or actual contributors matter. One of the problems of the ccs is socketpuppet accounts commenting and voting on proposal to stir sentiment according to the agenda of the puppet master.

## umma08 | 2023-11-26T13:51:45+00:00
> What does the escrow entail? Is it the same structure of before? Does this assume the way wallets are managed will be changed? How?

I think it's fair to assume the methodology for securing wallets/keys will change/improve. Exactly how would be decided after the vote. 

> One of the problems of the ccs is socketpuppet accounts commenting and voting on proposal to stir sentiment according to the agenda of the puppet master.

As always, we can assume that trusted community member votes hold more weight than new/unknown accounts. 



## hinto-janai | 2023-11-26T14:09:00+00:00
All of the plans proposed over the last few weeks have clear benefits over the current situation, however, they build on the assumption that the work to implement them is already done, will be done, and/or assumes other people will do it - not just the initial fix but afterwards as well, more work is assumed to be done by all future contributors and community members.

There's also a time constraint here - the CCS can't be in maintenance for an unknown extended amount of time without a clear plan and people dedicated to putting in work to fix it, thus returning to @luigi1111 (with proper security measures) is the most practical (but not ideal) solution.

## erciccione | 2023-11-26T14:41:10+00:00
Can we have an overview of what the proposals are for people who don't follow whatever channel was used to discuss this?

Please let's remember Monero is a very sensitive tool and any change should be treated as a change to a project somebody's life might depends on. This is an incredibly important discussion, since it effects directly the way people working on the project are funded, but what i'm seeing right now is mostly chaos.

That said, the ccs cannot be stopped from one day to another without creating major disruptions to Monero itself. I haven't seen an immediate alternative proposed, so i don't think there are many other choices than keep going with the current system in the immediate future, while working on an alternative and ideally, a full restructure of the Monero project and core team.

## DouglasMcSqueaky | 2023-11-28T22:20:29+00:00
Maybe. Luigi could be involved in the set up, but to be solely responsible is a single point of failure. Federated responsibility among multiple parties. Incorporate multi signature.

## plowsof | 2023-11-29T09:09:27+00:00
@erciccione just to clarify the "yes/no/maybe" and give some examples. This vote was proposed originally as a vote of confidence for luigi being involved (with whatever methods would be used) in escrowing CCS funds e.g. 
- Yes: i am confident luigi has learned from any mistakes made. funds will be secured moving forward. I have faith in Core choosing the appropriate methods (whatever they end up being).
- No: we do not know if or how luigi was targeted and the threat may persist / happen again, someone else has to take over his role.
- Maybe: luigi can be involved in escrowing CCS funds ONLY if [proposed method is used], otherwise, no.

In terms of what are the proposed methods, i can try to summarise or at least provide examples:
- luigi to escrow as usual. transactions are made offline via optical data transfer OR hardware wallets (definitely 'more secure' than the original setup and would prevent any online threats) 
    - does community/luigi want to do this? because the threat is unknown, will he be safe in the meatspace/physical world?
- bulk of funds in a multisig wallet sent out to a another wallet for convenient payouts (would luigi still escrwo the smaller wallet?)
    - is multisig known secure? no (MRL have discussed the steps how to get it secured...which will take several+ months imo, and require funding), is it convenient? no (UX is being worked on by tobtoht/jeffro256 as we speak)
- direct funding (either a buddy system or directly to the proposer)
    - the CCS is an escrow system thus would cease to exist in my view

## nahuhh | 2023-11-29T14:36:58+00:00
No. 

long:
if we were an org, the question wouldn't be on the table. Lack of communication was negligent. It would be a legal matter. He chose not to go the legal route after a massive theft from his person, and also neglected to notify community whitehats in anything remotely close to a timely manner.

Someone with such an intentionally lax commitment to a specific duty should not be reinstated for that same duty.

he leaves the devices unattended for long period of time. 
Example from after the hack, when moneroseedisigner asked about forensics: 

> nov 7 <l​uigi1111> I would appreciate that. Small caveat I won't have access until after Thanksgiving

tldr: lmao. No.

## vtnerd | 2023-11-29T20:20:49+00:00
This needs to get moved along; we've got quite the backlog in CCS proposals now. I'm seeing a lot of support (based on thumbs up) to keeping @luigi1111 as the escrow service, provided he takes some action (hardware wallet or cold wallet). And I'm seeing never-before-seen accounts suggest otherwise. Maybe some of these new accounts represent anonymous funders, tough to tell.

 > is multisig known secure? no (MRL have discussed the steps how to get it secured...which will take several+ months imo, and require funding), is it convenient? no (UX is being worked on by tobtoht/jeffro256 as we speak)

I think this is the biggest issue. The multisig implementation has one outstanding bug (as mentioned by @kayabanerve in #monero-research-lab) that "burns" funds (when leader is evil/hacked). And fixing the bug (and even switching to monero-serai) will take weeks/months. Meanwhile, the CCS is backlogged with contributors that use the funds like a salary.

Do we have @luigi1111 use hardware/cold wallet while we work diligently to improve multisig?

## vtnerd | 2023-11-29T20:22:33+00:00
I just re-read the first post, waiting until December 2nd, seems reasonable. But the rest of my post remains clear - getting multisig out of experimental is going to be a long ways out.

## kayabaNerve | 2023-11-30T03:38:35+00:00
@vtnerd That bug is not outstanding and was fixed before we shipped it as experimental. I found it while reviewing the multisig rewrite PR. My point was to highlight why the experimental label is justified, as the multisig had yet another issue found while the PR which was supposed to fix the issues was under review. I apologize for any confusion I caused.

## ridolfox | 2023-11-30T16:17:25+00:00
No. my vote is to dissolve CCS, only funding campaigns per project

## hyc | 2023-11-30T17:02:14+00:00
> No. I propose to dissolve the CCS

Suggestions like this should be summarily ignored. All that does is move the problem from a single systematic approach to bunch of separate ad hoc ones. No, just no.

An intermediary is needed because payouts can't be automatic - reviews of milestones must be performed before payouts can be approved. It would be stupid to recreate the intermediary on a case by case basis, redundant work. Extra work. 

## archerships | 2023-12-01T05:30:25+00:00
Nothing against Luigi, but it seems to me that the theft was a wakeup call to move to a more secure process.  I would recommend that we put a call out for proposals for a more secure pooled funding mechanism. 

## MoneroArbo | 2023-12-01T11:46:42+00:00
> Nothing against Luigi, but it seems to me that the theft was a wakeup call to move to a more secure process. I would recommend that we put a call out for proposals for a more secure pooled funding mechanism.

Okay but what do we do in the meantime? I think that's more the issue at hand.

I guess my question is, do we really not have anyone else, even on a temporary basis? I had suggested myself as a half joke, but in all seriousness there's a number of people in this very thread I'd be okay with having the job.

And although we don't have trusty multisig for the moment, if we come up with a short list of people, we can spread the funds between multiple people, so 1) each person only has access to a portion of the funds and 2) it'll be obvious who stole / lost the money. It's better than nothing, right?

Luigi I love you brother, but guys, let's please have some more imagination.

## trasherdk | 2023-12-01T12:45:56+00:00
**Yes** => I'm okay with Luigi, if he can set up a *secure* environment.

## rbrunner7 | 2023-12-01T14:01:12+00:00
I have troubles to form a clear opinion.

On the one hand, I for one still trust Luigi and see no reason for them to *not* continue to manage CCS funds on personal grounds.

On the other hand, as far as I learned until today, it's still unknown what happened, and that makes me really nervous and unsure. From a security perspective I think it could be dangerous if Luigi goes back to handling funds. Even with considerably better security. I see possible repeat scenarious, mostly in the direction of "evil maid" where somebody personally close to Luigi made a theft, and which might be able to overcome even better security simply because being near everything, and maybe still trusted.

Still, for lack of better candidates, it may still be the least bad choice to let Luigi handle funds again, under a new and better security regime, assuming that they are ready to do so of course.


## sanderfoobar | 2023-12-02T14:10:37+00:00
![](https://i.imgur.com/VodMlOz.jpg)

I vote Yes, please keep luigi around to manage the CCS :P

## Rucknium | 2023-12-02T15:01:48+00:00
My vote is "maybe" if there is no alternative. Monero R&D funding must continue.

I thank luigi for being honest about how CCS funds were managed. We now know that the funds were managed carelessly. It is foolish to put funds back into the hands of someone with poor judgement. It is more foolish to end the CCS. Sometimes the least bad alternative must be chosen.

ArticMine would be a better escrow agent since [he has considered and implemented strong OpSec in management of his own funds](https://piped.video/9XgG4sNVS38).

## scottAnselmo | 2023-12-02T15:36:31+00:00
Luigi has enough good will and we don't have clear root cause, so we have no guarantees the same thing won't happen to another person as escrow. So in the interest of operations continuity I'd vote yes and focus on making sure there's better procedures in place to mitigate this from happening again.

## satonotdead | 2023-12-03T02:28:49+00:00
> No.
> 
> The previous setup has been proven to contain an exploitable vulnerability and/or has been directly targeted by an attacker.
> 
> As we have no more concrete information, the only way to mitigate the vulnerability is to remove the set-up from the CCS process, including those that were responsible/in control of the set-up (i.e., Luigi and Fluffypony).

I'm agree with this comment with a solid NO.

It's not about any personal with luigi or fluffy but related to public known facts and common sense.

## jeffro256 | 2023-12-03T04:43:21+00:00
This is not personal towards Luigi, but I must voice my opposition to allowing Luigi to custody funds solely from here on out. We had made the assumption that Luigi, a pseudonymous contributor, would be able to securely control funds. This assumption has turned out to be false. We have no forensic evidence that would point us to a cause of the loss of funds. As such, even assuming that Luigi has nothing but the best of intentions, it would be a security misstep to assume that Luigi, from an OPSEC point of view, isn't still compromised.

In the long run, the CCS should do multisig among trusted community members to custody funds. If we must have a solution NOW, then we should leverage the legal system against an already doxxed member of the community. Allowing a public member of the community. preferably a citizen of a western country, to custody funds would allow the public to hold that member legally accountable for lost funds, as well as audit the security of their setup without additional loss of their privacy. 



## selsta | 2023-12-03T04:48:50+00:00
> If we must have a solution NOW, then we should leverage the legal system against an already doxxed member of the community. Allowing a public member of the community. preferably a citizen of a western country, to custody funds would allow the public to hold that member legally accountable for lost funds, as well as audit the security of their setup without additional loss of their privacy.

Who exactly steps up for this? Who wants to make themselves legally liable in addition to all other risks and work that come with managing these funds?

## jeffro256 | 2023-12-03T06:01:12+00:00
It's a lot of responsibility, which is the point. I'd be willing to do it if it wasn't a conflict of interest for me, since I benefit from the fund. We should make the bar high, since we can see what happens when we don't. 

## rbrunner7 | 2023-12-03T10:28:48+00:00
> It's a lot of responsibility, which is the point.

Good luck finding a judge, in case of loss because of an attack or exploit, that could decide whether you did due diligence and were just overpowered, so you go with a slap on the wrist, or whether you were negligent and go to jail for loss of large funds in custody.

Yeah, the judges in Western countries are totally known for groking crypocurrencies and their technologies, especially if they are as advanced as Monero's. I am confident to get a fair trial.

/s

## woodser | 2023-12-03T18:59:37+00:00
Yes, with a multisig wallet for escrow.

## jeffro256 | 2023-12-03T19:57:30+00:00
> Yeah, the judges in Western countries are totally known for groking crypocurrencies and their technologies, especially if they are as advanced as Monero's. I am confident to get a fair trial.

Would you prefer that the sole custodian of the CCS funds has zero accountability?

> I'm in favour of luigi continuing together with changing how the wallets are setup to either a hardware wallet or a proper cold wallet. 

The problem with doing this, as Luigi is a pseudonymous contributor, is that we can't actually verify that he follows the setup initially and continues to follow it. 

All in all, I think we should skip these "temporary" solutions and jump right into the correct solution, which is multisig, since I think that we might find that the "temporary" solution will tend to be not so temporary in practice. For the record, I'm not opposed to Luigi having 1 share of a multisig wallet such that the threshold (not total number of signers) is greater than or equal to, say, 3. I think the risk of a member exploiting a multisig zero-day exploit is less than the much more mundane risk of handing control of funds to a single entity. We should put into place emergency procedures if an exploit is discovered. Namely, we should designate one of the signers as an emergency custodian. If a multisig exploit is discovered, then signers should be made aware that the funds should be transferred ASAP to that emergency custodian, even before they know what the exploit is. 

I also agree with @selsta's point that the CCS generally shoudn't be handling as much funds as it was. I think the easiest way to do this would be to expire old proposals where the benefactor is MIA and hasn't had any updates in a while, and move those funds to new proposals automatically.


## 0xFFFC0000 | 2023-12-03T20:33:23+00:00
This **multisig discussion is not applicable at the time being**. As we discussed in the meeting, the multisig is not ready yet, and it might take a while to have the multisig ready.

So all the votes (mine included) that state “Yes, with multisig wallet” is just not applicable at this point. 

## woodser | 2023-12-03T20:41:18+00:00
> So all the votes (mine included) that states “Yes, with multisig wallet” is just not applicable at this point.

Then yes, until multisig is ready.

## tobtoht | 2023-12-03T23:00:51+00:00
Another vote for Luigi now, multisig when ready.

>to expire old proposals ... and move those funds to new proposals automatically.

Yes.

## dylan-sh | 2023-12-04T00:18:57+00:00
No.

> Yes, because Luigi has generously offered to do it, is well trusted, did a good job before (despite the theft), and is the least complex option we have.

Well yeah, everyone does a good job before all the money is gone lol.

Keeping Luigi is the biggest misstep we could have opsec wise. Clearly there was a failure somewhere, so keeping one of the potential causes of the failure simply because we can't pin down the exact cause is foolish at best and malicious at worst. 

Just hand the keys to another trusted member of the community, literally anyone would be better than someone who has already fumbled the funds. Whether it was intentional or unintentional is regardless, and a failure to secure something the community has entrusted you with is a failure full stop.

I thank Luigi for all that he's done for the community over the years, but I have no faith in a CCS that fails to expel any potential security flaws. Maybe multisig when that's ready.

## Final-Phoenix | 2023-12-04T00:32:57+00:00
No. 

Nothing personal but I don't think Luigi should continue as CCS escrow when we still don't know the full details of what happened and why. Whatever he is using could still be unknowingly compromised.

Order of preference:
1) Direct Community Funding (how this could work: https://monero.observer/cypherpunk-transmission-017-rethinking-monero-ccs-cypherpunk-proposal)
2) Multisig (not ready)
3) Escrow split up between several trusted members (if that has to include Luigi so be it)
4) Luigi

If Luigi ends up being escrow again out of necessity/practical reasons, then we should *AT LEAST* have concrete timelines setup for the public for the discussion of new options and when and how they'll be implemented.

Let's not get comfortable and leave this up in the air again...that's why we ended up in this situation to begin with.

## stanfieldr | 2023-12-04T01:47:23+00:00
This may be naive of me not knowing the internals, but since multisig isn't here, why can't we just generate & split a new seed phrase between multiple people in a docker container running in a pipeline for each funding event? When it's time to withdrawl, the seed holders come together to make a valid seed phrase and make a distribution of the funds and the wallet is abandoned. Repeat the process for new funding events.

## kayabaNerve | 2023-12-04T07:01:27+00:00
I'd fully advocate a multisig of trusted community members for use here *despite the experimental label*.

## luigi1111 | 2023-12-05T15:43:13+00:00
This problem isn't easy to solve, and any long term solution will seemingly take a signifcant amount of time to refine and integrate. Meanwhile we have a backlog of devs and other proposals that are stuck in limbo.

**Proposal**

Objective: continuity while discussion and long term solutions are implemented

Summary: Luigi escrows until March 1, 2024. Long term solutions are discussed and implemented then (or sooner if possible).

The Setup:
- single purpose laptop
- open to suggestions on OS choice
- never online after initial setup; powered off when not in use
- encrypted drive with strong password
- encrypted Feather wallet with separate strong password
- transactions via QR code (laptop camera)
- seed split in half and held in separate secure locations (both away from laptop)

**This can be up and running this week.**

For a longer term solution, I do think a community multisig could work (ideally non-experimental, of course). There are several names (long term Monero supporters) that come to mind that could be good choices for signers (Luigi would prefer not to be one). They could perhaps function as a sort of "CCS Board" as well. Of course, also open to other ideas.

## kayabaNerve | 2023-12-05T16:15:11+00:00
Qubes ideally, Debian minimal otherwise would be my suggestions for OS.

## Rucknium | 2023-12-05T17:31:45+00:00
(Not an expert on this) I suggest using physical dice as _supplemental_ entropy for generating the wallet seed. The original CCS wallet was generated on Qubes. We still do not know the cause of the theft of that wallet. Virtual Machines OSes like Qubes can produce insufficient entropy. @kayabaNerve can suggest how to use dice as supplemental entropy.

## kayabaNerve | 2023-12-05T17:45:09+00:00
I don't share Rucknium's views.

I could write a trivial Rust script, yet that would require installing the Rust toolchain and all that entails. Accordingly, here's a few Linux commands to generate a 32-byte effectively random value, incorporating misc entropy.

```sh
head -c 32 /dev/urandom >> ./entropy
 echo 4 >> ./entropy # Random number chosen by fair dice roll
sha256sum ./entropy
shred ./entropy
```

Please note the leading space before the `echo` so it doesn't become part of the history. Also please note this uses sha256sum, not sha512sum, which prevents a wide reduction from occurring. While wide reduction's are preferred, tevador has commentary on how they're unnecessary for Ed25519 and the current Monero codebase doesn't use them. Accordingly, the non-usage here is accepted.

What I actually suggest is a nice Trezor or Ledger hardware wallet for use with a reasonably secure laptop (any Linux distro, or even macOS, which you don't pirate video games onto).

## tobtoht | 2023-12-05T18:11:32+00:00
>I suggest using physical dice as supplemental entropy for generating the wallet seed.

`monero-wallet-cli` supports `--extra-entropy <file>`.

The next Feather release can create Polyseeds from entropy collected from dice rolls.

>Virtual Machines OSes like Qubes can produce insufficient entropy

Or have bugs https://github.com/QubesOS/qubes-core-agent-linux/commit/084c08f465476b750fbe40eae1dd10b34565cedf

>shred ./entropy

`shred` [does not work](https://unix.stackexchange.com/a/593340) on SSDs. If you go with this approach you should create an ephemeral encrypted volume with a random key (bit of a dependency issue here), write the file there, and forget the key after use.

## dylan-sh | 2023-12-05T18:18:38+00:00
> Summary: Luigi escrows until March 1, 2024. Long term solutions are discussed and implemented then (or sooner if possible).

I fear this stopgap solution will continue in perpetuity as no one will want to build a better solution when the time comes.

## luigi1111 | 2023-12-05T18:21:13+00:00
> I fear this stopgap solution will continue in perpetuity as no one will want to build a better solution when the time comes.

This is a legitimate concern. The "hard" stop date is to attempt to mitigate this, but will require some vigilance.

## hinto-janai | 2023-12-05T18:34:02+00:00
I suggest using an OS that has many eyes on it (attackers, reviewers, users).

Going against most opinions, I think Windows would be acceptable - the machine is offline after all, although I'd recommend Debian stable (bookworm 13) or Ubuntu LTS (22.04). Even Debian had its infamous [~18-bit entropy](https://lwn.net/Articles/281436/) [OpenSSL fiasco](https://www.debian.org/security/2008/dsa-1571) a while back, so more eyes on the OS matters.

The [QR library](https://github.com/fukuchi/libqrencode) in Debian/Ubuntu is open and battle-tested, so that's a benefit too (I believe Feather [uses it](https://github.com/feather-wallet/feather/blob/e40d4efd54f04c5c0f925f287ae255019ae65e60/HACKING.md?plain=1#L24C1-L24C107) internally).

@kayabaNerve `/dev/random` may be preferred as it always blocks until entropy is good ([1](https://en.wikipedia.org/wiki//dev/random#cite_ref-17), [2](https://unix.stackexchange.com/questions/324209/when-to-use-dev-random-vs-dev-urandom)). Behavior is identical on other Unixes but Linux is special. I would have commented on the `shred` too but @tobtoht beat me :)

## hinto-janai | 2023-12-05T18:40:27+00:00
Err - Debian stable is 12, not 13.

## j-berman | 2023-12-05T19:04:19+00:00
I am personally ok with Luigi custodying funds with the above setup (putting my vote in for Debian) until a stronger alternative is in place, however, I would feel more comfortable with the option to be paid directly.

Suggestion: give contributors the option to be paid directly via the CCS by allowing the choice to submit proposals with their own address and view key. When a proposal is on the "Funding Required" page, display the address alongside a warning (e.g. red text "WARNING: this address is owned by the contributor. Be careful donating, the contributor can run off with the funds without completing any work.").

If other contributors choose this option as well, then it could significantly reduce risk for funds held by the CCS, and it's a relatively simple option that can be put in place in the short-term.

The CCS is a solid system not only for its escrow benefits, but also as a consolidated place to see what can be/has been funded for Monero development, discuss proposals, and gather feedback. Plus it has the infrastructure in place to make it easier on contributors.

## luigi1111 | 2023-12-05T19:22:44+00:00
> Suggestion: give contributors the option to be paid directly via the CCS by allowing the choice to submit proposals with their own address and view key. When a proposal is on the "Funding Required" page, display the address alongside a warning (e.g. red text "WARNING: this address is owned by the contributor. Be careful donating, the contributor can run off with the funds without completing any work.").


This could be done in parallel with other changes, with hopefully only a small amount of dev work and compute resources (to scan the additional viewkey(s)). I would guess some loose restrictions should be in place on who would be eligible to have such proposals.

## Final-Phoenix | 2023-12-05T20:49:30+00:00
> I am personally ok with Luigi custodying funds with the above setup (putting my vote in for Debian) until a stronger alternative is in place, however, I would feel more comfortable with the option to be paid directly.
> 
> Suggestion: give contributors the option to be paid directly via the CCS by allowing the choice to submit proposals with their own address and view key. When a proposal is on the "Funding Required" page, display the address alongside a warning (e.g. red text "WARNING: this address is owned by the contributor. Be careful donating, the contributor can run off with the funds without completing any work.").
> 
> If other contributors choose this option as well, then it could significantly reduce risk for funds held by the CCS, and it's a relatively simple option that can be put in place in the short-term.
> 
> The CCS is a solid system not only for its escrow benefits, but also as a consolidated place to see what can be/has been funded for Monero development, discuss proposals, and gather feedback. Plus it has the infrastructure in place to make it easier on contributors.

I like this.

New proposers with no history would probably find it easier to get funding if they initially went with an escrow, but give them the choice. 
Trusted proposers with some history would likely easily get direct funding from the community.

escapethe3RA goes into details about how direct funding could work in practice here. Worth reading:
https://monero.observer/cypherpunk-transmission-017-rethinking-monero-ccs-cypherpunk-proposal

## plowsof | 2023-12-05T21:58:44+00:00
One of the most important Monero contributors has a funded/work in progress proposal. They are now on an indefinite hiatus from Monero work. Some proposers have simply dissapeared. We've also been scammed for as little as.1.5 xmr. This was all facilitated by the vetting system of our CCS.  It doesn't matter how much/little you trust a contributor. Things happen*, but funds remain in our control with an escrow system to be repurposed/leveraged as the community sees fit.

*Moving forward im confident there will be no thefts 

## Final-Phoenix | 2023-12-06T00:25:02+00:00
Of course. Nothing is guaranteed in either case. 
It doesn't matter how much/little you trust an escrow either.
Things can also happen.
Like 2,675 XMR going missing, months of keeping it hush, and no real idea given yet of what happened.

Direct Funding doesn't preclude vetting. We can still do that. It's the donors decision to heed that vetting.
Proposers should really be given the option to choose escrow or direct funding (in the way escapethe3RA lays out - or a variation)

## nahuhh | 2023-12-06T00:26:49+00:00
People are trying to be polite and not name names

## kayabaNerve | 2023-12-06T09:28:41+00:00
While I don't mind dice rolls as additional randomness, I'll note I do mind them as sole randomness.

Re: random/urandom, I'm fine with the commentary for /dev/random being slightly preferred due to the at-boot concern. /dev/random won't block post-boot (post-RNG-boot, not post-OS-boot) though. It was changed in 5.6 to not do so with the acknowledgement entropy doesn't actually go down upon usage.

## hyc | 2023-12-06T11:30:45+00:00
I would suggest FreeBSD for the laptop OS, because it is more reliable than Windows, is basically the foundation of MacOSX, and is less popular than Linux (i.e., there are already common Linux attacks out there, but most of them will fail on BSD.) And we already have official support for it.

There's no point using a virtual machine on a piece of hardware that is only used for a single purpose. Qubes doesn't offer any advantage in that scenario.

Ledger and Trezor have both proved themselves untrustworthy in different ways. They don't offer any real advantages over an offline / airgapped general purpose computer. Speaking of which - there's no reason it needs to be an x86 laptop. It could just as well be a Pine64, Orange Pi 5, or some other small Arm64 SBC.

## kayabaNerve | 2023-12-06T11:38:29+00:00
@hyc Qubes uses VMs for various parts of the system itself, so even in a single-application environment, it has advantages.

A hardware wallet may fundamentally not have any wireless technology in it. A laptop likely has a soldered WiFi chip.

## hyc | 2023-12-06T13:59:08+00:00
> @hyc Qubes uses VMs for various parts of the system itself, so even in a single-application environment, it has advantages.

> A hardware wallet may fundamentally not have any wireless technology in it. A laptop likely has a soldered WiFi chip.

Cheap SBCs won't necessarily have built in wifi, many of them only support it with add-in cards. It's also pretty simple to build a kernel for any given machine that omits all wifi drivers, so even if the hardware is there it's unusable. Stripping down existing functionality is just not a problem. And don't forget the f#ckery going on with Ledger https://old.reddit.com/r/Monero/comments/14axyn9/ledger_bad_ledger_good/

## nahuhh | 2023-12-06T14:00:21+00:00
I had a change of heart

https://nitter.net/watchfund/status/1732391070216908886

https://x.com/watchfund/status/1732391070216908886

(confirmed?)
@luigi1111 

## 0xFFFC0000 | 2023-12-06T14:30:08+00:00
> I would suggest FreeBSD for the laptop OS, because it is more reliable than Windows, is basically the foundation of MacOSX, and is less popular than Linux (i.e., there are already common Linux attacks out there, but most of them will fail on BSD.) And we already have official support for it.
> 
> 
> 
> There's no point using a virtual machine on a piece of hardware that is only used for a single purpose. Qubes doesn't offer any advantage in that scenario.
> 
> 
> 
> Ledger and Trezor have both proved themselves untrustworthy in different ways. They don't offer any real advantages over an offline / airgapped general purpose computer. Speaking of which - there's no reason it needs to be an x86 laptop. It could just as well be a Pine64, Orange Pi 5, or some other small Arm64 SBC.

Since we are going this route. I would say let's make it OpenBSD. They have proven right again and again in security community to be more reliable than FreeBSD and *nix. For example, in Spectre and Meltdown fiasco IIRC. They disabled hyper-threading from the very moment they heard about it, but in *nix community they were looking for software solutions for a long time. They have custom design for random number generator and proven to be reliable https://youtu.be/aWmLWx8ut20?feature=shared


## hyc | 2023-12-06T14:43:09+00:00
> I would say let's make it OpenBSD

I would agree but we don't have support for it, and certainly no reproducible builds for it.

## luigi1111 | 2023-12-22T05:26:53+00:00
Update:

The wallet has been created as follows:

Secret view key: 62ad19781466882d8df0ae85743abcc5c8ef81e52e051e7cc56fe3c610d18001
Address: 41hzbgqgkrYijnRVBLzr1KHsYc1iUBBCJYeeT9d3eiYE2PhbohxxwJLZCNVbTzvAMkhtYGF3RQcr2Ea187AJn8af149UG1G

Specs are as above.

Given the time elapsed and the time of the year, I propose modifying the target date for a viable alternative to March 31, 2024.

## plowsof | 2023-12-23T17:02:16+00:00
With the new temporary wallet details, this issue can be closed.

# Action History
- Created by: plowsof | 2023-11-25T16:01:01+00:00
- Closed at: 2023-12-23T17:02:16+00:00
