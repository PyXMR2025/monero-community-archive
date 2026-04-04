---
title: A memory leak：  crypto::cn_slow_hash(data, size, pwd_hash.data(), 0/*variant*/,
  0/*prehashed*/, 0/*height*/);
source_url: https://github.com/monero-project/monero/issues/8155
author: EWIT521
assignees: []
labels: []
created_at: '2022-01-24T09:20:19+00:00'
updated_at: '2022-02-18T22:56:48+00:00'
type: issue
status: closed
closed_at: '2022-02-18T22:56:48+00:00'
---

# Original Description
memory leak caused by calling “crypto::cn_slow_hash   in function generate_chacha_key, 
the leaky function is
crypto::cn_slow_hash(data, size, pwd_hash.data(), 0/*variant*/, 0/*prehashed*/, 0/*height*/);
file  path is :  src/crypto/chacha.h.   73 line 
start run 
![image](https://user-images.githubusercontent.com/22743089/150755047-aaaa3ca0-97e8-4ae5-baa0-a31d99ac079c.png)

find leak
![image](https://user-images.githubusercontent.com/22743089/150755162-11d1f7dd-2983-4830-858a-5dbb0d5e5fdd.png)



# Discussion History
## hyc | 2022-01-24T14:19:06+00:00
Looks like cn_slow_hash() is being called but cn_slow_hash_free_state() is missing. This isn't a leak, as the hash state isn't lost. It's in a thread local variable (see slow-hash.c:480) which means it will be there ready to be used again the next time the same thread calls cn_slow_hash(). I don't see anything that needs fixing here.

## EWIT521 | 2022-01-24T14:50:47+00:00
But, every time I call it ，hp_state, It is always NULL

## hyc | 2022-01-24T14:59:02+00:00
As |I said:
> It's in a thread local variable

Are you calling it from the same thread or a different thread every time?

## selsta | 2022-02-18T22:56:48+00:00
Closing this as there doesn't appear to be a leak according to hyc and there was no follow up reply. If the issue creator disagrees we can reopen it.

# Action History
- Created by: EWIT521 | 2022-01-24T09:20:19+00:00
- Closed at: 2022-02-18T22:56:48+00:00
