---
title: reference binding to null pointer discovered via LibFuzzer
source_url: https://github.com/monero-project/monero/issues/8119
author: swirsz
assignees: []
labels: []
created_at: '2021-12-23T04:43:40+00:00'
updated_at: '2021-12-24T17:40:06+00:00'
type: issue
status: closed
closed_at: '2021-12-24T17:40:06+00:00'
---

# Original Description
Bug detected via Libfuzzer & UndefinedBehaviorSanitizer.

./cold-outputs_fuzz_tests crash-c1c.txt

/src/monero/boost_1_70_0/boost/serialization/singleton.hpp:181:13: runtime error: reference binding to null pointer of type 'const boost::archive::detail::extra_detail::map<boost::archive::portable_binary_iarchive>'
SUMMARY: UndefinedBehaviorSanitizer

[crash-c1c.txt](https://github.com/monero-project/monero/files/7766724/crash-c1c.txt)



# Discussion History
## moneromooo-monero | 2021-12-23T10:22:56+00:00
That should be reported to boost.

# Action History
- Created by: swirsz | 2021-12-23T04:43:40+00:00
- Closed at: 2021-12-24T17:40:06+00:00
