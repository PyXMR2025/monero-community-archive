---
title: 'Transaction couldn''t be created:  internal error: Known ring does not include
  the spent output: 3736861'
source_url: https://github.com/monero-project/monero-gui/issues/1293
author: krtschmr
assignees: []
labels:
- bug
- resolved
created_at: '2018-04-08T03:45:53+00:00'
updated_at: '2018-07-04T10:18:29+00:00'
type: issue
status: closed
closed_at: '2018-07-04T10:18:29+00:00'
---

# Original Description
![image](https://user-images.githubusercontent.com/13366714/38463003-f314e90c-3b19-11e8-89e7-06fb6570aa57.png)


restored old wallet on new V12 GUI and can't send my funds. 0.1 XMR or 50 XMR won't matter. always that error.

# Discussion History
## cdevoss | 2018-04-08T18:57:51+00:00
I have the same issue. Downloaded latest Linux GUI v0.12.0.0 yesterday. Made a new wallet and deposited funds in it. I have it setup as a local node. I get the same error when I try and send funds from my wallet.

## dEBRUYNE-1 | 2018-04-08T20:03:28+00:00
+bug

## xmronadaily | 2018-04-08T21:09:57+00:00
I'm having the same issue as well, restored a wallet that hasn't been used since v 10 or so, and can't send any amount of funds from it, keep getting this same error.

## geumu | 2018-04-09T00:31:57+00:00
I also have the same problem. I do not know how to fix it.

## jamescanningcooke | 2018-04-09T23:34:55+00:00
Has this been fixed?

## xmronadaily | 2018-04-10T13:34:10+00:00
I don't think so, have you tried using only CLI?

## xmronadaily | 2018-04-10T13:45:48+00:00
Temprorary workaround is to use the CLI, it's working for me fine, even though gui isn't... Note that I completely deleted my blockchain and resynced from scratch, restoring the wallet from seed. 

## dEBRUYNE-1 | 2018-04-14T14:31:52+00:00
For visibility purposes, this issue is supposedly fixed by applying moneromooo's instructions:

https://github.com/monero-project/monero/issues/3539#issuecomment-380494664

## dEBRUYNE-1 | 2018-04-20T08:28:09+00:00
A user has posted a trivial fix for this particular issue here:

https://www.reddit.com/r/Monero/comments/89nofd/monero_gui_01200_lithium_luna_megathread_download/dxnhmgt/?context=3

Would someone be able to verify that his fix works? 

## gitmesomehub | 2018-05-01T13:18:41+00:00
@dEBRUYNE-1 That worked for me!

## WireChiefUSMC | 2018-05-05T21:58:45+00:00
I am going to answer some of the posted follow ups first, really appreciate those folks took time to read and respond. I am also adding a fix i came up with that may help others, (I figure if I asked for help, and figured out a solution I should shared, could help others), after I answer a few questions posted.

Questions answered section: Checked the Hash on download (made sure from Monero site), good to go. Running Antivirus, relatively good name brand.

First Wallet i used was 11. I then created new ones on 12, just seemed safe thing to do. However one of my wallets was on 11.

Show Status i did a few dozen times, each time was 100%.

What I did that fixed it for me SECTION below: (combination of prior posted fixes and 2 i came up with). So here is a solution that worked for me that includes some of what has been discussed and a clever thing I did to make it work.

You can close this thread as is fixed for me, or keep it live a few weeks to see if helps others. Here is what i did to fix it. Hope it helps others and bug fix info...Sorry to write TWO posts, the first post did not have a LINK so I though is would just sit that and after I put it in saw the link that I figured needed to be entered in a second post. Just getting the information entered was challenge, sorry for duplication, hope this helps users and developer fixes alike, thanks.

Did the usual painful searches and usual fixes recommended: I initially tried to send Monero GUI wallet to Binance. Got an error unknown recipient, the money never arrived. Did the usual 1) renamed wallet files and resynched, 2) deleted the funky file for Ring errors (C:\ProgramData.shared-ringdb), 3) granted all the users FULL access of directory (C:\ProgramData.shared-ringdb) where the users stopped inheritance from above, removed all prior user permissions as creating FULL permissions for the users of CREATOR + OWNER + SYSTEM ADMINS + USERS where giving them FULL Access did not remove the no access or lesser access so had to remove those entries “after” added the new once in ADVANCED 3) pointed the client from local to remote (node.moneroworld.com, 18089), 4) reset computer few times, 5) always ran the Windows GUI 64-bit in ADMINISTRATIVE mode (right click on the file monero-wallet-gui.exe and run as admin), 6) confirm the DAEMON + WALLET both synchronized (bottom left of GIU, and check the SETTINGS > SHOW STATUS. All of this was good (got details below) but only got me part of the way.

Clever idea 1of2 was: I had a transaction of a little amount less than 10 Monero or so to Binance as a test. That worked. The subsequent failed so I did the above. After all above, I saw a Monero Wallet GUI under HISTORY with “all” the coins as the last entry including the less than 10 I sent as a STORY. So MANUALLY typing amount instead of selecting ALL was the clever thing.

Clever idea 2of2 was: I got a new error saying I did not have enough to include a fee. That made sense. And Made progress. Soooo I recorded that error message, used that amount they showed should have been needed for fee, then did a little math. I took the total amount in upper left of wallet GUI, subtracted the FEE in the error message and MANUALLY TYPED in the amount, that amount less the fee to the amount to send, WORKED. In fact no Monero was left over as the FEE was the correct fee amount.

Below are steps in details to add to the above: Hopefully to help programmers fix this Monero GUI client BUG, yes I dare say BUG, I say again B-U-G. The Amount in HISTORY has to “equal” the amount on the upper left display (after FULL blockchain daemon synch and wallet synch) the HISTORY and both upper left Balance + Unlocked Balance should show same. Given these steps to recover were very complicated, and given I asked for HELP, I am adding what I did that worked for me, so others in same set of circumstances can use as a fix, and hopefully the developers will read this entire novel and hopefully give them the exact issue I had so that they can add some features to next release to fix things with buttons that make fixes automatic and avoid issues to begin with and make easier description than what I have here to cover this error and hopefully others similar.

I hope this gets sorted optimism: I love Monero, and I am a 30 year Information Technology tech, and this kicked my butt, and my fix along with all the others I really had to search for were challenging, frustrating when money being Monero Coin was locked with buggy software. Software getting better all the time, hopefully this helps others. Below are more details in case helps.

OK here are more details than the above (see below if need more details). There is a lot of duplication in notes below. I am tired, I would edit it or delete it but probably something in there is useful to someone, so leaving it.

The Clever thing I did, was, INSTEAD of selected ALL in the amount to send, instead I calculated what the total “should be” in other words the FULL amount minus the prior transaction of small test amount under 10 Monero. This amount did NOT give me double-spend error. In other words selecting ALL chose the WRONG amount reflected in the GUI wallet. Instead MANUALLY TYPING in the amount and figuring out what that should have been made progress.

That was the clever key, MANUALLY typing in the amount to send. In other words a amount lesser than the total amount in History. Note the upper left of Wallet client showed a number accurate that was LESS than the amount in HISTORY.

Ok using the manually typed in amount instead of ALL, because ALL uses the total in History the is not accurate. So typing in manually the amount instead of selecting ALL. Clever. Total pain in the you know what, but clever.

Was getting error: Couldn't send the money: transaction <12345678901234567890123456789012345678901234567890123456789012345> was rejected by daemon with status: Failed. Reason: double spend

Then I did: Wiped my wallet file (the only file without extension was renamed) Deleted the

Then got error: Can't create transaction: not enough money to transfer, available only xyz, transaction amount xyz+more = xyz + abc (fee)

This looked like it “TRIED” to send but the FEE added more then existed, soooo tried to reduce the amount to send by the amount of the fee as follows:

XYZ - ABC (fee) = NEW TOTAL Typed in NEW TOTAL to send (guessing the amount for fee in the error has not changed so removed that fee amount from the total I know the total should be.

Stopped LOCAL NODE in SETTINGS, then STARTED LOCAL NODE in settings.

At the CONFIRM TRANSACTION window I recorded all of that and recommend you do too, (screenshot and double-click to copy then paste to your notes).

Monero GUI Client dialogue box appeared showed successful sent: Monero sent successfully: 1 transaction(s) 12345678901234567890123456789012345678901234567890123456789012345

Note the remainder BALANCE and Unlocked Balance in Monero GUI Client now showed is zero as the math for the fee showed.

Interesting that: “Payment proof” was weird for 30 seconds to about 2 minutes (9 lines instead of usual less than 2 lines): SpendProof 12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345

A few minutes later and both the ADDRESS and Payment Proof both were “changed” and successful. This was WEIRD, but seen it before, takes a few seconds or minutes to update these two fields and these two fields are a source of many errors, so wait 3 minutes or so even 5 before changing anything and let it have tom to complete for 3 to 5 minutes even if it does not look like and you are frustrated because your coin is locked up, wait a little bit 3-5 minutes, then recheck these two fields idf you go to fast you may break a communication on sending and that is a pain to fix.

ADDRESS is correct or no longer unknown: 12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345

PAYMENT PROOF after 2 minutes (felt like 2 hours) this CHANGED and now reflected different and showed a more common shorter number like all the others sent to BINANCE:

OutProofV12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345

Transaction ID: 12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345

Hope that helps. I figure if I asked for help, and figured out a solution I should shared, could help others. Sorry long. But I did not want to take a day and edit the second half and I did not want to delete anything that could help another in similar fix their issue and provide enough meaningful info for users and software folks to use and potentially get in future releases some buttons under a “FIX” section perhaps to automate some of what I did that may apply for they scenario and fix bugs encountered that hope were described well enough. Hope this helps users and developer fixes alike, thanks.

## p0o | 2018-05-07T07:45:06+00:00
All solutions are for Windows users, we also on mac have the same problem. I think the issue should remain open until there is a real fix for this not work-arounds. 

## dEBRUYNE-1 | 2018-05-07T09:55:06+00:00
@p0o - Could you try these steps:

1. Exit the GUI and make sure to stop the daemon as well.

2. Use Finder to browse to `~/.shared-ringdb` | On Mac OS X, you can typically use `CMD + SHIFT + DOT` to unhide directories. In addition, note that `~` is typically short for `home/username`

3. Delete this `.shared-ringdb` folder / directory.

4. Restart the GUI (+ daemon).

5. Try to create another transaction.

Does it work now? 

-------------

For visibility purposes, these steps should work on Linux too. 

## p0o | 2018-05-07T10:33:12+00:00
@dEBRUYNE-1 Yes thank you very much. It worked well 😄  By the way, the folder `.shared-ringdb` is not in `~/.bitmonero/`, it was directly in the home directory `~/.shared-ringdb`

Is there a reason for this folder to be there? Took me long hours today to switch between cli, mymonero and GUI just to make it work. 

## dEBRUYNE-1 | 2018-05-07T20:28:45+00:00
> Yes thank you very much. It worked wel

You're welcome. 

> By the way, the folder .shared-ringdb is not in ~/.bitmonero/, it was directly in the home directory ~/.shared-ringdb

Thanks, edited my post. 

>Is there a reason for this folder to be there? 

Yes. It's purpose is to mitigate privacy issues stemming from forked coins that require users to reuse their keys. 



## WireChiefUSMC | 2018-05-08T12:00:03+00:00
use a manual typed in amount for the monero you wish to send.  Use a smaller amount than total as a test amount.  When you select ALL it chooses at least for me an incorrect total.  Selecting a manual typed in total and a smaller amount as a test may tell you if it works at all, then you can move some money until you get as much out as you can until bug is fixed. it is what worked for me. may be different issue than you have but a test of smaller amount may be worth a test.

## dEBRUYNE-1 | 2018-07-04T08:36:17+00:00
This particular issue is resolved in GUI v0.12.2.0: 

https://www.reddit.com/r/Monero/comments/8vkx2g/gui_v01220_released/

## dEBRUYNE-1 | 2018-07-04T08:36:21+00:00
+resolved

# Action History
- Created by: krtschmr | 2018-04-08T03:45:53+00:00
- Closed at: 2018-07-04T10:18:29+00:00
