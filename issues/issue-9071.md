---
title: print_height displays higher by 1 number on stagenet
source_url: https://github.com/monero-project/monero/issues/9071
author: quakemmo
assignees: []
labels: []
created_at: '2023-11-20T14:06:54+00:00'
updated_at: '2023-11-20T14:25:48+00:00'
type: issue
status: closed
closed_at: '2023-11-20T14:25:47+00:00'
---

# Original Description
Using Monero 'Fluorine Fermi' (v0.18.3.1-release) on Linux.

monerod's print_height command displays a number higher (by 1) than the actual blockchain height.
Displaying the latest block (as reported by print_height) results in an error. The issue doesn't seem to be there on mainnet.

```
print_height
1484213

print_block 1484213
Error: Unsuccessful -- 

print_block 1484212
<prints block json OK>

```

# Discussion History
## selsta | 2023-11-20T14:13:55+00:00
1484213 is currently being mined, 1484212 is the last mined block.

From what I can tell this behaviour is consistent on mainnet, testnet and stagenet.

## quakemmo | 2023-11-20T14:21:05+00:00
Correct, behavior is consistent between mainnet, and stagenet. I guess I just ran into a race condition when between the moment I typed print_height and print_block on mainnet, a block has been mined.

Is there a particular reason that the "currently being mined" block is included in the print_height result? This isn't consistent with other blockchains such as ethereum or bitcoin, where "blockchain height"  refers to blocks that already have been mined. Or am I completely wrong somewhere?

## selsta | 2023-11-20T14:24:36+00:00
From what I know behaviour has always been this way in monero, I don't know why exactly but changing this now would break a lot of existing systems.

## quakemmo | 2023-11-20T14:25:47+00:00
Thanks for your replies!

# Action History
- Created by: quakemmo | 2023-11-20T14:06:54+00:00
- Closed at: 2023-11-20T14:25:47+00:00
