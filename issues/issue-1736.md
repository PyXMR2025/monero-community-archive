---
title: Let's consider removing the merchants page
source_url: https://github.com/monero-project/monero-site/issues/1736
author: erciccione
assignees: []
labels:
- 💬 discussion
created_at: '2021-07-16T08:12:19+00:00'
updated_at: '2021-09-10T13:44:48+00:00'
type: issue
status: closed
closed_at: '2021-09-09T20:11:04+00:00'
---

# Original Description
Adding, removing merchants and in general dealing with requests from merchants is becoming very time consuming and recently started to take a considerable portion of my CCS-funded working hours, at the point that i'm asking myself if it really worth it or that time could better be spent doing something else.

Should we consider removing the merchants page and instead link to external merchant directories? Is the amount of resources needed to keep this page updated worth it?

# Discussion History
## AiloQito | 2021-07-16T09:41:01+00:00
I do not know how with other services but it is with exchangers page is very useful for users.
As a Monero crypto-enthusiast I very often picked up exchangers from this page.
The problem is that there are only crypto-exchanges in external catogories, and for Monero users who need to exchange, exchanges are not suitable, because there AML/KYC and all the anonymity of Monero is lost completely.
And you site can pick up exchangers that do not require AML / KYC and for users of monero this is ideal.

## AiloQito | 2021-07-16T09:42:05+00:00
As a Monero crypto-enthusiast I can help you and do analysis on exchangers, as it would be nice to feel a little bit in the Monero team.

## AiloQito | 2021-07-16T09:44:46+00:00
I would also suggest that you separate the Exchanges section
Into two sections
Cryptocurrency exchanges [KYC/AML]
Instant Exchange

## AiloQito | 2021-07-16T10:05:56+00:00
<img width="1157" alt="image" src="https://user-images.githubusercontent.com/87210500/125931346-9e5d6670-eaa2-45c9-adf4-fc0cc1b8a46a.png">
<img width="1153" alt="image" src="https://user-images.githubusercontent.com/87210500/125931360-81f0cae4-9d90-46a5-a154-21e132c0b671.png">


## AiloQito | 2021-07-16T10:07:26+00:00
Here's how to make partitions, There are only those that will remain, after all the deletions 

## AiloQito | 2021-07-16T10:08:24+00:00
It will be much more convenient for Monero users because it will not be necessary to scroll through the entire list if a user needs, for example, an instant exchanger without registration 

## AiloQito | 2021-07-16T10:08:52+00:00
Well, or the same if the user needs a crypto-exchange with monero.

## AiloQito | 2021-07-16T10:10:02+00:00
Well, as for me the presentation of information to the user will look gaurely more beautiful and understandable ato so many extra words near each exchanger should be only the name and I think this is enough.

## AiloQito | 2021-07-16T10:11:28+00:00
Well here is how you decide well this merchant page is very important for users why use any external katolog on other sites if he can get all the information he needs on the site Monero.

## AiloQito | 2021-07-16T10:17:20+00:00
I could also help you for free to analyze the claims of exchangers and add new exchangers and give you a ready result on the basis of which you will make decisions.
I just really like Monero because it is currently the only cryptocurrency that is anonymous.

## erciccione | 2021-07-16T10:36:07+00:00
@AiloQito please stop splitting your messages into several small posts. You made 10 in a short time and that's not acceptable. This is not a chat and it comes out very spammy and annoying. Make one single post if you want to say something.

## erciccione | 2021-07-16T11:00:39+00:00
> I would also suggest that you separate the Exchanges section

Please keep the discussion on topic. This issue is for discussing only if we want to remove the page or not.

> As a Monero crypto-enthusiast I can help you and do analysis on exchangers, as it would be nice to feel a little bit in the Monero team.

Thanks for volunteering, that's appreciated, but inspecting merchants is a task that requires a degree of trust in the person inspecting and you are a new account with no record of contributions in the Monero community, so i don't think that would be possible. Of course anyone is welcome to make and share their own analysis.

## erciccione | 2021-07-17T06:55:04+00:00
From #monero-site:

