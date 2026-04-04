---
title: Loading a wallet with 20 million sub-addresses is very slow, the reason has
  been found
source_url: https://github.com/monero-project/monero/issues/8926
author: EWIT521
assignees: []
labels:
- pending review
created_at: '2023-07-01T08:19:42+00:00'
updated_at: '2026-02-18T21:51:07+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
![image](https://github.com/monero-project/monero/assets/22743089/23248657-6d8b-49cb-bb2f-742d2ca929fc)
![image](https://github.com/monero-project/monero/assets/22743089/c1c228cc-a37d-41d8-816a-912381ce749a)
![d42a7dca-fefd-49ab-8138-4fc6082d9e69](https://github.com/monero-project/monero/assets/22743089/93d4812f-2b32-4196-aaba-f6063894b366)

Analyze logs to draw conclusions，
::serialization::detail::do_add(v, std::move(e));
After 4.7 million sub-addresses are loaded, they are stored in the first bucket

![image](https://github.com/monero-project/monero/assets/22743089/dadc1b64-cae5-4bec-bbcb-7a9403d91030)

The following is whether there is any optimization in Monroe's code, why the function is always inserted into the first bucket after calling the function
![image](https://github.com/monero-project/monero/assets/22743089/d5e8796c-e0db-4c38-92d3-02de389ad4e4)

Is it possible to further optimize and replace the hash function address with a value?

# Discussion History
## SChernykh | 2023-07-12T14:52:16+00:00
These hash functions are perfectly fine, assuming that the values they hash are random (which subaddresses are). How did you generate those 20 million subaddresses? If they weren't random and followed some pattern instead, then hashing will of course get broken.

# Action History
- Created by: EWIT521 | 2023-07-01T08:19:42+00:00
