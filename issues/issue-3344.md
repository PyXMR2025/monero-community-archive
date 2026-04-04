---
title: GUI not showing balance - Tried a lot of the solutions and nothing is working
  so far.  Please help?
source_url: https://github.com/monero-project/monero-gui/issues/3344
author: hopi369
assignees: []
labels: []
created_at: '2021-02-25T13:56:55+00:00'
updated_at: '2021-02-25T19:23:34+00:00'
type: issue
status: closed
closed_at: '2021-02-25T19:06:40+00:00'
---

# Original Description
Hey guys,

I hope you are doing good.  I opened a new Monero GUI wallet and transferred funds into it but after 4 days I am still not seeing the balance.  I am hoping this is user error and that I just missed a step from the many things I've tried.

details. 

Linux system
Trezor T
Simple wallet mode
remote node 

I know I put in the correct address,  on exploremonero reads as "done".  I do not recognise the output addresses, but isn't that because of XMR's privacy with sending monero? 

I reset wallet height, but perhaps did that incorrectly? 
Tried renaming old wallet and making new one.  have it labeled like this.... "name" old 

This morning I tried to create a new wallet on a different computer but was not able to restore wallet, so I am guessing block height is an error?

Is anyone up for helping me to sort this out?

Looking forward to hearing from you, really feeling like I screwed something up.







# Discussion History
## selsta | 2021-02-25T13:57:56+00:00
What did you enter as restore height during wallet restore?

## hopi369 | 2021-02-25T13:59:30+00:00
The last time I did it, I entered, 2278708

## selsta | 2021-02-25T14:01:17+00:00
Ok, do you know when you received that transaction? Do you have a transaction id?

> This morning I tried to create a new wallet on a different computer but was not able to restore wallet, so I am guessing block height is an error?

Could you be a bit more precise about the error?

## hopi369 | 2021-02-25T14:04:34+00:00
Yes, it was on February 19th.   

As far as the error, I just don't see my balance.  My wallet height says, 2278708, and on Daemon it is 2304605.  That means it's out of sync, right?

## hopi369 | 2021-02-25T14:15:28+00:00
Ah sorry, just saw you asked for transaction id.  Is that absolutely necessary?  It's on my other system so hard to transfer here.  Let me sort that out if you absolutely need it?

## hopi369 | 2021-02-25T14:18:25+00:00
here it is

https://www.exploremonero.com/transaction/b870789eb1dec5a44d777cc159c6122516eae8db4da4921c7a574c8dd1b48984

## selsta | 2021-02-25T14:19:54+00:00
As a first step I would try to connect to a remote node in case simple mode has issues: https://github.com/monero-project/monero-gui/issues/3140#issuecomment-706440354

Afterwards go through the restore process again.

Did you ever use different accounts in the GUI?

## hopi369 | 2021-02-25T14:21:26+00:00
Ok cool, is it safe to connect to other remote nodes?  I heard they are compromised sometimes.  

## hopi369 | 2021-02-25T14:24:51+00:00
Just read your pinned link from the hash...It says go into setting to change remote note but I don't see that option.  Can I also just click on the network status icon to switch to another public node?

## hopi369 | 2021-02-25T14:25:47+00:00
Ah, and I do have another account but it wasn't connected to this one at all.  

## selsta | 2021-02-25T14:25:53+00:00
You first have to switch to advanced mode. It should work if you follow all steps in the comment.

## selsta | 2021-02-25T14:26:15+00:00
One more question: Do you use a Trezor passphrase?

## hopi369 | 2021-02-25T14:28:08+00:00
Ok cool, I'll start going through the process.

Shit, I thought I did because it always asks me to confirm the transaction, but I don't remember setting one up...thought I was only using a pin.  

## selsta | 2021-02-25T14:29:24+00:00
Pin is fine, Trezor passphrase is an advanced setting that is disabled by default.

## hopi369 | 2021-02-25T14:30:38+00:00
Ah ok great.  After changing to advanced mode, the only option I see that seems like it would work for my setup is create a new wallet from hardware.  Do I select that one?  

## selsta | 2021-02-25T14:32:11+00:00
> Do I select that one?

You can do that. Afterwards please change to a remote node.

## hopi369 | 2021-02-25T14:38:47+00:00
Shit, I read earlier today about how remote nodes can attack the IP address.  I'm super paranoid man.  How do I know which nodes are safe?  

## selsta | 2021-02-25T14:40:13+00:00
The ones in the linked comment are from trusted community members.

## hopi369 | 2021-02-25T14:41:43+00:00
ok cool. 

## hopi369 | 2021-02-25T14:48:37+00:00
Thanks a lot for your help, I just have heard so much with scams even in official groups so I'm feeling uneasy about setting up a remote node.  Do you know of a way I can verify a node to see if it's safe or not? 

## hopi369 | 2021-02-25T14:52:15+00:00
think I found a way to verify.  Sorry about that, just paranoid...gonna add one you suggested now.

## hopi369 | 2021-02-25T14:55:37+00:00
synching...

## hopi369 | 2021-02-25T14:59:59+00:00
While it's synching do you mind if I ask you a different question?  Or are you already too busy?

## selsta | 2021-02-25T17:14:41+00:00
Just ask :)

## selsta | 2021-02-25T19:00:37+00:00
Please go back to your telegram messages and check what you sent him.

If you only sent him "seeds protected by hardware device." then you are fine.

If you sent him your Trezor 14 word seed then you should move out your coins and setup your Trezor from scratch.

## hopi369 | 2021-02-25T19:03:55+00:00
Okay great, I definitely only sent him  "seeds protected by hardware device."  At least as far as I know...the trezor word seed would not be online on the GUI wallet or anywhere else online unless I put it there, right?  Because I only wrote down my phrase on paper and have not put it on any computers manually. 

## hopi369 | 2021-02-25T19:04:36+00:00
I guess my question is that there is no way the GUI wallet embeds the see phrase in the show seed & keys section, right?

## selsta | 2021-02-25T19:04:37+00:00
> the trezor word seed would not be online on the GUI wallet or anywhere else online unless I put it there, right?

correct

## selsta | 2021-02-25T19:06:40+00:00
Closing as this seems resolved. Never share you seed, even if someone contacts you as an admin.

## hopi369 | 2021-02-25T19:08:13+00:00
Ok cool, I definitely did not put it anyway.  Yes, can't believe I shared anything with him...hard lesson learned.  Again, thanks so much again, I appreciate it so much.

# Action History
- Created by: hopi369 | 2021-02-25T13:56:55+00:00
- Closed at: 2021-02-25T19:06:40+00:00
