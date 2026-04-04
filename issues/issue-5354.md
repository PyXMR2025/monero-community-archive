---
title: Failed sending transaction using old version of GUI
source_url: https://github.com/monero-project/monero/issues/5354
author: abundantone
assignees: []
labels: []
created_at: '2019-03-26T12:53:40+00:00'
updated_at: '2019-03-28T13:51:22+00:00'
type: issue
status: closed
closed_at: '2019-03-28T12:17:46+00:00'
---

# Original Description
Hi, I tried to send 345 XMR from the GUI to an exchange about 8 hours ago.  Only later did I realize that the GUI was quite outdated (v0.11.1.0).  The balance in the GUI now reads zero but the transaction status shows as 'PENDING' and the exchange shows no deposit.   I also failed to take into consideration the recent hard-fork.  Any suggestions on how I can correct this?  Much appreciated! 

<img width="958" alt="Screen Shot 2019-03-26 at 8 48 39 AM" src="https://user-images.githubusercontent.com/30573590/54998346-4e654000-4fa4-11e9-94df-2d242639bd64.png">




# Discussion History
## moneromooo-monero | 2019-03-26T13:00:38+00:00
Quit the wallet, flush_txpool in monerod, run the wallet again, wait for it to refresh a couple times and realize the tx is gone and not mined.

## abundantone | 2019-03-26T13:12:48+00:00
> Quit the wallet, flush_txpool in monerod, run the wallet again, wait for it to refresh a couple times and realize the tx is gone and not mined.

Thanks for the super quick reply.

Once I do that, I assume that I should update the GUI prior to attempting to send again?

Is there anything that I need to do regarding the recent hard fork?

## moneromooo-monero | 2019-03-26T13:20:31+00:00
Yes, good point, run the latest release when starting again :)
That's the only thing you should need to do.

## dEBRUYNE-1 | 2019-03-26T13:26:37+00:00
You can resolve your issue with these guides:

https://monero.stackexchange.com/questions/7989/i-forgot-to-upgrade-from-cli-or-gui-v0-13-to-cli-or-gui-v0-14-and-as-a-result

https://monero.stackexchange.com/questions/7993/i-forgot-to-upgrade-from-cli-or-gui-v0-13-to-cli-or-gui-v0-14-and-created-pe



## abundantone | 2019-03-26T20:03:48+00:00
Hi,

Thank you so much for the guides.

I just have one question:

Do I need to upgrade to GUI v0.14.0 *first* and then use the following
guide to correct the blockchain?
https://monero.stackexchange.com/questions/7993/i-forgot-to-upgrade-from-cli-or-gui-v0-13-to-cli-or-gui-v0-14-and-created-pe

Or, do I follow that guide and correct the old GUI v0.11.1.0 *first *and
then upgrade to the new GUI v0.14.0?

Thanks so much in advance!

Jeffrey


On Tue, Mar 26, 2019 at 9:26 AM dEBRUYNE-1 <notifications@github.com> wrote:

> You can resolve your issue with these guides:
>
>
> https://monero.stackexchange.com/questions/7989/i-forgot-to-upgrade-from-cli-or-gui-v0-13-to-cli-or-gui-v0-14-and-as-a-result
>
>
> https://monero.stackexchange.com/questions/7993/i-forgot-to-upgrade-from-cli-or-gui-v0-13-to-cli-or-gui-v0-14-and-created-pe
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/5354#issuecomment-476632891>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AdKEFpFJLPIGr5SgTpjJ5RNzvm2KV8vEks5vaiAZgaJpZM4cLXnw>
> .
>


## abundantone | 2019-03-26T20:36:48+00:00
> Quit the wallet, flush_txpool in monerod, run the wallet again, wait for it to refresh a couple times and realize the tx is gone and not mined.

Hi,

Thank you so much for the guides.  

I just have one question:

Do I need to upgrade to GUI v0.14.0 first and then use the following guide to correct the blockchain?  
https://monero.stackexchange.com/questions/7993/i-forgot-to-upgrade-from-cli-or-gui-v0-13-to-cli-or-gui-v0-14-and-created-pe

