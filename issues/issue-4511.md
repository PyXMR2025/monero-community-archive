---
title: Two outputs with one stealth address
source_url: https://github.com/monero-project/monero-gui/issues/4511
author: goblinxak-cmyk
assignees: []
labels: []
created_at: '2025-10-16T06:42:13+00:00'
updated_at: '2025-10-23T09:14:28+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Help plz

I transferred a coin to a wallet, and after making sure it was sent, I transferred another coin to the same wallet, but it didn't reach its destination.

Tx Hash: c4dd27883364f8605508d3fd6347389415af246bd06b084432f3c0c7bd6594a7
Two outputs with one stealth address
all standard methods did not help
Blockchain Explorer Link:

https://xmrchain.net/myoutputs/c4dd27883364f8605508d3fd6347389415af246bd06b084432f3c0c7bd6594a7/46d3ApCxcsWR8epZLKdLGvUCmq5kPzzhqKfC3pmKhHBnZ6RgBQRfuwcappZB7uZzKmNqbxM5R5HSZaDLX6w9Amz9GexvDDe/036e6c8a555d0e4478a9efd6d47b6ae37e651cf87263f0c0eddd83163b0dc707

https://blockchair.com/monero/transaction/prove?txprove=0&address=46d3ApCxcsWR8epZLKdLGvUCmq5kPzzhqKfC3pmKhHBnZ6RgBQRfuwcappZB7uZzKmNqbxM5R5HSZaDLX6w9Amz9GexvDDe&viewkey=036e6c8a555d0e4478a9efd6d47b6ae37e651cf87263f0c0eddd83163b0dc707&txhash=c4dd27883364f8605508d3fd6347389415af246bd06b084432f3c0c7bd6594a7

# Discussion History
## selsta | 2025-10-16T13:29:48+00:00
Did you try a full restore of the wallet from scratch?

## goblinxak-cmyk | 2025-10-16T13:32:59+00:00
Yes

## selsta | 2025-10-16T13:35:11+00:00
And it shows the exact same issue, one incoming transaction shows up and the second does not?

## goblinxak-cmyk | 2025-10-16T13:36:24+00:00
Yes

## selsta | 2025-10-16T13:40:31+00:00
Did you use a different subaddress or subaccount for the second transaction?

## goblinxak-cmyk | 2025-10-16T13:43:56+00:00
I initially created several sub-addresses. I transferred 1 amount, when it arrived, I transferred the rest of the amount to the same address and it did not arrive. In the sender's mymonero wallet there is one transaction for the second amount, in the recipient's monero gui wallet there is also one transaction for the first amount. Both transactions have the same Hash


## selsta | 2025-10-16T14:34:58+00:00
Is the origin of both the transactions the same? If yes, can you say what it was? Your own wallet, third party servcie? Also can you share both transaction IDs?

## goblinxak-cmyk | 2025-10-17T06:50:40+00:00
I didn't understand your questions
The identifier in both wallets is the same:
c4dd27883364f8605508d3fd6347389415af246bd06b084432f3c0c7bd6594a7

## goblinxak-cmyk | 2025-10-17T07:10:22+00:00
https://dropmefiles.com/u1xiV

## plowsof | 2025-10-17T11:07:29+00:00
the 2 screenshots from the above file link: 
<img width="1414" height="589" alt="Image" src="https://github.com/user-attachments/assets/3f470e9f-573a-4566-bfdc-b1f5fe697b66" />
<img width="590" height="1278" alt="Image" src="https://github.com/user-attachments/assets/159d770e-611d-4244-bd1b-e56c04f563cf" />

## plowsof | 2025-10-20T13:27:07+00:00
seems like the outputs are involved in the same transaction: one of the wallets is view only or not fully synced and detects change as an input. if you control both wallets , sync both from 0 to see what actually happened. 

## goblinxak-cmyk | 2025-10-21T10:08:17+00:00
Это два полностью моих кошелька. Я не понимаю что мне нужно сделать((

## goblinxak-cmyk | 2025-10-22T11:33:20+00:00
I'll try to describe the process again, I just use a translator - perhaps because of it there is a problem with understanding.
I am the owner of both wallets.
I transferred the amount of 0.0001 XMR from mymonero wallet to monero gui wallet - the amount arrived.
I transferred the rest of the amount to the same monero gui wallet from mymonero wallet - the amount did not arrive.
In both wallets there is one transaction, transaction c4dd27883364f8605508d3fd6347389415af246bd06b084432f3c0c7bd6594a7 in monero gui for 0.0001 XMR which was the first and came, in the mymonero wallet there is also one transaction, it also has ID c4dd27883364f8605508d3fd6347389415af246bd06b084432f3c0c7bd6594a7, in the amount of minus 0.5 XMR, which did not arrive in the monero gui wallet.


## plowsof | 2025-10-22T13:33:59+00:00
"mymonero wallet to monero gui wallet -" the problem is with mymonero wallet, it did not sync its wallet correctly. mymonero requires that you upload key images so it knows which outputs are spent. its likely that it attempted to spend an already spent output (~~change~~) returning from that same transaction id. this is a mymonero wallet bug. https://mymonero.com/ ~~suggests you restore your mymonero wallet in another, and sync from 0 so you can see what actually happened.~~ suggests to send all balance to a new wallet* but as your mymonero wallet has fell out of sync so it will need to be restored else where. you can convert your mymonero 13 word wallet to a 25 word one by downloading and using offline this page https://xmr.llcoins.net/

## goblinxak-cmyk | 2025-10-22T13:41:53+00:00
In which wallet can I restore mymonero? I haven't found a wallet that uses a 13 word phrase, not even Cake Wallet, which mymonero advises, doesn't have a 13 word phrase input.

## plowsof | 2025-10-22T13:44:44+00:00
sorry for double ping. the website "llcoins" i link above can do this, you can download and use the page offline for security reasons if you wish.

## nahuhh | 2025-10-22T13:48:04+00:00
as far as i can tell, there was only 1 transaction sent from the wallet with this address 46d3ApCxcsWR8epZLKdLGvUCmq5kPzzhqKfC3pmKhHBnZ6RgBQRfuwcappZB7uZzKmNqbxM5R5HSZaDLX6w9Amz9GexvDDe

## goblinxak-cmyk | 2025-10-23T09:14:28+00:00
but in fact there were two

# Action History
- Created by: goblinxak-cmyk | 2025-10-16T06:42:13+00:00
