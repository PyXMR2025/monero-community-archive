---
title: Customisations requested to Kastelo repository
source_url: https://github.com/monero-project/meta/issues/136
author: michaesc
assignees: []
labels: []
created_at: '2017-11-12T18:06:41+00:00'
updated_at: '2023-12-18T13:29:52+00:00'
type: issue
status: closed
closed_at: '2023-12-18T13:29:51+00:00'
---

# Original Description
Our new repository is in use, but not yet customised. Please help us fine tune:

- [x] Remove 'Projects' from the tab bar (next to 'Code', 'Issues', 'Pull Requests', ...)
- [x] Remove 'Wiki' from the tab bar (next to 'Code', 'Issues', 'Pull Requests', ...)
- [ ] Add a IRC web hook to log Kastelo commits to #monero-hwcode
- [ ] Add a Taiga web hook as directed by https://tree.taiga.io/support/integrations/github-integration/#second:-configure-webhooks-in-your-github-repository

Our web hook 'Payload URL' is http://taiga.getmonero.org/api/v1/github-hook?project=9
~~Contact Michael to learn the web hook secret key, please.~~
Choose any secret key you want of the form [0-9A-Fa-f]{32} and tell it to Michael in a separate channel. By the way, the regular expression just indicated produces a secret of the type 51bb2f00d1234ABcd900bD00D4422998, where upper and lower case holds meaning.

- [x] Lastly, while many like the name Sekura it sounds too similar to a protocol used in Kovri. So please rename this repository from 'sekura' to **'kastelo'**.

**Q:** Why remove 'Projects' and 'Wiki'? **A:** Because we're using the Taiga system for those things.

Thank you!
  

# Discussion History
## anonimal | 2017-11-14T20:04:35+00:00
@michaesc Thank you for opening this issue (note: 'future' protocol).

@fluffypony @luigi1111 if you wouldn't mind, while you're here; referencing #77 and #78.

## michaesc | 2017-11-15T14:29:16+00:00
- [ ] Fill in website http://kastelo.org/
- [ ] Fill in topics: monero, cryptocurrency, blockchain, privacy, finance, hardware, wallet

It seems adding topics is explained [here](https://help.github.com/articles/classifying-your-repository-with-topics/).

**License:** It seems there's a place in the GitHub config for license? If so, ours is **CERN OHL**

In our repository: https://github.com/monero-project/kastelo/blob/master/LICENSE
The real license location: https://www.ohwr.org/documents/294/

@anonimal What is the name of the _future protocol_ again? I've forgotten.

**Description:** ~~The Monero hardware wallet is a printed circuit board design. It may credit card sized and composed of fewer (broader developer reach) or more (optimal electronic density) substrate layers.~~ It's fine to keep what's already there.

## michaesc | 2018-01-24T19:28:46+00:00
Any chance of having our repository name and features corrected before our team meeting later this week?

## michaesc | 2018-01-25T20:50:21+00:00
@luigi1111 @fluffypony We just got our USB PID assignment denied, because our repository name is instable. We worked hard to submit for this assignment, and it's quite a setback for the firmware effort.

https://github.com/pidcodes/pidcodes.github.com/pull/293#issuecomment-360561141
https://github.com/pidcodes/pidcodes.github.com/pull/293/commits/90f8ff08a757d3579c9b7d80d6933c60e7d705e5

## luigi1111 | 2018-01-26T19:02:46+00:00
Hi @michaesc sorry for the delay. @fluffypony is the one that makes changes using the monero-project account. I've pinged him out-of-band as I know he's been traveling.

Edit: looks like it's done.

## michaesc | 2018-03-08T14:21:04+00:00
Hi @luigi1111 and @fluffypony, thanks for the great administration so far. In our new Kastelo repository let's:

- [ ] Correct the description to **The Monero Hardware Wallet**
- [x] ~~Correct the~~ (working again!) **IRC commit feed #monero-hwcode** which worked before the Sekura name change
- [ ] Fill in the _website_ field to **http://kastelo.org/**
- [ ] Add a **Taiga web hook** to GitHub events, this is really easy (see above for information)
- [ ] Have a well deserved coffee :coffee: break (or :beer: + :pizza: ?)

We're just a few weeks from the conclusion of RFC-HWALLET-1, which requires some of these things. Thanks again!

## anonimal | 2018-03-09T01:44:23+00:00
>Correct the IRC commit feed #monero-hwcode which worked before the Sekura name change

This may be related https://github.com/monero-project/meta/issues/183.

## michaesc | 2018-03-23T12:57:42+00:00
Any chance at eliminating the **low hanging fruit** at least?

- [ ] Fill in the website field to http://kastelo.org/
- [ ] Correct the description to The Monero Hardware Wallet
- [ ] Fill in topics: monero, cryptocurrency, blockchain, privacy, finance, hardware, wallet

## nahuhh | 2023-12-18T09:00:40+00:00
@michaesc  can this be closed

## michaesc | 2023-12-18T13:29:51+00:00
> @michaesc can this be closed
>
I think it should be closed. The requested customisations are still incomplete, and have not been done. But it seems so unlikely that a person with access to the repository will implement them, that I think it should be closed.

Thanks @nahuhh for suggesting this.

# Action History
- Created by: michaesc | 2017-11-12T18:06:41+00:00
- Closed at: 2023-12-18T13:29:51+00:00
