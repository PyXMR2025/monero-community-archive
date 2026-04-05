---
title: Background option does not work under MacOS Monterey
source_url: https://github.com/xmrig/xmrig/issues/3059
author: smitty-codes
assignees: []
labels: []
created_at: '2022-05-26T01:01:58+00:00'
updated_at: '2025-06-28T10:35:02+00:00'
type: issue
status: closed
closed_at: '2025-06-28T10:35:02+00:00'
---

# Original Description
**Describe the bug**
The "-B" and "--background" options do not work under MacOS Monterey 12.3.1 (it did not work on Big Sur either).

**To Reproduce**
On MacOS 12.3.1, run the following command (xmrig v6.17.0):
`sudo ./xmrig -o pool.supportxmr.com:443 -u MyWalletString -k --tls --background -p MyMachine`

**Expected behavior**
The command compleates but is not running in the background - no xmrig process in Activity Monitor nor htop command, no cpu spike etc.

**Additional context**
As a workaround, I've been using tmux to run it in the background:
`sudo /usr/local/bin/tmux new -s xmrigsession -d 'caffeinate ./xmrig -o pool.supportxmr.com:443 -u MyWalletString -k --tls -p MyMachine'`


# Discussion History
## Spudz76 | 2022-05-26T02:08:07+00:00
If there is a `config.json` then whatever background option is in there, wins.

## JacksonChen666 | 2022-05-28T21:11:16+00:00
can reproduce bug, but requires changing `config.json` because i have it

## smitty-codes | 2022-05-28T21:56:36+00:00
> 

@Spudz76 I renamed the config.json to blah.txt in the xmrig folder and still --background nor -B does not work so it being the winner doesn't seem to be the cause.

## DeeDeeRanged | 2022-09-30T05:31:25+00:00
Running Debian testing (bookworm) and I have actually the same sort of issue trying to get xmrig to run in background with a gpu. 
From terminal nohup ./xmrig --http-host 0.0.0.0 --http-port 10050 --http-access-token xxxxxxxx --http-no-restricted --no-cpu --opencl --algo kawpow -o stratum+ssl://neox.2miners.com:14040 -u MyWallet.dranged >/dev/null 2>&1 & works but if I use -B or set it in the json file I cannot get it to run in the background. Fires up and dies or no mining.

# Action History
- Created by: smitty-codes | 2022-05-26T01:01:58+00:00
- Closed at: 2025-06-28T10:35:02+00:00
