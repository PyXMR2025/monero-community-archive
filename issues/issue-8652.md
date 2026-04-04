---
title: 'Can not send transaction Error: internal error: real output not found'
source_url: https://github.com/monero-project/monero/issues/8652
author: stanbar
assignees: []
labels: []
created_at: '2022-11-28T13:48:56+00:00'
updated_at: '2025-05-26T06:22:36+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi,
I'm trying to send a transaction using `monero-wallet-cli` connected to local stagenet.

I'm running local stage net two nodes (as suggested on [stackoverflow](https://monero.stackexchange.com/a/9869/14294))
```bash
monerod --version
Monero 'Fluorine Fermi' (v0.18.1.2-release)

monerod --stagenet --no-igd --hide-my-port --data-dir node1 --p2p-bind-ip 127.0.0.1 --p2p-bind-port 48080 --rpc-bind-port 48081 --zmq-rpc-bind-port 48082 --add-exclusive-node 127.0.0.1:38080

monerod --stagenet --no-igd --hide-my-port --data-dir node2 --p2p-bind-ip 127.0.0.1 --rpc-bind-ip 0.0.0.0 --confirm-external-bind --add-exclusive-node 127.0.0.1:48080
```

then connecting to them on two terminals with `monero-wallet-cli --stagenet`

After mining some XMR I try to send the transaction from the first one to the second one, but I get an error:
```
[wallet 5BKk1r]: version
Monero 'Fluorine Fermi' (v0.18.1.2-release)
[wallet 5BKk1r]: refresh
Starting refresh...
Refresh done, blocks received: 0
Currently selected account: [0] Primary account
Tag: (No tag assigned)
Balance: 69077.964019386086, unlocked balance: 68043.883242532499 (59 block(s) to unlock)
[wallet 5BKk1r]: transfer 571DVUhmatR9yJP9raWxK9WaZjd51hW2wUKy1hY3A1sVM7ifsWxbPYWetzXXeEG4ngVBSUuxkk1eQA3BMm5oAaubRKzHCpw 10
Wallet password:
Error: internal error: real output not found
```

I tried using two different machines, Arch linux x86 and MacBook Apple M1, both of them throw the same error.



# Discussion History
## ajordanBBN | 2023-07-07T19:42:23+00:00
I had the same problem. I think the problem is that the code to parse the arguments for the transfer command doesn't match the usage statement. You seem to have to provide a ring size, even though the usage statement indicates that it is an optional parameter:

https://github.com/monero-project/monero/blob/00fd416a99686f0956361d1cd0337fe56e58d4a7/src/simplewallet/simplewallet.cpp#L6273-L6290

Note that at line 6275, it only checks to see if you have more than zero arguments left, and if you do, it interprets the first argument as the ring size. This doesn't match the usage statement, and the error checking block for the call to `get_xtype_from_string` is, rather hilariously, empty.

I don't know how to fix the code, but I was able to get transactions to spend by putting a value in front of the address, so that the `ring_size` parameter gets a value. This worked:

`transfer 16 REDACTED_ADDRESS REDACTED_AMOUNT`

but this didn't:

`transfer REDACTED_ADDRESS REDACTED AMOUNT`

## preland | 2025-02-12T05:44:16+00:00
I can confirm that this behavior still exists, along with the misleading help output that implies that the ring amount is optional. This is probably still low priority unless anyone else is concerned.

## fxrstor | 2025-04-30T17:21:01+00:00
![Image](https://github.com/user-attachments/assets/ffae902c-4910-4d74-b226-49ea31b08fdf)
This issue still exists afaik.

## tczee36 | 2025-05-26T06:22:35+00:00
can confirm this issue exists in v0.18.4.0

# Action History
- Created by: stanbar | 2022-11-28T13:48:56+00:00
