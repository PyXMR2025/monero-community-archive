---
title: 'Issue when running monero-wallet-rpc (E: Failed to bind IPv4, ADDRESS ALREADY
  IN USE)'
source_url: https://github.com/monero-project/monero/issues/7973
author: albertodona
assignees: []
labels: []
created_at: '2021-09-25T08:29:07+00:00'
updated_at: '2021-09-25T10:40:18+00:00'
type: issue
status: closed
closed_at: '2021-09-25T10:40:18+00:00'
---

# Original Description
Hello everyone, I am running `monerod`and `monero-wallet-rpc` on the same machine, but when I try to launch the` monero-wallet-rcp` I get this error:
![Capture](https://user-images.githubusercontent.com/74737723/134764492-424a7903-cd40-4a19-8e34-9960340218b2.PNG)

This is the command that I use to launch `monero-wallet-rpc:` 
`monero-wallet-rpc --daemon-address 127.0.0.1:18081 --wallet-file=/path/to/my/wallet --rpc-bind-ip 127.0.0.1 --rpc-bind-port 18082  --log-level 1 --disable-rpc-login --prompt-for-password`

I suppose that the issue is caused by the `monerod` daemon that is binded on the same interface (127.0.0.1).

Maybe someone else faced this problem and can help us to get through.

Thanks

# Discussion History
## selsta | 2021-09-25T10:25:01+00:00
Port 18082 is used by monerod, try a different one.

## albertodona | 2021-09-25T10:40:18+00:00
> Port 18082 is used by monerod, try a different one.

**Thanks, this solved the issue.** I tought that `monerod` was binded to 18081 port as I specified in his relative config file...



# Action History
- Created by: albertodona | 2021-09-25T08:29:07+00:00
- Closed at: 2021-09-25T10:40:18+00:00
