---
title: '[request-advice] Privacy sensitive project seeking advice from monero project'
source_url: https://github.com/monero-project/monero/issues/6633
author: democracy365
assignees: []
labels: []
created_at: '2020-06-07T07:13:59+00:00'
updated_at: '2020-10-15T22:42:16+00:00'
type: issue
status: closed
closed_at: '2020-10-15T22:42:16+00:00'
---

# Original Description
**Opening Apologies**

Before starting I would like to apologies for creating this issue. I know that opening an issue of this nature is probably not the best method of approaching such a topic, and the Monero community probably has more appropriate ways of making this sort of request that we were not aware of. After reviewing options we decided to start here as we were unsure of all the other identified options.

**Introductions**

I represent a volunteer organisation that is actively working on promoting and advocating for democracy and the rule of law, based in but not limited to South Africa.

Privacy and anonymity are cornerstones of our organisation where our members and volunteers identities are considered there own to protect as they see fit and we actively promote and assist with using the right technologies to protect their identities and maintaining operational security as they work.

We a relatively new organization, staring in Dec of 2019 and have not yet gone public. We are targeting the 3rd quarter of 2020 for public launch. Until then we have decided to withhold our organisation's name.

**Why Monero?**

We have worked on identifying and documenting a technology stack related to privacy that our members and organisation can adopt and leverage. In our research, we have identified the Monero community as a free software project that exemplifies everything we are looking for. The little of the monero community we have observed in talks and other places, we are very impressed. From the kind gentle way your senior members operate to your security awareness and that you think about the people that use the software and that there is possible a human life at the other end of a cryptocurrency wallet address.

So not only do we see Monero playing a key role in our organisation's ability to fund our activities, exchange currency and pay for services, but we also see a community that has a lot of experience in privacy and security that could possibly point us in the right direction and prevent us from making rookie mistakes in the early phases of our project.

**What do you want?**

We have a few basic questions and are looking to develop an operational process related to financial transactions that allow us to operate and achieve our goals and does not compromise operational security and privacy.

Some questions are very simple and could be seen as trivial and many are just looking to confirm our own understanding and ideas.

**Context**

Some of our funds will come from ourselves (internal), some will be donated and we need to be able to move funds between volunteers and pay for online services that are untraceable, does not raise any suspicion or compromise operational security. This would require funds to be transferred from a local fiat currency to a cryptocurrency, move between different cryptocurrencies depending on the requirements and possibly back to a local fiat money.

**Questions**

When looking at these questions you can assume that TOR, mostly via Whonix will be used.

1. Is there any way of tracing local cryptocurrency wallet address IP / identity based on a transaction or mining?
1. Is there any way of tracing transactions between two cryptocurrencies EG: swap XMR for BTC?
1. If the only way of paying for a service is to use Bitcoin, do you recommend using monero to purchase the bitcoin?
1. Is there any value in using multiple monero wallets for obfuscation the way some people try to obfuscate transactions on public coins like bitcoin?
1. Is there any risk of mining not using TOR?
1. Is there any risks in long-lived wallets where the same wallet is used for a long period of time?
1. Do you recommend avoiding exchanges that require _"Know Your Customers"_ (KYC) and _"Anti money-laundering legislation"_ (AML) information?
1. If a transaction did go through an exchange that required KYC information, if those funds were swapped on another platform or move between monero wallets is the exchange still a risk?
1. Is there any specific exchange that you are allowed to recommend for there privacy?
1. Do you have any advice regarding using a fiat currency to purchase a service, EG: purchasing a USD debit card using BTC?
1. Do you have any advice or recommendations for privacy-aware or TOR friendly chat/messaging services or software that can safely be made public?

**Our Idea**

The primary idea we have is to use monero as a way of starting or ending any transaction to prevent tracing even if something like bitcoin is used or personal or donated funds are used as the original source of the funds.

**Thank you**

Thank you for your time, we understand people are busy and don't always have the time to entertain such requests. We would understand if you decide to decline our request. If you do decide to answer our questions please note that most of our volunteers, myself included are only able to operate at specific times in the day and week, so turnaround times on any follow-up questions and answers maybe 24 hours or more, we will do our best to try and not let this be a factor.

Thank you for a vital software project for privacy and freedom.

# Discussion History
## UkoeHB | 2020-06-08T20:15:54+00:00
My best attempt to answer your questions (not an expert).

