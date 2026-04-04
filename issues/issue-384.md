---
title: '[Discussion] Rebranding of "GUI" Wallet'
source_url: https://github.com/monero-project/meta/issues/384
author: scottAnselmo
assignees: []
labels: []
created_at: '2019-08-19T21:15:11+00:00'
updated_at: '2022-08-24T20:21:52+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Motivated out of the IRC discussion on -community, this issue is an attempt to semi-formally move forward on giving the GUI wallet on a name that can be better branded. Efforts were focused on this such as https://github.com/monero-project/monero-gui/issues/932 but for one reason or another didn't execute to finish.

"GUI" may work just fine for power users, but not necessarily for the every day user. The main focus for this change is driving adoption and brand-ability. This initial issue will serve as a living document for the process and remain open until the name has been picked.

### The process I propose very loosely mirrors that of release names:

1. Procure a list of suggested names via comments on a GitHub issue (most likely create a separate issue from this one) for a one month window
2. Allow for multi-choice voting for a one month window. Each one of the below may have limitations such as number of poll entries, etc. that will be worth exploring once we have loose consensus and moved beyond brainstorming. Polling systems that can potentially be utilized are:

- Twitter
- Comment via (another) GitHub issue
- Blockfolio
- (Please comment for any other recommended polling methods)

### General Guidance for name suggestions:

- Name is easy to spell ("Grafiko" is hard to spell because it could potentially be written as Gra**ph**iko)
- Name is not generic so as to be confusing when referencing it (Just download the "Monero App". _Which app?_)
- Esperanto based names may be preferred as it's the unofficial ecosystem naming convention
- (Please comment for any other suggestions)


### Action Required (AR) after deciding name:

- [ ] Update strings in GUI

- [ ] Update strings in monero-gui-guide

- [ ] Update Weblate (translate.getmonero.org)

- [ ] Update download page

- [ ] Update buildbot, ping repo package maintainers about rebrand

- [ ] (Please comment for any other AR suggestions)





# Discussion History
## selsta | 2019-08-19T21:25:39+00:00
AR: Update buildbot, ping repo package maintainers about rebrand

## ghost | 2019-09-21T18:30:57+00:00
What is it about: Monero
What is it: a wallet
Who releases it: Core

**Monero Core wallet**.

"_Just download the core wallet_".
"_The core wallet is recommended by the community_."

Advantages:
- it is not ambiguous
- "core" is part of the established crypto vocabulary and signifies a certain 'official-ness'

Disadvantages:
- name isn't particularly striking
- does not follow the Esperanto naming convention

CLI can be referred to as "Monero Core CLI wallet".

## SamsungGalaxyPlayer | 2019-09-21T22:02:41+00:00
@defterade honestly I love the simplicity of this.

## erciccione | 2019-09-22T13:22:43+00:00
@defterade the point is that the GUI was referred to as the "core wallet" years ago, the repository was `monero-core` and was later changed to `monero-gui`, because the word 'core' is mostly used to refer to the cli wallet. So, i think using the 'core' word again could be confusing.

## ghost | 2019-09-22T13:54:13+00:00
@erciccione
In the past 6 years there have been a total of 60 mentions of "core wallet" in /r/Monero.

