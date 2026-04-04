---
title: 'Error: failed to generate new wallet: failed to save file "home/portfolio.keys"'
source_url: https://github.com/monero-project/monero/issues/2045
author: masonsam
assignees: []
labels:
- invalid
created_at: '2017-05-24T19:09:22+00:00'
updated_at: '2017-08-08T10:30:15+00:00'
type: issue
status: closed
closed_at: '2017-08-08T10:30:15+00:00'
---

# Original Description
Hi,
I tried to create a walet with monero-wallet-cli but i get this error
 `Error: failed to generate new wallet: failed to save file "home/portfolio.keys"`
what can i do?
this is the command:
`./monero-wallet-cli --log-level 3 --generate-new-wallet   home/portfolio`
thank you!
Fixed

# Discussion History
## moneroexamples | 2017-05-24T23:40:58+00:00
You first need to create folder called "home". 
```
mkdir home
./monero-wallet-cli --log-level 3 --generate-new-wallet home/portfolio
```

## masonsam | 2017-05-25T10:00:51+00:00
I had the folder yet, i'm in ubuntu 16.4 and i put the wallet in Home 

## masonsam | 2017-05-25T23:49:05+00:00
I fixed it with / before path:
`./monero-wallet-cli --log-level 3 --generate-new-wallet home/portfolio`
thank you

## moneromooo-monero | 2017-08-07T17:38:48+00:00
+invalid

## moneromooo-monero | 2017-08-08T10:25:50+00:00
+resolved

# Action History
- Created by: masonsam | 2017-05-24T19:09:22+00:00
- Closed at: 2017-08-08T10:30:15+00:00
