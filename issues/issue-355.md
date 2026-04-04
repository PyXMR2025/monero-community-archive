---
title: Non-portable type used in wire protocol definition
source_url: https://github.com/monero-project/monero/issues/355
author: iamsmooth
assignees: []
labels: []
created_at: '2015-07-27T13:26:18+00:00'
updated_at: '2025-01-14T14:30:05+00:00'
type: issue
status: closed
closed_at: '2025-01-14T14:30:04+00:00'
---

# Original Description
Similar to issue #88, connection_entry in p2p_protocol_defs.h contains is_income (misspelling of is_incoming I believe) which is defined as a bool. The size of bool is implementation-defined.

Fortunately connection_entry is only used for node debugging, which we may not even have enabled. Nevertheless the code should be fixed if it isn't going to be removed.


# Discussion History
## moneromooo-monero | 2017-08-08T11:09:35+00:00
I think this is invalid, as the struct is not written as is, but the fields are serialized independently, and bool has an overload in the serialization code.

## iamsmooth | 2017-08-12T03:19:05+00:00
Quite possible. Where is this overload? 

## moneromooo-monero | 2017-08-12T11:24:38+00:00
It's in the list of handled types in:
struct base_serializable_types: public boost::mpl::vector<uint64_t, uint32_t, uint16_t, uint8_t, int64_t, int32_t, int16_t, int8_t, double, bool, std::string, typename t_storage::meta_entry>::type
but after that, I can't follow the serialize template code to know exactly where it does. I suspect serialize_int, but I'm not sure.

# Action History
- Created by: iamsmooth | 2015-07-27T13:26:18+00:00
- Closed at: 2025-01-14T14:30:04+00:00
