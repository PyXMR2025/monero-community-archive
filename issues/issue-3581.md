---
title: failed to get output distribution
source_url: https://github.com/monero-project/monero/issues/3581
author: m9ra
assignees: []
labels: []
created_at: '2018-04-07T23:33:04+00:00'
updated_at: '2018-06-25T22:25:01+00:00'
type: issue
status: closed
closed_at: '2018-06-25T22:25:01+00:00'
---

# Original Description
After upgrading my monero tools to reflect PoW change, I'm getting the following errors anytime I try to make a transfer through monero-wallet-rpc.

```
<Response [200]>
{
    "jsonrpc": "2.0",
    "id": "0",
    "error": {
        "message": "failed to get output distribution",
        "code": -4
    }
}
```

and in the wallet I can see this:

> 2018-04-07 22:36:54.664 [RPC0]  ERROR   wallet.wallet2  src/wallet/wallet2.cpp:5836     segregation_fork_height - d.start_height >= d.distribution.size(). THROW EXCEPTION: error::get_output_distribution
> 2018-04-07 22:36:54.664 [RPC0]  WARN    net.http        src/wallet/wallet_errors.h:794  /root/monero_v2/monero/src/wallet/wallet2.cpp:5836:N5tools5error23get_output_distributionE: failed to get output distribution, request = Distribution size too small


I tried to renew blockchain (deleting ~/.bitmonero and importing it from scratch) and the same error remains.

> /opt/monero/monero-wallet-rpc --version
> Monero 'Lithium Luna' (v0.12.0.0-master-8361d60)


# Discussion History
## kotehok | 2018-04-08T12:09:48+00:00
I have the same error after hard fork. Completely impossible to send any transaction. Please help.

## moneromooo-monero | 2018-04-08T15:00:48+00:00
Try https://github.com/monero-project/monero/pull/3584

## m9ra | 2018-04-09T06:38:11+00:00
Thank you, I accepted the pull request locally and after recompilation, the transfers are working.

## egonson | 2018-04-10T01:30:39+00:00
I have the same error too. ("failed to get output distribution")
Is #3584 the official solution?
If someone does not fetch is the error normal? 
Why is that code commited to master branch?

## moneromooo-monero | 2018-04-10T08:24:11+00:00
It is a good solution. We have no offices. I don't understand the third question. It is not committed to master yet.

## BKdilse | 2018-04-13T20:42:45+00:00
I'm also getting this today, on my 1st block.  Do we have an official solution?  Or and ETA on release?

## moneromooo-monero | 2018-04-13T21:29:05+00:00
Did you try 3584, and did it work ?

## BKdilse | 2018-04-13T21:32:07+00:00
Not really good with these merges and pulls, still learning.  Do I have to manually make the change to the file on my server, or just do a fresh download?

EDIT: Can see, it's not in the latest master, have downloaded it, edited, compiling.

## BKdilse | 2018-04-13T23:13:42+00:00
Can confirm this change fixes my issue too.

## moneromooo-monero | 2018-04-14T09:13:35+00:00
Great, thanks for testing.

## shnetinka | 2018-04-17T20:05:06+00:00
How can I get the build this is in?  I can't send anything from my wallet.  I have the release build v12 on Ubuntu 16.04.  I am not sure how to use git to just pull in this PR

## scoobybejesus | 2018-04-17T23:00:00+00:00
@shnetinka I just did this.  In the `monero` dir, `git pull origin pull/3584/head`. Then `make`.

@moneromooo-monero I had this problem (with `monero-wallet-cli` 2 hours ago (while it tried to communicate with my local node, on the same box, no less), and after building with #3584 I no longer have the problem.

## BKdilse | 2018-04-18T13:56:43+00:00
This may or may not be related, but I wanted to mention it in case this change caused the issue I had.  Full details in: https://github.com/Snipa22/nodejs-pool/issues/397

1st block paid out fine, after I made this manual change (adding * 1000) to the timeout.
2nd block paid out, but would not update the tables in SQL.

I did increase limits in Ubuntu and MySQL which could have resolved it, but I saw everything working once I updated to the latest Daemon, which does not have this manual fix in (which I initially tested working).

Please let me know your thoughts.

## shnetinka | 2018-04-18T20:57:04+00:00
@scoobybejesus  thanks.  That worked.  I thought that was how to do it but I think I had a master in the path somewhere which was obviously wrong.

@moneromooo-monero  - updated yesterday and the wallet appears to be working well.  Thanks!

## moneromooo-monero | 2018-06-25T22:00:01+00:00
+resolved

# Action History
- Created by: m9ra | 2018-04-07T23:33:04+00:00
- Closed at: 2018-06-25T22:25:01+00:00
