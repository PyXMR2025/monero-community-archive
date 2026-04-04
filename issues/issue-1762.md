---
title: Tooltip down arrow with incorrect position
source_url: https://github.com/monero-project/monero-site/issues/1762
author: rating89us
assignees: []
labels:
- bug
created_at: '2021-08-05T10:02:02+00:00'
updated_at: '2021-08-05T11:51:09+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
![image](https://user-images.githubusercontent.com/45968869/128331918-94c171cc-02c4-467d-a34d-a9cfc68780a3.png)

![image](https://user-images.githubusercontent.com/45968869/128331929-910f4af2-2840-4f7f-8000-373c9df1f6a7.png)


# Discussion History
## erciccione | 2021-08-05T10:21:25+00:00
On what operative system and browser are you seeing this?

## rating89us | 2021-08-05T11:48:27+00:00
Windows (chrome and firefox)
Website in mobile width

## rating89us | 2021-08-05T11:51:09+00:00
Changing `custom.css:4714` to `bottom: 100%` fixes for me on mobile width, but breaks the display on desktop width

# Action History
- Created by: rating89us | 2021-08-05T10:02:02+00:00
