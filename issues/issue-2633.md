---
title: Not showing incomming payment to integrated address
source_url: https://github.com/monero-project/monero-gui/issues/2633
author: nexon33
assignees: []
labels: []
created_at: '2019-12-19T11:11:49+00:00'
updated_at: '2020-02-11T23:52:32+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I have received a payment on an integrated address I generated myself, and using monero-wallet-cli I am able to verify that I have received the payment by using the command check_tx_key <txid> <txkey> <address>. 
I am able to verify that I received the monero using this command, It shows that the integrated address has received the monero as well as the subaddress that I used to generate the integrated address. But for some reason it is not showing up in the wallet gui, I have tried rescanning the wallet as well as changing the wallet restore height, and I can verify that it works correctly because I have received payments before on this address and those do show up.

The monero wallet cli uses the same local daemon as the monero gui.

# Discussion History
## selsta | 2019-12-19T11:13:31+00:00
You created an integrated address out of a subaddress?

## nexon33 | 2020-02-09T01:41:46+00:00
> You created an integrated address out of a subaddress?

Didn't notice yet, yes thats exactly what I did

## selsta | 2020-02-09T01:44:36+00:00
That’s not supported. How did you do that?

## nexon33 | 2020-02-09T14:27:44+00:00
A while ago I received an xmr transaction to my wallet, however I had to use an integrated address for this and couldn't find any way to generate one in the wallet itsself.

I will loop through what exactly I did to cause this issue but first I will provide evidence this is a bug.
So to start off, when I go into the wallet-cli it will show an incorrect balance because that xmr transaction is not included, but when I type in the cli "check_tx_key

"
It will show that the xmr is received. It doesn't matter if I put the integrated address or the subaddress used to generate the integrated address, it will always show the received balance.
If I do the same check on xmrchain.net it will also confirm that the transaction has been received.
How did I generate the integrated address?

I used https://dustinlemos.com/integrated-address-demo/ and entered my subaddress, this generated an integrated address which I first checked using https://xmr.llcoins.net/addresstests.html by entering my subaddress and afterwards entering my integrated address and confirming that the standard xmr address of both addresses where equal. This was in fact the case.

Do I still have all the information about this transaction?

Yes I do still have the integrated address, the subaddress I used, the payment id of the integrated address that I generated and the secret view key of the transaction as well as the txid. If you need those to check then please provide me an email or other way to contact you and send the information too.

What have I tried to solve it?

Redownloading the whole blockchain to see if the blockchain wasn't corrupted. I also tried installing the xmr wallet on another pc and see if that would give different results, but sadly it didn't.

Any other important information:

I use a Ledger nano s hardware device to log into the monero wallet.

I have copied this text from my other issue, which I closed now

## UkoeHB | 2020-02-09T20:22:05+00:00
Even if integrated addresses with a subaddress were supported, which I don't believe they are, the website you used https://dustinlemos.com/integrated-address-demo/ does not actually create an integrated address that would work. Notice that the first digit is '4' no matter what kind of address (subaddress or normal) you put in the field. '4' corresponds to a normal address, while '8' corresponds to a subaddress. Transactions are constructed differently based on if the recipient is a normal or subaddress.

In your case, the transaction was send to the subaddress _as if_ it were a normal address. Actually, if that website had produced an integrated address 'properly' then the wallet probably would have thrown an error when you tried to use it as a recipient (since integrated subaddresses are unsupported; the llcoins site has checks to prevent this kind of thing happening). I believe your funds are recoverable, although it may require quite a bit of work.
1. You need the private view and spend keys of your original wallet.
2. You need to manually calculate the private view and spend keys of the subaddress used (hardest part), possibly diving into the code base to access the relevant functions. This means you must know which index the subaddress was (I think it should show when you type `address all` into cli). To get you started, I recommend [Zero to Monero](https://web.getmonero.org/library/Zero-to-Monero-1-0-0.pdf) section 5.3. If you find some other, easier, way to get the subaddress private view and spend keys out of your wallet, please let me know (they should be stored/accessible in the wallet code somewhere, but since users never need to know these as they are generated from the basic view and spend keys, they aren't easy to get to)!
3. You need to create a new wallet with those subaddress private keys. It sounds like `--generate-from-keys` in the cli might work.
4. Once this new wallet is setup, scan for your transaction and it should hopefully(tm) be available to you.

## nexon33 | 2020-02-11T01:15:40+00:00
Okay thanks a lot! This seems doable al be it a lot of work, but thats what
you get when you don't read the docs first I guess lol. Thanks a lot and I
will keep you updated and write an explanation on how I did it as a future
reference for others should they ever stumble across this issue

Op zo 9 feb. 2020 21:22 schreef UkoeHB <notifications@github.com>:

> Even if integrated addresses with a subaddress were supported, which I
> don't believe they are, the website you used
> https://dustinlemos.com/integrated-address-demo/ does not actually create
> an integrated address that would work. Notice that the first digit is '4'
> no matter what kind of address (subaddress or normal) you put in the field.
> '4' corresponds to a normal address, while '8' corresponds to a subaddress.
> Transactions are constructed differently based on if the recipient is a
> normal or subaddress.
>
> In your case, the transaction was send to the subaddress *as if* it were
> a normal address. Actually, if that website had produced an integrated
> address 'properly' then the wallet probably would have thrown an error when
> you tried to use it as a recipient (since integrated subaddresses are
> unsupported; the llcoins site has checks to prevent this kind of thing
> happening). I believe your funds are recoverable, although it may require
> quite a bit of work.
>
>    1. You need the private view and spend keys of your original wallet.
>    2. You need to manually calculate the private view and spend keys of
>    the subaddress used (hardest part), possibly diving into the code base to
>    access the relevant functions. This means you must know which index the
>    subaddress was (I think it should show when you type address all into
>    cli). To get you started, I recommend Zero to Monero
>    <https://web.getmonero.org/library/Zero-to-Monero-1-0-0.pdf> section
>    5.3. If you find some other, easier, way to get the subaddress private view
>    and spend keys out of your wallet, please let me know (they should be
>    stored/accessible in the wallet code somewhere, but since users never need
>    to know these as they are generated from the basic view and spend keys,
>    they aren't easy to get to)!
>    3. You need to create a new wallet with those subaddress private keys.
>    It sounds like --generate-from-keys in the cli might work.
>    4. Once this new wallet is setup, scan for your transaction and it
>    should hopefully(tm) be available to you.
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero-gui/issues/2633?email_source=notifications&email_token=ALK2VEUOAXR2RQKSXBNYPADRCBQW5A5CNFSM4J5DGPLKYY3PNVWWK3TUL52HS4DFVREXG43VMVBW63LNMVXHJKTDN5WW2ZLOORPWSZGOELGW7JA#issuecomment-583888804>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ALK2VEXBKAX5UE4UOYJJSNTRCBQW5ANCNFSM4J5DGPLA>
> .
>


## UkoeHB | 2020-02-11T23:52:32+00:00
You might be able to use this function directly: https://github.com/monero-project/monero/blob/b8ab510f238e5a4b9907ea09ed0f364b34ab1ae5/src/device/device_default.cpp#L198 get_subaddress_secret_key().

# Action History
- Created by: nexon33 | 2019-12-19T11:11:49+00:00
