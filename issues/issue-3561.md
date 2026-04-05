---
title: Failed to start threads on Raspberry
source_url: https://github.com/xmrig/xmrig/issues/3561
author: Germardies
assignees: []
labels: []
created_at: '2024-10-13T08:59:04+00:00'
updated_at: '2025-06-18T22:06:34+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:06:34+00:00'
---

# Original Description
I have installed xmrig on my RaspberryPi.

But I get an error message after starting:
```
[2024-10-13 10:45:02.359]  cpu      thread #3 self-test failed
[2024-10-13 10:45:02.437]  cpu      thread #2 self-test failed
[2024-10-13 10:45:02.438]  cpu      thread #1 self-test failed
[2024-10-13 10:45:02.439]  cpu      thread #0 self-test failed
[2024-10-13 10:45:02.439]  cpu      disabled (failed to start threads)
```

This is how I installed it:
```
sudo apt update && sudo apt full-upgrade -y
sudo apt install git build-essential cmake libuv1-dev libssl-dev libhwloc-dev -y
git clone https://github.com/xmrig/xmrig.git
cd xmrig
mkdir build
cd build
cmake ..
make
```

![image](https://github.com/user-attachments/assets/409c06d2-70eb-405a-87c1-d61a924fff62)


# Discussion History
## scapegrace13 | 2025-01-03T19:42:32+00:00
Hey guys,

I am experiencing the same issue, even with threads parameter deleted (and 4 threads) all fail.

![raspi4_GR_xmrig_error](https://github.com/user-attachments/assets/9adea55f-9599-44ec-87c5-1aff3743abb3)

This command with RVN is running nicely:

`./xmrig -a rx -o stratum+ssl://rx.unmineable.com:443 -u RVN:WALLET.Raspi4b1 -p x -k -t 1 --max-cpu-usage 10 --cpu-priority 1`

# Action History
- Created by: Germardies | 2024-10-13T08:59:04+00:00
- Closed at: 2025-06-18T22:06:34+00:00
