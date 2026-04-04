---
title: '[Discussion] What to name the Monero GUI/repo'
source_url: https://github.com/monero-project/monero-gui/issues/674
author: ghost
assignees: []
labels:
- resolved
created_at: '2017-04-12T17:18:28+00:00'
updated_at: '2017-12-13T12:18:16+00:00'
type: issue
status: closed
closed_at: '2017-12-13T12:18:16+00:00'
---

# Original Description
The issue on what to name the GUI has been a long standing one. 

When the GUI repo was first created it was called monero-core, with Monero Core being the supposed name of the GUI software. The main purpose of calling it this was that the GUI would be the main (core) software that the average Monero user would use. As time went on though, the project title changed to "Monero GUI" so as to avoid confusion for people looking for the software that is central (core) to Monero's functionality (which would be the daemon/CLI). 

However, this has resulted in a disconnect, where the title of the project (Monero GUI) is now different from the name of the repository (monero-core), and where the actual [Readme](https://github.com/monero-project/monero-core#about-this-project) of the GUI states that the core implementation is actually elsewhere:

![gui-discussion](https://cloud.githubusercontent.com/assets/21302237/24970465/60415d30-1f82-11e7-8f52-77b1dec895b0.png)

This discussion thread hopes to arrive at a community consensus around what to call the Monero GUI going forward. It supersedes #654 and #663.

**Questions:**

1. Should the Monero GUI have a name?
2. What are the benefits/drawbacks of naming the GUI?
3. If it should have a name, what are the ideal characteristics of a good name?
4. What are some possible names?
5. How might the Monero Project decide on the specific name used?
6. Should the repository share this title, or can it be named differently (monero-wallet-gui)?

Additional posts on this topic:
1. [Names, names, names](https://www.reddit.com/r/Monero/comments/62iscn/names_names_and_more_names/)
2. [Survey results](https://www.reddit.com/r/Monero/comments/62sdkm/results_of_the_name_survey/)
3. [Dev meeting discussion](https://www.reddit.com/r/Monero/comments/64eel4/20170409_monero_dev_meeting_summary_and_logs/)

# Discussion History
## ghost | 2017-04-12T17:54:30+00:00
My thoughts:

1. Yes, I believe the GUI should have a name, not simply be called "Monero" since the project has other software besides it. Nor should the GUI be titled "Monero GUI", since average people won't know what GUI means, and GUI is not a very memorable or understandable term to most people. Take, for example, how Mozilla called its browser "Firefox" instead of "Mozilla Browser". When people talk about it or ask for help, someone might ask "What browser do you use?" another simply replies "Firefox". It's efficient and unique. Nothing else in the world can be mistaken for this term.
2. One benefit of giving a name to the GUI is easier reference for the general public. Another is clarifying the GUI's identity. For example, the operating system Qubes it titled to help describe how its security functions. Calling the Monero GUI "Monero Prime" might help communicate to the public that this is the main (prime) software to download among all the options we offer (CLI/Kovri/Mininode/etc). Calling it "Monero PrivateTx" would emphasize how our currency is privacy-focused. Another benefit is to make our GUI unique within the cryptocurrency world (IE: not calling it Monero-QT). One drawback of naming the GUI (besides it being simpler to simply do nothing) is the risk of a bad name making the GUI feel cheap and trite. Nobody wants to have the PR/marketing douchiness of your average altcoin, so a name like "Monero X7" would actually make things worse.
3. A good GUI name is a name that: 
* Separates the GUI from the rest of the Monero Project while still holding identity within it (eg: perhaps being an Esperanto word)
* Is easy to say and remember
* Is unique from other software in cryptoland
* Defines the purpose/mission of the GUI
4. Some possible names have already been mentioned in **[this](https://www.reddit.com/r/Monero/comments/64eel4/20170409_monero_dev_meeting_summary_and_logs/)** Reddit thread: 
* Monero Vidi or Vido (Esperanto for 'view')
* Monero Centra (Esperanto for 'central')
* Monero Prime
* Monero Manager
* Monero Kerna (Esperanto for 'core')
* Monero One
* Monero Grafiko/Grafikaj (Esperanto for 'graphic/graphical')
Of these current options I prefer **Monero Kerna**. It keeps the Esperanto theme of our project and has a name with a K, like Kovri. It also communicates the GUI as the basic (core/kerna) software that general public will use. It's unique in cryptoland and is easy to say and remember. That said, I also like **Monero Centra**. As a last option, I'm good with **Monero Prime**.
5. I think the community can help decide on the name. For example, if we feel there exist candidates beyond the eight options listed above, we could open a Reddit thread asking for suggestions. Or if we can't settle on one name, we could create a poll. But this isn't required. As far as I know, Kovri (for example) was simply selected by the devs without popular voting.
6. I don't have strong feelings, one way or the other, that the repo is named the same as the software. If people want to name the repo "monero-wallet-gui" that's fine with me.

## MoroccanMalinois | 2017-05-14T02:10:44+00:00
Some comments (just to reanimate ths :) )

1- I agree, but with that comes a new "brand" (with all the costs associated). Mozilla is a big foundation with relatively serious money on marketing and we are not competing against another implementation of the wallet. So maybe the branding should stay at Monero's level (where there is a supposed competition ? :) ).
2- I agree with all the benefits. Drawbacks : needs more communication/marketing (dns, website, logo)
3- + simple
4- Monero Manager.(or Monero App) : already can manage the daemon, will most probably manage kovri
5- TBH IDC about the name and I am a complete comm/marketing ignorant. But i would like to see the "core" removed from the repo's name and
6- imo, repo should have the same name ([KISS](https://en.wikipedia.org/wiki/KISS_principle))

## dternyak | 2017-06-11T18:11:35+00:00
> ...since average people won't know what GUI means

Average people who don't what a "GUI" is will never be using Monero. It will be abstracted away from them via their bank/some extremely user friendly app that will allow them to keep thinking in their fiat currency terms.

I recommend going with the simple and self-explanatory `monero-wallet-gui` as the official name for the GUI. 

The rest of the terms, while creative, do not actually explain to a new user what this software does. 

## MaxXor | 2017-07-12T19:11:31+00:00
1. The GUI doesn't need a special name, but it shouldn't be named "Monero Core" as this makes the impression this is the core repository (in terms of core functionality) of the Monero project.
2. Same as @MoroccanMalinois and @xmr-eric 
3. unique, easy to memorize, easy to pronounce
4. Monero GUI, Monero App, ... admittedly I'm also fine with more creative names like @xmr-eric mentioned.
5. Not sure, maybe a reddit thread announcing some candidates, devs get feedback about the top candidates and then the devs decide about the name.
6. The repository should have the same name.

## QuickBASIC | 2017-07-17T20:05:55+00:00
> I recommend going with the simple and self-explanatory `monero-wallet-gui` as the official name for the GUI.

I'm honestly not a fan of the word wallet because for lots of cryptocurrency a "wallet" implies that is that it is only just that.  The core gui, syncs the blockchain, can act as a node, acts as a wallet, etc. It's more than just a wallet.

In my mind it's backwards. I'm a fan of naming the GUI project `Monero` and naming the CLI project `monero-core` (flipping them). As in the gui is Monero, that's what we expect the multitudes of people to use and think of as Monero, whereas the core (the central or most important part of something) of the project, is the CLI.

## jonathancross | 2017-07-18T23:14:23+00:00
Considering the GUI is meant as the user-friendly noob default, I feel it should just be called "Monero" (or "Monero Wallet" which will help people know what it _does_).  We may not like the term Wallet, but if that is what users are searching for, we should use it here.

As for the daemon, I say the nerdier the better, ie "Monero Server" or "Monero Daemon" -- something that clearly says to new users "Warning: nerdy commandline ahead!"  It properly sets expectations as to what the user can expect.

I feel "Monero Core" name took on unnecessary baggage from Bitcoin (where the wallet and daemon were integrated).  It also makes more sense for Bitcoin as a way to differentiate between the reference client and the long list of alternative clients.  This is not an issue with Monero where this is the only client, so we don't need the "Core".

## qertoip | 2017-09-05T09:20:09+00:00
Let's decouple repository names from end-user brands and artefacts.

Why not simply rename this repo to "monero-gui" so new programmers can understand the monero-project structure immediately.

We can then independently consider end-user artefacts and branding, which I'm afraid is a much bigger discussion.

In any case, any rename will be better than none, as monero-core is super misleading for a GUI project.

## jonathancross | 2017-09-07T14:05:10+00:00
I'd be fine with "monero-gui" or "monero-wallet" as both would be an improvement and we have not come up with any better repo names.  GUI is quite nerdy, but at least it is not misleading.

## dEBRUYNE-1 | 2017-12-13T11:07:55+00:00
Renamed to `monero-gui`.

+resolved

# Action History
- Created by: ghost | 2017-04-12T17:18:28+00:00
- Closed at: 2017-12-13T12:18:16+00:00
