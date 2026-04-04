---
title: Remove "reasonably" from "reasonably private" on the homepage
source_url: https://github.com/monero-project/monero-site/issues/971
author: SamsungGalaxyPlayer
assignees: []
labels:
- 💬 discussion
created_at: '2020-05-09T16:45:24+00:00'
updated_at: '2020-06-12T13:49:56+00:00'
type: issue
status: closed
closed_at: '2020-06-12T13:49:56+00:00'
---

# Original Description
Initial MR: https://repo.getmonero.org/monero-project/monero-site/-/merge_requests/1136

Related discussion: https://repo.getmonero.org/monero-project/monero-site/-/merge_requests/1219

Related discussion: https://www.reddit.com/r/Monero/comments/f2m7la/a_reasonably_private_digital_currency_why_say/

While I agree that being careful about wording is prudent, I think this wording causes more confusion than anything else. We should point people to other, more detailed resources like the MRL papers and Breaking Monero if they are interested in understanding this further.

We can add some text to the downloads page description saying something along the lines of the following:

---

On this page you can find and download the latest version available of the Monero software, as well as hardware, light and mobile wallets. Monero is experimental software. **While it provides far greater privacy out of the box than other tools, you should understand the limitations if you are concerned about your privacy.** Using Monero without changing your habits, as with using Tor, isn't sufficient for all use-cases.

