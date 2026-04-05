---
title: Am i mining, what does the lines mean
source_url: https://github.com/xmrig/xmrig/issues/3007
author: qqiumax
assignees: []
labels: []
created_at: '2022-04-06T09:18:14+00:00'
updated_at: '2022-04-08T00:26:11+00:00'
type: issue
status: closed
closed_at: '2022-04-08T00:26:11+00:00'
---

# Original Description
What does the commands mean, and the lines?
![image](https://user-images.githubusercontent.com/102963434/161941687-121bfd3b-d2dc-4cda-9986-a988953e6bd7.png)


# Discussion History
## Spudz76 | 2022-04-07T02:41:12+00:00
Yes you're mining, the fixed job difficulty of 50000 is too high for your hashrate though so you will miss payments.  Should be an `accept` every 30 seconds or so.  Proper difficulty would be 30 * 370 = 11100.  At 50000 you might get a result every 50000 / 370 = 135 seconds which is too long (main chain jobs switch every ~120 seconds).

Not sure if minerxmr supports variable diff or custom fixed diff.  But also minexmr is too big you should use literally any other pool (but pick one with adjustable diff).

## qqiumax | 2022-04-07T04:58:41+00:00
really! But I have 0.000042 coins that has not been not drawn


## Spudz76 | 2022-04-07T19:01:24+00:00
0.000042XMR is less than one cent USD.  Not a loss?

## qqiumax | 2022-04-08T00:26:02+00:00
oh, ok



## qqiumax | 2022-04-08T00:26:11+00:00
thanks


# Action History
- Created by: qqiumax | 2022-04-06T09:18:14+00:00
- Closed at: 2022-04-08T00:26:11+00:00
