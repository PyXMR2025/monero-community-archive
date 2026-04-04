---
title: Didn't receive monero my balance is 0.
source_url: https://github.com/monero-project/monero/issues/8982
author: GpStop
assignees: []
labels: []
created_at: '2023-09-06T06:06:33+00:00'
updated_at: '2023-10-14T13:18:33+00:00'
type: issue
status: closed
closed_at: '2023-10-14T13:18:33+00:00'
---

# Original Description
Hello is there someone who can help me. i'm new in monero world and i'm not a developer and now i have a problem that i cannot resolve by myself. So my problem is:

Someone send me a monero, but i wasn't sync already. I download and instal monero GUI and connected it to my ledger, but the sync took much time. So they send me monero on my address before i sync. They send me a tx key that i check and the transaction was on.
I check online and i saw that i have to change wallet restore height. I did it i change it to 100001.
I'm in local node all sync but ballance is 0.00000
I use GUI interface and do rescan wallet balance, then scan transaction with the tx key. nothing happened.
I have windows firewall off. But i have also kaspersky antivirus on. Is this the problem? Should i have to uninstal kaspersky and windows firewall? How can i trace my missing transaction? How to fix my 0 balance?
I really don't know what to do. I need help. Is there someone who can help me fix it ?

# Discussion History
## selsta | 2023-09-06T12:42:47+00:00
As a first step go to Settings -> Info and share

- Wallet mode
- Version
- Wallet restore height

## GpStop | 2023-09-07T04:35:57+00:00
> As a first step go to Settings -> Info and share
> 
> * Wallet mode
> * Version
> * Wallet restore height

I've done this already
i set my wallet height to 100003, to be sure, but still 0 balance.

## selsta | 2023-09-07T09:20:47+00:00
Please answer my full question so that I can help you

## GpStop | 2023-09-07T10:57:54+00:00
> Please answer my full question so that I can help you

Advanced mode
0.18.2.2
100001

## selsta | 2023-09-07T10:58:41+00:00
Ok, go to Settings -> Log, type "status" and share the output here.

## GpStop | 2023-09-07T11:35:56+00:00
[9/7/2023 2:33 PM] 2023-09-07 11:33:12.387 I Monero 'Fluorine Fermi' (v0.18.2.2-release) 
Height: 1382070/2968904 (46.6%) on mainnet, not mining, net hash 137.16 MH/s, v5, 12(out)+0(in) connections, uptime 0d 0h 40m 48s

## selsta | 2023-09-07T12:07:13+00:00
If you use a local node you have to wait until it is synced to 100%. Yours is currently at 46.6%. If you don't want to wait you have to manually set a remote node.

## GpStop | 2023-09-07T12:17:44+00:00
i know i just start, that's why it's not 100%

## selsta | 2023-09-07T12:18:24+00:00
Yes, but your correct balance will only show up after your daemon is synced to 100%, otherwise it can't calculate your balance.

## GpStop | 2023-09-07T13:03:50+00:00
I know i did it many times.
100% sync with 0 balance.
They send me monero before sync, so i desided to change wallet restore hight with 100001.
everytime i open the GUI it takes a lot if time to sync.
But balance is 0


## selsta | 2023-09-07T13:07:12+00:00
Restarting the GUI does not delete your blockchain progress.

Did you manually delete the blockchain file?

To give you support you either need a local daemon that is 100% synced or you manually connect to a synced remote node.

## GpStop | 2023-09-08T07:16:57+00:00
it's not 100% sync. It takes more than 10 hours and i don't know why?
I've done this already. Usually when i got log in it takes few minutes, but now i don't know why it sync from 0.
My disc space was full with monero network about 217GB, now when i sync it was erased and start from 110Gb.
I don't understand why this happened.
Everyday it takes few minutes now ... hours.

## selsta | 2023-09-08T10:03:57+00:00
You are syncing your node from scratch, that takes between 12h to a couple days depending on your hardware and over 160GB of disk space.

If you don't have enough space then I would recommend you to either use a pruned node (you can select that during the initial wizard), or a remote node.

Do you know how to connect to a remote node or should I post the steps?

## GpStop | 2023-09-08T11:07:06+00:00
i know how to do it but not gonna do. 
i'm still waiting for now . it's almoust done.
2 more hours may be 

