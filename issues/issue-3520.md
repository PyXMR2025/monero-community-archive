---
title: Can't use xmrig in rpi4
source_url: https://github.com/xmrig/xmrig/issues/3520
author: alfonsop123
assignees: []
labels: []
created_at: '2024-07-30T03:57:51+00:00'
updated_at: '2025-06-18T22:12:47+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:12:47+00:00'
---

# Original Description

alfonsop123@raspberrypi:~/xmrig-6.21.3 $ sudo ./xmrig
./xmrig: 1: ELF: not found
./xmrig: 2: Syntax error: word unexpected (expecting ")")
alfonsop123@raspberrypi:~/xmrig-6.21.3 $ rm config.json
rm: remove write-protected regular file 'config.json'? y
alfonsop123@raspberrypi:~/xmrig-6.21.3 $ sudo ./xmrig
./xmrig: 1: ELF: not found
./xmrig: 2: Syntax error: word unexpected (expecting ")")
alfonsop123@raspberrypi:~/xmrig-6.21.3 $

# Discussion History
# Action History
- Created by: alfonsop123 | 2024-07-30T03:57:51+00:00
- Closed at: 2025-06-18T22:12:47+00:00
