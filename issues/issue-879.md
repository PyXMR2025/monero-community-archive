---
title: Deprecating hardware@getmonero.org
source_url: https://github.com/monero-project/meta/issues/879
author: SamsungGalaxyPlayer
assignees: []
labels: []
created_at: '2023-08-15T02:33:32+00:00'
updated_at: '2026-02-05T09:21:58+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
It doesn't seem like there's an important reason for the hardware@getmonero.org email to exist, and there's a possibility that the continued use of this email may cause confusion about the "official" nature of the workgroup and any related entities.

My recommendation is that, unless there's a good reason to keep it, this email address/group can be deprecated until it's needed again.

# Discussion History
## plowsof | 2023-08-15T08:18:18+00:00
https://repo.getmonero.org/monero-project/ccs-proposals/-/issues/69

## plowsof | 2023-08-17T08:46:09+00:00
Maybe we should get a list of all email handles @ getmonero , e.g. some others can be seen here* https://lists.autistici.org/message/20200712.204247.39cd8386.en.html micheal@ 

## plowsof | 2023-08-20T20:49:17+00:00
```
15:54:07 <m-relay> <p​lowsof:matrix.org> now moving on to the "deprecate hardware⊙go" email issue , have you followed any of the concerns or want to respond msvb-lab?
15:54:44 <m-relay> <p​lowsof:matrix.org> i personally would like it to be deprecated asap, and also question why you have a personal getmonero account , reserved only for members of core / high status
15:55:17 <m-relay> <m​ichael:monero.social> I just gave a Monero Hardware and Kastelo report using IRC. If you missed it due to technology flaws in bridging, please get an IRC log for #monero-community.
15:55:29 <m-relay> <p​lowsof:matrix.org> michael⊙go  belongs to you correct?
15:55:49 <msvb-lab> Yes, that's an email address that I use. Since about four or five years.
15:57:10 <msvb-lab> I don't have any information about deprecating email addresses, so there is no information from me.
15:57:10 <msvb-lab> Is there a proposal to deprecate all (email, IRC, matrix, Mattermost, mailing list...) our channels or only the one email address?
15:57:35 <msvb-lab> And what does deprecate mean, if the proposal succeeds will there be any damage or destruction to our communication systems?
15:57:53 <m-relay> <c​trej:matrix.org> https://github.com/monero-project/meta/issues/879
15:57:58 <m-relay> <p​lowsof:matrix.org> simply disable the email address
15:58:24 <m-relay> <p​lowsof:matrix.org> or have some transparency (which we have none at the moment)
15:58:27 <msvb-lab> I can't defend the email address from disablement, damage, or destruction. But I can defend all the other communication methods from being disabled.
15:58:38 <msvb-lab> Because I'm not the administrator for the email in question.
15:58:48 <msvb-lab> I just answer it, on a weekly basis.
16:01:24 <m-relay> <p​lowsof:matrix.org> people can look into the email issue if they wish in their free time (events also) - we have reached the hour , thank you all for attending
16:01:31 <msvb-lab> All the email fraud is happening on the mailing list (monero-hardware⊙lgo rather than hardware⊙go) so it seems a bit absurd to try to destroy the one that is clean and productive. Not sure what advantage we are seeking here.
16:01:43 <m-relay> <p​lowsof:matrix.org> events meeting is in 1 hour
16:01:45 <msvb-lab> Okay plowsof, dankon everyone for a good meeting.
```

midipoet provided some feedback on the issue stating that there are 2 separate issues here. "misuse" of an email, and who gets an email (e.g. sarang / sarae are no longer with the project anymore). 

Do we need to list all active getmonero email handles with their role in the project to avoid confusion / let people decide if personalised emails are needed? All the infra is sponsored by the community so what level of transparency are we entitled to? 

## SamsungGalaxyPlayer | 2023-08-21T14:56:02+00:00
I recommend against expanding the scope of this issue to all @getmonero.org emails; please focus on this specific one here.

## umma08 | 2023-08-23T08:20:56+00:00
If there is work being done on Monero related hardware design and development, would it not make sense to keep all these communications within/from one dedicated email address? 

That way, if the design and development work needed to be passed on, so could all the email/contact history?

## dan-is-not-the-man | 2023-08-23T09:12:00+00:00
1. Personally i think msvb should have his access removed from hardware@getmonero.org for clearly miss using it, even though the community rejected the defcon proposal and also disclose all the correspondence between defcon and hardware@getmonero email for transparency reasons and not "depreciated the email" to hide the miss use.

