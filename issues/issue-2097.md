---
title: Lots of warnings on OSX build
source_url: https://github.com/monero-project/monero/issues/2097
author: jtgrassie
assignees: []
labels: []
created_at: '2017-06-19T12:26:16+00:00'
updated_at: '2017-07-03T22:10:10+00:00'
type: issue
status: closed
closed_at: '2017-07-03T22:10:10+00:00'
---

# Original Description
`/monero/contrib/epee/include/net/net_utils_base.h:118:54: warning: expression with side effects will be evaluated despite being used as an
      operand to 'typeid' [-Wpotentially-evaluated-expression]`

Caused by commit 072102cfd23c47d36f4d51875026339a767f22ae


# Discussion History
## jtgrassie | 2017-06-20T13:35:27+00:00
Having researched this quite a bit now it seems the only resolution is to disable the warning. The problem with that is that it may hide other future issues.
I'm happy to add the exclusion specifically for Mac builds if there is consensus. 

## moneromooo-monero | 2017-06-20T14:22:39+00:00
Could you share a couple of the most pertinent links please, I want to see what's said about it ?


## jtgrassie | 2017-06-20T14:37:51+00:00
@moneromooo-monero there are quite a few but I think these both sum up well why the warning is being emitted and how to disable.

http://trac.wxwidgets.org/ticket/16968 (and/or http://thread.gmane.org/gmane.comp.lib.wxwidgets.devel/162524)
https://jira.mongodb.org/browse/SERVER-17728


## hyc | 2017-06-20T18:54:37+00:00
Seems like this typeid stuff is gratuitous complexity. Just treat this the way unions in C are handled - define an explicit field that you store a type identifier in (like a sockaddr's address family field). You know that's what C++ is doing under the covers anyway, and all of this C++ glue isn't actually making the code any easier to write or to understand. You still have to eventually do a switch(address_type) somewhere, when you start adding support for other types of network addresses.

## jtgrassie | 2017-06-20T19:07:27+00:00
@hyc I couldn't agree more. As I never wrote the commit that introduced the warning, this PR at least gets rid of the warning rather than needing an immediate rewrite.

## jtgrassie | 2017-06-20T20:04:14+00:00
@hyc how about an abstract method `type()` which returns a `std::type_info` on the class `network_address_base`. Then subclasses like `ipv4_network_address` can implement by returning `typeid(ipv4_network_address)`. Lastly `network_address::type()` can be rewritten to `return *this->type()`. 
To be honest though, I'm not enamored by the overall design in which `network_address` is subclassing a `boost::shared_ptr`! 

## moneromooo-monero | 2017-06-21T13:44:53+00:00
It avoids having an extraneous enum and extra functions in each derived classes that just return their own enum value. Admittedly, the extraneous code might not be too much, though.

## moneromooo-monero | 2017-06-21T15:28:02+00:00
In fact, I seem to have added a get_type_id anyway, as it was needed for serialization, so the typeid one can be removed since there's already something else. I'd forgot I had had to do that.


## moneromooo-monero | 2017-06-28T08:03:46+00:00
https://github.com/monero-project/monero/pull/2128

# Action History
- Created by: jtgrassie | 2017-06-19T12:26:16+00:00
- Closed at: 2017-07-03T22:10:10+00:00