![monero-core-wallet](https://user-images.githubusercontent.com/11379144/65388855-0014dc00-dd50-11e9-8849-30958ab79628.png)

4900 for 'CLI' [[1](https://i.imgur.com/2cyR5E4.png)] and 23.3k for 'GUI' [[2](https://i.imgur.com/SwBTOUO.png)]. 

It is clear that 'CLI' and 'GUI' are currently being used to refer to the wallets provided by the Core team.

The vast majority of people would expect "the core wallet" to refer to a graphical wallet. It makes sense to add a specifier for the CLI, not the other way around.

The name of the repo mostly concerns those that are already familiar with the term GUI. I see no reason to change it from `monero-gui`.

## erciccione | 2019-09-22T14:21:07+00:00
`monero-core` was changed to `monero-gui` because we usually call "core" the main Monero repo and because most of the people just called the GUI wallet simply GUI, You can verify by yourself that https://github.com/monero-project/monero-core still redirects to what now is `monero-gui`.

I'm just pointing out the in past we moved away from using 'core' and that that could crete confusion. Also, i don't think using reddit statistics in this case is useful. Beside the esponential increment of users in the last couple of years, most of the development happen on IRC and GitHub and the terminology used can be very different from the one used on reddit.

## ghost | 2019-09-22T15:09:40+00:00
We're discussing changing the branding "for the every day user" (most of the people on Reddit).

The terminology used by power users and developers (the people on IRC, GitHub) is what's irrelevant here, no?

The change you mentioned (`monero-core` to `monero-gui`) makes sense because it created ambiguity to what "_monero core_" referred to.
However, what I am proposing creates no such ambiguity. 
"_Core repo_" can still refer to `/monero-project`. Developers can still call the graphical wallet "_GUI_" because it makes sense it that context. And every day users refer to the graphical wallet as "_the core wallet_".

## scottAnselmo | 2019-09-22T16:19:21+00:00
I'm in agreement and quite like defterade's idea and looks like you beat to the punch on the mission and everyday vs technical. Repository names aren't the issue, technical contributors should know what a GUI and CLI are. I might further refine the idea to have the terminology on the downloads page, etc be 'Monero Core' app vs 'Monero Core (CLI only)' to make the GUI aspect more synonymous with Monero Core.

erciccione you do raise some good points about the failure for Monero Core to become synonymous though and it begs the question, 'Why did 'Monero Core' fail to stick?'. Looking back at the release notes and download pages, we never seemed to have described the wallet period as "Monero Core" outside of the repository names. For example the [LL release has 0 mentions of 'core'](https://github.com/monero-project/monero-gui/releases/tag/v0.12.3.0). [The download page also used the terms GUI and CLI, no 'core'](http://web.archive.org/web/20171211132015/https://getmonero.org/downloads/).

I think updating future download pages / release tags to reference Monero Core and Monero Core (CLI only) and grepping "Monero GUI Wallet" strings and replace with "Monero Core Wallet" would be feasible for this release as it's not a massive change and shouldn't break any builds... apart from the filename being monero-wallet-gui, so it may be best to hold off until next release; it's not mission critical, so if dsc et al would rather focus on refining i2p UX, etc that's going to be a bigger value add. 

I'm not an artist, but given the galaxy naming convention and use of 'core' makes me think of Star Trek warp reactor cores. There could potentially be some fun art to be had there for releases, a warp core reactor filled with butterflies, etc.

## selsta | 2019-09-22T16:27:44+00:00
Sorry, not a fan of `core`. The core team is also barely involved in the development of the GUI.

> "Core repo" can still refer to /monero-project. Developers can still call the graphical wallet "GUI" because it makes sense it that context. And every day users refer to the graphical wallet as "the core wallet".

That sounds rather confusing, especially if the CLI is named core too.

> apart from the filename being monero-wallet-gui, so it may be best to hold off until next release; it's not mission critical, so if dsc et al would rather focus on refining i2p UX, etc that's going to be a bigger value add.

Please not for this release :) We have to test things like renamed config files, etc. That’s better for v0.16.

## ghost | 2019-09-22T17:17:51+00:00
> The core team is also barely involved in the development of the GUI.

Neither is it in the development of the CLI (`git blame simplewallet.cpp`).
The CLI and GUI are the most "official" Monero wallets. They both live in the core repo and are made by the community and are _released by the core team_. I think their names should carry this weight.

> That sounds rather confusing, especially if the CLI is named core too.

The vast majority of people have no concept of a command-line interface and expect a wallet to be a GUI, "just like all the other wallets". 

For power users it is obvious to distinguish between them and so I expect that it will still be referred to as "the CLI" or "Core CLI wallet". "Monero Core (CLI only)" should draw the attention of any power user seeking the CLI and be ignored by everyone else.

## GBKS | 2019-09-26T07:53:32+00:00
I'd also try to keep it super simple and not introduce a new unique name:
Monero wallet for Windows/Mac/iOS/Android...
Monero command line wallet

I think people will mostly just say "I want to install Monero" and look for the right software package based on their use case or system. Introducing a new name (like the "Graphiko" example above) adds more complexity. I think new names are warranted for software that is created by third parties (not community efforts) or addresses non-core use cases.

## emesik | 2019-09-26T14:28:30+00:00
Why not just call it "Monero Wallet" and refer to it as "official Monero Wallet"? I see no simpler solution for that.

IIUC, the "Core" comes from Bitcoin. For someone who's not familiar with software development it might not be so apparent, but calling the GUI version "core" seems to be improper use of words. "Core" software should be automatic, require minimal user interaction and no graphical environment.

## ghost | 2019-09-26T14:54:49+00:00
>official

"Official" is meaningless and misleading in the context of a decentralized network, nothing is official. "Core" is as official as it gets.

>IIUC, the "Core" comes from Bitcoin.

Yes, the term was borrowed from Bitcoin and in the context of Monero mainly refers to [the Monero core team.](https://web.getmonero.org/community/team/)

In the context of Bitcoin: "Bitcoin Core is an open source project which maintains and releases Bitcoin client software called “Bitcoin Core”."

It would make sense to adopt a similar naming scheme for implementations and wallets released by the Monero Core team.

>"Core" software should be automatic, require minimal user interaction and no graphical environment.

For comparison, the [Bitcoin Core wallet](https://en.wikipedia.org/wiki/Bitcoin_Core) is a graphical application.

## knaccc | 2019-10-12T15:23:05+00:00
> "Official" is meaningless and misleading in the context of a decentralized network, nothing is official. "Core" is as official as it gets.

If there is an "official" Monero wallet, that implies there is an authority.

"Authority" does not necessarily imply the power to enforce. It is also used to communicate that there is a widely accepted and influential source. 

> 1a: power to influence or command thought, opinion, or behavior
(Source: https://www.merriam-webster.com/dictionary/authority )

The "official" wallet is clearly the most influential wallet software, which acts as a thought leader for other implementations.

I'd argue that the word "official" therefore clearly communicates the concept, and that the word "core" communicates very little to the average person. If anything, "core" could be confusing, as it implies that if someone wants a fully featured wallet, that they should look elsewhere, because a "core" wallet sounds like it would only contain core/basic functionality.

Of course, the makers of the wallet should not call it "Official Monero Wallet". They should just call it the "Monero wallet", and then refer to it as the "official Monero wallet" in recognition of its widely recognized status.

If the day comes when another team produces a wallet that challenges the current official Monero wallet for thought leadership, then perhaps that would be the time to refer to the current official Monero wallet as the "Monero wallet reference implentation" or by a code name.

## Thunderosa | 2019-10-12T18:22:45+00:00
'Monero Core Wallet' or 'Official Monero Wallet' are both significantly better than GUI. The CLI designation is fine and is meaningful to it's audience but acronyms should be avoided otherwise.

There seems to be consensus that the words 'Monero' & 'Wallet" are the most clear and I agree with that, simple and clear is best for this.

I think 'Official' is clearer than 'Core' and really can't think of a better word. There are words that might be more technically correct or even more meaningful, but they're not clearer to an average user getting started and that's the main thing.

## trasherdk | 2019-10-13T04:04:11+00:00
Giving the Monero wallet a noun appendix, will not magically clean Google Play for malware.

In my mind, the current names perfectly describe what is behind the names. To satisfy people,
who don't understand the tech slang (GUI/CLI/RPC) expanding the explanation might help.

Rebranding won't help with adoption, education will. Putting some distance to bitcoin would probably also help.


## trasherdk | 2019-10-13T04:26:37+00:00
**Monero GUI Wallet**
The official Monero desktop wallet with a **Graphical User Interface**.

## sanderfoobar | 2019-10-13T14:02:37+00:00
I have no particular preference on what we should call the wallet.

## binaryFate | 2019-10-14T10:25:21+00:00
I would advocate against using the term "official" in the name. It conveys too much of a centralized feeling. We are often struggling to explain to outside parties such as exchanges etc the degree of decentralization of Monero, and it would be good to avoid sending contradictory signals as part of the name of the software.

## trasherdk | 2019-10-14T14:55:27+00:00
@binaryFate I don't get it. This software is part of/bundled with the other parts of Monero.
All other wallets are 3rd. party implementations.

Would you consider running a wallet that comes with a monerod of unknown origin?

## binaryFate | 2019-10-15T09:55:21+00:00
@trasherdk I am only saying the particular word "official" is ill-suited. I agree with conveying idea that the software is the "main / core / community approved / community developed / getmonero.org / whatever" one, but I think the particular word "official" would not do the project any favor. 

Nothing can be "official" when there is no legal body such as a foundation. We have to literally explain this simple fact to outsiders on a regular basis -- they often are only familiar with highly-centralized for-profit crypto projects and assume Monero is similar.

Additionally it may make a difference in the future in some jurisdictions to protect developers and maintainers from some sort of liability that we do not want.

(I am aware people can and do use the term "official" in _everyday conversations_ to describe Monero elements such as the website or some software, that is fine -- but let's try to make some efforts to at least name important things so as not to shoot ourselves in the foot).

## emesik | 2019-10-15T10:47:25+00:00
> For comparison, the Bitcoin Core wallet is a graphical application.

And this is one of the worst software names I've encountered.

* For IT crowd, "core" is something that offers basic, essential functionality; GUI is the opposite of core.
* For laymen, "core" conveys no meaning.

Let's not repeat that mistake.

## trasherdk | 2019-10-19T09:58:48+00:00
I had actually given up on this discussion, but a few points kept nagging in the back of my head.

* Nothing can be "official" when there is no legal body such as a foundation.  

Even though I'm not a lawyer, I'm pretty confident that this is not the case. A community, such as this one, having paid representatives (Officials representing the community), can use the word **Official** to describe software developed.

* The question of liability..

Pretty much every file in this repository, and the [license](https://github.com/monero-project/monero/blob/master/LICENSEhttps://github.com/monero-project/monero/blob/master/LICENSE), contains a legal disclaimer

## hyc | 2019-10-26T17:42:34+00:00
Monero Wallet: Community Edition

## binaryFate | 2019-10-30T17:39:10+00:00
> Monero Wallet: Community Edition

I think the idea is perfect, a bit too long as is but if we colloquially say "the community wallet" whenever we speak of it, it works nicely. However it still does not convey "GUI" and distinguish from the CLI.

## SamsungGalaxyPlayer | 2019-10-31T14:59:19+00:00
"Community wallet" can refer to the GUI. "Community CLI wallet" can refer to the CLI.

## sethforprivacy | 2019-10-31T15:23:38+00:00
All for Community Wallet as well, it’s not 1999 so we don’t need to call out that the “Community Wallet” is a GUI wallet, as that’s the assumption, then specify “Community CLI Wallet” for those who want the CLI wallet specifically.

Just like all over Monero, need to make this dead simple for users to pick up the easiest option and get that sweet, sweet, digital cash rolling.

## trasherdk | 2019-10-31T16:52:23+00:00
How did you get from `Monero Wallet: Community Edition` to `Community Wallet` ?

The word `GUI` has meaning, even in 2019, just as `CLI` means something, no matter what year.

## sethforprivacy | 2019-10-31T16:59:26+00:00
Both are fine, but “Monero Community Wallet” is a bit cleaner/simpler IMO.

The bigger issue here is the catering to power user with naming the main wallet “GUI”, a term which most people don’t know and is not helpful to those that do if we name the CLI wallet accordingly (like we already do).

This should be dead simple for some random person on the internet to go to Monero’s site, click download, and immediately default to the GUI wallet (without calling it such in the name). Power users can figure out that they want the CLI wallet, average users don’t know the difference between GUI and CLI.

## sethforprivacy | 2019-10-31T17:00:16+00:00
As mentioned above, could “officially” name it “Monero Wallet: Community Edition” and just refer to it in passing as the “Monero community wallet”.

## Thunderosa | 2019-10-31T19:10:10+00:00
I really love the new 'Community' label, it's perfect and I don't think it needs to be designated 'GUI' for the average user it's just normal and expected to have a graphical interface. Designating CLI for power users makes sense to me.

This is really exciting, I love how Monero does stuff.

## jonathancross | 2019-11-02T15:56:10+00:00
Somehow "Community" doesn't quite convey that this is the "_Simple, friendly standard wallet for new users_" in my mind.

Do we have any data on how users actually search for their first Monero wallet?  Would be a great way to start rather than a bunch of use in the community guessing.  Maybe start by asking someone you know (spouse, sibling, etc) to "install a monero wallet" on their computer and watching what exactly they do.

## ITwrx | 2022-04-19T16:14:02+00:00
Many projects use "Desktop" instead of "GUI" and most people will understand what that means. i.e. "the normal wallet for a computer". 

That being said, i'm also fine with "Monero Wallet" (and "Monero CLI Wallet)", "Monero Community Wallet" (though "Community" might not convey what you want it to. It might actually be interpreted as "unofficial, less professional, less secure, more buggy, riskier edition" to a certain percentage of newcomers. Though you may choose to fight these misconceptions on purpose.), or even "Monero PC Wallet" as a "Desktop" alternative. 

"Main", "Primary", "Standard", or similar words could also be used, i suppose. 

I'm not huge on "Core" for reasons already listed.


## nahuhh | 2022-08-24T20:05:31+00:00
Monero GUI > Monero Desktop
Monero CLI > no change 

## sethforprivacy | 2022-08-24T20:17:15+00:00
> Monero GUI > Monero Desktop Monero CLI > no change

100% onboard with the changes here, really needs to happen as "GUI" means nothing to most users of the desktop wallet. I don't even call it that anymore as it just confuses people.



## ITwrx | 2022-08-24T20:21:52+00:00
> Monero GUI > Monero Desktop
 Monero CLI > no change

@nahuhh yes, this is the TLDR version. thanks :)

# Action History
- Created by: scottAnselmo | 2019-08-19T21:15:11+00:00