Or, do I follow that guide to correct the blockchain using my old GUI v0.11.1.0 first and then upgrade to the new GUI v0.14.0?

Thanks so much in advance!

## dEBRUYNE-1 | 2019-03-26T20:44:06+00:00
@abundantone - You first need to follow this guide:

https://monero.stackexchange.com/questions/7989/i-forgot-to-upgrade-from-cli-or-gui-v0-13-to-cli-or-gui-v0-14-and-as-a-result

Which means you have to upgrade to GUI v0.14.0.0. Please read aforementioned guide diligently, as there are some remarks on, for instance, the database conversion. Once GUI v0.14.0.0 is fully synced, you can apply this guide to recover your 'lost' transaction:

https://monero.stackexchange.com/questions/7993/i-forgot-to-upgrade-from-cli-or-gui-v0-13-to-cli-or-gui-v0-14-and-created-pe

## abundantone | 2019-03-26T21:16:51+00:00
Hi,

Sorry for so many questions :-/

I followed the first guide and downloaded GUI v0.14.0.0 and have attempted
to start the daemon several times but I keep getting the same error message:

[image: Screen Shot 2019-03-26 at 5.11.45 PM.png]

So, I click OK and I click on the 'Start daemon' button from the following
screen.

[image: Screen Shot 2019-03-26 at 5.08.59 PM.png]

But after a few minutes, this cycle repeats.

Is this normal?

With great appreciation.

J


On Tue, Mar 26, 2019 at 4:44 PM dEBRUYNE-1 <notifications@github.com> wrote:

> @abundantone <https://github.com/abundantone> - You first need to follow
> this guide:
>
>
> https://monero.stackexchange.com/questions/7989/i-forgot-to-upgrade-from-cli-or-gui-v0-13-to-cli-or-gui-v0-14-and-as-a-result
>
> Which means you have to upgrade to GUI v0.14.0.0. Please read
> aforementioned guide diligently, as there are some remarks on, for
> instance, the database conversion. Once GUI v0.14.0.0 is fully synced, you
> can apply this guide to recover your 'lost' transaction:
>
>
> https://monero.stackexchange.com/questions/7993/i-forgot-to-upgrade-from-cli-or-gui-v0-13-to-cli-or-gui-v0-14-and-created-pe
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/5354#issuecomment-476843211>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AdKEFsSPnSCFaWftOzMqisc4tqI7C8uKks5vaoakgaJpZM4cLXnw>
> .
>


## abundantone | 2019-03-26T22:29:00+00:00
[image: Screen Shot 2019-03-26 at 6.27.41 PM.png]

Jeffrey Lee


On Tue, Mar 26, 2019 at 5:16 PM Jeffrey Lee <jwlee4925@gmail.com> wrote:

> Hi,
>
> Sorry for so many questions :-/
>
> I followed the first guide and downloaded GUI v0.14.0.0 and have attempted
> to start the daemon several times but I keep getting the same error message:
>
> [image: Screen Shot 2019-03-26 at 5.11.45 PM.png]
>
> So, I click OK and I click on the 'Start daemon' button from the following
> screen.
>
> [image: Screen Shot 2019-03-26 at 5.08.59 PM.png]
>
> But after a few minutes, this cycle repeats.
>
> Is this normal?
>
> With great appreciation.
>
> J
>
>
> On Tue, Mar 26, 2019 at 4:44 PM dEBRUYNE-1 <notifications@github.com>
> wrote:
>
>> @abundantone <https://github.com/abundantone> - You first need to follow
>> this guide:
>>
>>
>> https://monero.stackexchange.com/questions/7989/i-forgot-to-upgrade-from-cli-or-gui-v0-13-to-cli-or-gui-v0-14-and-as-a-result
>>
>> Which means you have to upgrade to GUI v0.14.0.0. Please read
>> aforementioned guide diligently, as there are some remarks on, for
>> instance, the database conversion. Once GUI v0.14.0.0 is fully synced, you
>> can apply this guide to recover your 'lost' transaction:
>>
>>
>> https://monero.stackexchange.com/questions/7993/i-forgot-to-upgrade-from-cli-or-gui-v0-13-to-cli-or-gui-v0-14-and-created-pe
>>
>> —
>> You are receiving this because you were mentioned.
>> Reply to this email directly, view it on GitHub
>> <https://github.com/monero-project/monero/issues/5354#issuecomment-476843211>,
>> or mute the thread
>> <https://github.com/notifications/unsubscribe-auth/AdKEFsSPnSCFaWftOzMqisc4tqI7C8uKks5vaoakgaJpZM4cLXnw>
>> .
>>
>


