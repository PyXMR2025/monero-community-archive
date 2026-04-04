---
title: Cannot allocate memory
source_url: https://github.com/monero-project/monero/issues/4766
author: AndrVdov
assignees: []
labels: []
created_at: '2018-10-31T13:46:26+00:00'
updated_at: '2022-08-16T17:47:53+00:00'
type: issue
status: closed
closed_at: '2018-11-22T12:33:09+00:00'
---

# Original Description
Problem with monero-wallet-rpc
Periodically logs error:
ERROR	default	contrib/epee/src/mlocker.cpp:63	Error locking page at 0x5595b3078000: Cannot allocate memory
![2018-10-31 15-43-19](https://user-images.githubusercontent.com/34911315/47792115-fd6a5c00-dd23-11e8-8753-ba437f065164.png)


Any idea how this can be solved?



# Discussion History
## moneromooo-monero | 2018-10-31T14:26:20+00:00
Bump locked memory limit (ulimit -l).
This is not an actual OOM error, just that it can't lock the memory. It will still work fine, it will just be unable to lock the memory.

## AndrVdov | 2018-11-01T08:41:49+00:00
Thanks for help.
The server now has the following settings:
- soft memlock 262144
- hard memlock 262144
What limit is recommended?


## moneromooo-monero | 2018-11-01T10:16:30+00:00
I've been running with that same amount and never noticed any of those errors.

## moneromooo-monero | 2018-11-04T23:27:06+00:00
https://github.com/monero-project/monero/pull/4790

## moneromooo-monero | 2018-11-22T12:27:44+00:00
There's a warning at startup now if the limit is low. I'll call that a fix since that's no bug anyway.

+resolved

## gituser | 2019-03-07T00:33:05+00:00
I have the same issue (just noticed) on new version `v0.14.0.1` in wallet-rpc:

```
grep -i 'Error locking page' simplewallet_product.log |head
2019-02-25 21:25:14.891	[RPC0]	ERROR	default	contrib/epee/src/mlocker.cpp:63	Error locking page at 0x7fc912c7c000: Cannot allocate memory
2019-02-25 21:25:14.892	[RPC0]	ERROR	default	contrib/epee/src/mlocker.cpp:63	Error locking page at 0x7fc912c7c000: Cannot allocate memory
2019-02-25 21:25:14.892	[RPC0]	ERROR	default	contrib/epee/src/mlocker.cpp:63	Error locking page at 0x7fc912c7d000: Cannot allocate memory
2019-02-25 21:25:14.893	[RPC0]	ERROR	default	contrib/epee/src/mlocker.cpp:63	Error locking page at 0x7fc912c7c000: Cannot allocate memory
2019-02-25 21:25:14.893	[RPC0]	ERROR	default	contrib/epee/src/mlocker.cpp:63	Error locking page at 0x7fc912c7c000: Cannot allocate memory
```
It started after the upgrade to `v0.14.0.1` from `v0.13.0.4`.

The memory limits never changed: 12GB of RAM and `Max locked memory         65536                65536                bytes`

There is nothing regarding the mentioned warning in the logs upon startup:

```
$ grep -i lockable *.log
$ 
```

I've bumped the limit to 64Mb (though 1Mb should be enough according to the commit you've mentioned):  `ulimit -l $((64*1048576))` will see how it goes..

Still the warning should be displayed somehow upon startup?

## r0b0 | 2022-08-16T17:47:52+00:00
You might want to add 
`LimitMEMLOCK=1048576`

to the [example monerod.service file](utils/systemd/monerod.service)

# Action History
- Created by: AndrVdov | 2018-10-31T13:46:26+00:00
- Closed at: 2018-11-22T12:33:09+00:00
