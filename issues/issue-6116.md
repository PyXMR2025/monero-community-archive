---
title: Calculate Atomic Units?
source_url: https://github.com/monero-project/monero/issues/6116
author: Fenny
assignees: []
labels: []
created_at: '2019-11-10T16:59:39+00:00'
updated_at: '2019-11-10T19:34:29+00:00'
type: issue
status: closed
closed_at: '2019-11-10T19:34:29+00:00'
---

# Original Description
I'm having a brainfart and I want to make sure I got it right before I use my code in production.

I calculate xmr from usd ( or any currency ) then to atomic units using the following calculation:

```javascript
var usd  = 25.00;
var rate = 62.00;
var xmr  = usd / rate;  // 0.4032258064516129
var units = parseFloat((xmr  / 100).toFixed(12)); // 0.004032258065
```

But I'm not sure if the [Atomic Units](https://web.getmonero.org/resources/moneropedia/atomic-units.html) calculation is correct. I need to use the [wallet-rpc#transfer](https://web.getmonero.org/resources/developer-guides/wallet-rpc.html#transfer) input.

Please correct me if I'm wrong, thank you!

***Edit
@moneromooo-monero gave me the solution in the IRC
```javascript
var units = Math.round(xmr * 1000000000000);
```

# Discussion History
# Action History
- Created by: Fenny | 2019-11-10T16:59:39+00:00
- Closed at: 2019-11-10T19:34:29+00:00
