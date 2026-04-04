---
title: Send to multiple addresses in the gui
source_url: https://github.com/monero-project/monero-gui/issues/740
author: fresheneesz
assignees: []
labels: []
created_at: '2017-05-24T05:02:54+00:00'
updated_at: '2021-03-30T18:05:45+00:00'
type: issue
status: closed
closed_at: '2021-03-30T18:05:45+00:00'
---

# Original Description
The GUI should be able to send to multiple addresses. Is it possible to send with multiple addresses as inputs? If so, that should be added too

# Discussion History
## medusadigital | 2017-08-08T00:40:51+00:00
sounds like a reasonable request to me. also simply becasue its one of the basic features in the cli wallet.

if its realistic and worth the effort needs to be discussed. 

solving this UX wise seems like another task. might have effect on:

- send tab
- confirmation pop up
- transaction history details

opinions welcome



## chpio | 2018-02-12T13:57:21+00:00
any news on this one?

## ankurss | 2018-02-21T11:47:46+00:00
would like to see this implemented too, please check how its implemented in electrum or other btc gui clients

i send payments daily to 20+ address using btc with single transaction, would switch to xmr if this is implemented 

## ankurss | 2018-03-26T13:27:49+00:00
@medusadigital @Jaqueeee can you implement this in coming version ? 

## binaryFate | 2019-02-17T13:33:28+00:00
Would be nice to have that by now.

## SamsungGalaxyPlayer | 2019-02-17T19:06:25+00:00
It's feasibly possible, but I would like to see some UI mockups before recommending this feature's inclusion. I'm concerned this will clutter the UI.

## fresheneesz | 2019-02-18T06:09:50+00:00
How bout we do it like any email client would? Here's a UI mock for ya:

![monero multi-address ui](https://user-images.githubusercontent.com/149531/52931292-b4550c80-3300-11e9-9b6d-b991b186411f.PNG)


## binaryFate | 2019-03-03T17:39:10+00:00
Looks good but not sufficient: their amounts might be different and should be displayed too. A drop-down type of display could display more.

## fresheneesz | 2019-03-17T21:09:11+00:00
Great point. Here's another try:

![monero multi-recipient transactions ui](https://user-images.githubusercontent.com/149531/54497964-3879c000-48be-11e9-9379-337276306cf0.PNG)

Note that I've left out the advanced options, so use this mock up mindfully as a starting point.

## SamsungGalaxyPlayer | 2019-04-23T16:27:13+00:00
I'd love to see some UI mockups for this in the latest versions. The simple mode should not support this feature imo, but the advanced/expert mode should :)

## selsta | 2019-04-23T17:28:18+00:00
This could be helpful for this issue: https://doc.qt.io/qt-5/qtqml-javascript-dynamicobjectcreation.html

## selsta | 2019-05-14T09:29:05+00:00
I’m currently working on this: https://streamable.com/bzw7p

@GBKS I’d need your design help on this :)

## ankurss | 2019-05-14T12:43:41+00:00
> 
> 
> I’m currently working on this: https://streamable.com/bzw7p
> 
> @GBKS I’d need your design help on this :)

Looks nice, can you we also have a textarea option also ? so someone doesn't need to manually enter each and can copy/paste from exports of other software

like this : https://imgur.com/3Qii6Y1



## GBKS | 2019-05-16T01:58:21+00:00
This is a tricky one. Hard to keep things simple for single-recipient transfers (which are probably the majority of transfers) while still making it easy to add/manage multiple recipients. Let me know what you think of the layout below, we'll probably have to iterate a few things.

![monero-send-multiple-recipients-gbks-190515](https://user-images.githubusercontent.com/695901/57820757-053b9c00-775c-11e9-94c0-da46608bff99.png)

I really like the idea of having an email-like way of handling contacts that prioritizes names over addresses. That might be a separate project/task though, since we'd have to ensure that whenever an address is entered, users have a super easy way to associate it to a name, and I think that touches  more than just this screen. Maybe split that into a separate discussion?

## fresheneesz | 2019-05-16T06:44:24+00:00
@GBKS That looks fantastic! (Love the dark mode too). I think it covers the ground very well. Names vs addresses should probably be a separate discussion tho.

## selsta | 2019-05-23T14:23:33+00:00
@GBKS Thank you! I really like the design :)

## GBKS | 2019-05-23T16:08:28+00:00
@selsta awesome. Are there any more interactive states or other details you'd like to see mocked-up? Otherwise, I'll put these designs up on Zeplin.

