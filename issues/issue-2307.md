---
title: Another osx build warning
source_url: https://github.com/monero-project/monero/issues/2307
author: jtgrassie
assignees: []
labels: []
created_at: '2017-08-18T11:44:46+00:00'
updated_at: '2017-09-20T17:05:25+00:00'
type: issue
status: closed
closed_at: '2017-09-20T17:05:25+00:00'
---

# Original Description
```
/Users/jethro/Projects/monero/external/db_drivers/liblmdb/mdb.c:10731:46: warning: data argument not used by format string [-Wformat-extra-args]
                                (int)mr[i].mr_pid, (size_t)mr[i].mr_tid, txnid);
                                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~
/usr/include/secure/_stdio.h:47:56: note: expanded from macro 'sprintf'
  __builtin___sprintf_chk (str, 0, __darwin_obsz(str), __VA_ARGS__)
                                                       ^~~~~~~~~~~
```

# Discussion History
## hyc | 2017-08-18T12:06:07+00:00
The warning is incorrect. The argument is used, but only sometimes, since the format string is conditionalized.

## jtgrassie | 2017-08-18T12:09:25+00:00
Understood, but we need to find a way of suppressing individual warnings when it's known as a false flag IMHO.

# Action History
- Created by: jtgrassie | 2017-08-18T11:44:46+00:00
- Closed at: 2017-09-20T17:05:25+00:00
