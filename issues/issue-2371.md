---
title: GUI update, Advanced and Settings button into a one cogwheel symbol, drop of
  one unnecessary wallet mode
source_url: https://github.com/monero-project/monero-gui/issues/2371
author: potatoisfood
assignees: []
labels: []
created_at: '2019-09-03T15:55:50+00:00'
updated_at: '2019-09-21T08:48:14+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Some GUI updates

1 Lets get rid of the left-hand-side menu’s sub-buttons.

Send button has one sub-button. Address Book.
Advanced button has four sub-buttons. Mining, Prove/check, Shared RingDB and Sign/verify.
Receive button has one sub-button. Merchant.
Settings button has no sub-buttons in the menu. Instead the buttons are at the top edge of the Settings page.

Lets do it this way with Send and Advanced buttons too. Sub-buttons to the top edge of each page. And they should be exactly like buttons on Settings page. Horizontally at the top edge of the page.

Receive button's sub-button Merchant has so different functionality than rest of the wallet, that it could look very different than the other buttons and could be located somewhere bottom edge of the Receive page.

2 We also could combine the Advanced and the Settings buttons in to a one button. That could be called just Settings button. At the top edge of the settings page there would be located horizontally Wallet, Interface, Node, Log, Info, Mining, Prove/check, Shared RingDB and Sign/verify buttons. They could be in one or two rows depending how much there is space. And they really should look like they look now at the Settings page, and be horizontally, because the look so good.

3 The combined Settings and Advanced button could also be replace by a cogwheel symbol. Once there is available, for a written word, a widely know symbol, it should be used. And remember, less text, more intuitive. The cogwheel symbol could be located at the bottom left corner of the wallet. Further, once there is needed to add some other settings functionality, there would be no need to wonder where to add it, just behind the cogwheel symbol like the other settings.

If the Advanced and Settings Buttons are combinet in to a one cogwheel symbol, all wallet modes, Simple mode, Simple mode bootstrap and Avanced mode would look the same. So the Simple mode boostrap could be dropped of and there would be left only two modes, Simple mode and Advanced mode. Only difference would be the node location.
Just select mode and open the wallet. And after that three buttons. Account, Send and Receive. Just use Monero. Easy.


# Discussion History
## ghost | 2019-09-04T16:51:23+00:00
His proposal 1 visualized (ignore changes from #2367, #2339, #2325, #2304, #2298):

![image](https://user-images.githubusercontent.com/46682965/64386722-26d9cf80-d03a-11e9-9933-66af07f9bd4c.png)
Not sure if I like it. It adds visual complexity to every page. In return, it makes the menu nicely static.

## SamsungGalaxyPlayer | 2019-09-06T16:58:26+00:00
This seems more complex to me.

## potatoisfood | 2019-09-07T16:36:06+00:00
Did you understand it correctly? The main idea is, that there are no sub-buttons in the menu. The buttons will be in the each page.

## ghost | 2019-09-07T16:43:01+00:00
> Did you understand it correctly? The main idea is, that there are no sub-buttons in the menu. The buttons will be in the each page.

Did you miss my image? Or is my image wrong?

## potatoisfood | 2019-09-08T18:00:13+00:00
Your image is right. I was thinking SamsungGalaxy understood something wrong.

Could you draw also the other pages, specially the combined Setting and Advanced page, so people would understand better how good the GUI would be. 

## ghost | 2019-09-10T15:32:51+00:00
> Could you draw also the other pages, specially the combined Setting and Advanced page, so people would understand better how good the GUI would be.

The critique of the new submenu was: "Pages are more complex." So I can't see how it would get _better_ by showing even _more complex_ pages. But I'll keep an eye on it and think about it. Because you're right, the submenus in the menu aren't great. For example just the fact that some menu items only have just ONE submenu item. That's not good.

# Action History
- Created by: potatoisfood | 2019-09-03T15:55:50+00:00
