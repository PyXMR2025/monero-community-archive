---
title: P2Pool failed to load to Monero Wallet on IMAC M1
source_url: https://github.com/monero-project/monero-gui/issues/4604
author: 24jaking-hue
assignees: []
labels: []
created_at: '2026-06-10T00:21:22+00:00'
updated_at: '2026-06-16T20:54:23+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I have been able to solo mine from Monero wallet but when I try to set up mini P2Pool I get a P2Pool Failed to load message.


# Discussion History
## 24jaking-hue | 2026-06-16T20:27:55+00:00
Yes, it was an issue with gpg, working now.Sent from my iPhoneOn Jun 16, 2026, at 1:17 PM, kyliebryna45-prog ***@***.***> wrote:﻿kyliebryna45-prog left a comment (monero-project/monero-gui#4604)
@24jaking-hue Have you been able to resolve this issue?

—Reply to this email directly, view it on GitHub, or unsubscribe.Triage notifications, keep track of coding agent tasks and review pull requests on the go with GitHub Mobile for iOS and Android. Download it today!
You are receiving this because you were mentioned.Message ID: ***@***.***>

## selsta | 2026-06-16T20:30:23+00:00
Reminder to not use P2Pool unless you manually update to the latest version outside GUI, or you wait until the next GUI release.

https://github.com/SChernykh/p2pool/security/advisories/GHSA-fm6j-gf38-p925

# Action History
- Created by: 24jaking-hue | 2026-06-10T00:21:22+00:00
