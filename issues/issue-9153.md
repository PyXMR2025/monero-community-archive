---
title: wallet2.cpp-3e34503d.o.tmp infected with malware
source_url: https://github.com/monero-project/monero/issues/9153
author: sandytrevor
assignees: []
labels: []
created_at: '2024-02-06T03:22:35+00:00'
updated_at: '2024-02-06T03:26:44+00:00'
type: issue
status: closed
closed_at: '2024-02-06T03:24:06+00:00'
---

# Original Description
Tried to compile release-v0.18 on macOS Sonoma, but Avast found MacOS:Miner-GP[PUP] in wallet2.cpp-3e34503d.o.tmp.  Should I be using a different release, or is this a false threat by Avast?

# Discussion History
## selsta | 2024-02-06T03:24:06+00:00
The wallet contains miner code and that's why Avast is complaining, you can ignore it. Not malware.

## sandytrevor | 2024-02-06T03:26:42+00:00
Thanks!

 

From: selsta ***@***.***>
Reply-To: monero-project/monero ***@***.***>
Date: Monday, February 5, 2024 at 10:24 PM
To: monero-project/monero ***@***.***>
Cc: sandytrevor ***@***.***>, Author ***@***.***>
Subject: Re: [monero-project/monero] wallet2.cpp-3e34503d.o.tmp infected with malware (Issue #9153)

 

The wallet contains miner code and that's why Avast is complaining, you can ignore it. Not malware.

—
Reply to this email directly, view it on GitHub, or unsubscribe.
You are receiving this because you authored the thread.Message ID: ***@***.***>



# Action History
- Created by: sandytrevor | 2024-02-06T03:22:35+00:00
- Closed at: 2024-02-06T03:24:06+00:00
