---
title: bitmonerod crashes on ARM (pine64)
source_url: https://github.com/monero-project/monero/issues/858
author: antanst
assignees: []
labels:
- invalid
- arm
created_at: '2016-06-08T08:11:16+00:00'
updated_at: '2018-01-08T14:32:32+00:00'
type: issue
status: closed
closed_at: '2018-01-08T14:32:32+00:00'
---

# Original Description
uname -a

> `Linux pine 3.10.101-4-pine64-longsleep #51 SMP PREEMPT Thu May 26 18:20:37 CEST 2016 aarch64 aarch64 aarch64 GNU/Linux
> `

At commit `a837c9cb0feeb7c8c4e616df64cbf650e38355f7`

Bitmonerod crashes with message:

> `bitmonerod: /usr/include/boost/thread/pthread/recursive_mutex.hpp:104: boost::recursive_mutex::~recursive_mutex(): Assertion '!pthread_mutex_destroy(&m)' failed.`


# Discussion History
## radfish | 2016-06-21T22:58:40+00:00
Does `--max-concurrency 1` make a difference?


## antanst | 2016-06-22T08:34:00+00:00
Can't try it anymore...unfortunately my Pine64 gave up the ghost (talk about reliability). I'm waiting for a new one at the moment.


## ghost | 2016-09-15T14:57:53+00:00
Hi @antanst is this issue still present or can it be closed?


## luigi1111 | 2016-12-15T17:39:39+00:00
@antanst Did you ever a get a new one?

## moneromooo-monero | 2017-09-20T21:17:05+00:00
Was it on exit only by any chance ?

## dEBRUYNE-1 | 2018-01-08T13:00:16+00:00
+invalid

# Action History
- Created by: antanst | 2016-06-08T08:11:16+00:00
- Closed at: 2018-01-08T14:32:32+00:00
