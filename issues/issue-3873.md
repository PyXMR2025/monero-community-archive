---
title: Signed binaries / Code signing for Windows
source_url: https://github.com/monero-project/monero-gui/issues/3873
author: MajesticBank
assignees: []
labels: []
created_at: '2022-03-26T11:09:31+00:00'
updated_at: '2022-03-26T21:41:05+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hello,

 The proposal is to consider distributing signed binaries for Windows specifically since historically antivirus software showed no interest in recognizing monero official wallet as legitimate software and were quicker to flag it as malware / unwanted rather the whitelisting the software by hash or similar.

Considering integrity of binaries are provides with hash values, code singing main purpose would be to defeat Windows defender attacking / jamming on Monero wallet and other proactive and heuristic antiviruses doing the same thing. We often encounter problems with our customers that  Monero wallet is locked in which way that for an average user can't solve often by following simple steps and without us compromising their privacy to help them.

There are two types of code singing certificate EV and OV. EV it a bit more advanced because it allows singing drivers on Windows 10 and after and required hardware token, like one you get in the bank acting as OTP but its nothing super complicated considering level of sophistication on which monero works.

Other and much more simpler option would OV code signing certificate required no extra hardware, would bring legitimacy to monero binaries across antivirus reputation networks.

Code singing issuance process is rather easy and is completed within week or two maximum.

Mostly newbie users would benefit from this and those who might doubt in Monero all together when first time encountering with Monero.

Signed binaries are shipped for both Bitcoin and Litecoin code binaries.

Price is nothing expensive and community including us can easily come up easily to sponsor that.



 


# Discussion History
## selsta | 2022-03-26T21:41:05+00:00
As far as I know Feather wallet will try to sign their wallet with an EV cert. Then we can see if it makes a difference in regards to anti virus.

# Action History
- Created by: MajesticBank | 2022-03-26T11:09:31+00:00
