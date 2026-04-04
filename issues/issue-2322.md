---
title: 'Fiat balance: Use € and $ sign instead of ¥ (Yen) to toggle'
source_url: https://github.com/monero-project/monero-gui/issues/2322
author: ghost
assignees: []
labels: []
created_at: '2019-07-26T16:32:08+00:00'
updated_at: '2019-08-12T08:32:18+00:00'
type: issue
status: closed
closed_at: '2019-08-12T08:32:18+00:00'
---

# Original Description
![image](https://user-images.githubusercontent.com/46682965/61966613-575a3280-afd3-11e9-994b-e1d3ec3527b4.png)
We should use € and $ sign instead of ¥ (Yen) to toggle the currency.

If the problem with that is the risk of unit confusion, the solution shouldn't be introducing ¥ (Yen), the solution should be introducing XMR. Which brings us to #2298: If that were to be adopted we could drop the toggle symbol completely and go like this:
![image](https://user-images.githubusercontent.com/46682965/61965606-e0bc3580-afd0-11e9-9ca1-781363cf630f.png)

# Discussion History
## rating89us | 2019-07-28T14:44:17+00:00
Yes, we should use the symbol of the currency that was selected in Settings > Interface.
![image](https://user-images.githubusercontent.com/45968869/62008319-d1ff8b00-b156-11e9-9d30-9701931e0e17.png)

## selsta | 2019-08-11T22:12:05+00:00
Implemented the easy version in #2347. Do you want to add the second design to #2298 so that we can close this for now?

## ghost | 2019-08-12T08:32:18+00:00
nice!!!
sure! done!

# Action History
- Created by: ghost | 2019-07-26T16:32:08+00:00
- Closed at: 2019-08-12T08:32:18+00:00
