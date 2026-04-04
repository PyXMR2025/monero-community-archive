---
title: 'GUI Re-design improvements. '
source_url: https://github.com/monero-project/monero-gui/issues/2024
author: ghost
assignees: []
labels: []
created_at: '2019-03-18T06:32:14+00:00'
updated_at: '2021-09-05T21:46:19+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
![Asset 1](https://user-images.githubusercontent.com/32292415/54509730-80afe580-4985-11e9-8d5a-009d1877bb55.png)

I've done some re-designing of the GUI of the past few days of which I would greatly appreciate some feedback on. I have broken down each main aspect of the GUI I have changed below. If there is too much individual changes to be made for a single issue I'd be happy to break this thread up into multiple issues. I understand not everyone will like each change I have made but don't look at this as a package deal, rather each element has merit on its own independent from my overall design. 

1) The side bar is what I first set out to re-design. Frankly the original sidebar is a bit of a eye sore from the clunky nature of the menus when navigating them to the use of multiple colored dots (not sure why this was done, basic design mistake). The side, top and bottom sections are hex color #23272a, a slight change from the original #1a1a1a. Deep blacks like #1a1a1a never look that great and look even worse when on a very high or very low end monitor. All icons are from font awesome, they are colored white with a 50% opacity to blend some background color in. 

2) The latest GUI update introduced the 'Account' menu option - I really don't see the purpose of this as it is basically the same as the Receive but it calls addresses accounts instead. This just adds unnecessary cognitive load to the user, I suggest having a Dashboard section instead (which I will do a mock up design of soon) which is hierarchical in its nature as I have in my design. 
This dashboard section would give a brief one page overview of your wallet. Everything from Balance / unlocked balance, ability to switch between the different wallet modes (though I also think this feature is unnecessary, simple mode should be the default option with the 'advanced' features simply part of settings), syncing details, mining H/s (if enabled), addresses (list maybe 5 or so) and tx history overview (latest 5-10 tx's for example). The dashboard button has a slight gradient going from a light orange #ff6c37 at the top to a darker orange #bf5129 at the bottom - it is suble but looks a lot nicer than a static orange. 

3) A simple addition, adding a visibility toggle for your balance next to your balance. Clicking the eye hides the balance and unlocked balance.

4) Moved the syncing section to a new bottom menu. Looks a lot less cluttered than having it in the side menu. A total syncing % should also be added (combining both wallet / daemon syncs). Users like to be able to quickly see the progress status - just listing x amount of blocks remaining isn't that meaningful to most people. If the user is using a remote node / simple mode this area will say just that instead. This area also has quite a lot of extra space available that we could add other useful information (mining H/s being one example). 

5) Another simple change - moved the language button to the bottom menu and used a more relevant icon (also a font awesome icon). Having it at the top does not make hierarchical sense as its not an option people regularly interact with so having it at the bottom makes more sense from a UX perspective.

6) Changed the arrow icon to use a font awesome, close menu arrow. It would be ideal if this arrow reversed direction when clicked. When the menu is collapsed also it shouldn't completely disappear, this adds an extra click that the user has to make when re-opening the menu and then going to their desired menu section. I've included an image below illustrating what I mean. 

![Asset 2](https://user-images.githubusercontent.com/32292415/54510722-78f24000-4989-11e9-8427-459ccb96e40f.png)

7) The body section is something I still want to do some work on, mostly with the re-designing the input fields. Again I don't think using a deep black looks as nice, the background color I changed it to is #2c2f33 

8) This is a new feature in and of itself. I think we should have the ability to seamlessly switch between different Monero wallets (if the encrypted key files are present on that device that is). By clicking on this menu you will be shown your various wallets you have previously connected to your GUI (maybe done in the settings?). By clicking on a different wallet to the current one you have open will simply prompt you to enter the password for that wallet and upon doing so will open that wallet straight in the GUI. It seems unnecessary to have to completely close the current wallet and click on the 'Open wallet from file' option in the startup again. 

Bear in mind all of this is still a work in progress. I didn't want to go deep without getting feedback from the community first. 

Looking forward to your replies! 

# Discussion History
## knaccc | 2019-03-18T07:24:56+00:00
Beautiful design, I like it a lot.

> The latest GUI update introduced the 'Account' menu option - I really don't see the purpose of this as it is basically the same as the Receive but it calls addresses accounts instead. This just adds unnecessary cognitive load to the user, I suggest having a Dashboard section instead (which I will do a mock up design of soon) which is hierarchical in its nature as I have in my design.

Exactly. Everyone is going to be completely confused about what "Account" means. The visual hierarchy needs to make it crystal clear that someone can have multiple accounts (which is like having multiple bank accounts with separate balances), and each of those accounts can have multiple "bank account numbers" a.k.a. subaddresses.

