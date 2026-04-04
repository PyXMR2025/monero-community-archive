---
title: Monroe handles raw transactions too slowly
source_url: https://github.com/monero-project/monero/issues/5604
author: gzlkylin
assignees: []
labels: []
created_at: '2019-06-03T07:56:51+00:00'
updated_at: '2019-06-04T08:50:41+00:00'
type: issue
status: closed
closed_at: '2019-06-04T08:50:41+00:00'
---

# Original Description
Why is the max number of threads in tools::threadpool always 0? 
The m_incoming_tx_lock critical section is too large, causing on_send_raw_tx rpc to be a serial processing transaction.
How to modify the code to deal with raw transaction quickly?

# Discussion History
## moneromooo-monero | 2019-06-03T09:44:19+00:00
What platform (precisely), and what version of boost ?
Are you sending lots of transactions at once ?

## gzlkylin | 2019-06-03T11:15:53+00:00
platform  CentOS Linux 7  version of  boost 1.58

You can see max_thread = 0 here，and can't be modified.
monero\src\common\threadpool.h
````
namespace tools
{
//! A global thread pool
class threadpool
{
public:
  static threadpool& getInstance() {
    static threadpool instance;
    return instance;
  }
//...
  ~threadpool();

  private:
    threadpool(unsigned int max_threads = 0);
//...
};
}
````

----------------------------------------------------------------
I send lots of transactions at once, and one node with some connection.
````
Thread 21 (Thread 0x7ffadb520700 (LWP 12250)):    
#0  0x00007ffb1e5ac51d in __lll_lock_wait () from /lib64/libpthread.so.0    
#1  0x00007ffb1e5a7e36 in _L_lock_870 () from /lib64/libpthread.so.0    
#2  0x00007ffb1e5a7d2f in pthread_mutex_lock () from /lib64/libpthread.so.0    
#3  0x00005562dda46ca4 in cryptonote::core::handle_incoming_txs() (...)    
#4  0x00005562dda48698 in cryptonote::core::handle_incoming_tx(...)    
#5  0x00005562dd8d7733 in cryptonote::core_rpc_server::on_send_raw_tx
````

View thread information, blocked here.


## moneromooo-monero | 2019-06-03T11:44:00+00:00
This is a misunderstanding. The max number of threads is not 0. It is what boost thinks your processor can do (number of cores).

About sending many txes, some of the work could be done without the tx lock, but it's more complex for a corner case, so I don't think I'm going to change that for now. Though if someone does the work and it's solid, we'll merge.


## gzlkylin | 2019-06-03T12:48:28+00:00
Thanks reply
If I want to contribute code, which branch is best based？

## moneromooo-monero | 2019-06-03T13:04:26+00:00
Please use master. Feel free to pop by #monero-dev if you have questions on that code.

# Action History
- Created by: gzlkylin | 2019-06-03T07:56:51+00:00
- Closed at: 2019-06-04T08:50:41+00:00
