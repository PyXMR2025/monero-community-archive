---
title: Very important CLI warning about writing down 25 word seed not encoded in native
  languages
source_url: https://github.com/monero-project/monero/issues/2003
author: ghost
assignees: []
labels: []
created_at: '2017-04-24T19:07:35+00:00'
updated_at: '2017-11-14T20:40:31+00:00'
type: issue
status: closed
closed_at: '2017-11-14T20:40:31+00:00'
---

# Original Description
Hi all,

Is there any way we can call the following text from the wallet seed file to present it to the user in their native language? The translations already exist in the GUI code so copying that over is easy. 

However I can't quite figure out how to write the logic in the wallet code to read and present it to the user.

PLEASE NOTE: the following 25 words can be used to recover access to your wallet. Please write them down and store them somewhere safe and secure. Please do not store them in your email or on file storage services outside of your immediate control.



# Discussion History
## moneromooo-monero | 2017-04-24T19:45:39+00:00
See README.i18n for instructions

## moneromooo-monero | 2017-11-14T19:48:10+00:00
Anyway, it already seems to be translate-ready, and is currently translated in French and Italian. That's all we can reasonably do codewise, so I'll call it fixed. If you want your language, feel free to update translations/monero_XX.ts for your language code.

+resolved

# Action History
- Created by: ghost | 2017-04-24T19:07:35+00:00
- Closed at: 2017-11-14T20:40:31+00:00
