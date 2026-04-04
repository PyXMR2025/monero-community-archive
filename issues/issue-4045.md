---
title: Warning messages about Qt and "Transaction extra" when starting monero-wallet-gui
source_url: https://github.com/monero-project/monero-gui/issues/4045
author: kdf8jsa1
assignees: []
labels: []
created_at: '2022-10-06T09:10:04+00:00'
updated_at: '2022-10-09T18:23:21+00:00'
type: issue
status: closed
closed_at: '2022-10-07T23:12:22+00:00'
---

# Original Description
When I run `monero-wallet-gui` the terminal prints what's below.

I have no issue with the wallet per se. All transactions are showing. The balance is accurate. I am just wondering what these messages mean, whether there is something wrong I should pay attention to, and/or fix.

Please let me know if I should open a single issue for each of the warning message.

```
$ ./monero-wallet-gui
2022-10-06 08:13:21.612	W Qt:5.15.6 GUI:- | screen: 1366x768 - available: QSize(1366, 767) - dpi: 96 - ratio:0.97775
2022-10-06 08:13:24.065	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.066	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.066	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.066	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.066	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.066	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.066	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.066	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.066	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.066	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.067	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.067	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.085	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.085	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.085	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.085	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.085	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.085	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.086	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.086	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.138	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.139	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.139	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.139	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.139	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.139	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.139	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.139	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.139	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.139	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.140	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.140	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.156	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.156	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.156	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.157	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.157	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.157	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.157	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.157	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.197	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.198	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.198	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.198	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.198	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.198	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.198	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.198	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.198	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.198	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.198	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.198	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.922	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.940	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.940	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.940	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.940	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.940	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.940	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.940	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:24.940	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:25.207	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:25.207	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:25.207	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:25.207	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:25.208	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:25.208	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:25.208	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:25.208	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:25.208	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:25.208	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2022-10-06 08:13:25.439	W Logging to "/home/user/.bitmonero/monero-wallet-gui.log"
2022-10-06 08:13:25.445	W qrc:/qt-project.org/imports/QtQuick/Controls/ApplicationWindow.qml:259:9: QML ContentItem: Binding loop detected for property "implicitWidth"
2022-10-06 08:13:25.457	W Invalid DNSSEC TXT record signature for updates.moneropulse.org: validation failure <updates.moneropulse.org. TXT IN>: no DNSKEY rrset for trust anchor . while building chain of trust
2022-10-06 08:13:29.199	W Loaded wallet keys file, with public address: <public address>
2022-10-06 08:14:03.930	I Monero 'Fluorine Fermi' (v0.18.1.2-release)
Forking to background...
2022-10-06 08:14:44.779	W Transaction extra has unsupported format: <d2d0feb53bdb5189c47847c4adc11264a54a6a984bc9b82b228522ab108b4985>
2022-10-06 08:14:44.780	W Transaction extra has unsupported format: <355f2db5ea9ba5eeff301e4543f94a6fe3b18c62b9a76f6914e7dd22f4d3de6a>
2022-10-06 08:14:44.780	W Transaction extra has unsupported format: <eeb260164fe10ff65f6d7fdc4032548bad3768eeea2cf9b04d0c2b7a7a59db8c>
2022-10-06 08:14:44.780	W Transaction extra has unsupported format: <232b76fcd082f5039c027dd8dd6eb2c87997200952d5a6b8a1926bcb17631dc5>
```

Settings > info: 

GUI version: 0.18.1.2-release (Qt 5.15.6)
Embedded Monero version: 0.18.1.2-release
Wallet path: /home/user/Monero/wallets/user/user
Wallet restore height: 2578730
Wallet log path: /home/user/.bitmonero/monero-wallet-gui.log
Wallet mode: Advanced mode (Local node)
Graphics mode: OpenGL

```
$ uname -a
Linux x220 5.4.0-126-generic #142+10.0trisquel11 SMP Wed Sep 21 13:30:40 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux
```

I found a mention of `Detected recursive rearrange. Aborting after two iterations` in https://github.com/monero-project/monero-gui/issues/3961 but I have no clipboard issue (i.e. the clipboard doesn't replace the address copied), and I am following https://github.com/monero-project/monero/issues/8452 with regards to:

`W Invalid DNSSEC TXT record signature for updates.moneropulse.org: validation failure <updates.moneropulse.org. TXT IN>: no DNSKEY rrset for trust anchor . while building chain of trust`.

So far I found no relevant hints about the warning messages:

`W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.`

and

`W Transaction extra has unsupported format`.

That would be great if someone can enlighten me about the meanings or implications of these warning messages.




# Discussion History
## sanderfoobar | 2022-10-07T23:10:37+00:00
As you may have noticed, all messages start with a `W`, this means they are categorized as warnings. Generally, in software development, warnings can be ignored by the user. They don't necessarily impact the core functionality of the program. They provide extra information for developers.

> Detected recursive rearrange. Aborting after two iterations.

This relates to QtQuick/QML which is the rendering and markup language used to create the graphical user interface. The warnings indicate some sort of fail-safe that has been triggered by the engine to stop a possible recursive loop (and subsequently quits after 2 iterations).

> no DNSKEY rrset for trust anchor

The information related to this problem is present in [issue #8452](https://github.com/monero-project/monero/issues/8452) (that you already found). For users, this message is benign and can be ignored.

> Transaction extra has unsupported format

More info [here](https://monero.stackexchange.com/a/6531). Again, can be ignored.



## kdf8jsa1 | 2022-10-09T18:23:20+00:00
Thank you for taking the time to write up the above explanation @selsta. Very clear.

# Action History
- Created by: kdf8jsa1 | 2022-10-06T09:10:04+00:00
- Closed at: 2022-10-07T23:12:22+00:00
