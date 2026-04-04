---
title: Botton SHOWLOG in Settings can produce Application freeze
source_url: https://github.com/monero-project/monero-gui/issues/450
author: medusadigital
assignees: []
labels: []
created_at: '2017-02-03T11:43:18+00:00'
updated_at: '2017-04-18T09:49:16+00:00'
type: issue
status: closed
closed_at: '2017-04-18T09:49:16+00:00'
---

# Original Description
If the Logfile becomes too big, pressing the button SHOWLOG in settings tab can cause the application to freeze. 


Reproduce: press Button SHOWLOG, and enter command set_log 3. close and reopnen log popup a few times. 


possible solution: Scrollback should be reduced even more. Maybe this is also casued by font rendering and can be solved by changing the font in the log window?



# Discussion History
## medusadigital | 2017-04-18T09:49:16+00:00
Button removed --> solved

# Action History
- Created by: medusadigital | 2017-02-03T11:43:18+00:00
- Closed at: 2017-04-18T09:49:16+00:00