## GpStop | 2023-09-08T11:43:22+00:00
is it going to do load from scratch every time? because new time will have no disc space.
How to stop this .
I did this download this and now again it doesn't seem right.
Do i have to change wallet hight again with something more.
now its 100001 do i have to do it at may be 2100000.


## selsta | 2023-09-08T11:45:16+00:00
> is it going to do load from scratch every time?

No, but you said in your previous comment that your disk space was full so it seems you manually deleted the blockchain at some point?

> Do i have to change wallet hight again with something more.

Depends on if your funds show up.

## GpStop | 2023-09-08T12:13:20+00:00
how to stop that. i mean my disk wasn't full but after this is going to be. and i don't know how i delete the blockchain. How i delete the blockchain and my space is lower now? i have 100GB less than before. if i deleted it somehow , the space should't be less?


## selsta | 2023-09-08T12:15:09+00:00
I don't know what happened but there is no integrated function to delete the blockchain. Either you deleted it yourself or you set a different blockchain location in Settings -> Node.

## GpStop | 2023-09-08T12:19:37+00:00
i'm still waiting. i gues 1 more hour, after that what do u want me to do?

## selsta | 2023-09-08T12:21:35+00:00
The last percentage of the daemon sync takes the longest so it will likely take more than 1 hour.

To me it seems it seems that you have limited disk space so it might make sense to connect to a remote node for now, at least until your funds show up. Running a node with a close to full disk won't be a good experience.

## GpStop | 2023-09-08T22:32:37+00:00
[9/9/2023 1:29 AM] 2023-09-08 22:29:46.914 I Monero 'Fluorine Fermi' (v0.18.2.2-release) 
Height: 2969956/2969956 (100.0%) on mainnet, not mining, net hash 2.16 GH/s, v16, 12(out)+0(in) connections, uptime 0d 18h 37m 14s

## GpStop | 2023-09-08T22:38:17+00:00
that's my second download of the monero system. Now i have only a 80GB free. 
I don't have space for 3 times. my balance is still 0.
what if i download monero network on another pc. do the hashes can i use my wallet. i mean my exact wallet with my exact address. can i use them on another pc like recover or something?
im asking because if there is no space i have to do something or erase my network on this pc and start over again or new pc with same wallet address.


## selsta | 2023-09-08T22:41:01+00:00
Let's first try to find your balance and then check regarding remaining storage.

If you go to Settings -> Info, click on "Change restore height", set it to 1 and then click on ok twice, now it should only sync the wallet from scratch. This will likely take 30 minutes or so but it will not use more storage.

## GpStop | 2023-09-12T12:13:17+00:00
> Let's first try to find your balance and then check regarding remaining storage.
> 
> If you go to Settings -> Info, click on "Change restore height", set it to 1 and then click on ok twice, now it should only sync the wallet from scratch. This will likely take 30 minutes or so but it will not use more storage.

## GpStop | 2023-09-12T12:15:01+00:00
Hello friend i'm back.
Now i'm 100% online 24/7 
I'm waiting for you advice. i'm all yours.
I set my wallet height to 1 as u told me.


## selsta | 2023-09-12T12:15:46+00:00
Did you let it sync after changing it to 1?

## GpStop | 2023-09-12T12:21:21+00:00
all sync


## selsta | 2023-09-12T12:22:18+00:00
And still no funds? ... Do you have the transaction id of a transaction that should be inside your wallet?

## GpStop | 2023-09-12T12:23:02+00:00
no funds. i have tx key


## selsta | 2023-09-12T12:24:34+00:00
Do you have multiple wallets / seed and made sure that you didn't open the wrong one?

## GpStop | 2023-09-12T12:28:07+00:00
Just one hardware wallet. no multiple wallets.


## selsta | 2023-09-12T12:29:25+00:00
Ledger / Trezor? Did you confirm that your wallet address is correct compared to your old wallet?

Also can you make a screenshot of the bottom left part of the GUI where it shows the status?

## GpStop | 2023-09-12T12:31:55+00:00
ledger yes everything.

