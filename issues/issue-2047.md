---
title: Mac Client Generated a Broken Wallet? Money lost?
source_url: https://github.com/monero-project/monero-gui/issues/2047
author: bbstm
assignees: []
labels:
- invalid
created_at: '2019-04-01T15:54:38+00:00'
updated_at: '2019-04-03T11:29:55+00:00'
type: issue
status: closed
closed_at: '2019-04-03T00:18:32+00:00'
---

# Original Description
Hello,

I downloaded the Monero GUI and generated a wallet, all the keys were generated successfully and I generated a QRCode of my wallet to do the transfer, from another wallet I tried to do a transfer but the  money never arrived. It was very strange, so I downloaded another Wallet and tried, all transactions to this wallet (Monero Gui) can't be completed, they do a check and say the transaction failed before being processed.

Unfortunately the first wallet software did not applied this check, so it "sent" the money anyway. I used this javascript tool (https://xmr.llcoins.net/checktx.html) developed by luigi1111 to check the transaction and the result was weird, see below please:

> This address doesn't own output 0 with pubkey: [EDITED01] for amount: Confidential
> RingCT amount for output 1 with pubkey: [EDITED02] decoded incorrectly! It will not be spendable.


# Discussion History
## selsta | 2019-04-01T15:56:42+00:00
What was the first wallet software that you used?

## bbstm | 2019-04-01T16:01:09+00:00
Not sure, it was from a transaction made online with a person from localbitcoins. BTW, he sent me the receipt.

## selsta | 2019-04-01T16:02:09+00:00
Is it possible that you share your wallet public address? The address that you sent the other person?

## bbstm | 2019-04-01T16:11:24+00:00
Sure.

## selsta | 2019-04-01T16:26:03+00:00
That’s a valid XMR address. It doesn’t make sense that Guarda Wallet has problems sending to this address, probably a problem on Guarda’s side.

## dEBRUYNE-1 | 2019-04-01T16:27:18+00:00
Can you try these steps to verify the transaction?

1. Go to the `Settings` page of the GUI and press on `Show seed & keys`. Subsequently, copy the *private / secret* view key. 

2. Go to [this](https://xmrchain.net) blockexplorer.

3. Enter your transaction ID / hash.

4. Now search the page for `Decode outputs`. 

5. Enter your private view key. In addition, enter your address in the second box.

6. Press on decode outputs.

7. If it shows "output true" it proves you correctly received your XMR.


## bbstm | 2019-04-01T16:43:14+00:00
> That’s a valid XMR address. It doesn’t make sense that Guarda Wallet has problems sending to this address, probably a problem on Guarda’s side.

Humm... but what happened with the real transaction that failed with the seller from localbitcoins?

BTW, it was not guarda.

thanks.

## bbstm | 2019-04-01T16:46:46+00:00
> Can you try these steps to verify the transaction?
> 
>     1. Go to the `Settings` page of the GUI and press on `Show seed & keys`. Subsequently, copy the _private / secret_ view key.
> 
>     2. Go to [this](https://xmrchain.net) blockexplorer.
> 
>     3. Enter your transaction ID / hash.
> 
>     4. Now search the page for `Decode outputs`.
> 
>     5. Enter your private view key. In addition, enter your address in the second box.
> 
>     6. Press on decode outputs.
> 
>     7. If it shows "output true" it proves you correctly received your XMR.

I did, the output edited is below:

> Tx hash: [HashID]
> Tx public key: [TXPubID]
> Payment id (decrypted): 0000000000000000 (value incorrect if you are not the recipient of the tx)
> Block: 17984743
> Timestamp [UCT]: 2019
> Age [y:d:h:m:s]:
> Fee: 0.000016240000
> Tx size: 1.4382 kB
> Checking which outputs belong to the given address and viewkey
> address: 
> viewkey: ****************************************************************
> Outputs (2)
> output public key
> amount
> output match?
> [EDITED]
> ?
> false
>[edited]
> XX.YY0000000
> true 
> Sum XMR from matched outputs (i.e., incoming XMR): XX.YY0000000000 
> 

If I understood it properly it was transferred, but my balance still appears as zero. :(

Thanks.

## dEBRUYNE-1 | 2019-04-01T17:32:16+00:00
Upon installing the GUI wallet, which mode did you choose? 

## bbstm | 2019-04-01T23:57:28+00:00
> Upon installing the GUI wallet, which mode did you choose?

Advanced mode. 

## dEBRUYNE-1 | 2019-04-02T06:20:20+00:00
@bbstm - Can you perform these steps?

**[1]** Go to the `Settings` page of the GUI.

**[2]** Go to the `Log` tab.

**[3]** Type `status` into the `command + enter (e.g. 'help' or 'status')` box.

**[4]** Post the output here. 

## bbstm | 2019-04-03T00:11:41+00:00
> @bbstm - Can you perform these steps?
> 
> **[1]** Go to the `Settings` page of the GUI.
> 
> **[2]** Go to the `Log` tab.
> 
> **[3]** Type `status` into the `command + enter (e.g. 'help' or 'status')` box.
> 
> **[4]** Post the output here.

Sure sir.

>>> status
[4/2/19 7:08 PM] Height: 1381623/1804569 (76.6%) on mainnet, not mining, net hash 140.41 MH/s, v5, up to date, 8(out)+0(in) connections, uptime 1d 9h 0m 44s

Does it explain why the money doesnt show up?

Thanks.

## selsta | 2019-04-03T00:15:55+00:00
Your blockchain is still syncing up with the network. Once it is at 100%, your funds should show up.

I’ll close this as this doesn’t seem to be a bug. Please comment if you still have problems once your blockchain is fully synced up.

+invalid

## bbstm | 2019-04-03T09:26:30+00:00
> Your blockchain is still syncing up with the network. Once it is at 100%, your funds should show up.
> 
> I’ll close this as this doesn’t seem to be a bug. Please comment if you still have problems once your blockchain is fully synced up.
> 
> +invalid

Hummm.. I think it synced but still no money in balance.

> 
> >>> status
> [4/3/19 7:19 AM] Height: 1399343/1399343 (100.0%) on mainnet, not mining, net hash 273.78 MH/s, v5 (next fork in 0.9 days), up to date, 0(out)+0(in) connections, uptime 0d 2h 34m 50s
> >>> sync_info
> [4/3/19 7:19 AM] Height: 1399343, target: 1399343 (100%)
> Downloading at 0 kB/s
> 0 peers
> 0 spans, 0 MB

One thing that called my attention is that sometimes Height appear with 1399343 and sometimes 1804569 . Why?

Thanks.

## dEBRUYNE-1 | 2019-04-03T11:29:55+00:00
It may be accidentally reporting that you are fully synced. Perhaps it would be worthwhile to switch to `Simple mode (bootstrap mode)`? This is done as follows:

1. Go to the `Settings` page of the GUI wallet.

2. Press `Close wallet`

3. Choose `Simple mode (bootstrap mode)`

4. Reopen your wallet via the `Open a wallet from file` option. 

# Action History
- Created by: bbstm | 2019-04-01T15:54:38+00:00
- Closed at: 2019-04-03T00:18:32+00:00
