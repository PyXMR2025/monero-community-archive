---
title: Cant interact with wallet due to "Login error"
source_url: https://github.com/monero-project/monero-gui/issues/4236
author: Mashedpot5
assignees: []
labels: []
created_at: '2023-10-29T07:50:00+00:00'
updated_at: '2023-10-29T13:49:39+00:00'
type: issue
status: closed
closed_at: '2023-10-29T13:49:39+00:00'
---

# Original Description
An unexpected application error occurred.

Please let us know of the following error message as it could be a bug:

 <p><span style='font-size: 11px;'>TypeError: Cannot read property 'view' of undefined</span></p>TypeError: Cannot read property 'view' of undefined
    at WalletDetailsView._configureUIWithWallet__accountInfo (C:\Program Files\MyMonero\resources\app.asar\local_modules\Wallets\Views\WalletDetailsView.web.js:677:41)
    at WalletDetailsView.setup (C:\Program Files\MyMonero\resources\app.asar\local_modules\Wallets\Views\WalletDetailsView.web.js:42:10)
    at new WalletDetailsView (C:\Program Files\MyMonero\resources\app.asar\local_modules\Wallets\Views\WalletDetailsView.web.js:29:10)
    at WalletsListView.pushRecordDetailsView (C:\Program Files\MyMonero\resources\app.asar\local_modules\Lists\Views\ListView.web.js:232:20)
    at WalletsListView.cellWasTapped (C:\Program Files\MyMonero\resources\app.asar\local_modules\Lists\Views\ListView.web.js:251:12)
    at WalletsListCellView.cell_tapped_fn (C:\Program Files\MyMonero\resources\app.asar\local_modules\Lists\Views\ListView.web.js:186:15)
    at C:\Program Files\MyMonero\resources\app.asar\local_modules\Lists\Views\ListCellView.web.js:96:14
    at WalletsListCellView.overridable_cellTapped (C:\Program Files\MyMonero\resources\app.asar\local_modules\Lists\Views\ListCellView.web.js:103:5)
    at WalletsListCellView.__cellTapped (C:\Program Files\MyMonero\resources\app.asar\local_modules\Lists\Views\ListCellView.web.js:94:10)
    at HTMLDivElement.<anonymous> (C:\Program Files\MyMonero\resources\app.asar\local_modules\Lists\Views\ListCellView.web.js:27:14)Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) MyMonero/1.3.3 Chrome/83.0.4103.122 Electron/9.4.4 Safari/537.36

tried uninstalling but that didn't work.
![image](https://github.com/monero-project/monero-gui/assets/149293156/337fc422-c7df-4ffb-a167-cce8e5bd32bb)

![image](https://github.com/monero-project/monero-gui/assets/149293156/0bd430d6-843e-4d9f-980f-0d09dfedc94e)


# Discussion History
## selsta | 2023-10-29T13:49:39+00:00
Please report this to MyMonero support. This repository is for a different wallet software.

# Action History
- Created by: Mashedpot5 | 2023-10-29T07:50:00+00:00
- Closed at: 2023-10-29T13:49:39+00:00
