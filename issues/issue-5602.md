---
title: compiler warning with rpc_handler.cpp, memory specified size exceeds maximum
  object size
source_url: https://github.com/monero-project/monero/issues/5602
author: sherifomran
assignees: []
labels: []
created_at: '2019-06-02T14:16:25+00:00'
updated_at: '2019-08-27T15:09:59+00:00'
type: issue
status: closed
closed_at: '2019-08-27T15:09:59+00:00'
---

# Original Description
While compling the monero on linux i get this warning !

[135/220 0.3/sec] Building CXX object src/rpc/CMakeFiles/obj_rpc.dir/rpc_handler.cpp.o
In static member function ‘static boost::optional<cryptonote::rpc::output_distribution_data> cryptonote::rpc::RpcHandler::get_output_distribution(const std::function<bool(long unsigned int, long unsigned int, long unsigned int, long unsigned int&, std::vector<long unsigned int>&, long unsigned int&)>&, uint64_t, uint64_t, uint64_t, const std::function<crypto::hash(long unsigned int)>&, bool, uint64_t)’:
cc1plus: warning: ‘void* __builtin_memset(void*, int, long unsigned int)’: specified size 18446744073709551536 exceeds maximum object size 9223372036854775807 [-Wstringop-overflow=]




# Discussion History
## moneromooo-monero | 2019-06-04T10:58:35+00:00
Compiler bug AFAICT.

## moneromooo-monero | 2019-06-04T11:06:44+00:00
It might be helpful if you can try to isolate what part of that function causes the warning, by commenting out bits one at a time.

## moneromooo-monero | 2019-06-08T17:58:55+00:00
Which compiler (including version) and architecture ?

## moneromooo-monero | 2019-06-12T23:38:45+00:00
https://github.com/monero-project/monero/pull/5636

## moneromooo-monero | 2019-08-27T15:06:12+00:00
+resolved

# Action History
- Created by: sherifomran | 2019-06-02T14:16:25+00:00
- Closed at: 2019-08-27T15:09:59+00:00
