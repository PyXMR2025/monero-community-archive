---
title: monero-gui-osx-10.11 build crash
source_url: https://github.com/monero-project/monero-gui/issues/2139
author: Afron-Lysias
assignees: []
labels:
- resolved
created_at: '2019-05-01T00:15:10+00:00'
updated_at: '2019-05-05T01:18:35+00:00'
type: issue
status: closed
closed_at: '2019-05-05T01:18:35+00:00'
---

# Original Description
For the last few weeks I have been testing monero-gui-osx-10.11 builds on a mac without brew (on purpose). 
Any build newer than #1682 crashes for the following reason:

Dyld Error Message:   Library not loaded: /usr/local/Cellar/openssl/1.0.2q/lib/libcrypto.1.0.0.dylib

Since this was a problem that created a lot of confusion during the previous version update, I open this issue as an alert to make shure that this time we can avoid similar mistakes in the final version.

# Discussion History
## selsta | 2019-05-01T00:30:00+00:00
Could you check https://build.getmonero.org/downloads/monero-wallet-gui-ff6ce62-osx-10.12.zip ?

## Afron-Lysias | 2019-05-01T07:04:04+00:00
This is an osx-10.12 build. I'm testing exclusively osx-10.11 builds. 
I have tested ALL new osx-10.11 builds since #1682.

Test Results for monero-wallet-gui-ff6ce62-osx-10.12:
Application: Runs
Wallet: Opens
Daemon: Failed to start

`[RPC0]	ERROR	net.ssl	contrib/epee/src/net_ssl.cpp:388	SSL handshake failed, connection dropped: no shared cipher
 `

## xiphon | 2019-05-01T15:41:05+00:00
@Afron-Lysias 
 
> Daemon: Failed to start

Did you try to start `monerod` with `monero-wallet-gui-ff6ce62-osx-10.12.zip` and it crashed right after the start?

## Afron-Lysias | 2019-05-01T19:57:30+00:00
Yes, I started monerod within monero-wallet-gui-ff6ce62-osx-10.12. 
GUI itself didn't crash. The daemon just failed to start.

## dEBRUYNE-1 | 2019-05-01T20:15:33+00:00
Could you open a separate issue for that daemon failed to start issue on the main repository (i.e. https://github.com/monero-project/monero/issues)?

## Afron-Lysias | 2019-05-03T23:02:33+00:00
Regarding "monero-wallet-gui-ff6ce62-osx-10.12" problem, aren't issues expected, since I'm running an older macOS (10.11) than required, according to the file name?

## xiphon | 2019-05-03T23:20:04+00:00
> Regarding "monero-wallet-gui-ff6ce62-osx-10.12" problem, aren't issues expected, since I'm running an older macOS (10.11) than required, according to the file name?

Nope. is static build, there was a good chance it might get working on 10.11. Usually OS dumps some error message and details in the console output like seg fault or library loading error, for example.

Anyway working on static 10.11 build now. Will let you know once it is ready.

## Afron-Lysias | 2019-05-04T00:21:00+00:00
Here it is:
https://github.com/monero-project/monero-gui/issues/2159

## xiphon | 2019-05-04T15:46:00+00:00
@Afron-Lysias 
Please check this one https://build.getmonero.org/downloads/monero-wallet-gui-3c1fe1da-osx-10.11.zip

## Afron-Lysias | 2019-05-04T18:24:21+00:00
@xiphon 
This version is OK. Everything is back to normal, plus the white light theme.

## Afron-Lysias | 2019-05-04T18:36:17+00:00
This version has also fixed this problem:
https://github.com/monero-project/monero-gui/issues/1459

## selsta | 2019-05-05T01:09:19+00:00
+resolved

# Action History
- Created by: Afron-Lysias | 2019-05-01T00:15:10+00:00
- Closed at: 2019-05-05T01:18:35+00:00
