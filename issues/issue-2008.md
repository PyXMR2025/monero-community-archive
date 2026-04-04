---
title: Recently used destination addresses aren't displayed in History tab
source_url: https://github.com/monero-project/monero-gui/issues/2008
author: rating89us
assignees: []
labels: []
created_at: '2019-03-11T11:52:19+00:00'
updated_at: '2020-11-29T07:59:04+00:00'
type: issue
status: closed
closed_at: '2020-11-29T07:59:04+00:00'
---

# Original Description
My friend sent me his address as a WhatsApp message, therefore I couldn't copy and paste it (I had to type it manually in address field of Send tab).

After 10 minutes, I wanted to send some XMR again to my friend, but I couldn't find his address anywhere on the GUI wallet. Unfortunately the History tab didn't display the destination address of my recent transaction (it displayed "Unkown Recipient"). So I had to type his address all over again.

So my suggestion is to display recently used destination addresses in the History Tab.

# Discussion History
## dEBRUYNE-1 | 2019-03-11T16:01:06+00:00
The recipient address is normally saved under transaction details on the `History` page. Is it not saved for you? 

## rating89us | 2019-03-11T16:32:47+00:00
hmmm I checked it now and it is appearing. But it was not appearing yesterday (transaction was not confirmed yet), it was displaying "Unknown Recipient".

## dEBRUYNE-1 | 2019-03-11T18:15:40+00:00
That's expected as far as I know. Can I close this then? 

## rating89us | 2019-03-11T18:42:58+00:00
The problem is still there. Isn't there a way to display the destination address on the transaction details of an unconfirmed transaction?

## dEBRUYNE-1 | 2019-03-12T10:22:04+00:00
Maybe, but I am not sure whether it is worthwhile to actually implement it if the information is shown properly after the transaction is confirmed (which is typically within a few minutes). It may require a lot of work and we only have limited dev time available. 

## rating89us | 2019-03-13T12:56:08+00:00
Maybe we could just change this "Unknown" text to "Waiting confirmation". So the user will know that the typed address of his last transaction will appear as soon as a confirmation is made.

Alternatively, the address field in Send tab could save the last typed values in a list.

# Action History
- Created by: rating89us | 2019-03-11T11:52:19+00:00
- Closed at: 2020-11-29T07:59:04+00:00
