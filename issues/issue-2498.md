---
title: 'Main menu: don''t display welcome page before language settings if it''s not
  the first run'
source_url: https://github.com/monero-project/monero-gui/issues/2498
author: rating89us
assignees: []
labels: []
created_at: '2019-11-26T11:40:56+00:00'
updated_at: '2019-12-04T04:24:40+00:00'
type: issue
status: closed
closed_at: '2019-12-04T04:24:40+00:00'
---

# Original Description
In an already initialized Monero GUI (not first run), when a wallet is closed, user is redirected to main menu, where the change wallet mode page can be opened, which has a `Change language` button:
![image](https://user-images.githubusercontent.com/45968869/69626432-f1e18580-1048-11ea-8dbd-f7244c19a636.png)

Why is there a `Change language `button in the wallet mode selection page? Shouldn't we remove it?

Anyway, the `Change language` button will open a welcome page that should only appear when Monero GUI is running for the first time. This welcome page has a `Continue` button that sends the user back to the change wallet mode page.
![image](https://user-images.githubusercontent.com/45968869/69626409-e68e5a00-1048-11ea-92a4-22550f87e237.png)


# Discussion History
# Action History
- Created by: rating89us | 2019-11-26T11:40:56+00:00
- Closed at: 2019-12-04T04:24:40+00:00