```
14:09:58 <fluffypony> ErCiccione: what if we redirect everyone to https://cryptwerk.com/pay-with/xmr/ ?
14:10:14 <fluffypony> we can even have a link on the Merchants page to that site (and I'm sure there are a few others)
14:28:25 <ErCiccione> yeah that's what i had in mind as well. I know the cryptwerk folks are quite active, don't know if there is anything else like that. We could also leave a small sectionof the merchants page with only decentralized exchanges to encourage people to use those
14:30:34 <fluffypony> good idea
14:31:05 <fluffypony> https://www.acceptedhere.io/catalog/currency/xmr/
14:31:22 <fluffypony> I think if we link to both of those that will be good
14:43:48 <ErCiccione> I missed that one. Yeah sounds good
17:06:11 <binaryFate> agree, it's a waste if it takes up significant time from your website time, and it would only get worse
```

## johnr365 | 2021-07-19T16:36:32+00:00
+1 to this proposal, and to the above point about referencing cryptwerk + acceptedhere

It makes more sense to re-allocate time to other more important tasks.

## erciccione | 2021-07-21T11:06:52+00:00
Writing it down so i don't forget it: The 'payment gateways' list is useful, we should keep it, but move it somewhere else (maybe in the new 'Tools' page?)

## erciccione | 2021-07-23T09:35:57+00:00
Changes proposed in #1743

## AiloQito | 2021-07-23T12:29:31+00:00
I would advise to specify a link to the cryptocurrency Monero in the cotalog.
https://cryptwerk.com/pay-with/xmr/

## QuickBASIC | 2021-08-17T03:30:32+00:00
Hi, I haven't contributed in a while, but I wanted to share my opinion. I think that it's probably a good move to remove merchants from the official page.

While I agree that it's relatively unmaintainable because it takes some time, I also always disliked that we didn't actually have a good way to vet most of them. Despite the disclaimer, I think there's some responsibility that we have when we direct people to other sites to know that those are legitimate sites or businesses that aren't going to rip them off and there's simply not the manpower vet every one.

I think having links to Exchanges may still be acceptable as many are either regulated or frequently used enough by members of the community that we aren't probably going to list any that are problematic and Monero doesn't have any exposure on many mainstream apps or Exchanges (Coinbase or Robinhood or whatever), so it might be good to let non-crypto savvy folks that are visiting know where to buy aome.

## erciccione | 2021-08-17T07:53:29+00:00
Happy to see you around again @QuickBASIC :)

As i mentioned, i agree with listing CEXes as well, but we need to make a list of trusted/reliable ones. Any ideas?

## Silokonger | 2021-08-19T09:12:12+00:00
I think it's very stupid to remove all the exchangers from the page

And I also paid attention to a very interesting fact to pay attention to all the exchangers that you have removed the same type of complaints I paid and they say that the purse does not belong to them, and the funny thing is that it was all exchangers that were removed for these reasons work and at the moment and no one else no complaints about them did not come anywhere else but on your site.

Don't you think you've just been misled into removing unnecessary exchangers?

And what is more, I use exchangers from your list more than 1 year and not when none of the exchangers did not fail me and I also use those that you have removed and even sometimes even now for small amounts they use and they work fine.

You have not had a complaint at any exchanger for many years? And in one moment went the same type of complaints on all exchangers think about it you are looking for the problem is not where it is.

## Silokonger | 2021-08-19T09:21:57+00:00
As I think it is extremely stupid to remove direct exchangers from the list, and just as stupid to make a list with some exchangers that work for years and type of reliable, as new exchangers which can be 1-2 months can provide better exchange conditions and quality of service than those who work for years.

And what you want to do may severely affect the anonymity of Monera if you leave only a list of exchangers that require a customer AML / KYC, what kind of anonymity Monera will then be if what would it need to exchange AML / KYC.

As we know a lot of people don't like Monera because of its anonymity, and many would like to discredit it. And if you take away the ability to exchange Monera without AML/KYC then the usefulness of Monera anonymity will be zero, because in order to exchange it for something will always need to pass AML/KYC 

You came up with the nonsense and now you do not know how to solve it you realized that there is no kotalogov not anything where would be provided a list of Monero exchangers and now you want to come up with a wheel when you have already come up with it on the site there is a list and nothing new to do is not necessary.

As you write that this page takes you a lot of time, so it is one of the most important pages of the site Monera)))

Well, it's up to you how and what to do well as a user of your idea I see only negative sides not a positive you want to leave the site only exchangers that require AML / KYC and why they need users to exchange Monera? those who chose Monera they want anonymity and they do not agree with the rules AML / KYC

## erciccione | 2021-08-20T09:53:27+00:00
I want to add a list of centralized exchanges, but we have to find a solution that won't bring us back to the original problem. Please see https://github.com/monero-project/monero-site/pull/1743#issuecomment-902576657

