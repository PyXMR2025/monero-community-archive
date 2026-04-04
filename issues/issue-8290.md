---
title: 'Unexpected error: Trezor returned failure: code=99, message=Firmware error'
source_url: https://github.com/monero-project/monero/issues/8290
author: michnovka
assignees: []
labels: []
created_at: '2022-04-25T15:41:23+00:00'
updated_at: '2022-10-08T15:01:55+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Trying to send ALL funds from secondary (8xxxx) account with Trezor and I am encoutering this error repeatedly:

```
2022-04-25 15:37:30.485 W (Parent is Wallet(0x7f76bd9ea3c0), parent's thread is QThread(0x561c7d141530), current thread is QThreadPoolThread(0x561c7d1e6620)
2022-04-25 15:37:30.488 E Can't create transaction:  unexpected error: Trezor returned failure: code=99, message=Firmware error
2022-04-25 15:37:30.489 W "Could not convert argument 0 at"
2022-04-25 15:37:30.489 W        "onTransactionCreated@qrc:/main.qml:826"
2022-04-25 15:37:30.489 W "Passing incompatible arguments to C++ functions from JavaScript is dangerous and deprecated."
2022-04-25 15:37:30.489 W "This will throw a JavaScript TypeError in future releases of Qt!"
```

After few tries I sent smaller amount and this went through OK.

using 0.17.3.1 gui version on Kubuntu 20.04. Trezor on latest fw

# Discussion History
## selsta | 2022-04-25T15:42:39+00:00
@ph4r05 was there a Trezor firmware update?

## michnovka | 2022-04-25T15:44:32+00:00
Not for loong time, using 2.4.3

Btw I am sending in smaller batches and it works fine. The original transaction had 27 inputs, I saw hashing input 1/27, 2/27, 3/27 and then it failed. Sometimes it failed after 1, sometimes after 4.

The smaller ones that are going through had max 6 outputs so far

## michnovka | 2022-04-25T15:48:03+00:00
Ok, by trial and error I seem to have identified the cause.

Up to 16 inputs seem to work just fine. 17+ result in the above error.

## ph4r05 | 2022-04-26T17:54:20+00:00
Thanks for the report @michnovka! We are dealing with similar report here: https://github.com/trezor/trezor-firmware/issues/2213

We are currently investigating possible causes.

## ph4r05 | 2022-04-26T18:26:08+00:00
btw @michnovka I forgot to ask, do you use a custom Trezor background image? It can affect memory layout due to possible bug. Thanks for info!

## michnovka | 2022-04-26T18:34:44+00:00
@ph4r05 Yes I do

## michnovka | 2022-04-26T18:35:37+00:00
Custom homescreen + password protected wallet

## ph4r05 | 2022-04-27T05:49:13+00:00
Thanks for info @michnovka! I could not replicate this with a custom background :/ Does the problem persist when you reconnect the Trezor and try to perform the transaction with 17+ UTXOs fresh from start? (Due to a possible memory fragmentation from previous operations).  

## michnovka | 2022-04-27T06:37:05+00:00
yes, i tried that many times

## michnovka | 2022-04-27T06:40:39+00:00
I am using long trezor password, custom logo on trezor, rotated screen. fw 2.4.3. Monero gui 0.17.3.1 on kubuntu 20.04. trying to send between 8xxxx and 8xxxx addresses

## prusnak | 2022-04-27T08:02:18+00:00
@michnovka Try removing custom background. Unplug Trezor, reconnect it and try again, please.

## michnovka | 2022-04-27T16:56:36+00:00
@prusnak I consolidated my UTXOs already. Need to create them again, so will get to this when I get some free time.

## oswinfox | 2022-10-08T10:12:49+00:00
Hello, I have the same issue with a Trezor model T device and using the latest firmware. Is there any future update for this issue? 

## prusnak | 2022-10-08T11:23:38+00:00
> Hello, I have the same issue with a Trezor model T device and using the latest firmware. Is there any future update for this issue? 

Have you tried steps mentioned above in the conversation? (Removing homescreen, trying smaller batches, etc.)

## oswinfox | 2022-10-08T11:38:14+00:00
Hello @prusnak, yes: 

- Removing homescreen: Does not change the issue
- trying smaller batches: This is not a solution because the marchant I am trying to use automated the monero process of creating the address to send to and I do not have the possibilities to send in smaller batches. 
- It is working when I am sending from a standard address to another one
- Last time I could do my transaction was in April 2022




## ph4r05 | 2022-10-08T12:06:38+00:00
@oswinfox are you sending to an integrated address? I am not sure the PR fixing problem with sending to an integrated address (https://github.com/trezor/trezor-firmware/pull/2479) is already released in a new firmware version. However, workaround there is to transfer required amount to a soft wallet, then transfer to the destination.

https://github.com/trezor/trezor-firmware/issues/2213#issuecomment-1243899355

If you have too many inputs, you can consolidate them by sending more UTXOs (N) to yourself, which reduces number of UTXOs from N to 1.

## oswinfox | 2022-10-08T12:54:35+00:00
Hey yes I am sending to an integrated address and yes this is what I do as small fix, I am sending the amount to another non trezor wallet and do my paiement! 



## selsta | 2022-10-08T14:53:40+00:00
@oswinfox This bug will be fixed once Trezor releases a new firmware version. @prusnak do you have any ETA for it?

## prusnak | 2022-10-08T15:01:55+00:00
> @oswinfox This bug will be fixed once Trezor releases a new firmware version. @prusnak do you have any ETA for it?

Yes, middle of November.

# Action History
- Created by: michnovka | 2022-04-25T15:41:23+00:00
