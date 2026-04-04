---
title: Couldn't open wallet v0.18
source_url: https://github.com/monero-project/monero-gui/issues/4002
author: Petr-Mi
assignees: []
labels: []
created_at: '2022-08-11T20:07:40+00:00'
updated_at: '2022-11-03T21:16:36+00:00'
type: issue
status: closed
closed_at: '2022-11-03T21:16:36+00:00'
---

# Original Description
I get error **_Couldn't open wallet: failed to read file "C:\Users\...keys"_** from v0.18+
In version 0.17.3.2 it's OK.

I try v0.18.0.0 and v0.18.1.0 now. Both give this error.

# Discussion History
## selsta | 2022-08-11T20:55:29+00:00
Can you make a screenshot? Can you post the file size of your wallet and your wallet.keys file?

## Petr-Mi | 2022-08-11T21:08:52+00:00
@selsta 
The problem is in the diacritics in name of user.
Wallet has 3,11 MB, keys has 1,54 kB

![Monero v0 18 1 0](https://user-images.githubusercontent.com/81816858/184241516-fce1f1b3-7ad6-4ead-a682-988212245586.png)
[monero-wallet-gui.log](https://github.com/monero-project/monero-gui/files/9312118/monero-wallet-gui.log)



## selsta | 2022-08-11T22:12:24+00:00
Can you reproduce the same behavior with monereo-wallet-cli ?

## Petr-Mi | 2022-08-12T06:53:17+00:00
CLI (monero-wallet-cli.exe) cannot find wallet.

![image](https://user-images.githubusercontent.com/81816858/184300418-98e207ba-e056-4b90-a320-0d206688051c.png)

![image](https://user-images.githubusercontent.com/81816858/184300459-44f4dea0-c93c-41e1-b5c6-534d0ecedd3a.png)



## Petr-Mi | 2022-08-12T06:58:18+00:00
CLI v0.17.3.2 also don't work. GUI v0.17.3.2  work.

## selsta | 2022-08-15T00:38:33+00:00
Did you start it like this? `monero-wallet.cli.exe --wallet-file C:\path\to\wallet.keys`

## Petr-Mi | 2022-08-15T07:36:48+00:00
The same issue with diacritics in path. If I moved *.keys to folder without diacritics then Monero CLI work.
I had to use quotes in the path.

![image](https://user-images.githubusercontent.com/81816858/184594798-f16d755d-e39c-457f-886f-9299b9af68b8.png)


## AlesRFK | 2022-08-19T20:30:17+00:00
Moving my *.keys to the path without diactritics solved the same error. Díky.

## selsta | 2022-08-19T20:31:08+00:00
I don't think this is anything we have touched in a long time that's why I'm surprised that this errors on v0.18 and works on v0.17

## selsta | 2022-09-02T03:35:59+00:00
We found the issue and it will be fixed in the next release.

## selsta | 2022-11-03T21:16:36+00:00
Fixed in v0.18.1.1

# Action History
- Created by: Petr-Mi | 2022-08-11T20:07:40+00:00
- Closed at: 2022-11-03T21:16:36+00:00
