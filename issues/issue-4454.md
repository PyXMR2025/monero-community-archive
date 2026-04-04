---
title: Monerod 0.12.3.0 seg fault on MacOS 10.13.6
source_url: https://github.com/monero-project/monero/issues/4454
author: Zaphod101010
assignees: []
labels: []
created_at: '2018-09-26T13:46:10+00:00'
updated_at: '2022-02-22T21:45:58+00:00'
type: issue
status: closed
closed_at: '2022-02-22T21:45:58+00:00'
---

# Original Description
node had been running for a few weeks.  I woke up this morning and it had crashed at some point over night.

[monerod_2018-09-25-183645.log](https://github.com/monero-project/monero/files/2419955/monerod_2018-09-25-183645.log)


# Discussion History
## moneromooo-monero | 2018-09-26T14:02:19+00:00
Looks like an internal boost function called when a network operation has completed. It could be a boost bug, or monerod deleting an object which a boost async function still references. Is there anything interesting in the log shortly before the crash ?

## Zaphod101010 | 2018-09-29T16:04:33+00:00
Nothing interesting in the logs.

I have rpc turned on, in restricted mode with a username and password, so I can use my node with cake wallet...  but other than that everything is normal.

## moneromooo-monero | 2018-10-01T11:27:28+00:00
This has happened once only ?

## Zaphod101010 | 2018-10-01T14:04:08+00:00
Yes, this has only happened once.

## selsta | 2022-02-22T21:45:58+00:00
There were a lot of crash related fixes in the last releases, please try v0.17.3.0 and open a new issue if you continue to have issues.

# Action History
- Created by: Zaphod101010 | 2018-09-26T13:46:10+00:00
- Closed at: 2022-02-22T21:45:58+00:00
