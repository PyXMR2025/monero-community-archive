---
title: Monero Wallet Gui Won't Connect to Remote Node
source_url: https://github.com/monero-project/monero-gui/issues/4422
author: misterjuicebox
assignees: []
labels: []
created_at: '2025-03-22T02:05:01+00:00'
updated_at: '2025-05-17T19:33:41+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I'm running 0.18.3.4-release (Qt 5.15.13) on Apple Silicon Macbook pro. I cannot get the gui to connect to any remote node. When I click on the log tab there is nothing logged to diagnose the issue. When I try to connect to the remote nodes via my terminal with an nc -zv command, the connection succeeds. Any idea what's going on?

# Discussion History
## selsta | 2025-03-22T12:30:23+00:00
Did this work in the past? Do you use some per-application firewall?

## misterjuicebox | 2025-03-22T19:17:42+00:00
It never worked. As far as I know I don't have any firewall or per application firewall setup. It works on another macbook I have, but that Macbook is running Sonoma, while the one where the gui won't connect is running Sequoia. I'm afraid to update the 2nd Macbook to see if the issue is related to the OS version

## selsta | 2025-03-24T18:20:56+00:00
I use monero-wallet-gui on the latest macOS version so that should not be an issue.

## ckcr4lyf | 2025-04-24T05:55:16+00:00
if you know the IP of the remote node, can you try and use wireshark to see if any packets are being sent at all?

Is it a tor node? If so make sure you've enabled Socks5 Proxy in the "interface" tab.

(FWIW: I use a remote tor node on `0.18.3.4-release (Qt 5.15.16)` , Arch Linux)

## St3v3-wq | 2025-05-17T19:31:37+00:00
I can confirm this issue on linux version 0.18.3.4. It seems that p2pool will not be installed when needed. The standalone (binary) version is working well.

# Action History
- Created by: misterjuicebox | 2025-03-22T02:05:01+00:00
