---
title: devguides wallet/daemon rpc missing params
source_url: https://github.com/monero-project/monero-site/issues/2253
author: plowsof
assignees: []
labels: []
created_at: '2024-03-01T11:40:26+00:00'
updated_at: '2024-10-07T07:40:48+00:00'
type: issue
status: closed
closed_at: '2024-10-07T07:40:48+00:00'
---

# Original Description
https://github.com/monero-project/monero/issues/9186#issuecomment-1973003427
> > I went through the RPC docs a ~year ago and updated pretty much everything.
> 
> For reference, here what I found out of date in the core RPC:
> 
> * `get_connections` lacked in his response field `connections` the fields `address_type`, `rpc_credits_per_hash` and `rpc_port`
> * `get_version` lacked in his response the fields `current_height` and `hard_forks` array (as well as its underlying object)
> * `get_output_distribution` lacked in his parameters the field `binary` (for disabling epee encoding) and `compress` (for disabling compression)
> 
> There are also methods like `sync_info` that did not contain in their outputs the `top_hash`, `credits` or `untrusted` fields.



# Discussion History
## SyntheticBird45 | 2024-03-01T11:47:31+00:00
address_type: 0 = invalid, 1 = ipv4 and 2 = ipv6.
compress = ignored if binary is set to false

## HardenedSteel | 2024-10-07T00:56:39+00:00
can be moved to: https://github.com/monero-project/monero-docs

## nahuhh | 2024-10-07T03:34:23+00:00
I'm not sure about @SyntheticBird45 's comment, but the relevant PRs were merged on docs

# Action History
- Created by: plowsof | 2024-03-01T11:40:26+00:00
- Closed at: 2024-10-07T07:40:48+00:00
