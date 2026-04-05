---
title: Cannot enable 1GB pages on Ubuntu 20.04
source_url: https://github.com/xmrig/xmrig/issues/2601
author: Unnameless
assignees: []
labels: []
created_at: '2021-09-23T11:23:51+00:00'
updated_at: '2021-09-23T12:12:02+00:00'
type: issue
status: closed
closed_at: '2021-09-23T12:12:02+00:00'
---

# Original Description
Hello,

I tried all the usual stuff, ran xmrig with sudo, tried the enable 1GB pages shell script, nothing really works. I can't seem to enable 1GB pages. 

```
:~/Desktop$ sudo ./1gb.sh 
vm.nr_hugepages = 256
1GB pages successfully enabled

:~/Desktop$ cat /etc/sysctl.conf | grep "huge"
vm.nr_hugepages=1280


```

Ran the miner as sudo and still nothing.
![Screenshot from 2021-09-22 21-47-11](https://user-images.githubusercontent.com/36138092/134498652-1bb6e7a4-80d7-4199-935d-acab9580ce33.png)


# Discussion History
## SChernykh | 2021-09-23T11:35:43+00:00
Did you set `"1gb-pages": true,` in config.json?

## Unnameless | 2021-09-23T12:12:02+00:00
I am dub! Completely forgot about that! Sorry! I'll see myself out...

# Action History
- Created by: Unnameless | 2021-09-23T11:23:51+00:00
- Closed at: 2021-09-23T12:12:02+00:00
