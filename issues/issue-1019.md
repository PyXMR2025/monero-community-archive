---
title: '[SE] Simplewallet: failed to load wallet: basic_string::resize'
source_url: https://github.com/monero-project/monero/issues/1019
author: JamesCullum
assignees: []
labels: []
created_at: '2016-08-30T16:11:36+00:00'
updated_at: '2016-09-23T05:49:51+00:00'
type: issue
status: closed
closed_at: '2016-09-21T18:31:09+00:00'
---

# Original Description
Issue regarding this SE post: http://monero.stackexchange.com/questions/1380/wallet-initialization-failed-basic-stringresize

**Requisites**
-  Enterprise Laptop: Win 7 Enterprise SP1, Intel i5-3220M @ 2.60GHz, 8GB Ram, 32bit
- Unrestricted Wifi but sometimes enterprise network. No admin access, only r/w access to C:\Temp
- Throwaway demo-wallet created via MyMonero.com

> seed: fugitive orange ruling jazz pedantic lynx utopia duration broken vogue peaches wildly pedantic
> adr: 48hY1ykp48SAeqjZL8TaM8iKD78BuTWbMdVpvkzsSnQiTvhxVoZRvaoB9oYVbuEoFTfCAjzCPG8sNTGzYSWcfEmyGF8eDfR
> spend: 62cd442da77ec50a51c08d2059a97a29a88bb92c53d49d37aa100ad6ce974003
> view: eec2b6788f78eda160f44932ee6abcc2f413cae3553a9ed2c0c4511648af490d
> wallet pass below: helloworld

**CMD Log**

> Microsoft Windows [Version 6.1.7601]
> Copyright (c) 2009 Microsoft Corporation. Alle Rechte vorbehalten.
> 
> C:\Users[winName]>cd C:\Temp\Monero
> 
> C:\Temp\Monero>simplewallet --generate-from-keys demo
> Creating the logger system
> Monero 'Hydrogen Helix' (v0.9.3.0-release)
> Logging at log level 0 to C:\Temp\Monero\simplewallet.log
> password: **********
> Standard address: 48hY1ykp48SAeqjZL8TaM8iKD78BuTWbMdVpvkzsSnQiTvhxVoZRvaoB9oYVbu
> EoFTfCAjzCPG8sNTGzYSWcfEmyGF8eDfR
> Spend key: 62cd442da77ec50a51c08d2059a97a29a88bb92c53d49d37aa100ad6ce974003
> View key: eec2b6788f78eda160f44932ee6abcc2f413cae3553a9ed2c0c4511648af490d
> Generated new wallet: 48hY1ykp48SAeqjZL8TaM8iKD78BuTWbMdVpvkzsSnQiTvhxVoZRvaoB9o
> YVbuEoFTfCAjzCPG8sNTGzYSWcfEmyGF8eDfR
> [wallet 48hY1y]: exit
> 
> C:\Temp\Monero>simplewallet --wallet-file demo --password helloworld --daemon-ho
> st node.moneroclub.com --daemon-port 8880
> Creating the logger system
> Monero 'Hydrogen Helix' (v0.9.3.0-release)
> Logging at log level 0 to C:\Temp\Monero\simplewallet.log
> Error: failed to load wallet: basic_string::resize
> 
> C:\Temp\Monero>simplewallet --wallet-file demo --password helloworld --daemon-ho
> st node.monero.net --daemon-port 13666
> Creating the logger system
> Monero 'Hydrogen Helix' (v0.9.3.0-release)
> Logging at log level 0 to C:\Temp\Monero\simplewallet.log
> Error: failed to load wallet: basic_string::resize

**simplewallet.log**

> 2016-Aug-30 17:52:35.548438 Monero 'Hydrogen Helix' (v0.9.3.0-release)
> 2016-Aug-30 17:52:35.548438 Setting log level = 0
> 2016-Aug-30 17:52:35.548438 default_log: C:\Temp\Monero\simplewallet.log
> 2016-Aug-30 17:52:35.548438 Logging at log level 0 to C:\Temp\Monero\simplewallet.log
> 2016-Aug-30 17:53:49.431438 ERROR C:/msys32/DISTRIBUTION-BUILD/contrib/epee/include/net/http_client.h:867 failed to connect localhost:18081
> 2016-Aug-30 17:53:49.431438 ERROR C:/msys32/DISTRIBUTION-BUILD/src/wallet/wallet2.cpp:564 !r. THROW EXCEPTION: error::no_connection_to_daemon
> 2016-Aug-30 17:53:49.431438 C:/msys32/DISTRIBUTION-BUILD/src/wallet/wallet2.cpp:564:N5tools5error23no_connection_to_daemonE: no connection to daemon, request = getblocks.bin
> 2016-Aug-30 17:55:41.352438 Monero 'Hydrogen Helix' (v0.9.3.0-release)
> 2016-Aug-30 17:55:41.352438 Setting log level = 0
> 2016-Aug-30 17:55:41.352438 default_log: C:\Temp\Monero\simplewallet.log
> 2016-Aug-30 17:55:41.352438 Logging at log level 0 to C:\Temp\Monero\simplewallet.log
> 2016-Aug-30 17:55:41.415438 Loaded wallet keys file, with public address: 48hY1ykp48SAeqjZL8TaM8iKD78BuTWbMdVpvkzsSnQiTvhxVoZRvaoB9oYVbuEoFTfCAjzCPG8sNTGzYSWcfEmyGF8eDfR
> 2016-Aug-30 17:55:41.475438 Error: failed to load wallet: basic_string::resize
> 2016-Aug-30 17:55:41.476438 ERROR C:/msys32/DISTRIBUTION-BUILD/src/simplewallet/simplewallet.cpp:1006 failed to open account
> 2016-Aug-30 17:55:41.476438 ERROR C:/msys32/DISTRIBUTION-BUILD/src/simplewallet/simplewallet.cpp:2750 Failed to initialize wallet
> 2016-Aug-30 17:56:44.501438 Monero 'Hydrogen Helix' (v0.9.3.0-release)
> 2016-Aug-30 17:56:44.501438 Setting log level = 0
> 2016-Aug-30 17:56:44.501438 default_log: C:\Temp\Monero\simplewallet.log
> 2016-Aug-30 17:56:44.501438 Logging at log level 0 to C:\Temp\Monero\simplewallet.log
> 2016-Aug-30 17:56:44.563838 Loaded wallet keys file, with public address: 48hY1ykp48SAeqjZL8TaM8iKD78BuTWbMdVpvkzsSnQiTvhxVoZRvaoB9oYVbuEoFTfCAjzCPG8sNTGzYSWcfEmyGF8eDfR
> 2016-Aug-30 17:56:44.626238 Error: failed to load wallet: basic_string::resize
> 2016-Aug-30 17:56:44.626238 ERROR C:/msys32/DISTRIBUTION-BUILD/src/simplewallet/simplewallet.cpp:1006 failed to open account
> 2016-Aug-30 17:56:44.626238 ERROR C:/msys32/DISTRIBUTION-BUILD/src/simplewallet/simplewallet.cpp:2750 Failed to initialize wallet

