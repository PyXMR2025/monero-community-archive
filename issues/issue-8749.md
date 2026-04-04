---
title: Why is there no serializable_unordered_map template function for serialization
source_url: https://github.com/monero-project/monero/issues/8749
author: EWIT521
assignees: []
labels:
- easy
created_at: '2023-02-24T14:05:36+00:00'
updated_at: '2024-07-16T22:34:39+00:00'
type: issue
status: closed
closed_at: '2024-07-16T22:34:39+00:00'
---

# Original Description
![image](https://user-images.githubusercontent.com/22743089/221196765-11299158-2f17-4b65-b621-977d9c0a9885.png)
When calling:
 ::serialization::detail::do_reserve(v, cnt);
 while v is  map than call    
 void do_reserve(C &c, size_t N) {}
Why not add a template function, like this：
 template <typename K, typename V> void do_reserve(serializable_unordered_map<K,V> &c, size_t N) {  c.reserve(N); }

# Discussion History
## EWIT521 | 2023-02-24T14:13:17+00:00
Why does vector have do_reserve and serializable_unordered_map does not?

## EWIT521 | 2023-02-27T02:58:59+00:00
![image](https://user-images.githubusercontent.com/22743089/221462703-99948463-bff7-4e07-b4f5-ade1b92f89fd.png)
![image](https://user-images.githubusercontent.com/22743089/221462790-579384d4-7322-4168-a142-57cf4594d6a8.png)
![image](https://user-images.githubusercontent.com/22743089/221462997-b5374c47-8ab2-4578-8801-d3ef6ccc9756.png)



## EWIT521 | 2023-02-27T13:45:06+00:00
One line of logs is printed for every 100,000 serialized records. In the beginning, one line is printed every 20 seconds, and in the last one minute, the processing speed becomes slower and slower
2023-02-27 09:53:57.824     7f7ee25e5640        WARNING net     src/serialization/container.h:112       do_serialize_container 333  for i 3200000
2023-02-27 09:54:11.901     7f7ee25e5640        WARNING net     src/serialization/container.h:98        do_serialize_container 111 for i 3300000
：3.2 million to 3.3 million takes 14 seconds

2023-02-27 10:05:54.925          7f7ee25e5640        WARNING        net        src/serialization/container.h:112        do_serialize_container 333 for i 7800000
2023-02-27 10:06:43.517          7f7ee25e5640        WARNING        net        src/serialization/container.h:98        do_serialize_container 111 for i 7900000
：7.8 million to 7.9 million takes 47 seconds

## moneromooo-monero | 2023-03-01T08:59:49+00:00
Because I did not realize unordered_map had a reserve function. Feel free to add it.

## ghost | 2024-04-19T07:25:35+00:00
> Because I did not realize unordered_map had a reserve function. Feel free to add it.

Seems like this issue is made obsolete by commit 2525200185e6b470c6e6cec3c3c8044a0eb0ecc0

# Action History
- Created by: EWIT521 | 2023-02-24T14:05:36+00:00
- Closed at: 2024-07-16T22:34:39+00:00
