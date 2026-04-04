---
title: monerod fails to start when installed as windows service on startup
source_url: https://github.com/monero-project/monero-gui/issues/4023
author: zubair72
assignees: []
labels: []
created_at: '2022-09-09T07:35:09+00:00'
updated_at: '2023-01-17T05:00:29+00:00'
type: issue
status: closed
closed_at: '2023-01-17T05:00:29+00:00'
---

# Original Description
Steps to reproduce error

1. Run command as administrator
2. Switch to path where monerod.exe is located
3. type monerod --install-service
4. After successfull message if you did run the monero wallet gui and then closed the service then you can start the service else it fails
5. Please note it will fail to start automatically on windows startup but if one logins and run the monero-gui-wallet afterwards you may stop the daemon when from gui or when closing the wallet and able to start the daemon service without issue

Note: if prior to starting service you run the monerod from cmd line it again fix the service start issue

Please have look into this

# Discussion History
## selsta | 2022-09-09T17:29:32+00:00
Can you reproduce this issue without monero-wallet-gui being involved?

## zubair72 | 2022-09-09T20:05:02+00:00
Issue appears if monero-wallet-gui is not run, it does not appear if you run monero-wallet-gui prior to doing steps upto 4, similarly if you run monerod from elevated command line prior to doing 4 steps, issue again does not appear
Summary: to reproduce issue restart windows to ensure monerod was not running, do step 1-4 and notice monerod service refuse to start.

## selsta | 2022-09-09T20:06:21+00:00
If this issue also appears without running monero-wallet-gui then please open an issue here instead: https://github.com/monero-project/monero

## zubair72 | 2022-09-09T20:16:49+00:00
done as advised to and create new issue at [https](https://github.com/monero-project/monero)

## selsta | 2023-01-17T05:00:29+00:00
https://github.com/monero-project/monero/issues/8560

# Action History
- Created by: zubair72 | 2022-09-09T07:35:09+00:00
- Closed at: 2023-01-17T05:00:29+00:00