# Discussion History
## erciccione | 2020-05-10T12:48:33+00:00
My opinion is [on the old MR on Gitlab](https://repo.getmonero.org/monero-project/monero-site/-/merge_requests/1219#note_8930)

## dginovker | 2020-05-11T20:53:46+00:00
If Monero wants to keep people private, we want people to be use the tools most easily adopted for privacy. We should encourage and promote Monero, not hide behind words like "reasonably" in case someone does something silly like share their private key.

## geonic1 | 2020-05-11T21:19:53+00:00
+1 for “reasonably”. It appeals to people's sense of reasoning and has the added benefit of not pigeonholing Monero as a “privacy coin”. I.e. it is reasonably private in the same way that it is reasonably fast and reasonably scalable.. the description is inclusive rather than exhaustive.

## bitlamas | 2020-05-11T21:26:53+00:00
Particularly speaking, I would remove that word, I do not necessarily see how much benefit it brings versus the misinterpretation it can cause to new users.

Semantically this word is the most accurate description, because there are specific scenarios where an entity with unlimited resources could decrease the efficiency of certain elements of the protocol that integrate the privacy aspect of Monero. Such scenarios need not be explained here and can be found in the Breaking Monero series available on YouTube.

That said, it would not be the first nor the last time in the history of languages where we have assigned an adjective to something without that adjective being true in absolute 100% of cases. Bulletproof cars are not bulletproof against all types of ammo out there, and yet it would make no sense to market them or present them as _reasonably_ bulletproof. The impact of using such a word could cause a potential user to choose another car armor provider that does not demonstrate on its home page with large letters the possibility that the product might not work properly in very specific scenarios, although I'm sure this is explained later when the user decides to buy such product. No product makes it so clear on its home page (or in its packaging with very large letters) that the product may not work properly **if** you use it incorrectly or in extremely exceptional cases, so I don't see why it should be the same with Monero. I think there's a case to be made where having the word there might make a new user unnecessarily raise an eyebrow.

Knowledge of such exceptional cases can and should be explained at a later time to the user, but I see no compelling case to be on the home page other than a way to defend ourselves from a troll that will one day write an article about Monero accusing the website maintainers of being bad actors because they wrote that the protocol is private and there are exceptional cases where the protocol is only _reasonably_ private.

Another alternative would be to simply change the headline to something like privacy-protecting digital currency, or privacy focused, or something else.

![image](https://user-images.githubusercontent.com/34245203/81612908-8e0b0900-93ab-11ea-8dd6-6df3235e7d8d.png)


## SomaticFanatic | 2020-05-11T22:04:23+00:00
While we’re at it, can we please remove the “Monero is Untraceable” paragraph? Technically I love Moneros untraceability but for the layperson it sounds like it’s made for people to do crimes and not get caught.

## geonic1 | 2020-05-11T22:08:50+00:00
![81612908-8e0b0900-93ab-11ea-8dd6-6df3235e7d8d](https://user-images.githubusercontent.com/48529862/81616892-3663a200-9399-11ea-86e0-eedfb693e37c.png)
That looks good!

## Gingeropolous | 2020-05-12T12:07:07+00:00
Or, yah know, we just call it MONERO: A Digital Money

I still think calling money private is like calling water wet. 

its inherently private, due to needing a fungible nature to be money. 

Its only because of bitcoin and the other transparent cryptocurrencies that privacy is even thought to be a novelty. 

are we to carry the semantic (or perhaps technical) debt of flawed technology?

to carry the bulletproof car analogy, it'd be like making a bullet proof car that actually stops bullets and calling it a "Bullet resistant bullet proof car".

but then again, I bought a Mr. Coffee machine because I figured if you call yourself Mr. Coffee, you probably know what your talking about. I hate marketing. Its like consciousness hacking. 

But if we're gonna go the route of calling Monero private cryptocurrency, we should also call it Monero: A privacy-protecting digital decentralized permissionless cryptocurrency. 

even though a cryptocurrency should be permissionless, decentralized, and private (fungible). 

so how far do we carry the burden of shit technology?



## binaryFate | 2020-05-12T13:11:56+00:00
I would remove "reasonably" from the homepage. I was fairly neutral on this but now I I think it makes a point that is only understood in nerdy circles, otherwise it seems to confuse most people.

There are ample resources presenting an honest and cautious picture to users, this phrasing in particular is overdoing it.

## erciccione | 2020-05-13T07:02:32+00:00
[The last discussion on reddit](https://www.reddit.com/r/Monero/comments/ghuwsx/discussion_remove_reasonably_from_reasonably/) seems to suggest most people (at least who replied to that post) are ok with keeping "reasonably". For now the community appear to be split on this.

## Sunray-Nucleon | 2020-05-18T17:22:08+00:00
I say yes we should remove it. 
**A Reasonably Private Digital Currency** 
and the **A** suggests there are more like this, but i think Monero is unique. So i think we should go for **Private Digital Currency** as it already is, by the way, in the German version **Private Digitale Währung** is **Private Digital Currency**

edit: But does "private" imply something else, like "not public" or so? Than i would say, yes, privacy protecting is very good. It also implies that it probably can not do everything for your privacy, but it is protecting it.

## binaryFate | 2020-05-18T17:57:49+00:00
"Privacy-preserving digital currency"

it is longer and more convoluted, but that conveys the best meaning

## Sunray-Nucleon | 2020-05-18T19:59:40+00:00
"currency" sounds like something abstract to trade with, for professionals; why not Privacy-protecting digital **money** - true we know it is more as money, can also be utilized for messaging and so on, but money sounds more catchy for all sorts of people. And a main aspect is to be like money, to behave like money. And money has a world-wide meaning somehow. Currency sounds like something regional or something with specific aspects or limited possible field of application. Money is just world-wide and already sounds like cash money without saying this.

'preserving' is to concluded imo - it is still the case that if you are using it wrong, its capabilities are naturally limited or than can not preserve it, but is still protecting its users furthermore

## geonic1 | 2020-05-18T20:14:01+00:00
Should we get a vote on "Privacy-preserving digital money"?

edit: "privacy-preserving" has the added benefit of conveying that "privacy" is the natural state of things.

## Sunray-Nucleon | 2020-05-18T21:24:02+00:00
i was thinking that privacy is used to much and has a negative connotation because of all the privacy debates and privacy breaches - some people are maybe averse to the term. maybe they don't understand it at all or just thinking like "i don't want to have anything to do with privacy, i have nothing to hide" tbh i've been hearing this a hundred times the last years even making me sick to talk about privacy. so how to try to avoid this term? it is a fundamental human right in the western world (but maybe not in areas we could and should also reach with the global digital money)
how about something like **liberty-preserving digital money** or **freedom-preserving digital money** by thinking about this, a talk of riccardo is coming to my mind: he was saying something like we should build and distribute technology that acts like a privacy trojan horse! ideally people are using it without even noticing that it is privacy protecting, its just a base layer with this in mind from beginning on. people are just using it and it brings privacy but that should be the standard. we don't have to write 'something privacy' on our front door but we are still always try to best protect the users as main focus

## erciccione | 2020-06-05T12:29:56+00:00
@SamsungGalaxyPlayer I would say let's discuss this next community meeting, so we can take a final decision. What about that?

Also @moneromooo-monero could be interested, since he initially suggested to add "reasonably".

## erciccione | 2020-06-07T08:44:14+00:00
During yesterday's community meeting it was decided to remove "reasonably". If somebody has the log, please post them here.

#1032

# Action History
- Created by: SamsungGalaxyPlayer | 2020-05-09T16:45:24+00:00
- Closed at: 2020-06-12T13:49:56+00:00
