---
title: XMRig 5.3.0 - enabling 1GB leads to significant hashrate reducing
source_url: https://github.com/xmrig/xmrig/issues/1430
author: Shekelme
assignees: []
labels:
- question
created_at: '2019-12-16T04:53:07+00:00'
updated_at: '2020-08-28T16:43:01+00:00'
type: issue
status: closed
closed_at: '2020-08-28T16:43:01+00:00'
---

# Original Description
After I executed the `enable_1gb_pages.sh` I've got the following result:

![image](https://user-images.githubusercontent.com/26449500/70880136-772dd980-1ffa-11ea-9843-68a76820b126.png)

And the hashrate lowered from 9150 to 5613...

# Discussion History
## xmrig | 2019-12-16T06:34:57+00:00
You not set `"1gb-pages": true,` in `"randomx"` object in config file.
Thank you.

## Spudz76 | 2019-12-17T23:03:31+00:00
the 1GB script reduces your 2MB hugepages
and you didn't turn on 1GB mode so it is running on not-enough 2MB hugepages

## Shekelme | 2019-12-18T02:15:46+00:00
Looks like I understand - there will be less hugepages but hugepages will be of bigger size.

## Spudz76 | 2019-12-19T23:55:10+00:00
No, some parts of the miner use the 2MB hugepages either way.  The script sets the count of 2MB hugepages to number of processors which is not enough for all algos

Only RandomX and its variants can use 1GB hugepages.  And even then it uses a few 2MB ones, I think.

So for best multi-algo results you would need both the full allocation of 1280 hugepages and the 3 1GB hugepages.  Either edit the enable script to change the hugepages from nproc to 1280, or do `sysctl vm.nr_hugepages=1280` after running the enable script.

Also check `ulimit -l` which should be at least `5905580032` which is `(1280*2 + 3072)*1048576`

# Action History
- Created by: Shekelme | 2019-12-16T04:53:07+00:00
- Closed at: 2020-08-28T16:43:01+00:00
