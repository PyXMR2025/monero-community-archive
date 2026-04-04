---
title: Monero GUI refuses to acknowledge  value Wallet restore height. Please help.
source_url: https://github.com/monero-project/monero-gui/issues/4406
author: LateAtNight25
assignees: []
labels: []
created_at: '2025-01-27T14:40:40+00:00'
updated_at: '2025-01-27T19:24:09+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Monero GUI Version 0.18.3.4 ignores any change I made in "Wallet Restore Height".
The result is that after Daemon is synchronized, the Indicator "Wallet Blocks Remaining" starts always from from Block height 1487123, while at the moment of this message the height is 3334533 blocks. And then I see that status bar lagging at a speed 10x lower then a snail.

So it takes days and the more its aproaching the end, the more it goes slower.
This is for me a big pain. Especially when starting up Monero GUI again. Already took weeks before daemon was synchronized.

Yes, I use a HDD, and no, the lmdb is not in C:\program files\Monero GUI Wallet, lmdb is located at E:\... Why? I don't want the lmdb files eating away C:\ space. That can endanger proper functioning of windows.

C:\ drive is an SSD drive. 
E:\ is an HDD.

# Discussion History
## selsta | 2025-01-27T14:44:04+00:00
How is the HDD connected to your computer?

## LateAtNight25 | 2025-01-27T14:47:26+00:00
The usual way, with motherboard via cables

## LateAtNight25 | 2025-01-27T14:48:21+00:00
The C:\SSD is type connected in a memory bank

## selsta | 2025-01-27T15:08:47+00:00
Is this issue when you create / restore a new wallet? Or when you change an existing restore height? Also do you use a Ledger hardware wallet?

## LateAtNight25 | 2025-01-27T15:18:34+00:00
I had restored the wallet weeks back. The issue is related to this wallet when I try to change the existing restore height. No, I don't use a Ledger hardware wallet altough I have a Trezor one. Wich I am not using at the moment.

## selsta | 2025-01-27T16:42:56+00:00
Please ignore the comment above, I reported it.

@LateAtNight25 do you have the same issues when restoring the wallet with the new restore height instead of changing it in settings?

I currently think it's some performance issue with the daemon, though it's not clear what causes it.

## LateAtNight25 | 2025-01-27T17:28:03+00:00
In hindsight, at the beginning of the restore process I was not aware of
the Restore wallet height possibility. I should have done that first, But
then I did not realize how big the Blockchain already was

Op ma 27 jan. 2025 17:43 schreef selsta ***@***.***>:

> Please ignore the comment above, I reported it.
>
> @LateAtNight25 <https://github.com/LateAtNight25> do you have the same
> issues when restoring the wallet with the new restore height instead of
> changing it in settings?
>
> I currently think it's some performance issue with the daemon, though it's
> not clear what causes it.
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero-gui/issues/4406#issuecomment-2616327116>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/BONT7CAQXJAME3TOEW55O232MZO2NAVCNFSM6AAAAABV6HWBXKVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZDMMJWGMZDOMJRGY>
> .
> You are receiving this because you were mentioned.Message ID:
> ***@***.***>
>


## LateAtNight25 | 2025-01-27T17:35:03+00:00
I am reasoning from within the Monero Gui point of view. So I mean "Wallet
Restore Height" within the tab "Settings" in the GUI. I don't feel
encouraged to work with command lines within Powershell . That's like
walking into the absolute dark without guidance.

Op ma 27 jan. 2025 18:27 schreef Lightseekr ***@***.***>:

> In hindsight, at the beginning of the restore process I was not aware of
> the Restore wallet height possibility. I should have done that first, But
> then I did not realize how big the Blockchain already was
>
> Op ma 27 jan. 2025 17:43 schreef selsta ***@***.***>:
>
>> Please ignore the comment above, I reported it.
>>
>> @LateAtNight25 <https://github.com/LateAtNight25> do you have the same
>> issues when restoring the wallet with the new restore height instead of
>> changing it in settings?
>>
>> I currently think it's some performance issue with the daemon, though
>> it's not clear what causes it.
>>
>> —
>> Reply to this email directly, view it on GitHub
>> <https://github.com/monero-project/monero-gui/issues/4406#issuecomment-2616327116>,
>> or unsubscribe
>> <https://github.com/notifications/unsubscribe-auth/BONT7CAQXJAME3TOEW55O232MZO2NAVCNFSM6AAAAABV6HWBXKVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZDMMJWGMZDOMJRGY>
>> .
>> You are receiving this because you were mentioned.Message ID:
>> ***@***.***>
>>
>


## LateAtNight25 | 2025-01-27T17:39:14+00:00
Typing "help" does for me not matter much. Still bumping into from the one
syntax problem to another.

Op ma 27 jan. 2025 18:34 schreef Lightseekr  ***@***.***>:

> I am reasoning from within the Monero Gui point of view. So I mean "Wallet
> Restore Height" within the tab "Settings" in the GUI. I don't feel
> encouraged to work with command lines within Powershell . That's like
> walking into the absolute dark without guidance.
>
> Op ma 27 jan. 2025 18:27 schreef Lightseekr ***@***.***>:
>
>> In hindsight, at the beginning of the restore process I was not aware of
>> the Restore wallet height possibility. I should have done that first, But
>> then I did not realize how big the Blockchain already was
>>
>> Op ma 27 jan. 2025 17:43 schreef selsta ***@***.***>:
>>
>>> Please ignore the comment above, I reported it.
>>>
>>> @LateAtNight25 <https://github.com/LateAtNight25> do you have the same
>>> issues when restoring the wallet with the new restore height instead of
>>> changing it in settings?
>>>
>>> I currently think it's some performance issue with the daemon, though
>>> it's not clear what causes it.
>>>
>>> —
>>> Reply to this email directly, view it on GitHub
>>> <https://github.com/monero-project/monero-gui/issues/4406#issuecomment-2616327116>,
>>> or unsubscribe
>>> <https://github.com/notifications/unsubscribe-auth/BONT7CAQXJAME3TOEW55O232MZO2NAVCNFSM6AAAAABV6HWBXKVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZDMMJWGMZDOMJRGY>
>>> .
>>> You are receiving this because you were mentioned.Message ID:
>>> ***@***.***>
>>>
>>


## selsta | 2025-01-27T19:24:07+00:00
I meant going to Settings -> Wallet, then press "Close this wallet"... and then "restore wallet ... from mnemonic seed", and then set the restore height you want. Does that work faster or do you have the same issue? If you have the same issue then it's a daemon performance issue.

# Action History
- Created by: LateAtNight25 | 2025-01-27T14:40:40+00:00
