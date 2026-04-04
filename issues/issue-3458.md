---
title: Can TESTNET be reset?
source_url: https://github.com/monero-project/monero/issues/3458
author: Admiral-Noisy-Bottom
assignees: []
labels:
- invalid
created_at: '2018-03-21T09:00:04+00:00'
updated_at: '2018-03-28T00:00:50+00:00'
type: issue
status: closed
closed_at: '2018-03-28T00:00:50+00:00'
---

# Original Description
I'm having a problem with pool payments and it might be related to me using --stagenet. After downloading Linux binaries (I had previously built from source) I discovered that --stagenet isn't even an option.

I'm switching to --testnet to confirm that I'm not imagining the --stagenet issue.

BUT, the damned test net is almost as huge as the real net. FFS, now I have to wait days for it to sync up!!!!

There doesn't seem to be a bootstrap for testnet!!!!

Chances are I'm about to waist days syncing only to find my problem still exists.

CAN TESTNET BE RESET SO PEOPLE CAN TEST WITHOUT WAITING A LIFE TIME. 

# Discussion History
## moneromooo-monero | 2018-03-21T11:59:48+00:00
No. However, now that we have network types, maybe a "instant start on version N" network might be a good idea.

Besides, you can reset the testnet yourself, by not connecting to others (--offline).

## Admiral-Noisy-Bottom | 2018-03-21T21:17:57+00:00
Oh, I looked at the --offline option and ran monerod --offline for a short while.

Can my pool be tested like that? Without peers, will a genesis block get created and then further blocks for test purposes?

That would be awesome and I'll try it - if it works I'll retract my FFS comment.


## moneromooo-monero | 2018-03-21T22:17:36+00:00
I certainly test stuff like that when I don't have a compatible daemon and don't need more than one node. A genesis block will get created if you're starting without one. If you have a partly synced chain, it'll just use that.

## Admiral-Noisy-Bottom | 2018-03-21T22:29:21+00:00
It didn't work, so I've continued with the sync process.

Daemon started using the --testnet --offline and all looked normal.

Wallet created using --testnet and then opening in wallet-rpc using --testnet.

But it all turned to custard when the pool node started. It went round and round in circles with a message "Core busy".

Oh well, it was worth a try. My testnet is only 346 days behind - it'll get there eventually.

## moneromooo-monero | 2018-03-21T23:28:00+00:00
What commit hash are you running ? Recent versions should not be doing that.

## Admiral-Noisy-Bottom | 2018-03-21T23:32:11+00:00
I assume by commit hash you're referring to the version or something like that. I download a binary from your site yesterday. 

I had also download source and built my own binaries (it has --stagenet but the binaries downloaded yesterday don't).

But the one I'm running now is from your getmonero.org site for Linux 64.



## moneromooo-monero | 2018-03-22T08:36:49+00:00
Then use the one you built, which should be recent enogh.

## Admiral-Noisy-Bottom | 2018-03-22T08:42:25+00:00
Ok, I've made a discovery (I think). The pool was not paying while using --stagenet and the binaries I built. I download the pre-built binaries from your site and synced --testnet (--stagenet doesn't exist) and payment to miners works. In summary, miners not payed while on stagenet and binaries built from latest source. Miners are paid using binaries pre-built and testnet. Odd!

I changed nothing in the pool. The only thing that changed was the binaries and I moved to --testnet. I'm about to switch back to the binaries I built and use --testnet and see what happens.

LOL, I've just run the binaries I built using the the same command line and monerod says I'm 89 days ahead! Yet under the binaries downloaded it was synced just 5 minute ago.

## Admiral-Noisy-Bottom | 2018-03-22T09:19:54+00:00
Ok, the latest build works on testnet but not stagenet. I'm not too bothered now I've got it work but it might be something for you to look at for later on.

## moneromooo-monero | 2018-03-27T23:27:00+00:00
So you're now saying stagenet does not work when used with a pool to pay miners, right ?
If so, can you please open a bug for this, and I'll close this one.

+invalid

# Action History
- Created by: Admiral-Noisy-Bottom | 2018-03-21T09:00:04+00:00
- Closed at: 2018-03-28T00:00:50+00:00
