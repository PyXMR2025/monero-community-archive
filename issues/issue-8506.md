---
title: Offset arg undocumented for import_key_images
source_url: https://github.com/monero-project/monero/issues/8506
author: mrtestyboy781
assignees: []
labels: []
created_at: '2022-08-15T19:34:05+00:00'
updated_at: '2024-07-31T23:18:41+00:00'
type: issue
status: closed
closed_at: '2024-07-31T23:18:41+00:00'
---

# Original Description
https://www.getmonero.org/resources/developer-guides/wallet-rpc.html#import_key_images is missing documentation for `offset` param in the `import_key_images` rpc command. When performing very large key imports the monero_wallet_rpc throws error 
```
{
 "error": {
   "code": -38,
   "message": "no connection to daemon"
 },
```

Logs from wallet-rpc
```
2022-08-15 18:21:19.183 T Throttle <<< global-IN: packet of ~8192b  (from 8192 b) Speed AVG=89788[w=1.995] 89788[w=1.995] /  Limit=16 KiB/sec  [45244416 138190848 160 0 0 0 0 0 0 0 ]
2022-08-15 18:21:19.183 T Throttle throttle_speed_in: packet of ~8192b  (from 8192 b) Speed AVG=89792[w=1.995] 89792[w=1.995] /  Limit=16 KiB/sec  [45252608 138190848 160 0 0 0 0 0 0 0 ]
2022-08-15 18:21:19.183 T Throttle <<< global-IN: packet of ~8192b  (from 8192 b) Speed AVG=89792[w=1.995] 89792[w=1.995] /  Limit=16 KiB/sec  [45252608 138190848 160 0 0 0 0 0 0 0 ]
2022-08-15 18:21:19.183 T Throttle throttle_speed_in: packet of ~8192b  (from 8192 b) Speed AVG=89796[w=1.995] 89796[w=1.995] /  Limit=16 KiB/sec  [45260800 138190848 160 0 0 0 0 0 0 0 ]
2022-08-15 18:21:19.183 T Throttle <<< global-IN: packet of ~8192b  (from 8192 b) Speed AVG=89796[w=1.995] 89796[w=1.995] /  Limit=16 KiB/sec  [45260800 138190848 160 0 0 0 0 0 0 0 ]
2022-08-15 18:21:19.183 T Throttle throttle_speed_in: packet of ~8192b  (from 8192 b) Speed AVG=89800[w=1.995] 89800[w=1.995] /  Limit=16 KiB/sec  [45268992 138190848 160 0 0 0 0 0 0 0 ]
2022-08-15 18:21:19.183 T Throttle <<< global-IN: packet of ~8192b  (from 8192 b) Speed AVG=89800[w=1.995] 89800[w=1.995] /  Limit=16 KiB/sec  [45268992 138190848 160 0 0 0 0 0 0 0 ]
2022-08-15 18:21:19.183 T Throttle throttle_speed_in: packet of ~5432b  (from 5432 b) Speed AVG=89804[w=1.995] 89804[w=1.995] /  Limit=16 KiB/sec  [45274424 138190848 160 0 0 0 0 0 0 0 ]
2022-08-15 18:21:19.183 T Throttle <<< global-IN: packet of ~5432b  (from 5432 b) Speed AVG=89804[w=1.995] 89804[w=1.995] /  Limit=16 KiB/sec  [45274424 138190848 160 0 0 0 0 0 0 0 ]
2022-08-15 18:21:19.184 I HTTP [127.0.0.1] POST /json_rpc
2022-08-15 18:21:20.674 I [127.0.0.1:26902 INC] Calling RPC method import_key_images
2022-08-15 18:21:21.841 T Problems at write: Broken pipe
2022-08-15 18:21:21.841 E HTTP_CLIENT: Failed to SEND
2022-08-15 18:21:21.841 I Failed to invoke http request to  /is_key_image_spent
2022-08-15 18:21:21.843 E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
```

The solution is to chunk the key import by offset, which is undocumented 

# Discussion History
## plowsof | 2022-08-15T22:07:44+00:00
Nice! question, i dont understand how an offset achieves chunking? if i send 1 million key images with an offset of 10, will this send 1 key image at position 10? send everything in chunks of 10? use an inbuilt chunk value of x?

## selsta | 2022-08-15T22:13:43+00:00
I have opened this now: https://github.com/monero-project/monero-site/pull/2023

## moneromooo-monero | 2022-08-16T13:36:05+00:00
It it key images 10-1000009.

## mmbbee | 2023-06-12T12:36:42+00:00
Issue is resolved now, can be closed

# Action History
- Created by: mrtestyboy781 | 2022-08-15T19:34:05+00:00
- Closed at: 2024-07-31T23:18:41+00:00
