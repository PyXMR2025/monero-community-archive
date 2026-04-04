---
title: Data allowance for throttling
source_url: https://github.com/monero-project/monero/issues/4601
author: Gingeropolous
assignees: []
labels: []
created_at: '2018-10-15T20:22:23+00:00'
updated_at: '2018-11-05T07:46:15+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The existing throttling feature leaves much to be desired. It throttles the rate, but you can still use 10s of GBs if you get a lot of peers etc. Some people don't run nodes because they fear hitting data caps from their ISPs, VPN, or VPS providers. 

What if we can have a setting that would provide a data allowance for seeding new nodes. E.g., 

``` --data-cap 1G day```

would put the cap at 1 gb a day

``` --data-cap 10G month```

would put the cap at 10 GB a month. 

After the daemon hits that cap, it stops offering bootstrapping / seeding service, and just relays transactions and/or blocks. 

+hacktoberfest

it might be too much for hacktoberfest.... it needs a database... ermagerd

# Discussion History
## stoffu | 2018-11-05T07:46:14+00:00
Appears to be related: #4393

# Action History
- Created by: Gingeropolous | 2018-10-15T20:22:23+00:00