## dEBRUYNE-1 | 2019-03-27T07:24:25+00:00
The release thread of the GUI states:

>This version, if using your own (local) node, requires a database conversion, which may take 5-10 minutes and the GUI will show that it's Disconnected (or unable to connect) from the daemon (monerod). I'd advise to simply let it run and after the database conversion has completed the GUI will connect back to the daemon (monerod).

Given that you have to perform two database conversions, it will take significantly longer. Hence my previous comment of "Please read aforementioned guide diligently, as there are some remarks on, for instance, the database conversion.". 

## abundantone | 2019-03-27T13:01:37+00:00
The updated GUI is now in the process of synchronizing.   The confusing
part is that I kept getting the error message of the the daemon failing to
start and requesting my password again and again.   But it finally seems to
be progressing.

Thanks so much for your continuing support and patience.

Jeffrey Lee


On Wed, Mar 27, 2019 at 3:24 AM dEBRUYNE-1 <notifications@github.com> wrote:

> The release thread of the GUI states:
>
> This version, if using your own (local) node, requires a database
> conversion, which may take 5-10 minutes and the GUI will show that it's
> Disconnected (or unable to connect) from the daemon (monerod). I'd advise
> to simply let it run and after the database conversion has completed the
> GUI will connect back to the daemon (monerod).
>
> Given that you have to perform two database conversions, it will take
> significantly longer. Hence my previous comment of "Please read
> aforementioned guide diligently, as there are some remarks on, for
> instance, the database conversion.".
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/5354#issuecomment-477012922>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AdKEFmbMZhpBSLKyVMiuwxbkCN9g_Msvks5vaxy0gaJpZM4cLXnw>
> .
>


## abundantone | 2019-03-27T23:14:41+00:00
Hi,

The GUI has synchronized however it is stuck ->  the 'Wallet Blocks
Remaining' metric is stuck at 330170.

Do you have any suggestions?

Thanks!

Jeffrey
[image: Screen Shot 2019-03-27 at 6.40.45 PM.png]

On Wed, Mar 27, 2019 at 9:01 AM Jeffrey Lee <jwlee4925@gmail.com> wrote:

> The updated GUI is now in the process of synchronizing.   The confusing
> part is that I kept getting the error message of the the daemon failing to
> start and requesting my password again and again.   But it finally seems to
> be progressing.
>
> Thanks so much for your continuing support and patience.
>
> Jeffrey Lee
>
>
> On Wed, Mar 27, 2019 at 3:24 AM dEBRUYNE-1 <notifications@github.com>
> wrote:
>
>> The release thread of the GUI states:
>>
>> This version, if using your own (local) node, requires a database
>> conversion, which may take 5-10 minutes and the GUI will show that it's
>> Disconnected (or unable to connect) from the daemon (monerod). I'd advise
>> to simply let it run and after the database conversion has completed the
>> GUI will connect back to the daemon (monerod).
>>
>> Given that you have to perform two database conversions, it will take
>> significantly longer. Hence my previous comment of "Please read
>> aforementioned guide diligently, as there are some remarks on, for
>> instance, the database conversion.".
>>
>> —
>> You are receiving this because you were mentioned.
>> Reply to this email directly, view it on GitHub
>> <https://github.com/monero-project/monero/issues/5354#issuecomment-477012922>,
>> or mute the thread
>> <https://github.com/notifications/unsubscribe-auth/AdKEFmbMZhpBSLKyVMiuwxbkCN9g_Msvks5vaxy0gaJpZM4cLXnw>
>> .
>>
>