[9/12/2023 3:30 PM] 2023-09-12 12:30:51.356 I Monero 'Fluorine Fermi' (v0.18.2.2-release) 
Height: 2972561/2972561 (100.0%) on mainnet, not mining, net hash 2.18 GH/s, v16, 12(out)+0(in) connections, uptime 0d 1h 43m 39s

## GpStop | 2023-09-12T12:39:49+00:00
wallet daemon sync network status connected 
account #0 xmr balance 0 thats all

## selsta | 2023-09-12T12:41:15+00:00
Does it show a transaction history on the "Transactions" tab?

## GpStop | 2023-09-12T12:41:49+00:00
no transactions yet

## GpStop | 2023-09-12T12:42:24+00:00
how about these commands in the log
where can i type for tx key to my wallet

## selsta | 2023-09-12T12:51:06+00:00
I don't know what you mean exactly with tx key.

Can you enter your transaction id / hash into https://xmrchain.net and then share the link?

## GpStop | 2023-09-12T12:57:20+00:00
Tx hash: 
Tx public key: 
Payment id (encrypted): 
Transaction  was carried out on the Monero network on 2023-07-05 16:02:37. The transaction has 14312 confirmations

is that helpful i don't want to share the exact id and stuff 


## selsta | 2023-09-12T12:58:51+00:00
Is this supposed to be an incoming or an outgoing transaction?

## GpStop | 2023-09-12T13:00:31+00:00
they send it to me, so the transaction was going but my address was not sync, so i have to find it.
it should be outgoing to me.

## selsta | 2023-09-12T13:01:32+00:00
Try to go to Settings -> Wallet, click on "Scan transaction", and then enter the transaction hash and press ok. What happens?

## GpStop | 2023-09-12T13:04:29+00:00
transfer succesfully searched . and that's it .
still 0


## selsta | 2023-09-12T13:05:57+00:00
Did you change the account number on your physical Ledger? In the settings you can switch between account 0, 1, etc. Make sure you have 0 selected.

## GpStop | 2023-09-12T13:14:04+00:00
on ledger  settings - select wallet - it will reset the application! 0+ 1 2 3 4 5 6 7 8 9  these are the options
the other select network - test network stage network main network+
these are options i don't do anything wrong because it says reset

main adress - major:0 minor:0 

## GpStop | 2023-09-12T13:36:17+00:00
what should i do i mean i don't want to crash something

## selsta | 2023-09-12T13:41:26+00:00
There's something non-obvious going on. Usually a resync from 0 is enough to solve everything.

Did you setup your Ledger from scratch at some point with a new seed? When was the last time you had access to your funds?

## GpStop | 2023-09-12T13:50:28+00:00
monero is new for me . i made a new address and wallet especially for this transaction. so i did it for the first time.
download it from getmonero.org install hashes new hardware wallet averything is brand new and for the first time.
so i did't have any transactions and actions on the monero network.
i've had only bitcoin account but this is different. i had also a kaspersky antivirus. can it block the monero network or search for transactions?

## GpStop | 2023-09-12T14:24:57+00:00
let end for today. see ya tomorrow 

## selsta | 2023-09-12T15:12:20+00:00
> i made a new address and wallet especially for this transaction

How did you do this?

## GpStop | 2023-09-13T08:33:11+00:00
> > i made a new address and wallet especially for this transaction
> 
> How did you do this?

I didn't have monero at all. so i have to get the monero network. i go to getmonero and follow steps.
download instal hash and make a new wallet advance option and that kind of stuff. i didn't have monero adress before that.


## GpStop | 2023-09-13T08:36:05+00:00
hey friend i want to ask u something. 
in the cli version of monero there is a commands that u can control everything. 
what about if i use these commands into my gui. there is a window with commands that u told me to write status. is it going to work?


## plowsof | 2023-09-13T09:06:46+00:00
Edit* i see you have used scan tx already, ignore. Surely your transaction history is no ponger empty after successfully scanning the tx?

Those commands are sent to your local node aka daemon/monerod. 

## selsta | 2023-09-13T11:53:47+00:00
Can you go to the Accounts page in the GUI and check if you have multiple accounts? Do you still know if the address you sent to the other party started with a 4 or 8?

> what about if i use these commands into my gui. there is a window with commands that u told me to write status. is it going to work?

