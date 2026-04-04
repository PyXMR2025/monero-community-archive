---
title: 'build of current master fails on mac osx '
source_url: https://github.com/monero-project/monero/issues/2093
author: schnerchi
assignees: []
labels: []
created_at: '2017-06-18T22:27:48+00:00'
updated_at: '2017-06-19T08:14:43+00:00'
type: issue
status: closed
closed_at: '2017-06-19T08:14:43+00:00'
---

# Original Description
I think this is stopping it : 

/dev/bitmonero/contrib/epee/include/net/net_utils_base.h:131:19: error: use 'template' keyword to treat 'as' as a dependent template name
                                        KV_SERIALIZE(as<ipv4_network_address>());
                                                     ^
                                                     template 


# Discussion History
## kenshi84 | 2017-06-18T23:24:58+00:00
Addressed by #2094 

## schnerchi | 2017-06-19T08:14:43+00:00
works!

# Action History
- Created by: schnerchi | 2017-06-18T22:27:48+00:00
- Closed at: 2017-06-19T08:14:43+00:00
