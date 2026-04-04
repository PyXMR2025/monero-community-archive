---
title: '[wallet] no stdout flush on wallet creation'
source_url: https://github.com/monero-project/monero/issues/9655
author: tankf33der
assignees: []
labels:
- wallet
created_at: '2024-12-26T17:49:00+00:00'
updated_at: '2025-01-17T07:08:20+00:00'
type: issue
status: closed
closed_at: '2025-01-17T07:08:19+00:00'
---

# Original Description
versions: - 0.18.3.3 and 0.18.3.4
 
I can repeat this ONLY on Alpine Linux 3.20, 3.21 (musl!).

Manjaro (ArchLinux) is OK!!!

https://asciinema.org/a/50bn1StLcSCY90zmBJsI0QT1V

No output for "Confirm password:" and it is tricky to complete a wallet creation wizard.

```
diff --git a/src/common/password.cpp b/src/common/password.cpp
index e6dff95ea..c0edf7a78 100644
--- a/src/common/password.cpp
+++ b/src/common/password.cpp
@@ -185,7 +185,7 @@ namespace
         return false;
       if (verify)
       {
-        std::cout << "Confirm password: ";
+        std::cout << "Confirm password: " << std::flush;
         if (!read_from_tty(pass2, hide_input))
           return false;
         if(pass1!=pass2)
```


# Discussion History
## tankf33der | 2024-12-26T17:56:38+00:00
Patched version works on Alpine now.

## selsta | 2025-01-17T07:08:19+00:00
Solved in #9656

# Action History
- Created by: tankf33der | 2024-12-26T17:49:00+00:00
- Closed at: 2025-01-17T07:08:19+00:00
