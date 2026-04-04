---
title: 'MacOS/MoneroGui: button to do first-run install'
source_url: https://github.com/monero-project/monero/issues/9296
author: kirk-kerekes
assignees: []
labels:
- reproduction needed
created_at: '2024-04-20T00:45:34+00:00'
updated_at: '2025-12-29T01:26:38+00:00'
type: issue
status: closed
closed_at: '2025-12-29T01:26:38+00:00'
---

# Original Description
I have determined that it is downright easy to end up with Monero-GUI "installed", but without an OS-authorized monerod. There probably should be a button that does whatever voodoo is required to authorize monerod to macOS, no matter if Monero-GUI thinks that this has already been done. OR, every "launch monerod" button should do the entire first-run voodoo.

# Discussion History
## selsta | 2024-04-20T00:46:50+00:00
How did you install monero-gui?

## kirk-kerekes | 2024-04-20T01:02:11+00:00
Dragged app to user applications folder. (~/Applications)Interrupted first run setup when I decided to use a clone of my existing blockchain rather than download. When it ultimately ran, the gui could not launch monerod. I launched it manually and handled the authorization, and then ran the gui. Kirk Kerekes On Apr 19, 2024, at 7:47 PM, selsta ***@***.***> wrote:﻿
How did you install monero-gui?

—Reply to this email directly, view it on GitHub, or unsubscribe.You are receiving this because you authored the thread.Message ID: ***@***.***>

## selsta | 2024-04-20T01:03:50+00:00
monerod is both codesigned and notarized by Apple, so everything should be done from our side. What do you mean with "authorization"? What did you authorize? Do you have a screenshot or remember what it said?

## kirk-kerekes | 2024-04-20T01:15:07+00:00
It was the typical os alert saying that monerod couldn’t be run because Apple could not determine that it came from a recognized developer. The dmg was a copy of the one I used without difficulty to install on another Mac. But on that Mac I did not interrupt the first-run process. So I assume that the issue was either the location (not in /Applications) or the interruption of the first-run. Or perhaps both. I assume that the gui is executing the monerod instance in the macOS folder of the app, and not copying it somewhere else. Kirk Kerekes On Apr 19, 2024, at 8:04 PM, selsta ***@***.***> wrote:﻿
monerod is both codesigned and notarized by Apple, so everything should be done from our side. What do you mean with "authorization"? What did you authorize? Do you have a screenshot or remember what it said?

—Reply to this email directly, view it on GitHub, or unsubscribe.You are receiving this because you authored the thread.Message ID: ***@***.***>

## kirk-kerekes | 2024-04-20T05:31:13+00:00
I should mention that the downloaded app dmg was “monero-gui-mac-armv8-v0.18.3.3.dmg”Kirk Kerekes On Apr 19, 2024, at 8:04 PM, selsta ***@***.***> wrote:﻿
monerod is both codesigned and notarized by Apple, so everything should be done from our side. What do you mean with "authorization"? What did you authorize? Do you have a screenshot or remember what it said?

—Reply to this email directly, view it on GitHub, or unsubscribe.You are receiving this because you authored the thread.Message ID: ***@***.***>

## kirk-kerekes | 2024-04-21T21:23:58+00:00
Additional notes:1. The Mac on which monerod launches and runs successfully is running a VPN (WireGuard), while the one that does not launch is _not_ running a VPN.2. I poked around in Console and noted that monerod appears to repeatedly launch and exit during the Monero-GUI startup. No error messages.Kirk Kerekes (iPad)On Apr 19, 2024, at 8:04 PM, selsta ***@***.***> wrote:﻿
monerod is both codesigned and notarized by Apple, so everything should be done from our side. What do you mean with "authorization"? What did you authorize? Do you have a screenshot or remember what it said?

—Reply to this email directly, view it on GitHub, or unsubscribe.You are receiving this because you authored the thread.Message ID: ***@***.***>

## selsta | 2024-04-22T00:36:42+00:00
We have codesigned all the programs and notarized the .dmg itself, basically everything required by Apple. I don't know why it complains about unknown developer.

## kirk-kerekes | 2024-04-22T00:59:51+00:00
I notice that the gui source contains a fork,etc utility— is that the normal path, or is that used only when the user enables “background” operation?Kirk Kerekes On Apr 21, 2024, at 7:37 PM, selsta ***@***.***> wrote:﻿
We have codesigned all the programs and notarized the .dmg itself, basically everything required by Apple. I don't know why it complains about unknown developer.

—Reply to this email directly, view it on GitHub, or unsubscribe.You are receiving this because you authored the thread.Message ID: ***@***.***>

## kirk-kerekes | 2024-04-22T18:34:39+00:00
The real issue is that the gui can’t successfully launch the daemon. ** What does the gui use to determine whether to run the first-run setup?I notice that if I run the daemon from Terminal it doesn’t honor the blockchain location info in the gui — it forces it to the default ~/.bitmonero folder. ** Is that the expected behavior? Or is that a clue?I have checked on my successful installation, and it is using the separate SSD correctly and apparently ignoring the original .bitmonero folder.I have the blockchain path in the gui set to a different physical volume because I see complaints in the logs that monerod is doing excessive writes to the SSD and I would rather replace a M.2 SSD than have my motherboard SSD get worn out.  Kirk Kerekes (iPad)On Apr 21, 2024, at 7:37 PM, selsta ***@***.***> wrote:﻿
We have codesigned all the programs and notarized the .dmg itself, basically everything required by Apple. I don't know why it complains about unknown developer.

—Reply to this email directly, view it on GitHub, or unsubscribe.You are receiving this because you authored the thread.Message ID: ***@***.***>

# Action History
- Created by: kirk-kerekes | 2024-04-20T00:45:34+00:00
- Closed at: 2025-12-29T01:26:38+00:00