There is no way anyone is going to be able to figure out any of what I've just said from just playing with the wallet.

I agree that most users should not need to be distracted by the notion of what an "account" is.

Here is my previous attempt at making the visual hierarchy clear:
https://github.com/monero-project/monero-gui/pull/793#issuecomment-314477091
Account selection: https://imgur.com/a/sGNcc
Once account has been selected: https://imgur.com/a/1gcr0

## janrothen | 2019-03-18T08:10:09+00:00
A very clean look and suddenly the GUI is intuitive.
I like it very much. Well done & thx!

## ghost | 2019-03-18T08:12:09+00:00
> 
> 
> A very clean look and suddenly the GUI is intuitive.
> I like it very much. Well done & thx!

Thanks! its far from being implemented but!

## briangibb | 2019-03-18T09:47:03+00:00
Overall i like it, but the Left menubar and bottom left corner are a bit to flat for me. I have difficulty seperating the different elements. Maybe a subtile divider line would go a long way.

## GBKS | 2019-03-18T10:35:55+00:00
Looks really good. As I mentioned in the chat, there's a lot to discuss here.

1. Sidebar
The initial impression is nice, it feels simpler. I'd just like to see this fleshed out more to see where all the other pages we have fit in your navigation system (address book, merchant page, everything in advanced). With an eye on a mobile version of this wallet in the future, it would be great so simplify the sidebar to 5 bigger sections that could then work as a tab bar, with all the other options in sub-navigations (like the tabs in the current settings page). I [mocked something like this up](https://github.com/GBKS/monero-wallet-design/blob/master/screens/future/responsive%20layout.png a while back, maybe we could collaborate and work through this and propose a unified navigation system? 

2. Dashboard
Hard to judge without seeing it. Could clicking the balance section above maybe take you to that screen instead of introducing the new button? Not sure about using the action button style for navigation. For the gradient, just be careful with darker oranges, they start to look dirty. Might be good to mix in some other colors to avoid that effect.

3. Visibility button
This is great. Do you think it should work for just the balance box, or be a toggle for the whole UI? In a scenario where I don't want people to see my balance, I probably also don't want to accidentally reveal amounts when I review transactions, etc.

4. Network status
Your proposal matches what many other wallets have, from what I've seen. Definitely saves some space. Do you think we could push it further and make this more easily understandable for non-tech people? Something simple like "5-10 minutes left" or just a single bar? I always found the block counts hard to figure out.

5. Language selector
Do we need this at all as a globally available option? What's the use case?

6. Icon-based sidebar
Yes, would be cool to do this.

7. Body section styling
Are you mostly looking into usability or visual styling? To give some background on the choice of the deep black, my idea was to go a bit stronger visually to match the spirit of Monero in a sense. I designed a black and white theme, each one being a bit more stark than what you see in many other interfaces. Monero is black and white in its values around privacy, community, etc, so I wanted to capture that in a way.

8. Wallet picker
I like it. How about adding it above the sidebar, and also only for users that have multiple wallets set up? I'm also curious if that could be merged with the dashboard option you're thinking about. Clicking this wallet name could take you to the dashboard. There could be a small switch icon to the right side of this wallet name for switching between wallets.

I think we have to be super careful with the hierarchy of wallet->account->address so we don't confuse people.

Hope that feedback was helpful. There's a lot of good stuff here. I'd just suggest breaking it up a bit into individual updates. That makes it easier to give feedback and also to implement.




## ghost | 2019-03-18T10:59:19+00:00
> Overall i like it, but the Left menubar and bottom left corner are a bit to flat for me. I have difficulty seperating the different elements. Maybe a subtile divider line would go a long way.

There is a very faint divider line Ill make it more prominent, thanks!

## ghost | 2019-03-18T14:05:16+00:00
@GBKS Thanks for the comprehensive feedback, appreciate it!

1) Happy to do more pages up following this design if you would like? Yeah I'd be happy to help with the mobile wallet also. You could say have send button then receive button then a larger, orange main home button that is more prominent (for the dashboard if we go this route) then history / settings on right of that. 

2) I'll do a rough mock up tomorrow and share it, I have a vague idea of how it would look in my head. I think its good to have some heirarchal signifigance in a menu. The button does does just that as the dashboard would cover the largest cognitive load off the user as its convenient information in one place. Its only a very small splash of the darker orange to give it that slight shadow effect but ill keep that in mind!

3) I just had the balances in mind but yeah that would be cool to have it turn a sort of 'private mode' on that hides more than just the balances. 

