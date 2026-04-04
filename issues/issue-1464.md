---
title: source contains PNG file with embedded non-free ICC profile
source_url: https://github.com/monero-project/monero-gui/issues/1464
author: jonassmedegaard
assignees: []
labels: []
created_at: '2018-06-17T13:08:33+00:00'
updated_at: '2018-07-17T21:31:13+00:00'
type: issue
status: closed
closed_at: '2018-07-17T21:31:13+00:00'
---

# Original Description
The file <lang/flags/denmark.png> contains an embedded color calibartion profile which is copyright Adobe and lacks a free license.

Please simply strip the ICC profile: It is highly unlikely needed. More information e.g. at <https://github.com/monero-project/monero/issues/3944>

# Discussion History
## erciccione | 2018-06-18T13:13:45+00:00
Thanks. Fixed in #1466 

# Action History
- Created by: jonassmedegaard | 2018-06-17T13:08:33+00:00
- Closed at: 2018-07-17T21:31:13+00:00
