---
title: Add lupdate to building process
source_url: https://github.com/monero-project/monero-gui/issues/2160
author: erciccione
assignees: []
labels:
- enhancement
created_at: '2019-05-04T18:41:30+00:00'
updated_at: '2019-06-21T19:31:16+00:00'
type: issue
status: closed
closed_at: '2019-06-21T19:31:16+00:00'
---

# Original Description
Would be great to include `lupdate` in the building process right before the language files are built. This would resolve the sync problems happening when something change in the code and consequently the referred string in the language files (`/translations`), causing the string getting ignored in the compiled wallet, even if correctly translated.

This was solved in past by resyncing all language files before tagging a release. Including the resync with lupdated every time the wallet is built is a better and cleaner solution.

The command that should run is:
```
lupdate -pro monero-wallet-gui.pro -ts translations/monero-core_*.ts -no-obsolete
```

*As discussed in the meeting of the Lcalization Workgroup (monero-ecosystem/monero-translations#51).*

# Discussion History
## erciccione | 2019-05-04T18:42:55+00:00
+enhancement

## selsta | 2019-05-05T01:01:36+00:00
One thing to note is that it can get pretty annoying with merge conflicts if translation file changes are included with with every commit.

## erciccione | 2019-05-05T09:38:46+00:00
I'm not sure of what you mean. There wouldn't be any conflict or commit, it would be just a refresh of the language files during the compilation process. No git involved

## mmbyday | 2019-06-01T06:15:31+00:00
@erciccione Does that PR close this issue? :-)

## erciccione | 2019-06-01T10:28:47+00:00
Left a comment in #2189 . Yes, that PR will resolve this issue.

# Action History
- Created by: erciccione | 2019-05-04T18:41:30+00:00
- Closed at: 2019-06-21T19:31:16+00:00