4) Yeah I agree with that sentiment, just a simple % or progress bar, amount of data stored and time left would be suffice for 98% of users. If people are interested in the more technical aspects of the sync i'd say they would be using the CLI over the GUI anyways.

5) Pretty limited, but some people may speak multiple languages and might want to switch. Also fun languages like pirate are always fun to play around with haha. 

6) Cool, this was I firstly set out to change so glad you like it

7) This section I mostly put in as filler. I still want to revamp that area quite a bit but that is the general direction I am going. I agree with that perspective though the deep blacks can not look so great on some monitors were a more dark grey is a bit more adaptable.

8) Yeah I like the idea of merging this part with the dashboard more so than puttig it above the balance. When I do the mockup ill keep that in mind! 

Will do, are you still primarily maintaining the designs? Happy to push any updates you like to your monero-wallet-design repo. 

## MaxelsS | 2019-03-19T00:45:01+00:00
Looks cool. This is something new, fresh. As an ordinary user, I would like to express my opinion and suggestions:

1. It seems to me odd XMR in the name of the tabs Send and Receive. Also, the highlighting of the selected tab (Send XMR) is too merged with the general background. The color of the body section (7) would be more obvious.
Icons are really cool.
2. Look forward to design
3. Necessary thing for monero
4. Agree with @briangibb
5. No opinion (maybe for someone need)
6. Excellent
7. The input fields are thick. If they are made wider at the same thickness it will look better. And the font of address can be done more.
8. Agrees with @GBKS

History tab suggestion:

1. Suppose I have many subaddresses (eBay, Exchange, Online Store, etc.). In the current GUI, when I select the eBay subaddress and go through the history, I see all the transactions of the base address and I can’t track what amount the eBay subaddress has arrived. I think it should be different: when I choose the base address, I see all the transactions performed on this account (possibly with a note on which subaddress), and when I select a specific subaddress I should see only its transactions.
2. You can add a small menu to select the number of transactions displayed. As an example:

![Новый точечный рисунок](https://user-images.githubusercontent.com/48657060/54572558-30726b00-49f9-11e9-822f-e61eba791979.jpg)

## AdeilnAcinrst | 2019-03-19T12:18:32+00:00
In this redesign, is it possible to have the cashier screen in a different window?

I guess it's more useful in a 2 monitor configuration, where the operator sees the entire wallet while the customer sees only its information.

## GBKS | 2019-03-19T21:04:40+00:00
@Electricsheep01 I just pushed a bigger update to all the design files [here](https://github.com/GBKS/monero-wallet-design). They match the current wallet release more closely now. Not sure how helpful it is to work with, since your styling its quite different, but a big part of why I maintain them is to make it easier for others to come in and improve them.

I'd definitely like to find a way to get your work integrated. My approach is to keep my main design files almost 1:1 with the current wallet release and then create separate Sketch files for individual feature updates in the "sketch/future" folder. Once something is implemented, I merge it into the main files. The benefit of this is that each individual update can be discussed and implemented separately, which really simplifies collaboration. While it's great for getting things done, it's a bit tedious and doesn't allow for blue sky explorations, so I do those separately and just share exported PNGs in conversations (like this [mobile concept](https://www.dropbox.com/s/inodkkm8xjv7sry/Monero-mobile-concept-gbks-180823.png?dl=0) I made last year). But that's just what I've found to work out well. For now, I'd just keep doing what you're doing to find the best design solutions and we figure out the details when we get there.

@AdeilnAcinrst good idea. I'm working on a design iteration of the merchant page ([first draft is here](https://www.dropbox.com/s/kf1t5hmip64kpuk/monero-merchant-page-gbks-190314.png?dl=0)) and will try to mock that up. Anything else you think would be good to add?

## ghost | 2019-03-20T07:57:18+00:00
@GBKS How's about I create a seperate folder inside the future section of your repo? I can put put all my designs there and you can incorporate as you wish

## GBKS | 2019-03-20T08:19:20+00:00
@Electricsheep01 that works. Just create a new branch, set up the folder in there and work away. We can also use issue to track and discuss anything that's in progress.

I am not sure if Sketch files can be merged the way code typically gets merged (probably not), but I can figure something out there.

## AdeilnAcinrst | 2019-03-20T12:45:58+00:00
@GBKS Having an option to select a source for exchange rate in the local fiat could be nice, but this would require some settings and code to configure and read the source. This exchange rate could be shown in the merchant page.

## xanoni | 2021-09-05T21:46:19+00:00
Just wanted to check that you are all aware of this PR: https://github.com/monero-project/monero-gui/pull/2936

Hope there are no conflicts between them. Haven't checked in detail.

# Action History
- Created by: ghost | 2019-03-18T06:32:14+00:00