## GBKS | 2019-05-25T06:36:58+00:00
@selsta it's up on Zeplin. There are no new icons in this one, so you should be able to get everything from existing files.

## selsta | 2019-08-29T22:20:45+00:00
Progress update:

- https://github.com/monero-project/monero/pull/5518 was merged.
- GUI integration is still work in progress. Thanks to dsc for helping me :P
- WIP image:
<img width="1026" alt="Screenshot 2019-08-30 at 00 17 21" src="https://user-images.githubusercontent.com/7697454/63980353-9dffe880-cabb-11e9-9218-d83901a17ae8.png">


@GBKS The current problem is that the `+` next to the address/amount row can be confusing. The user could think that clicking the + is required to save the input so we thought it would be better to have a dedicated button underneath. But that’s now looking quite bad in combination with the other 2 buttons :P Any idea how we could solve this?

## GBKS | 2019-08-30T09:21:46+00:00
Is this this as primarily a power-user features, that's why I made the initial suggestion of having it smaller and next to the amount. It also provides a nice space for the 'remove' option, which you don't have in the screenshot above. So I'd suggest going back to the proposed design.

Alternatively, it would help to add the table headers. If you see "Recipients" at the top, the option to "Add recipient" makes more sense.

Does that help?

A small note, the spacing between the icon and text, as well a the vertical distance between each icon button is a bit too big.




## rating89us | 2020-06-27T10:36:19+00:00
I made some drafts considering that the maximum number of outputs in a transaction is 16 (transaction without change). I'd use a GridView with 8 rows and 2 columns, which will display a single column when there are less than 8 recipients. The last item of the gridview would be a + button (add new recipient), which would be displayed below the last recipient.

When mouse is over a recipient field, recipient # is displayed on the left side, borders are highligthed, address book button is displayed, and delete recipient (X) button is displayed.

Total amount field: it has two functions: 1) All (sweep_all function), which spend all unlocked amount in the account. 2) Split, which splits the inserted total amount equally between the recipients.

Fonts in recipient and amount fields probably will need to be smaller.

Since displaying the fiat conversion in each amount field is too much information, I added a switch XMR <> USD/EUR above Amount fields.

