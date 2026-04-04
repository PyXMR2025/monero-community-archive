---
title: Revise home page top card
source_url: https://github.com/monero-project/monero-site/issues/1483
author: SamsungGalaxyPlayer
assignees: []
labels:
- 💬 discussion
- enhancement
created_at: '2021-02-27T01:06:47+00:00'
updated_at: '2021-06-18T20:48:01+00:00'
type: issue
status: closed
closed_at: '2021-06-18T20:48:01+00:00'
---

# Original Description
The current home page has many lacking attributes. First, the MONERO text is unnecessary. Second, there is no obvious call to action other than "learn more."

The top card should be far more descriptive of Monero and intended for a broader audience. Further, there should be other additional calls to action, most importantly "Join Community."

### Current

![image](https://user-images.githubusercontent.com/12520755/109370262-391a7f80-7865-11eb-84bf-50052f5cf075.png)

### Proposed

![image](https://user-images.githubusercontent.com/12520755/109370246-27d17300-7865-11eb-9595-bc89ddf9620a.png)

"Join community" will link to https://www.getmonero.org/community/hangouts/ (revision also pending)
"Get Monero" will link to the merchants page for now https://www.getmonero.org/community/merchants/#exchanges
"Lean why it's the standard" will link to https://www.getmonero.org/get-started/what-is-monero/ (revision also pending)

The top card in its current form is not nearly as good as it should be in my opinion.

Related to #1484 #1485 #1486

# Discussion History
## ghost | 2021-02-28T00:37:09+00:00
Instead of removing all of the existing text from the card, I think a simple change of the header could accomplish a similar goal:
![image](https://user-images.githubusercontent.com/23042683/109404045-2f118300-7930-11eb-833a-4b5e87a6c13a.png)
Also, I believe the call to action is to 'Get Started.' The main content of the page explains how to create a wallet and buy/sell Monero. I'm not sure it's necessary to include a 'Get Monero' button in the top card when there is one right beneath it:
![image](https://user-images.githubusercontent.com/23042683/109404188-9ed43d80-7931-11eb-9e07-83b73ac49f93.png)
As for the 'Join Community' button, perhaps it could just link to the bottom of the page?





## erciccione | 2021-02-28T08:51:46+00:00
If people want to change the slogan at the top, a dedicated issues should be created, since that will require some consensus.

I don't see much the benefits of this redesign. Beside the change of slogan, the main point seems to be to remove the "learn monero" button in favour of 2-3 buttons. The thing is that the "get some coin" section is right below the box and "Join the community" is below that. I don't see the utility of adding redundant buttons.

## tallest-man | 2021-03-01T17:05:40+00:00
I think the major change accomplished by this revision would be to have more calls to action "above the fold". Current is 2 calls to action (Video, clicking play is a weak call, and Learn More About Monero is a strong call). Proposed is 4 calls to action (Video, clicking play is a weak call, Learn Why its the Standard is a medium call, Join Community and Get Monero are both strong calls). IMO the calls to action are better above the fold, even thought they currently exist below the fold in some form or another. These calls below the fold could be removed to avoid duplication. I agree that the current large MONERO text is just taking up valuable space and isn't needed. 

## robby-d | 2021-03-01T23:17:11+00:00
We can say that the vast majority of users for a given cryptocurrency are casual users (i.e. not deeply involved in the project). This is perhaps 9 of 10 of users, but that is just my own informal estimate. The exact number may differ, but we can definitely say that the majority of users in any cryptocurrency "community" could be classified as casual users.

For all users -- casual ones and those that ultimately become more involved -- the initial thing they seem to do is "join" the community using their preferred means, and buy some of the coin. I think our reasoning with this top card choice is to put those two most common means of interaction (buying the coin and joining a community chatter medium) at the top, and not force reading or parsing lots of text to find it -- as most users won't spend the time.

Given this, as well as the good feedback raised thus far, a scaled down option from what @SamsungGalaxyPlayer proposed is this:

1. Keep the top card text body as-is.
2. Change "MONERO" text to either "How digital cash is supposed to work." or "The global standard for private, digital payments" -- having "MONERO" there is totally redundant - it's already in the page header.
3. Keep the "Learn More about Monero" button, but name it "Learn More", and add a second button "Join Community" that goes to the hangouts page.

This jives with some of @wirrickelliot's input -- as I get his point that the buy link is pretty close, but there is no hangouts mention on the home page, and having a Join Community button takes care of this first and super common use-case without requiring users to dive into drop-down menus to find it (especially among non-english native speakers, they may not know what "Hangouts" is -- or be unclear on it).

We also hold off on the "Learn why it's the standard" thing for now. We could (and probably should) tackle that as a separate item.

## SamsungGalaxyPlayer | 2021-03-02T00:13:20+00:00
In any case, "MONERO" needs to go imo. It adds nothing and wastes the most important and most valuable space.

## erciccione | 2021-03-02T10:10:55+00:00
> Change "MONERO

I agree with removing it, but then we have to consider changing "A private digital currency" under it as well.

> there is no hangouts mention on the home page

True and should be fixed.

> especially among non-english native speakers, they may not know what "Hangouts" is -- or be unclear on it

This is partially the case. I agree the word "hangouts" is not very clear and probably we should consider replacing it with something else, but consider that this website is translated in many of the most spoken languages, so there is a high probability that a non english speaker will not read "Hangouts", but the word in their language.

## erciccione | 2021-03-06T11:15:57+00:00
I opened #1503 to discuss the change of header.

## erciccione | 2021-05-13T08:01:52+00:00
> there is no hangouts mention on the home page

This is fixed by #1622 

## erciccione | 2021-05-19T09:35:50+00:00
#1633

# Action History
- Created by: SamsungGalaxyPlayer | 2021-02-27T01:06:47+00:00
- Closed at: 2021-06-18T20:48:01+00:00