## abundantone | 2019-03-28T01:09:59+00:00
I just downloaded Daedalus v0.13.1#3.0.1.5130 and I have the same problem.

Jeffrey


On Wed, Mar 27, 2019 at 7:14 PM Jeffrey Lee <jwlee4925@gmail.com> wrote:

> Hi,
>
> The GUI has synchronized however it is stuck ->  the 'Wallet Blocks
> Remaining' metric is stuck at 330170.
>
> Do you have any suggestions?
>
> Thanks!
>
> Jeffrey
> [image: Screen Shot 2019-03-27 at 6.40.45 PM.png]
>
> On Wed, Mar 27, 2019 at 9:01 AM Jeffrey Lee <jwlee4925@gmail.com> wrote:
>
>> The updated GUI is now in the process of synchronizing.   The confusing
>> part is that I kept getting the error message of the the daemon failing to
>> start and requesting my password again and again.   But it finally seems to
>> be progressing.
>>
>> Thanks so much for your continuing support and patience.
>>
>> Jeffrey Lee
>>
>>
>> On Wed, Mar 27, 2019 at 3:24 AM dEBRUYNE-1 <notifications@github.com>
>> wrote:
>>
>>> The release thread of the GUI states:
>>>
>>> This version, if using your own (local) node, requires a database
>>> conversion, which may take 5-10 minutes and the GUI will show that it's
>>> Disconnected (or unable to connect) from the daemon (monerod). I'd advise
>>> to simply let it run and after the database conversion has completed the
>>> GUI will connect back to the daemon (monerod).
>>>
>>> Given that you have to perform two database conversions, it will take
>>> significantly longer. Hence my previous comment of "Please read
>>> aforementioned guide diligently, as there are some remarks on, for
>>> instance, the database conversion.".
>>>
>>> —
>>> You are receiving this because you were mentioned.
>>> Reply to this email directly, view it on GitHub
>>> <https://github.com/monero-project/monero/issues/5354#issuecomment-477012922>,
>>> or mute the thread
>>> <https://github.com/notifications/unsubscribe-auth/AdKEFmbMZhpBSLKyVMiuwxbkCN9g_Msvks5vaxy0gaJpZM4cLXnw>
>>> .
>>>
>>


## abundantone | 2019-03-28T06:58:57+00:00
Oops - sorry, please disregard the last email re Daedalus GUI.

The syncing of the Monero GUI seems to be making progress, albeit very
slowly.

Thanks for all your help.
[image: Screen Shot 2019-03-28 at 2.56.28 AM.png]

.Jeffrey


On Wed, Mar 27, 2019 at 9:09 PM Jeffrey Lee <jwlee4925@gmail.com> wrote:

> I just downloaded Daedalus v0.13.1#3.0.1.5130 and I have the same problem.
>
> Jeffrey
>
>
> On Wed, Mar 27, 2019 at 7:14 PM Jeffrey Lee <jwlee4925@gmail.com> wrote:
>
>> Hi,
>>
>> The GUI has synchronized however it is stuck ->  the 'Wallet Blocks
>> Remaining' metric is stuck at 330170.
>>
>> Do you have any suggestions?
>>
>> Thanks!
>>
>> Jeffrey
>> [image: Screen Shot 2019-03-27 at 6.40.45 PM.png]
>>
>> On Wed, Mar 27, 2019 at 9:01 AM Jeffrey Lee <jwlee4925@gmail.com> wrote:
>>
>>> The updated GUI is now in the process of synchronizing.   The confusing
>>> part is that I kept getting the error message of the the daemon failing to
>>> start and requesting my password again and again.   But it finally seems to
>>> be progressing.
>>>
>>> Thanks so much for your continuing support and patience.
>>>
>>> Jeffrey Lee
>>>
>>>
>>> On Wed, Mar 27, 2019 at 3:24 AM dEBRUYNE-1 <notifications@github.com>
>>> wrote:
>>>
>>>> The release thread of the GUI states:
>>>>
>>>> This version, if using your own (local) node, requires a database
>>>> conversion, which may take 5-10 minutes and the GUI will show that it's
>>>> Disconnected (or unable to connect) from the daemon (monerod). I'd advise
>>>> to simply let it run and after the database conversion has completed the
>>>> GUI will connect back to the daemon (monerod).
>>>>
>>>> Given that you have to perform two database conversions, it will take
>>>> significantly longer. Hence my previous comment of "Please read
>>>> aforementioned guide diligently, as there are some remarks on, for
>>>> instance, the database conversion.".
>>>>
>>>> —
>>>> You are receiving this because you were mentioned.
>>>> Reply to this email directly, view it on GitHub
>>>> <https://github.com/monero-project/monero/issues/5354#issuecomment-477012922>,
>>>> or mute the thread
>>>> <https://github.com/notifications/unsubscribe-auth/AdKEFmbMZhpBSLKyVMiuwxbkCN9g_Msvks5vaxy0gaJpZM4cLXnw>
>>>> .
>>>>
>>>


