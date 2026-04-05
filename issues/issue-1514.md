---
title: Xmrig bus error arm galaxy s5
source_url: https://github.com/xmrig/xmrig/issues/1514
author: Izder456
assignees: []
labels: []
created_at: '2020-01-24T11:47:56+00:00'
updated_at: '2021-04-12T15:01:51+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:01:51+00:00'
---

# Original Description
I get a bus error on my galaxy s5 {see screenshot} 
![Screenshot_20200124-054851](https://user-images.githubusercontent.com/16585414/73067094-595f5a00-3e6d-11ea-870d-2ce6c71ef3b3.png)



# Discussion History
## Spudz76 | 2020-01-27T20:38:14+00:00
Not enough memory.  RandomX requires 2080MB (that's 2GB + 32MB) and the Galaxy S5 has 2GB total.  Need 4GB devices minimum for RandomX.  The only bug is it should have exited rather than trying the "slow" mode (which also has not enough memory).

It should mine other algos that aren't RandomX based...

# Action History
- Created by: Izder456 | 2020-01-24T11:47:56+00:00
- Closed at: 2021-04-12T15:01:51+00:00
