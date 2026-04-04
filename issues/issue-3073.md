---
title: UI strings of monerod are not localizable
source_url: https://github.com/monero-project/monero/issues/3073
author: ordtrogen
assignees: []
labels:
- wontfix
created_at: '2018-01-06T21:13:16+00:00'
updated_at: '2018-01-09T20:48:29+00:00'
type: issue
status: closed
closed_at: '2018-01-09T20:48:29+00:00'
---

# Original Description
Looking at monero/translations/monero.ts I can only find strings related to the monero-wallet-cli, it seems like. No strings from monerod.

Source confirms it:

in src/simplewallet/simplewallet.cpp has
  const command_line::arg_descriptor<std::string> arg_generate_new_wallet = {"generate-new-wallet", sw::tr("Generate new wallet and save it to <arg>"), ""};

whereas src/common/command_line.cpp has
  const command_line::arg_descriptor<std::string> arg_check_updates = {
    "check-updates"
  , "Check for new versions of monero: [disabled|notify|download|update]"
  , "notify"
  };

Notice there's a sw::tr("...") in simplewallet.cpp but not in command_line.cpp ? That's the magic what makes a string localizable.  Should probably go thru all strings in source of monero repo. 


# Discussion History
## ordtrogen | 2018-01-06T21:13:46+00:00
Is this what we mentioned at the meeting, @erciccione ?




## moneromooo-monero | 2018-01-07T10:45:50+00:00
The daemon was not considered important enough to bother, and what is outputs are normal logs (mostly). This means a lot more stuff to make translatable for less benefit than the wallet. Moreover, this is not only the daemon, but all the libs too. Now that we have a GUI wallet, this is also much less important since most people will use the GUI wallet which is translatable.


## dEBRUYNE-1 | 2018-01-09T20:46:35+00:00
+wontfix

# Action History
- Created by: ordtrogen | 2018-01-06T21:13:16+00:00
- Closed at: 2018-01-09T20:48:29+00:00
