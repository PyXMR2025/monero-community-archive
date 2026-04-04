---
title: Incorrect fee labels
source_url: https://github.com/monero-project/monero-gui/issues/2412
author: jtgrassie
assignees: []
labels:
- resolved
created_at: '2019-10-10T01:14:33+00:00'
updated_at: '2019-11-11T22:54:36+00:00'
type: issue
status: closed
closed_at: '2019-11-11T22:54:36+00:00'
---

# Original Description
Please see https://monero.stackexchange.com/a/11658/7493.

Essentially the multiplier amounts are labelled incorrectly.

https://github.com/monero-project/monero-gui/blob/e6458b58ef34a74aa45d48d54ac7b659a2400c8c/pages/Transfer.qml#L214-L217



# Discussion History
## rating89us | 2019-10-13T16:38:28+00:00
I see that 
0.2 x1  = 0.2
0.2 x5  = 1
0.2 x25 = 5
0.2 x 1000 = 200

Where does this 0.2 come from?







## jtgrassie | 2019-10-13T17:01:17+00:00
@rating89us 
> Where does this 0.2 come from?

As the internal multipliers are actually `1, 5, 25, 1000`. Scaling to Normal being x1, the display multipliers can be calculated: 
<pre>slow = 1/5 = <strong>0.2</strong>
normal = 5/5 = <strong>1</strong>
fast = 25/5 = <strong>5</strong>
fastest = 1000/5 = <strong>200</strong></pre>.

## selsta | 2019-11-11T22:52:25+00:00
+resolved

# Action History
- Created by: jtgrassie | 2019-10-10T01:14:33+00:00
- Closed at: 2019-11-11T22:54:36+00:00
