---
title: Warning "Passing incompatible arguments to C++ functions from JavaScript is
  dangerous and deprecated.
source_url: https://github.com/monero-project/monero-gui/issues/4237
author: grigio
assignees: []
labels: []
created_at: '2023-10-30T19:59:10+00:00'
updated_at: '2023-11-01T22:44:36+00:00'
type: issue
status: closed
closed_at: '2023-11-01T22:44:36+00:00'
---

# Original Description
0.18.3.1-release (Qt 5.15.11)  I get this warning in a multi recipient tx, but it works

```
2023-10-30 19:45:12.700	W "Could not convert argument 0 at"
2023-10-30 19:45:12.700	W 	 "onTransactionCommitted@qrc:/main.qml:984"
2023-10-30 19:45:12.700	W "Passing incompatible arguments to C++ functions from JavaScript is dangerous and deprecated."
2023-10-30 19:45:12.700	W "This will throw a JavaScript TypeError in future releases of Qt!"
```

# Discussion History
## selsta | 2023-11-01T22:44:36+00:00
This is just a Qt related warning that can be ignored as an end user. It's not directly monero related and doesn't cause any harm.

# Action History
- Created by: grigio | 2023-10-30T19:59:10+00:00
- Closed at: 2023-11-01T22:44:36+00:00
