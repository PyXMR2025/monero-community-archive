---
title: 'Transfer: error on transaction fee estimative '
source_url: https://github.com/monero-project/monero-gui/issues/3497
author: rating89us
assignees: []
labels: []
created_at: '2021-05-22T10:22:00+00:00'
updated_at: '2021-07-14T20:44:17+00:00'
type: issue
status: closed
closed_at: '2021-07-14T20:44:16+00:00'
---

# Original Description
Transaction fee estimative is not displaying on Send page anymore. I get the following warning when changing transaction priority or updating amounts:
```
W "Could not convert argument 1 at"
W 	 "expression for fee@qrc:/pages/Transfer.qml:693"
W 	 "onClicked@qrc:/components/StandardDropdown.qml:213"
W "Passing incompatible arguments to C++ functions from JavaScript is dangerous and deprecated."
W "This will throw a JavaScript TypeError in future releases of Qt!"
```


# Discussion History
## selsta | 2021-07-13T22:19:41+00:00
Does this error still show up?

## rating89us | 2021-07-14T20:44:16+00:00
I haven't seen it anymore.

# Action History
- Created by: rating89us | 2021-05-22T10:22:00+00:00
- Closed at: 2021-07-14T20:44:16+00:00
