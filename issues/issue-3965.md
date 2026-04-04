---
title: Missing Transaction and Zero Balance by mymonero.com Scam Alert
source_url: https://github.com/monero-project/monero/issues/3965
author: Gyng3r
assignees: []
labels: []
created_at: '2018-06-08T20:27:40+00:00'
updated_at: '2020-08-21T19:02:11+00:00'
type: issue
status: closed
closed_at: '2018-07-09T15:18:59+00:00'
---

# Original Description
Hello community,

I send from Wallet A to Wallet B XMR and i lost all my balance on Wallet B. This was on 15.12.2017 Here a screenshot.

Wallet A: http://fs1.directupload.net/images/180408/8gx4s6wd.png
Wallet B: http://fs1.directupload.net/images/180408/ajy6rnl5.png

Screenshot from Client: http://fs1.directupload.net/images/180429/u25cyy5t.jpg

As you can see, the 0.392 XMR will not be credited to the Wallet B but will be deducted from the entire balance.

The TXID was: feee95adce58c705875401b89bce435e384ad7ca803c491281a5b58642a45e5d

https://xmrchain.net/search?value=feee95adce58c705875401b89bce435e384ad7ca803c491281a5b58642a45e5d

https://xmrchain.net/block/1465210
I was also not hacked or became a victim of a phishing attack.

Many users have the same problem and it was on 15.12.2017

https://www.reddit.com/r/Monero/comments/7k8m1x/xmr_stolen_from_mymonerocom_some_facts/

I synced the wallet with the GUI but it displayed the same as in the webwallet. Whether node or blockchain synchronization it does not bring success. blockchain status shows 100%. Clear cache did not help. Just like flush_txpool. The Wallet runs on Win Server 2008 R2. 
**If someone can help, he will be paid as well.**

# Discussion History
## mkrufky | 2018-06-09T14:44:56+00:00
@Gyng3r I noticed a similar problem, with both the Electroneum and Stellite CLI wallets as well.

The destination wallet's payments can be verified in the blockchain explorers using my private view key, but never actually show up in my wallet.

I was able to fix it by restoring the non-working wallet to a new wallet.  (no transfers are necessary)

To do this, first you must have your Electrum seed ready.  (If you don't know your seed, you can get it using the `seed` command in the CLI)

Open the monero wallet CLI using the command line argument `--restore-deterministic-wallet`

The wallet will ask for a name for the newly restored wallet, your seed, and a blockchain height (or date) to restore from.  You can say 0 if you're not sure, but this will take some more time.

After you're done, the new wallet will refresh, and you'll likely find your missing transactions as well.

I normally wouldn't ask for payment for this kind of help, but if you're really offering, and only if it has actually helped you, then sure ... feel free to tip me: 
```
88GjfNKvYgVPJQwdyRddQ6MGD4yV8qH4wbBzgSzTTM4QHLsPi1KooVdE7JqzYFPxkq4SmdEdYm1EzjJkDdgZdyWYHpN9MuS
```

However, this is probably a bug in the monero wallet CLI, and I have not touched any of that code.  If somebody actually fixes this bug (and the fix gets propogated to other affected wallets, such as Stellite and Electroneum) then whomever actually fixes the bug would truly deserve your tip.  But really, that's up to you.  :-)

I'm sure that everyone will be interested to hear if this helps you.

EDIT:  after typing all of this, I re-read your original question, and I'm not sure this is the same problem.  But, it doesn't hurt to try.

## moneromooo-monero | 2018-06-13T08:56:26+00:00
Do you have the tx key from the tx you made to B ? If so, you can run check_tx_key in monero-wallet-cli to see if the destination was really wallet B. If not, it looks like a mymonero problem.

## Gyng3r | 2018-06-15T19:21:04+00:00
@mkrufky that does not help
@moneromooo-monero When i check the transaction to Wallet B on https://xmr.llcoins.net/checktx.html this result: This address doesn't own output 0 with pubkey: ea511022dff573b2af9a8ecbd23029d3b3ab71fc318d3d9a0fbda04006d2f439 for amount: Confidential
This address doesn't own output 1 with pubkey: 4437a47efb332744f858e823b3a5ac146472273bf9b44281e5a29bd7eea51239 for amount: Confidential

Total received: 0

I still have to check it with the client. I have specified the correct receiving address of Wallet B and the transaction also appears in the XMR Blockchain.

## moneromooo-monero | 2018-06-15T19:25:04+00:00
You made that tx with mymonero, right ? Not monero-wallet-{gui,cli} ?

The tx was sent to another address. It could be a mymonero bug, or some malware, or SSL MITM. Maybe other reasons.


## Gyng3r | 2018-06-15T19:28:08+00:00
@moneromooo-monero  Yes I have used to send mymonero.com. As usual, something went wrong. I heard that somebody changed the web certificate of mymonero on that day. I do not understand why the entire credit at Wallet B is gone. Although I only entered Wallet B's address on Wallet A and did not log in to Wallet B on the day in mymonero. On another Webwallet I have is also the balance available without error. So it has to be the transaction. And how is anyone to withdraw Wallet B's entire balance without having the Private Keys? You can see on the screenshots that the balance of Wallet A has not arrived.

## Gyng3r | 2018-07-07T14:17:49+00:00
I also can not recover the TX Key. To check if it was sent something mymonero are the biggest scammers. And since 2 months I hear nothing more from the mymonero.com support. Stay alert.

## moneromooo-monero | 2018-07-07T22:54:54+00:00
So this is totally unrelated to the monero software AFAICT. Either a mymonero issue, user error, or malware, right ?

## Gyng3r | 2018-07-08T22:01:30+00:00
No it has nothing to do with the software so i hope so. The owner of mymonero.com has changed the web certificate on 15.12.17 and so the error has arisen. And all payments in the period are flawed. As the owner of the site he should have taken the page offline and should not change anything during operation. You do not build on your PC during operation. The monero support does not answer, should I show the site owner to the police? No one has refunded the amount for 7 months.

## fluffypony | 2018-07-09T15:18:59+00:00
@Gyng3r We've had several attempts at prefix hijacking (ie. BGP hijacking) of our servers. In that event you could end up accessing a phishing site, but you would get lots of SSL errors and would have to ignore them and visit the site anyway. Newer browsers won't even let you do this without overriding a default security setting. These are outside of our control, and we can't "take the page offline" because the upstream tier one ISPs normally kill the bad routes by the time we're notified of the attempt.

Also, MyMonero support answers just fine.

Lastly, this is not a Monero problem, so this issue is being closed.

## Gyng3r | 2018-07-17T21:18:07+00:00
The browser was fresh and the url was correct. The monero reception address was also the right one. Look on the screens. The amount did not arrive in wallet B. Do you get the bug fixed? If so, how long will that take?

## ann61wang | 2020-03-02T18:41:18+00:00
Have you solved your problem? I have the same problem as you. Our query results are similar

## Gyng3r | 2020-08-21T19:02:11+00:00
> Have you solved your problem? I have the same problem as you. Our query results are similar

Hi, the problem is therefore. I created two wallets again and nothing arrived on the other wallet. This is just a joke and the support is ridiculous.



# Action History
- Created by: Gyng3r | 2018-06-08T20:27:40+00:00
- Closed at: 2018-07-09T15:18:59+00:00
