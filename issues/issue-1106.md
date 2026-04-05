---
title: 2.99.x-evo api hugepages
source_url: https://github.com/xmrig/xmrig/issues/1106
author: doadin
assignees: []
labels:
- bug
created_at: '2019-08-07T19:12:14+00:00'
updated_at: '2019-08-09T09:45:22+00:00'
type: issue
status: closed
closed_at: '2019-08-09T09:45:22+00:00'
---

# Original Description
console shows huge pages 4/4 100% but web api shows hugepages: false, .

```
    "cpu": {
        "enabled": true,
        "huge-pages": true,
```

in config

# Discussion History
## xmrig | 2019-08-08T05:40:28+00:00
Huge pages in complicated thing now, it not just true or false, actual huge pages information can be found in `GET /2/backends` as 2 numbers for example:
```json
"hugepages": [1184, 1184],
```
First number is huge pages count, second is total pages count, in this example 100% of huge pages allocated, I did't make final decision about this information in `GET /1/summary` endpoint, so it always false now.
Thank you.

## xmrig | 2019-08-08T18:52:31+00:00
Fixed, old endpoint `/1/summary` returns `true` if 100% of hugepages obtained, new endpoint `/2/summary` returns it as 2 numbers.
Thank you.

## doadin | 2019-08-09T04:45:36+00:00
sounds like a good solution, thanks for that and the quick response.

## xmrig | 2019-08-09T09:45:22+00:00
v2.99.5-beta released https://github.com/xmrig/xmrig/releases/tag/v2.99.5-beta

# Action History
- Created by: doadin | 2019-08-07T19:12:14+00:00
- Closed at: 2019-08-09T09:45:22+00:00
