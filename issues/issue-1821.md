---
title: Smart Mining not properly differentiating between idle and non idle.
source_url: https://github.com/monero-project/monero/issues/1821
author: doobilydo
assignees: []
labels: []
created_at: '2017-02-27T23:24:10+00:00'
updated_at: '2017-12-31T17:32:30+00:00'
type: issue
status: closed
closed_at: '2017-12-31T17:32:30+00:00'
---

# Original Description
Running this command: `start_mining <threads> true true`

The battery check doesn't appear functional (not the point of this issue), which was already mentioned; so I'm keeping that parameter **true**.

I'm running this command from **wallet-cli**, so as to not worry about the wallet address.

**Problem:**
It appears to start normally, detecting that the computer is somewhat/mostly idle (is *idle* just a matter of how much CPU is being used?). It adjusted based on how much CPU I used.

Locking the computer and letting it sit (idle) appears to have not tiggered a mostly idle status. So, returning to the computer resulted in me seeing no mining.

**Update:**
Now, starting it initially, it recognizes a 96% (fluctuating  in the 90s) idle CPU, but remains at 1% mining, hashrate of  0. 

**My specs:**
- Ubuntu 16.04 LTS (64-bit)
- AMD
- monero-v0.10.2.1
- (anything else?)

----------------------
@revler1082

# Discussion History
## vtnerd | 2017-02-28T02:49:27+00:00
This is going to be a duplicate of https://github.com/monero-project/monero/issues/1810 .

Is this running in a VM or container?

## doobilydo | 2017-02-28T02:58:59+00:00
I considered that. I have been mining successfully on each previous version
of monerod and wallet-cli.

It's not a VM. Enlighten me as to what a container is.

On Mon, Feb 27, 2017, 8:49 PM Lee Clagett <notifications@github.com> wrote:

> This is going to be a duplicate of #1810
> <https://github.com/monero-project/monero/issues/1810> .
>
> Is this running in a VM or container?
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/1821#issuecomment-282926008>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AGT7KBUg3VaOftW2z2-p4NM5tD3YIjReks5rg4s5gaJpZM4MNw4x>
> .
>


## moneromooo-monero | 2017-02-28T19:52:12+00:00
A container is a kind of souped up jail, where you can run up to an entirely different userspace with the same kernel. Docker, for example.

## vtnerd | 2017-03-01T01:55:10+00:00
Yes in particular I am concerned that the information in the container under `/proc/stat` is different than the information provided by the VPS console. Although it sounds like you might be running this locally.

## doobilydo | 2017-03-01T01:59:02+00:00
Correct. This is local.

It sounds like #1810 is discovering that the bug is "larger", since it is
affecting normal mining as well.

On Tue, Feb 28, 2017, 7:55 PM Lee Clagett <notifications@github.com> wrote:

> Yes in particular I am concerned that the information in the container
> under /proc/stat is different than the information provided by the VPS
> console. Although it sounds like you might be running this locally.
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/1821#issuecomment-283220861>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AGT7KIKPuQEb2MTKii14cJ8QxXug3SBzks5rhNAAgaJpZM4MNw4x>
> .
>


## vtnerd | 2017-03-01T02:19:43+00:00
But are you have an issuing with "normal" mining, or just "smart" mining?

Edit: Nevermind, the other thread states you had an issue with both.

## doobilydo | 2017-03-01T02:21:50+00:00
Both, since 10.2.1. I haven't done extensive troubleshooting yet.

On Tue, Feb 28, 2017, 8:19 PM Lee Clagett <notifications@github.com> wrote:

> But are you have an issuing with "normal" mining, or just "smart" mining?
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/1821#issuecomment-283224843>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AGT7KAzizascB0Rg8jFUbz4V1f5R-PEDks5rhNXCgaJpZM4MNw4x>
> .
>


## doobilydo | 2017-04-08T06:11:57+00:00
A little ashamed to admit, I finally got around to building and running monerod from source. 

I'm slowly working my way through the workflow. Has there been progress on the smart mining bug that I can zone in on? 

## moneromooo-monero | 2017-04-08T07:06:44+00:00
Apply the patch in https://github.com/monero-project/monero/pull/1946, and run with --log-level 0,miner:DEBUG and paste the log to fpaste.org after you have run into the bug again.

## doobilydo | 2017-04-09T23:00:19+00:00
Question:

I'm _not_ running into the idle (hashrate 0) problem, smart mining on monerod 10.3.1 via source.

I went back to run monerod 10.2.1, hoping to recreate the bug (`./monerod --log-level 0,miner:DEBUG`) via the downloaded tar (where I found the problem), but now I'm not seeing **monerod.log** in **~/.bitmonero/**. I deleted the file to clear it for the new 10.2.1 logging. It's not being written again by monerod. **bitmonero.log** is updated by monerod.

Would the log be in a different place? I'm not finding it in the directory where I'm running monerod either. Was **monerod.log** a new file created in 10.3.1?

## moneromooo-monero | 2017-04-10T17:58:02+00:00
The filename was changed when the daemon was renamed from bitmonerod to monerod. This was fairly recently, can't recall exactly when, maybe a few months ago.


## moneromooo-monero | 2017-12-23T11:56:44+00:00
Can I assume it's been working with the patch mentioned above, and thus this bug can be closed ?

## doobilydo | 2017-12-31T17:32:30+00:00
With or without the patch, I couldn't duplicate the issue in 0.10.3.1. There are other problems occurring with 0.11.0.0 that I don't have the time to debug. 

# Action History
- Created by: doobilydo | 2017-02-27T23:24:10+00:00
- Closed at: 2017-12-31T17:32:30+00:00
