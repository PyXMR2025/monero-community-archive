---
title: incorrect password when using --password on creation
source_url: https://github.com/monero-project/monero/issues/1957
author: grummerd
assignees: []
labels: []
created_at: '2017-04-04T09:41:50+00:00'
updated_at: '2017-08-07T18:24:19+00:00'
type: issue
status: closed
closed_at: '2017-08-07T18:24:19+00:00'
---

# Original Description
Plz confirm this as an awful nasty critical bug

1. Delete the old wallet files or don't. This step is just so there is no ambiguity on the wallet file names

1. Make a new wallet, passing in the password from the command line using --password=[password]

1. Once wallet is sync'ed, type in the command `viewkey`

1. Prompted for a password. Type in the password manually

**The password will be invalid**

    ./monero-wallet-cli --generate-new-wallet=~/.monero/earl-grey-latte.xmr.wallet --password=[the password] --daemon-address=[daemon ip]:18081 --trusted-daemon --daemon-login=[daemon login]:[daemon password]

In summary,

This is critical cuz the **user will believe they have a usable wallet**. Possibly accept a payment and then be unable to use their wallet!

This bug could cause, monero-wallet-cli users to lose their ability to access their monero

# Discussion History
## moneromooo-monero | 2017-04-04T10:43:14+00:00
Please name bugs in relation with their content (here, eg, incorrect password when using --password on creation).

Besides, it works for me. Are you sure you didn't used characters which get interpreted by your shell ?


## ghost | 2017-04-04T11:04:25+00:00
Can you give us a sample password that fails?

## grummerd | 2017-04-04T11:04:50+00:00
You maybe correct about the shell escaping characters

This is an UX issue. If there is the slightest possibility of producing an unusable wallet and users losing access to funds then it should be prevented if possible.

Suggested solution is preventing `--generate-new-wallet` (--generate-from-view-key, --generate-from-keys, --generate-from-json, --restore-deterministic-wallet, or --electrum-seed) and `--password` being used together

Using `--password` and `--wallet-file` was able to get into the wallet. Giving the impression the wallet is usable.

The non-alphanumeric character is dollar sign ($) in the middle of the password

The command is an alias within ~/.profile

So we are both right! None the less, it's still a critical UX bug

In the very least there needs to be a warning in the `--help`

    --password arg                      Wallet password. **Be careful shell isn't interpreting special characters. Confirm password works whenever creating wallets**  

## grummerd | 2017-04-04T11:06:13+00:00
@NanoAkron 

Hope the explanation above is enough to reproduce this issue

## moneromooo-monero | 2017-04-04T11:07:19+00:00
Yes, $ is variable expansion, which explains it.
This falls under basic OS usage. If you want to use $, either escape, or quote.


## grummerd | 2017-04-04T11:13:29+00:00
If people can lose BIG MONEY. It's an UX issue. Not a coding bug. Even if only dumb noobs might run into this issue. It's money we are talking about. And noobs losing their money is bad

Minimally, needs a disclaimer in `--help`

## moneromooo-monero | 2017-04-04T11:17:23+00:00
I'll add a "duh" bit in --password help, yes.

## grummerd | 2017-04-04T11:30:39+00:00
@moneromooo-monero 
ty

That *duh bit*, if it prevents disasters is well worth it. Monero needs to cater to everyone, not just the IT literate.

Even the IT literate make mistakes

Been following monero since it was usd$0.70 Still going thru the learning curve. 

In the back of my head often thinking, "how am i going to teach this to utter idiots". Been able to teach bitcoin. Monero is next!

## moneromooo-monero | 2017-04-06T22:23:28+00:00
https://github.com/monero-project/monero/pull/1959/files

## jonathancross | 2017-06-03T12:54:58+00:00
This is now fixed and can be closed.

## moneromooo-monero | 2017-08-07T18:02:04+00:00
+resolved

# Action History
- Created by: grummerd | 2017-04-04T09:41:50+00:00
- Closed at: 2017-08-07T18:24:19+00:00
