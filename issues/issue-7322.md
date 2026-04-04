---
title: transfer_split doesn't split for too many outputs
source_url: https://github.com/monero-project/monero/issues/7322
author: lxop
assignees: []
labels: []
created_at: '2021-01-18T02:57:08+00:00'
updated_at: '2021-02-18T19:02:23+00:00'
type: issue
status: closed
closed_at: '2021-02-18T19:02:23+00:00'
---

# Original Description
The description for `transfer_split` is
> Same as transfer, but can split into more than one tx if necessary.

However, if I try to send funds to more than 15 outputs with `transfer_split` I simply get an error - the transaction is not split into more than one tx:
```
curl -u <rpcusername>:<rpcpassword> --digest localhost:7000/json_rpc -d '{"method":"transfer_split", "params":{"destinations":[<more than 15 destinations>]}}'
{
  "error": {
    "code": -4,
    "message": "sv\/gamma are too large"
  },
  "id": 0,
  "jsonrpc": "2.0"
}
```

Could the logic to split transactions be applied to splitting them in this case too?

For context, I am trying to get set up for airgapped signing of transactions, and need to be sending quite a few outputs. Without a `transfer_split` working in the way I am hoping, I need to create a transaction, move it to the airgapped machine, sign it, move the signed tx back to the online machine, broadcast it, and import key images into the online machine before I can create the next tx. With hundreds of outputs, this is a massively tedious and time-consuming process. If `transfer_split` will split my transfers into appropriate transactions for me, then I can just do this process once regardless of the number of outputs I have.

I am willing to make the changes myself if it is possible, but I want to get some feedback here first.

# Discussion History
# Action History
- Created by: lxop | 2021-01-18T02:57:08+00:00
- Closed at: 2021-02-18T19:02:23+00:00
