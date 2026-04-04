---
title: Make it difficult to close wallet in Simple mode + implement back button on
  onboarding Wizard
source_url: https://github.com/monero-project/monero-gui/issues/2007
author: rating89us
assignees: []
labels: []
created_at: '2019-03-11T10:34:47+00:00'
updated_at: '2019-03-11T15:15:19+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I'm using GUI wallet in simple mode on Mac.

It is really easy to close wallet inadvertedly. I was redirected to onboarding Wizard two times, without option to coming back (no "Back" button available!).

User can close wallet in two places:
![image](https://user-images.githubusercontent.com/45968869/54117458-1af5b380-43f1-11e9-92cd-1edfd4c9a6ad.png)

![image](https://user-images.githubusercontent.com/45968869/54117508-39f44580-43f1-11e9-975c-d056d687a08e.png)

A warning should be created when leaving ("closing") wallet on these two places.
When onboarding wizard is called from an opened wallet, it should definitely have a back button.

Alternatively, instead of being redirected to the onboarding wizard, the GUI wallet could present a list of all wallets that it holds, just like MyMonero and Cake Wallet do.

# Discussion History
## sanderfoobar | 2019-03-11T11:44:14+00:00
When you close the wizard, you return to the main menu. From here, you can choose to re-open your wallet (third menu option). I'm against wallet closing confirmation, as you actively have to press these buttons and it doesn't really happen on accident.

## rating89us | 2019-03-11T11:55:00+00:00
Where do I close the wizard? When I click on the close button (x button on right top), the whole GUI wallet is closed.

There is no close button on this screen:
![image](https://user-images.githubusercontent.com/45968869/54122623-dae8fd80-43fd-11e9-958e-7848af03a659.png)

But there is a close button on this screen:
![image](https://user-images.githubusercontent.com/45968869/54122654-f0f6be00-43fd-11e9-82a5-7ac452f39e85.png)



## sanderfoobar | 2019-03-11T13:24:12+00:00
Pressing 'Close Wallet' will close the wallet A.K.A 'quit' the wallet. You will return to the main menu.

> A warning should be created when leaving ("closing") wallet on these two places.

I would argue against as previously explained.

> When onboarding wizard is called from an opened wallet, it should definitely have a back button.

Back to what? You closed the wallet.

## rating89us | 2019-03-11T13:47:06+00:00
I mean these things from a perspective of a newbie. When you close the wallet through these two methods cited above and access the onboarding screen again, it seems that you have clicked a button "Forget my wallet (and don't display it anymore)", and not a button "Close wallet".

On onboarding wizard there is no button or text saying: "Re-open recently created wallet (Wallet name)". You simply arrive on an onboard screen just like the first time you open GUI, with no reference to your wallet that has already been created. I'm not a newbie and I know I can retrieve my wallet by clicking in "Open a wallet from file", but I guess many newbies will try to create a new wallet or will believe that they have deleted the recently created wallet.

We should either 1) Make it more difficult to "Close wallet" OR 2) Display on onboarding Wizard a reference/link/button to the wallets that have been recently created/imported by the GUI wallet software.

Additionaly, the icon below has no tooltip and it doesn't inform that it will close the wallet.
![image](https://user-images.githubusercontent.com/45968869/54128075-88164280-440b-11e9-8d0d-6b66dd18f0bc.png)


## sanderfoobar | 2019-03-11T14:49:18+00:00
> I mean these things from a perspective of a newbie. When you close the wallet through these two methods cited above and access the onboarding screen again, it seems that you have clicked a button "Forget my wallet (and don't display it anymore)", and not a button "Close wallet".

I see what you mean, but please be aware that closing a wallet takes you back to the main menu. That's just how the GUI works. In addition, to avoid confusion, lets call it 'main menu' :-) The onboarding wizards are when you create a wallet or setup the GUI for the first time.

![](https://i.imgur.com/3ytE3WH.png)

> On onboarding wizard there is no button or text saying: "Re-open recently created wallet (Wallet name)". 

If you click 'Open a wallet from file' you can open your recently opened wallets.

> but I guess many newbies will try to create a new wallet or will believe that they have deleted the recently created wallet.

I would argue against. They previously created a wallet, it showed them where the wallet will be stored (if they paid attention in the onboarding wizards). So the concept of the wallet being a file should be clear.

> We should either 1) Make it more difficult to "Close wallet" OR 2) Display on onboarding Wizard a reference/link/button to the wallets that have been recently created/imported by the GUI wallet software.

1. I disagree. See my first reply in this thread.
2. See third menu option.

> Additionaly, the icon below has no tooltip and it doesn't inform that it will close the wallet.

#2002

## rating89us | 2019-03-11T15:09:59+00:00
I was calling the main menu "onboarding wizard" because I though that it was the same menu which is displayed when opening wallet for the first time, they look really similar to me.

I guess >90% of "common" users don't know they have a wallet file in their computer. When I closed the wallet inadvertedly, I saw that there was no back/return button, and than I though "damn, I shouldn't have closed the wallet! What should I do now?". Imagine a newbie using this... they really won't figure out that they have to click on 3rd menu option.

In my opinion, main menu should be like mymonero wallet (see below). It displays recently imported/created wallets and there is a button (+) that redirects user to a import/create new wallet section.

I would argue that 95% of users that close the wallet will close it inadvertedly, and only 5% will close it because they want to create a second wallet or because they want to restore a different wallet from a file/seed.

![image](https://user-images.githubusercontent.com/45968869/54133794-fca2ae80-4416-11e9-95c4-a349ace2f4fa.png)


## rating89us | 2019-03-11T15:15:19+00:00
Also, the main menu should not have the same background color as the wallet. It seems that you are still on the same section of the software.

Look how main menu and languages pages look the same (black background), even though the first one is displayed with closed wallet and the second one is displayed with open wallet. 

The only difference is that the second one has a close button.



# Action History
- Created by: rating89us | 2019-03-11T10:34:47+00:00