The "status" message is a command to your daemon. That is unrelated to the CLI wallet.

## GpStop | 2023-09-13T13:19:31+00:00
my address start with 4 

## GpStop | 2023-09-13T13:21:40+00:00
if i use a another pc and there i install cli wallet is it going to work? i mean if i succeed to put my wallet there and if i use commands to tranck and to catch the missiong transaction to my wallet?

## selsta | 2023-09-13T13:23:08+00:00
One thing we can try is that you give me your address (can be a subaddress if you are concerned about privacy) and I send you a small amount of XMR. If that shows up and the other transaction doesn't show up it means it was sent to a different wallet.

You can get a subaddress by clicking on the Receive tab.

## GpStop | 2023-09-13T13:30:35+00:00
we can try this.

## GpStop | 2023-09-13T13:32:58+00:00
subaddress but same wallet right?


## selsta | 2023-09-13T13:33:39+00:00
Yes, subaddress from the same wallet.

## GpStop | 2023-09-13T13:37:55+00:00
87JFnK3764MbaADmExNHc22PZTo7akobR8P143Kex8rwdEj7jRxEFoj4FpJxkWVaDR3UyKWAedgFics6Pt4PKRo83vTC4DE

my subaddress starts with 8
my 0 address start with 4


## selsta | 2023-09-13T13:45:25+00:00
Sent <137b4190f10618c81394a2e39467a40f3741c86f835abf37f64887597d7ef7f8>

## GpStop | 2023-09-13T13:48:56+00:00
Do I have to do something or just wait

## selsta | 2023-09-13T14:12:21+00:00
It should show up by itself, did your balance increase?

## GpStop | 2023-09-13T14:14:16+00:00
no nothing


## selsta | 2023-09-13T14:15:15+00:00
Did you export your private view key on your Ledger when opening your wallet?

## GpStop | 2023-09-13T14:15:44+00:00
yes


## selsta | 2023-09-13T14:16:40+00:00
Did you take the subaddress from the "Receive" or the "Account" page?

## GpStop | 2023-09-13T14:18:24+00:00
u told me receive and i did it .


## selsta | 2023-09-13T14:19:05+00:00
Yes, Receive is correct. I just try to double check everything.

## GpStop | 2023-09-13T14:23:21+00:00
i'm telling u that's very strange. i feel like i download the network and complete everything. i verify evrything and everything looks nice and done. but the transactions didn't come to me it's like something is blocking me.


## GpStop | 2023-09-13T14:26:29+00:00
by the way i just notice that the wallet is doing the sync.
after u tell me u sent, wallet waiting to sync and sync is complete.wallet is syncronised. it does it couple of times.
but still 0


## GpStop | 2023-09-13T14:28:35+00:00
and keep doing that. sync is complete wallet is sync. and then start over again. wallet sync then sync .

## selsta | 2023-09-13T15:20:01+00:00
Is this how it looks like in the bottom left corner?

<img width="289" alt="" src="https://github.com/monero-project/monero/assets/7697454/7b34bf5b-cd92-4d98-8d1a-72e6065fff3f">



## GpStop | 2023-09-13T15:24:36+00:00
yes


## GpStop | 2023-09-13T15:29:17+00:00
0.001000

## selsta | 2023-09-13T15:29:55+00:00
Yes, so that did show up?

## GpStop | 2023-09-13T15:30:35+00:00
just now

## GpStop | 2023-09-13T15:41:57+00:00
show_transfers in 2800000 doesn't work on gui


## selsta | 2023-09-13T15:55:29+00:00
Because it is a CLI commands, not a daemon command. These are two separate programs.

## selsta | 2023-09-13T15:57:07+00:00
Next thing to try:

You go to Settings -> Info, click on "Change", enter 2920000 and then on okay twice.

Now you wait for it to resync and once it is finished tell me how many transactions you see.

If it is still just 1 then the transaction got sent into a different wallet.

## GpStop | 2023-09-13T15:59:07+00:00
yes but this block is after the transaction i need
i think 2800000 will be better

## selsta | 2023-09-13T16:00:08+00:00
https://xmrchain.net/search?value=2920000 is 2023-07-01 07:35:10

