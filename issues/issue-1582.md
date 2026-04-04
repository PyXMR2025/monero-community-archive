---
title: All languages need to be updated for 0.13 - Call for translators
source_url: https://github.com/monero-project/monero-gui/issues/1582
author: erciccione
assignees: []
labels:
- Hacktoberfest
created_at: '2018-10-02T17:30:17+00:00'
updated_at: '2019-05-16T15:57:33+00:00'
type: issue
status: closed
closed_at: '2018-10-15T12:55:19+00:00'
---

# Original Description
Another hard fork is approaching, and with it, a mayor release: 0.13
Since 0.12.3, the GUI changed a bit. Some strings were added and some were removed. #1572 refreshed all language files, so now **they can all be updated with the missing translations**, before 0.13 is out.

**This is a call for translators**, down here can be found the list of the available languages. If the language is thicked, somebody worked on it and the translation is already PRd.

**If you wish to contribute, please make sure your language is still labelled as 'needed' on the [Issue tracker of the Localization Workgroup on Taiga](https://taiga.getmonero.org/project/erciccione-monero-localization/taskboard/test)**. The task related to this issue is "Update strings (0.13)". If the task is 

+ **Needed**: nobody worked on it and still need a translator.
+ **Work in progress**: somebody is actively working on the language, but haven't opened a PR yet. 
+ **Ready for test**: the translation was PRd on this repository (the link to the PR can be found in the description of the task)

**If you start to work on a language, please write here or let me know** using one of the communication channel listed below, so that i can update the issue tracker and avoid double works.

- [x] **Arabic** - #1591 - *Merged*
- [ ] **Bulgarian** - New! Merged in #1637 , but won't be included in 0.13
- [x] **Catalan** - #1620 (not sure it will make it for 0.13)
- [x] **Chinese (Simplified)** - #1600 - *Merged*
- [x] **Chinese (Taiwanese)** - #1581 - *Merged*
- [ ] **Croatian**
- [x] **Czech** - #1618 - *Merged*
- [x] **Danish** - #1556 - *Merged*
- [x] **Dutch** - ~~#1594~~ replaced by #1599 - *Merged*
- [ ] **Esperanto**
- [x] **Finnish** - #1593 - *Merged*
- [x] **French** - #1586 - *Merged*
- [x] **German** - #1588 - *Merged*
- [x] **Hebrew** - #1603 - *Merged*
- [x] **Hungarian** - #1612 - *Merged*
- [ ] **Indonesian**
- [x] **Italian** - #1584 - *Merged*
- [x] **Japanese** - #1597 - *Merged*
- [ ] **Korean**
- [x] **Lithuanian** - #1608 - *Merged*
- [ ] **Pirate**
- [x] **Polish** - #1589 - *Merged*
- [x] **Portuguese (pt)** - #1596 - *Merged*
- [x] **Portuguese (br)** - #1590 - *Merged*
- [x] **Romanian** - #1607 
- [x] **Russian** - #1598 - *Merged*
- [x] **Serbian** - #1611 - *Merged*
- [x] **Slovak** - #1592 - *Merged*
- [x] **Slovenian** - #1613 - *Merged*
- [x] **Spanish** - #1601 - *Merged*
- [x] **Swedish** - #1609 - *Merged*
- [x] **Turkish** - #1585 
- [ ] **Ukrainian**

## How to translate?
Before starting the translation, we ask you to follow these few guidelines:

+ When possible, do not use gender specific terminology
+ If available, use the glossary for your language. This will help keep translations consistent over different works. Available glossaries are: [Italian](https://github.com/monero-ecosystem/monero-translations/blob/master/italian-terminology.md), [German](https://github.com/monero-ecosystem/monero-translations/blob/master/german-terminology.md), [Swedish](https://github.com/monero-ecosystem/monero-translations/blob/master/swedish-terminology.md),  [Spanish](https://github.com/monero-ecosystem/monero-translations/blob/master/spanish-terminology.md) and [French](https://github.com/monero-ecosystem/monero-translations/blob/master/french-terminology.md)
+ If a string contains number, just keep them as they are
+ Read the guide [Translation tips for Monero translators](https://github.com/monero-ecosystem/monero-translations/blob/master/translation-tips.md), Which cointains many useful tips and tools.

**A step-by-step guide on how to translate the GUI wallet** is available [here](https://taiga.getmonero.org/project/erciccione-monero-localization/wiki/translating-the-gui) (the guide is about how to add a new language, but the instructions are also valid for updating one), but, basically, what a translator need to do is:

1. Look for the correct language file in [monero-gui/translations](https://github.com/monero-project/monero-gui/tree/master/translations)
2. Find the strings labelled `<translation type="unfinished">`
3. Add the correct translation of the `<source>` string between the `<translation>` label (removing the `type="unfinished"`tag)
4. when done, commit and open a Pull Request with your changes. ***Please refer to this issue (#1582) when the PR is opened**.

## Support
If you need help/informations, or have dubts about the workflow, post on this thread or contact me on these channels:

+ *#monero-translations* - Live support chat based on Freenode/IRC, but relayed on matrix/riot and MatterMost
+ *reddit*- just pm /u/ErCiccione
+ *email* - translate[at]getmonero[dot]org
+ *Twitter* - DM @calciferciccio
+ *Wire* - @ErCiccione

### Ping them all!
Pinging contributors who helped with translations in past and members of the Monero Localization Workgroup:

@3b7ameed @edwardlow @ruzaq @cryptobench @falcongoat @Rafficer @lovvskillz @Keksoj @i3visio @lh1008 @cryptochangements34 @glv2 @assylias @milargos @jonahar @TasmaniaKrama @hrumag @kenshi84 @takuto-h @isaacdigs @ProkhorZ @ElectricSlacks @fridzema @einsteinsfool @szogun1987 @netrik182 @rmbb @ordtrogen @mandrill-pie @fero-sk @jernejml @xmronadaily @alexej996 @snaggen @rtonline @zhizhongzhiwai @Lafudoci @el00ruobuob @Leza89 @turossztrapacska @rpinola @monerorus @kasperaitis @Fajl @TheFuzzStone @IST34 @kerastinell @MalMen 

# Discussion History
## erciccione | 2018-10-02T17:33:29+00:00
still pinging them all :P

@4broaf @ni311 @xmoreee @vp1111 @v1docq47 @Re-Diculous @jarole @joli80 @Gelesztaa

## bitlamas | 2018-10-02T17:55:58+00:00
I have some free time this week and probably the other weekend, pretty sure I can get pt_BR done before 18th October. Count me in :)

## el00ruobuob | 2018-10-02T17:58:57+00:00
I have started French already. Should be done tomorrow (if I can build easily).

## apertamono | 2018-10-02T18:28:08+00:00
I want to give other Dutch speakers the opportunity to volunteer, since some Redditors were worried about me doing everything. But I'll be able to translate or review this if nobody else steps up. It's a small update, right? 74 lines in ZH-TW.

## erciccione | 2018-10-02T18:37:29+00:00
@vp1111 i'm afraid we have much less time than that, if you can, PR as soon as possible, i don't think we have more than a week before tagging

@el00ruobuob always the best :)

@ProkhorZ yes, luckily not too many lines. That's fine, just keep in mind we don't have much time before the release

## serhack | 2018-10-02T18:44:17+00:00
@erciccione I'm starting Italian.

## netrik182 | 2018-10-02T18:55:28+00:00
> 
> 
> I have some free time this week and probably the other weekend, pretty sure I can get pt_BR done before 18th October. Count me in :)

@vp1111 I'm available to help you on this. Reach me on IRC, same nick, to share the duty.

## ElDuderinoBerlin | 2018-10-02T19:09:08+00:00
Need german?

## erciccione | 2018-10-02T19:14:08+00:00
@maddinthegreat somebody already contacted me and should be working on the german translation as we speak. Anyway, i will contact you if i don't heear any update or even just to review it. Thanks :)

@netrik182 Since @vp1111 could start working on the translation only next week, would be great if you could start ASAP and maybe then vp11 can review or help you finish

## netrik182 | 2018-10-02T19:17:51+00:00
@erciccione sure. I'll do it.

## bitlamas | 2018-10-02T19:52:40+00:00
> @vp1111 i'm afraid we have much less time than that, if you can, PR as soon as possible, i don't think we have more than a week before tagging

Why so little time? The GUI wasn't ready enough to give translators a little bit more time than a couple days? You usually don't want people rushing translations. I also said I would start the translation this week. I will try to get in touch with @netrik182 and see how I can help.

## erciccione | 2018-10-02T20:30:52+00:00
@vp1111 We definitely have more than a couple of days. The problem is that wasn't clear if the GUI was ready or not, this because an actual code freeze never happened. I waited as much as i could to avoid that potential new parts of the GUI would end up not translated, so at the end i refreshed the language files almost a week ago, but the PR was merged only yesterday. If that's not enough, It's still not clear when we are going to tag the release, that's why i prefer to have all the translations as soon as possible, to have more time for reviews and push as many translations as possible before the tag .

## netrik182 | 2018-10-02T23:03:18+00:00
Done. Sent new PR on #1590

## AbdelhamidGamal | 2018-10-03T03:32:24+00:00
All done <https://github.com/monero-project/monero-gui/pull/1591>

On Wed, Oct 3, 2018 at 1:03 AM netrik182 <notifications@github.com> wrote:

> Done. See PR #1587
> <https://github.com/monero-project/monero-gui/pull/1587>
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero-gui/issues/1582#issuecomment-426459014>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AgtlclkMhCD8PF5HZjHAWpjkRq7fuIbtks5ug_DBgaJpZM4XEg4L>
> .
>


## ni311 | 2018-10-03T07:01:14+00:00
@ni311 - I will take care in weekend

On Tue, Oct 2, 2018 at 8:33 PM erciccione <notifications@github.com> wrote:

> still pinging them all :P
>
> @4broaf <https://github.com/4broaf> @ni311 <https://github.com/ni311>
> @xmoreee <https://github.com/xmoreee> @vp1111 <https://github.com/vp1111>
> @v1docq47 <https://github.com/v1docq47> @Re-Diculous
> <https://github.com/Re-Diculous> @jarole <https://github.com/jarole>
> @joli80 <https://github.com/joli80> @Gelesztaa
> <https://github.com/Gelesztaa>
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero-gui/issues/1582#issuecomment-426362725>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AkpqqiYyohpl-GvcTaame7zfFemIH41qks5ug6N6gaJpZM4XEg4L>
> .
>


## jarole | 2018-10-03T08:37:19+00:00
@erciccione I am working on Slovak translation

## ghost | 2018-10-03T09:19:08+00:00
I can start on the dutch translation tonight if needed


Op di 2 okt. 2018 20:28 schreef ProkhorZ <notifications@github.com>:

> I want to give other Dutch speakers the opportunity to volunteer, but I'll
> be able to translate or review this if nobody else steps up. It's a small
> update, right? 74 lines in ZH-TW.
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero-gui/issues/1582#issuecomment-426381524>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AiFiAmBDGvuUVjjucNsMUP4I4G5zfQmnks5ug7BCgaJpZM4XEg4L>
> .
>


## erciccione | 2018-10-03T10:07:40+00:00
@ElectricSlacks It's still needed, thanks :)

## apertamono | 2018-10-03T12:48:34+00:00
@ElectricSlacks: 
> I can start on the dutch translation tonight if needed

Great! Could you correct a typo in the existing translation, please? 
`u hersteltekst` should be `uw hersteltekst`.

## serhack | 2018-10-03T13:28:40+00:00
#1584 Waiting for any inputs :) 

## ghost | 2018-10-03T18:32:31+00:00
> 
> 
> @ElectricSlacks:
> 
> > I can start on the dutch translation tonight if needed
> 
> Great! Could you correct a typo in the existing translation, please?
> `u hersteltekst` should be `uw hersteltekst`.
Done that and some more
#1594 

## apertamono | 2018-10-03T21:42:28+00:00
I reviewed the Dutch translation. I'll translate it myself tomorrow, which will be less work than trying to edit this contribution.

## takuto-h | 2018-10-04T03:41:39+00:00
I'm working on Japanese translation.

## turossztrapacska | 2018-10-04T18:42:41+00:00
@erciccione I'm working on the hungarian update

## Equim-chan | 2018-10-05T00:23:19+00:00
@erciccione I'm working on Chinese (Simplified).

## apertamono | 2018-10-05T00:52:02+00:00
Finished my Dutch translation. I don't have the time to research this now, but it looked like some strings were marked as untranslated while they had been translated before. Maybe with some invisible formatting changes? So it may be worthwhile to search an older version of the translation file, e.g. from May 2018.

## AbdelhamidGamal | 2018-10-05T01:22:16+00:00
@ProkhorZ found the same thing in Arabic translation

On Fri, Oct 5, 2018, 2:52 AM ProkhorZ <notifications@github.com> wrote:

> Finished my Dutch translation. I don't have the time to research this now,
> but it looked like some strings were marked as untranslated while they had
> been translated before. Maybe with some invisible formatting changes? So it
> may be worthwhile to search an older version of the translation file, e.g.
> from May 2018.
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero-gui/issues/1582#issuecomment-427213860>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/Agtlcp7zD0MjOvqri6fpq1HLL5YXlND0ks5uhq03gaJpZM4XEg4L>
> .
>


## erciccione | 2018-10-05T12:04:35+00:00
> some strings were marked as untranslated while they had been translated before.

@ProkhorZ @3b7ameed That's just `lupdate`. while refreshing the language it happens that some strings get marked as 'unfinished' even if they are finished. Nothing to worry about, it's enough to check if the translation is still valid, and, if that's the case, just remove the label

## erciccione | 2018-10-05T12:05:00+00:00
+Hacktoberfest

## apertamono | 2018-10-05T12:58:21+00:00
> it's enough to check if the translation is still valid, and, if that's the case, just remove the label

Oh, I should do that before opening it in Qt Linguist next time.

## NullPiotrException | 2018-10-05T13:09:44+00:00
@erciccione I think they didn't mean the "unfinished" ones. There were some translations that were previously translated but were completely missing from the newest translation files. Some were really long strings. what I did was check the history of my .ts file and copy-paste my old translations.

## erciccione | 2018-10-05T13:22:29+00:00
> There were some translations that were previously translated but were completely missing from the newest translation files

If those strings are missing, it means they are not in the code anymore

> what I did was checking the history of my .ts file and copy-pasting my old translations.

This is not a correct workflow, ~~the new strings you added were removed because obsolete. Next tiime, please stick to the refreshed file, without adding and removing anything. Thjis time is not a big deal btw,~~ i will syncronize all the language files again anyway before 0.13 is tagged.

edit: Sorry, i misunderstood what you meant at first. Yes, QT can delete whole translations while lupdating, sadly, there is no way to avoid that

## jarole | 2018-10-06T18:36:06+00:00
Hi, why do we translate [message](
https://github.com/monero-project/monero-gui/blob/2ac690ce20157f42a3f0d53d03fdfeb5a53cfbbf/translations/monero-core.ts#L2642) relating to custom ring size?
`WARNING: non default ring size, which may harm your privacy. Default of 7 is recommended.`

Shouldn't be v0.13 with fixed ring size = 11 ?


## erciccione | 2018-10-06T19:17:20+00:00
@jarole You are right, but the GUI still give the possibility to use a personalized ringsize. Will signal this to the GUI devs. Thanks :)

## Medardas | 2018-10-07T04:27:55+00:00
Hey @erciccione , I'll start working on Lithuanian

## erciccione | 2018-10-07T13:02:27+00:00
GUI 0.13 will be tagged in a couple of days.
If you have works still in progress, please PR them before Tuesday

## radamihai | 2018-10-07T14:17:57+00:00
@erciccione I'm working on Romanian

## kasperaitis | 2018-10-07T14:21:27+00:00
> Lithuanian

Just PR what I updated already.

## radamihai | 2018-10-07T14:25:33+00:00
> @erciccione I'm working on Romanian

Oh, never mind, someone just PRd it

## erciccione | 2018-10-07T14:29:58+00:00
@radamihai Yes was just PRd, but a review would be appreciated :)

@kasperaitis Seen it, thanks. I'm about to review it, if you have time and want to push some more commits, we have a full day before release.

## kasperaitis | 2018-10-07T14:31:47+00:00
> 
> 
> @radamihai Yes was just PRd, but a review would be appreciated :)
> 
> @kasperaitis Seen it, thanks. I'm about to review it, if you have time and want to push some more commits, we have a full day before release.

I'll do my best, but saw that @Medardas started working on Lithuanian language.

## erciccione | 2018-10-07T14:40:19+00:00
@kasperaitis Yes, i asked him [on Taiga](https://taiga.getmonero.org/project/erciccione-monero-localization/task/392) to integrate his work with yours. Hopefully he will contact you, but at least now, in the worst case scenario, we have a PR for the Lithuanian language open and technically ready to be merged

## alexej996 | 2018-10-07T22:28:59+00:00
@erciccione Working on Serbian now.

## gorazdko | 2018-10-08T15:06:57+00:00
@erciccione i'll do Slovene (Slovenian)

## duub | 2018-10-08T19:12:04+00:00
Catalan translation is work in progress

## enaSo97 | 2018-10-09T09:20:24+00:00
@erciccione Working on Korean 

## geomars | 2018-10-09T14:27:31+00:00
@erciccione, I'm working on Indonesian. 
Done! See PR #1687

## erciccione | 2018-10-09T14:40:09+00:00
@duub @enaSo97 @geomars Thanks, but keep in mind your translation may not make it for 0.13
Anyway, 0.13.1 should happen soon enough and your works could be included

## TheFuzzStone | 2018-10-13T11:37:50+00:00
@erciccione, I started work on the Ukrainian translation. I plan to finish tomorrow or the day after.  

## erciccione | 2018-10-15T12:55:19+00:00
GUI 0.13.2 has been [tagged](https://github.com/monero-project/monero-gui/tree/v0.13.0.2).
Thanks to all translators and contributors for this huge work :)

## erciccione | 2019-02-22T16:53:23+00:00
Sorry to use this issue, but we are starting to translate the GUI 0.14.0. All translations process has been moved to Pootle: translate.getmonero.org, please submit your translatins directly there.

Also, remember to use the Monero Terminology Guide if available for your language: https://github.com/monero-ecosystem/monero-translations/tree/master/terminology-guides

For any question: #monero-translations or translate@getmonero.org

## erciccione | 2019-05-16T15:57:33+00:00
Hijacking this issue again because we need translators to work on the next release of the GUI (0.14.1 i guess). Please check out the [announcement on reddit](https://www.reddit.com/r/Monero/comments/bojcre/the_new_gui_for_the_next_release_is_ready_but_the/)

Translations can be submitted directly on Pootle: https://translate.getmonero.org/projects/monero-gui

If you have questions or comments, please use the related issue in the *monero-translations* repository: monero-ecosystem/monero-translations#53

# Action History
- Created by: erciccione | 2018-10-02T17:30:17+00:00
- Closed at: 2018-10-15T12:55:19+00:00
