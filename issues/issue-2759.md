---
title: serialization
source_url: https://github.com/monero-project/monero/issues/2759
author: zhangdaoling
assignees: []
labels:
- invalid
created_at: '2017-11-04T07:06:42+00:00'
updated_at: '2017-11-09T13:00:27+00:00'
type: issue
status: closed
closed_at: '2017-11-09T13:00:27+00:00'
---

# Original Description
I want to develop open source implementations of serialize and sign for golang.
my question is :should i use uint64 or uin32 for size_t when doing serialize?
do I miss something?

the c++ code use many "size_t" 
for example:  "monero/src/serialization/string.h"

template <template <bool> class Archive>
inline bool do_serialize(Archive<true>& ar, std::string& str)
{
  size_t size = str.size();
  ar.serialize_varint(size);
  ar.serialize_blob(const_cast<std::string::value_type*>(str.c_str()), size);
  return true;
}



# Discussion History
## glv2 | 2017-11-04T14:08:03+00:00
Integers are not serialized as raw uint32 or uint64, but as variable size integers (see #2340).


## moneromooo-monero | 2017-11-09T12:56:10+00:00
I'd use uint64_t. That way you can handle > 4 GB data :) In practice I think this will only happen if your implementation is attacked, so make sure you test the case :)

Closing as it's not a but report or feature request.

+invalid


# Action History
- Created by: zhangdaoling | 2017-11-04T07:06:42+00:00
- Closed at: 2017-11-09T13:00:27+00:00