## xmrstickers | 2021-08-25T22:37:52+00:00
If this list is removed, is there any alternative way for XMR businesses to get the word out for free (without spamming /r/monero or similar, which is in bad taste anyways...) 

## erciccione | 2021-08-26T08:53:11+00:00
@xmrstickers we'll add two merchant directories: cryptwerk.com and acceptedhere.io


## test24853 | 2021-09-01T13:15:54+00:00
![image](https://user-images.githubusercontent.com/36427497/131671820-dfa431d7-280c-460a-92bb-2df8fabd9653.png)

Dear community and community managers,

I do not write a lot, mainly read the subreddit, neither do I hold a significant amount of coins (any), but I use Monero for as many transactions as possible. I try to pay my domains with Monero, gigs that I outsource, etc. The merchant page in its current state might be "obsolete" or may be replaceable by a third party, yes. But I do think that a "merchant" page - I do not like that name because it might be misleading - an adoption page with even reviews might be helpful. Especially if those directories' intention is to make money off the traffic (ref links, affiliate links, redirect cookie links) and not really care much about the adoption of Monero. If sellers mainly want to attract new customers that pay with Bitcoin, they will just up the discounts, and customers will ask themself: "Why would I pay 20% more just to pay with Monero, the discount on purchase with Bitcoins is much better". 

Putting such an important task - education about adoption and acquiring new merchants - into a thirds party hand, that makes all its decisions based on which coin makes them more ad/affiliate revenue, seems to be a not wise move. It seems like a lot of (good) effort is being done on content within the Monero community, which I personally like as someone being part of that community, but growth (actually doing payments and not just investing) wise, Monero depends on the vendors and merchants. Instead of getting rid of a directory that is mainly a struggle to maintain - which I completely agree with (in its current form), I would double down and maybe get a new directory done. I am quite confident the community is willing to do some donations for such a task. Setting up a WP Page with a merchant directory plugin (200$) or even outsource a handmade portal (6000$, which I do not advise) and picking admins from the community will be much more healthy in the long run.

Imagine you are a merchant/vendor. Why would you spend time and effort to get vetted into a directory? To get access to new customers that want to support their ideas (Monero) and are willing to even pay a premium for it. So if a new company wants to get entered in the directory, they need to accept Monero to get access to that community. On the other hand, companies that do want to get access to those 3rd party sites, only need to accept Bitcoin. The leverage is the community. Access to more customers. Access to more exposure. Talking to merchants that do not offer Monero yet, showing them that they miss out on a niche customer base that is loyal, should be a high priority. Even higher than all the within-the-community content. People will arrive at Monero when they get a benefit if they pay with it. Those benefits - in this marketing environment - reflect either by exclusivity or by discounts. There are multiple user demographics that do not use Monero yet. Some of them don't know it, some do not believe in it and some would love to pay with Monero, but whatever they want to buy does not support Monero as a payment method. At the end of the day, the question should be, to which customer demographic is this effort designed for. I am not involved enough in Monero (community-wise) to say: "Do this and that, it will work". But I highly recommend, as a daily-use Monero person, to take a step back and ask: Is it a good idea to give adoption into the hands of a third party? I understand that the current directory is almost useless, but that is not the state it needs to stay in. It can be a strong and important tool if the community and the leaders work together to push forward daily-use adoption. Please, only get rid of it once there is a solid and meaningful replacement, in my personal opinion.

Edit: There are also quite a few big merchants - that play a big role in the privacy world - missing in that list. Maybe its worth adding them even if they do not step forward themself. 

## erciccione | 2021-09-02T07:04:49+00:00
@test24853 thanks for your feedback. I saw your message on reddit as well, but i will be answering only here :)

>  I would double down and maybe get a new directory done. I am quite confident the community is willing to do some donations for such a task

Sure, this is the best option there is, the problem is that you need somebody willing to create and maintain such directory and there are no volunteers for such job at the moment. Additionally, the maintainer must have a degree of trust in the community, so that people know that the list they are seeing is legit and not influenced by external factors (like money). Personally i agree a merchants list is useful, but this repository is not the a good place where to maintain such list.

## HardenedSteel | 2021-09-10T09:49:40+00:00
What will happen current merchants page? Should we inform users merchants page will be removed?

## erciccione | 2021-09-10T13:44:48+00:00
Yes, we will probably publish some social media posts about it

# Action History
- Created by: erciccione | 2021-07-16T08:12:19+00:00
- Closed at: 2021-09-09T20:11:04+00:00
