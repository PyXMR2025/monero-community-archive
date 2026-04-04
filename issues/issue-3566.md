---
title: 'History: some transaction amounts are exported to CSV file in scientific notation'
source_url: https://github.com/monero-project/monero-gui/issues/3566
author: rating89us
assignees: []
labels: []
created_at: '2021-06-16T11:34:44+00:00'
updated_at: '2021-06-21T18:38:46+00:00'
type: issue
status: closed
closed_at: '2021-06-21T18:38:46+00:00'
---

# Original Description
![image](https://user-images.githubusercontent.com/45968869/122543369-ff47d180-d02b-11eb-916c-4ab0fefa6d63.png)


# Discussion History
## selsta | 2021-06-18T00:07:14+00:00
Oops, accidentally removed my comment. Did you confirm that it isn't Excel (or whatever program you are using) that converts the number to scientific notation? Fee uses display amount, scientific notation should not happen. 

## rating89us | 2021-06-18T09:53:36+00:00
> Fee uses display amount, scientific notation should not happen.

You're right, just some transaction amounts are being exported in scientific notation. LibreOffice Calc was converting fee to scientific notation.

# Action History
- Created by: rating89us | 2021-06-16T11:34:44+00:00
- Closed at: 2021-06-21T18:38:46+00:00
