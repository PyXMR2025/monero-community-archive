---
title: Add all descriptions cmake options
source_url: https://github.com/xmrig/xmrig/issues/982
author: snipeTR
assignees: []
labels: []
created_at: '2019-03-11T08:06:47+00:00'
updated_at: '2019-04-01T06:17:34+00:00'
type: issue
status: closed
closed_at: '2019-04-01T06:17:34+00:00'
---

# Original Description
![image](https://user-images.githubusercontent.com/31975916/54108676-aa996300-43ed-11e9-871d-52f967a50622.png)
![image](https://user-images.githubusercontent.com/31975916/54108697-b71dbb80-43ed-11e9-8a71-cc2dc8ee6232.png)

please add https://github.com/xmrig/xmrig/wiki/Windows-Build descriptions

# Discussion History
## snipeTR | 2019-03-11T08:49:29+00:00
> ![image](https://user-images.githubusercontent.com/31975916/54108676-aa996300-43ed-11e9-871d-52f967a50622.png)
> ![image](https://user-images.githubusercontent.com/31975916/54108697-b71dbb80-43ed-11e9-8a71-cc2dc8ee6232.png)
> 
> please add https://github.com/xmrig/xmrig/wiki/Windows-Build descriptions

-DWITH_LIBCPUID=OFF Disable libcpuid. Auto configuration of CPU after this will be very limited.

-DWITH_AEON=OFF Disable CryptoNight-Lite support.

-DWITH_SUMO=OFF disable CryptoNight-Heavy support

-DWITH_CN_PICO=OFF DİSABLE "CryptoNight-Pico support"

-DWITH_CN_GPU=OFF disable CryptoNight-GPU support

-DWITH_HTTPD=OFF Build without built in http server and API.

-DWITH_DEBUG_LOG=OFF disable debug log output

-DWITH_TLS=OFF Disable SSL/TLS support.

-DWITH_ASM=OFF Disable ASM accelerated cryptonight/2.

-DBUILD_STATIC=OFF Disable Build static binary

-DWITH_EMBEDDED_CONFIG=OFF Enable internal embedded JSON config

## xmrig | 2019-03-11T12:01:36+00:00
Done. Thank you.

# Action History
- Created by: snipeTR | 2019-03-11T08:06:47+00:00
- Closed at: 2019-04-01T06:17:34+00:00
