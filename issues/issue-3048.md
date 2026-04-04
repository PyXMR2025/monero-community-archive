---
title: 'Inconsistent terminology: "wallet"'
source_url: https://github.com/monero-project/monero/issues/3048
author: ordtrogen
assignees: []
labels: []
created_at: '2018-01-02T22:37:17+00:00'
updated_at: '2018-01-06T21:44:57+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
As I was doing some localization work, I think I found a few inconsistencies in terminology. The file translations/monero.ts contains the strings of the command line interface and in it you find references to "watch only wallet", "view only", "incoming-only wallet". I guess these refer to the same thing and should therefore not be different. As for keys there are references to "view key" and "watch-only keys". There is a parameter called "-generate-from-view-key"

Moneropedia also uses the term "view key", so maybe this type of wallet should be called "view-only wallet"?

(Actually, when you begin to look into "key" a bit more there are many variations, but I'll try to summarize them in a separate issue.)

The GUI refers to "ReadOnly wallet", "view only wallet". Shouldn't it use only one and shouldn't it be consistent with the CLI? (I'll create a separate issue in that repo)

Just opening this for discussion. I can fix and create a PR once there is consensus.

CLI:
"This is a watch only wallet"
"Wallet is view only"
"Opened watch-only wallet"
"wallet is watch-only and has no spend key"
"Password for new watch-only wallet"
"wallet is watch-only and has no seed"
"wallet is watch-only and cannot transfer"
"Save a watch-only keys file"
"wallet is watch-only and cannot sign"
"wallet is watch-only and cannot export key images"
"Generate incoming-only wallet from view key"
"Restricts to view-only commands"


# Discussion History
## moneromooo-monero | 2018-01-04T12:29:58+00:00
 "Restricts to view-only commands" has nothing to do with view only wallets (and used to be right, but is not anymore).


## ordtrogen | 2018-01-04T20:25:21+00:00
I guess I could appeal to the old "I just put it there to see if someone would notice" :-)
Actually I had filtered on the word 'only' and copied all the matches. I can see that that string wasn't relevant.

Thanks @moneromooo-monero, at least someone replied. But I'm not sure what you mean. 
What used to be right but isn't anymore? The message "Restricts to ..." ? Should we open an issue for it? I'm not sure what it refers to





 


## moneromooo-monero | 2018-01-05T12:07:33+00:00
I just meant that the code restricts to commands which are appropriate, not stricly view only, so that message is technically incorrect, though gives an idea of what it does.

## ordtrogen | 2018-01-06T21:44:57+00:00
This issue is related to https://github.com/monero-project/monero-gui/issues/1058


# Action History
- Created by: ordtrogen | 2018-01-02T22:37:17+00:00
