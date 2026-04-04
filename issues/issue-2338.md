---
title: all the money spent will be received in watch-only wallet
source_url: https://github.com/monero-project/monero/issues/2338
author: Cherisher
assignees: []
labels:
- bug
created_at: '2017-08-24T03:53:36+00:00'
updated_at: '2017-11-27T05:16:41+00:00'
type: issue
status: closed
closed_at: '2017-11-27T05:16:41+00:00'
---

# Original Description
When I use Watch-only wallet  file in wallet client,  I found all the transactions are received. I try to run command "rescan_bc", but it don't work.
when run "show_transfers",  this cause balance is not correct, all the money spent will be received.
    1722     in      07:07:35 AM          2.300000000 1d4c1ca9a71cc7ea1d3f6a9c4196a6b84119b5734e8ab0de156e76712b40e991 0000000000000000 - 
    1722     in      07:07:35 AM          2.700000000 f8e25164c71e50ebd9090ad127cba4dbcff769e7b63809982b880195bd53a630 0000000000000000 - 
    1722     in      07:07:35 AM          3.300000000 5e431cdea903d6a7160ccd996a2a900a7decfc92c0b204ffd0077f310b80d0e9 0000000000000000 - 
    1726     in      07:15:24 AM          4.200000000 dceed9cbcf4edf0a69c5496fadf143c8cc80eeb850d3d90c2f5b70355b4c5aaf 0000000000000000 - 
    1730     in      07:17:36 AM          4.400000000 b42b078c13b702f236448dd5b9a80a3928aa09bb4ae0e15745463da53bcdafc0 0000000000000000 - 
    1734     in      07:21:55 AM          4.600000000 67c45e6dee56852eae3555fcbfd79097be68b3532c1195c4dc7c181c086b7d29 0000000000000000 - 
    1744     in      07:35:37 AM          2.170373600 b6d83677a9f001655b75f2e3bf547abd89d15006a2ce84e3a59ae13860a77c0f 0000000000000000 - 
    1747     in      07:42:34 AM          0.693375500 5e7ed239c0a5cf1075a8a8ea9dc75bf32296b1359733d930488b7a93ff526e57 0000000000000000 - 


# Discussion History
## moneromooo-monero | 2017-08-24T05:58:04+00:00
It's not clear what you're saying, but I suspect it might be the same as https://github.com/monero-project/monero/issues/2327, can you confirm ? If so, this is how it works.

## Cherisher | 2017-08-24T09:10:00+00:00
Yes, it is the same. but when I import key_images, I can show the realy money, but I can't find the direction of each transaction(everyone is in direction)when I use the command "show_transfers".  I do not know where I went wrong.

this is the result:
import_key_images b
Signed key images imported to height 39384, 4.034000000 spent, 37.430469500 unspent

## moneromooo-monero | 2017-08-24T10:58:46+00:00
Ah, yes I can see it'd need to update that, it appears to be a bug. Thanks.

## Cherisher | 2017-08-24T13:17:35+00:00
If I have the viewkey, then I should have at least permission to see the account's transaction information and account balance. That is, I should have all the permissions of the wallet except change the attributes of wallet.  This is my understanding.
So, how long the bug will be fixed?

## moneromooo-monero | 2017-08-24T15:18:03+00:00
The viewkey will be enough for incoming. The spendkey (key images) for outgoing. I don't know yet when the bug will be fixed.

## dEBRUYNE-1 | 2017-08-25T15:51:57+00:00
+bug

## mps01k | 2017-08-27T17:14:14+00:00
+Bug also observed this on view only wallet.

## Cherisher | 2017-08-29T14:38:12+00:00
I found in the function
bool generate_key_image_helper(const account_keys& ack, const crypto::public_key& tx_public_key, size_t real_output_index, keypair& in_ephemeral, crypto::key_image& ki)
{
.....
crypto::derive_secret_key(recv_derivation, real_output_index, ack.m_spend_secret_key, in_ephemeral.sec);
....
}

In this function, the spendkey is needed, so there is no concept of "read-only wallet" in this theory.

## stoffu | 2017-08-29T16:01:02+00:00
I'm currently working on a patch that addresses this issue.

## moneromooo-monero | 2017-10-03T16:42:30+00:00
Can you check whether that patch above solves your issue ? It's been merged to master now.

## Cherisher | 2017-10-07T15:07:08+00:00
The patch needs key image which was generate by the wallet with spend key. But my issue is I only have view key, and don't have the key image. So I can't scan money from blockchain correctly.

## moneromooo-monero | 2017-10-07T19:13:05+00:00
The view wallet gets the key image this way:

view: export_outputs
cold: import_outputs
cold: export_key_images
view: import_key_images

## moneromooo-monero | 2017-11-25T22:07:35+00:00
Can you double check this works now, with the commands above ? If no reply in a few days, I'll close as resolved otherwise.

## Cherisher | 2017-11-27T03:56:45+00:00
I think you don't understand what I mean. 
That is, I only have wallet address and view key, I don't have spend key, so I create a watch-only wallet by 
 address and view key,  I can't export_outputs andexport_key_images, there is no way to see the balance corrently. All the transactions are received including sending to others.

the Code in simplewallet is:
bool simple_wallet::export_key_images(const std::vector<std::string> &args)
{
  if (args.size() != 1)
  {
    fail_msg_writer() << tr("usage: export_key_images <filename>");
    return true;
  }
  if (m_wallet->watch_only())
  {
    fail_msg_writer() << tr("wallet is watch-only and cannot export key images");
    return true;
  }

## stoffu | 2017-11-27T04:19:05+00:00
A watch-only wallet can't generate key images since it doesn't have the spend secret key. You should do a bit more research on e.g. StackExchange: https://monero.stackexchange.com/questions/tagged/watch-only-wallet

## Cherisher | 2017-11-27T05:16:41+00:00
I can't get my balance (or transactions details ) if I only have address and viewkey.  This is not a so-called watch-only wallet. I understand like this. I will close this issue.
Thanks for your response.


# Action History
- Created by: Cherisher | 2017-08-24T03:53:36+00:00
- Closed at: 2017-11-27T05:16:41+00:00
