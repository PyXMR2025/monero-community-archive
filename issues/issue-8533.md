---
title: Could blockchain sync use more than 2 cores?
source_url: https://github.com/monero-project/monero/issues/8533
author: stefan-reich
assignees: []
labels: []
created_at: '2022-08-23T16:49:03+00:00'
updated_at: '2022-08-28T20:38:19+00:00'
type: issue
status: closed
closed_at: '2022-08-23T16:56:57+00:00'
---

# Original Description
I'm using monero-wallet-gui and a local node to sync the blockchain.

When doing so, it appears monerod is using between one and two cores.

Could this be increased? Or is there a  fundamental problem?

Thanks in advance for any answers

# Discussion History
## selsta | 2022-08-23T16:50:03+00:00
Which OS are you using? Did you set a custom blockchain location?

## stefan-reich | 2022-08-23T16:51:07+00:00
> Which OS are you using? Did you set a custom blockchain location?

Sorry for editing the question while you already answered. I took out the reference of the GUI core use because it went to 0% just after I typed this. (Occasionally the GUI process is using a full core while syncing the blockchain which I'd like to understand, but it's not that important.)

Regarding your question, I am using Linux and yes it is a custom blockchain location.

## selsta | 2022-08-23T16:53:19+00:00
Is the blockchain stored on a HDD or SSD?

## stefan-reich | 2022-08-23T16:53:42+00:00
> Is the blockchain stored on a HDD or SSD?

SSD in a VeraCrypt volume

## selsta | 2022-08-23T16:54:47+00:00
VeraCrypt volume will likely significantly slow down sync.

## stefan-reich | 2022-08-23T16:55:22+00:00
> VeraCrypt volume will likely significantly slow down sync.

OK I see. So monerod is generally able to use all available cores?

## selsta | 2022-08-23T16:56:16+00:00
Yes, it can use more than 2 cores.

## stefan-reich | 2022-08-23T16:56:57+00:00
> Yes, it can use more than 2 cores.

Ah, that answers my question. Thanks a lot. I'll try to move the blockchain out of the encrypted volume.

## selsta | 2022-08-23T17:00:48+00:00
Initially sync also uses checkpoints to skip known PoW hashes during block verification, the last couple percentage won't use checkpoints so system CPU usage should significantly increase.

## stefan-reich | 2022-08-28T11:12:24+00:00
Just quick feedback: I moved the blockchain to a non-encrypted drive and CPU use went up a tiny bit, I saw 2.5 cores used max (out of 8).

## selsta | 2022-08-28T20:38:19+00:00
Which height are you? After the latest checkpoint (~2661600) CPU usage should go up.

# Action History
- Created by: stefan-reich | 2022-08-23T16:49:03+00:00
- Closed at: 2022-08-23T16:56:57+00:00
