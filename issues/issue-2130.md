---
title: '[UX] Add toggle to disable send button'
source_url: https://github.com/monero-project/monero-gui/issues/2130
author: Mansarde
assignees: []
labels:
- feature
created_at: '2019-04-29T12:13:55+00:00'
updated_at: '2019-06-10T15:04:11+00:00'
type: issue
status: closed
closed_at: '2019-06-10T15:04:10+00:00'
---

# Original Description
At the moment the only way to ensure a full wallet does not relay a transaction is with the CLI's start option `--do-not-relay`
For the GUI (with full wallet) there is an advanced button to sign a TX file, but there is no option to disable the send button.

That means in the CLI (with `--do-not-relay`) you can't accidentally relay a transaction.
With the GUI you *can* accidentally relay if you're not careful.

**Suggestion:**
Add a setting for the GUI that diables the "Send" button or alternatively replace it with the "Create TX file" button from the "Advanced" menu.

This way one does not have to remember *not* to click "Send" everytime, but only needs to set an option once.

EDIT: Changed the wording to clarify a bit more.

# Discussion History
## sanderfoobar | 2019-04-29T16:56:07+00:00
+feature

## GBKS | 2019-05-25T06:44:53+00:00
I'm not super familiar with this function, so I have a few questions.

What's the reason to make this a setting vs. just another option under "Advanced"? Is there a specific use case where you want to enforce this?

And what happens when you press this button? Does it download a file to your desktop?

## Mansarde | 2019-05-25T10:55:31+00:00
> What's the reason to make this a setting vs. just another option under "Advanced"?

It actually already is a button under "Advanced".
For my reason why to disable or swap out the normal send button, see the use case below.

> And what happens when you press this button? Does it download a file to your desktop?

It would act just like the "Sign tx file" button under "Advanced".

> Is there a specific use case where you want to enforce this?

Use case:
I use a full hot wallet together with a hardware device (e.g. Ledger).
I want to use the full hot wallet only for checking my balance and transactions, but I don't want to send transactions directly from my network.
Instead, I would like to set an option so that my wallet will always create TX files instead, just like with the CLI option `--do-not-relay`.
This way I never accidentally send transactions via my normal network connection.

I'd sleep easier if the normal send button could be disabled (just like with a watch-only wallet) or maybe be swapped out with the "Sign tx file" button.

## GBKS | 2019-05-25T12:30:26+00:00
Got it, thanks for the explanation. So what differs this from a watch-only wallet? Just the option to still use a hardware device to transact?

## Mansarde | 2019-05-25T13:19:54+00:00
The difference is that with a watch-only wallet I can't see my true balance.
At least not without TX export/import + key images import/export shenanigans.

The CLI only allows to relay a transaction immediately *or* create a signed TX file, depending on whether the wallet has been started with `--do-no-relay` or not.
The GUI offers both relaying *and* creating a signed TX file (as an advanced button).

In the CLI I can't accidentally relay a transaction if the `--do-not-relay` option was set.
In the GUI I *can* accidentally relay a transaction if I'm not careful.

That's why I'm asking for an option to simply disable the "Send" button (just like with viewonly wallets) or even to replace it with the "Create TX file" button.

## GBKS | 2019-05-26T07:52:18+00:00
Thanks for patiently explaining everything. That does sound like it could be a simple toggle in the settings, and replacing "Send" with "Creation transaction file" would be better than just disabling "Send".

Do you think this is something a lot of people would use?

## Mansarde | 2019-05-26T10:47:15+00:00
That's hard to say, as I can only speak for myself.
But judging from how many mistakes Monero users have already done I would think anything that can help someone prevent making accidental mistakes (which could compromise their privacy) is a plus.

It's probably not something *most* people would use, I admit.
But just as with any other of the advanced options I can imagine it's something many people would use that have a need for it.
That could be anyone who A) uses a hot full wallet (because of a hardware device or whatever reason) and B) wants to sleep easy that their IP remains clear from Monero usage (i.e. privacy).

I'd say people are just as likely going to use this proposed feature like any other existing privacy option, depending on their privacy needs, like "Hide Balance" for example.

The CLI provides this already because `--do-not-relay` makes it *impossible* to accidentally relay a transaction. So a CLI user won't get punished when making a transaction and forgetting to choose the right command (because there is only one command to create a TX and it's toggleable via `--do-not-relay`).
But the GUI doesn't provide this optional restriction yet and thus creates a potential for an accidental leak, because both options are available at the same time.

Btw. I appreciate your patience and tact. This community is awesome.^^

## GBKS | 2019-05-31T15:52:17+00:00
Considering users still have to enter their password to make a transaction, do you think the risk is still high enough for accidental sends?

## Mansarde | 2019-06-10T15:04:10+00:00
> Considering users still have to enter their password to make a transaction, do you think the risk is still high enough for accidental sends?

I suppose it will probably deter some accidental sends, where the accident would've otherwise been noticed immediately after that one click.
I'm not sure what amount of risk is considered necessary here for inclusion of a feature.
The initial reason for creating this feature request was mostly to get functional parity of the send-workflow when compared to the CLI, even though I described it in terms of accidental sends.

But it looks like someone has created a pull request in the meantime.
If the PR does not make it then I'll take that as a hint that the feature is not useful enough for enough people.

In any case, thanks for your consideration, much appreciated! :)

# Action History
- Created by: Mansarde | 2019-04-29T12:13:55+00:00
- Closed at: 2019-06-10T15:04:10+00:00
