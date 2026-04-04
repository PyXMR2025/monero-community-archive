---
title: '[RFC] Formalise log levels'
source_url: https://github.com/monero-project/monero/issues/1187
author: ghost
assignees: []
labels: []
created_at: '2016-10-06T12:31:26+00:00'
updated_at: '2017-02-24T06:07:55+00:00'
type: issue
status: closed
closed_at: '2017-02-24T06:07:55+00:00'
---

# Original Description
Hi all, just wanted to seek some comments about formalising the logging system.

`Log Level 0` Turn off all logging. Leave log files in situ but do not log any events
`Log Level 1` Major system events including activation/deactivation of major components and block synchronisation. Fatal errors and major component errors through `LOG_ERROR`
`Log Level 2` Minor system events including activation/deactivation of sub-components with more details of peer connectivity. Now log warnings through `LOG_WARNING`
`Log Level 3` Log all details. Could including programmer's notes for later debugging through `LOG_NOTE`


# Discussion History
## moneromooo-monero | 2016-10-07T10:36:12+00:00
I'd do that as part of the change of logging system (eg, easylogging++).


## ghost | 2016-10-07T11:14:05+00:00
Agreed. Adding a new logging system is way beyond my skill level though so was just wanting to get something formally agreed about the definitions of the logging levels and publicly available for all developers. 


# Action History
- Created by: ghost | 2016-10-06T12:31:26+00:00
- Closed at: 2017-02-24T06:07:55+00:00
