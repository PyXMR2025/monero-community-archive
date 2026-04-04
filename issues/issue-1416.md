---
title: Usage of quantum-proof Diffie Hellman method
source_url: https://github.com/monero-project/monero/issues/1416
author: Silur
assignees: []
labels: []
created_at: '2016-12-08T15:31:47+00:00'
updated_at: '2016-12-15T15:59:42+00:00'
type: issue
status: closed
closed_at: '2016-12-15T15:59:42+00:00'
---

# Original Description
Quantum-computers are an emerging threat to the logarithm and prime-factorization problems that holds 99% of our common crypto standards, including ECDH. Call me paranoid but I write every software of mine with quantum-proof cryptography included and AFAIK monero is for... paranoid people :)

There's a wonderful, stable, reviewed [library](https://www.microsoft.com/en-us/research/project/sidh-library/) from microsoft that provides 128bit security against shor's algorithm.

I'd really like to implement it myself and make a pull request but I cannot and actually don't want to touch C++ code but let me know if I can help with that using pure C.


# Discussion History
## moneromooo-monero | 2016-12-08T20:10:14+00:00
Looks unexpectedly good (MIT, actually compiles on Linux). I wouldn't trust MS though with their history, especially if we can find other code. I believe some people in MRL are going to look at QC resistant algorithms, and I'll get the link passed on.

## moneromooo-monero | 2016-12-08T21:06:43+00:00
Turns out the MRL people already knew about it, and it isn't useful in this case.

Thanks


## Silur | 2016-12-09T10:43:16+00:00
Sorry but what is MRL? and why exactly isn't it useful, you use ECDH in a way that breaking it doesn't expose users to the public?

## anonimal | 2016-12-09T11:04:17+00:00
@Silur https://lab.getmonero.org/ https://github.com/monero-project/research-lab

## moneromooo-monero | 2016-12-09T18:24:30+00:00
I don't know the details of why it wasn't useful, but you can talk to luigi1111 on IRC.

## luigi1111 | 2016-12-15T15:59:42+00:00
This is an area to research, rather than just up and replace. :) Further discussion and findings can/should be added to the lab repo.

# Action History
- Created by: Silur | 2016-12-08T15:31:47+00:00
- Closed at: 2016-12-15T15:59:42+00:00
