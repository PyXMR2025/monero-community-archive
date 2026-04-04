---
title: 'Idea: use std::unique_ptr deleter to support custom destructor in custom smart
  pointer in dns_utils?'
source_url: https://github.com/monero-project/monero/issues/8732
author: ndcroos
assignees:
- '0xFFFC0000'
labels:
- enhancement
- easy
created_at: '2023-02-04T22:09:10+00:00'
updated_at: '2023-12-20T08:44:38+00:00'
type: issue
status: closed
closed_at: '2023-12-20T08:44:38+00:00'
---

# Original Description
There is this line with a TODO:
https://github.com/monero-project/monero/blob/9489586add5116a48039616140bb7267b16ba7b1/src/common/dns_utils.cpp#L198

std::unique_ptr supports a custom deleter, but I am not sure if this fits all requirements.

# Discussion History
## 0xFFFC0000 | 2023-09-12T18:45:42+00:00
The problem is not the deleter. The problem is none of the smart pointer libraries in std (or Boost) provide an easy way to do `&` like we do it [here](https://github.com/monero-project/monero/blob/9489586add5116a48039616140bb7267b16ba7b1/src/common/dns_utils.cpp#L335). 

Of course, it would be possible to get `.get()` the pointer and get the address and use it, but it is not as clean as `&scoped_ptr_variable`.

And to make it worse, the result of `.get()` is an rvalue, so you have to get (and how) into the whole address of the rvalue business. 

P.S. `auto_ptr` is deperacated. std provides `unique_ptr` as a replacement.

## vtnerd | 2023-09-12T21:21:48+00:00
I think converting to `.get()` is fine here.

## vtnerd | 2023-09-12T21:24:13+00:00
Nevermind, I see the issue. `operator&` is returning a `**`, which cannot simulate easily. I thought there was something in Boost for this (or at least proposed), but I cannot find it at the moment.

# Action History
- Created by: ndcroos | 2023-02-04T22:09:10+00:00
- Closed at: 2023-12-20T08:44:38+00:00