1.     Is there any way of tracing local cryptocurrency wallet address IP / identity based on a transaction or mining?
Yes, if your ISP sees you sending or receiving Monero data, they will know you are doing something with Monero. Transactions you submit to the network don't have your IP address attached, aside from connecting to a node for distributing those transactions. It's the same for mining. The node you connect to won't realize you originated a transaction or new block (it may have originated elsewhere). Dandelion++ is one technology that helps mitigate tracing the origin of transactions.

2.     Is there any way of tracing transactions between two cryptocurrencies EG: swap XMR for BTC?
Yes, the exchange you use can and most likely will keep records. Atomic swaps, if implemented, may address that problem.

3.     If the only way of paying for a service is to use Bitcoin, do you recommend using monero to purchase the bitcoin?
Hard to say, although it doesn't sound more potentially dangerous than buying Bitcoin for fiat and spending it directly.

4.     Is there any value in using multiple monero wallets for obfuscation the way some people try to obfuscate transactions on public coins like bitcoin?
No, since within a wallet your funds can be separated into multiple 'accounts' which are functionally equivalent to multiple wallets while being more efficient.

5.     Is there any risk of mining not using TOR?
If mining is banned in your location, or will entice scrutiny by officials, then I'd prefer TOR. Otherwise it sounds inefficient.

6.     Is there any risks in long-lived wallets where the same wallet is used for a long period of time?
Not inherently. If you own outputs that are very old then spending them may imply they are really being spent. However, if that really concerns you then you can periodically sweep all your outputs together, which basically refreshes their age.

7.     Do you recommend avoiding exchanges that require "Know Your Customers" (KYC) and "Anti money-laundering legislation" (AML) information?
It's up to you. Assume all that information will be available to government agencies.

8.     If a transaction did go through an exchange that required KYC information, if those funds were swapped on another platform or move between monero wallets is the exchange still a risk?
Hard to say, what do you mean by 'risk'?

9.     Is there any specific exchange that you are allowed to recommend for there privacy?
I am not well versed in different exchanges.

10.     Do you have any advice regarding using a fiat currency to purchase a service, EG: purchasing a USD debit card using BTC?
I imagine if you do this too much the tax authorities will be unhappy.

11.     Do you have any advice or recommendations for privacy-aware or TOR friendly chat/messaging services or software that can safely be made public?
I am not well versed in those services/software.

## democracy365 | 2020-06-09T07:25:25+00:00
@UkoeHB 
Thank you very much for taking the time to answer our questions, any help and advice is greatly appreciated. 

**Follow up**

8.  > Hard to say, what do you mean by 'risk'?

The primary risk we are concerned with is associated with the tracing of our volunteer's identity within the bounds of the law. Being an organisation founded to promote democracy and rule of law, everything we do looks to be 100% lawful but at the same time maintaining operational security with privacy and anonymity being the highest priority.

4. > No, since within a wallet your funds can be separated into multiple 'accounts' which are functionally equivalent to multiple wallets while being more efficient.

Do you know of any documentation or information related to this that we could review?

5. > If mining is banned in your location, or will entice scrutiny by officials, then I'd prefer TOR. Otherwise it sounds inefficient.

We are considering mining in our personal private capacity without using TOR and then distributing funds from mining to our member's wallets using TOR.

## UkoeHB | 2020-06-09T13:00:16+00:00
> > If a transaction did go through an exchange that required KYC information, if those funds were swapped on another platform or move between monero wallets is the exchange still a risk?
> The primary risk we are concerned with is associated with the tracing of our volunteer's identity within the bounds of the law. Being an organisation founded to promote democracy and rule of law, everything we do looks to be 100% lawful but at the same time maintaining operational security with privacy and anonymity being the highest priority.

If the funds are swapped on another platform, then someone with access to both exchanges will realize you own Monero. Once you own Monero, it's much harder to figure out what you are doing with it, or how much you still have.

> Do you know of any documentation or information related to this that we could review?

https://monerodocs.org/public-address/subaddress/

> We are considering mining in our personal private capacity without using TOR and then distributing funds from mining to our member's wallets using TOR.

That sounds reasonable.

# Action History
- Created by: democracy365 | 2020-06-07T07:13:59+00:00
- Closed at: 2020-10-15T22:42:16+00:00
