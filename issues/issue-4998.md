---
title: monero-wallet-cli doesn't accept password at command line
source_url: https://github.com/monero-project/monero/issues/4998
author: jacoblyles
assignees: []
labels:
- invalid
created_at: '2018-12-19T19:16:58+00:00'
updated_at: '2019-01-18T18:33:19+00:00'
type: issue
status: closed
closed_at: '2019-01-18T18:33:19+00:00'
---

# Original Description
`monero-wallet-cli` isn't allowing me to supply the wallet password with a command line argument. This hinders automation. 

For example, the following command will pause and ask me for the password:

`$ monero-wallet-cli --wallet-file wallet_4 --password "" --command prepare_multisig`

The output is:

```2018-12-19 19:14:47,179 INFO  [default] Page size: 4096
This is the command line monero wallet. It needs to connect to a monero
daemon to work correctly.
WARNING: Do not reuse your Monero keys on another fork, UNLESS this fork has key reuse mitigations built in. Doing so will harm your privacy.

Monero 'Beryllium Bullet' (v0.13.0.4-release)
Logging to monero-wallet-cli.log
Opened wallet: 49PNTCFicPUcbFhVSE6sWZQoJsdef11TTBFP7J7cDtk7ZpaJep3bbHJXtXsZYEW1ssVXrgAJcX56xTPhnkdLfUdNMDGpfid
**********************************************************************
Use the "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************
Wallet password:
```

# Discussion History
## rbrunner7 | 2018-12-21T16:37:53+00:00
I can't reproduce this problem with current HEAD, on a Debian Linux variant: It does not ask for a password but correctly complains that the `prepare_multisig` command needs parameters to execute (if I just use the command as listed above).

I tried with an empty password, as suggested by the command line, and also with a password set.

## fluffypony | 2018-12-21T16:41:09+00:00
Just to be clear - is this with a blank password or not? Also do you have to run release builds or can you run head?

## jacoblyles | 2018-12-21T19:29:56+00:00
Running on latest master ed54ac8fdfe332c4ec6b9fd9331024d862ecad51 built and running on Mac OS 10.14.2

I tried with an empty password and a password set. 

```
./monero-wallet-cli --wallet-file mywallet2 --password 123 --command prepare_multisig
This is the command line monero wallet. It needs to connect to a monero
daemon to work correctly.
WARNING: Do not reuse your Monero keys on another fork, UNLESS this fork has key reuse mitigations built in. Doing so will harm your privacy.

Monero 'Beryllium Bullet' (v0.13.0.0-master-6bc0c7e6)
Logging to ./monero-wallet-cli.log
Opened wallet: 49UbTpH7SUjiHbiNb6GiYuYkVgqBMGNUM1kgVvKudhTm8VBAoripmHuisCaZhBda4pZaVFXEeRoPxZ3P2jJco8kb3J67Rkt
**********************************************************************
Use the "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************
Wallet password:
```

`prepare_multisig` does not require parameters. When I supply the password, it returns the expected multisig data. 

## jacoblyles | 2018-12-21T19:31:30+00:00
Do you think this could be a Mac vs. Linux thing? I could spin up a linux box somewhere and see if I get what you get. 

## rbrunner7 | 2018-12-21T19:55:41+00:00
> prepare_multisig does not require parameters. When I supply the password, it returns the expected multisig data.

Yes - I think chose one of the other multisig commands by accident.

I just tried with 0.13.0.4 release on Windows and could reproduce the problem. As I tried with **HEAD** on Linux I would guess that one of the commits since release corrects the problem. Command-line parsing is so simple it's very hard to imagine that there are accidental or unexpected differences between Linux and MacOS there.

## moneromooo-monero | 2018-12-21T20:27:51+00:00
If you want to automate things, monero-wallet-rpc is really what you want, but I suspect you can bypass that particular password prompt by setting the wallet to not ask (set ask-password 0).

## dethos | 2019-01-11T13:54:45+00:00
> but I suspect you can bypass that particular password prompt by setting the wallet to not ask (set ask-password 0).

This actually solves the reported problem. 
The issue with the initial command is that the `--password` argument is used to "open" the wallet file, but running the `prepare_multisig` command also requires the password and that is the one being asked on the provided output example.

## moneromooo-monero | 2019-01-18T18:31:38+00:00
+invalid

# Action History
- Created by: jacoblyles | 2018-12-19T19:16:58+00:00
- Closed at: 2019-01-18T18:33:19+00:00