2. In terms of emails i think we should keep "hardware@getmonero.org" and only allow specific non personal named emails ie "michael@getmonero.org" and have a public email contact directory on  getmonero with these emailsie "outreach@getmonero.org". If this is meant to be a community/open project its reasonable to expect that it is open and transparent.
![ima_a59e303(1)](https://github.com/monero-project/meta/assets/142721047/63159ad5-8a8d-417e-92f2-a9c902be7ffa)


## nahuhh | 2023-08-23T09:55:56+00:00
> I recommend against expanding the scope of this issue to all @getmonero.org emails; please focus on this specific one here.

I recommend against narrowing this issue to focus on one specific incident/email; please focus on the elephants in the room, not just the pink one.

## nahuhh | 2023-08-23T10:30:42+00:00
> If there is work being done on Monero related hardware design and development 
> 

there is not.

> needed to be passed on, so could all the email/contact history?

They should be, as these at least 2 of these emails are being misused.

## michaesc | 2023-08-31T22:01:39+00:00
This comment relates to only the hardware@getmonero.org email address, and does not relate to messages from agents not connecting to the MX.

Q-1: Is the resource active and used regularly for its intended purpose?
A-1: Yes.

Q-2: Has the email ever originated a SMTP transaction (without a In-Reply-To header) aside from test (for maintenance) messages?
A1-2: No.
A2-2: This means that all UCE, spam, abuse, and irrelevant emails are sent by fraudulant parties. We have no reports that this has ever happened, which is impressive. Please use SPF and DKIM.

Q-3: Do we reply to all messages?
A-3: No, we only reply to messages with relevance to (1) Monero, (2) cryptosecure electronics, (3) nonelectronic hardware, or related topics like journalist requests or meetings hosting 1, 2, or 3.

A-4: Are we following a rigid ruleset?
Q-4: No, so if mining questions are received we answer them.

Q-5: Why is it printed on hardware user manuals distributed at Monero events?
A-5: See A-3.

Q-6: Why isn't this printed on other user manuals?
A-6: It's not appropriate on hardware at HiP and other CCC events where Monero is not welcome, so instead an CCC email is printed there. The original hardware design of the Konferenco badge (as indicated in the user manual) is derived from a CCC design.

Q-7: Is there any fraud or commercial activity?
A-7: Yes, today we received the offer 'BOOST Sales, 1 million emails = $1000'

Q-8: How much fraud is on this semiprivate (point to point) resource compared to our public mailing list monero-hardware@lists.getmonero.org?
A1-8: About 10% of the fraud reaches us on this resource, 90% on the list.
A2-8: Like with all our resources (IRC, Matrix, private email, public list, Mattermost, Github) we remove (if possible) fraudulant or very off topic content during maintainance.

Q-9: How do we deal with commercial requests that are made in good faith?
A-9: If it's Monero related or hardware relevant, we reply 'sorry, commerce is not offered.'

Q-10: Has any request for information been made?
A-10: Yes, one on a private channel that was recently made and answered. One vague question inviting a response to the destruction efforts was made during a community meeting, with the answer 'I cant defend the email address from disablement, damage, or destruction.'

Q-11: Is this a constructive or destructive proposal?
A-11: Destructive.

Q-12: Would the Monero community lose, if destroying this resource?
A1-12: Yes, but the loss would likely be minimal if we're lucky or moderate if not. It's unclear which party would gain or win after the destruction.
A2-12: If destroyed, the result might resemble in nature, our recent loss of outreach.getmonero.org.

Q-13: What is the efficiency level?
A-13: 100%. We have never refused or failed to answer any (see A-3) message.

Q-14: How long has the resource served hardware enthusiasts inside and outside the Monero community?
A-14: About five years.

B - Monero community members in good standing
C - Monero community members in good standing with hardware engineering experience
D - Monero core members
E - getmonero.org
Q-15: Why is the resource administered by B, content managed by C, paid by D, and hosted on E?
A-15: To maintain a moderate to high level of tranparency for the Monero community. We could easily change B/C/D/E if we didn't care about the ability to get truthful information without revealing private information.

A-16: Is there any stated primary purpose?
A-16: Yes, our public mailing list states 'Discussion of Monero open hardware projects' and this private resource has the same primary purpose.

Q-17: How can information be obtained?
A1-17: By asking on the workgroup's IRC channel. Or by attending community meetings, putting hardware on the agenda, and inviting a workgroup member. This already happens regularly with low frequency.
A2-17: Next time you want information, please ask during a meeting. Making a request on Github to damage or destroy this resource gives the false impression of an under handed attack on community resources. I assume the real reason for this request is curiosity by an uninformed community member.

Q-18: Has there been abuse, fraud, or deceit using ideas in this bug report as an excuse?
A-18: Yes.

## dan-is-not-the-man | 2023-12-18T07:44:15+00:00
BUMP .........So whats the go, emails getting shown?

## plowsof | 2026-02-05T09:21:58+00:00
Removed from workgroups page in https://github.com/monero-project/monero-site/pull/2259 

Time to deprecate the email handle until such time the workgroup is active and the community calls for it.

# Action History
- Created by: SamsungGalaxyPlayer | 2023-08-15T02:33:32+00:00
