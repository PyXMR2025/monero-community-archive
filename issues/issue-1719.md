---
title: 'Could not find the following static Boost libraries: boost_thread (missing
  dependency: Threads)'
source_url: https://github.com/monero-project/monero-gui/issues/1719
author: CokeBear666
assignees: []
labels:
- resolved
created_at: '2018-11-02T09:38:11+00:00'
updated_at: '2018-11-29T07:27:24+00:00'
type: issue
status: closed
closed_at: '2018-11-29T07:27:24+00:00'
---

# Original Description
**### When I execute the ./ios_get_libwallet.api.sh , I get an exception.
Mac os v10.14**

![image](https://user-images.githubusercontent.com/6119459/47907147-9edce380-dec5-11e8-9880-99df42540920.png)

**### And I can see libboost_thread-mt.a  and  libboost_thread-mt.dylib  in my package .**
![image](https://user-images.githubusercontent.com/6119459/47907437-37736380-dec6-11e8-83e6-b5ffb15c13aa.png)



# Discussion History
## sanderfoobar | 2018-11-02T12:21:39+00:00
Try a more recent version of Boost. I am on 1.65 and 1.67. In addition, during Boost compilation you  can check what parts of Boost are being installed.

## BigslimVdub | 2018-11-29T04:43:10+00:00
latest boost on brew should be 1.68.0

 " To reinstall 1.68.0, run `brew reinstall boost`"

## sanderfoobar | 2018-11-29T07:23:59+00:00
+resolved

# Action History
- Created by: CokeBear666 | 2018-11-02T09:38:11+00:00
- Closed at: 2018-11-29T07:27:24+00:00
