---
title: View only wallet shows incorrect balance
source_url: https://github.com/monero-project/monero/issues/7365
author: voidzero
assignees: []
labels: []
created_at: '2021-02-09T09:49:11+00:00'
updated_at: '2021-02-10T11:07:26+00:00'
type: issue
status: closed
closed_at: '2021-02-10T11:07:26+00:00'
---

# Original Description
In the Windows GUI I created a view only wallet, and it shows an incorrect balance... like I only received, but never spent anything. So the balance is higher than it's supposed to be.

I have also tried to create the wallet in the monerujo android wallet using my address and viewkey secret, and the same incorrect balance is shown. Using the most recent version of Monero. The full wallet has two accounts, maybe that has something to do with it? I don't know.

# Discussion History
## moneromooo-monero | 2021-02-09T22:28:12+00:00
Are you sure you correctly imported key images ?

## voidzero | 2021-02-10T05:40:16+00:00
Yeah, well in the gui there's only a button so that's why I used that one to verify. In monerujo I added my public address and my private view key. I added the correct block number - one below my first transaction (incoming). All incoming transactions show properly but the outgoing just do not show up. I'll try it again from the Linux cli later today, but this does already appear to be a bug at least from the GUI and monerujo.

## voidzero | 2021-02-10T10:42:13+00:00
Ok, used the monero-wallet-cli utility to create a view only wallet as described in <https://www.getmonero.org/resources/user-guides/view_only.html>. Same issue: only inputs, no outputs. However, I get this text here:

_"Some owned outputs have missing key images - import_key_images needed"_

So I guess the answer to your question is no, I haven't imported key images. How should I go about doing this? The CLI offers the option using a filename, the GUI does not fafaik. Monerujo also doesn't, although I could use the wallet I generate on the cli. This is suboptimal though.


## selsta | 2021-02-10T10:46:23+00:00
You have to import your key images.

Please see https://monero.stackexchange.com/questions/7217/view-only-wallets-only-shows-incoming-transactions-only-how-to-see-outgoing-asw

## voidzero | 2021-02-10T10:47:35+00:00
Oh! There you go. Thank you, @selsta. Maybe who manages the getmonero.org website could make a note of this on that page I posted.

## voidzero | 2021-02-10T10:50:06+00:00
I also need to learn how to read. Because it does say:

_If your wallet has outgoing transactions, the balance displayed will not be correct. To get a correct balance in a view-only wallet, you have to import the accompanying key images of each output of the wallet._

Sorry about that. Still, the *how* could be posted to the page.

## voidzero | 2021-02-10T11:07:26+00:00
Again my apologies for not reading the page thoroughly and the invalid bug. I will go ahead and close this and I apologize for taking up your time.

# Action History
- Created by: voidzero | 2021-02-09T09:49:11+00:00
- Closed at: 2021-02-10T11:07:26+00:00
