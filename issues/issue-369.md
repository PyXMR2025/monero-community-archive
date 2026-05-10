---
title: monero-wallet-rpc random password generation seems "broken"
source_url: https://github.com/seraphis-migration/monero/issues/369
author: kic0
assignees: []
labels: []
created_at: '2026-05-09T19:36:36+00:00'
updated_at: '2026-05-09T20:38:28+00:00'
type: issue
status: closed
closed_at: '2026-05-09T20:38:28+00:00'
---

# Original Description
When running monero-wallet-rpc if we don't set a username and password it generates one for us like:

./monero-wallet-rpc --rpc-bind-ip 127.0.0.1 --rpc-bind-port 28088 --testnet --log-file ~/wallet-rpc.log

2026-05-09 19:30:15.984 W RPC username/password is stored in file monero-wallet-rpc.28088.login

$ cat monero-wallet-rpc.28088.login 
monero:DJTg+CDpTk9AHMoE74F2GQ==

all good, although by running it several times I notice that the last 2 of the 24 chars are always 2 "=" 

monero:LGxDSrVtClBq8VbRUiXoew==
monero:sKk0XcXoBM+J99Go3oGXmA==
....

I understand that given the password is 24 chars long with letters numbers upper/lowercase etc this doesn't narrow down cracking the password much, but I do wonder if something in the random password generation is not working properly.

# Discussion History
## j-berman | 2026-05-09T20:38:28+00:00
The password is base64 encoded which appends = until there are a multiple of 3 chars: https://stackoverflow.com/questions/6916805/why-does-a-base64-encoded-string-have-an-sign-at-the-end

It's using 128 bits of randomness

# Action History
- Created by: kic0 | 2026-05-09T19:36:36+00:00
- Closed at: 2026-05-09T20:38:28+00:00
