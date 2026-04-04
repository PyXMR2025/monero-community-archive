---
title: 'error: ‘class Monero::Wallet’ has no member named ‘useForkRules’'
source_url: https://github.com/monero-project/monero-gui/issues/610
author: voidzero
assignees: []
labels: []
created_at: '2017-03-26T00:34:52+00:00'
updated_at: '2017-03-26T21:25:50+00:00'
type: issue
status: closed
closed_at: '2017-03-26T21:25:50+00:00'
---

# Original Description
```
../src/libwalletqt/Wallet.cpp: In member function ‘bool Wallet::useForkRules(quint8, quint64) const’:
../src/libwalletqt/Wallet.cpp:592:26: error: ‘class Monero::Wallet’ has no member named ‘useForkRules’
     return m_walletImpl->useForkRules(required_version,earlyBlocks);
                          ^~~~~~~~~~~~
```

This was added in commit 9c4c34d502 [(here)](https://github.com/monero-project/monero-core/commit/9c4c34d502e7179964061c6af72470e37f9257af#diff-baee99f2666264019ce07f83673811f0R590)
The commit message says 'requires #1915' but I don't know what that refers to.

# Discussion History
## ghost | 2017-03-26T02:25:24+00:00
That refers to PR #1915 on the main monero project: https://github.com/monero-project/monero/pull/1915

Since this was merged, it should automatically be included when your GUI builds the daemon. So I'm unsure what the issue is. Perhaps Jaquee has a better idea.

## Jaqueeee | 2017-03-26T12:45:12+00:00
if v0.10.3 was pulled when you tried to build the GUI you didn't get the last patches. Please try again

## voidzero | 2017-03-26T21:25:50+00:00
Indeed. My bad. Sorry!

# Action History
- Created by: voidzero | 2017-03-26T00:34:52+00:00
- Closed at: 2017-03-26T21:25:50+00:00
