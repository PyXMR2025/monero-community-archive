---
title: multisig signing error
source_url: https://github.com/monero-project/monero/issues/3447
author: egonson
assignees: []
labels:
- invalid
created_at: '2018-03-20T06:11:50+00:00'
updated_at: '2018-05-16T11:40:57+00:00'
type: issue
status: closed
closed_at: '2018-05-16T11:40:57+00:00'
---

# Original Description
I signed multisig tx and I lost the tx_data_hex. So I signed again, but I met the error.

curl -X POST --digest --user "monero:monero" http://127.0.0.1:18083/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"sign_multisig","params":{"tx_data_hex":"[transfer result multisig_txset]"}}' -H 'Content-Type: application/json'
{
  "error": {
    "code": -35,
    "message": "Failed to sign multisig tx: This signature was made with stale data: export fresh multisig data, which other participants must then use"
  },
  "id": "0",
  "jsonrpc": "2.0"
}

question.
How can I sign multisig tx again? or how can I get the previous signed tx data?


# Discussion History
## moneromooo-monero | 2018-03-20T10:22:19+00:00
The message says it: export multisig info, and import it. You can't sign twice with the same info, as it woul open up a vulnerbility.

## rbrunner7 | 2018-03-24T20:48:41+00:00
If you say *You can't sign twice with the same info*, what is this "info" that you refer to? The state of the wallet, as produced by the last executed `import_multisig_info` command?

Is the consequence of this that you never can have 2 or more multisig transactions "in transit", that you must fully do one after the other strictly in sequence, with an obligatory exchange of "multisig_info" in between?

I guess so, because what I did to get the same error was a crystal-clear sequence of actions with the CLI wallet:

- `transfer` in wallet A, rename `multisig_monero_tx` to `multisig_monero_tx_1` to avoid overwrite
- `transfer` again in wallet A to start a second transaction right away
- `sign_multisig` in wallet B, with the first file `multsig_monero_tx_1`
- `sign_multisig` again in wallet B, with the second file `multisig_monero_tx`

That last action then leads to the error that the OP also got:

*Error: Multisig error: This signature was made with stale data: export fresh multisig data, which other participants must then use*

## moneromooo-monero | 2018-03-24T22:41:36+00:00
Yes to all (theoretically you could modify the wallet to export/import lists of such L/R data instead of one per at a time).

## moneromooo-monero | 2018-05-16T10:59:17+00:00
Seems to work as designed, you can't sign twice with the same data.

+invalid


# Action History
- Created by: egonson | 2018-03-20T06:11:50+00:00
- Closed at: 2018-05-16T11:40:57+00:00
