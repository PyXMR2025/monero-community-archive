---
title: UI Proposal
source_url: https://github.com/monero-project/monero-gui/issues/869
author: ghost
assignees: []
labels:
- proposal
created_at: '2017-09-09T15:39:34+00:00'
updated_at: '2021-09-05T21:51:35+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Guys, been testing the GUI and started to work on some layouts to help out if welcome.


![home 2x](https://user-images.githubusercontent.com/19602081/30241545-d9e3c322-955b-11e7-8d44-d754389449fe.png)
![send 2x](https://user-images.githubusercontent.com/19602081/30241546-d9e75dca-955b-11e7-9829-11bcb6ef20ab.png)




# Discussion History
## traviss01 | 2017-09-11T14:07:55+00:00
Personally this looks much better to me, much more clean and aesthetic. 

## ghost | 2017-09-11T14:37:37+00:00
thanks for your feedback. I think simple changes would go long ways in the UX and UI. From aesthetic to things like showing the list of transactions as default. Also, filtering and sorting dont have to be primary components on the UI. Can be secondary. Icons also help, maybe even a way of collpasing the left column would make sense so its more minimal.

## ghost | 2017-09-11T14:44:07+00:00
collapsed column sample

![collapsed 2x](https://user-images.githubusercontent.com/19602081/30280984-915da946-96e7-11e7-95c4-41208d6452bd.png)



## scoobybejesus | 2017-09-11T21:40:33+00:00
Looks very nice.  Any chance you could mock it up to show two sync bars?  When used locally, there are two synchronizations that take place.  There is the sync status of the daemon downloading and building your local copy of the blockchain.  And there's the wallet syncing with the blockchain.  I think it would be helpful to see a Network Status and a Wallet Status.

Also, in the collapsed view, the unlocked balance should probably be black or bold, since it's arguable just as important as the total balance.

And the date should probably be YYYY/MM/DD, so people around the world aren't confused.

Whatever.  I'm nitpicking.  Looks clean.  Could maybe use a teeny less white space.  And the squared-off top bar screams Windows, but otherwise I like it a lot.

## ghost | 2017-09-11T21:54:13+00:00
thanks for feedback.

ill take those comments for sure. Im not from the team, but hopefully I can
contribute and gets picked.

I agree with the sync component. i want something that works collapsed and
expanded. will update.

the window chrome on top is the default I see on mac and linux, so kept
that as it was today.



On Mon, Sep 11, 2017 at 6:40 PM scoobybejesus <notifications@github.com>
wrote:

> Looks very nice. Any chance you could mock it up to show two sync bars?
> When used locally, there are two synchronizations that take place. There is
> the sync status of the daemon downloading and building your local copy of
> the blockchain. And there's the wallet syncing with the blockchain. I think
> it would be helpful to see a Network Status and a Wallet Status.
>
> Also, in the collapsed view, the unlocked balance should probably be black
> or bold, since it's arguable just as important as the total balance.
>
> And the date should probably be YYYY/MM/DD, so people around the world
> aren't confused.
>
> Whatever. I'm nitpicking. Looks clean. Could maybe use a teeny less white
> space. And the squared-off top bar screams Windows, but otherwise I like it
> a lot.
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero-core/issues/869#issuecomment-328666766>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/ASsaoRC09L7ij6wAuUKZ7xHrdjuFt_Zzks5shajTgaJpZM4PSB5r>
> .
>


## ghost | 2017-09-12T04:40:13+00:00
did some updates, still thinking about the connection states.

![collapsed copy 2x](https://user-images.githubusercontent.com/19602081/30308369-478498ec-975b-11e7-9f40-c121549c81dc.png)


## dEBRUYNE-1 | 2017-09-12T10:28:25+00:00
I like this design, as it's quite aesthetic and more elegant than the current design.. However, would you be able to code / implement this yourself?

## ghost | 2017-09-12T10:55:11+00:00
thanks, im a product designer. not a coder!


On Tue, Sep 12, 2017 at 7:28 AM dEBRUYNE-1 <notifications@github.com> wrote:

> I like this design, as it's quite aesthetic and more elegant than the
> current design.. However, would you be able to code / implement this
> yourself?
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero-core/issues/869#issuecomment-328811647>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/ASsaoY_u0MQVdVLQPYcbBbqWL8VzFWqbks5shlzLgaJpZM4PSB5r>
> .
>


## ghost | 2017-09-12T17:38:18+00:00
some updates 

**synced/connected  state**
![normal](https://user-images.githubusercontent.com/19602081/30339863-d550e8c2-97c6-11e7-9c2d-78659ebe72d5.png)

**Syncing State**
![syncing](https://user-images.githubusercontent.com/19602081/30339885-eb3a476e-97c6-11e7-8a36-5d60e3b46e8d.png)

**Daemon Loading**
![message-daemon](https://user-images.githubusercontent.com/19602081/30339895-f8957500-97c6-11e7-97c0-41a4fc89265d.png)

On this example a message appears and would fade out, messaging about the daemon

![message-daemon2](https://user-images.githubusercontent.com/19602081/30340164-f7d18892-97c7-11e7-8635-7f4a0a206586.png)


This latest notification message on top could be used as a status indicator, so a whole popup doesnt block the wallet. If thats technically possible. So would be a background thing.

We could also use the top bar as status for things like the daemon, since its something quite technical, I dont think the regular user should be exposed that much to some things. 

**Sample below**

![daemon-windowchrome](https://user-images.githubusercontent.com/19602081/30340039-8853f860-97c7-11e7-9a60-d86890447e2b.png)




## apezio | 2017-09-14T00:04:02+00:00
Looks great!  Much better than the existing GUI. 

I was going to suggest displaying the name of the currently open wallet.

How about an estimated time to sync?

## 0x63dev | 2017-09-18T01:57:55+00:00
Maybe also add estimated value of XMR in $?

## ghost | 2017-09-18T02:09:47+00:00
yes @apezio name of the wallet is handy for sure. It could even be on the window chrome on top. Ill include that in a version. I was thinking time to sync, and remaining blocks could appear as a hover information. So if you want the detail you have it, without adding stuff to the UI.

@0x63dev yes, for sure valuable info.maybe it could appear as a hover initially. Hovering over the balances, we show the USD Estimate. As an initial implementation. 

## 0x63dev | 2017-09-18T02:49:41+00:00
@alphathree Maybe show it \w same font size but green color under unlocked balance?

## QuickBASIC | 2017-10-01T04:19:39+00:00
> Maybe also add estimated value of XMR in $?

Sure, but where would we get that info? Kraken, Polo, Bitfinex, PurpleCatSlaveTradeExchange? What about people that don't transact in USD or care about the USD value? What about ten years from now when your car note is priced in BTC? 

I don't think it's wise to start adding extraneous information to the GUI. If someone cares about the value in fiat they'll know where to find that information.

Possibly, we should consider making it easier to copy the values from the balance (top left) or transactions list so that they can paste it into a calculator.

## jonathancross | 2017-10-20T02:32:35+00:00
Thanks @alphathree, looks nice!  Did you create the icons yourself or are they public domain / CC?  Can you make seperate svg files for each icon?

I noticed that your mock-up of the _History_ tab doesn't include the transaction BlockHeights.  I should point out that there is an issue with using dates -- they can be highly inaccurate and even out of order it seems. Only _BlockHeight_ is reliable for ordering.  See [#679](https://github.com/monero-project/monero-core/issues/679#issuecomment-295703832)

> Shouldn't the icon for Receiving have an arrow pointing to the coin instead of away from it

I agree with @geozdr, the current icon is unclear.  Seems to rely on "moving right" = "send" and "move left" = "receive", but that is not intuitive to me.  I'd suggest that "receive" somehow indicate an arrow "coming into" a box, wallet, coin, etc.

**RE: New features:**
The more straightforward and focused the design changes are, the more likely this is to be implemented. So please try and stay with current functionality rather than suggesting new features  :-)

> I was going to suggest displaying the name of the currently open wallet.

@apezio This feature request should be discussed here: #655

> Maybe also add estimated value of XMR in $?

@0x63dev Fiat exchange rate feature should be discussed in #621

Finally:  Any changes like this to the GUI are likely to interfere with / delay the launch of an official mobile wallet.  So we might want to consider how important / urgent this is in relation to that effort.


## ghost | 2017-10-20T03:11:15+00:00
hi. was hoping it gets picked to put more time. Some icons were done, some need to check. But didnt spend time in production level asests or versions. 

If we want to implement this design (which would be great) i would need to spend spme time doing a production level design and assets. ill do it in the next days.

ok. ill add block height. 

i can prepare some options for the icon and we review whats best. 

Yes. name of the opened wallet its useful. 

ill send uodates as I can and if its useful better :)





> On 19 Oct 2017, at 23:32, Jonathan Cross <notifications@github.com> wrote:
> 
> Thanks @alphathree, looks nice! Did you create the icons yourself or are they public domain / CC? Can you make seperate svg files for each icon?
> 
> I noticed that your mock-up of the History tab doesn't include the transaction BlockHeights. I should point out that there is an issue with using dates -- they can be highly inaccurate and even out of order it seems. Only BlockHeight is reliable for ordering. See #679
> 
> Shouldn't the icon for Receiving have an arrow pointing to the coin instead of away from it
> 
> I agree with @geozdr, the current icon is unclear. Seems to rely on "moving right" = "send" and "move left" = "receive", but that is not intuitive to me. I'd suggest that "receive" somehow indicate an arrow "coming into" a box, wallet, coin, etc.
> 
> RE: New features:
> The more straightforward and focused the design changes are, the more likely this is to be implemented. So please try and stay with current functionality rather than suggesting new features :-)
> 
> I was going to suggest displaying the name of the currently open wallet.
> 
> @apezio This feature request should be discussed here: #655
> 
> Maybe also add estimated value of XMR in $?
> 
> @0x63dev Fiat exchange rate feature should be discussed in #621
> 
> Finally: Any changes like this to the GUI are likely to interfere with / delay the launch of an official mobile wallet. So we might want to consider how important / urgent this is in relation to that effort.
> 
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub, or mute the thread.
> 


## acrelab | 2017-10-22T15:38:42+00:00
Any considerations for the use of the Monero symbol "ɱ" or `ɱ` in addition to the stock ticker symbol `XMR`? Expressing 10.75ɱ or 10.75 XMR depending on preference?

## ghost | 2017-10-23T02:12:22+00:00
@jonathancross , made some changes, let me know if I prepare the assets for Dev.

I usually use Zeplin for sending specs and assets, with an email, i can send you an invite to that repository and specs. 

I updated:

1. Added wallet name at the top of the app
2. added block height
3. updated icons

![monero-core-gui-0 2](https://user-images.githubusercontent.com/19602081/31869424-4732030a-b77e-11e7-8fe1-1a101c915e05.png)


## ghost | 2017-10-23T02:36:08+00:00
possible first run. No transaction history. it could contain some basic help for the user.

![first run 2x](https://user-images.githubusercontent.com/19602081/31869974-c437b3d8-b781-11e7-97ca-d7fc865b124c.png)

how the expansion of the icons would work.

![mining 2x](https://user-images.githubusercontent.com/19602081/31869975-c68f164e-b781-11e7-82cb-d03383bddcd3.png)

Possible hover tooltip. In this case showing the remaining blocks when syncing. Can also show the label of the icons. (Transactions, Send, Receive, Tools, Settings, etc)

![popups 2x](https://user-images.githubusercontent.com/19602081/31870197-0593faa2-b783-11e7-94db-79bd00d1fe2e.png)



## zhlyzv | 2017-10-23T11:21:35+00:00
Hey guys,

Has anyone started working on this UI?

I was thinking if we could create the GUI in Electron, we'd have much more control over the frontend, however this would result in bigger package size.. 

## basjoe | 2017-10-23T19:36:41+00:00
@alphathree Cool designs..! 

Ill be willing to pick up the code side of things - any way we can get in touch?

## ghost | 2017-10-23T19:57:27+00:00
sure, send me an email to 

alphathree@protonmail.com

i usually work with Zeplin, so deliver assets, specs, etc. 



> On 23 Oct 2017, at 16:36, basjoe <notifications@github.com> wrote:
> 
> @alphathree Ill be willing to pick up the code side of things - any way we can get in touch?
> 
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub, or mute the thread.
> 


## jonathancross | 2017-10-25T21:52:59+00:00
@defunkt1721 I personally haven't started on anything and I assume any major redesign should be discussed on IRC with devs like @Jaqueeee, @luigi1111 and @fluffypony 

## ghost | 2017-10-25T22:33:29+00:00
is there an easy URL to access that IRC channel? @jonathancross 
will ping them. I have specs and assets ready.

## QuickBASIC | 2017-10-25T22:55:04+00:00
@alphathree

https://mattermost.getmonero.org is relayed or you can use https://webchat.freenode.net.

## ghost | 2017-10-25T23:12:17+00:00
thank you @QuickBASIC just sent a message there, will keep on pushin :)

## ghost | 2017-10-26T15:57:38+00:00
update considering latest features. have some questions. are accounts the same as wallets? or users have wallet files and accounts ?

![accounts](https://user-images.githubusercontent.com/19602081/32063317-39e4424a-ba4d-11e7-8dff-724d7cfd2afe.png)


## SamsungGalaxyPlayer | 2017-10-26T16:13:05+00:00
@alphatree accounts are different than addresses. Each account is identified by its unique mnemonic seed. Under these accounts are addresses. One account can contain multiple sub-addresses.

Does that answer your question?

## scoobybejesus | 2017-10-26T16:17:19+00:00
@ alphathree What you are referring to as an "account" is more specifically called a "subaddress."

One wallet will contain one private spend key and one private view key.  From the private spend key, ultimately, the header address and the subaddresses are derived.

I tried to simplify the answer for you, as did @SamsungGalaxyPlayer, whose answer is also correct, though we sort of come at it differently.

## ghost | 2017-10-26T17:24:04+00:00
got it. 

thanks @SamsungGalaxyPlayer @scoobybejesus 


## basjoe | 2017-10-26T18:43:13+00:00
@alphathree email sent btw.

## ghost | 2017-11-01T15:48:41+00:00
heres a draft of the UX part of the proposal and rationale.
_
[Monero Proposal_0.1.pdf](https://github.com/monero-project/monero-core/files/1434698/Monero.Proposal_0.1.pdf)
_

## ghost | 2017-11-01T15:59:09+00:00
simplified version of transactions im exploring. the idea is to put most of the tx data after "details"

![simplified](https://user-images.githubusercontent.com/19602081/32283891-642a782e-bf04-11e7-8531-6ae945a6e8df.png)


## SamsungGalaxyPlayer | 2017-11-01T16:48:21+00:00
@alphatree thanks for your work!

I'm not sure if I agree that the proposal to fix problem 3 in the PDF is intuitive. The switch makes it appear as if a user could theoretically select multiple accounts at the same time. Perhaps highlight the selected one with an orange outline instead? Maybe a normal radio button?

## ghost | 2017-11-01T16:51:22+00:00
@SamsungGalaxyPlayer agree the switch is not perfect. maybe some kind of custom radio button could work as well. or something depicting activated/deactivated. makes sense to explore that for sure. thanks for your feedback.

## traviss01 | 2017-11-01T16:51:23+00:00
I assumed the slider would only let you enable one wallet into the active position. Perhaps something like this https://healthycities.zendesk.com/hc/en-us/article_attachments/209780927/met-green-500px.png or a similar icon to indicate a wallet is active or something.

## ghost | 2017-11-01T16:53:11+00:00
@unknownids was thinking something similar! will explore then. accounts are a powerful concept. but adds another layer of complexity. so definitely worth brainstorming the whole impact/behavior/design of them.

## tracyarciaga | 2017-11-16T11:04:45+00:00
Interested to help, how?

## ghost | 2017-11-16T12:01:43+00:00
yep

> On 16 Nov 2017, at 08:04, tracyarciaga <notifications@github.com> wrote:
> 
> Interested to help, how?
> 
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub, or mute the thread.
> 


## ghost | 2017-11-16T12:08:08+00:00
What's your name on IRC?

On 16 Nov 2017 8:04 am, "tracyarciaga" <notifications@github.com> wrote:

> Interested to help, how?
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero-core/issues/869#issuecomment-344890390>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/ASsaoco0pVI58OrWYBGVdxWwOnl_Y40fks5s3BbPgaJpZM4PSB5r>
> .
>


## m-henderson | 2017-12-19T15:48:27+00:00
looks great! how can I help? 

## ghost | 2017-12-19T15:55:49+00:00
I guess someone needs to implement it. I'm here to support as well from
strategy and design. UX and Visual.

On 19 Dec 2017 12:48 pm, "Michael" <notifications@github.com> wrote:

> looks great! how can I help?
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero-gui/issues/869#issuecomment-352798332>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/ASsaob0Z5hIsf16_ZuhAdzIqsaIVU2h3ks5tB9rOgaJpZM4PSB5r>
> .
>


## m-henderson | 2017-12-19T19:59:06+00:00
@alphathree is this just a wireframe or have you written the code to produce this UI? 

## ghost | 2017-12-19T20:01:49+00:00
i can provide wires and visual design and prototype when makes sense to develop that. not final code. 

would be great to have a dev help with this. 


> On 19 Dec 2017, at 16:59, Michael <notifications@github.com> wrote:
> 
> @alphathree is this just a wireframe or have you written the code to produce this UI?
> 
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub, or mute the thread.
> 


## fresheneesz | 2017-12-27T07:08:55+00:00
Sleek look! Some feedback: 

I think you should keep the text descriptions of each section tab. This makes it easier for new comers and old goers alike. If you're worried about space, make the text small. Small text is better than no text (or even hover text). 

I'd suggest that pressing "Details" expands the history item area with additional info instead of using a popup like it currently does. And rather than using up and down arrows for send and receive, use + and - to indicate debit from or credit to your account. 

Your send form doesn't seem to include transaction priority or the "sweep unmixable" button.

Some additional areas for hover info:
* Syncing - # blocks remaining, also once https://github.com/monero-project/monero-gui/issues/750 is done, some additional information that differentiates between necessary interaction with the remote node vs syncing the blockchain locally.
* Unlocked balance - display help info as to what that means (honestly I knew at one point, but I've forgotten what this means. I assume its waiting for confirmations?)

Details should include ring size, number of confirmations, and the receiving address if available (is it against monero policy to store the address you sent a transaction to?).

## sanderfoobar | 2018-03-30T01:36:54+00:00
+proposal

## jonathancross | 2021-05-26T10:38:07+00:00
Hi All, there has been significant changes to the GUI since this proposal was last discussed.  Many of the changes (or solutions to related issues) have been incorporated already.  I suggest we close this issue.

## fresheneesz | 2021-05-26T18:31:09+00:00
If we close this, can we enumerate the issues brought up here that have *not* been incorporated already? Perhaps it's worth making a new issue that focuses just on those.

## xanoni | 2021-09-05T21:51:34+00:00
For awareness, wanted to make sure this is linked to these PRs and issues:

- https://github.com/monero-project/monero-gui/pull/2936
- https://github.com/monero-project/monero-gui/issues/2024



# Action History
- Created by: ghost | 2017-09-09T15:39:34+00:00
