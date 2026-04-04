---
title: Creating a new wallet using a hardware device has a buggy label for the restore
  option
source_url: https://github.com/monero-project/monero-gui/issues/2020
author: sudo-run-dos-run
assignees: []
labels:
- resolved
created_at: '2019-03-15T20:43:14+00:00'
updated_at: '2019-05-02T00:45:39+00:00'
type: issue
status: closed
closed_at: '2019-05-02T00:45:39+00:00'
---

# Original Description
I cannot say how it's meant to look like but it's obviously broken in some way.

![mon-gui-hw-wallet-bug](https://user-images.githubusercontent.com/3670192/54460821-f3914480-476a-11e9-8e32-e52913b39c87.png)


# Discussion History
## selsta | 2019-03-15T21:07:34+00:00
This is a Qt 5.7 issue. Until it is fixed you can access the restore height text box by inserting your cursor inside the `Wallet location` text box and pressing tab once.

## dEBRUYNE-1 | 2019-03-17T15:55:21+00:00
#2021

## lacksfish | 2019-03-17T16:55:53+00:00
Ran into the same issue, https://github.com/monero-project/monero-gui/pull/2021 should fix that

(you'd have to build the GUI from that branch or wait for a release)

## selsta | 2019-05-02T00:41:44+00:00
+resolved

# Action History
- Created by: sudo-run-dos-run | 2019-03-15T20:43:14+00:00
- Closed at: 2019-05-02T00:45:39+00:00
