---
title: Receive page
source_url: https://github.com/monero-project/monero-gui/issues/2381
author: ghost
assignees: []
labels: []
created_at: '2019-09-07T10:07:02+00:00'
updated_at: '2020-06-19T22:25:48+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
(Updated! Thx @tficharmers for input! Ignore changes from #2339, #2325, #2304, #2298.)

![image](https://user-images.githubusercontent.com/46682965/66268529-74667980-e83e-11e9-9a77-c2e6a0bf1bcb.png)
Currently:
![image](https://user-images.githubusercontent.com/46682965/66257269-0450e880-e797-11e9-9cc2-0584e119b3f0.png)




# Discussion History
## tficharmers | 2019-09-07T12:22:22+00:00
Interesting. You have made me think about this page. By the way, you'll need to think about what to do with the two button icons when you create a new sub address.

When you have multiple sub addresses, it isn't particularly obvious which sub address the QR code is associated with. So my thoughts are shown in the following edited screenshot.

1. To edit the name of a sub address, when you hover the mouse over the name, it changes to orange (perhaps a tooltip appears at the bottom of the page). When selected, the 'Set label' text field overlay appears.
2. To copy an address, hover the mouse over the address and it changes to orange (perhaps a tooltip appears at the bottom of the page). When selected the address is copied to the clipboard. This is mirroring functionality on the 'Transactions' page.
3. There is a new QR code icon associated with each address that when selected, makes the QR code appear in an overlay (like the 'Set label' overlay).
4. I agree that the QR code buttons should be labelled with text. I would have them saying 'Copy' and 'Download'. Both in grey.
5. When you 'Create new address', I think text in the text field should already be set to "Sub address 'n'". This text should also be auto selected so that if people start typing their own label, it auto writes over it. This prevents users from having to think of a new label. It also helps new users understand that they have just created what is known as a 'Sub address'. I obviously had it as 'Sub 1', etc, but I've just thought of this and can't be bothered to change the screenshot :P

That's it.

![gui](https://user-images.githubusercontent.com/23356013/64474812-09a81c80-d172-11e9-96c3-a53a9fa3ee6e.png)


## ghost | 2019-09-07T13:55:25+00:00
> 1. when you hover the mouse over the name, it changes to orange

Excellent idea! --> Proposal updated. Edit: Updated again. Idea wasn't that excellent.

With regard to copying the address by clicking on it: It's suboptimal if you click on something just for fun and then it copies it to the clipboard deleting what you previously had in your clipboard. Also it's suboptimal that the user must find out how to copy the address to the clipboard and just can't see it - but it's the most important thing one want to do on this page, so a button is really not too much. Also it's suboptimal that clicking on the name edits the name but clicking on the address copies the address. - On the other hand, that solution would offer the lowest visual complexity, which is **very** nice!

## tficharmers | 2019-09-07T14:05:16+00:00
I see your points. The copy address functionality mirrored existing functionality from the Transactions page, but even there it isn't obvious you are about to copy to the clipboard. A 'Copy' button might be required here.

I think the bigger issue for me though, which is why I knocked up the concept, is the floating/disassociated QR code. What are your thoughts on making it obvious which address this QR code is related to? Or do you think a QR code icon/button to bring it up in an overlay?

## ghost | 2019-09-07T14:24:26+00:00
> The copy address functionality mirrored existing functionality from the Transactions page

uuuuh - didn't think of that. I'd rather prefer your copy solution than not having consistency on all pages. Edit: Problem solved, proposal updated.

> What are your thoughts on making it obvious which address this QR code is related to?

Highlight it? Thousand ways to do so! :D But just highlighting the account number is not enough, 100% agreed.

Another problem I just encountered: My rename solution is probably bullshit. If an address is labeled with an empty string it doesn't work. Edit: Problem solved, proposal updated.

## tficharmers | 2019-09-07T14:31:40+00:00
> Another problem I just encountered: My rename solution is probably bullshit. If an address is labeled with an empty string it doesn't work.

The '#1', '#2', etc, could also activate the 'Set label' overlay. 

## ghost | 2019-09-07T15:16:11+00:00
> The '#1', '#2', etc, could also activate the 'Set label' overlay.

thx for trying to help me out, but no, that's not intuitive.


--> CLOSED because my proposal sucks because it sucks if on some pages clicking on text copies the text while on other pages clicking on text edits the text. 

## tficharmers | 2019-09-07T17:04:09+00:00
Well, your ideas prompted my ideas. Perhaps both our ideas will prompt others?

## ghost | 2019-09-09T09:36:32+00:00
Reopened because updated! (100% recommended now.)

## rating89us | 2019-11-12T09:14:42+00:00
Copy button should have a copy icon ( ![image](https://user-images.githubusercontent.com/45968869/68658079-1449ae00-0535-11ea-829c-5b61631c285f.png) ) in it.


## ghost | 2019-11-12T09:20:25+00:00
> Copy button should have a copy icon ( ![image](https://user-images.githubusercontent.com/45968869/68658079-1449ae00-0535-11ea-829c-5b61631c285f.png) ) in it.

Would you also say that Apple should use a copy icon?
![image](https://user-images.githubusercontent.com/46682965/68658559-f6c91400-0535-11ea-8e59-805d22aa992a.png)
I think they don't do that because the copy/cut/paste icons are not super clear for everybody.

Do you want the copy icon instead of the text or added to the text? If added: Don't you worry that the button gets even bigger? If instead: Don't you worry that the button gets a quadratic shape, which is not really natural for a button?

## rating89us | 2019-11-12T09:26:52+00:00
> Do you want the copy icon instead of the text or added to the text?

Added to the text, like this: Copy ![image](https://user-images.githubusercontent.com/45968869/68658982-c170f600-0536-11ea-9621-92a69842cede.png)
 It won't get much bigger.


## ghost | 2019-11-12T09:50:21+00:00
so would you say Apple should add icons here additionally to the text?
![image](https://user-images.githubusercontent.com/46682965/68660774-1f530d00-053a-11ea-8e7b-3936fef58507.png)
I'm strongly against adding an icon. It adds no value. But we lose space. And it adds visual complexity.

## rating89us | 2019-11-25T23:01:59+00:00
**Some ideas for the position of UI elements in the screen:**
- Since Monero addresses/subaddresses are never stored in the blockchain, they can be reused to receive many transactions from the same sender. Therefore displaying labels are important, so the receiver can remember "subaddress 1 is for Bob", "subaddress 2 is for Charlie", and so on...
- After receiving from many different senders, it is expected for a wallet to have accumulated dozens or hundreds of subaddresses. In a Bitcoin wallet, these used addresses should never be reused and usually are hidden from the user. But since this is Monero, all these used addresses should be visible for the users, so they can reuse them (with the same sender to avoid off-chain linking).
- The `Create new address` button should always be visible, , even when there are hundreds of used addresses in this page.
- The `QR code` should always be visible when an address is selected, even when there are hundreds of used addresses in this page.

**Current design. Example of an user with 17 addresses:**
- Very long addresses list
- `Edit label` button too far away from the label
- `QR code` + `Create new address` button hidden at the bottom
- When an address is selected, user can't see that the QR code was updated at the bottom
- No indication of what address is inside the QR code

![8](https://user-images.githubusercontent.com/45968869/69585106-0db04180-0fdf-11ea-815e-5afd614caa87.gif)

**My suggestion:**
- Scrollable and compact Addresses list
- Maybe add pagination in the future. If users create a single address for every contact they receive Monero from (and not for every transaction), they will not have many receiving addresses and maybe pagination won't be necessary.
- `Edit label` button near the label
- `QR code` fixed at the right side (always visible when an address is selected: user can see it updating when an address is selected)
- `Title above QR code` indicates which address is included in it
- `Create new address` button always visible

![image](https://user-images.githubusercontent.com/45968869/69586542-30dcf000-0fe3-11ea-83a8-47d7d42df442.png)

My suggestion is inspired by Trezor wallet:
![image](https://user-images.githubusercontent.com/45968869/69584215-f07a7380-0fdc-11ea-9d29-13497a7e14bf.png)

## ghost | 2019-11-26T10:07:33+00:00
> * Scrollable and compact Addresses list with pagination

Scrollable is good, pages suck. Who likes to navigate through pages!? That's why nothing has pages anymore. (Google, Facebook...)

> * `Edit label` button near the label

Nice. That's already included in my design.

> * `QR code` fixed at the right side (always visible: user can see it updating when an address is selected)

Please no! This feature is barely used so let's not give it such a prominent place. Instead, let's emphasize the most used element on this page by presenting it adequately (see my initial proposal).

> * `Title above QR code` indicates which address is included in it

Nice.

## rating89us | 2019-11-26T11:00:12+00:00
> This feature is barely used so let's not give it such a prominent place.

Everyone that sends crypto from a mobile to a desktop wallet uses a QR code, even more if the crypto is Monero, which has lengthy addresses.

## ghost | 2019-11-26T11:09:21+00:00
> Everyone that sends crypto from a mobile to a desktop wallet uses a QR code, even more if the crypto is Monero, which has lengthy addresses.

Exactly. **Only** everybody who sends from a mobile wallet to a desktop wallet uses QR code, while most of our users send to/from a desktop wallet to/from an exchange or other service. 


# Action History
- Created by: ghost | 2019-09-07T10:07:02+00:00
