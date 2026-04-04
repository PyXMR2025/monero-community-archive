---
title: Improve balance readability / balance card overhaul
source_url: https://github.com/monero-project/monero-gui/issues/2298
author: ghost
assignees: []
labels: []
created_at: '2019-07-18T15:56:23+00:00'
updated_at: '2023-10-04T00:35:26+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
[Updated! #2322, #2293 closed and integrated here. Ignore changes from #2325, #2339, #2304.]

![image](https://user-images.githubusercontent.com/46682965/64294009-21af4e80-cf6e-11e9-8993-0040beb4b724.png)

- The user only is bothered with locked funds **when** he's on the `Send` page **and** funds are locked.
- **[>90% of voters](https://www.reddit.com/r/Monero/comments/cynicf/poll_how_would_you_prefer_your_fiat_balance_to_be/)** want the fiat balance to be displayed _additionally_ to the XMR balance (instead of toggling). I've explored [several design variants](https://github.com/monero-project/monero-gui/issues/2298#issuecomment-527047912). This one is the best IMO:
![image](https://user-images.githubusercontent.com/46682965/64131970-816df400-cdcc-11e9-8344-c4e1d91c3673.png)
- Text to be shown when the user clicks on `(Why?)`:

`For safety reasons, in Monero there's a waiting time of 10 blocks (~20 minutes) until newly received funds can be spent. But not only receiving funds, also sending funds can cause such a waiting time. The reason for this is that when you send for example 1 XMR, technically 5 XMR may be send and you get 4 XMR back as change - a process that you may not notice at all, but technically the 4 XMR count as newly received funds and cause the same waiting time as regularly received funds.`

# Discussion History
## GBKS | 2019-07-19T08:07:39+00:00
I really like how you're simplifying things. What do you think of using Roboto Mono for the numbers and replacing the word "Monero" with the account name (something I also suggested [here](https://www.reddit.com/r/Monero/comments/c23zxn/feedback_request_ideas_for_improving_how_multiple/))? Something looks a little off still about "XMR" being bigger next to the smaller numbers...

![monero-balance-card-readability-190719-gbks](https://user-images.githubusercontent.com/695901/61519666-bab0f700-aa0c-11e9-8f75-b3c36c5eb277.png)




## ghost | 2019-07-19T09:15:17+00:00
@GBKS You are so right! My "XMR" was too big, and we should simplify even more! Thanks for your great input!

Plz check out my proposal 3 (yours is 2, my first one is 1):
![monero 5](https://user-images.githubusercontent.com/46682965/61524248-627ef280-aa16-11e9-8164-349773133555.jpg)

Please everybody tell your thoughts! I will then make a final proposal.

By the way: Who here is using multiple accounts? Because if 99% are using just one account, we maybe should put the balance in the first line, and the account in the second line (smaller or in brackets).



## GBKS | 2019-07-19T09:36:25+00:00
My concern would be that longer account names don't fit in. Somebody at Google told me a while back that German is 60% longer than English on average, so they always assume that that much more text has to fit. Here's an example of putting the account number and name in separate lines, with some rulers for the layout to keep things visually structured.

![monero-balance-card-readability-2-190719-gbks](https://user-images.githubusercontent.com/695901/61525473-c86c7980-aa18-11e9-8c1c-f810c4b83dfe.png)

How many accounts people use has been a [big discussion](https://www.reddit.com/r/Monero/comments/c23zxn/feedback_request_ideas_for_improving_how_multiple/). We don't have reliable data on account usage as far as I know. I heard statements that we should support 50+ accounts, others think people should use just 1, or maybe 2-3 accounts. Generally speaking, it is a core feature that people also know from their traditional banking experience. Kinda makes sense to split your funds up for a few different use cases (which will differ if you're an individual, business with employees, exchange, vendor...).


## ghost | 2019-07-19T10:09:27+00:00
Great Input again! Great red lines! Great idea to drop the colon! Thank you so much!

Proposal 5:
![image](https://user-images.githubusercontent.com/46682965/61527654-3f0b7600-aa1d-11e9-83c3-2bc4bb3ccac7.png)
- Can u live with the reduced height? (Of course the background would have to be fixed)
- Can u live with my use of the text color gray?
- Can u live with cutting long account names with "..."? (That's how it is done right now anyway, because account names can be VERY long.)

Only problem that's open for me: We have dropped the little door symbol, which closes the wallet!^^ That looks good for sure, but I guess that's not ok to just drop it^^

## parasew | 2019-07-19T10:49:54+00:00
These changes are very good, i just have a few things to mention: there is a lot of text-redundancy in the interface which take up a lot of space in the UI. 

- "XMR" (as long as the wallet only supports XMR it is not necessary to mention this everywhere, people are aware imho that the numbers are the XMR in question). This also goes for the logo in my opinion.
-  "Account #1" could be possibly reduced to just "#1", as there is "account #1" and "primary account" spelled out. 


## ghost | 2019-07-19T11:10:49+00:00
> * "XMR" (as long as the wallet only supports XMR it is not necessary to mention this everywhere, people are aware imho that the numbers are the XMR in question). This also goes for the logo in my opinion.

Sorry, no! Sure, 99% of the users are aware - but it's about catching mistakes! It's about the 1% who are doing a transaction late at night, have multiple windows open and so forth. Example: You see your balance "20.00" without unit. It's late at night and you want to pay somebody "19.95 USD". Oh boy! There the drama starts! That's why we ABSOLUTELY need units! And in the future, when XMR is rising, the unit mXMR will become more and more common. We ABSOLUTELY need units!

> * "Account #1" could be possibly reduced to just "#1", as there is "account #1" and "primary account" spelled out.

Sorry, no!
- "primary account" is just the default label - anybody can change it!
- Account numbering starts with 0, that makes it easy to confuse "0" and "1" and what is "primary". (Funny: You just made that mistake yourself. Primary account is 0, not 1.)
- Since we dropped the word "Balance", the word "Account" now kinda serves as the headline of the balance field. 



## ghost | 2019-07-19T11:42:32+00:00
> The title bar's logo and balance panel's logo has a different color It seems a bit strange ?

- I have no idea why the logo in my title bar is grayish! (Others have it colored.)
- IMO the white-only logo in the balance panel looks great! It harmonizes well with the white text. However, I'm totally open for redesign proposals!

## GBKS | 2019-07-19T14:10:29+00:00
![monero-balance-cards-gbks-190719](https://user-images.githubusercontent.com/695901/61541191-7c80fb00-aa3f-11e9-9cd2-6b1e5752d324.png)

Here are my 2 cents on the logo. We should keep the original orange/grey one in the title bar, so it matches the other treatments. For the white theme, we should also use it (obviously no white on white), but it is nice to go for white in the black theme. 

## ghost | 2019-07-19T15:35:18+00:00
@GBKS 
Your design SLIGHTLY changed:
![image](https://user-images.githubusercontent.com/46682965/61547358-827cd900-aa4b-11e9-8277-1b543039b5ee.png)

How it would look in the GUI:
![image](https://user-images.githubusercontent.com/46682965/61548636-6cbce300-aa4e-11e9-8c6e-fa95754a3a64.png)

@GBKS I think your aspect ratio is better, but I'm begging you to change the font size(s) of the balance a little bit in my direction!


## selsta | 2019-07-19T15:56:56+00:00
@GBKS Can you upload your design to Zeplin?

## SamsungGalaxyPlayer | 2019-07-19T18:24:25+00:00
Personal take: Roboto Mono font is better, decimal values can be a little larger (0.1 XMR is still worth seeing at ~$10).

## GBKS | 2019-07-20T13:49:53+00:00
![monero-balance-cards-gbks-190721](https://user-images.githubusercontent.com/695901/61579417-03e47200-ab05-11e9-81d1-ca94650f0b60.png)

Here's another update, which I also put on Zeplin (screen is called 'balance cards' in the 'UI elements' section. The top cards are 16:9 ratio, the bottom cards 20px shorter. I like the top ones better personally with the little bit of extra breathing room. For the card on the right, I put in a larger amount and 12 decimals, which just barely fits into the card. Unless we start trimming decimals, we don't have room to make the text size larger. I'd be happy to adjust text size if this space issue is not a problem.

And just for fun, here's one using the Fibonacci spiral (but please let's not use that one).
![monero-balance-cards-fib-gbks-190721](https://user-images.githubusercontent.com/695901/61579477-c9c7a000-ab05-11e9-8b6f-e26c26fd7dd8.png)



## ghost | 2019-07-20T15:16:04+00:00
1. Great job!
2. **Under NO CIRCUMSTANCES we can use the comma as separator for the thousands. That's forbidden by both DIN and ISO for the confusion that it causes internationally, instead they encourage the use of a half blank. A half blank looks INCREDIBLY beautiful and does the readability job perfectly well! However, I wonder if we need such a separator at all, since those guys who have over 1000 XMR are REALLY rare, and since we already have the trick with the 2 different font sizes, which helps a lot! Furthermore, one only really needs that separator for numbers like 1,250,000 - not for numbers like 1250.**
3. Agreed: Your 16:9 ratio looks best!!! (Took me some time to see it! I could live with both.)
4. I understand the problem with the font size and too long numbers that you are reporting. We COULD solve that problem like this:
![image](https://user-images.githubusercontent.com/46682965/61581245-436a8880-ab1c-11e9-9005-2d3d71741bed.png)

The "XMR" at the end helps with our size problem, since the main number now must not start where the label above starts.
5. Your main number never was bold, right?? I guess that's what I was missing all the time! Go for bold please, which will allow you to go smaller with the font size (and bigger with decimal digits)!
6. I'm all for your Fibonacci spiral^^ It will make other coiners think: "Looks like these Monero guys are on to something, we gotta find out before they moon without us!"


## SamsungGalaxyPlayer | 2019-07-20T17:37:35+00:00
I like having the XMR in front of the value for consistency.

## ghost | 2019-07-20T17:51:57+00:00
> I like having the XMR in front of the value for consistency.

Me too.
![image](https://user-images.githubusercontent.com/46682965/61582190-ba594e80-ab27-11e9-974e-f69542f6893e.png)
![image](https://user-images.githubusercontent.com/46682965/61582385-7b78c800-ab2a-11e9-9634-88b57826b420.png)

Let's wait for @GBKS. Could you live with one of the two?

## GBKS | 2019-07-22T07:42:12+00:00
This looks great, nice job. If you wanted to be super picky, you could move "Account #0" and "Retirement savings" 1px down, so it's better centered vertically with the logo. Thanks for the input on DIN and ISO standards. Are there any graphics you need on Zeplin that are not up there yet to build this?

One thing to note is that I put a pretty big, diffused-looking drop shadow with negative spread on the cards. This makes it feel a bit more realistic than a smaller drop shadow without spread, since it's a bit more how real light and shadows work. But it's also harder to implement, since the card image is way bigger than just the card itself. Unless of course, QT has a built-in filter for nice drop-shadows. This doesn't matter so much on the dark theme, since there is enough contrast to the black background. But it might become an issue with the white theme, where the card might blend too much with the background if the drop shadow is executed differently. Let me know if this ends up being an issue.

## ghost | 2019-07-22T07:49:33+00:00
@GBKS 
- Thanks
- You're right it should be 1px down! (MUST be!)
- I'd love the drop shadow effect you're talking about!
- I can't build it :(  (I'm working with paint.exe) PLEASE, can you do it?
- So happy that you "insisted" so long in 16:9! It reminds of a credit card!


## GBKS | 2019-07-22T08:05:31+00:00
I also can't build it, that's what we have our experts like _dsc, selsta, and others for. Always a team effort 😉 

If you are interested in trying a more professional UI design tool, [Figma](https://www.figma.com) is a great entry point. It works in the browser, has free accounts, and absolutely matches the other tools out there commonly used for UI design these days (like Sketch and Adobe XD). My design files (Sketch) are [here](https://github.com/GBKS/monero-wallet-design), and can be easily imported to Figma.

## ghost | 2019-07-22T08:44:30+00:00
I didn't only mean I can't build it, I also meant I don't know how to deliver what is needed to build it.
I'm just trying out Figma, it looks great and powerful! Thanks. Don't know when delivery, though. (Gotta learn about Github, qt, Zeplin first.)

Which of the last 2 proposals looks best?

## selsta | 2019-09-01T00:49:09+00:00
@GBKS The dark version of the new card isn’t downloadable, I can only download the light one. Am I doing something wrong? :) Also it says 260x115 but the card size is 381px × 246px, is this also intended?

## realindiahotel | 2019-09-01T10:48:20+00:00
I think it is normal form to put the currency tag after the balance is it not?

So xxxx.xxxxxxxxxxxx XMR not XMR xxxx.xxxxxxxxxxxx

From Bitcoin Core Example 
![image](https://user-images.githubusercontent.com/2297007/64075293-d260e800-ccf9-11e9-9147-5ea640d6e11e.png)

And indeed TX in Monero listing same with XMR after amount spent/received. Should it not be same in Balance Card for consistency sake?

## ghost | 2019-09-01T10:59:19+00:00
There's no right and wrong here.
![image](https://user-images.githubusercontent.com/46682965/64075411-3d89ca80-ccb8-11e9-9b5e-c4ba7f20d9f5.png)
But you're right, it is more common at the end (on global average). However, in our case with many, size-reduced decimal numbers it's less intuitive at the end IMO:
![image](https://user-images.githubusercontent.com/46682965/64075405-2f3bae80-ccb8-11e9-95e1-612c9b1a8db9.png)
Others here said the same.

> And indeed TX in Monero listing same with XMR after amount spent/received. Should it not be same in Balance Card for consistency sake?

Valid point, but lists should be like this anyway:
![image](https://user-images.githubusercontent.com/46682965/64075800-1aade500-ccbd-11e9-9ee1-877bc9f3b35b.png)
That said, I certainly don't hardcore-insist on my position. If people want it at the end, I'm totally fine with it!


## kayront | 2019-09-02T06:51:28+00:00
To continue the discussion from #2368 (here, as requested), the points I raised were the following:

```


    The "main" balance display (the bigger letters, presumably above the "secondary", "XMR" in the case above) can be XMR, but it could also be swapped for a configured fiat currency -- or in other words, if the user so chooses, the fiat currency display could become the "main" one displayed on the wallet.

    Under the "main" balance display, and rather than using the little toggle menu shown in the image above, the "secondary" currency is shown, in smaller letters. The advantage of this method is that the user no longer needs t constantly hit a toggle or a button to compare XMR value with desired currency.

    In order to enable the functionality described in the two points above, there has to be a way to select which fiat currency the user is interested in displaying. Since the idea is eliminating toggle menus and extra buttons, the first thing that comes to mind is relegating that preference to the settings window, but then it can get cumbersome to swap currencies (out of curiosity, for practical purposes that don't come to mind right away, etc). So how about this: Create a new section in settings where the user can choose which altcurrencies will be available, and then when the user clicks the "XMR" (image above), the "main" currency gets swapped for altcurrency1, one more click and altcurrency2, one more and back to XMR: meanwhile XMR, for as long as the "main" currency is an altcurrency, gets displayed below as "secondary", with smaller letters. Once back to/when XMR is set as "main" currency, the "secondary" becomes clickable, and the GUI will cycle between the chosen (from settings) altcurrencies.

    Another suggestion is to not just stop at fiat currency! Allow the user to choose Gold, Silver, and even Bitcoin as altcurrencies.
```

@Realchacal wrote in reply:

```
image
is not necessary so I deleted it in #2298. It also explains: "You would toggle the currency (XMR <--> fiat) by clicking on the currency. The currency would be highlighted while the mouse is hovering over it." IMO this is so simple and beautiful while a second balance would add so much (visual) complexity!
```

**I disagree, and here is why**.

Nobody in their right mind makes a XMR (or BTC for that matter) tx without looking at the corresponding fiat value, because of volatily.

Because of that, it seems more sensible to me to **have the fiat value displayed at the same time as the XMR in the account**, rather than having to click the currency to switch between one and the other.

Think about it - the user *is* going to do that to confirm exchange rates anyway, why force an extra click when all the information (and it isn't that much) could be clearly presented instead?


## ghost | 2019-09-02T08:09:42+00:00
- We should implement what people want.
- IMO the 2-balance solution will look less beautiful:
![image](https://user-images.githubusercontent.com/46682965/64099985-eabd1b00-cd6a-11e9-9946-617a0542555d.png) ![image](https://user-images.githubusercontent.com/46682965/64106035-a6844780-cd77-11e9-8c4a-57badb724946.png) 



## kayront | 2019-09-02T09:34:10+00:00
My thoughts are as follows.

The first image has both XMR and fiat with the same text size, giving more highlighting/relevance to neither, which in my opinion is not pretty.

The middle one appears to me as the most aesthetically pleasing (I am aware of previous debate concerning XMR $amount vs $amount XMR), **but** I would try a couple of things to make it even better:

  - Make the "secondary" (lower one, USD, in the screenshot) even smaller.

  - Get rid of the parenthesis.

  - Probably get rid of USD and use the dollar sign instead, but it is not clear how to make this consistent across fiat curriencies that share the dollar sign (this is the smallest problem imo), gold, BTC, or indeed even XMR if it's been set to "secondary" and thus appears below.

I would also *probably* (hard to tell without seeing a screenshot) move the secondary/lower/smaller-letters currency to the right.

**edit**: I think the same observations about aligning (just not as much to the right) and no parenthesis would apply to the "$amount XMR" solution, the third image above, just the same.

The toggle sure is simpler, although I disagree that it is more beautiful (this is a highly personal opinion of course and different people will say different things).

But this much to me appears certain: the point still stands that it's simpler cognitively and from a user interaction perspective to have *both* fiat and XMR values displayed at the same time, with one given more relevance/highlighting by means of font size.

## kayront | 2019-09-02T09:40:13+00:00
By the way, and I don't mean to derail this issue, but is there any ongoing discussion about making similar changes related to fiat amounts in:

  * Send (as the user types XMR amount, fiat amount is displayed in real time)
  * Receive (shows fiat balance in historically-accurate rates, privacy must be taken into account)
  * Tx history (combination of both above)

If not, should I start a new issue to discuss?

## ghost | 2019-09-02T10:00:52+00:00
> I would try a couple of things to make it even better

See my previous comment (2 variants added as proposed by you)

> is there any ongoing discussion about adding fiat to all the other pages, if not, should I start a new issue to discuss?

I'm not aware of such discussion. This feature would be nice, but the problem with it is: Adding fiat values **optionally** everywhere is a pain because you can't really optimize your design for one or the other. IMO, it depends on what users want. If they all want fiat everywhere, we should go fiat everywhere.

## kayront | 2019-09-02T13:57:07+00:00
![img](https://user-images.githubusercontent.com/46682965/64106035-a6844780-cd77-11e9-8c4a-57badb724946.png)

The one on the right is the clear winner, imo.

I see you shared on reddit with $ instead of USD, that one looks even better.


Some people have expressed concern that it not clear how to swap between fiat currencies (in my proposal above, just click anywhere in the fiat amount), and I can sympathize with this from some Android apps where only after months of using them did I realize it was possible to tap on something to change its name.. but a simple dialog that pops up the first time and can be dismissed or a small paragraph describing how to toggle between chosen alternative currencies in the settings where alternative currencies are enabled should be enough to guide the user the right way.

One or two people also suggested that the USD (or whatever currency) should be on top, but that is a very personal decision; I can understand it though, and that is why in my previous proposal I suggested the ability to relegate XMR to the "secondary" (lower, smaller, where USD is in your screenshots) position by clicking anywhere in the "XMR $BALANCE" - doing so would swap the currencies, click again for next chosen altcurrency, etc etc until back to XMR.

## ghost | 2019-09-03T07:51:13+00:00
- I've got to give credit to you, @kayront: [**>90%** voted for your idea](https://www.reddit.com/r/Monero/comments/cynicf/poll_how_would_you_prefer_your_fiat_balance_to_be/). --> Proposal updated!
- With regard to your idea that clicking on the fiat balance should allow you to change the currency: I don't see that many users need to quickly change their fiat currency. So I think that clicking on the fiat balance just should take you to the fiat settings page.
- With regard to your idea to allow an optional swap of the 2 balances: Too complex IMO. (If we had unlimited developing resources then sure, why not!)
- With regard to your idea that the user should be informed about the fiat feature when he is starting the GUI for the first time: IMO we only should bother the user with things that are absolutely necessary - the fiat feature is not.

## ghost | 2019-09-03T14:26:54+00:00
@selsta 
> The dark version of the smaller card isn’t downloadable

- The small card will cause pain to display the (new) [fiat balance](https://github.com/monero-project/monero-gui/issues/2298#issue-469853014).
- The small card is not in [golden ratio](https://www.google.com/search?tbm=isch&q=golden+ratio). It won't feel naturally right.
- Space is not a concern here.

## selsta | 2019-09-05T18:45:22+00:00
Okay, I’ll use the bigger one but I can’t download it from Zeplin :P ping @GBKS :) (https://github.com/monero-project/monero-gui/issues/2298#issuecomment-526876303)

## GBKS | 2019-09-05T22:42:47+00:00
@selsta sorry, just updated the "balance cards" screen in Zeplin to make things exportable. The taller cards is a 16:9 ratio. The other card is slightly shorter (don't like it much, TBH). The original card was 4:3.  Let know if you still have problems.

I think I mentioned it before, the cards have pretty big, diffuse shadows. We can ignore them for  the dark theme since they are barely noticeable, but they are important for the white theme to create enough contrast from the background. If you bake the shadow into the graphic, it gets quite big. Would be great if there was a way to render it dynamically (the way you would in a website via the box-shadow CSS property).

## selsta | 2019-09-05T22:47:22+00:00
@GBKS Thank you for uploading them :) Is it possible that you can update them without the drop shadow? We use QML `DropShadow {}` component for that.

Also we only need the larger ones.

## ghost | 2019-09-05T22:52:48+00:00
What's the Zeplin link to the assets you're talking about plz? I only have the link to the *.png files. 

## selsta | 2019-09-05T22:56:00+00:00
@Realchacal What is your zeplin username? I can invite you to the project.

## GBKS | 2019-09-05T22:56:11+00:00
@selsta give it a try now. The shadow I used has a negative spread, is that possible in QML? It looks more realistic that way.

## selsta | 2019-09-05T22:59:31+00:00
@GBKS Awesome, thank you. Looks good now.

https://doc.qt.io/qt-5/qml-qtgraphicaleffects-dropshadow.html

Looks like negative spread isn't possible but having the shadows inside the image wasn’t ideal to integrate so it’s good now.

## ghost | 2019-09-05T23:01:42+00:00
> @Realchacal What is your zeplin username? I can invite you to the project.

@selsta Realchacal - thx.

## selsta | 2019-09-05T23:20:18+00:00
@Realchacal Looks like it requires an email address to invite.

## kayront | 2019-09-06T07:54:34+00:00
A bit late to the party @Realchacal, but in reply to your post from a few days ago..

> With regard to your idea that clicking on the fiat balance should allow you to change the currency: I don't see that many users need to quickly change their fiat currency. So I think that clicking on the fiat balance just should take you to the fiat settings page.

Well, imagine you have the wallet set with 3 alternative currencies: EUR, USD and XAU.

Now, this particular user is American, so USD makes the most sense when it comes to make purchases. But turns out he's also a gold bug, and more interested in how XMR is fluctuating against XAU rather than USD.

Nevertheless, when the time comes to make a payment, it is likely that the user will want the USD value instead.

But wait! He is actually ordering abroad from Europe, and so the order is in EUR.

In sum: for day-to-day stuff the user likes having XMR/XAG, for payments in his country he switches it over to USD, but sometimes he orders stuff from Europe and then it makes more sense to set it to EUR.

Let's not forget the international nature of the project, and the very diverse people who are and will be using the software - that is, I believe, a decent part of the reason why the GUI team bet so heavily on translations.

For users who quickly want to gauge what their XMR is worth in more than a single XMR/? pair, it would be very cumbersome to go back and forth to fiat settings and change it just for that.

This sort of small details matters a lot; For instance, in Monerujo have you ever tried to make a payment that does *not* involve a qrcode?

While you can paste the XMR address, it is not possible to *paste the amount to be paid*. And that's the story of how I frequently end up quadruple-checking 8 or so digits ...

Small detail. Big consequences. User friction.

> With regard to your idea to allow an optional swap of the 2 balances: Too complex IMO. (If we had unlimited developing resources then sure, why not!)

Bear in mind I'm just proposing stuff, it is perhaps no accident that as you said >90% of moneritos polled agreed with the design, I have a group of ~10 non-technical people that are getting deeper and deeper into Monero and find it intriguing, but who were (back in the day) pretty turned off by the lack of user friendliness in the GUI.

Almost all of them agree that the software has vastly improved in the mean time, and almost all of them agree with the suggestions I'm making here.

Me? I use simplewallet cli and that serves me well, but we cannot ignore that 99.999% of people won't, and of those, perhaps 90% (being generous) are not, and will not be, very technical.

So this sort of small friction stuff matters. A normal person would've quit on Monerujo when he realized that he'd have to quadruple-check every last digit of a XMR amount because of a simple oversight.

> With regard to your idea that the user should be informed about the fiat feature when he is starting the GUI for the first time: IMO we only should bother the user with things that are absolutely necessary - the fiat feature is not.

You are probably right on this one, perhaps better to say a sentence about it in settings, properly contextualized.

## ghost | 2019-09-06T08:39:23+00:00
@selsta 
> @Realchacal Looks like it requires an email address to invite.

_["To invite a teammate enter the email address or their username..."](https://support.zeplin.io/en/articles/1988444-adding-a-teammate-to-a-project)_ - Account was brand new yesterday maybe that was the problem. Try again plz **with lower case "R": realchacal**

## ghost | 2019-09-06T09:56:19+00:00
@kayront Ok, clicking on the fiat balance should cycle through user-preselected currencies (opt-in): 
![image](https://user-images.githubusercontent.com/46682965/64429714-ecfade80-d0b6-11e9-8a19-6ecaf3967a0c.png)
But for this we need the other changes shown here first. And also [this (comment)](https://github.com/monero-project/monero-gui/issues/2368#issuecomment-528785070).

With regard to optionally swapping the small and the big balance: Personally: No. If **many** users want it: Sure. In any case: The other changes proposed here must be implemented first.

## selsta | 2019-09-06T11:26:00+00:00
@Realchacal 

<img width="322" alt="Screenshot 2019-09-06 at 13 25 18" src="https://user-images.githubusercontent.com/7697454/64424617-d7cb8300-d0a9-11e9-86d2-fea265fa8592.png">

It requires an email address.

## ghost | 2019-09-06T13:08:52+00:00
@selsta lavegar@mail-search.com thx


## selsta | 2019-09-06T22:42:04+00:00
Current work in progress
<img width="971" alt="Screenshot 2019-09-07 at 00 35 58" src="https://user-images.githubusercontent.com/7697454/64464289-b1d4cb80-d107-11e9-81ea-1082d22a0a98.png">
<img width="971" alt="Screenshot 2019-09-07 at 00 35 54" src="https://user-images.githubusercontent.com/7697454/64464290-b1d4cb80-d107-11e9-8f0e-d994ef733c10.png">

## ghost | 2019-09-06T22:49:31+00:00
Nice!
- Balance cards mixed up on purpose? (White card on dark theme and vise versa)
- IMO `4458` looks better when [smaller but bolder](https://github.com/monero-project/monero-gui/issues/2298#issue-469853014).

## selsta | 2019-09-07T22:28:43+00:00
> Balance cards mixed up on purpose? (White card on dark theme and vise versa)

What do you think of it? IMO it looks nice :)

> IMO 4458 looks better when smaller but bolder.

I dislike bold fonts in general but I can try to reduce the size of the font a bit.

## ghost | 2019-09-08T08:45:41+00:00
Your brown on white harmonizes better than our current brown on black! (Personally, I'd prefer my [grey on black](https://github.com/monero-project/monero-gui/issues/2298#issue-469853014).) The ~6 other colors and all the small stuff in your screenshots make it difficult to fairly judge your composition, though.

## selsta | 2019-09-09T19:38:45+00:00
#2383 

Can you explain what you mean with 6 other colors?

## ghost | 2019-09-09T22:36:02+00:00
> Can you explain what you mean with 6 other colors?

Just all these colors (which I don't have in my designs):
![image](https://user-images.githubusercontent.com/46682965/64571070-e98b7f80-d362-11e9-834c-c81e3c49c05f.png)
Without them every design looks way sleeker, obviously.




## GBKS | 2019-09-10T07:12:37+00:00
When the white theme came out, it still had the black card and there were requests for a white card. Just wanted to add that bit of information to the decision. Personally, I prefer the card to match the theme and would tweak the designs slightly if we got opposite.

## selsta | 2019-09-10T11:45:13+00:00
Without using the opposite card:

<img width="1026" alt="Screenshot 2019-09-10 at 13 43 25" src="https://user-images.githubusercontent.com/7697454/64611118-0199e800-d3d1-11e9-99b0-1ffdb126cf13.png">
<img width="1026" alt="Screenshot 2019-09-10 at 13 43 30" src="https://user-images.githubusercontent.com/7697454/64611119-0199e800-d3d1-11e9-84da-c991b4dd7330.png">

I find white on white a bit boring :) That’s why I switched them up.

## jafarivahid748 | 2023-10-03T21:00:34+00:00
Xmr

## jafarivahid748 | 2023-10-03T21:00:54+00:00
Eo.finance xmr

# Action History
- Created by: ghost | 2019-07-18T15:56:23+00:00