Example of transaction with less than 8 recipient addresses. 
![image](https://user-images.githubusercontent.com/45968869/85920585-50880f80-b875-11ea-918e-ea4b48735ad5.png)

Example of transaction with more than 8 recipient addresses.
![image](https://user-images.githubusercontent.com/45968869/85920581-48c86b00-b875-11ea-88ea-208b8340c490.png)



## GBKS | 2020-07-03T09:56:53+00:00
Looks really good. Do you really need that number indicator ("#9" in front of the address input)?

If you really want the "+" button below to the inputs, I'd add a label "+ Add recipient" and left-align it. Makes it more consistent with some of the other screens. I'd also left-align the "Recipient" label just like about have "Transaction priority" and "Description".

Is the "Total" input purely display or can I enter a number? If so, what's the interplay between entering values for each recipient, and then changing the total?

## SamsungGalaxyPlayer | 2020-07-03T22:31:39+00:00
Looks like adding a number in "total" and then clicking "split" will divide the total among all participants? Maybe I'm off here. Or does "All" assign the value to all outputs but "Split" divides them equally? That should be more clear.

## rating89us | 2020-07-12T18:57:53+00:00
I coded some parts already, see below.

Regarding addresses inputs, what is your opinion about using single line (not displaying the whole address but having a smaller grid height) vs. multiple line input (displaying whole address but having a larger grid height)? 

Monero addresses are really large (95 chars) and our window space is really limited. I don't know if we can change the default window size.

![multisend](https://user-images.githubusercontent.com/45968869/87254248-73274480-c481-11ea-9950-c08fe39f338e.gif)


## selsta | 2020-07-12T21:24:15+00:00
> I don't know if we can change the default window size.

A lot of people use small monitors or VMs, AFAIK we already had complaints that the default window height is too large. So I don’t think we should change it.

> Regarding addresses inputs, what is your opinion about using single line (not displaying the whole address but having a smaller grid height) vs. multiple line input (displaying whole address but having a larger grid height)?

I we say be default display it in a single line. When someone clicks into the textbox it should expand to display the full address.

## rating89us | 2020-07-12T23:51:27+00:00
Total field sums all recipients amounts

"SPLIT TOTAL" splits the total amount equally between all recipients

"CLEAN ALL" cleans all recipients amounts
![multisend2](https://user-images.githubusercontent.com/45968869/87259363-19d40b00-c4ab-11ea-88b4-16a7e2fc38e8.gif)

## SamsungGalaxyPlayer | 2020-07-13T14:38:21+00:00
This looks busy to me with the very prominent address buttons. Can we quiet those down? Maybe make remove the grey and just make the icons selectable. Maybe this will be less busy if the button only appears if hovered over like in your mock-up.

I also don't love the (1-8) and (9-15), but I don't have a better idea.

Good start :)

## GBKS | 2020-07-22T08:28:36+00:00
I mocked up a layout that tries to calm things down a little visually and make more room for addresses.

- Add recipient now looks like the other "Add buttons"
- Moved split and clear into the labels
- Turned all the rows into a table
- Only show address book button on hover (also only show the "X" on hover?)
- Simpler address book icon (the ragged edge on the current icon is really messy)
- For the 9+ address view, I made the text much smaller and tightened up spacing (is this dense enough now?)
- Made every 5th dividing line brighter as a more subtle indicator to segment recipients (tried to come up with something different than the numerical indicators, not sure how successful the brighter lines are)

And a question - "Clean all" only clears amounts and not recipients, right?

<img width="2348" alt="monero-send-multiple-recipients-gbks-200722" src="https://user-images.githubusercontent.com/695901/88153101-40a9e400-cc05-11ea-8028-05dcc84b86b1.png">

Let me know what you think.


## SamsungGalaxyPlayer | 2020-07-22T18:40:57+00:00
I really like this :)

## erciccione | 2020-07-24T16:50:30+00:00
I like it too, but i don't think we should divide addresses in segments. It's not consistent with the CLI and all the other wallets (afaik) and looks a bit confusing to me.

## GBKS | 2020-07-27T07:44:34+00:00
@erciccione segmenting (and the mono font for multiple lines) helps keep track of where you are when comparing addresses. Similar to how phone numbers, credit card numbers, IBANs, etc are segmented.

To me personally, the fact that the CLI doesn't do something is not an argument, because CLI options are so limited. Graphical interfaces can take advantage of very different possibilities.

## erciccione | 2020-07-27T14:22:37+00:00
I understand why segmenting is useful, my concern is only that could confuse people. It did it with me for a moment and i'm fairly familiar with the technology. If i'm the only one with this opinion, feel free to ignore it :)

> the fact that the CLI doesn't do something is not an argument,

As i said, it's not just about the CLI. No other wallets that i know of is segmenting addresses. If "the official" wallet segments and others don't, users may think the format of the address is different in other wallets (thinking about mobile wallets in particular)

## GBKS | 2020-07-28T08:44:47+00:00
Maybe it's just a matter of finding the right segment width? So it's functional but does not confuse? Here is an overview of a view options. Maybe a few more people can chime with what they think is the right way to go.

<img width="640" alt="address-display-gbks-200728" src="https://user-images.githubusercontent.com/695901/88641250-3aad7a80-d0bf-11ea-95d8-d8fed96b3569.png">




## erciccione | 2020-07-28T17:32:27+00:00
'Roboto with segmenting' looks like a good solution to me :)

## rating89us | 2020-10-29T09:52:25+00:00
I prefer without segmenting, because since monero addresses have 95 characters, we always have a single segment with 3 characters (instead of 4). 

Monero GUI currently displays addresses in the following format:
- AAAA AAAA AAAA ... AAAA AAAA **ABCD**

But since we need to display the full address in this field on send page, it would have a 3 characters segment at the end:
- AAAA AAAA AAAA ... AAAA AAA**A** **BCD**

Alternatively, we could also change the splitting so that the 3 characters segment stay at the middle of the string, something like this:
- AAAA AAAA AAAA ... AAA ... AAAA AAAA **ABCD**


## GBKS | 2020-10-29T13:38:42+00:00
I'm OK with a 3 character segment at the end. The bank account number on my debit card also has a 2 character segment at the end. I think it's pretty standard that way.

## xiphon | 2021-02-05T16:29:16+00:00
Initial implementation https://github.com/monero-project/monero-gui/pull/3332.

## jarjarfan666 | 2021-02-21T15:04:37+00:00
Fantastic that this got added. I hope my feedback isn't too late for a future version.

It would be great to see the recipient in the Send page also. The recipient's name is in the Address Book page, and in the final confirmation page, but I would personally feel a lot more comfortable seeing it int the Send page also when I'm entering the send amounts.

# Action History
- Created by: fresheneesz | 2017-05-24T05:02:54+00:00
- Closed at: 2021-03-30T18:05:45+00:00
