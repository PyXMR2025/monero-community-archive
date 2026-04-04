---
title: Monero changes wallet file permission to current user
source_url: https://github.com/monero-project/monero/issues/4674
author: ghost
assignees: []
labels: []
created_at: '2018-10-20T12:15:48+00:00'
updated_at: '2019-08-19T17:09:41+00:00'
type: issue
status: closed
closed_at: '2019-08-19T17:09:41+00:00'
---

# Original Description
I use a different user to run monerod and rpcd to protect my system from any attacks.

When I open wallet file in root using cli or rpc, the program changes its owner to root and permission to 0600.

This is not desirable as I need to check the wallet on other user and start rpc again. There could be fixes like if the program is run by root don't change wallet file permission or ask for it.

Also, when monero can't locate it's file because of permissions, it shows only file read error which is impossible to debug what's going on. I hope it notifies the user about the wrong permission though i don;'t think it's possible.

# Discussion History
## moneromooo-monero | 2018-10-20T17:22:31+00:00
Monero does not change the owner, but writes the entire file anew. So if you run as root, the new file is created as root. If you do not want the file owned by root, then do not run the wallet as root.

Errors could be made more informative, yes. There are plenty of places in Monero where errors are kinda "bundled", which is not very good.



## ghost | 2018-10-21T03:45:01+00:00
There must be a better solution than to write the entire wallet. I've dealt with many daemons and monero wallet daemon fails pretty frequently with no information to debug and loses everything...

I fixed the problem by having two wallets with two daemons, one restarting once per day and one taking the failover while restarting... I think there could be an elegant way to deal with this kind of problems.

## moneromooo-monero | 2018-10-21T08:41:44+00:00
Fails to write the wallet cache file ? If so, becaue of permissions problems, or other problems too ?

## ghost | 2018-10-21T09:13:49+00:00
Running for months..... And when rpc does not respond, no trace data on log, nothing to debug on, systemd service shows green. god knows why it’s wrong.

Replaces it with failover daemon, tries to fix it, nothing works, sysadmin declares it dead, have no option but to kill it. Loses wallet data, past read blocks, txes...

Inform users new subaddresses and hope for new daemon to work fine.

And life goes on....

## moneromooo-monero | 2018-10-21T09:18:59+00:00
If it dies like this:

gdb /path/to/monero-wallet-rpc \`pidof monero-wallet-rpc\`
thread apply all bt


## iDunk5400 | 2018-10-21T10:12:14+00:00
(Added for proper quoting)
```gdb /path/to/monero-wallet-rpc `pidof monero-wallet-rpc` ```
`thread apply all bt`

It might be easier to c/p a file's contents than to c/p screen by screen of gdb output
```
gdb /path/to/monero-wallet-rpc `pidof monero-wallet-rpc` -ex "thread apply all bt" -ex detach -ex quit > /path/to/monero-wallet-rpc_stack_trace.txt
```

## ndorf | 2018-10-25T09:42:14+00:00
> Monero does not change the owner, but writes the entire file anew. So if you run as root, the new file is created as root. 

Why not just truncate the file instead of recreating it? Otherwise, opening a wallet through a symlink or hardlink results in quite a nasty surprise: the original wallet is left unchanged (i.e. out of date), and the link is replaced with a separate, updated copy.




## moneromooo-monero | 2018-10-25T09:47:30+00:00
Because then it is not atomic and you might end up with a partially written file.

## ndorf | 2018-10-25T20:16:35+00:00
@moneromooo-monero In light of that, the keys file could be a problem: unlike the big file, this one is truncated and then rewritten. So, with some really bad luck, one could lose the keys during a password change (or wallet upgrade, if that ever happens)?

`wallet2::change_password()` via `store_keys()` [ends up here](https://github.com/monero-project/monero/blob/1e74586ee99e4bd89626d2eb4d23883cd91f0f81/src/wallet/wallet2.cpp#L3142):
```
r = r && epee::file_io_utils::save_string_to_file(keys_file_name, buf); //and never touch wallet_keys_file again, only read
```

[Then](https://github.com/monero-project/monero/blob/1e74586ee99e4bd89626d2eb4d23883cd91f0f81/contrib/epee/include/file_io_utils.h#L73):
```
fstream.open(path_to_file, std::ios_base::binary | std::ios_base::out | std::ios_base::trunc);
fstream << str;
fstream.close();
```

## moneromooo-monero | 2018-10-25T21:14:04+00:00
Can you file a bug about it ? It used to be it never got written to, but started to be due to the settings.
That said, the settings could also go in the cache file...

## ndorf | 2018-10-25T23:29:05+00:00
> Can you file a bug about it ? 

I just created PR https://github.com/monero-project/monero/pull/4729 to fix it. Do I need to create the issue as well?


## moneromooo-monero | 2018-10-26T08:21:40+00:00
No, the issue is just so it doesn't get forgot, a PR is better :)

## hyperreality | 2019-08-18T22:47:25+00:00
Since the PR just above was merged, can this original issue be closed out? Explicitly chown'ing the wallet files back down to a lower security level when root is running the wallet would seem like an antipattern. 

I don't think it makes sense to run monero-wallet-* as root and should be discouraged anyway. 

## moneromooo-monero | 2019-08-19T17:07:15+00:00
+resolved

# Action History
- Created by: ghost | 2018-10-20T12:15:48+00:00
- Closed at: 2019-08-19T17:09:41+00:00
