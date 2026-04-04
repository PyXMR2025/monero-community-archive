---
title: monero gui win64 install suggested download hash does not match
source_url: https://github.com/monero-project/monero/issues/6680
author: drinkyd
assignees: []
labels: []
created_at: '2020-06-22T06:56:25+00:00'
updated_at: '2020-06-22T21:17:30+00:00'
type: issue
status: closed
closed_at: '2020-06-22T21:17:30+00:00'
---

# Original Description
I'm getting a different hash. Could there be a error on the hash page? D/L from the gui suggestion link.

# Discussion History
## selsta | 2020-06-22T06:59:00+00:00
Which hash are you getting and which hash is getting displayed? Seems ok here.

## drinkyd | 2020-06-22T21:08:15+00:00
From this site: https://web.getmonero.org/downloads/hashes.txt

0820aeb30b39bb86b550ff5d6e641c16491cff3cff2b9ab9873bdc05acc6a041  monero-gui-install-win-x64-v0.16.0.0.exe

After I run "certUtil -hasfile monero-gui-install-win-x64-v0.16.0.0.exe" in CMD, I get this: 

SHA1 hash of monero-gui-install-win-x64-v0.16.0.0.exe:
43626772be9503770d0499f5030c5130ff4ffcb4
CertUtil: -hashfile command completed successfully.

Am I doing it wrong?

## selsta | 2020-06-22T21:10:08+00:00
You are comparing SHA1 and SHA256

## drinkyd | 2020-06-22T21:10:57+00:00
How do I compare the SHA256?


## xiphon | 2020-06-22T21:16:34+00:00
> How do I compare the SHA256?

`certutil.exe -hashfile monero-gui-install-win-x64-v0.16.0.0.exe SHA256`

# Action History
- Created by: drinkyd | 2020-06-22T06:56:25+00:00
- Closed at: 2020-06-22T21:17:30+00:00
