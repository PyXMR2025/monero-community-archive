---
title: xmr rpc 401 Unauthorized
source_url: https://github.com/monero-project/monero/issues/6186
author: NoBugBoy
assignees: []
labels: []
created_at: '2019-11-26T07:41:00+00:00'
updated_at: '2022-04-08T16:40:42+00:00'
type: issue
status: closed
closed_at: '2022-04-08T16:40:42+00:00'
---

# Original Description
--rpc-login

There is no problem with the specified user name and password. Now an error is reported:

<html><head><title>Unauthorized Access</title></head><body><h1>401 Unauthorized</h1></body></html>

Does anyone have java source code to see how to connect

![image](https://user-images.githubusercontent.com/33510892/69608722-ff0b6e00-1062-11ea-8b4e-d8bcde15ffde.png)

![image](https://user-images.githubusercontent.com/33510892/69608814-22ceb400-1063-11ea-81b9-d52d5cd39d4b.png)






# Discussion History
## vtnerd | 2019-11-26T16:05:48+00:00
This might be a CORs issue depending on how you are connecting.

## binlaniua | 2019-12-27T08:35:55+00:00
it's not basic auth, it's use digest auth

## moneromooo-monero | 2020-05-16T16:19:49+00:00
If no further information showing there's likely a bug, I'll close.

# Action History
- Created by: NoBugBoy | 2019-11-26T07:41:00+00:00
- Closed at: 2022-04-08T16:40:42+00:00
