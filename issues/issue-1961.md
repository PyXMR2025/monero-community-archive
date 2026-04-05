---
title: Pretty sure this is at least memory leak
source_url: https://github.com/xmrig/xmrig/issues/1961
author: ViralTaco
assignees: []
labels:
- question
created_at: '2020-11-30T23:34:52+00:00'
updated_at: '2020-12-09T13:27:54+00:00'
type: issue
status: closed
closed_at: '2020-12-09T13:27:53+00:00'
---

# Original Description
Might be UB. In any case this is bad style so now I have to fork the whole repo. 
```
void xmrig::Buffer::move(Buffer &&other)
{
    if (m_size > 0) {
        delete [] m_data; // <-- m_data (char*)
    }

    m_data = other.m_data; // :sigh: 
    m_size = other.m_size;  // legit would be faster to use std::string. 

    other.m_data = nullptr; // <-- not freed
    other.m_size = 0;
}
```
Anyway… I'll make a pull request when I come to it 

# Discussion History
## xmrig | 2020-12-01T03:15:42+00:00
This is part of the move operator, so free is not supposed to be here.
Sooner or later whole `Buffer` class will be replaced to https://github.com/xmrig/xmrig-nonces-heatmap/blob/master/src/base/tools/Buffer.h
Thank you.

## SChernykh | 2020-12-01T14:22:07+00:00
Memory leak is by definition when memory is not freed and there's no pointers left pointing to it. This is not the case here, `m_data` still points to it. This function implements standard move semantics operation and takes rvalue reference in the first parameter.

## ViralTaco | 2020-12-05T06:47:19+00:00
> Memory leak is by definition when memory is not freed and there's no pointers left pointing to it. This is not the case here, `m_data` still points to it. This function implements standard move semantics operation and takes rvalue reference in the first parameter.

Yeah but given the type of m_data is char pointer and not char array I'm not sure. Maybe there's an overload for this scenario that I missed.
other.m_data is never released/deleted/freed, is it? The Buffer is (presumably) moved into the function, when is it destroyed? 
If it is then there is the problem of use after move since m_data, again, is a raw pointer to char. 
Now I've not done c++ in a while so I'll ask smarter people to have a look. 

## SChernykh | 2020-12-05T08:31:13+00:00
You don't need to release other.m_data because it's a nullptr after the call. Current buffer releases its own m_data first and then takes ownership of other.m_data. There's no memory leak here.

## ViralTaco | 2020-12-09T13:27:53+00:00
> You don't need to release other.m_data because it's a nullptr after the call. Current buffer releases its own m_data first and then takes ownership of other.m_data. There's no memory leak here.

Yeah… I finally managed to wrap my head around that. There's no indication that ownership is transferred. 
Thank you for the explanation. I'll close this thread since the "issue" is solved. 

# Action History
- Created by: ViralTaco | 2020-11-30T23:34:52+00:00
- Closed at: 2020-12-09T13:27:53+00:00
