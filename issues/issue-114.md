---
title: Issue with failover pools.
source_url: https://github.com/xmrig/xmrig/issues/114
author: lolcocks123
assignees: []
labels: []
created_at: '2017-09-18T13:20:33+00:00'
updated_at: '2017-09-18T13:38:46+00:00'
type: issue
status: closed
closed_at: '2017-09-18T13:37:55+00:00'
---

# Original Description
Hello, I have integrated my pools into the exe using the below code:

`m_pools.push_back(new Url("pool.example.com", 3333, "WALLET", "PASSWORD"));`

I have integrated multiple pools.

To test them out, I blocked the first pool using the Windows Hosts file located at

`C:\Windows\System32\drivers\etc\hosts`

When I did that, after failing to connect to pool for the first 5 attempts, xmrig connected to the second failover pool and then instantly reverted back to the first pool and was stuck with the first pool forever.
Check the screenshot below:

![1](https://user-images.githubusercontent.com/16006564/30543671-9d25764a-9ca1-11e7-9c7b-1dc549eef3ef.png)

After that, I disabled connection to the second pool as well as the first one in the hosts file, which also produced similar results.

![2](https://user-images.githubusercontent.com/16006564/30543724-c1ca2112-9ca1-11e7-8275-18dd0092ecce.png)

Any idea how to fix this?

EDIT:
Oh and I forgot to mention, xmrig fails to mine to the failover pools with regards to the above issue.

EDIT 2:
This happens with the release unmodified version of xmrig as well.

# Discussion History
## xmrig | 2017-09-18T13:31:16+00:00
Right error messages confusing, but it works as expected on first screenshot used pool 2 and on second used 3, see pool address in new job messages. It just try recover connection and not affect current connection. After primary pool available again it will switch back.
Thank you.

## lolcocks123 | 2017-09-18T13:37:55+00:00
Ahh, I see.
I did not know that xmrig will switch back to the primary pool (or atleast try to switch) while it's using failover pools.

Thank you for your great support once again @xmrig .

# Action History
- Created by: lolcocks123 | 2017-09-18T13:20:33+00:00
- Closed at: 2017-09-18T13:37:55+00:00
