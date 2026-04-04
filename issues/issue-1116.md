---
title: All translations need updates
source_url: https://github.com/monero-project/monero-gui/issues/1116
author: erciccione
assignees: []
labels: []
created_at: '2018-02-14T12:06:52+00:00'
updated_at: '2018-04-04T12:27:17+00:00'
type: issue
status: closed
closed_at: '2018-04-04T12:27:17+00:00'
---

# Original Description
After #1076 all translations of the GUI need to be updated. Some are already in progress, but many other need to be checked and updated before the next release. 

These are the languages that aren't in porgress and need to be updated. I pinged in this issue all contributors who helped in past with the relative language, hoping they can contribute this time as well.

- [x] Croatian
- [x] German: @leonklingele @Schnoffel
- [x] Hebrew: @jonahar
- [x] Danish: @cryptobench
- [x] Portoguese Brazilian: @fabionitto @moneroj
- [x] Portuguese
- [x] Dutch: @potatored @fridzema @ProkhorZ
- [ ] Esperanto: @Keksoj
- [ ] Indonesian: ?
- [x] Japanese: @kenshi84
- [ ] Korean: @isaacdigs
- [x] Romanian: @mandrill-pie
- [x] Russian: @cheebeez @LvMsterfild

If you start working on a translation, please communicate it in the comments (if you have it, with the link to the WIP repository), so i can thick the relative language and consider it 'in progress'. Our tracking platform, [Taiga](https://taiga.getmonero.org/project/erciccione-monero-localization/backlog), is costantly updated and a great place to check what languages are in progress and who is working on them.

If you need help/infos ask down here, [PM me on reddit](https://www.reddit.com/message/compose/?to=ErCiccione) or come chat on `#monero-translations`

# Discussion History
## ordtrogen | 2018-02-14T17:39:19+00:00
Just mentioning I'm hard at work on the Swedish one. As soon as I have a PR I'll make it known and anyone'll be welcome to comment.



## apertamono | 2018-02-15T15:46:27+00:00
OK, thanks for the reminder. I started updating the Dutch translation. It's ~100 new or edited strings.

@potatored Thanks for correcting some bad typos. If you have time to contribute translations, could you work on the Monero website?
@fridzema I see you're busy coding. Great!

## netrik182 | 2018-02-19T16:26:27+00:00
The strings marked with ``<translation type="unfinished">`` are ready to be translated or should we expect any changes in the english text before the release?

## erciccione | 2018-02-19T16:30:45+00:00
@netrik182 they are ready to be translated, just take off the `type="unfinished">` part and put your translation between `<translation></translation>`

## netrik182 | 2018-02-19T16:33:37+00:00
@erciccione ok, thanks!

## apertamono | 2018-02-19T17:46:58+00:00
@netrik182 If you use Qt Linguist, it will take you automatically to the new and updated strings, and it will remove the 'unfinished' tag for you. It has other useful features too, like copying translations for repeated strings. Annoyingly, there's no official distribution other than the whole Qt package, but the [download from Softpedia](http://www.softpedia.com/get/Others/Home-Education/Qt-Linguist.shtml) will probably be safe.

## netrik182 | 2018-02-19T18:28:00+00:00
@ProkhorZ I'll take a look. Thank you

## mandrill-pie | 2018-02-19T18:39:33+00:00
Almost done with the Romanian translation. But here's a bit I'm having difficulties understanding:
```
Payment ID
A unique user name used in the address book.
It is not a transfer of information sent during the transfer.
```
What does that actually mean? Any other way to phrase it to help me translate it?

## mandrill-pie | 2018-02-19T18:41:14+00:00
Also, what's the next step when I'm done? A PR like last time?

## georgi-id | 2018-02-19T23:53:39+00:00
I was wondering about that same passage @mandrill-pie. The last sentence especially doesn't sound good in english either.

## LvMsterfild | 2018-02-19T23:59:06+00:00
Perhaps, this is more correct link (
https://github.com/monero-project/monero-gui/pull/1076/files):
https://github.com/jonathancross/monero-gui/blob/84d363999139f8fb25e3a58d65508ec4c3592d24/translations/monero-core_ru.ts

2018-02-20 1:53 GMT+02:00 Omgthehorror <notifications@github.com>:

> I was wondering about that same passage @mandrill-pie
> <https://github.com/mandrill-pie>. The last sentence especially doesn't
> sound good in english either.
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero-gui/issues/1116#issuecomment-366829518>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AYPanXM_AIFcXHDnwXpygu5UE4ztoZeYks5tWgmGgaJpZM4SFNqM>
> .
>


## mandrill-pie | 2018-02-20T09:45:33+00:00
@erciccione Romanian updated. I've opened a pull request #1125 

## erciccione | 2018-02-20T12:16:14+00:00
@LvMsterfild that PR was merged into the code, no need to link it directly

@mandrill-pie thanks! i'm gonna review it

## takuto-h | 2018-02-21T03:12:57+00:00
Hi, I've created a PR to update Japanese translation: #1132 

## netrik182 | 2018-02-24T03:46:04+00:00
@erciccione Just created PR for Brazilian Portuguese #1136 

## cryptobench | 2018-02-26T15:02:25+00:00
PR submitted for danish translation #1142 

## jonathancross | 2018-02-26T16:00:46+00:00
@mandrill-pie You are correct, this is bad English.

Should be something like:

    Payment ID
    An arbitrary, unique identifier used to distinguish payments.
    The ID can be either 64 or 16 hexadecimal characters long.
    If 16, it will be encrypted, if 64, it will be visible on the blockchain.
    An ID can be combined with an address to form an Integrated Address.

Maybe best to fix the english and update all languages separately from this?

## Keksoj | 2018-04-03T16:28:12+00:00
Hi, I'm the one who made the last translation fixes on the esperanto version. But if I check it at 
https://github.com/monero-project/monero-gui/blob/master/translations/monero-core_eo.ts 
I can't see any problem to it. Maybe I'm not looking good enough. Are they new lines to be added ?

Oh, okay, I just realised there's a bunch of 

type="unfinished"

So, do I edit it, create a pull request and so on ? I'll have @erciccione help me for the details since I'm a bit of a noob. 
You can count on me anyway !

## pazos | 2018-04-03T17:15:31+00:00
@erciccione: can we switch translation upgrades to a platform like transifex or  weblate? I think it would help contributors to get the work done. 

## erciccione | 2018-04-03T18:19:07+00:00
@pazos That's already in process. After the new release is out we will start working on the web platform. In our case, Pootle

## erciccione | 2018-04-04T12:27:17+00:00
[The new releaseis out!](https://github.com/monero-project/monero-gui/releases/tag/v0.12.0.0)
Thanks everybody :)

# Action History
- Created by: erciccione | 2018-02-14T12:06:52+00:00
- Closed at: 2018-04-04T12:27:17+00:00
