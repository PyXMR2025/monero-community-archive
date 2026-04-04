---
title: Intuitive node symbols
source_url: https://github.com/monero-project/monero-gui/issues/2318
author: ghost
assignees: []
labels: []
created_at: '2019-07-25T10:43:28+00:00'
updated_at: '2019-09-04T08:27:05+00:00'
type: issue
status: closed
closed_at: '2019-09-04T08:25:42+00:00'
---

# Original Description
![image](https://user-images.githubusercontent.com/46682965/61868228-3a413900-aed9-11e9-83a1-f3c3645446b9.png)

Local node symbol: "Reload page"???
Remote node symbol: "Paper with arrow"???

More intuitive:
![image](https://user-images.githubusercontent.com/46682965/61868302-652b8d00-aed9-11e9-96f4-4ba9f596d745.png)

# Discussion History
## selsta | 2019-07-25T12:33:26+00:00
<img width="627" alt="Screenshot 2019-07-25 at 14 31 44" src="https://user-images.githubusercontent.com/7697454/61874543-f7875d00-aee8-11e9-9955-7bd748330618.png">
<img width="636" alt="Screenshot 2019-07-25 at 14 32 17" src="https://user-images.githubusercontent.com/7697454/61874569-02da8880-aee9-11e9-902f-b0edc9a39aa6.png">

Opinion?

## ghost | 2019-07-25T12:59:16+00:00
@selsta ULTRA NICE!!! IMO your cloud just seems a LITTLE BIT too fat (needs shrinking in height), but that's a SMALL detail :)

We should ask @GBKS for his opinion, to make sure the symbols fit GUI-wide.

## GBKS | 2019-07-25T13:17:36+00:00
Not sure where these white icons are coming from. I had designed icons for this a while back that I assumed we used (but maybe someone changed them, which is also cool). Here are the ones I came up with (this is a screen that's also in [Zeplin](https://scene.zeplin.io/project/5a0777492a92d8ac5beb3125) and my [Github repo](https://github.com/GBKS/monero-wallet-design/blob/master/screens/desktop-dark/onboarding%20-%20how%20to%20connect.png)). There are several more of these larger, orange icons that are used in the onboarding flow ([see here](https://github.com/GBKS/monero-wallet-design/blob/master/screens/desktop-dark/Icons.png)).

![onboarding - how to connect](https://user-images.githubusercontent.com/695901/61877240-e0e40480-aeee-11e9-8a38-6161fcc6b644.png)


## selsta | 2019-07-25T13:22:58+00:00
> Not sure where these white icons are coming from.

They are on the left middle side [here](https://github.com/GBKS/monero-wallet-design/blob/master/screens/desktop-dark/Icons.png), but I don’t know what they were originally intended for.

## ghost | 2019-07-25T13:25:51+00:00
- Nice to see that you already had the idea with the cloud, @GBKS !!
- @selsta see the cloud from @GBKS? That's a healthy cloud!
- But double arrows NOT good. They don't add any value, just make it more complex.
- @GBKS your local node symbol is technically more correct, but the house symbol actually gives the better impression at a glance.

I'd go with @selsta's house and @GBKS's cloud (without arrows). Color: I'd go with white or very bright gray.

## selsta | 2019-07-25T13:28:40+00:00
@GBKS Can you upload just the cloud icon alone to the icons page? The white arrows don’t play well together with the white theme.

## GBKS | 2019-07-25T13:41:23+00:00
@selsta sorry, I was just wondering how those white icons made it in the interface, because we used to have the orange ones in there. Maybe it was changed when the white theme was added. Can we use different icons for the dark and white themes? That would be ideal. 

@Realchacal not sure I agree about the icons not adding value. Please also keep in mind that these icons are part of a family of larger icons you can [see here](https://github.com/GBKS/monero-wallet-design/blob/master/screens/desktop-dark/Icons.png). They are meant to match in style, visual weight, color treatments, etc. I'd like to avoid doing per-icon adjustments that result in things don't matching overall (obviously a balance of both of these approaches, the whole context vs. consistency thing). What icon would you use for the bootstrapped mode (called "Recommended" in [this mockup](https://scene.zeplin.io/project/5a0777492a92d8ac5beb3125/screen/5c5701cf125496435bbe04bd))? A smaller house?

## selsta | 2019-07-25T13:43:20+00:00
Yes, a different icon for each theme would work.

## ghost | 2019-07-25T13:56:49+00:00
@GBKS  I TOTALLY get the corporate design thing! That's why I dropped your name here. :)

I didn't had the mode selection window on my mind when making my proposal. Thanks.
![image](https://user-images.githubusercontent.com/46682965/61879633-b6487a80-aef3-11e9-9ac6-ed630c14dd70.png)

Your symbols are nice and they are technically more correct. But @selsta's are more intuitive. (A house symbol stands for YOUR house - while a computer symbol can stand for your computer or any other computer/server. And a computer symbol isn't recognized as quickly as a house symbol.)

Bootstrap mode I'd go with something like this:
![image](https://user-images.githubusercontent.com/46682965/61880115-949bc300-aef4-11e9-9760-7f5e99872636.png)
![image](https://user-images.githubusercontent.com/46682965/61882235-57393480-aef8-11e9-8446-94602dc206f9.png)


I think the symbols should be white to match the text beside them (not the button below them). But if not possible because of corporate design, it's ok!




## ghost | 2019-07-25T14:12:56+00:00
@GBKS 
> I was just wondering how those white icons made it in the interface...

I assume that was because the orange ones had too much visual weight (color and size) to be integrated into the settings!

Do they have too much visual weight for that, @GBKS? 

## ghost | 2019-07-26T19:47:30+00:00
This issue should wait for #2320 and #2321.

## GBKS | 2019-08-01T08:47:04+00:00
The diagonal strike-through line instantly makes me think that it's not allowed (or disabled), like the way it's used in street signs.

If we want to use the old orange icons, I created white versions and put them on Zeplin ([here](https://scene.zeplin.io/project/5a0777492a92d8ac5beb3125)). 

Regarding the visual weight, I had reduced the icons in the settings page by 50% in size to accommodate for that.

Can you maybe explain what you mean by corporate design? I can't tell if you're trolling or not, and what non-corporate design would be if you're not. Either way is fine, just want to know what you mean.

## ghost | 2019-08-01T14:02:47+00:00
> If we want to use the old orange icons, I created white versions and put them on Zeplin ([here](https://scene.zeplin.io/project/5a0777492a92d8ac5beb3125)).

**They look great! Let's use them! A million times better than what we have right now.**

Just for the record: Now we'll be using the same icon for "Advanced mode" as for "Local node", and the same icon for "Simple mode" as for "Remote node".
![image](https://user-images.githubusercontent.com/46682965/62350804-22366e80-b504-11e9-8222-f5eebd10f9fe.png)
That's messy. But the problem is NOT the (new) icons in the settings! They are excellent! The problem is our UNLOGICAL MODES, WHICH BUNDLE THINGS THAT DON'T BELONG TOGETHER, WHICH NEEDS FIXING: #2320.

> Can you maybe explain what you mean by corporate design? I can't tell if you're trolling or not.

No, I was not trolling! (Never on GitHub.) I was just using the term "corporate design" in a wrong way. Normally, "corporate design" refers to the design that a **company** uses across all its products and websites and letters and everything. And I transferred that term to our GUI project, which was wrong, since obviously our GUI project is not a company. Next time I'm gonna use "consistent design language" instead of "corporate design".

## selsta | 2019-08-14T18:40:32+00:00
I openend #2351 for now.

@GBKS, I kinda agree with @Realchacal, using the same icon for “Advanced mode” and “Local node” isn’t perfect and I think the colored icons don’t fit on the node settings page (they do fit into the mode selection page). 

## GBKS | 2019-08-15T05:33:38+00:00
Cool. Consistent icons help people recognize things more easily. We could create monotone versions of the colored ones for the settings page to avoid a visual clash.

The benefit of some more visual icons is that they can then also be used on the website. This was very handy in my [landing page mock-ups](https://www.reddit.com/r/Monero/comments/cnn57p/feedback_request_concept_for_a_new_landing_page/).

Anyhow, let's decide on something and move forward. I'm good either way.

## ghost | 2019-08-15T06:45:33+00:00
- For the node settings both variants are great. I'd prefer @selsta's variant for now.
- The mode selection page is where I see a problem. A noob wonders: "Why is the cloud a symbol for simplicity?! Why is a computer a symbol for Advanced?! What am I missing here??" (--> proposed solution: #2320)

## ghost | 2019-09-04T08:25:42+00:00
Closing this because #2351. (I wonder why it wasn't auto-closed, though.)

# Action History
- Created by: ghost | 2019-07-25T10:43:28+00:00
- Closed at: 2019-09-04T08:25:42+00:00
