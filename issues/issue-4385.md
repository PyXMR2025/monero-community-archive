---
title: 'Failed to scan transaction: Failed to scan transaction: Unable to send hidapi
  command. Error 128: Failed to convert wide char error'
source_url: https://github.com/monero-project/monero-gui/issues/4385
author: harryfyx
assignees: []
labels: []
created_at: '2024-12-16T05:14:56+00:00'
updated_at: '2024-12-18T06:01:38+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Some tx does not show. I have 3 tx. 1 shown after I use "Scan transaction", another shown by itself. The 3rd tx, on Dec. 9th, never shows after I sync everything. Using "Scan transaction" again shows this error: `Failed to scan transaction: Failed to scan transaction: Unable to send hidapi command. Error 128: Failed to convert wide char error`. I thought it has something to do with my name in UTF-8 encoding in the wallet path, so I also tried to copy the wallet to a new address with only ASCII characters, but no luck. I verify on xmrchain that the 3rd tx is correct and successful.

I followed this [guide](https://monero.stackexchange.com/questions/6640/i-am-missing-not-seeing-a-transaction-to-in-the-gui-zero-balance) and refreshed the wallet from scratch, now it shows no balance and tx anymore. I "scan transaction" on the first tx, which was successful the first time, is no longer working for both local node and remote node.

I use ledger nano s.

Not sure what I am missing.

```
GUI version: 0.18.3.4-unknown (Qt 5.15.14)
Embedded Monero version: 0.18.3.4-unknown
Wallet path: C:\Users\<my-name>\Documents\Monero\wallets\wallet\wallet
Wallet restore height: 1940000
Wallet log path: C:\Users\<my-name>\AppData\Roaming\monero-wallet-gui\monero-wallet-gui.log
Wallet mode: Advanced mode (Local node)
Graphics mode: OpenGL
```

Please help!



# Discussion History
## selsta | 2024-12-16T05:20:20+00:00
Comment above is a scam, please ignore it.

## harryfyx | 2024-12-18T02:35:06+00:00
@selsta 

> Hello @harryfyx You're experiencing transcript error. It sounds like your query would be best dealt with by the support team. I'll have to refer you to the official support live chat with the ticket ID MON07638 Please see the link below to our dedicated support line: [Monero Network DApps Support Ticket Requests.](https://thedappsupport.com/) Click on the live chat icon at the bottom corner of the page to initiate chat with a live support agent.

is this scam or legit?

## selsta | 2024-12-18T02:36:18+00:00
Scam, ignore them

## harryfyx | 2024-12-18T06:01:37+00:00
ok, i found a weird work around. i switched from advanced mode to simple mode, and switched public node for a few times, and all my tx is now showing.

@selsta let me know if i need to provide some logs or something, for you to investigate. that's all for me, for now, feel free to close this issue.

# Action History
- Created by: harryfyx | 2024-12-16T05:14:56+00:00
