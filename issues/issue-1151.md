---
title: '[feature] --language option for monero-wallet-cli'
source_url: https://github.com/monero-project/monero/issues/1151
author: athanclark
assignees: []
labels: []
created_at: '2016-09-30T15:40:49+00:00'
updated_at: '2017-09-19T23:24:20+00:00'
type: issue
status: closed
closed_at: '2017-09-19T23:24:20+00:00'
---

# Original Description
There's a `--password=...` argument, but there isn't a `--language="0"` argument: generating a wallet forces a programmer to supply the language int via stdin, which isn't healthy.


# Discussion History
## mbe24 | 2016-10-05T23:13:01+00:00
I will try to look into that.


## mbe24 | 2016-10-08T21:57:49+00:00
The problem lies within `std::string simple_wallet::get_mnemonic_language()`. There, a language out of a list provided by `crypto::ElectrumWords::get_language_list` has to be chosen be its index.


## athanclark | 2016-10-12T17:19:35+00:00
I did a little digging too, but C++ is way out of my league. I think there's some kind of options parsing class or something that clearly declares the CLI options, and different subcomponents peek into its instance to see if the option was provided already or not. I might be wrong though - I'll fetch a line number here soon.

This is similar with the "restore block height" input needed when restoring a deterministic seed; there's a `--restore-height` argument that has no effect when using `--restore-deterministic-wallet`, and again the index of the list of options needs to be supplied via stdin similarly.


## mbe24 | 2016-10-12T20:39:31+00:00
The problem lies in `simplewallet.cpp`. I'll change it so that when `--language=<int>` is provided, the program continues. If the parameter is missing, the language-to-index mapping is printed and the user is prompted. 

Please create another issue for your second request. Maybe I'll look into it, after I finished this one.


## rserranon | 2017-02-07T03:20:49+00:00
Also important for --restore-deterministic-wallet , there is no way to specify the language of words, I have found issues restoring wallets in spanish, documentation is not clear and test cases does not seem to have other languages for restore, any update on this? thx

## ghost | 2017-06-15T09:41:40+00:00
Bump.
Writing an application and could use this feature right now since it is not possible to create a wallet via RPC.

## hyc | 2017-06-15T13:55:28+00:00
Creating a wallet via RPC is supported in git master. 110b683152e4930247c88d426799d53943f19e72

## ghost | 2017-06-15T17:21:37+00:00
@hyc thank you for referencing me to this, however I'm afraid over the past two days of my research that it's not officially documented anywhere, or to at least what I have searched for. Could this be suggested as well?

Thanks.

## jonathancross | 2017-09-19T22:50:37+00:00
@mbe24 Did you ever make any progress on this?

## hyc | 2017-09-19T23:03:12+00:00
@ghost the docs are online now https://getmonero.org/resources/developer-guides/wallet-rpc.html#createwallet

## hyc | 2017-09-19T23:05:53+00:00
monero-wallet-cli now has a `--mnemonic-language` option. It was added in #2293 

## hyc | 2017-09-19T23:19:37+00:00
+resolved

# Action History
- Created by: athanclark | 2016-09-30T15:40:49+00:00
- Closed at: 2017-09-19T23:24:20+00:00
