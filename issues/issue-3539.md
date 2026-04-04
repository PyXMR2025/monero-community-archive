---
title: 'internal error: Known ring does not include the spent output: nnn'
source_url: https://github.com/monero-project/monero/issues/3539
author: m2049r
assignees: []
labels: []
created_at: '2018-04-02T09:51:52+00:00'
updated_at: '2018-08-26T21:03:46+00:00'
type: issue
status: closed
closed_at: '2018-06-18T14:49:11+00:00'
---

# Original Description
On Android, sometimes transfering from v0.11 wallets with v0.12 code results in ```"internal error: Known ring does not include the spent output: nnn"```. Restoring the wallet fixes the problem.

Unfortunately I don't have & cannot get logs.

Reading the code, maybe
https://github.com/monero-project/monero/blob/8361d60aef6e17908658128284899e3a11d808d4/src/wallet/ringdb.cpp#L329-L330
should explicitly check for ```dbr != MDB_SUCCESS```. Or mabye ```THROW_WALLET_EXCEPTION_IF(dbr != MDB_SUCCESS, ...``` is better?

# Discussion History
## moneromooo-monero | 2018-04-02T18:31:18+00:00
It does so just above. AFAIK, you're using modified code, so if you have no logs there's nothing I can do.

## moneromooo-monero | 2018-04-02T18:35:17+00:00
If you can repro it with simplewallet though, please do (and post logs).

## m2049r | 2018-04-02T21:22:37+00:00
@moneromooo-monero modified code is only using heap for ```cn_slow_hash()``` & creating ```address.key.txt``` for new wallets. getting peoples logs is nearly impossible. we are talking about the very first transaction ever with v0.12 code - maybe that rings a bell?

## moneromooo-monero | 2018-04-02T23:08:41+00:00
Did you say you had half disabled the ringdb code ?

## m2049r | 2018-04-03T10:07:17+00:00
nope - didn't touch that.

## m2049r | 2018-04-03T21:02:17+00:00
this may be a side-effect of a buffer overflow. will close it and reopen if/when I have more info & logs.

## arnuschky | 2018-04-09T04:58:32+00:00
Seeing this too during testing. @m2049r any news?

## apertamono | 2018-04-09T06:56:37+00:00
I'm getting this error with unmodified code, and so do others: https://www.reddit.com/r/Monero/comments/8age4z/question_help_needed_using_the_gui_trying_to_send/

## m2049r | 2018-04-09T08:18:37+00:00
this is sortof good news as it's not a monerujo issue - @moneromooo-monero ?

## m2049r | 2018-04-09T08:20:58+00:00
i also just finished building a debug version which spits out the monero debug log. @arnuschky maybe you can try it - posted on mattermost.

## moneromooo-monero | 2018-04-09T09:41:42+00:00
Try with 3550 and 3574.

## jamescanningcooke | 2018-04-09T23:35:39+00:00
Has this been fixed?

## moneromooo-monero | 2018-04-10T08:24:40+00:00
Depends whether it works with 3550 and 3574.

## jamescanningcooke | 2018-04-10T09:26:07+00:00
Can you specify what action a GUI v.012 on Windows 10 Home user will need to make? 

## moneromooo-monero | 2018-04-10T10:19:07+00:00
If you're having that problem, then apply PRs 3550 and 3574 on top of the release-0.12 branch, and run monerod and monero-wallet-gui from that.

## jamescanningcooke | 2018-04-10T13:35:19+00:00
If people are not able to program this is not an option. How long before a new release comes out that will fix this bug? There are people with funds frozen. 

## apertamono | 2018-04-10T13:58:22+00:00
Since I'm busy and I haven't compiled anything before, it'll take a few days before I'm able to apply the patches, so I can't test this yet.

## johnsmith90909 | 2018-04-11T14:53:10+00:00
@moneromooo-monero Could you explain to me how to apply PR 3550 and 3574 like I'm a 5 year old? I have gui v0.12 running on linux. 

