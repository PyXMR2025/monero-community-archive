---
title: Code coverage not updated ?
source_url: https://github.com/monero-project/monero/issues/4589
author: calidion
assignees: []
labels: []
created_at: '2018-10-14T16:46:44+00:00'
updated_at: '2024-07-31T23:25:30+00:00'
type: issue
status: closed
closed_at: '2024-07-31T23:25:30+00:00'
---

# Original Description
I searched coverall by `grep coverall -Rn` only found it in the README.md file.

Does it mean code coverage info currently generated automatically but not  updated to coveralls.io?
```
./README.md:48:| Coveralls | [![Coveralls Status](https://coveralls.io/repos/github/monero-project/monero/badge.svg?branch=master)](https://coveralls.io/github/monero-project/monero?branch=master)
```

# Discussion History
## moneromooo-monero | 2018-10-14T20:24:15+00:00
No idea how that works.This got added by someone a while back (who was working with them I think), but I don't think they're around anymore. If you find it useful and know how to fix/enable it, please do.

## calidion | 2018-10-15T04:57:31+00:00
I am trying to add code coverage report badge to my project.
So I am referencing monero. 
It is sad to know that monero is not updated on coverage report either.

## calidion | 2018-10-15T09:20:11+00:00
@moneromooo-monero 

I have added codecov.io coverage badge to [my project](https://github.com/vigcoin/coin), it is much easier than coveralls.io.

If it is allowed, I would like to add it to monero too when I get more familiar with monero.

## moneromooo-monero | 2018-10-15T11:28:47+00:00
I don't know it, but it would probably be useful, thanks.


## moneromooo-monero | 2020-05-16T16:41:04+00:00
Is this something you still want to do at some point ?

## selsta | 2024-07-31T23:25:30+00:00
Closing as we currently don't use coveralls.

# Action History
- Created by: calidion | 2018-10-14T16:46:44+00:00
- Closed at: 2024-07-31T23:25:30+00:00
