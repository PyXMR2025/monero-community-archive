---
title: TypeError during prove payment, silent fail.
source_url: https://github.com/monero-project/monero-gui/issues/1123
author: qubenix
assignees: []
labels: []
created_at: '2018-02-20T00:06:31+00:00'
updated_at: '2018-03-06T19:02:46+00:00'
type: issue
status: closed
closed_at: '2018-03-06T19:02:46+00:00'
---

# Original Description
When trying to prove payment there is a TypeError that is displayed in the term log, but the gui fails silently. Here is the output of the term:

```
qml: getProof: Generate clicked: txid 74baa4cbfe47ea6656c25a0a91b6b0124f1c448f8424a950b68bf3955cc94d44, address 9vz3MBqiWwLbsF4K9WCSgpH3UsW4pknan2xmyGgsCBfgA1pD8jC3XpW3s4mVffyErZfWuC2s4HqZ1JJpBXB1FgNwPCHrDm3, message: 
qml: Getting payment proof: 
qml: 	txid:  74baa4cbfe47ea6656c25a0a91b6b0124f1c448f8424a950b68bf3955cc94d44 , address:  9vz3MBqiWwLbsF4K9WCSgpH3UsW4pknan2xmyGgsCBfgA1pD8jC3XpW3s4mVffyErZfWuC2s4HqZ1JJpBXB1FgNwPCHrDm3 , message:  
qrc:///main.qml:785: TypeError: Property 'startsWith' of object InProofV11XFBohNW5t1BgV64L3MKepTb84xMT8zxWguBUUnHtkLLAx3sXbp1U11bDuHoGJYoh7542NP1Rdo54AMMWmYrQa4qT3ZrLfbftEKbyVN5qPj2dNQuaA3AfUFdGi9wj2pKixPk is not a function
```

# Discussion History
## stoffu | 2018-02-20T01:05:40+00:00
Hmm, I wrote that code but I don't observe that behavior (macOS 10.12.6). Is there anyone else with this error?

## qubenix | 2018-02-20T01:44:46+00:00
Sorry, I should have mentioned that I'm on Debian 9.

## stoffu | 2018-02-20T02:45:34+00:00
OK, I also observe this issue on Ubuntu 16.04.

## stoffu | 2018-02-20T03:14:14+00:00
#1124 

## qubenix | 2018-03-06T19:02:46+00:00
Closed #1123 via 5db91854091e90c819ef06d9ba1d81998faff350

# Action History
- Created by: qubenix | 2018-02-20T00:06:31+00:00
- Closed at: 2018-03-06T19:02:46+00:00
