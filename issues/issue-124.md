---
title: Repository needed for RFC-HWALLET-1
source_url: https://github.com/monero-project/meta/issues/124
author: michaesc
assignees: []
labels: []
created_at: '2017-10-06T13:56:10+00:00'
updated_at: '2017-10-18T13:33:04+00:00'
type: issue
status: closed
closed_at: '2017-10-18T13:33:04+00:00'
---

# Original Description
## New Repository

Since others are already showing interest and even offering to participate, we need a repository for the current hardware wallet work underway.

> Let's give the hardware wallet an Esperanto name.
> - fluffypony, 20171006, 08:14:28
>
> Hardware in Esperanto is Aparataro.
> - rehrar, 20171006, 08:58:08
>

The repository should be named _aparat_ and be subtitled _Hardware wallet (RFC-HWALLET-X) monero project sources:_

monero-project/**aparat**
Hardware wallet (RFC-HWALLET-X) monero project sources

While not required it would be nice  to have some form of administrative privilege of this repository, so I can give push or merge permissions to trustworthy teammates.

# Discussion History
## anonimal | 2017-10-06T19:15:47+00:00
Hi @michaesc,

1. Can we find an official, non-google, translation for "hardware wallet" or "hardware" in the context of a hardware wallet?
2. If we stick with aparataro, then why not `monero-project/aparataro`?

## rehrar | 2017-10-06T19:18:34+00:00
I've been fostering a good relationship with the people in the ##esperanto IRC channel. I'll ask them. I'm learning Esperanto too for this purpose btw. 

## michaesc | 2017-10-06T19:57:02+00:00
I don't like aparataro because it's (1) hard to spell, (2) slow to type, has (3) four 'a' characters, (4) and not about the same size as 'monero.' That's why I shortened it, but to be honest this preference is not a strong one. We can use 'aparataro' if that seems better.

On the other hand, I wonder what 'wallet' or 'purse' is translated to. That would be a much better term probably, since 'hardware' may not be descriptive enough once a second hardware project starts.

I'll bet rehrar can help find a good term leveraging his Esperanto connection. It was his idea with 'aparataro' that helped us get started, after all.

## rehrar | 2017-10-07T21:54:58+00:00
Alright, me and the Esperanto guys hashed out what would be acceptable in this instance, so I'll give some of the ideas we covered:

- Aparata: this is an adjectivized "aparataro" (anything ending in "a" is an adjective in Esperanto), and while it doesn't have the noun beside it, the noun can be implied. So the translation would be "Hardware (implied: wallet)"
- Aparata Monujo: Monujo is wallet in Esperanto, and this is what the full "Hardware wallet" would look like.
- Aparato: This means "apparatus", but may still work in this context.

My vote would be for Aparata, despite it still having four 'a' characters as @michaesc wasn't too thrilled about. I think it servers the purpose well enough.

## michaesc | 2017-10-08T19:02:30+00:00
I like all three choices quite a lot:

- Aparata
- Aparato
- Monujo

...namely because they are not too long and easy enough to spell when hearing the word over phone or voice whatever. Having four _a_ characters is much more of a bummer when combined with multiple _r_ characters and many consonants.

Too bad that the real translation for _wallet_ is _monujo_ because it resembles _monero_ too much, don't you think? By the way, it seems that _purse_ translates to _mansaka_, but this sounds a bit weird to me.

It's a bit hard for me to vote for the translation of _hardware_ since others in the community are interested in hardware projects of their own, like an ATM machine.

Should we therefore choose _aparato_ or should it be _aparata_ as @rehrar prefers? It would be very nice of @anonimal to break this tie vote, unless he's unhappy with both choices.

## michaesc | 2017-10-10T11:00:26+00:00
Both glosbe.com and dicts.info translate _device_ and _appliance_ to the word **aparato**. It's still a bit generic, but I couldn't find a way to shorten two or more words describing the wallet nature.

Please make the repository:

monero-project/**aparato**

...and we'll change it later if there is opposition.

## QuickBASIC | 2017-10-10T13:35:43+00:00
Considering we've taken some liberties with Esperanto for our purposes, (SI prefixes for Monero denominations drop `mo` i.e. `piconero`,  `nanonero`, `decinero`, etc), I don't feel like we have to be perfectly grammatically correct. In fact in this example, we've lost the root of the Esperanto word which is `mona` (money) and left `ero` (bit) and made the names nonsensical in Esperanto, which I feel is okay.

We have to remember that we're creating a brand name, as such, we don't want to just have plain language descriptions of things. If our official wallet is simply named `hardware wallet` we can't exactly be upset that someone else uses a similar name. (The Android mobile wallet is already called `Monerujo` which translates literally with the affix `ujo` (container) added to the base `mona` (money), so `money container`. 

I don't feel that creating a neologism if appropriately using Esperanto affixes is a bad thing. I propose possibly: 
* `Monestro` (money master/leader/boss); similar to `lernejestro` (a school principal), `urbestro` (a mayor, from 'city'), `centestro` (a centurion, from 'hundred')
* `Monilo` (money instrument/tool); similar to `ludilo` (a toy, from 'play'), `trancilo` (a knife, from 'cut'), `helpilo` (a remedy, from 'help'), `solvilo` (a solution, from 'solve')
* `Moningo` (money holder/sheath); similar to `glavingo` (a scabbard, from 'sword'), `kandelingo` (a candle-holder), `dentingo` (a tooth socket), `sraubingo` (a nut, from 'bolt'), `piedingo` (stirrup, from 'foot'), `kuglingo` (a cartridge, from 'bullet')

Honestly I think we need to disambiguate from the 'wallet' paradigm. Wallets hold things, you don't take a series of bits and stuff them in a file or hardware wallet like you do a paper bill that you put in a physical wallet.  If you lose your physical wallet with physical bills in it, that money is gone. Cryptocurrency wallets are more like keys that unlock your funds that are stored elsewhere (the blockchain). This concept of wallets is why so many new users are confused about how cryptocurrency works. (How many of you have interacted with a newbie who's scared that his wallet file was lost or corrupted because he didn't realize his coins were safe on the blockchain waiting to be unlocked by the keys that he can restore from his seed?)
* `slosilo` (lock tool i.e. `key`)
* `slosilringo` (key ring)
* `elcifrigilo` (cryptographic-key literally tool for decoding')

Juxtaposition (concatenating nouns/verbs) is allowed in Esperanto in some cases, so:
* `cifrimonilo` (a tool for encrypting money)
* `cifrimoningo` (a cryptographic money holder)

We have to remember that Esperanto is like other languages where there are root words and affixes that make up the word. (In English we have greek root words, german root words, latin root words, etc that we add affixes (suffixes and prefixes to) to make up words. BUT it's taken to a whole new level. (You can take any root word and add affixes to it to give it a new meaning, action, amount, or clarify what it is.

 See this [List of Esperanto Affixes](https://en.wikibooks.org/wiki/Esperanto/Appendix/Table_of_affixes). I think we can be more creative than calling the hardware wallet `apparatus` in Esperanto.


## QuickBASIC | 2017-10-10T14:24:20+00:00
Just adding. My favorite is `Monestro` (money master). The Monestro Project has a ring to it and it's extended name and/or description can be "the Monestro hardware wallet". It keeps 'Mone' to liken it to Monero, while still having a meaning in Esperanto that's not literally describing what it is, but gives a good idea of what it does, it is the master of your money. (i.e. it keeps track of your money.)

## michaesc | 2017-10-10T14:39:50+00:00
Excellent that @QuickBASIC found the time to provide a urgently needed bit of creativity, thanks. Many of your suggestions are better than what we had before. Although I like _money master_ (monestro) best, the name _monero_ postfixed with the suggested **slosilo** seems best from a differentiation standpoint.

![image](https://user-images.githubusercontent.com/4779602/31392115-b1870200-add8-11e7-9cb8-9303523d45cd.png)

You're right that anything with wallet perpetuates a failed communication policy and a simple hardware or device word is too lame. If nobody objects, let's please create the repository:

[monero-project/**slosilo**](https://github.com/monero-project/slosilo/)

## QuickBASIC | 2017-10-10T14:53:21+00:00
Thank you. I was throwing out thoughts to stir the pot of creativity. Thank you for recognizing that. The only problem with 'slosilo` is that there exists a [project](https://github.com/cyberark/slosilo) with that name already.

Our affinity for it might be from it's similarity with the German Schlüssel. I'm certain you're eager to have the repository set up, but certainly we can leave some time for others to further comment and discuss.

## michaesc | 2017-10-10T14:57:44+00:00
I read your addendum too late, before suggesting _slosilo_. Should we use _monestro_ instead? That would look like this:

![monestrologo](https://user-images.githubusercontent.com/4779602/31393466-0f3f1632-addc-11e7-9bcb-b3b8deb9a840.png)

## QuickBASIC | 2017-10-10T15:00:00+00:00
I agree that the name `Monestro` is lacking simply because it is too visually similar to `Monero`.  Kovri simply means onion in Esperanto, but has great connotations for what the software does... I was hoping that someone would be inspired to make better suggestions that I already have... I think you're right we should not use `Monestro`.

## michaesc | 2017-10-10T15:13:03+00:00
Yes, it's no problem to take some time to get it right. A couple frankenwords that fit are:

- cifrimon
- silringo

And two other combo names are:

- finestro
- bankestro

I hope I'm correct about _finance boss_ translating to **finestro**. That would look like this:

![finestrologo](https://user-images.githubusercontent.com/4779602/31394281-3bcdbb52-adde-11e7-9731-cf0d7b798087.png)

## michaesc | 2017-10-10T15:14:12+00:00
By the way, there are no repositories on GitHub named **Finestro** so we're at least partially safe with this one.

## ghost | 2017-10-10T15:18:10+00:00
Using the Esperanto word "banko" (bank): Bankilo (using the suffix ilo = an instrument).

Senriska also means "safe (money)". Doesn't even need to play with suffixes or prefixes.

I also like Finestro and Bankestro.

## QuickBASIC | 2017-10-10T15:26:16+00:00
Sorry for multiple relies, but having some time on lunch break, I gave it some more thought.

Maybe we're being too literal.
* `testudo` is turtle, who have a tough exterior and protect their insides
* `urso` is bear, which is very protective of their young
* `raketon` is raccoon, which is very sneaky
* `kokoso` is coconut, which has a hard shell to break
* `volbo` is vault.

## michaesc | 2017-10-10T15:36:05+00:00
Do you @QuickBASIC strongly prefer any of those nonliteral names, or what about _finestro_ or _bankestro_? Would losing the _boss_ and replacing with _instrument_ benefit?

Another idea is _vault boss_ or **volbestro**.

They are possibly too literal, buy my preferences so far are:

1. finestro
2. volbestro

## QuickBASIC | 2017-10-10T15:45:39+00:00
Just not reading both @michaesc and @ViolentlyPeaceful replies:

I like `Finestro`, but I'm sure it's technically correctly smooshed together from the root `financo` and affix `-estro`... I believe `financoestro` is technically correct, which is a mouth-full.

`volbestro` is nice too, but once again. I'm not certain about exactly how affixes are appended to roots, so I'm not sure how proper it is.

## michaesc | 2017-10-10T15:51:56+00:00
It's quite possible that we're perverting Esparonto with these smush words, but no worse than Whatsapp or RaspberryPi does. Also _fintech_ is quite prevalent in this space, so possibly _finboss_ would work for the same reason, when translating to **finestro**.

## QuickBASIC | 2017-10-10T16:04:49+00:00
> It's quite possible that we're perverting Esparonto with these smush words

Maybe. We'll probably offend some language nerd (non-pejorative nerd meaning) somewhere, but I believe we're fine creating neologisms in Esperanto (Part of the fun of the Esperanto version of Scrabble, is convincing others that the word you just created is validly crafted and has a real meaning.) 

I'm not in love with `finance` as the root, because finance is such a large topic and carries connotations of economic scale. Money is personal.

Nobody likes `kokoso` for coconut apparently? We'd have onions and coconuts.

## michaesc | 2017-10-10T16:19:24+00:00
The difference between kokoso and inkasso is small enough to make me think of debt collection and bankruptcy due to germanics, but I'm likely alone in that category. It would be nice to have a vegetables theme, but I'm failing to come up with good examples. Maybe truffle or potato.

What about a word or multiword conveying personal money like _privafond_, _privafondo_, or _privamon_?

Or _privolbo_ which is made from _privata_ and _volbo_?

Most people will think that 'priv' stands for 'private' which almost makes for a dual benefit in our case. If any of those seem good enough @QuickBASIC can you say which two are the favourites?

## generalizethis | 2017-10-10T16:40:22+00:00
What about sekura or volbo?

## ghost | 2017-10-10T16:53:16+00:00
_Durio_ is the Esperanto word for the Durian fruit (also known as the king of fruits). I like it because it also reminds the latin word _durus/durum_ that means "hard", which you will see the similarity in neo-latin languages like French (dur), Spanish (duro), Portuguese (duro) and Italian (duri).

## jrob-io | 2017-10-10T17:00:19+00:00
Possible verbs with app-eqsue names:
- deponi = to bank, to deposit
- formeti = put away, store
- ŝpari = save, spare 
- gajni = earn, gain, win


## rehrar | 2017-10-10T17:01:52+00:00
Whatever names reach a rough consensus, I would like to take the Esperanto community just to triple check. I realize not everything has to be super accurate, but it'd still be good to get their opinions on what we've decided.

## QuickBASIC | 2017-10-10T17:10:49+00:00
@rehrar 

It would be nice if they could take part of the discussion here, but I understand many of them probably don't have a GitHub account. I do agree that their opinions would be beneficial so we don't name it something dumb.

## serhack | 2017-10-10T17:14:42+00:00
Monero Hardware (In esperanto)

## bitofdon | 2017-10-10T17:22:15+00:00
I really like Volbo. It's pretty easy to remember

## michaesc | 2017-10-10T17:34:07+00:00
@flavoredtaco Do you like _volbestro_ (vault boss) as well, or prefer the simpler variant?

The ones by @jrob-io _deponi_ and _formeti_ are quite nice. Would they be best left alone or combined with _ilo_ (instrument) to become:

- deponilo
- formetilo

![formetilogo](https://user-images.githubusercontent.com/4779602/31401049-e1d2bef4-adf1-11e7-8295-0ec6f8907f2a.png)


## michaesc | 2017-10-10T17:43:22+00:00
Do you @ViolentlyPeaceful prefer simple _durio_ (durian) or _durestro_ (durian boss) combined? I follow your logic and it's quite good. Those are expensive fruits, and it would keep us on the food trajectory.

As some english speakers equate money with bread, we might consider _panestro_ (bread master.)

On a related note, _benjeto_ is the word for _doughnut_. A bit bizarre, but no more so than Raspberry Pi.

## miziel | 2017-10-10T18:36:12+00:00
sekura - secure, safe 
monero sekura sounds good, doesn't it?
I also like monestro, although google translate gets it as "monster" (stupid ai?)
How about metomono (as in "I put money"?) or lokomono ("I place money")? (not sure if this translates correctly...)

## QuickBASIC | 2017-10-10T18:45:58+00:00
> google translate gets it as "monster" (stupid ai?)

Google Translate uses statistical machine translation and there's not a lot of Esperanto text out there (as it's an invented language), so the translation is very bad.

## michaesc | 2017-10-10T19:00:46+00:00
Yes @miziel monero sekura does sound quite good indeed. What do you think @QuickBASIC about it, does it need a -boss or -instrument addition?

![sekuralogo](https://user-images.githubusercontent.com/4779602/31404929-bda9baa8-adfd-11e7-9b73-17f4ee545731.png)

The combination gives Monero a **stable and secure** marketing sound. There is no other Github repository with the name _sekura_.

## ghost | 2017-10-10T19:15:12+00:00
There are many good options out there, I think we should make a shortlist with maybe 3 to 5 options, confirm the names with the Esperanto community and then decide in one. Make even a public poll if you want. 😜

@michaesc both _durio_ and _durestro_ sound good. I like durio a little bit more because you can buy "hack" domains like dur.io or getdur.io (to follow the getmonero trend). But I also know that many people dislike these domain hacks.

## stamparm | 2017-10-10T19:18:34+00:00
+1 for Sekura. "Monero Sekura" sounds really good (IMO)

## JollyMort | 2017-10-10T19:34:27+00:00
I like Moningo. Btw, google translate auto-detected it as Japanese and translated into "Even a person". Even a person can use Monero, yeah :D 

## michaesc | 2017-10-10T19:40:31+00:00
Okay @stamparm I think you're the only one who has provided a **fourth grade of consensus**, after @generalizethis, @miziel, and myself @michaesc.

Would it be okay with us all, if @rehrar takes _monero sekura_ to the Esperanto community for their blessing? If they say anything but 'yes, good' then we'll keep trying other options?

## ghost | 2017-10-10T19:43:15+00:00
> **Kovri** simply means onion in Esperanto

@QuickBASIC In what sense? “Kovri” means “to cover”; onion (fruit) would be “cepo”.

> **`raketon`** is raccoon, which is very sneaky

“Raketo” is a rocket. Raccoon is “lavurso”.

> **volbo** is vault.

Only in the sense of a ceiling, though. (Not sure if you're aiming for that.)

> **cifrimonilo** (a tool for encrypting money)

Actually, the main part of the root(?) has to come last, so this would be “a tool for ‘money used for encryption’”, or something along those lines.

> How about **metomono** (as in "I put money"?) or **lokomono** ("I place money")? (not sure if this translates correctly...)

@miziel “Placing money” and “placing money”, respectively; see above.

> I hope I'm correct about finance boss translating to **finestro**.

@michaesc “Fino” means “end”, so this would be master of ends. Finance boss would have to be “financestro”.

> **formeti** = put away, store

@jrob-io “For” may hint that you don't intend to take back whatever it is that you're putting away, so I would look for other options.

-----

“Sekura” is fine when used in combination with “Monero …”. Technically the whole name would mean “Secure Coin”, but I suppose that's not an issue with a brand name.

## bitofdon | 2017-10-10T19:47:06+00:00
@michaesc i think keeping it simple is the best Volbo > Volbestro (in my opinion)

## michaesc | 2017-10-10T19:47:13+00:00
Wow @F3nd0 quite some mastery of the language, and thanks for the corrections and advice. It seems one of the options that's both linguistically correct and might positively influence understanding of the project is _Sekura_, which seems to be the direction in which we're headed.

## michaesc | 2017-10-10T19:48:54+00:00
Did you @flavoredtaco see the comment where _volbo_ means a type of ceiling? It seems adding _boss_ (which I like a lot in general) would lead to the meaning **ceiling boss**.

## QuickBASIC | 2017-10-10T20:09:03+00:00
@F3nd0 Thank you for all your feedback.

> @QuickBASIC In what sense? “Kovri” means “to cover”; onion (fruit) would be “cepo”.

Probably misremembered from somewhere and reinforced by the logo. In any case, all my examples were from a poor attempt to understand the language from Google searches today.

> Actually, the main part of the root(?) has to come last, so this would be “a tool for ‘money used for encryption’”, or something along those lines. 

Is it possible to express a tool for encrypted money with compound words in Esperanto? 

## rehrar | 2017-10-10T20:24:52+00:00
@F3nd0 is from the Esperanto community on IRC. I asked them to come by and weigh in and he did. Let's all sing happy birthday to them as a thank you.

(P.S. I vote 'Sekura')

## ghost | 2017-10-10T20:31:44+00:00
Oh and here's a note: Esperanto has some letters with hats. When it's not feasible to use those, it's most common to use either the (standard) h-system, or the x-system. So instead of “ĉ ĝ ĥ ĵ ŝ ŭ”, you can type either “ch gh hh jh sh u” (no “uh”) or “cx hx hx jx sx ux”. The former is original, while the latter is always unambiguous (because there is no “x” in Esperanto's alphabet). Both are in use today, and should be preferable to simply omitting the hats.

Also, I would advise against using a generic name if “Monero …” is not to be included in the full name. In my opinion, it's generally not a great idea to give apps generic names. For “monujo”, consider how “wallet” would work for a name; for “sekura”, consider how “secure” would work for a name. The "Monero …” part removes the issue by making a unique combination (from a brand name).

> Is it possible to express a tool for encrypted money with compound words in Esperanto?

@QuickBASIC Yes, it should be. Perhaps “ĉifra'mon'ilo” or “ĉifro'mon'ilo” would be appropriate, though I haven't given it the necessary thought to say for sure.

## bill-mcgonigle | 2017-10-10T21:37:55+00:00
I took a brief look around at other concerns named 'Sekura'.  There is a company that sells anti-shoplifting gear, a windows and doors company, a non-lethal defense products company, a bike/motorcycle lock company, etc.  In finance it looks like there used to be a Sekura company but that is [out of business](https://www.bloomberg.com/research/stocks/private/snapshot.asp?privcapId=22354902). I didn't see anybody doing something like a hardware wallet.



## KeeJef | 2017-10-10T21:58:08+00:00
Adding my vote for Sekura 

## QuickBASIC | 2017-10-10T22:01:06+00:00
I like `Sekura`. Nice and short and a decent rough cognate with English `secure`, Spanish/Portuguese `seguro`, Swedish `säkra`, etc.

## Fankadore | 2017-10-10T22:03:27+00:00
Google tells me that "Access" translates as "Aliro". I think the verb "To Access" would be more appropriate, "Aliri". If we don't have to stick to strict Esperanto then I would stylize as Alira, but I suppose that could mean "Accessible", which is the opposite of what we're getting at.

## Alex058-2 | 2017-10-10T22:04:54+00:00
Hi, I think that "to carry" translates to "Vesto" in Esperanto. Nice short name, "Monero Vesto". Not sure if there are other projects with the name Vesto though. On the Monero-reddit I posted this name too, more people seem to like it.

## miziel | 2017-10-10T22:12:07+00:00
How would "a vessel to carry", a carrier, be in Esperanto?

11.10.2017 00:04 "Alex058-2" <notifications@github.com> napisał(a):

> Hi, I think that "to carry" translates to "Vesto" in Esperanto. Nice short
> name, "Monero Vesto". Not sure if there are other projects with the name
> Vesto though. On the Monero-reddit I posted this name too, more people seem
> to like it.
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/meta/issues/124#issuecomment-335622177>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AYbirOib20os0o-ecgsqvoVAcfvOX2GWks5sq-oIgaJpZM4PwhNW>
> .
>


## miziel | 2017-10-10T22:32:33+00:00
1.  Is it definite that name be "Monero smth"?
2. @F3nd0 would sekurio be a grammatically correct word?

## emesik | 2017-10-10T22:35:57+00:00
Perhaps `monsekura`? There's [monkarto](https://eo.wikipedia.org/wiki/Monkarto) so I hope _monsekura_ won't be a linguistical abomination. And it doesn't exist in search engines, we have easy positioning here.

We could easily go Spanish with nice sounding `monedero`, but this is every-day word, which might not serve well.

Also I like `testudo`. Has a nice sound and meaning.

PS: Esperanto word `fido` means _confidence, faith, trust_. `monero-project/fido`?

## enricodias | 2017-10-11T04:41:02+00:00
I don't like `aparato`. In Portuguese it means a group of items that perform an action (kinda) and it doesn't sound good for a wallet.

`Vesto` sounds good.

## gregchinsue | 2017-10-11T06:11:19+00:00
Instead of a bank or vault that conveys more a sense of a place for multiple people to store coins, how about going with something that is seemingly more personal or local like a wallet would be:

- **kesto** = box, chest (of treasure), coffer, crate, trunk, ark, or case (of beer!)
- **keston** = accusative singular of kesto
- **kofro** = trunk, chest (of treasure not body part)
- **kofron** = accusative singular of kofro


## ghost | 2017-10-11T09:27:58+00:00
> Hi, I think that "to carry" translates to "**Vesto**" in Esperanto.

@Alex058-2 “Vesto” is an article of clothing. “To carry” would be “porti”.

> How would "a vessel to carry", a carrier, be in Esperanto?

@miziel If we're talking about some sort of a container used to carry pretty much anything, then “portujo” would be fitting.

> @F3nd0 would sekurio be a grammatically correct word?

Technically it has a correct _form_, but has no meaning, and would present a new word root. (“-i'” is not a proper affix, either, so it can't be interpreted as “sekur'i'o”.)



## anonimal | 2017-10-12T21:12:48+00:00
Monestro.

Note: in 2015, "Sekreta" was among the ballot of Kovri's first name until I, FP, and community decided on Kovri. I long ago reserved 'Sekreta' for a future Kovri anonymity protocol though.

Sekuro(a) != Sekreta but perhaps they are too close for comfort?

## Alex058-2 | 2017-10-13T05:35:41+00:00
“Sekreta” would not go down well in Dutch-speaking countries, eg The Netherlands, because it sounds and looks like “sekreet”. That’s a not a nice thing to say to someone in Dutch. 

## Keksoj | 2017-10-17T19:45:39+00:00
Hi Guys, I gave a hand improving the GUI's esperanto translation, please tag me when you have such esperanto-naming discussions :-)
I'm fluent BTW. 

## anonimal | 2017-10-18T05:34:11+00:00
>“Sekreta” would not go down well in Dutch-speaking countries, eg The Netherlands

Can't make everyone happy.

## QuickBASIC | 2017-10-18T13:27:39+00:00
https://github.com/monero-project/sekura

The repository has been created. @michaesc, do you mind closing this issue?

## michaesc | 2017-10-18T13:33:04+00:00
Thanks folks, we had almost fifty suggestions and it seems like half of them were valid. Since **sekura** got +11 votes and no minus casted, we'll use that for the project code name.

If the decision seems a bit opaque, it's due to a couple reaons. Namely, after two weeks we hardware developers can't afford to go without a repository any longer. Also the marketing name of whatever is delivered will be chosen outside the scope of this project, so there may be a 'anniversary' hwallet, 'kovri' hwallet, DefCon party hwallet, whatever... That's when we need to consider Esperanto logic and marketing a lot more, and hopefully we can collaborate again.

I'm still incredibly impressed by **our teamwork and individual Esperanto knowledge,** so thanks to all of us and please keep in touch by monitoring the new repository and project pages:

https://github.com/monero-project/sekura/
https://taiga.getmonero.org/project/michael-rfc-hwallet-1-implementation/

For extra fun, consider participating as a tester for the chance at a [device preview.](https://taiga.getmonero.org/project/michael-rfc-hwallet-1-implementation/wiki/preview/)

# Action History
- Created by: michaesc | 2017-10-06T13:56:10+00:00
- Closed at: 2017-10-18T13:33:04+00:00
