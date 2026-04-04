---
title: 'Can''t create transaction: internal error: Daemon response did not include
  the requested real output'
source_url: https://github.com/monero-project/monero/issues/4718
author: kr1-ch
assignees: []
labels: []
created_at: '2018-10-24T20:30:35+00:00'
updated_at: '2018-10-27T15:30:06+00:00'
type: issue
status: closed
closed_at: '2018-10-27T15:27:37+00:00'
---

# Original Description
When I try to send a transaction from the 0.13.0.3 GUI, I keep getting stuck with this error:

> Can't create transaction: internal error: Daemon response did not include the requested real output

I tried to close the wallet and open it back, but nothing changes. I also tried from the 0.13.0.3 CLI, unfortunately the problem is the same.

I already tried the command "rescan_bc" to rescan the wallet from seed, but unfortunately nothing seems to work. I also tried to delete the lmdb folder and the p2pstate.bin file, to download all the blocks again. 

I tried on multiple computers (Windows & Mac OS), but the issue is still the same. 

It's strange because the daemon status is "synchronised" but the unlocked balance has the status "waiting for blocks":

![zg16p](https://user-images.githubusercontent.com/11709283/47456487-fc41a800-d7d4-11e8-84b8-52caf51c9652.png)

The problem happened after I tried to send moneros from the Monero wallet GUI v0.11.1.0 last Sunday. The day after the order was still stucked with a Blockheight status "PENDING" during several hours, so I updated to Wallet v0.13.0.3 and was finally able to cancel the order (then the status changed to "FAILED"). 

Then I tried again to send money to the same address (using the same key), but it doesn't work and I am stucked since.

For information I am using the same daemon version as CLI and GLI.

# Discussion History
## moneromooo-monero | 2018-10-24T20:58:30+00:00
Are you willing to build with a patch with extra logs ?

## kr1-ch | 2018-10-25T06:46:37+00:00
> Are you willing to build with a patch with extra logs ?

Yes of course, how can I do that?

## moneromooo-monero | 2018-10-25T08:43:23+00:00
Copy this patch to a file:

<pre>
diff --git a/src/wallet/wallet2.cpp b/src/wallet/wallet2.cpp
index 6ddc0d348..5f4019162 100644
--- a/src/wallet/wallet2.cpp
+++ b/src/wallet/wallet2.cpp
@@ -7207,11 +7207,20 @@ void wallet2::get_outs(std::vector<std::vector<tools::wallet2::get_outs_entry>>
       for (size_t n = 0; n < requested_outputs_count; ++n)
       {
         size_t i = base + n;
+        MGINFO("base for " << n << ": " << i);
         if (req.outputs[i].index == td.m_global_output_index)
           if (daemon_resp.outs[i].key == boost::get<txout_to_key>(td.m_tx.vout[td.m_internal_output_index].target).key)
             if (daemon_resp.outs[i].mask == mask)
               real_out_found = true;
       }
+if(!real_out_found)
+{
+MGINFO("Not found: " << td.amount() << "/" << td.m_global_output_index << " in " << requested_outputs_count);
+MGINFO("key " << boost::get<txout_to_key>(td.m_tx.vout[td.m_internal_output_index].target).key << ", mask " << mask);
+MGINFO("List of outs we got:");
+for (size_t i = 0; i < daemon_resp.outs.size(); ++i)
+  MGINFO("key " << daemon_resp.outs[i].key << ", mask " << daemon_resp.outs[i].mask << ", txid " << daemon_resp.outs[i].txid);
+}
       THROW_WALLET_EXCEPTION_IF(!real_out_found, error::wallet_internal_error,
           "Daemon response did not include the requested real output");
 
</pre>

Apply with with:

patch -p1 < filename-you-saved-to

make (or make debug, whichever you used before)


## kr1-ch | 2018-10-25T12:35:46+00:00
I tried to patch but got an error:
> patching file src/wallet/wallet2.cpp
> Hunk #1 FAILED at 7207.
> 1 out of 1 hunk FAILED -- saving rejects to file src/wallet/wallet2.cpp.rej

The content of wallet2.cpp.rej:

```
***************
*** 7207,7217 ****
        for (size_t n = 0; n < requested_outputs_count; ++n)
        {
          size_t i = base + n;
          if (req.outputs[i].index == td.m_global_output_index)
            if (daemon_resp.outs[i].key == boost::get(td.m_tx.vout[td.m_internal_output_index].target).key)
              if (daemon_resp.outs[i].mask == mask)
                real_out_found = true;
        }
        THROW_WALLET_EXCEPTION_IF(!real_out_found, error::wallet_internal_error,
            "Daemon response did not include the requested real output");
  
--- 7207,7226 ----
        for (size_t n = 0; n < requested_outputs_count; ++n)
        {
          size_t i = base + n;
+         MGINFO("base for " << n << ": " << i);
          if (req.outputs[i].index == td.m_global_output_index)
            if (daemon_resp.outs[i].key == boost::get(td.m_tx.vout[td.m_internal_output_index].target).key)
              if (daemon_resp.outs[i].mask == mask)
                real_out_found = true;
        }
+ if(!real_out_found)
+ {
+ MGINFO("Not found: " << td.amount() << "/" << td.m_global_output_index << " in " << requested_outputs_count);
+ MGINFO("key " << boost::get(td.m_tx.vout[td.m_internal_output_index].target).key << ", mask " << mask);
+ MGINFO("List of outs we got:");
+ for (size_t i = 0; i < daemon_resp.outs.size(); ++i)
+   MGINFO("key " << daemon_resp.outs[i].key << ", mask " << daemon_resp.outs[i].mask << ", txid " << daemon_resp.outs[i].txid);
+ }
        THROW_WALLET_EXCEPTION_IF(!real_out_found, error::wallet_internal_error,
            "Daemon response did not include the requested real output");
```




## moneromooo-monero | 2018-10-25T13:41:16+00:00
What version are you trying to apply it on ?

## kr1-ch | 2018-10-25T20:29:06+00:00
The last one I guess.

I simply ran the command `git clone --recursive https://github.com/monero-project/monero`
Then `cd monero`
Finally `patch -p1 < filename-you-saved-to`

It was the first time I installed the whole project. Usually I only use the Wallet GUI or CLI for Windows and Mac OS

## moneromooo-monero | 2018-10-25T21:25:55+00:00
It looks like github is mangling *some* of the <> chars.

First:

git reset --hard

Then apply this variant instead, same command:
https://paste.debian.net/hidden/bdcf3449/

## kr1-ch | 2018-10-26T05:52:43+00:00
OK this time it worked.

git reset --hard
> HEAD is now at 29073f65 Merge pull request #4705

patch -p1 < patch1.txt

> patching file src/wallet/wallet2.cpp
> Hunk #1 succeeded at 7153 (offset -15 lines).

What must I do now?

## moneromooo-monero | 2018-10-26T08:22:17+00:00
Repro the problem, and get me those new logs afterwards.

## kr1-ch | 2018-10-26T09:26:00+00:00
OK but before yesterday I never installed the whole Monero project. Usually I only use the Wallet CLI or GLI downloadable from the Monero website.

How can I ensure my Wallet will use the local patched project?

## moneromooo-monero | 2018-10-26T09:31:04+00:00
Run the new binary instead of the old one.
So, instead of cd /old/path ./monero-wallet-cli, you do: cd /new/path; ./monero-wallet-cli
And add the usual options, like --log-level --wallet-file, etc.
If your wallet was in the old directory, you'll have to give the path to that wallet file too so it can be found.

## kr1-ch | 2018-10-26T14:22:17+00:00
Thanks for explanation.

Then I ran the CLI inside this folder /monero/build/Darwin/_HEAD_detached_at_v0.13.0.4_/release/bin 

Here is what I found in logs:
```
2018-10-26 14:05:45.346	  0x7fffb0d4e380	INFO 	logging	contrib/epee/src/mlog.cpp:277	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-10-26 14:10:00.504	  0x7fffb0d4e380	INFO 	logging	contrib/epee/src/mlog.cpp:277	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-10-26 14:14:49.211	  0x7fffb0d4e380	INFO 	logging	contrib/epee/src/mlog.cpp:277	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
```

## moneromooo-monero | 2018-10-26T14:57:42+00:00
Add "--log-level 1", the wallet does not log by default. I'll need the logs which have "global" in them.

## kr1-ch | 2018-10-26T16:18:20+00:00
Am I supposed to add it after the command?
`transfer ADDRESS AMOUNT PAYMENTID --log-level 1`
Or when opening CLI?

## moneromooo-monero | 2018-10-26T16:19:48+00:00
On the monero-wallet-cli command line.

## kr1-ch | 2018-10-26T16:37:56+00:00
OK, then when I do:
`transfer ADDRESS AMOUNT PAYMENTID --log-level 1`

There is an error:

> Error: amount is wrong: 3e94c7b940ff121efc56f2b655f178fc347183bedd2779b842309133fd481632 --log-level, expected number from 0 to 18446744.073709551615

Where "3e94c7b940ff121efc56f2b655f178fc347183bedd2779b842309133fd481632" is the payment id I want to use.

I also tried to an address without payment id, the error was:

> Error: failed to parse address

I think I am not doing it the right way!?

## moneromooo-monero | 2018-10-26T17:34:22+00:00
Yes, as I said above, --log-level 1 goes on the monero-wallet-cli command line, not the transfer command.

## kr1-ch | 2018-10-26T19:31:15+00:00
I finally was able to run it with `open monero-wallet-cli --args log-level 1` (is this the right way on Mac OS?)
Unfortunately after another try to transfer, there is nothing more in logs.

## moneromooo-monero | 2018-10-26T20:02:26+00:00
I don't know where you got that idea. It is definitely not what I said above.
I said "--log-level 1".
But then maybe the open command on Mac does that ? No clue.

## iDunk5400 | 2018-10-26T20:34:22+00:00
Open a terminal, `cd` to the folder with the binaries, type
`./monero-wallet-cli --wallet-file /path/to/your/wallet --log-level 1`


## kr1-ch | 2018-10-26T21:15:25+00:00
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 0: 0
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 1: 1
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 2: 2
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 3: 3
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 4: 4
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 5: 5
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 6: 6
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 7: 7
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 8: 8
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 9: 9
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 10: 10
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 11: 11
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 12: 12
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 13: 13
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 14: 14
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 15: 15
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 16: 16
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 17: 17
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 18: 18
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 19: 19
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 20: 20
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 21: 21
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 22: 22
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 23: 23
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 24: 24
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 25: 25
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 26: 26
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 27: 27
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 28: 28
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 29: 29
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 30: 30
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 31: 31
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 32: 32
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 33: 33
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 34: 34
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 35: 35
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 36: 36
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 37: 37
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 38: 38
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 39: 39
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 40: 40
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 41: 41
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 42: 42
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 43: 43
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 44: 44
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 45: 45
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 46: 46
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 47: 47
> 2018-10-26 21:05:47.288	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 48: 48
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 49: 49
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 50: 50
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 51: 51
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 52: 52
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 53: 53
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 54: 54
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 55: 55
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 56: 56
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 57: 57
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 58: 58
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 59: 59
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 60: 60
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 61: 61
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 62: 62
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 63: 63
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 64: 64
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 65: 65
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7156	base for 66: 66
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7164	Not found: 21772686660000/5224156 in 67
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7165	key <016c67a7360aa110283fae4d3eb20ce8d054639cd4c39eec4d5889994344f5a5>, mask <19b887496ede3ff9bde6cf673e9993fc07c5c65ef192dcacd606cc4318e1dca1>
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7166	List of outs we got:
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <fc31a65733d6ed0753e9e0595a31c21d0b7e364161b086d004dd3d91d267574b>, mask <c8b457672b33f41b441038e19716150fecf3ed5cc7c082c7b383dd0fd8acdec9>, txid <6708d16336a7af14f1ac40165004dcf81beacb9167fbcd48a6bfbccae81ac226>
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <63d6fd71359e5f800e473aac1c8bb32a2c43bd6edc9003f72035ae128538a4e1>, mask <3d433bd5f49246e1b09604df8d8d2cff03ac44ece494e8a2a0b5b11d1c588016>, txid <9932e9c854c553e9fc16496076616cbb220f8cbffcfa0868ef6a35e8f0ad9da3>
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <2cd7b3259fd8ce677cd13a189e5f8254e205ef17d9b5917894fc443a713fc3a5>, mask <675649bcd05b60e2d5aac582f526721a4615710d898486cbafa3146bb8a60be5>, txid <7b5db1f2ca40041a38ec5234be8c07db807e07eb483e08e4ac850ac228252d5f>
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <c33bac69b38823cbdb759c63f76108775d8b07166125ad77dc17775774611cde>, mask <125df875f3fd487e892449f6cbdfdcf44ddd18ba9a93b1f0ac7047a85674af43>, txid <b7e43a4b492bb99b6933b97355121784244d492857a7a14c34631f826c9c2c46>
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <64f5aee66af833630de046893f8c02346c9762566bf33f0f57e862acc01dd3b8>, mask <027afb9c9b46588729c69cbf7b0915164c9de3a649433b4db1d72418a43d980a>, txid <18a49792c569694dda701fc182984943d08551910a7652c45dd744b7510639d1>
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <b7c8675f5b44e5fc637df98b1c9847995ab1edf09aba2bab6cebb390ed2b1051>, mask <c8b6521a418effba82e41ac690245bbe1ee99762d358a561573900a6d1925c3f>, txid <1303f3f3aa952e7b66d1e9ef4358b4ea9ceefca3db4352c3fa66dfa9318e93f6>
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <b803cc19ff1148a64f9b4aa0e0493c1ceae1323b066f5961e8fdd0ae13c6d36b>, mask <0758c7b1cf8679668a58fd375caf746acbd8d44730082e2c7f02657524832461>, txid <083e9387edb2766b66450a8c5d0af25d9ad28e5c4fef3132ed8c7546f86a4001>
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <50da372b59d7a5b5163b72e06f49c32dbfc2ec5a23af247b7fb9fe21865ca7fb>, mask <a824571cb239f03979abd313fcf96ca85fb827ecd7a593c2fe7c96e39d574699>, txid <5aec9b0add9c5b11b401b94ef1373019e42121f0e6d480e77d834a8faf3ed42d>
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <8ae31163ae72f461b20ffc0e3fb5e95d9ef4c205872398ce3f46322c759f638a>, mask <628a388bda8fceade19a73af3c27ce82a7bc57ff2786549f91d5ad1374b189da>, txid <59f88983a70fb3713942ee1aa239cfa996d33a275a48ff00e9624337ceed904d>
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <ad0735e56292c7187e2770e18284e81d139110fa142eae6eba865cea490d308c>, mask <bf40a7eb60686a7dbacfdf199e31d19512a2e492770735c48897ec31519ed020>, txid <3abfff62d244519f0d288737fe94229affdff545ec404283b11b9bbaf1ce492f>
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <d9f44d0c9bf6e9d6cc2f9ddb37390f447246a248c8064bec061c07cae0b515ce>, mask <131fb16db5d5722dd293ba7ea6cc76cdf5725cf15aac4f5a777925af2df6c55a>, txid <1ad66b0ecd0c03498476b762e120472332c2b3537d6edd3e7ce9ec74d390f6e9>
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <d5d3df300ff1c4c76c1d8fa0a99c18fdce3a9558873db99d75f1a6b2eb78d64c>, mask <45c55e29b469ddeff34f2a6112c5ed75986702db8d84f82f3dc85837ed441151>, txid <f595cf74d6849f2c0616a3bac2099a65838ea596636c2a936ab33c33dbafbdb6>
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <ba249c69dd7b6131f1d977dd84afebd114cb249877d8b05b56826d2d5da1486c>, mask <e04f71244fc031cfd69c35b3923b6bdd754fab53aa4e75de4dd22ce603b86337>, txid <8821ad94297c4e00c8f89d45e5270035db342dc2651db07d9454663982bcebd9>
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <e24b8f0f498c1546ee514448e0929d1f6ebc406f4d5befa5d7b8b2a5a48d076a>, mask <d55222ab140647c78a1597b40f55438a2d76b61c1782a7acb63a95538023bfd4>, txid <8e86506f9f8a3bef5a38e5b1f4a5967573583e9496e8606c91d842d61d3e19ef>
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <d0aa7c2c872db824e5486860e884d4c7c6474f1ffd518d0f8920214d41a0b1ec>, mask <2ec4ad6a2f7139eb8c2933d857f2489820e81f16875cbca5eccd62a58e54f1a6>, txid <e69f119fcd6709ddcff5e2ad32c6857c6f8c878f5a5c63529d794a4175713aa9>
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <fafce707fd676194cc03bc897c03ccfcee78ff98369e8c93c9ec7d30e5284e7e>, mask <a12806d9a84ba256070ff63580035b983441e9c1cbf2828ae0a179866984a219>, txid <8b706dd6b5e823b2d572f7a2919ced381afcf40723c69e36a970156e5ac37a40>
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <181b8d1d92a79af856532c2b2335c7e4242c61d631bb0e3f53894c3c56717b9a>, mask <70d88c2bc9e310b74252280eccd07783d063dd3788040c92e2a537934a9f13ab>, txid <8094ffa37f5ad65bf279666a8981b697a3f647df94bba7543f89c8e14ba8dbc1>
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <d55880dc6934a0035a474da2229fedb4eafd9323af36a076cb320c6b52763a0f>, mask <bf8f1259713b2ecbf22785edecb47eee74f63a9b0db0a88534d8aa71d569d2da>, txid <83f5c000adff9677b6552ff5d78f74513028bfcef3bb1ef0dfc63ad58bb0c4cb>
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <6fea9ef957f1da5f34b7a1e462c53f6e3a80555fdea4d53442f15bfee57c1c10>, mask <0c3ff34e1ec297cfd1896eca5b6db069933750661dc0c95ac1feaabc1018fef4>, txid <e4e6ff920c4924b24fb9dc89fe08a225516f5f49939935c67ae0ce681b7271c3>
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <e4940dc6d8532d4c6d39ecc9ed57720f4cefdc340031f2fdc2d1da6949c3444e>, mask <e545d2f1338d3e2dc12fee0e58570bed5356e0f4cf81befdb77fd5afc688809a>, txid <30559cc6d4a91d09024df404639e70638d503cdce8ea4eec6e400f4870fd58ff>
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <a370bca9796f170e8da1c42e281854e4af4ef846a4960ccaa10e902986c76b05>, mask <6686e565772a17ef078fcb5177eab8032bda3b2b3791da196d85e60f45caf606>, txid <25f110a0aec7bbc4192c34a408764a74204e3104d76e97288340bb8f39c6e224>
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <17ac5e6dc39152a70fec2da0bfec9eaf5619bbfe7d512eb5731a3f867da8b071>, mask <d79beba1050f5a1e4c834b6a100e5ccf909fb9bc6df588675ac5b38910c9c79f>, txid <a290a7eb2ab45977170539db8715d7dd20b8ccb617562675b0158e8ad2c0317c>
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <5bc6e215166470c7595474d77e3f18be9d5ded26f96ac595194e16c2bebc3dd7>, mask <5bc689539d11905d3df3b2d291873ba8cbaa8d4d69bc9c5cb73dd427a5492d60>, txid <c04da12ce613e4cca51186aa6c2bbdbf259b171b50349c7eef11775944520688>
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <3719ee49a27e8adcec19d933100f3e916ba715bb08f4172874032cf3bd36430b>, mask <d097a631a36a84b0d755ebec55ea93f1a8ffa964267695ea843fc72b7fe4dbb5>, txid <193ba49719f58de9726ba58566dcaf6c94005374d578a2cc4677bffa128db640>
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <c42d77d630abe44f1f36bf4a32f8781c76a762ead8b96ae246df7cbfe7509c04>, mask <ea05a3ebf1c04d667188204f120cf7085e3828ccd6d7bebd1668079b3c3aa997>, txid <93461a9da8d96994ba6bdf85c7fff59b0543e07452fc5d7f13271142254ca58b>
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <90cdf60e0ae5587a2952c7b0db3a9e725198e3c52cd7b02914ef28ac04a0e6e1>, mask <48e50f8bc6f3111ff725bbd4668b3f7c1284c9fdb0df477c0d41e5fd13177493>, txid <3e8aaa72d5792c21c385f87d28a59722a65f05243f171243149890d1c9853852>
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <90e408aae3093d127e32e69c70f987a3537768ed58504c6a1f9e1fde27fa1d49>, mask <613fe32e33ca94e5a746974206e1af2902ec0087ff93d7422b773148ce4fc8c1>, txid <b7f5b2567ec854d78f6963a354935ab04516eb86795770b95ca63e32a904f898>
> 2018-10-26 21:05:47.289	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <2c2da21438a3765d9341898865da88c0e923f7d8bd8a4dd81551cd12fac9a56f>, mask <f6baaa4a8392fe1230215860438270247ecd73412c77d9055214dac95cf700b0>, txid <1b3df65010960f883608c1fdce9169c3fa961689f5d45bdec1e02a1c77763f25>
> 2018-10-26 21:05:47.290	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <b7490f2e94103afdfad9543a274efaf7986597c2cc6158ac96fd9fb2ab11dd5a>, mask <d2db156941c787ca2da1527462b509127795a25c252ffc45ba35098ffee04659>, txid <631c6716cf44b44c14373eaaa9b32af6d7c06136db5b2462cc0be169de026294>
> 2018-10-26 21:05:47.290	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <6016ec3c52400ba89248bb530686de167306cca4b4aadc57bae85b491f35418f>, mask <07ee443a85bb75ea78d634a8e40fa4c3050a1f0c84a9b8a30274aada4ebf8853>, txid <373e01972658bc5059f9550513da96aa2af00a6c02fc88bb14a979e2625f3318>
> 2018-10-26 21:05:47.290	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <e77ad57a1dbd431c7220e1705bd6a9bebacf7a53e8f5c5b06b97f4fbb1374b86>, mask <226346863a224dad5d92597dc22eb1620e6238042e731037e92aac6a7d18aa21>, txid <e665b195218cad5a5eff539bc119eb59b6d38e765cc5e653a166e04a3d03263e>
> 2018-10-26 21:05:47.290	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <0e7704eeb9ab2247926f63881454977572175e444c83cd80cda70e8d0ed7da9f>, mask <43bc3f8f65ef40ced5aff252c361796edb8358564d9ac0a8845c5054df9f7a42>, txid <fbe44f36488fbe0cc3d56c54bf13de12e30c085ad8428c2a737a008eaebb5c69>
> 2018-10-26 21:05:47.290	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <89582e149fde1b050e24589182e56c643f85b8ef959eea417a1a95e7dc764e24>, mask <26a887085cbd38ff995cb32354ab8b97f762d1157b511f03aa218bf6927217e7>, txid <8441505b66bb261691240002ff3d2325c6f330c420e1da1dccacab096d254299>
> 2018-10-26 21:05:47.290	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <d97c5661ce02c92c9b1721329a76c6f3fedaead7652e8e699ec8138482b0fd06>, mask <9f2543b227e1782cee7002d33e3725cb6d2699b8cc502b7f859dd3a7229ff448>, txid <e356ef6849468902c898a07c1098695d6c86284f39a394803ce431b9e6b90928>
> 2018-10-26 21:05:47.290	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <d0dfa8b8e03bb2dc84500d797799e24eb5b648e6ac01f55557662e450bce10ac>, mask <ed5fca1ea81dbc482aa2526bdc9d7670697c95257e02e7a23191e8dc53e1ceb9>, txid <946babbcd3e926b02f5d36ff662a34545804d758c03af8e4423337aeac8e0712>
> 2018-10-26 21:05:47.290	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <cb3267564f7a51ce52ec1c81b3b2d2f5ebc2bf82676927b1561e94f449679886>, mask <f69e77d22d775065c487009f036f64c881070cfb8e46744dbbf64c103bcdc9a9>, txid <7e68697050fe670415849a4da668552b00ede2d3ba2e4ab93040825a1e7362d7>
> 2018-10-26 21:05:47.290	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <6e6fcebfe715b02da3cfe28fd3f7762a503331a9826a1f7260e193b702779089>, mask <062bc761f1af048e560884303cbd551ece7a5e3e9b1ef453c70a857db782a4e2>, txid <653de0bdd5456a18f6ebb481df440b8488cbed16a3d8004abbd87126066b6c99>
> 2018-10-26 21:05:47.290	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <6491de02770ef85e08b46d997c6188b209835185d24594480bff0383e56dfa6c>, mask <c30faac31752337de71ea011d8e7c29e5ee4e11a7cfd8257b33759028a667752>, txid <ab30a77709a128c872356d134ec12d4455985313c8ec3f66e61fad92a8af9802>
> 2018-10-26 21:05:47.290	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <589bdc05ce86a12f55452b41d561c2d290eb7782ab28264c35bf59b1c634de37>, mask <f15a2d16808f29bb55a0702ccb08d5d4c8d9992fe134e8626fb824c36fc80f50>, txid <f40be373a30b26ddcf8c83e92832da6bd23a5f21269aed99ac7f58b8ad6e390d>
> 2018-10-26 21:05:47.290	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <850dbdebbb1941b8bc82cf74bc868bcea407625dcaf9911a8e64e852c0ce4ad4>, mask <401d94c38f0888addbfd09a04fbb70fac34047cf66d061c1ba433a8e611c107c>, txid <d1784774f08b3b08799e28532a8ff7913d26c57b45b27756c8e1566539ac461f>
> 2018-10-26 21:05:47.290	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <0287b4352e87bce7166a6eb54f631ffbd479a1782b56a663d93d833d23227927>, mask <f868b32c9c46abdcc9bb9e375af98ac81aa796bf855e35b2b625fb744d1238b7>, txid <ecfbce6413eb1d9b57dc6e7167c4a6499bd68e5c78b6669be55c970a5fa037ce>
> 2018-10-26 21:05:47.290	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <c7b9e35851fa1d8d779c33bd4718db7d62edec8dd862e7c1aab3d1748475ed6a>, mask <04106f867513800fa1d0c9ac8aa676d038004e920713930c387c39cff2d24cf3>, txid <aed189a7f339130f5231322d201304a858b5755546f2c001bd36b4e2eb2d32a7>
> 2018-10-26 21:05:47.290	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <b5cfc9632934c4736071d1b9a3d0ce1e61d8a3467ad91e331946e49cc149c596>, mask <74bfb5d5c6b3315f4a69837f8afd9df300caa1867f5f064872e0cc1c89666363>, txid <1fc38bfcf358b561192ee897bbb89d806fdc6a404c6b48b8c99cff9db29582a2>
> 2018-10-26 21:05:47.290	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <c22a84bb61edb3a99c8c7c8cb3970e60560b81161a865418220dac75fbf51e21>, mask <f7ec9726d36e7f6f977ef6c74f6804904eb7d2da6a22ef230ff6abd6e9709db8>, txid <035a8317e6c696b791fea2a43c2502956c3bbef981090cc7709b250bed7a9c17>
> 2018-10-26 21:05:47.290	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <69ad22be313023933a793e493ef06c6e4d8d8bdbeaa8a4c1aaaa09a2f7718641>, mask <83c2e47c348c7f69c0b158d9dd083ecfeac4cf8663751e2306f39f96d3c70cfc>, txid <3ad84097f2e5947a4e61207893c75ab93f7d42be4784dd6175c18519ba6254dd>
> 2018-10-26 21:05:47.290	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <e2a63f0c8d1987f1835854b81779d9d7bf5f42b7d98e112e09fb212271559587>, mask <68b2719442d9fe099005bc82cb28583ce80d647331537c0002814dad0bd35e41>, txid <202a5b0b94730aaac46de18deff00fb69aab0f9c9002cd7a53edfb170a1d9302>
> 2018-10-26 21:05:47.290	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <fed20205fb12f10a8a3afb5d92c6f0f606ebb9e5d2ade2039f3c80ce68ceb860>, mask <f92eccc966bb93af37bbc272e364625a0fbea9aa366dd078fa834954af6d60a3>, txid <991e57f36690858a6ac9c302a00b9e9687efb5ea3ab67c3860d5723097694348>
> 2018-10-26 21:05:47.290	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <68ec23d4e8b64d40a657490037eb7f3752b3dff80af6a473e4d68037eb8819fb>, mask <e2e5a3e334c452268322dda88fd4167838bbea6a642d452ced5e9346d5f360de>, txid <7b83b3c88e4dd87f0cd49fd72b7c473238c5b4bb49eeaca5698da88ce037c736>
> 2018-10-26 21:05:47.290	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <62e630ca48e6a4fe91d196f4b31b64431db015f6022e51346292875642ae8c01>, mask <449461fb6dfa013f40a29b61f8c2b8ba4147aef109c0f22462e266d5d51cc012>, txid <9e686693ad145369ab49c3751c67633e71202ccb48b7c98f16cdf7af0947110b>
> 2018-10-26 21:05:47.290	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <859e19cb3072ec9150095b0f6b4617bd0630153584eb2b3904a70407d9681571>, mask <92cc0cb166b09a49003ac7f41dab198652a5047aec53be60f371affe55d58b3f>, txid <d27dd62dad28d5537fcc47751b274106429efa308fa80e6c5dfe551e165c76ac>
> 2018-10-26 21:05:47.290	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <2a225d47a14cfc73aac55842aab520ef46a0aabcce87fa7d83c852f4c1017b0b>, mask <0de896001e8d6d3a65bb8a8a6c8957fd0bf8f6c06d401e413b5df0b241307eca>, txid <80791cdcca105fe91619888ce4d589c461e827adc700cac27cea8aaa901d2f28>
> 2018-10-26 21:05:47.290	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <bcf3c11788a606ef6dfce1025f4c7a738423ecee5a6ba12e95b3d44febe3eceb>, mask <2ff95b0540ed2c77f9c7086eb264f68110eb5099ea216e33937e62572085d1ef>, txid <87fff85cf47524e0be93e367c891fb619b580690b37c5fcbfa9f1bf57ae74c21>
> 2018-10-26 21:05:47.290	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <00e137bbc51cc48c4fe4336a5e2a50dc009bae1381c2bfed040ee7ac88e04733>, mask <0810c53461a8d9a945cffd8b386879b621ec9ae8b4ba0442fcf06cc8a499921a>, txid <2ff7c8dcc98bc291b2f045be22f5c295f99cc672d6cd38596d8cf6aec0944d30>
> 2018-10-26 21:05:47.290	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <f232f4d1994acda464769f83b4d0e68d3780e20f8bc9adc978141fa20a94fc08>, mask <86a7ae9232d03044910689ff8617fd895dc0f69ce14bcfd454430c534af01e84>, txid <cbf8f2efe4588d4dc70beefd6444cd33e35184b7b9608bef18212dfe81b90b05>
> 2018-10-26 21:05:47.290	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <e157bc9993c105594cdcbeb5c0a421d28fc184d4e18b3915bb41424b35bd5636>, mask <7b049fa756310df9685611cb3e6cdb3413099e82960500d7879c62de6f0956c2>, txid <3fa201f977b21cab895a1bac0041f5b6ab447c55a85c99a281ecfa9c09261ed1>
> 2018-10-26 21:05:47.290	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <0c75912cef9ee8973839e045fb9eeafd6b06407806df4ac4247dce7ab8784bb6>, mask <110a318900efa3303354d8d61fa19e523675c796d1534a46edb76fc69add1a42>, txid <69d84c39dc66feb726f3931a3d1a4552d1762acb043772700a467a52e8a05808>
> 2018-10-26 21:05:47.290	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <fbc2193acee444fac83a28bc61c18ec9d32deff23c26b038af6d7cc17b94d92a>, mask <624f01e18ece7752778abb9c71c4da881ff01680c19838be0b4ec6724d0577cf>, txid <f7662353cda05940d22a8f8c5cbbb0be7b6b3a17bbc5844d98752f0f0b9d2b14>
> 2018-10-26 21:05:47.290	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <78ccddb69356c211bc8ac45ef77e67de42d096c299593c7c22aa53bf6d7d113d>, mask <b85b2ad4e5b8f054032df4fbccfae55c2e2b082565fdb2df8b6d3992b37e51b6>, txid <3f1ba7102853ce92001666018590b1a5d5570faed741980b4537e596af22f111>
> 2018-10-26 21:05:47.290	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <dfe446026970e43075456aa3655fb9b4b944e3df2b0d1d32bcb54d4757d6f81c>, mask <7dcf74f48f87c417c219204c2c7022b21f23491128eb5eb9dbe7ca6cc6fee30d>, txid <b311fe790ef1cdd09bc0efd68e5a6313dc0438f802fca4c506efab9cb9b98cef>
> 2018-10-26 21:05:47.290	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <22ec545572ec7f1572f070bfd1dbfc0bd1b56cada382a0bb06014b61f9fe61f7>, mask <1c3741aef02cc62717d7b6a10ed522086e8a82a940bdd2e9d1372e5e937f1a95>, txid <31fb1ee685e5cb2179b3a1735a17988323650f80c808faf57dc95c2a7535ee78>
> 2018-10-26 21:05:47.290	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <55154133db65e2763528954cf9375748f4cfc5505e5d90677ac1596ca729cedb>, mask <5612f1b27252598fa8e2054d68a5656b8fadfa847bd0c016c2b3854ed6e59cc7>, txid <bfc99f30aebb31fbb06a2c4291a1d059c313cf32d49389032ed409a4c33fdb72>
> 2018-10-26 21:05:47.290	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <446ff26426d8fae213d375221bb2ddfd3cc40d116d7969aa11c80de85daaeced>, mask <2f2cfbbadadd15b6d66a4b95856d14a3e9e0312de1e76e412458170c30950f09>, txid <eb1e796657f82201073a6d32c08c0e01a884653c37fd1cf32451aba6f2716d7a>
> 2018-10-26 21:05:47.290	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <792e29b3b510d6ec620bf2bc99596f592a2c5abd42ead3ca172042a777556565>, mask <bea493cd4295c895f92ef84d2c245e302f01ad18492777a2633f0d4d14f7187b>, txid <e6122687e9b24330dc499b4c3e2d3f77b9d5b973ddda771b44562d27188b0c69>
> 2018-10-26 21:05:47.290	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <8855a8ffc2bdf327d4eda479cf976f14e5b96ae14dfe3d35c4a3eac0865bbdc1>, mask <dd09c265d2f8603809bcc44313349848426ef7c038dc86dc89d84f6c40b10908>, txid <4d009a6fcaf01b1b7dcbf8fbe545c526686381752770c22bceae339f277dca12>
> 2018-10-26 21:05:47.290	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <1211b1c7c41d7138b2f8a3c093e996c238b2efe930a25394965f7e061221dd02>, mask <235318417b1b0692fa052f0ec9c61fd72d94a369cfeb521213991ad8e5aa437c>, txid <e8d4253e59209929a9d081c127faaadc5d749c39e375ae820060b4d412443439>
> 2018-10-26 21:05:47.290	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <0624f17f9fc540c38bd987f25505e64f12a54c8133c224fa446e09684e8deef1>, mask <992242100f05298e41b281f17850c4a37a1bbfbc7188d4f2b326141bed61e022>, txid <3eed32d6bc5c584a9baa7ebe2fa503d98841b0d91bc34585872ffee025fb87c2>
> 2018-10-26 21:05:47.290	  0x7fffb0d4e380	INFO 	global	src/wallet/wallet2.cpp:7168	key <b8044a2fd8e5939da1e69c8d8010e0a5514b5fbf357e20e2b43eb4bde0ccb9ea>, mask <2ae32f9eb8d648e9609c2e38651d9c299668bbef1a5f8004e2ae56db59fbf8e2>, txid <fe03f894590c9c08a715932b8a66ad24582faad8f9d330f9edeead7a1d79ba0e>

## moneromooo-monero | 2018-10-26T22:14:57+00:00
Looks like github mangled that log. Can you please paste it to fpaste.org or paste.debian.net and post hte URL here ?

## kr1-ch | 2018-10-26T22:28:18+00:00
https://paste.fedoraproject.org/paste/MT8Zy0VX0UrDWaQ1MzcOiw

## iDunk5400 | 2018-10-27T09:11:19+00:00
You received that 22.77 in May using GUI v0.11.1.0, right ? If so, what you have in that wallet is not Monero (XMR).

## kr1-ch | 2018-10-27T09:40:14+00:00
I received 21.77 moneros (XMR) on 16th May. I don't remember if I used the GUI or if this payment was from an exchange. I can investigate if it's important.

If it's not moneros, what is this?? 

## iDunk5400 | 2018-10-27T09:49:11+00:00
If you were still using v0.11.x.x in May, and hadn't upgraded to v0.12.x.x, the funds you received were not Monero (XMR), which was at v7 block version at the time, but some other forked coin like XMV/XMC/XMO/XMwhatever that forked Monero's v6 blockchain.

## kr1-ch | 2018-10-27T14:28:35+00:00
OK, so on May 16th I sent moneros (or whatever it's, I thought it was XMR) to this wallet using GUI v0.11.1.0. 

I checked the wallet I used to send these moneros, and actually there is almost the same amount (with fees) in this wallet (I was expecting this wallet to be empty), which seems to indicate that moneros (XMR) are still in this wallet.

![screenshot 2018-10-27 at 16 24 16](https://user-images.githubusercontent.com/11709283/47605283-d0a50480-da04-11e8-8ea1-79e10b67f90c.png)

I can't see the order in history, but I'm pretty sure I used this wallet on May.

So, I tried to transfer with this one and the transaction was good. But now the transaction is PENDING for at least one hour and the balance is not completely unlocked.



 

## iDunk5400 | 2018-10-27T14:55:38+00:00
If it was you who sent the original amount from wallet A to wallet B, and your wallet A had that amount before block 1546000, your Monero (XMR) funds are still in wallet A, as you have already noticed. That is because, as far as Monero network is concerned, that transfer on 16th May never happened. Funds in wallet B cannot be used on Monero blockchain.

As to why your most recent transfer from wallet A never made it to the txpool, try to see if the tx is still in your daemon's txpool. `print_pool_sh` and find your txid there. If you can see it, try `relay_tx <txid>`, where \<txid\> is your 7bd9... txid.

## iDunk5400 | 2018-10-27T15:11:02+00:00
That seems to have worked. Your tx [has been mined](https://xmrchain.com/tx/7bd9fcc57df92a8f98d31127a04a2d5567a2d13884f0827ccc28c9bc2ab74600).

## kr1-ch | 2018-10-27T15:23:18+00:00
Yeah thank you so much for your help! :)

# Action History
- Created by: kr1-ch | 2018-10-24T20:30:35+00:00
- Closed at: 2018-10-27T15:27:37+00:00
