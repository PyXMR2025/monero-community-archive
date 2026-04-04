---
title: Discussion about CCS translations
source_url: https://github.com/monero-project/meta/issues/732
author: netrik182
assignees: []
labels: []
created_at: '2022-09-06T08:26:47+00:00'
updated_at: '2022-09-28T14:49:49+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
It has been recently decided to disallow CCS translations [(source)](https://web.archive.org/web/20220731193144/https://monero.observer/monero-community-decides-disallow-translation-ccs-proposals/), as the system has been gamed in the past and the fact that we lack contributors to do reviews. It's worth mentioning that translation to all our resources **are still possible and encouraged**, and can be done via our Weblate instance at https://translate.getmonero.org/

As already publicity stated on #monero-translations some time ago, I'm personally in favor that translations are done voluntarily, from the logs:
```
<netrik182>	it's hard to assess a translation css because the content must be not only translated but also reviewed. And the latter is hard to achieve when the former was paid work
<netrik182>	and also because translations, specially for monero-gui and website, need to be updated from time to time
<netrik182>	I'm speaking for myself, of course, not for the workgroup. But I'd rather have volunteer work and so, community members will translate on their free time
<netrik182>	that's the 'magic' about Weblate and really any other translation tool
<netrik182>	people can just go there, submit some translations then others will come and agree with that translation, correct it if needed
``` 

However, some translators have voiced their desire to get paid for translation work via CCS and I would like to have a broader discussion on how we can move forward. There are a couple of alternatives:

- bounties.monero.social could be an obvious alternative. Personally I think it would have the same cons as CCS if the bounty terms requires the work to be reviewed before paying out.
- volunteer work coupled with donations. We have some long time contributors who could possibly ask for donations after or even before they have done some translation work by posting their addresses on a reddit post, for example. 
- translators / reviewers setup donations using @plowsof's [wishlist as a service](https://github.com/plowsof/xmr-wishlist-aaS)
- have a `xmrtranslatorslist` similar to this https://bitcoindevlist.com/ so that translators don't need to setup the waas themselves

It goes without saying but the alternative donations routes, except for the bounties, would work the same way volunteer translations work. That is, contributors go to weblate and submit their translations and those translations get reviewed organically. In fact, as we have more and more translators being incentivized by spontaneous donations, they would be capable of not only submitting translations but also review translations submitted by others.

Anyway, please leave your suggestions and concerns.

# Discussion History
## erciccione | 2022-09-06T13:59:27+00:00
I have to clarify this because for some reason got forgotten. I pointed it out recently, but i'll clarify it again for correct context:

CCS for translations has been already suspended in agreement with @Luigi1111 long time ago, when i was still coordinating. Some contributors opened a series of CCS for translations, but used automatic tools for the actual work, which resulted in poor quality work. After that we decided that it was too time consuming and basically impossible to assure the quality of each contributor and suspended the possibility of opening new proposals for translations. We still used [the small fund of the Localization workgroup](https://github.com/monero-ecosystem/monero-translations/blob/master/rewards.md), that now has been given back to core, to review the still ongoing CCS.

The problem is that it's very hard to evaluate translator's work for a coordinator, we tried to unlock that by rewarding reviewers and allowing paid translations for only a handful of languages, but even if it simplified things a little, it didn't resolve the core problem.

The suggestion i can give is that whatever you choose to do, translators should be rewarded after their translations have been reviewed and deemed of high quality or if a translator has already done high quality translations before and they can prove it.

## v1docq47 | 2022-09-06T19:55:13+00:00
I agree that without some financial motivation it is very difficult to attract people to spend their personal time working on translations. On the other hand, I don't see anything wrong with funding translations through CCS, but I agree that the candidacy and experience of a translator should be considered separately.

As an option, assign volunteers from the community to be responsible for translating some specific languages. The responsible person does not have to make a translation, he can "management" the correctness of the translation into a particular language and point out any inaccuracies or help in translating complex and controversial formulations, or he will simply be contacted in the process of working on the translation (if there are any questions).

What I think is even more difficult is the ability to maintain the correctness of the translation with the appearance of new strings. Often, after the completion of the planned translation and receipt of payment, the translator leaves and simply not interesting the project/translation. And as a result of working on the translation of a large number of people without a single flight of thought and at a distance of several years, the translation can be greatly distorted or simply look unrelated.

Translation is a very delicate matter...

## michaelizergit | 2022-09-10T20:29:55+00:00
In my opinión, every work that’s important for monero should be funded to ensure quality. In Spanish (which one would believe is one of the biggest communities in terms of languages), sadly, you can see how many translations done by the community have been there for months, not to mention that many of them are wrong, and many of them have been upvoted when being wrong. So, for me, the problem with volunteer contributors is the time it takes for a translation to be suggested and then upvoted, plus the quality of those translations, since it’s better not to have a translation than having a bad one. With a paid, verified team of translator(s) and reviewer(s) (reviewer if needed) you can ensure consistency and quality.

Not all languages have to be opened at once but at the pace good translators/reviewers are found. Now, the process to determine who are good and who are not is not entirely clear to me unless you have a verified reviewer, which creates kind of a loop… so I think it would be expected that some languages get ready sooner than others.

The content in languages we don’t understand just doesn’t exist for us, and that’s happening to many people now. I know, for instance, that erciccione and luigi have been working hard towards a solution despite their many other occupations, but since I began translating for Monero in November 2020, the whole process has been really slow; we have still managed to deliver translations for the Spanish community thanks to them and now netrik who has also helped a lot, but it’s been almost two years. I’m just saying that we may be missing a lot of people; the cost of a translation is insignificant compared to the value added, and the community is the one paying for it.

You mentioned constant updates to the strings. I, for example, do not have any issues on creating a monthly of bimonthly (in case there are not too many updates in one month) proposal for the translation of those strings, which could be the same for every other language. With time, the fact that translations are paid and incentivized will attract more and more translators, it’s just a matter of knowing who’s good and who’s not. When the community of translators is big enough and all major content has been translated (with only often updates left), then I think we can talk about volunteer translations, but until then I think it would just stuck the translation process long enough to hurt more than would hurt the +/-$5000 per language that had to be paid to have everything translated into that language. This has even less sense when talking about languages like English, Chinese, Spanish, Russian, Hindi, and others that are really important.

I really believe that one should pay for everything that has to be done so that one can demand and be guaranteed quality.


## elibroftw | 2022-09-28T14:49:49+00:00
Literally would be better to just pay someone from fiverr / upwork for each language to do translations and pay per word like that. Then there's no need to worry about fraud while simulatenously getting the work done in a timely manner.

This is the way I'd go if I had international software and people have already donated 100k+ to the project (monero general fund). This is exactly what the general fund should be used for and hope it will be used like this.

Personally I too like volunteered donations in comparison to RFF or RFP but this system can only go so far as you push users to contribute. I push the users of my software to contribute as soon as they install the software. They get a notification on first run that translators are needed and appreciated. A complete non tech user who uses monero is not going to understand that the software needs translators because they'll just see their language and say oh it's done already. Am I incorrect in my assumption.

But the thing remains. Monero has been around since 2014 and the general fund is no empty. It is quite ridiculous that 8 years later, internationalization is still a topic of discussion and that no one has taken the initiative to just round up freelance translators and completed it. We need a PROJECT MANAGER. 

# Action History
- Created by: netrik182 | 2022-09-06T08:26:47+00:00