You said your transaction is from 2023-07-05 16:02:37 so it should work. 2800000 also works.

## GpStop | 2023-09-13T16:04:38+00:00
only 1 transaction


## GpStop | 2023-09-13T16:08:58+00:00
let's stop for today. i have 2 ideas for u for tomorrow. ok 

## GpStop | 2023-09-15T05:51:41+00:00
So we check the monero network is working.
Now we do something else. the missing transaction is in the monero network. it's hidden encrypted locked or whatever.
I have a key for that transaction, i'm not sure id key or tx key but i have it. so i have to catch this from the monero network.
i saw in the cli that there is a commands to do that, so should be in the gui interface.
in the log that  u tell me to type status, there is also help command. when u type it there is some commands that are tx and id .
so i want u to test these commands type and see what will happen.

## plowsof | 2023-09-15T06:27:59+00:00
@GpStop 

Now then. You have a ledger. So extract the private viewkey (i think featherwallet shows it now, not certain, otherwise follow [this guide](https://shawnhogan.com/2021/07/how-to-get-monero-private-view-key-from-ledger.html)

Great, we have the private viewkey , the txid and the address it was sent to, perfect. Now, go to a blockchain explorer like the p2pool one which even has a tor link. Then enter your txid first. (open source so you can host it yourself if you want) example: https://p2pool.io/explorer/tx/5dbd3a47b1174d0442aed9f4ad87e5704b2b905e35a2e4e288649b422c1aea8b

There is a decode outputs box. So i want you to type your private viewkey + address it was sent  to and see what happens.

## GpStop | 2023-09-15T12:17:35+00:00
 transactions appear to be findable with print_tx

## selsta | 2023-09-15T12:26:39+00:00
Yes, the transaction exists. But it wasn't sent to your wallet, otherwise it would have shown up. You have to think if you ever created a separate wallet? Do you have malware on your computer that changes the address when copying? Did you double check on the "Account" page that you didn't send it to a different account? 

## GpStop | 2023-09-15T12:34:15+00:00
check check and check


## GpStop | 2023-09-15T13:47:34+00:00
The print_tx monerod command finds a transaction by its txid:


  print_tx TXIDHERE

The output will tell you whether that transaction was found, and if it was, whether it is mined or still in the txpool. If it was mined, you'll see when it was mined

how about that?


## GpStop | 2023-09-15T13:47:45+00:00
should i do this?

## selsta | 2023-09-15T13:49:08+00:00
`print_tx` is a monerod command, it will just say yes this transaction exists in the blockchain. It will not say anything about if this transaction is in your wallet.

Who sent you this transaction? Are they an reputable exchange?

## GpStop | 2023-09-15T14:16:26+00:00
was not an exchange, a person send me for the first time to see and check the monero network what is it.

## GpStop | 2023-09-15T14:17:44+00:00
there are other commands that contains tx


## selsta | 2023-09-15T14:23:06+00:00
All commands on monerod are solely network related, they are not related to your wallet. wallet and monerod are separate and isolated programs.

Can you double check and ask this person what address they sent the funds to? Maybe you still have the chatlog?

## GpStop | 2023-09-15T14:26:53+00:00
 what will happen if i type  print_tx (and tx address) 
i don't want to type anything without u say because i don't want to crash something.
i check and recheck the address and wallet and evrything is 100% but it's still not in my wallet.
they send it to me before i sync and that's it.
I know where is it what block what date they send it the tx key my address everything, so i have to catch it somehow.


## GpStop | 2023-09-15T15:15:44+00:00
what JSON HEX is ?

## selsta | 2023-09-15T17:03:04+00:00
The print_tx command can only help you to see if the transaction is on the blockchain, it does not help you to see if it is in your wallet.

I sent some XMR to you and it showed up correctly. The fact that the other don't show up means they didn't send it to your address.

## GpStop | 2023-09-16T04:54:20+00:00
i gues i have to try cli interface.

## GpStop | 2023-09-16T04:57:40+00:00
i can see the number of the exact block, should i have to mine it?


## selsta | 2023-09-16T15:17:20+00:00
The CLI interface won't help here and you don't have to mine the block, the block is already mined. The person who sent you the funds sent it to the wrong address. You don't have to do anything if it's sent to the correct address, like the 0.001 XMR I sent you a couple days ago. It would show up correctly.

## GpStop | 2023-10-04T10:31:03+00:00
Hello selsta. Sorry for not answearing u  i was sick.
I want to ask u something.
I saw a person who has the same problem. He said that he go to remote note and refresh wallet and that helped.
He said he had transaction of monero before his wallet sync. Just like me. should i try this because this is the only thing i didnt do.


## selsta | 2023-10-04T10:54:00+00:00
We already did a full rescan in this comment: https://github.com/monero-project/monero/issues/8982#issuecomment-1717906469

As far as I can see only my transaction showed up. I still assume the person who sent you the money didn't send it to the correct address.

## GpStop | 2023-10-10T04:52:23+00:00
I want to try remote note. Can u help me with that. 
I haven't done it before. Do u know a good remote note that i can join. I don't know how to find any?


## Unkn8wn69 | 2023-10-10T05:02:57+00:00
Xmrguide.org had a couple

## selsta | 2023-10-10T16:34:08+00:00
address: selsta1.featherwallet.net port: 18081
address: selsta2.featherwallet.net port: 18081

## GpStop | 2023-10-12T10:41:08+00:00
Couldn't connect to Daemon: 127.0.0.1:18081
i can't join your stuff selsta

## selsta | 2023-10-12T10:43:47+00:00
My nodes are online and the message you posted is irrelevant for remote nodes. What does it say in the bottom left corner?

## GpStop | 2023-10-12T10:47:37+00:00
remote node

## selsta | 2023-10-12T10:49:25+00:00
<img width="305" alt="remote node" src="https://github.com/monero-project/monero/assets/7697454/2641ae14-c4ff-4a69-9cc0-39d45b2ea2d1">

If it looks like this it means it's connected correctly.

## GpStop | 2023-10-12T10:50:14+00:00
yes

## selsta | 2023-10-12T11:42:23+00:00
I can only repeat again, whoever sent you the transaction didn't send it to the correct address. That's why my test transaction shows up and the other one doesn't. It's not a node related issue.

## GpStop | 2023-10-14T09:48:12+00:00
selsta u told me to do this: 
https://p2pool.io/explorer/tx/5dbd3a47b1174d0442aed9f4ad87e5704b2b905e35a2e4e288649b422c1aea8b

There is a decode outputs box. So i want you to type your private viewkey + address it was sent to and see what happens.

## GpStop | 2023-10-14T09:58:04+00:00
it says that transaction is send to my wallet address. i check it several times.
i have to try cli.
Would u like to guide me step by step, i mean, i don't what to do with it.
I can only download and then...
would u like to help me more?

## selsta | 2023-10-14T10:00:21+00:00
What transaction is this? https://p2pool.io/explorer/tx/5dbd3a47b1174d0442aed9f4ad87e5704b2b905e35a2e4e288649b422c1aea8b

The transaction is from Sep 11, but you opened this issue on Sep 6 so it can't be the missing transaction.

## GpStop | 2023-10-14T10:02:53+00:00
the transaction was send before i sync my gui

## GpStop | 2023-10-14T10:05:21+00:00
this is wrong that i send u i'm sorry.
u send me https://xmrchain.net to check my transaction
and i did many times


## selsta | 2023-10-14T10:05:41+00:00
Sending before syncing the GUI is not an issue. I juat don't know what this transaction id (5dbd..) is. It can't be your missing transaction since it's from days after you even opened this issue.

## GpStop | 2023-10-14T10:10:56+00:00
don't look at this id(5dbd...) i was posting something wrong


## selsta | 2023-10-14T13:18:33+00:00
I feel like this is going in circles. Since the transaction I sent you is showing up after a rescan, but the transaction this other person sent you doesn't show up it's almost certain they didn't send it to the correct address. Using a different wallet, node etc. isn't going to help here. It appears they simply didn't send it to the correct place.

I'll close this issue since the bug tracker isn't the right place for this but if you continue to need support I'd suggest the #monero-support matrix channel: https://www.getmonero.org/community/hangouts/

# Action History
- Created by: GpStop | 2023-09-06T06:06:33+00:00
- Closed at: 2023-10-14T13:18:33+00:00
