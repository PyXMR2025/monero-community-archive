---
title: OSX build failing
source_url: https://github.com/monero-project/monero/issues/2096
author: jtgrassie
assignees: []
labels: []
created_at: '2017-06-19T11:58:37+00:00'
updated_at: '2017-07-03T22:09:51+00:00'
type: issue
status: closed
closed_at: '2017-07-03T22:09:51+00:00'
---

# Original Description
Build on OSX now failing:
`/monero/contrib/epee/include/net/net_utils_base.h:118:54: warning: expression with side effects will be evaluated despite being used as an
      operand to 'typeid' [-Wpotentially-evaluated-expression]
                const std::type_info &type() const { return typeid(**this); }
                                                                   ^
/monero/contrib/epee/include/net/net_utils_base.h:131:19: error: use 'template' keyword to treat 'as' as a dependent template name
                                        KV_SERIALIZE(as<ipv4_network_address>());
                                                     ^
                                                     template 
/monero/contrib/epee/include/serialization/keyvalue_serialization.h:85:74: note: expanded from macro 'KV_SERIALIZE'
#define KV_SERIALIZE(varialble)                           KV_SERIALIZE_N(varialble, #varialble)
                                                                         ^
/monero/contrib/epee/include/serialization/keyvalue_serialization.h:71:63: note: expanded from macro 'KV_SERIALIZE_N'
  epee::serialization::selector<is_store>::serialize(this_ref.varialble, stg, hparent_section, val_name);`


# Discussion History
## danrmiller | 2017-06-19T12:12:55+00:00
Fixed in #2094 

## jtgrassie | 2017-06-19T12:20:15+00:00
#2094 fixes the build error on Mac but does it have side effects for other platforms?

## danrmiller | 2017-06-19T12:30:15+00:00
I'm not the best person to speak to the substance of the change, but #2094 builds on all our platforms including non mac osx (the tests don't build but those are fixed in #2095).

## jtgrassie | 2017-06-19T12:33:26+00:00
Just did a Ubuntu build and works OK there too. 
Those pesky test errors - I'll be pleased when that PR gets merged.

## kenshi84 | 2017-06-19T12:54:43+00:00
It should compile on other platforms since the change makes the code more conforming to the C++ standard.

# Action History
- Created by: jtgrassie | 2017-06-19T11:58:37+00:00
- Closed at: 2017-07-03T22:09:51+00:00
