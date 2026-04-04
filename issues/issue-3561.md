---
title: MoneroD CLI output skipping some records of launched treads
source_url: https://github.com/monero-project/monero-gui/issues/3561
author: dzintars
assignees: []
labels: []
created_at: '2021-06-14T16:44:48+00:00'
updated_at: '2023-01-18T06:12:49+00:00'
type: issue
status: closed
closed_at: '2023-01-18T06:12:43+00:00'
---

# Original Description
Not sure is it important, but will leave it there in any case.

![image](https://user-images.githubusercontent.com/547420/121928160-8f45fc80-cd48-11eb-9efc-b4981323af32.png)

As you can see from the output, only 7 treads was started (actually 8), and 8 treads was stopped. 6th thread missing from the starting treads MoneroD CLI output.

# Discussion History
## selsta | 2023-01-18T06:12:43+00:00
Could be resolved by https://github.com/monero-project/monero/pull/7929

If not please open an issue here: https://github.com/monero-project/monero since this isn't GUI related.

# Action History
- Created by: dzintars | 2021-06-14T16:44:48+00:00
- Closed at: 2023-01-18T06:12:43+00:00
