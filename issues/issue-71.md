---
title: Transaction public key uniformity
source_url: https://github.com/monero-project/research-lab/issues/71
author: SarangNoether
assignees: []
labels: []
created_at: '2020-02-19T19:48:21+00:00'
updated_at: '2020-02-21T00:57:34+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Currently, the number of transaction public keys included in a transaction can, in some cases, reveal that one or more outputs are directed to subaddresses. A mitigation is to uniformly include a separate transaction public key for each output.

# Discussion History
## Mitchellpkt | 2020-02-19T20:10:28+00:00
Here is preliminary data exploiting this information leak to study subaddress adoption. 

Key word: *preliminary* ... This plot actually shows the fraction of transactions that contain extra public keys, not taking into account transaction structure. A plot of subaddress adoption for >2-output transactions would be more informative, and I'll make this modification next time I can carve out a few minutes for research.

![image](https://user-images.githubusercontent.com/21246742/74871695-c224df80-5310-11ea-9453-9aaedbeeeb66.png)


## UkoeHB | 2020-02-21T00:35:23+00:00
*Background*

There is some intricacy to when additional transaction public keys are used (see code path transfer_selected_rct() → construct_tx_and_get_tx_key() → construct_tx_with_tx_key() → generate_output_ephemeral_keys() and classify_addresses()) surrounding change outputs where the transaction author knows the recipient’s view key (since it’s himself; also the case for dummy change outputs, which are created when a 0-amount output is necessary, since the author generates that address). Whenever there are at least two non-change outputs, and at least one of their recipients is a subaddress, add #tx_pub_keys == #outputs (a current bug in the core implementation adds an extra transaction public key to transaction data even beyond the additional keys, which is not used for anything). If either just the change output is to a subaddress, or there is just one non-change output and it’s to a subaddress, then only one transaction public key is created. These details help mingle a portion of subaddress transactions amongst the more common normal address transactions, and 2-output transactions which compose around 95% of transaction volume as of this writing.

*My thoughts*

I feel like ambiguity around the true population of subaddress transactions is a strong argument against adding dummy transaction public keys. It could be the case that 90% of actual transactions use subaddresses (assuming they are made with the core implementation), so an analyst doesn't necessarily get a big advantage seeing transactions which have additional public keys.

This may change if Janus (issue #62) is implemented.

# Action History
- Created by: SarangNoether | 2020-02-19T19:48:21+00:00
