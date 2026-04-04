---
title: Welcome page requires user to understand two English words
source_url: https://github.com/monero-project/monero-gui/issues/2503
author: rating89us
assignees: []
labels: []
created_at: '2019-11-26T16:26:59+00:00'
updated_at: '2020-12-04T19:52:36+00:00'
type: issue
status: closed
closed_at: '2020-12-04T19:52:36+00:00'
---

# Original Description
**Current:**
The first page that is opened in Monero GUI is a welcome page with two buttons with English words (`Language` and `Continue`). Not everyone knows what these words mean. See below:
![image](https://user-images.githubusercontent.com/45968869/69651799-eb670400-1070-11ea-8e1c-910e37640609.png)

**Suggestion:**
The first page should be a welcome page AND a selection language page, so that anyone can understand it:
![image](https://user-images.githubusercontent.com/45968869/69652550-20c02180-1072-11ea-9559-b7e9a80db785.png)

# Discussion History
## erciccione | 2019-11-29T16:47:43+00:00
We used to use flags for showing the available languages, but that was changed (See #1092). I agree would be better to avoid English words, maybe we could make the globe clickable?

Anyway, this is very minor IMO. The page seems intuitive enough to me.

## garlicgambit | 2020-09-14T18:12:40+00:00
Alternative option: Open the language selection menu by default and remove the `Language` button.

## rating89us | 2020-12-04T19:52:35+00:00
Fixed in #3210

# Action History
- Created by: rating89us | 2019-11-26T16:26:59+00:00
- Closed at: 2020-12-04T19:52:36+00:00
