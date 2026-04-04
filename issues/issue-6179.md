---
title: 'monero gui linux suggested download hash does not match '
source_url: https://github.com/monero-project/monero/issues/6179
author: wallaceturner
assignees: []
labels: []
created_at: '2019-11-25T05:14:58+00:00'
updated_at: '2019-11-26T08:41:36+00:00'
type: issue
status: closed
closed_at: '2019-11-26T08:41:36+00:00'
---

# Original Description
I am using monero-gui-linux-x64-v0.14.1.0

Running the app I get the following message:

```
New version of Monero v.0.15.0.1 is available.

Download:
https://downloads.getmonero.org/gui/monero-gui-linux-x64-v0.15.0.1.tar.bz2

SHA256 Hash:
260edb14b1614e5b862b761eccd6259c1f0914d978016b227a9f4558059e4866
```

however the hash of this file is in fact
```
85a6885849d578691a09834c66ed55af4783ea8347b7784de9ea46e90995a57c
```

can someone please clarify? Both my current version(0.14.1.0) and the new version i have GPG verified.

![image](https://user-images.githubusercontent.com/2849980/69514226-78cd2a00-0f85-11ea-9c99-b999d2b7f77c.png)



# Discussion History
## selsta | 2019-11-25T06:07:04+00:00
Software bug, it displays the hash of the v0.15.0.1 GUI source code.

https://downloads.getmonero.org/source/monero-gui-source-v0.15.0.1.tar.bz2

Fixed in https://github.com/monero-project/monero-gui/pull/2485

## dEBRUYNE-1 | 2019-11-26T08:33:30+00:00
This has been fixed on the GUI side. 

## dEBRUYNE-1 | 2019-11-26T08:33:36+00:00
+resolved

# Action History
- Created by: wallaceturner | 2019-11-25T05:14:58+00:00
- Closed at: 2019-11-26T08:41:36+00:00
