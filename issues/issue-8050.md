---
title: Erro message
source_url: https://github.com/monero-project/monero/issues/8050
author: maogo
assignees: []
labels: []
created_at: '2021-11-09T02:56:25+00:00'
updated_at: '2021-11-09T03:04:52+00:00'
type: issue
status: closed
closed_at: '2021-11-09T03:03:29+00:00'
---

# Original Description
2021-11-09 01:13:09.178	E string len count value 509411601 goes out of remain storage len 32966
2021-11-09 01:13:09.179	E Exception at [portable_storage::load_from_binary], what=string len count value 509411601 goes out of remain storage len 32966


From master b328fbecc



# Discussion History
## selsta | 2021-11-09T02:59:55+00:00
Is there an issue apart from the error message? It just means someone sent invalid data.

## maogo | 2021-11-09T03:03:24+00:00
> Is there an issue apart from the error message? It just means someone sent invalid data.

 everything else is norma.

## selsta | 2021-11-09T03:04:52+00:00
I have seen that a couple times in the past, seems like someone using buggy software.

# Action History
- Created by: maogo | 2021-11-09T02:56:25+00:00
- Closed at: 2021-11-09T03:03:29+00:00
