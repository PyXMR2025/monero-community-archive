---
title: all funds gone through 3.9 XMR in fee
source_url: https://github.com/monero-project/monero/issues/8447
author: kvnkmth
assignees: []
labels: []
created_at: '2022-07-20T23:29:41+00:00'
updated_at: '2022-08-11T18:04:40+00:00'
type: issue
status: closed
closed_at: '2022-08-11T10:15:37+00:00'
---

# Original Description
Sent a transaction as usual but did realize my funds we all gone through the fee.
transaction hash 2d97b227942d46aead4ae7dd788adc2a2e83b8540f9e6a5f70f13dad67724e9a

# Discussion History
## selsta | 2022-07-20T23:46:37+00:00
Which version are you using?

## kvnkmth | 2022-07-20T23:49:22+00:00
sadly 0.17.1.9 

## selsta | 2022-07-20T23:50:51+00:00
We have added a high fee warning, plus we have scanned all remote nodes multiple times and were not able to find whatever node is behind this. 

![](https://user-images.githubusercontent.com/7697454/165557782-af28867d-a759-43b9-8a31-d2dea0fa157c.png)

If you use v0.17.1.9 that fee warning sadly doesn't exist yet. We hoped that people would upgrade due to the auto updater :/

## selsta | 2022-07-20T23:53:11+00:00
How much XMR are still left in your wallet?

## kvnkmth | 2022-07-20T23:57:30+00:00
nothing actually. its zero

## kvnkmth | 2022-07-20T23:58:12+00:00
> How much XMR are still left in your wallet?



> We have added a high fee warning, plus we have scanned all remote nodes multiple times and were not able to find whatever node is behind this.
> 
> ![](https://user-images.githubusercontent.com/7697454/165557782-af28867d-a759-43b9-8a31-d2dea0fa157c.png)
> 
> If you use v0.17.1.9 that fee warning sadly doesn't exist yet. We hoped that people would upgrade due to the auto updater :/

i wish i upgraded

## selsta | 2022-07-20T23:58:50+00:00
That's.. bizarre. What wallet mode are you using in Settings -> Info?

## kvnkmth | 2022-07-21T00:02:38+00:00
it was in simple mode

## selsta | 2022-07-21T00:03:49+00:00
And that happened a couple weeks ago, right? Can you make a screenshot from the transaction inside the GUI? Do you remember anything that was weird about that transaction? Did it fail at first or something?

## kvnkmth | 2022-07-21T00:09:36+00:00
i remember the transaction took ages to send. and the first confirmation took like 30 mins


## kvnkmth | 2022-07-21T00:18:26+00:00
![fee](https://user-images.githubusercontent.com/6536172/180103783-96ad221c-ad92-41f3-9b06-880a0a2153f0.png)
How do i recover the funds?

## selsta | 2022-07-21T00:21:47+00:00
What does it say in the top left corner: `XMR :.??`

## kvnkmth | 2022-07-21T00:29:00+00:00
thats the balance why bruh

## selsta | 2022-07-21T00:34:28+00:00
Because I have never seen `:.??` as a balance. It's either `?.??` or a number. To figure out what's going on a technical level I need to know your exact remaining balance.

Regarding "recovering" funds, this was 2 weeks ago and whatever mining pool has mined this transaction has already paid out the fee to miners.

## kvnkmth | 2022-07-21T00:37:26+00:00
its zero 0.0000 this is version 0.18 am running

## kvnkmth | 2022-07-21T00:43:47+00:00
but the balance is zero. its just that i cropped the screenshot
its all i had left
which pool mined it?

## selsta | 2022-07-21T02:27:14+00:00
Did you intend to send 0.5 XMR or did you intend to send your whole balance?

## kvnkmth | 2022-07-21T09:16:54+00:00
i sent 0.5 xmr. and it arrived but fee was 3.9 and didnt realize it till yesterday

## Cactii1 | 2022-07-21T19:22:11+00:00
> Because I have never seen `:.??` as a balance. It's either `?.??` or a number.

This isn't answered by "I cropped the screenshot".

## Cactii1 | 2022-07-21T19:24:47+00:00
Let's get the obvious answered first.

Where did you download your wallet from?
Do you still have the archive and can you verify the hash on that archive?
Can you post the hash of the GUI wallet file that you're running?

## Cactii1 | 2022-07-21T19:28:24+00:00
If you sent it 14 days ago you didn't send it with the software you're currently using (v0.18)

## kvnkmth | 2022-07-21T21:13:37+00:00
i sent it with v0.17.1.9 
got it from getmonero.org
sha256sum edc47b1540510640a40e8d52ad4ab3a6220f935e881fd65b02ccce94a28c3fa2

## kvnkmth | 2022-07-21T21:15:01+00:00
> i sent it with v0.17.1.9 got it from getmonero.org sha256sum edc47b1540510640a40e8d52ad4ab3a6220f935e881fd65b02ccce94a28c3fa2

its for monero-gui-install-win-x64-v0.17.1.9.exe

## Cactii1 | 2022-07-21T21:23:37+00:00
Alright, that's the correct hash.

Maybe this makes the case to make it so simple mode remembers where it gets its information from when forming a transaction.

## kvnkmth | 2022-07-22T07:30:08+00:00
how do i recover the funds

## Cactii1 | 2022-07-22T15:05:38+00:00
> how do i recover the funds

Your funds are not recoverable.

## kvnkmth | 2022-07-22T15:14:24+00:00
great

## plowsof | 2022-07-28T19:01:54+00:00
Just to clarify. 
- using a custom gui wallet which shows balance as ":".?? instead of "?":??
- fee of 3.954
- sent 0.5
- total = 0.5 + 3.954 = 4.454
- if your balance before sending this transaction was exactly 4.454 then your wallet balance is now zero

can you confirm?

## Cactii1 | 2022-07-28T19:06:39+00:00
That would be very strange that the fee would be exactly enough to empty the wallet of all funds.

## fugbixer | 2022-08-10T02:52:39+00:00
>That would be very strange that the fee would be exactly enough to empty the wallet of all funds.

> its for monero-gui-install-win-x64-v0.17.1.9.exe

1.could it be a pointer usage which leads malware to get the value
2.blocks all other than the malicious node
3. manipulates the memory of the monero gui  fee when creating the transaction to steal funds ? 

could the node operator somehow obtain the fees?

@selsta 

good counter to show the high fees warning but it is not noob safe enough. 
maybe adding a won't proceed when the xmr fee is above a certain unreasonable amount like 0.1+ 
depending on how serious this issue could be / become



## kvnkmth | 2022-08-10T12:09:42+00:00
> Just to clarify.
> 
> * using a custom gui wallet which shows balance as ":".?? instead of "?":??
> * fee of 3.954
> * sent 0.5
> * total = 0.5 + 3.954 = 4.454
> * if your balance before sending this transaction was exactly 4.454 then your wallet balance is now zero
> 
> can you confirm?

no the fee did not wipe the whole wallet.
it left around 0.5xmr
so the gui wallet is compromised?

## plowsof | 2022-08-10T14:50:16+00:00
"exactly".... "around" .. posting the wrong txid initially, and you're using a modified version of the gui .. please close this issue nothing can be done for you. 

To me this looks like a bad attempt to try and 'get a refund' for something that didn't happen to you OR you really did download a compromised version of the Monero GUI and there is still nothing we can do, and i apologise for the accusation.



## kvnkmth | 2022-08-10T15:35:13+00:00



> "exactly".... "around" .. posting the wrong txid initially, and you're using a modified version of the gui .. please close this issue nothing can be done for you.
> 
> To me this looks like a bad attempt to try and 'get a refund' for something that didn't happen to you OR you really did download a compromised version of the Monero GUI and there is still nothing we can do, and i apologise for the accusation.

Which transaction are you talking about.
My funds are gone through the fee and you just speculate am lying?
you don't even try to check with me properly.
the hashes for gui wallet all checked out
check well this is my transaction `2d97b227942d46aead4ae7dd788adc2a2e83b8540f9e6a5f70f13dad67724e9a`
you are sitting on the edge of an attack may be @fugbixer is right

 

## fugbixer | 2022-08-11T07:24:17+00:00
@kvnkmth please calm down, losing money sucks for everyone. since its crypto you cant get a refund. 
so @plowsof ur the first who brought this up. he was asking if there is a way to recover the funds, we told him no there is not.
end of story. 

@selsta made a solution  which is good, but i think can be improved. 

>good counter to show the high fees warning but it is not noob safe enough.
maybe adding a won't proceed when the xmr fee is above a certain unreasonable amount like 0.1+

so the thread can be closed and we can hope the fix will be in the next wallet release so that this does not happen anymore.
no one is responsible for devices security beside the owner, for the wallet issue we are thankful that it got reported so in case some is trying to manipulate the wallet / or its somehow caused by a bug, it will not happen in the future. 

## kvnkmth | 2022-08-11T10:15:30+00:00
@fugbixer cool i hope no one else will fall for this bug

## selsta | 2022-08-11T15:46:01+00:00
@fugbixer we will likely hardcode a couple community run nodes so that this issue doesn't even happen in the first place.

## fugbixer | 2022-08-11T18:01:58+00:00
please make it fail safe with a fallback mode in case that none of the community nodes can be reached since they could become a primary target of ddos attacks / censorship.  

introducing a trust factor in terms of up time and reliability could create a stable ranking of nodes to choose.  

# Action History
- Created by: kvnkmth | 2022-07-20T23:29:41+00:00
- Closed at: 2022-08-11T10:15:37+00:00