## dEBRUYNE-1 | 2019-03-28T07:04:20+00:00
If the wallet refresh (i.e. "Wallet blocks remaining") is not progressing anymore, try restarting the GUI. 

## abundantone | 2019-03-28T07:48:37+00:00
Yes, I had to restart the GUI many time but ... Success at last!

[image: Screen Shot 2019-03-28 at 3.47.03 AM.png]




Jeffrey Lee


On Thu, Mar 28, 2019 at 3:40 AM dEBRUYNE-1 <notifications@github.com> wrote:

> If the wallet refresh (i.e. "Wallet blocks remaining") is not progressing
> anymore, try restarting the GUI.
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/5354#issuecomment-477474451>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AdKEFhXMb65JygMtrUHkKRg6zzZ_yEUgks5vbGmqgaJpZM4cLXnw>
> .
>


## dEBRUYNE-1 | 2019-03-28T12:10:19+00:00
Good to hear! Going to mark this as resolved then.

## dEBRUYNE-1 | 2019-03-28T12:10:24+00:00
+resolved

## abundantone | 2019-03-28T13:51:22+00:00
I think I need more help.

I started to follow guide:
https://monero.stackexchange.com/questions/7993/i-forgot-to-upgrade-from-cli-or-gui-v0-13-to-cli-or-gui-v0-14-and-created-pe

I was able to flush the tx pool and the balance restored in the GUI.

I exited the GUI (leaving the Daemon running) and renamed the wallet in the
directory.

When I re-started the GUI, the GUI did not recognize my computer:

[image: Screen Shot 2019-03-28 at 9.15.08 AM.png]
[image: Screen Shot 2019-03-28 at 9.24.45 AM.png]
[image: Screen Shot 2019-03-28 at 9.44.53 AM.png]
[image: Screen Shot 2019-03-28 at 9.30.42 AM.png]


Is this what should have happened?

What mode should I select?  Simple mode or advanced mode?

One other question concerns the location of the old and new versions of the
GUI:

[image: Screen Shot 2019-03-28 at 9.47.51 AM.png]

The new version of the GUI v0.14.0.0 got stored in a folder on my desktop
instead of replacing the old version of the GUI which is stored in
'Applications' folder.  Can I / Should I delete the old version(s) of the
GUI in the 'Applications' folder and move the new GUI into the
'Applications' folder?

Thanks once again!

Jeffrey


On Thu, Mar 28, 2019 at 8:18 AM issue-helper <notifications@github.com>
wrote:

> Closed #5354 <https://github.com/monero-project/monero/issues/5354>.
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/5354#event-2236070557>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AdKEFm9jlequwUssATqNBYDT1EALBtPaks5vbLL4gaJpZM4cLXnw>
> .
>


# Action History
- Created by: abundantone | 2019-03-26T12:53:40+00:00
- Closed at: 2019-03-28T12:17:46+00:00
