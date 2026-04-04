---
title: 'gentoo build: missing readline for linking'
source_url: https://github.com/monero-project/monero-gui/issues/882
author: raspadev
assignees: []
labels:
- resolved
created_at: '2017-09-18T08:22:08+00:00'
updated_at: '2017-10-27T14:09:12+00:00'
type: issue
status: closed
closed_at: '2017-10-27T14:09:12+00:00'
---

# Original Description
Dear devs,

build from source fails on Gentoo with missing `-lreadline`:
```
$ gcc --version
gcc (Gentoo 5.4.0-r3 p1.3, pie-0.6.5) 5.4.0

QT_SELECT=5 ./build.sh
[...]
/home/user/monero-core/monero/lib/libepee.a(readline_buffer.cpp.o): In function `attempted_completion(char const*, int, int)':
readline_buffer.cpp:(.text+0x2): undefined reference to `rl_attempted_completion_over'
/home/user/monero-core/monero/lib/libepee.a(readline_buffer.cpp.o): In function `handle_line(char*)':
readline_buffer.cpp:(.text+0x1c4): undefined reference to `rl_done'
readline_buffer.cpp:(.text+0x25c): undefined reference to `rl_done'
readline_buffer.cpp:(.text+0x26a): undefined reference to `rl_set_prompt'
readline_buffer.cpp:(.text+0x27e): undefined reference to `add_history'
readline_buffer.cpp:(.text+0x284): undefined reference to `history_length'
readline_buffer.cpp:(.text+0x289): undefined reference to `history_set_pos'
readline_buffer.cpp:(.text+0x2b6): undefined reference to `rl_done'
[...]
```

Workaround:
```patch
diff --git a/monero-wallet-gui.pro b/monero-wallet-gui.pro
index 27c0477..c34674f 100644
--- a/monero-wallet-gui.pro
+++ b/monero-wallet-gui.pro
@@ -91,6 +91,7 @@ LIBS += -L$$WALLET_ROOT/lib \
		 -lwallet_merged \
		 -lepee \
		 -lunbound \
+		 -lreadline \
		 -leasylogging
 }
```
I'm not submitting a PR because I'm not sure if this is the right place for that and if it is possibly affecting other archs/builds/...

# Discussion History
## dEBRUYNE-1 | 2017-09-18T20:07:36+00:00
See #868. 

## dEBRUYNE-1 | 2017-10-27T13:47:22+00:00
+resolved

# Action History
- Created by: raspadev | 2017-09-18T08:22:08+00:00
- Closed at: 2017-10-27T14:09:12+00:00
