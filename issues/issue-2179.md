---
title: monero-wallet-rpc now prompts for password if none is supplied
source_url: https://github.com/monero-project/monero/issues/2179
author: moneromooo-monero
assignees: []
labels: []
created_at: '2017-07-17T11:43:34+00:00'
updated_at: '2017-12-02T09:56:23+00:00'
type: issue
status: closed
closed_at: '2017-12-02T09:56:23+00:00'
---

# Original Description
It would previously error out. I think that was better, since it allows starting unattended (if a --password or --password-file is supplied, obviously). Opinions ?

# Discussion History
## moneromooo-monero | 2017-07-17T12:05:03+00:00
Actually, it also asks if the wallet being loaded has no password, so this needs changing anyway.

## Timo614 | 2017-10-30T18:35:48+00:00
Just to write down my understanding of this and confirm the behavior we want:

- <s>No `--wallet-file` and no password is passed in it asks for the wallet name
  - Wallet name exists? Asks for password and if valid logins in; failure invalid password message
  - Wallet name does not exist? Asks user if they'd like to make it and asks them for a password for the wallet (was CLI specific case / diverges from the RPC's login interface and I've adjusted my PR so that it only affects RPC now)</s>
- `--wallet-file` specified with a password
  - If password is correct logins
  - If password is invalid fails with an invalid password message
- `--wallet-file` specified with no password
  - Asks for password and if valid logins in; failure invalid password message

So the behavior here we're trying to fix is for the case of a `--wallet-file` that expects no password?
`--password ""` can handle that at the moment but it's less immediately obvious with a wallet with no password that you'd need to supply it in that way.

So the correct behavior here is to just treat the lack of the password as if the password was empty in the place of asking for one? If so sounds good.

## moneromooo-monero | 2017-10-31T11:04:25+00:00
I think the best would be to have an --prompt-for-password flag, to allow monero-wallet-rpc to prompt. The problem I have with prompting is that tools like monero-wallet-rpc are supposed to be used in scripts (ie, a restart script), and/or without a human at the console, so you usually don't want them to prompt and wait till they get some input.

## moneromooo-monero | 2017-12-02T09:14:26+00:00
+resolved

# Action History
- Created by: moneromooo-monero | 2017-07-17T11:43:34+00:00
- Closed at: 2017-12-02T09:56:23+00:00
