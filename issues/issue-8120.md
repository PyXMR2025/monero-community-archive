---
title: load of value, which is not a valid value for type 'bool'  discovered by LibFuzzer
source_url: https://github.com/monero-project/monero/issues/8120
author: swirsz
assignees: []
labels: []
created_at: '2021-12-23T04:55:30+00:00'
updated_at: '2022-05-29T15:36:13+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
2 similar bugs detected via Libfuzzer & UndefinedBehaviorSanitizer.

./levin_fuzz_tests crash-1a5

[crash-1a5.txt](https://github.com/monero-project/monero/files/7766778/crash-1a5.txt)

/src/monero/monero/contrib/epee/include/net/levin_protocol_handler_async.h:543:31: runtime error: load of value 247, which is not a valid value for type 'bool'
SUMMARY: UndefinedBehaviorSanitizer: 


./load-from-binary_fuzz_tests crash-f31

[crash-f31.txt](https://github.com/monero-project/monero/files/7766781/crash-f31.txt)

/src/monero/monero/contrib/epee/include/storages/portable_storage_from_bin.h:157:17: runtime error: load of value 249, which is not a valid value for type 'bool'
SUMMARY: UndefinedBehaviorSanitizer


# Discussion History
## moneromooo-monero | 2021-12-23T10:21:59+00:00
Those seem easy to fix with !!. Thanks.

# Action History
- Created by: swirsz | 2021-12-23T04:55:30+00:00