## jamescanningcooke | 2018-04-11T15:01:39+00:00
Ditto for Windows 10 :)

## moneromooo-monero | 2018-04-11T15:29:37+00:00
git clone https://github.com/monero-project/monero
cd monero
git checkout release-0.12
git branch fix-3550-3574
git checkout fix-3550-3574
git fetch origin pull/3550/head:3550
git fetch origin pull/3574/head:3574
git cherry-pick 58f66073821450c8b7fef642dfe04a173f06dbaf  2897c269de2d16473d7ad665285c8b712cf08227 cdf9ecfd0fbfb72313565311447fb4195c0788d4


## moneromooo-monero | 2018-04-12T13:16:05+00:00
These are now merged to the release-0.12 branch, which should be way easier to try out.

## jamescanningcooke | 2018-04-14T14:52:29+00:00
Where can I abs other non tech people download the latest release where this bug is fixed. 

## moneromooo-monero | 2018-04-15T11:04:29+00:00
It will be on https://getmonero.org/downloads/

## dEBRUYNE-1 | 2018-04-20T08:29:36+00:00
Crosspost:

>A user has posted a trivial fix for this particular issue here:

>https://www.reddit.com/r/Monero/comments/89nofd/monero_gui_01200_lithium_luna_megathread_download/dxnhmgt/?context=3

>Would someone be able to verify that his fix works? 

## jamescanningcooke | 2018-04-25T10:50:46+00:00
How long before the next update so people can unfreeze funds from this bug "internal error: Known ring does not include the spent output: nnn" using the old GUI. It will be posted here right?  https://getmonero.org/downloads/

## dEBRUYNE-1 | 2018-04-25T11:32:57+00:00
@jamescanningcooke - Did you look at my post? Also, there's currently no specific ETA for v0.12.1.0, but it'll probably be released in 1-2 weeks. 

## apertamono | 2018-04-25T12:33:38+00:00
@jamescanningcooke Did you try deleting the file ".shared-ringdb" in the %PROGRAMDATA% folder, as suggested in the Reddit link above? And as @dEBRUYNE-1 mentioned elsewhere on Reddit, if you have an Android phone, you could also create a wallet in Monerujo using your mnemonic seed. That's what I did, and it worked - apparently @m2049r already applied this patch.

## moneromooo-monero | 2018-04-25T20:38:04+00:00
Deleting that is dumb :/ It'll screw your future cross chain spends (so it's only fine if you're not going to any cross chain spends).

## WireChiefUSMC | 2018-05-05T18:27:48+00:00
The instructions above asked to how to apply PR 3550 and 3574 like I'm a 5 year old.  Apparently I am 1 2 year old.  I have all my Monero coin tied up.  And applying a patch using the below instructions makes no sense.  I am a GUI user that is a Windows 64 bit GUI client, i dont know Linus and do not care to, i dont know red hat.  At Stanford University no one uses Read hat or Linux for real business settings as it is garbage easily hacked, dont need instructions for either.  Need Windows GUI 64 bit could care less about GIT commands, never heard of them in 30 years of IT work, no one else has either, in fact i doubt they have anything to do with Windows GUI client.  The world FYI uses Windows for better or worse at all business settings, instructions "should" include a fix for that Monero GUI wallet for windows.   I am a Information Technology professional for 30 years.  Does anyone have any useful instructions how to get these patches applied to a Monero Gui so this client will no longer suck please.  This is a total joke that a ton of personal Monero coin is held up on such an error that patch intructions are not clear for Windos Gui Wallet client.  I am in a International worl country right now, visiting in-laws in Ukraine.  Is there any possibility this client wont suck and there are useful instructions that are easy to follow for Monero GUI wallet 64 bit so i can get my darn coin the hell out of this totally buggy crappy client that is a joke to have money in?  I really have lost my patience, i would be fired if i had to support such a buggy client and i have tried more than you know to get this darn thing to work.  Any truly clear instructions to fix this bug in English that is for a WINDOWS GUI Client would really be appreciated.  My money is screwed until this bug gets fixed.  Thank for any assistance.

