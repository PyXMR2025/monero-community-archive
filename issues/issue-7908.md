---
title: 'Can''t create transaction: unexpected error: Unable to send hiapi command
  Error 64'
source_url: https://github.com/monero-project/monero/issues/7908
author: hendrash
assignees: []
labels: []
created_at: '2021-08-30T01:53:53+00:00'
updated_at: '2021-08-30T01:59:52+00:00'
type: issue
status: closed
closed_at: '2021-08-30T01:55:10+00:00'
---

# Original Description
2021-08-30 01:48:17.253	E Unable to send hidapi command. Error 64: Unknown error
2021-08-30 01:48:17.253	W QObject: Cannot create children for a parent that is in a different thread.
2021-08-30 01:48:17.253	W (Parent is Wallet(0x7f9a501b4410), parent's thread is QThread(0x55987e493e10), current thread is QThreadPoolThread(0x55987e54d440)
2021-08-30 01:48:17.261	E Can't create transaction:  unexpected error: Unable to send hidapi command. Error 64: Unknown error
2021-08-30 01:48:17.263	W "Could not convert argument 0 at"
2021-08-30 01:48:17.263	W 	 "onTransactionCreated@qrc:/main.qml:822"
2021-08-30 01:48:17.263	W "Passing incompatible arguments to C++ functions from JavaScript is dangerous and deprecated."
2021-08-30 01:48:17.263	W "This will throw a JavaScript TypeError in future releases of Qt!"

![Screenshot from 2021-08-29 21-54-16](https://user-images.githubusercontent.com/26557257/131274797-163c2362-704c-457b-aa9d-db5eec6dfb24.png)



# Discussion History
## selsta | 2021-08-30T01:55:10+00:00
Let's continue in #7907 

## hendrash | 2021-08-30T01:59:52+00:00
> Let's continue in #7907
Sorry I was trying to make an issue under the GUI as I saw there was a separate repo for that and close the other issue


# Action History
- Created by: hendrash | 2021-08-30T01:53:53+00:00
- Closed at: 2021-08-30T01:55:10+00:00
