---
title: Trying to make sense of this.
source_url: https://github.com/xmrig/xmrig/issues/2878
author: d3nd3
assignees: []
labels: []
created_at: '2022-01-19T17:35:44+00:00'
updated_at: '2022-01-19T19:12:15+00:00'
type: issue
status: closed
closed_at: '2022-01-19T19:12:15+00:00'
---

# Original Description
https://github.com/xmrig/xmrig/blob/718c7e0fc1452353bc1361b85c8a2a4c81c1379e/src/base/kernel/config/BaseTransform.cpp#L125

where arg is a const char *
and m_coin is a class Coin instance.

How does this assignment work/compile.  Isn't it illegal to set a class to a const char *

# Discussion History
## SChernykh | 2022-01-19T17:45:54+00:00
Type conversion. const char* is converted into Coin via constructor: https://github.com/xmrig/xmrig/blob/718c7e0fc1452353bc1361b85c8a2a4c81c1379e/src/base/crypto/Coin.h#L52

## d3nd3 | 2022-01-19T17:48:38+00:00
I see, I didn't know that was possible. Its under "Implicit Conversion" ?
https://en.cppreference.com/w/cpp/language/implicit_conversion
I need to know where it says this is possible, sorry to bother you.

## SChernykh | 2022-01-19T17:52:43+00:00
Yes, see https://en.cppreference.com/w/cpp/language/implicit_conversion
Right side is converted from const char* to Coin and then this temporary Coin object is copied into m_coin.

# Action History
- Created by: d3nd3 | 2022-01-19T17:35:44+00:00
- Closed at: 2022-01-19T19:12:15+00:00
