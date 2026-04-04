---
title: really ignore battery-checking if --ignore-battery option is given
source_url: https://github.com/monero-project/monero/issues/2886
author: Piraty
assignees: []
labels:
- bug
created_at: '2017-12-05T16:19:15+00:00'
updated_at: '2018-02-20T15:47:15+00:00'
type: issue
status: closed
closed_at: '2018-02-20T15:47:15+00:00'
---

# Original Description
you should reverse the logic and call that function only if --ignore-battery flag is not used

https://github.com/monero-project/monero/blob/8512a83572094f96aff95e02db359914a37c3c71/src/cryptonote_basic/miner.cpp#L622-L638

sth like 
```
if( m_ignore_battery )
  on_ac_power = true;
else
{
  boost::tribool battery_powered(on_battery_power());
  ...
}
```

because my system, despite having the flag set, issues warnings that it can't find the powersupply status (because there is none).
`ERROR   miner   src/cryptonote_basic/miner.cpp:940      couldn't query power status from /sys/class/power_supply`

# Discussion History
## dEBRUYNE-1 | 2018-01-08T12:31:56+00:00
+bug

# Action History
- Created by: Piraty | 2017-12-05T16:19:15+00:00
- Closed at: 2018-02-20T15:47:15+00:00
