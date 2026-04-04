---
title: Add sub-navigation to the settings screen
source_url: https://github.com/monero-project/monero-gui/issues/1361
author: GBKS
assignees: []
labels:
- resolved
created_at: '2018-04-29T11:46:01+00:00'
updated_at: '2018-12-17T14:55:26+00:00'
type: issue
status: closed
closed_at: '2018-12-17T11:18:28+00:00'
---

# Original Description
![monero-wallet-settings-nav-gbks-180429](https://user-images.githubusercontent.com/695901/39406210-e01d2c0c-4b80-11e8-8cd3-02f0fdce60c4.png)

The settings screen is currently a long list of buttons and toggles that is hard to parse. I attached an idea of how we could split this screen into multiple sub-sections. This helps users ideally find the settings they are looking for more quickly (by just picking the right nav option). It also gives each section more space for explanations. For the log section, the actual log display could be within the screen (instead of being an overlay).

For mobile, four short section labels easily fit horizontally (see attached). But if there will be more, then a vertical list would work better.

This issue is just about the navigation. I tried to revise how the settings are laid out also, add some explanations, etc, but I'm sure I missed a lot of details there, so please ignore those. 

Other than that, feedback is highly appreciated and I'm happy to iterate this design as needed. Thanks.

# Discussion History
## krtschmr | 2018-04-30T14:18:39+00:00
very nice indeed. the node page is propably the most important one for beginners thus it needs more improvement. why we can't just provide a list with default trusted remote-nodes? because we trust nobody?

 a friend created his wallet today and without my help he would never been able to use a remote node. he doesn't even know what a port is.

## GBKS | 2018-04-30T14:25:18+00:00
@krtschmr that's a valid topic, how about we split that into a separate issue? I'd love to keep the topic here on just the navigation UI and the basic split-up of the options.

## sanderfoobar | 2018-04-30T15:34:42+00:00
> why we can't just provide a list with default trusted remote-nodes? because we trust nobody?

Trusted by whom is the question. Monero is about trusting no one but the code. We can't have a predefined list of nodes in the official wallet as it goes against decentralization.

> a friend created his wallet today and without my help he would never been able to use a remote node. he doesn't even know what a port is.

Users want a more trivial experience while Monero developers/contributors want to maintain operational security. 

We must meet somewhere in the middle where we encourage users to run a full-node yet make it more apparent that using a remote node is an option. 

Pre-defined remote node lists / remote node only / light wallets would have to be third-party.


## pazos | 2018-04-30T20:36:44+00:00
@krtschmr: please give your friends a link to [GUI guide](https://github.com/erciccione/monero-GUI-guide/blob/master/monero-GUI-guide.md#212-daemon-settings). Is better to educate people than to be always fixing their stuff. :dancer: 



## krtschmr | 2018-05-01T04:18:42+00:00
@pazos even i agree with you, but that's the time when people then say *fuck it, i'll pay with bitcoin*. 

## krtschmr | 2018-05-01T04:19:22+00:00
@skftn  

> Trusted by whom is the question. Monero is about trusting no one but the code. We can't have a predefined list of nodes in the official wallet as it goes against decentralization.

we could setup community nodes with decentralized DNS?

## rbrunner7 | 2018-05-24T08:59:51+00:00
Definitely an improvement, IMO. I think mostly people new to Monero are drawn to the GUI wallet, and for such people the additional explanations that this layout allows are very valuable.

## lopanism | 2018-05-24T09:21:27+00:00
Another piece of feedback on the wallet UI: try to simplify main menu as well. 
Note that some elements are nouns, and some verbs, this can be improved, as verbs are really actions (i.e. Send, Receive), while nouns are ‘destinations’ (i.e. Address book, settings, transactions.) 

The best place to start would be to try to separate nouns from verbs and see where it gets you. Having
Send/Receive as persistent buttons on the screen might be an interesting idea. 

Then you can categorize nouns:
Settings and Advanced are far less important ad Transactions (at a first glance), address book might not even deserve its own entity, and live contextually in Teansactions and Send/Receive flows. 

If you think along these lines, you can get to a drastically simplified navigation, and overall app structure. Which is easier to use, build and maintain. 

I can provide examples if it interests you.

## sanderfoobar | 2018-07-08T23:20:39+00:00
I started working on this. Some WIP:

![](https://i.imgur.com/sKsFRum.png)

![](https://i.imgur.com/9BWkALp.png)

## sanderfoobar | 2018-07-08T23:25:13+00:00
@GBKS Could you perhaps provide the icons on `zpl.io` for those red squares?

Thanks :)

## GBKS | 2018-07-09T12:34:59+00:00
@skftn check out the "Icons" screen in Zeplin (zpl.io/a8E3WJx), should already be there. But let me know if it's not, or if you need a different size, etc.

## mmbyday | 2018-12-17T08:37:33+00:00
+resolved
by 1511

## erciccione | 2018-12-17T11:12:01+00:00
+resolved

## krtschmr | 2018-12-17T14:55:26+00:00
#1511 

# Action History
- Created by: GBKS | 2018-04-29T11:46:01+00:00
- Closed at: 2018-12-17T11:18:28+00:00
