---
title: Update all language files for 0.12.1 - Call for translators
source_url: https://github.com/monero-project/monero-gui/issues/1377
author: erciccione
assignees: []
labels: []
created_at: '2018-05-08T09:25:38+00:00'
updated_at: '2018-07-24T16:42:13+00:00'
type: issue
status: closed
closed_at: '2018-07-24T16:42:13+00:00'
---

# Original Description
The GUI is frozen, now we need to update all existent languages. Keep in mind that the new GUI will be released once all languages will be updated, so please, if you are working on something else, **give the maximum priority to the GUI**.

 ~~I refreshed all language files (see #1376 ), you can find the uploaded version of each language on the `refresh-lang` branch of my repo. Please **use these updated files, NOT the ones on the official repository**. Updated language files can be found at this link:~~ 

~~https://github.com/erciccione/monero-core/tree/refresh-lang/translations~~

Pull the file related to your language from ~~that link~~

https://github.com/monero-project/monero-gui/tree/master/translations

translate the missing strings and, when done, open a PR against monero-project/monero-gui referencing to this issue.

**! Do not update the .ts file and don't run any command, just pull the correct file for your language and translate it. Stick to this workflow, please. !**

## Languages and tasks
Refer to the Taiga task to know the status of each language (if a task's status is 'in progress' or 'assigned to', somebody else is already working on it). I listed down here all available languages, as soon as a translation is PRd, the correspondent language will be thicked.

- [ ] **Arabic** - [Taiga task](https://taiga.getmonero.org/project/erciccione-monero-localization/task/255)
- [ ] **Catalan** - [Taiga task](https://taiga.getmonero.org/project/erciccione-monero-localization/task/256)
- [x] *Merged* **Czech** - [Taiga task](https://taiga.getmonero.org/project/erciccione-monero-localization/task/284)
- [x] *merged* **Danish** - [Taiga task](https://taiga.getmonero.org/project/erciccione-monero-localization/task/260)
- [x] *Merged* **German** - [Taiga task](https://taiga.getmonero.org/project/erciccione-monero-localization/task/264)
- [x] *Merged* **Esperanto** - [Taiga task](https://taiga.getmonero.org/project/erciccione-monero-localization/task/262)
- [x] *Merged* **Spanish** - [Taiga task](https://taiga.getmonero.org/project/erciccione-monero-localization/task/277)
- [x] *merged* **French** - [Taiga task](https://taiga.getmonero.org/project/erciccione-monero-localization/task/263)
- [x] *Merged* **Hebrew** - [Taiga task](https://taiga.getmonero.org/project/erciccione-monero-localization/task/265)
- [ ] **Croatian** - [Taiga task](https://taiga.getmonero.org/project/erciccione-monero-localization/task/259)
- [ ] **Indonesian** - [Taiga task](https://taiga.getmonero.org/project/erciccione-monero-localization/task/266)
- [x] *Merged* **Italian** - [Taiga task](https://taiga.getmonero.org/project/erciccione-monero-localization/task/267)
- [x] *Merged* **Japanese** - [Taiga task](https://taiga.getmonero.org/project/erciccione-monero-localization/task/268)
- [ ] **Korean** - [Taiga task](https://taiga.getmonero.org/project/erciccione-monero-localization/task/269)
- [x] *Merged* **Dutch** - [Taiga task](https://taiga.getmonero.org/project/erciccione-monero-localization/task/261)
- [x] *Merged* **Polish** - [Taiga task](https://taiga.getmonero.org/project/erciccione-monero-localization/task/270)
- [x] *Merged* **Portuguese Brazilian** - [Taiga task](https://taiga.getmonero.org/project/erciccione-monero-localization/task/272)
- [x] *merged* **Portuguese** - [Taiga task](https://taiga.getmonero.org/project/erciccione-monero-localization/task/271)
- [x] *Merged* **Romanian** - [Taiga task](https://taiga.getmonero.org/project/erciccione-monero-localization/task/273)
- [x] *Merged* **Russian** - [Taiga task](https://taiga.getmonero.org/project/erciccione-monero-localization/task/274)
- [x] *merged* **Slovak** - [Taiga task](https://taiga.getmonero.org/project/erciccione-monero-localization/task/283)
- [ ] **Slovenian** - [Taiga task](https://taiga.getmonero.org/project/erciccione-monero-localization/task/276)
- [x] *Merged* **Serbian** - [Taiga task](https://taiga.getmonero.org/project/erciccione-monero-localization/task/275)
- [x] *Merged* **Swedish** - [Taiga task](https://taiga.getmonero.org/project/erciccione-monero-localization/task/278)
- [x] *Merged* **Turkish** - [Taiga task](https://taiga.getmonero.org/project/erciccione-monero-localization/task/279)
- [ ] **Ukrainian** - [Taiga task](https://taiga.getmonero.org/project/erciccione-monero-localization/task/280)
- [x] *Merged* **Chinese Traditional** - [Taiga task](https://taiga.getmonero.org/project/erciccione-monero-localization/task/257)
- [x] *merged* **Chinese Simplified** - [Taiga task](https://taiga.getmonero.org/project/erciccione-monero-localization/task/258)

## Workflow
Please read our [General guidlines for translators](https://taiga.getmonero.org/project/erciccione-monero-localization/wiki/home) before you start.

If you are on the localization team on Taiga, use this workflow:

- I opened a new task called "Updates for release 0.12.1" and marked it as "needed" for each of the 29 languages available. Once you are actively working on the translation, change its status to 'in progress' (and preferably, assign the task to yourself).
- All needed translations will be marked as 'needed'. if somebody is already working on your language, contact the translator (here on GitHub or on Taiga) and offer him/her your help. *Do not* start translating anyway. Ask if in dubt.
- Once your work is ready and pushed on GitHub, add the link of the PR in the apposite custom field and change the status of the task to 'ready for tests'.

**If you are not on Taiga but you are working on a translation, just comment here signaling you started working on a language, and keep us updated on the status of your work. I will keep Taiga updated for you. This will avoid double works**

## Help/Support
If you need any help/support: comment this issue, come chat on `#monero-translations`(Freenode, [MatterMost](https://mattermost.getmonero.org/monero/channels/monero-translations), matrix/riot), or [PM me on reddit](https://www.reddit.com/message/compose/?to=ErCiccione)

Pinging past contributors and members of the localization workgroup on GitHub:

@3b7ameed @edwardlow @ruzaq @cryptobench @falcongoat @Rafficer @lovvskillz @Keksoj @i3visio @lh1008 @cryptochangements34 @glv2 @assylias @milargos @jonahar @TasmaniaKrama @hrumag @kenshi84 @takuto-h @isaacdigs @ProkhorZ @ElectricSlacks @fridzema @einsteinsfool @szogun1987 @netrik182 @rmbb @ordtrogen @mandrill-pie @fero-sk @jernejml @xmronadaily @alexej996 @snaggen @rtonline @zhizhongzhiwai @Lafudoci @el00ruobuob 

# Discussion History
## apertamono | 2018-05-08T10:36:53+00:00
Thanks for freezing! I'm working on the Dutch translation.

## erciccione | 2018-05-08T10:46:41+00:00
thanks @ProkhorZ , i updated the task on Taiga to 'In progress'

## netrik182 | 2018-05-08T10:50:34+00:00
I will start working on pt-BR today 

## erciccione | 2018-05-08T11:28:57+00:00
thanks @netrik182 

## ordtrogen | 2018-05-08T11:29:04+00:00
I've been working on the Swedish one for a while and have assigned it to myself on Taiga


## takuto-h | 2018-05-08T11:33:14+00:00
I'm working on the Japanese translation.

## cryptochangements34 | 2018-05-08T12:28:18+00:00
I'll get started on french

## Lafudoci | 2018-05-08T14:03:23+00:00
I'll translate the Traditional Chinese as always. But there is a minor mistake in the languages and tasks list (in first comment) @erciccione. The Traditional Chinese in GUI basically indicates Taiwanese Chinese. Might be a typo for Simplified Chinese? BTW, I have been in the Taiga for a while, but I still can't find how to assign myself to a task? The assign text seems not clickable.

## erciccione | 2018-05-08T15:13:42+00:00
@Lafudoci I'm confused about the difference in the GUI between Taiwanese, traditional and simplified. At the moment we have `monero-core_zh-tw.ts` and `monero-core_zh-cn.ts` available in the GUI. these are Chinese Taiwanese and Traditional Chinese right? so the typo should be on Taiga, where i named Simplified Chinese the Simplified Chinese translation. Am i correct?

About Taiga. Make sure you are logged in and you should see on the [task's page](https://taiga.getmonero.org/project/erciccione-monero-localization/us/59?milestone=10) the `assign or assign to me` option. You should be able to click 'assign to me'

## ParsifalX | 2018-05-08T16:13:21+00:00
Any chance of adding Greek so i can start working on it?

## erciccione | 2018-05-08T16:33:38+00:00
@ParsifalX I'm afraid the GUI is already frozen, too late to add another language. But if you wish to contribute there is a lot tha could be translated, starting from getmonero.org. See: https://taiga.getmonero.org/project/erciccione-monero-localization/wiki/translating-monero-website

## SamsungGalaxyPlayer | 2018-05-08T16:48:42+00:00
@ParsifalX you can absolutely still help with Greek, but it will most likely make it in the August/September release. In the meantime, you can help with other stuff including the website like @erciccione mentioned.

## ParsifalX | 2018-05-08T16:58:18+00:00
Thanks @erciccione and @SamsungGalaxyPlayer. I'll start working on getmonero.org and i'll get back to GUI before the next point release.

## Lafudoci | 2018-05-08T18:02:00+00:00
@erciccione The Traditional Chinese is officially used in Taiwan `monero-core_zh-tw`. And Simplified Chinese is officially used in China `monero-core_zh-cn` and some other country. But in some regions like Hong-Kong and Singapore, they have their local Traditional and Simplified styles. They are not in GUI yet. Or it will be like `monero-core_zh-hk`.

For taiga, I didn't find `assign or assign to me option`. Here is my screen. The `Assign` in sidebar is not clickable.
![default](https://user-images.githubusercontent.com/10460270/39774124-8d4457ea-532c-11e8-9a46-63738e0b75ab.PNG)


## faudi | 2018-05-08T18:04:23+00:00
I see the italian translation is already being worked on. Anything I can do?

## erciccione | 2018-05-08T18:24:18+00:00
Thanks @ParsifalX , contact me if you need any help

@Lafudoci Thank for the clarifications, will fix the nomenclature on Taiga. About the assign issue, i checked, looks like you are not a member of the team, i guess that's the problem. It's odd, because i remember adding you. Could you send me the email you used to subscribe on Taiga? I will resend you the invitation (you can write me on erciccione[at]protonmail[dot]com)

@faudi Would be great to have hrumag's work reviewed once he is done, could you help with that?

## faudi | 2018-05-08T18:27:07+00:00
@erciccione I'd be glad to! :)

## szogun1987 | 2018-05-08T18:40:30+00:00
I can help someone with Polish translations (e.g. review them), but I'm not able to translate all phrases.

## NullPiotrException | 2018-05-08T19:33:01+00:00
@szogun1987 Feel free to review mine.

## RatusNatus | 2018-05-09T03:00:02+00:00
Looks my language is already done.

## ni311 | 2018-05-09T07:17:25+00:00
I'd like to start working on Romanian but I cannot assign the task to me.

## erciccione | 2018-05-09T08:37:33+00:00
@RatusNatus What's your language? if it's already PRd would be nice to have it reviewed

@ni311 if you are not a member of the team on Taiga, i will move the task to 'in progress' for you. You don't need to be subscribed to Taiga to work on this, but if you want to be added just send me your email address by email (my address is some comments above). Thanks and keep us updated please :)

## erciccione | 2018-05-11T12:09:24+00:00
Quick update on the status of this issue:

8 languages are still 'needed'
7 languages PRd and ready for tests
13 languages being worked on ('in progress')

Needed translations at the moment:
Arabic, Catalan, Croatian, Indonesian, Turkish, Slovak, Chinese Simplified, Portuguese

Ping @7dNp8xK3Ed

## lh1008 | 2018-05-11T16:55:27+00:00
Done :) Updated spanish GUI translation https://github.com/monero-project/monero-gui/pull/1399 

## fero-sk | 2018-05-11T20:58:32+00:00
Working on Slovak...

## bh1nyr | 2018-05-13T19:24:25+00:00
I'm working on the simplified chinese translation.

## bh1nyr | 2018-05-14T16:04:53+00:00
Update simplified chinese translations for 0.12.1 #1414 

## fero-sk | 2018-05-15T15:57:42+00:00
Slovak: I finished 1242 lines - attached - additional lines are too dificult for me to translate :(
Can someone else continue on this work?
[monero-core_sk.ts.txt](https://github.com/monero-project/monero-gui/files/2005707/monero-core_sk.ts.txt)


## erciccione | 2018-05-15T16:22:12+00:00
Hey @fero-sk , i see most of the file is translated, you can open a pull request anyway even if not 100% complete, 1242 strings are more than enough. In the meantime, we can ask on our channels if somebody can help with the missing strings. Also, i see many strings marked 'unfinished', but the strings are translated, please remove 'unfinished', or the original string (in english) will be picked by the GUI.

## erciccione | 2018-05-22T16:52:14+00:00
0.12.1 is a matter of hours now. If you worked on a translation and haven't opened a PR yet. Now it's the time

## erciccione | 2018-07-24T16:42:13+00:00
0.12.2 was out some weeks ago. Thanks everybody :)

# Action History
- Created by: erciccione | 2018-05-08T09:25:38+00:00
- Closed at: 2018-07-24T16:42:13+00:00