**Created files**
- demo // demo.address.txt // demo.keys
- ZIP file (GitHub forbid me to upload the file directly but the message said ZIPs are allowed. Guess i gotta report that one too) - rename file! [Monero.pptx](https://github.com/monero-project/bitmonero/files/445366/Monero.pptx)


# Discussion History
## moneromooo-monero | 2016-08-30T16:21:26+00:00
Thank you for the detailed report.
Trying those steps work for me on Linux x86_64, the wallet can be loaded after saving, so it looks like a windows and/or 32 bit issue.


## JamesCullum | 2016-08-30T16:37:42+00:00
Can you access the generated files?


## moneromooo-monero | 2016-08-30T16:39:45+00:00
Yes, using the command "simplewallet --wallet-file demo --password helloworld", it then loads just fine.


## moneromooo-monero | 2016-08-30T16:40:35+00:00
Actually, could you try with the 0.9.4 binaries ? It might be a 0.9.3 bug, rather than a Windows or 32 bit bug.


## JamesCullum | 2016-08-30T16:47:12+00:00
It looks like https://getmonero.org/downloads/ or simplewallet has an issue - i just downloaded the 32bit binarys (again, originally 2 days ago) from https://downloads.getmonero.org/win32 and the downloaded file is called monero.win.x86.v0-9-4-0.zip; When extracted and simplewallet gets called, it displays "Monero 'Hydrogen Helix' (v0.9.3.0-release)". The change date of all files is the 02.04.16, just like the release of 0.9.4: https://getmonero.org/2016/04/02/monero-0.9.4-released.html

I dont know if the version number of simplewallet wasnt corrected in 0.9.4 or if getmonero.org accidently packed the 0.9.3 files as 0.9.4 - can you verify either?


## fluffypony | 2016-09-01T08:31:02+00:00
@JamesCullum looks like we goof'd and packaged 0.9.3 as 0.9.4. I'll rebuild it now and update this thread.


## moneromooo-monero | 2016-09-01T10:52:56+00:00
I think it's likely to be due to https://github.com/monero-project/bitmonero/commit/878ab5d896c1a9cb5c50c36a0ded5da998c941d5, which is part of 0.9.4, but not 0.9.3.


## JamesCullum | 2016-09-01T17:53:04+00:00
@fluffypony Same files in the official announcement: https://getmonero.org/2016/04/02/monero-0.9.4-released.html

@moneromooo-monero You mean that the bug existed in 0.9.3 but was fixed in 0.9.4?


## moneromooo-monero | 2016-09-01T19:01:42+00:00
That is what I meant, assuming that this bug is indeed what you are seeing.


## JamesCullum | 2016-09-01T19:06:58+00:00
Thanks for the help, as soon as i get the 0.9.4 binaries i will give it a shot and it will hopefully be resolved here and on SE :)


## JamesCullum | 2016-09-02T20:02:57+00:00
@fluffypony Any updates on the compiling? Its almost two days after "now", and i cant wait to close the issue :)


## JamesCullum | 2016-09-11T15:00:31+00:00
10 days, still nothing :/


## guzzijones | 2016-09-11T15:14:41+00:00
JamesCullum, are you able to download the latest source and compile it?  I do not have a 32 Win OS to test this on and it looks like moneromoo has already verified things on working on linux 64 bit.


## JamesCullum | 2016-09-11T15:31:00+00:00
No, i am unable to install the development environment for it due to the mentioned r/w restrictions.


## moneromooo-monero | 2016-09-17T15:45:19+00:00
Sorry about that. There'll be a 0.9.5 or something in the next couple days though.


## moneromooo-monero | 2016-09-21T17:17:09+00:00
See https://github.com/monero-project/monero/issues/1106


## JamesCullum | 2016-09-21T18:31:09+00:00
Its a different issue, but i tested my details from the start post again with 0.10.0 and it works now. So we can assume that it was indeed the bug in 0.9.3 and a wrong version on getmonero.org that caused the issue.


## fluffypony | 2016-09-23T05:49:51+00:00
Closed by the release of 0.10


# Action History
- Created by: JamesCullum | 2016-08-30T16:11:36+00:00
- Closed at: 2016-09-21T18:31:09+00:00
