---
title: ' error: can''t bind socket: Permission denied. for 0.0.0.0'
source_url: https://github.com/monero-project/monero/issues/6714
author: maogo
assignees: []
labels: []
created_at: '2020-07-19T16:34:16+00:00'
updated_at: '2022-06-27T10:53:56+00:00'
type: issue
status: closed
closed_at: '2020-07-20T05:14:52+00:00'
---

# Original Description
Start the monerod sometimes gets " error: can't bind socket: Permission denied. for 0.0.0.0",  is this an issue and will it affect use？

![aa](https://user-images.githubusercontent.com/20197997/87880050-1ef00780-ca21-11ea-8e87-20ea15592f9f.png)

usually the problem is resolved after monerod restart.


# Discussion History
## P-A-Trick | 2022-06-09T16:48:30+00:00
> Start the monerod sometimes gets " error: can't bind socket: Permission denied. for 0.0.0.0", is this an issue and will it affect use？
> 
> ![aa](https://user-images.githubusercontent.com/20197997/87880050-1ef00780-ca21-11ea-8e87-20ea15592f9f.png)
> 
> usually the problem is resolved after monerod restart.

and unusually? restart does not solve the problem for me

## myselfeuh | 2022-06-27T10:53:00+00:00
Hi,
I have the same error message with monerod version 0.17.3.2-release running on Windows.
Restarting doesn't change anything for me neither.
The daemon seems to run fine though.

# Action History
- Created by: maogo | 2020-07-19T16:34:16+00:00
- Closed at: 2020-07-20T05:14:52+00:00
