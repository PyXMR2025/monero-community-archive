---
title: 500%+ Speedup Hack for Slow Transaction Creation on Slow Nodes (Time Critical
  Deposits)
source_url: https://github.com/monero-project/monero/issues/5420
author: MoneroChan
assignees: []
labels: []
created_at: '2019-04-11T03:32:23+00:00'
updated_at: '2019-07-04T13:57:45+00:00'
type: issue
status: closed
closed_at: '2019-07-04T13:57:45+00:00'
---

# Original Description
xmrdsc advised me to post this here as it apparently affects both CLI and GUI. 
-
I’ve made a bootstrap hack to speed up initial transaction creation times on an Old PC running a monero node (turned on only to send a transaction).

This hack has been Successfully used to resolve other github issues, e.g;
https://github.com/monero-project/monero-gui/issues/1995#event-2235518223

**Why use this hack:**
Creating a transaction quickly is Critical for deposits to fixed rate exchanges ( LRoS , XMR.TO etc..), as you only have a short timeframe to make a deposit to qualify for that exchange rate once you get the payment information.

https://github.com/monero-project/monero-gui/issues/2045

Speed Comparison (Core2 Duo, 160GB Spinning HDD, Monero V14)
- Normal: Over 50+ seconds to 2 minutes 
- Bootstrap hack: 10 seconds (500%++ Speedup)


**Here's How to perform this Hack on the Monero GUI Wallet (v14) (internet connected):**

- Step 1: Power on your node, Sync the blockchain and start the Monero GUI.

- Step 2: Create a dummy transaction (prepare to send 0.00000001 XMR to Yourself)

- Step 3: Click SEND ONCE (this should NOT send the funds, but will cause the GUI to bootstrap the wallet, and the 'creating transaction' screen should now appear. This is the bootstrap phase.

- Step 4: After a long wait, The Enter Password Screen finally appears. DO NOT ENTER YOUR PASSWORD. Click "CANCEL"/BACK" and you will return to the Send screen

- Step 5: The hack is now complete. Your wallet is now bootstrapped for rapid transaction creation. Your wallet transaction generator is Now in sync with the more recent blocks and can now prepare Transactions much faster from this point (at least for the next 10 minutes or so). Do Not close the GUI / wallet.

- Step 6: Go to your exchange (XMR.TO/ LROS etc) and book/arrange a time sensitive order now.

- Step 7: Go back to your wallet and send the payment from the screen where you left off.

- Step 8: Enter the payment details and click send. Now, the Create transaction screen should only take a few seconds (500%+ Speedup)

- Step 9: Enter your password and click Send again, to actually send the funds.


How to perform this Hack on GUI View only wallet (Cold sign wallet):

- Step 1: Power on your node, Sync the blockchain and start the Monero GUI.

- Step 2: Create a Dummy transaction (prepare to send 0.00000001 XMR to Yourself)

- Step 3: click 'Create TX file.' (advanced options if it doesn't appear) the 'preparing transaction'/'creating transaction' screen now appears. This is the bootstrap phase.

- Step 4: After a long wait, you will be asked to save the transaction file, Just cancel or save the file anywhere and delete it.

- Step 5 to 7 is the same as above.

Haven't tried this with the CLI yet, but i'm guessing it's the same process. 
Maybe someone can test it out?

This has already helped a lot of people, so I hope it helps someone.

Given how significant this is, maybe the Devs can insert a button to perform this bootstrap hack? 
maybe call it  "bootstrap" / "prepare" / "prime" or something similar?

Cheers
MC

# Discussion History
## jtgrassie | 2019-04-12T23:33:28+00:00
I have never needed had the problem you are describing with the CLI. I'd suggest this is a GUI related problem if you are experiencing it repeatedly in the GUI and therefore a) this issue should be raised in the GUI repository and b) it would seem more appropriate to diagnose the problem as opposed to suggesting hack as a solution?

## moneromooo-monero | 2019-04-24T14:34:11+00:00
Are you using 0.14.0.2 ? Earlier ? Later ?

## jtgrassie | 2019-04-24T22:27:52+00:00
@moneromooo-monero me? tested both latest release tag and master.

## moneromooo-monero | 2019-04-24T23:40:09+00:00
No, the reporter. I see Monero V14, which is likely 0.14.0.2, but master show 0.14.1.0.
Anyway, it looks likely to be the get_output_distribution, not sure when that got sped up, but the reported should test with current master to see if that's still happening.

## MoneroChan | 2019-04-25T05:42:34+00:00
Hi @moneromooo-monero
- Maybe you can ask xmrdsc? I'm only posting here since XMRDSC said it affected his CLI, and advised me to post it here instead of the GUI Repository.  I don't use the CLI myself. 

- I emphasize that this Hack only boosts the **Very 1st Transaction** at Node startup (e.g on a slow Non-AES-NI CPU) .
(e.g for those who power on their node briefly to do a transfer and shutdown)

- If your node runs Nonstop and you've made a transaction in the past, that effectively acts as the hack in itself ; for this reason, some users may report not having this issue, because they've done the hack without knowing it. or maybe they use hibernate and the GUI hacked state is saved, etc...

- i haven't dug into the code as the hack works very well for me and only takes 2 seconds to do.
Cheers


## MoneroChan | 2019-04-25T05:59:01+00:00
Maybe set 'get_output_distribution' module to run at startup will fix this? 
i'm stupid, i don't know anything. lol

## sanderfoobar | 2019-04-25T14:19:01+00:00
> Maybe you can ask xmrdsc? I'm only posting here since XMRDSC said it affected his CLI

Don't misquote me, I said I suspect the same issue is present in CLI. You did not test this, so we don't know if this is a CLI or GUI issue :-) Please validate first, else current bug report is invalid.

## kayront | 2019-06-08T09:28:38+00:00
I'm fairly sure this is a problem with monerod itself. On my "slow" node with a SSD cache and 90GB of RAM, it takes well over two minutes for the first transaction to go through. In the mean time the mechanical hard disks can be heard working furiously in the background.

For whatever reason, as OP noticed, canceling the transaction and retrying tends to work.

Otherwise, waiting the 2+minutes the first time and then transacting again also tends to work.

The strange thing I could not wrap my head around is that in my system there are many GBs of cached blockchain data in both RAM and the fast SSD and the cache is still around when this happens.

## moneromooo-monero | 2019-06-15T10:42:23+00:00
Is it fixed in 0.14.1.0 ? :)

## MoneroChan | 2019-07-04T13:57:37+00:00
I'm glad to report a major improvement is noticable in GUI v0.14.1.0
The Time taken to create transaction is now reduced to 18 seconds on the first attempt :)
Job well done! :)

# Action History
- Created by: MoneroChan | 2019-04-11T03:32:23+00:00
- Closed at: 2019-07-04T13:57:45+00:00
