---
title: Fails to build with Boost 1.69 (develop snapshot)
source_url: https://github.com/monero-project/monero/issues/4695
author: jbeich
assignees: []
labels: []
created_at: '2018-10-22T18:35:56+00:00'
updated_at: '2019-01-22T03:11:17+00:00'
type: issue
status: closed
closed_at: '2018-10-26T21:01:13+00:00'
---

# Original Description
After boostorg/logic@23cd89d4c80f build fails. See [error log](https://ptpb.pw/Y-V9).
```c++
src/cryptonote_basic/miner.cpp:640:25: error: assigning to 'bool' from incompatible type 'boost::logic::tribool'
          on_ac_power = !battery_powered;
                        ^~~~~~~~~~~~~~~~
```


# Discussion History
## moneromooo-monero | 2018-10-22T21:12:33+00:00
Does this fix it ?

<pre>
diff --git a/src/cryptonote_basic/miner.cpp b/src/cryptonote_basic/miner.cpp
index d0b03593e..d8ca2dd35 100644
--- a/src/cryptonote_basic/miner.cpp
+++ b/src/cryptonote_basic/miner.cpp
@@ -637,7 +637,7 @@ namespace cryptonote
         boost::tribool battery_powered(on_battery_power());
         if(!indeterminate( battery_powered ))
         {
-          on_ac_power = !battery_powered;
+          on_ac_power = !(bool)battery_powered;
         }
       }
 
</pre>


## jbeich | 2018-10-22T22:07:44+00:00
@moneromooo-monero, yes, it fixes build. `(bool)...`, `bool(...)`, `bool{...}` work. However, `!(bool)...` and `(bool)!...` are **not** the same if `...` evaluates to `boost::indeterminate`.

## moneromooo-monero | 2018-10-22T22:16:56+00:00
That's fine in this case since it's only run if it is not indeterminate.

## moneromooo-monero | 2018-10-22T22:20:35+00:00
https://github.com/monero-project/monero/pull/4700

## moneromooo-monero | 2018-10-26T20:53:16+00:00
+resolved

## Franzferdinan51 | 2019-01-22T03:11:16+00:00
one would apply this patch where? i have the same issue sorry to reopen 

# Action History
- Created by: jbeich | 2018-10-22T18:35:56+00:00
- Closed at: 2018-10-26T21:01:13+00:00
