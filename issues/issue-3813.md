---
title: monero-wallet-cli frozen after confirming transfer command
source_url: https://github.com/monero-project/monero/issues/3813
author: vertangelx
assignees: []
labels: []
created_at: '2018-05-16T19:49:31+00:00'
updated_at: '2018-06-21T21:16:15+00:00'
type: issue
status: closed
closed_at: '2018-06-05T11:16:57+00:00'
---

# Original Description
Tried to use `monero-wallet-cli`(Monero 'Lithium Luna' (v0.12.0.0-master-release)
) on my Ubuntu system to send some XMR out of my wallet.

However after confirming that no payment id is included, it just freezes there.

    [wallet 46yPyn]: transfer unimportant 47SQNwzYsD5Pfry6CtpNcFfwWp3u5hNQ9PhrYkVx8WRHToS81ifwgNuLdudTUWorQH6R5aozAPqXXXXXXXXXXXXXXXXXXXX 0.013
    Wallet password:
    No payment id is included with this transaction. Is this okay?  (Y/Yes/N/No): y

Is something wrong?


# Discussion History
## moneromooo-monero | 2018-05-16T22:27:15+00:00
Probably a timeout with a slow RPC. Try with https://github.com/monero-project/monero/pull/3815

## athenawisdoms | 2018-05-19T05:32:19+00:00
@moneromooo-monero I am experiencing the same slowness when doing a transfer from both monero-wallet-cli and monero-wallet-rpc.

Do you mind elaborating on how we can make use of issue #3815 to solve the slowness/timeout?

Thank you so much

## moneromooo-monero | 2018-05-19T07:37:02+00:00
You just apply the commit in that PR.

git fetch origin pull/3815/head:PR3815
git cherry-pick PR3815

That will apply the commit to your current branch. You may want to switch branches to a temporary one first if you're on master.

## athenawisdoms | 2018-05-21T04:07:26+00:00
@moneromooo-monero Tried your instructions and re-compiled the binaries after applying the new PR3815 commits to a new branch.

Now when I try to send some funds `transfer unimportant xxx 0.1 yyy` this time with payment ID, it prompts for wallet password, then nothing happens for over a minute, then it says

> There is currently a 1 block backlog at that fee level. Is this okay?  (Y/Yes/N/No): y

Is it supposed to freeze for so long?

## moneromooo-monero | 2018-05-21T09:04:44+00:00
Yes in the general case. It'll be fixed later.
There's a cache for the common case, which you're apparently not hitting though.
What is "segregation_height" set to when you type "set" in monero-wallet-cli ?

## moneromooo-monero | 2018-05-21T09:07:08+00:00
Also, I updated 3815 to add another case, make sure you're running the current one.

## athenawisdoms | 2018-05-21T21:42:54+00:00
`segregation_height = 0`

Tried sending again today (without your new update to PR3815) and it appears faster. Not sure what was the difference compared to the slow one yesterday when using  PR3815 fix.

## moneromooo-monero | 2018-05-22T14:14:56+00:00
I've now fixed it, but it requires a db change, so that's not going to be in 0.12.1.0. It'll be instant when it's in.

0 is the expected height, and it should then hit the cache. I don't see why it'd be slow then.

## moneromooo-monero | 2018-06-05T11:00:29+00:00
The cache is now in 0.12.2.0, it should be fast unless you override segregation height. If you still get slowness with the default, please reopen.

+resolved


## blankclemens | 2018-06-21T21:16:15+00:00
On Windows 10, using 0.12.2.0 I experience the same: The moment I answer the payment id question (with Y), the cli freezes. 

# Action History
- Created by: vertangelx | 2018-05-16T19:49:31+00:00
- Closed at: 2018-06-05T11:16:57+00:00
