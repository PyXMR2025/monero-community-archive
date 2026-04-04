---
title: 'Cannot use Ledger-based wallet: "Invalid Password"'
source_url: https://github.com/monero-project/monero-gui/issues/3088
author: Apy17750
assignees: []
labels:
- bug
created_at: '2020-09-14T18:46:44+00:00'
updated_at: '2021-04-22T03:38:43+00:00'
type: issue
status: closed
closed_at: '2021-04-22T03:38:43+00:00'
---

# Original Description
I am attempting to create a new wallet from a hardware Ledger device (Nano X) using the Monero GUI (v0.16.0.3 - Nitrogen Nebula, though I also encounted this issue on 0.16.0.2) on macOS (v10.15.6). I followed the steps [here](https://monero.stackexchange.com/questions/9901/how-do-i-generate-a-ledger-monero-wallet-with-the-gui-monero-wallet-gui).

I can successfully create the wallet and set any password; however, I consistently receive the following error while attempting to open the wallet:


<img width="462" alt="image" src="https://user-images.githubusercontent.com/71286826/93124624-bcad2f00-f67e-11ea-97dc-0fa07169f257.png">

I've tried setting & opening with:
* No password
* The letter 'a'
* A random password, copied & pasted both times

I've tried both the restore & the create new wallet options, and both have this issue. I found a [Reddit thread](https://www.reddit.com/r/monerosupport/comments/hxqv2m/monero_gui_and_ledger_invalid_password/) where a Windows user is describing a similar issue.

Steps to reproduce:
1. Open a new Monero wallet on the Ledger device
2. Attempt to create or restore a wallet from a hardware device in the Monero GUI
3. Set any passphrase
4. Attempt to open the wallet (which happens automatically)

# Discussion History
## selsta | 2020-09-16T01:27:16+00:00
Does this only happen when creating a Ledger wallet?

## cryptonaus | 2020-09-16T16:52:07+00:00
I haven't tested with Trezor devices, but choosing the "Create a new wallet" option works without issues.

## selsta | 2020-09-21T01:07:59+00:00
> Steps to reproduce:

Sadly I’m not able to reproduce with Ledger on macOS. Anything else that you would call special with your setup?

## cryptonaus | 2020-09-25T21:24:17+00:00
The only other thing that I've done specially was select the advanced bootstrap mode. Otherwise, it was a fresh install of Monero GUI & Monero on the device itself. Perhaps the latter has been updated since then; I'll try again.

## noterminusgit | 2021-02-19T05:53:22+00:00
I'm having the same issue on Linux. This is a new device, fresh install of everything, and the only custom parameter is I'm using a "remote" node running locally in another process, so the daemon isn't dependent on the GUI application.

Ubuntu 20.04.2
Ledger Nano X FW 1.2.4-5
Ledger App Version 1.7.5
monero-gui v0.17.1.9

Here's some syslog output:
Feb 18 21:46:03 x org.gnome.Nautilus[21216]: 2021-02-19 05:46:03.018#011I [PARSE URI] regex not matched for uri: ^((.?)://)?([(.)](:(\d+))?)(.*)?
Feb 18 21:46:41 x org.gnome.Nautilus[21216]: 2021-02-19 05:46:41.285#011W SSL peer has not been verified
Feb 18 21:46:41 x org.gnome.Nautilus[21216]: 2021-02-19 05:46:41.482#011I ~WalletImpl
Feb 18 21:46:41 x org.gnome.Nautilus[21216]: 2021-02-19 05:46:41.482#011I closing wallet...
Feb 18 21:46:41 x org.gnome.Nautilus[21216]: 2021-02-19 05:46:41.482#011I Calling wallet::stop...
Feb 18 21:46:41 x org.gnome.Nautilus[21216]: 2021-02-19 05:46:41.482#011I wallet::stop done
Feb 18 21:46:41 x org.gnome.Nautilus[21216]: 2021-02-19 05:46:41.483#011I Generating SSL certificate
Feb 18 21:46:41 x org.gnome.Nautilus[21216]: 2021-02-19 05:46:41.484#011I ~WalletImpl finished
Feb 18 21:46:41 x org.gnome.Nautilus[21216]: 2021-02-19 05:46:41.487#011I ringdb path set to /home/x/.shared-ringdb
Feb 18 21:46:48 x org.gnome.Nautilus[21216]: 2021-02-19 05:46:48.728#011E portable_storage: wrong binary format - signature mismatch
Feb 18 21:46:48 x org.gnome.Nautilus[21216]: 2021-02-19 05:46:48.729#011E !r. THROW EXCEPTION: error::invalid_password
Feb 18 21:46:48 x org.gnome.Nautilus[21216]: 2021-02-19 05:46:48.730#011W /monero-gui/monero/src/wallet/wallet2.cpp:4353:N5tools5error16invalid_passwordE: invalid password
Feb 18 21:46:48 x org.gnome.Nautilus[21216]: 2021-02-19 05:46:48.731#011E Error opening wallet: invalid password
Feb 18 21:46:48 x org.gnome.Nautilus[21216]: 2021-02-19 05:46:48.744#011E Error opening wallet with password: invalid password

That's all the detail I can find about the issue. If there's another log, or a way to launch the application with more extensive logs, I'll be happy to share those as well.

EDIT: I've found the monero-wallet-gui.log. Here's some output from that. It looks like the times were adjusted to UTC. I'm in PST.

2021-02-19 06:13:41.396	    7f98364ba700	INFO	net.ssl	contrib/epee/src/net_ssl.cpp:131	Generating SSL certificate
2021-02-19 06:13:54.437	    7f9837d39800	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:INFO,global:INFO,stacktrace:INFO,logging:INFO,msgwriter:INFO,perf.*:DEBUG
2021-02-19 06:13:54.439	    7f97fa989700	INFO	net	contrib/epee/include/net/net_parse_helpers.h:141	[PARSE URI] regex not matched for uri: ^((.*?)://)?(\[(.*)\](:(\d+))?)(.*)?
2021-02-19 06:13:54.441	    7f97fa989700	INFO	net.ssl	contrib/epee/src/net_ssl.cpp:131	Generating SSL certificate
2021-02-19 06:13:54.552	    7f9836cbb700	INFO	WalletAPI	src/wallet/api/wallet.cpp:453	~WalletImpl
2021-02-19 06:13:54.553	    7f9836cbb700	INFO	WalletAPI	src/wallet/api/wallet.cpp:770	closing wallet...
2021-02-19 06:13:54.553	    7f9836cbb700	INFO	WalletAPI	src/wallet/api/wallet.cpp:781	Calling wallet::stop...
2021-02-19 06:13:54.553	    7f9836cbb700	INFO	WalletAPI	src/wallet/api/wallet.cpp:783	wallet::stop done
2021-02-19 06:13:54.553	    7f9836cbb700	INFO	WalletAPI	src/wallet/api/wallet.cpp:466	~WalletImpl finished
2021-02-19 06:13:54.555	    7f9836cbb700	INFO	wallet.wallet2	src/wallet/wallet2.cpp:7622	ringdb path set to /home/x/.shared-ringdb
2021-02-19 06:14:02.356	    7f9836cbb700	ERROR	net.http	contrib/epee/include/storages/portable_storage.h:173	portable_storage: wrong binary format - signature mismatch
2021-02-19 06:14:02.357	    7f9836cbb700	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:4353	!r. THROW EXCEPTION: error::invalid_password
2021-02-19 06:14:02.357	    7f9836cbb700	WARNING	net.http	src/wallet/wallet_errors.h:896	/monero-gui/monero/src/wallet/wallet2.cpp:4353:N5tools5error16invalid_passwordE: invalid password
2021-02-19 06:14:02.357	    7f9836cbb700	ERROR	WalletAPI	src/wallet/api/wallet.cpp:719	Error opening wallet: invalid password
2021-02-19 06:14:02.362	    7f9837d39800	ERROR	frontend	src/wallet/api/wallet.cpp:416	Error opening wallet with password:  invalid password


I should note that I just created the wallet on the Ledger with this same configuration immediately before having this issue when trying to open the wallet.

## selsta | 2021-02-19T23:03:14+00:00
@gitfreebeer Thanks for the logs, "Wrong binary format - signature mismatch" might be interesting.

## selsta | 2021-02-19T23:51:03+00:00
@gitfreebeer could you please also test if you can open the wallet fine with monero-wallet-cli?

## noterminusgit | 2021-02-22T04:19:51+00:00
@selsta the CLI application worked. The GUI still does not. It doesn't even prompt for the key export before it fails.

...on this PC.

On another Linux box, with the same software, the GUI application opens this wallet fine. All the software, including the blockchain and the wallet file, were copied over from one to the other.

## moneromooo-monero | 2021-03-05T00:08:03+00:00
If you can run with this patch to monero-wallet-gui, can you:
- run with --log-level 2
- NOT paste the logs, as they'll contain your secret keys
- Look for a line starting with "Decrypted with chacha20", and one with "Decrypted with chacha8" (the latter might not be there)
- Check whether the data on the last of these lines look like JSON, similar to: {"key_data":"......
- Whether the log contains a line with "Keys file has wrong format"


```
diff --git a/src/wallet/wallet2.cpp b/src/wallet/wallet2.cpp
index d4727f957..0f6d2f45e 100644
--- a/src/wallet/wallet2.cpp
+++ b/src/wallet/wallet2.cpp
@@ -4214,11 +4214,16 @@ bool wallet2::load_keys_buf(const std::string& keys_buf, const epee::wipeable_st
   std::string account_data;
   account_data.resize(keys_file_data.account_data.size());
   crypto::chacha20(keys_file_data.account_data.data(), keys_file_data.account_data.size(), key, keys_file_data.iv, &account_data[0]);
+MGINFO("Decrypted with chacha20: " << account_data);
   if (json.Parse(account_data.c_str()).HasParseError() || !json.IsObject())
+  {
     crypto::chacha8(keys_file_data.account_data.data(), keys_file_data.account_data.size(), key, keys_file_data.iv, &account_data[0]);
+MGINFO("Decrypted with chacha8: " << account_data);
+  }
   // The contents should be JSON if the wallet follows the new format.
   if (json.Parse(account_data.c_str()).HasParseError())
   {
+    MERROR("Keys file has wrong format");
     is_old_file_format = true;
     m_watch_only = false;
     m_multisig = false;
@@ -4517,6 +4522,9 @@ bool wallet2::load_keys_buf(const std::string& keys_buf, const epee::wipeable_st
     return false;
   }
 
+MGINFO("account_data (len): " << account_data.size());
+MGINFO("account_data (hex): " << epee::string_tools::buff_to_hex_nodelimer(account_data));
+MGINFO("account_data (raw): " << account_data);
   r = epee::serialization::load_t_from_binary(m_account, account_data);
   THROW_WALLET_EXCEPTION_IF(!r, error::invalid_password);
   if (m_key_device_type == hw::device::device_type::LEDGER || m_key_device_type == hw::device::device_type::TREZOR) {
```

## noterminusgit | 2021-03-25T00:54:32+00:00
@moneromooo-monero, I'm not sure what to do with that code. I've checked out tags/v0.17.1.9 on a local repo, but where do I apply the code? I assume I'm supposed to compile from source with that code pasted somewhere?

## selsta | 2021-03-25T14:25:41+00:00
@gitfreebeer  try

```
cd monero-gui/monero
patch -p1 < /path/to/patch
cd ..
mkdir build
cd build
cmake -D MANUAL_SUBMODULES=ON ..
make -j2
```

## fabiobfava | 2021-04-19T19:57:12+00:00
> > Steps to reproduce:
> 
> Sadly I’m not able to reproduce with Ledger on macOS. Anything else that you would call special with your setup?

I'm using Monero-GUI-Mac version 0.17.2.1 and this issue persists. The wallet can be created and password set, but Monero-GUI-Mac cannnot open the wallet, may it be created by itself or monero-wallet-cli, wich is actually not working very well, it freezes after connecting to the Ledger and never stops "Refreshing..." 


## selsta | 2021-04-19T19:58:33+00:00
> it freezes after connecting to the Ledger and never stops "Refreshing..."

Did you export your view key?

## fabiobfava | 2021-04-19T20:00:44+00:00
Can't understand what you mean. It's a Ledger wallet.

## selsta | 2021-04-19T20:01:35+00:00
Did you accept exporting the view key on the Ledger device after opening your wallet?

## fabiobfava | 2021-04-19T20:01:56+00:00
No, but it works this way. Sometimes it freezes.

## selsta | 2021-04-19T20:02:55+00:00
> No, but it works this way. Sometimes it freezes.

You have to accept exporting the view key. The Ledger device is not strong enough to do all calculations on device so it will freeze.

## fabiobfava | 2021-04-19T20:05:57+00:00
Ok I'll try it now. No problem on reduced privacy?


## selsta | 2021-04-19T20:10:17+00:00
At worst someone could see your incoming transactions if they hacked your computer. But if your computer is hacked they can see your incoming transactions anyway once you open the wallet.

## fabiobfava | 2021-04-19T20:13:58+00:00
Nobody has hacked my pc. Thank you for the infos it's now working and very fast! Thanks!

On the other hand, Monero-GUI (Mac) cannot open the Ledger wallet. Any provisional date for having this fixed?

## selsta | 2021-04-19T20:15:07+00:00
> On the other hand, Monero-GUI (Mac) cannot open the Ledger wallet.

None of the devs were able to reproduce this yet. Until then not a lot we can do :/

## fabiobfava | 2021-04-19T20:32:59+00:00
Well, I have never managed to open my Ledger Monero wallet using Monero-GUI. The Application says the password is invalid. I've never found any solution to that, just using the monero-wallet-cli instead. But I'd rather prefer using the Monero-GUI. Not sure why this happens, the wallet and the keys just work.

## selsta | 2021-04-19T22:33:24+00:00
ping @gitfreebeer Do you maybe have time to compile moneromooo's diff? https://github.com/monero-project/monero-gui/issues/3088#issuecomment-806847524

It would be great help for us to potentially find this issue.

## fabiobfava | 2021-04-19T23:02:50+00:00
Thank you @selsta for looking a bit deeper into this. It's really impossible to open a wallet on my Ledger Nano X from the Monero-GUI-Mac. I can open it via Monero-GUI-Win64 and Monero-Wallet-CLI, but as a Mac-user since my childhood, I'd rather prefer to just open via Monero-GUI-Mac. Thanks folks!

Mac OS 10.14.6 Mojave - Monero-GUI-Mac latest version

## noterminusgit | 2021-04-20T03:29:46+00:00
> @gitfreebeer try
> 
> ```
> cd monero-gui/monero
> patch -p1 < /path/to/patch
> cd ..
> mkdir build
> cd build
> cmake -D MANUAL_SUBMODULES=ON ..
> make -j2
> ```

@selsta I get an error that it can't find the file from line 5. It seems that it's looking for the wallet file? Is that correct?

> ~/Downloads/monero-gui/monero$ patch -p1 < ~/Downloads/monero-patch 
> can't find file to patch at input line 5
> Perhaps you used the wrong -p or --strip option?
> The text leading up to this was:
> --------------------------
> |diff --git a/src/wallet/wallet2.cpp b/src/wallet/wallet2.cpp
> |index d4727f957..0f6d2f45e 100644
> |--- a/src/wallet/wallet2.cpp
> |+++ b/src/wallet/wallet2.cpp
> --------------------------
> File to patch: ^C
> ~/Downloads/monero-gui/monero$

## selsta | 2021-04-20T04:23:47+00:00
@gitfreebeer Did you save

```
diff --git a/src/wallet/wallet2.cpp b/src/wallet/wallet2.cpp
index d4727f957..0f6d2f45e 100644
--- a/src/wallet/wallet2.cpp
+++ b/src/wallet/wallet2.cpp
@@ -4214,11 +4214,16 @@ bool wallet2::load_keys_buf(const std::string& keys_buf, const epee::wipeable_st
   std::string account_data;
   account_data.resize(keys_file_data.account_data.size());
   crypto::chacha20(keys_file_data.account_data.data(), keys_file_data.account_data.size(), key, keys_file_data.iv, &account_data[0]);
+MGINFO("Decrypted with chacha20: " << account_data);
   if (json.Parse(account_data.c_str()).HasParseError() || !json.IsObject())
+  {
     crypto::chacha8(keys_file_data.account_data.data(), keys_file_data.account_data.size(), key, keys_file_data.iv, &account_data[0]);
+MGINFO("Decrypted with chacha8: " << account_data);
+  }
   // The contents should be JSON if the wallet follows the new format.
   if (json.Parse(account_data.c_str()).HasParseError())
   {
+    MERROR("Keys file has wrong format");
     is_old_file_format = true;
     m_watch_only = false;
     m_multisig = false;
@@ -4517,6 +4522,9 @@ bool wallet2::load_keys_buf(const std::string& keys_buf, const epee::wipeable_st
     return false;
   }
 
+MGINFO("account_data (len): " << account_data.size());
+MGINFO("account_data (hex): " << epee::string_tools::buff_to_hex_nodelimer(account_data));
+MGINFO("account_data (raw): " << account_data);
   r = epee::serialization::load_t_from_binary(m_account, account_data);
   THROW_WALLET_EXCEPTION_IF(!r, error::invalid_password);
   if (m_key_device_type == hw::device::device_type::LEDGER || m_key_device_type == hw::device::device_type::TREZOR) {
```

as monero-patch? The patch command works here.

## selsta | 2021-04-20T07:44:04+00:00
@gitfreebeer You have to clone monero-gui first like this:

```
git clone --recursive https://github.com/monero-project/monero-gui
```

and then do the steps in my comment.

## selsta | 2021-04-20T16:00:58+00:00
@fabiobfava Can you confirm that KDF rounds says 1 on your Mac?

<img width="1026" alt="Screenshot 2021-04-20 at 18 00 38" src="https://user-images.githubusercontent.com/7697454/115428084-51be6a80-a202-11eb-9624-2941916762e0.png">


## fabiobfava | 2021-04-20T17:30:59+00:00
Yes @selsta it says 1 KDF round.

## selsta | 2021-04-20T18:54:19+00:00
@fabiobfava 

Can you select the `1` inside KDF rounds field, change it to `2` and then immediately after select and change it back to `1`? Afterwards please try to reopen the Ledger wallet.

## fabiobfava | 2021-04-20T19:37:49+00:00
Hey @selsta it works! I can now open my Ledger wallet on the Monero-GUI-Mac! Thank you so much!

## selsta | 2021-04-20T19:39:15+00:00
Thanks for confirming.

@gitfreebeer https://github.com/monero-project/monero-gui/issues/3088#issuecomment-823522464 should also resolve your issue.

## noterminusgit | 2021-04-22T03:28:40+00:00
> Thanks for confirming.
> 
> @gitfreebeer [#3088 (comment)](https://github.com/monero-project/monero-gui/issues/3088#issuecomment-823522464) should also resolve your issue.

It does fix the issue for me.

# Action History
- Created by: Apy17750 | 2020-09-14T18:46:44+00:00
- Closed at: 2021-04-22T03:38:43+00:00