## WireChiefUSMC | 2018-05-05T18:33:41+00:00
removed the funky directory (C:\ProgramData\.shared-ringdb) did not work.
renamed wallet file, reset computer, still did not work.
tried  local client - all caught up - did not work.
Tried remote client - did not work.

Want my money out of this buggy client as all others sell off from the MoneroV air drop, screwed, pissed, client sucks, not happy all money tied up and spend days and hours reading all these posts.  Need instructions for Windows GUI wallet 64 bit for patches.

apply PR 3550 and 3574 like i just learned English, step by step, and yes, oh yes windows GUI CLIENT 64 bit.

These steps were not even on the web site to get client patches, so how again are the steps for Windows client????
git clone https://github.com/monero-project/monero
cd monero
git checkout release-0.12
git branch fix-3550-3574
git checkout fix-3550-3574
git fetch origin pull/3550/head:3550
git fetch origin pull/3574/head:3574
git cherry-pick 58f6607 2897c26 cdf9ecf

all my money is tied up, and consideration for a fix to this bug would go a long way.

## WireChiefUSMC | 2018-05-05T22:02:46+00:00
I am going to answer the posted follow ups first, really appreciate those folks took time to read and respond. I am also adding a fix i came up with that may help others, (I figure if I asked for help, and figured out a solution I should shared, could help others), after I answer a few questions posted.

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

## pazos | 2018-05-05T23:09:16+00:00
@WireChiefUSMC: wow, such clever, many success :dancer: Even without met Linus and without giving a sh*t about GIT.

Jokes aside you need to understand where to [ask for help](https://www.reddit.com/r/Monero/) and where to ask [tech questions](https://monero.stackexchange.com/)  .

 I agree with you, the [gui](https://github.com/monero-project/monero-gui) is not as good as the core distribution. There you'll find a [bug tracker](https://github.com/monero-project/monero-gui/issues). I would prefer a short description of actual behaviour vs expected behaviour rather than emotional rants. I think others would agree.


## WireChiefUSMC | 2018-05-08T12:02:19+00:00
Yep shorter is better, it was late, i am in a different country visiting abroad and trying to fix this on a time schedule.  i would have summarized better but tired and afraid to cut out stuff needed.  Putting in a manual amount and sending test send was a good small test in addition to above steps.

## moneromooo-monero | 2018-05-16T10:39:53+00:00
AFAICT, this is now fixed by catching errors creating the shared db. Anyone still getting this using the current release-0.12 code ?

## moneromooo-monero | 2018-06-10T19:05:23+00:00
If no further claim of it breaking with current code, I'll close as fixed soon.

## moneromooo-monero | 2018-06-18T14:44:24+00:00
+resolved

## jamescanningcooke | 2018-07-12T23:18:58+00:00
Same problem with GUI 12.2.0 as with 12.0.00. 
Tried to send a transaction from GUI wallet, and same error message: Can't create transaction: internal error: Known ring does not include the spent output: xxxxxxx

## kevin14389 | 2018-08-07T12:59:10+00:00
Same problem with GUI 0.12.3.0 -> "Impossible de créer la transaction : internal error: Daemon response did not include the requested real output"

## Molokai | 2018-08-26T20:56:10+00:00
I am also getting this error, and an additional error, on transfers with 0.12.3 wallet-cli and 0.12.1 monerod:


Error: internal error: Daemon response did not include the requested real output
Error: There was an error, which could mean the node may be trying to get you to retry creating a transaction, and zero in on which outputs you own. Or it could be a bona fide error. It may be prudent to disconnect from this node, and not try to send a tranasction immediately. Alternatively, connect to another node so the original node cannot correlate information.

If I use same monerod instance and same wallet - but 0.12.0 wallet-cli, it works fine.

Edit: using monerod 12.3 with the 12.3 wallet-cli also works fine.

# Action History
- Created by: m2049r | 2018-04-02T09:51:52+00:00
- Closed at: 2018-06-18T14:49:11+00:00
