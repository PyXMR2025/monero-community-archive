---
title: sign_multisig error
source_url: https://github.com/monero-project/monero/issues/5665
author: aaronovz1
assignees: []
labels: []
created_at: '2019-06-17T22:53:08+00:00'
updated_at: '2019-06-18T16:48:29+00:00'
type: issue
status: closed
closed_at: '2019-06-18T16:48:29+00:00'
---

# Original Description
I am trying to sign a multisig transaction over RPC and I am getting the error:
`Failed to sign multisig tx: This signature was made with stale data: export fresh multisig data, which other participants must then use`

It is not clear to me how exactly I resolve this. I think what happened is, I was able to sign the transaction initially but an error in my code caused `submit_multisig` not to run and then I lost the output from `sign_multisig`. Subsequent attempts to re-sign now give the error.

The message says to export fresh data but my attempts at this have not resolved the problem. Here is what I tried to do:

1. Person A runs `export_multisig_info`
2. Person B runs `import_multisig_info` with file from Person A (step 1)
3. Person B runs `transfer` to generate unsigned transaction file
4. Person A attempts to sign tx with `sign_multisig`

What am I missing in this process?

# Discussion History
## moneromooo-monero | 2019-06-17T23:02:27+00:00
A tries to sign. For this, A needs to use data from B. A did not import data from B in your steps above.

## moneromooo-monero | 2019-06-17T23:11:19+00:00
Actually, no, that looks kinda right. A will need to lookup its k that corresponds to what B used, which was supplied by A.

## moneromooo-monero | 2019-06-17T23:18:01+00:00
Ah, right, A's k was already used by signing that first tx, so it can't use it again. So it needs to export, B needs to import, and create a tx with that. B creates its own set of kLR when it exports new multisig data. In this case, I think it might work if B also exports, but A does not need to import. Can you try that ?

## aaronovz1 | 2019-06-18T01:17:13+00:00
That appears to have worked. The steps I did were:

1. B exports
2. A imports
3. A saves
4. A exports
5. A saves
6. A creates tx
7. B signs tx

I added the extra `save` commands just in case.

# Action History
- Created by: aaronovz1 | 2019-06-17T22:53:08+00:00
- Closed at: 2019-06-18T16:48:29+00:00
