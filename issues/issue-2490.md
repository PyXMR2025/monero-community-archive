---
title: 'Send page: remove XMR logo, add XMR to amount, move Fiat conversion to amount
  field'
source_url: https://github.com/monero-project/monero-gui/issues/2490
author: rating89us
assignees: []
labels: []
created_at: '2019-11-25T07:31:51+00:00'
updated_at: '2019-11-25T07:47:16+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Some thoughts:
- Remove XMR logo
- Add "XMR" after the amount
- Append Fiat conversion as non editable text after the typed amount. It shouldn't be displayed in the same place and with the same design as the Paste button (see address field below)

Current:
![image](https://user-images.githubusercontent.com/45968869/69520520-37c11f80-0f5d-11ea-92aa-8610a29f8844.png)

Suggestion:
![image](https://user-images.githubusercontent.com/45968869/69520447-09434480-0f5d-11ea-963f-9e0866f4f5bd.png)

Fiat conversion in dark color:
![image](https://user-images.githubusercontent.com/45968869/69521114-89b67500-0f5e-11ea-8a04-db731a8abb33.png)


# Discussion History
## xiphon | 2019-11-25T07:33:06+00:00
Test the proposal with 12345678.123456789123 XMR amount

## rating89us | 2019-11-25T07:39:47+00:00
Option 1
![image](https://user-images.githubusercontent.com/45968869/69521382-1d884100-0f5f-11ea-9436-b28567ef6cdc.png)

Option 2
![image](https://user-images.githubusercontent.com/45968869/69521442-46103b00-0f5f-11ea-913e-0b31dfdb4005.png)

Option 3
![image](https://user-images.githubusercontent.com/45968869/69521570-9c7d7980-0f5f-11ea-86e8-458995bcf0b0.png)



## xiphon | 2019-11-25T07:44:03+00:00
Won't fit the current page design, will overlap `Transaction priority` field.

## rating89us | 2019-11-25T07:47:15+00:00
I'm using Simple mode (`Transaction priority` field isn't displayed).
But in Advanced mode we could move `Transaction priority` below amount field.

# Action History
- Created by: rating89us | 2019-11-25T07:31:51+00:00
