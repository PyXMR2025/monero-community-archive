---
title: Daemon Log shows different block height than GUI
source_url: https://github.com/monero-project/monero-gui/issues/554
author: dternyak
assignees: []
labels: []
created_at: '2017-03-12T00:57:25+00:00'
updated_at: '2017-03-12T20:46:00+00:00'
type: issue
status: closed
closed_at: '2017-03-12T20:13:56+00:00'
---

# Original Description
<img width="298" alt="screen shot 2017-03-11 at 6 56 23 pm" src="https://cloud.githubusercontent.com/assets/7861465/23828107/84d66956-068c-11e7-9908-6ee4a831d4d3.png">

Using 897bc58


# Discussion History
## dternyak | 2017-03-12T04:20:36+00:00
A complete reboot did end up fixing this. 

## Jaqueeee | 2017-03-12T13:10:23+00:00
the target height used to count the remaining blocks is cached for 30 seconds. Did you wait longer than that?

## dternyak | 2017-03-12T20:13:54+00:00
Yes, much longer than 30 seconds. The GUI was behaving strangely at the time, this coincided with the transaction error issue I posted. 

A reboot fixed this as well, so I'm inclined to believe it was some temporary funkyness on both sides. Going to close, but at least now you're aware there might be something going on. 

## Jaqueeee | 2017-03-12T20:21:18+00:00
ok. thanks. Will do another smoke test after point release. 

## Jaqueeee | 2017-03-12T20:30:47+00:00
@medusadigital pointed out that there's nothing wrong in that screenshot. Subtracting the numbers in the popup gives 961264 remaining blocks. More or less the same as shown in bottom left.  

## dternyak | 2017-03-12T20:45:59+00:00
Shoot, i was confused and thought it was the total # left still.
On Sun, Mar 12, 2017 at 3:30 PM Jaqueeee <notifications@github.com> wrote:

> @medusadigital <https://github.com/medusadigital> pointed out that
> there's nothing wrong in that screenshot. Subtracting the numbers in the
> popup gives 961264 remaining blocks. More or less the same as shown in
> bottom left.
>
> —
> You are receiving this because you modified the open/close state.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero-core/issues/554#issuecomment-285974010>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AHf02XPFfARiwAJQTI35tBH7jtRYNUAtks5rlFX3gaJpZM4MaZH0>
> .
>


# Action History
- Created by: dternyak | 2017-03-12T00:57:25+00:00
- Closed at: 2017-03-12T20:13:56+00:00
