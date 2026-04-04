---
title: export_outputs should export all outputs
source_url: https://github.com/monero-project/monero/issues/5716
author: hokkjoy
assignees: []
labels: []
created_at: '2019-07-01T12:38:20+00:00'
updated_at: '2020-12-14T14:06:10+00:00'
type: issue
status: closed
closed_at: '2020-12-11T17:24:06+00:00'
---

# Original Description
`export_outputs` only actually exports outputs that haven't been exported before, leading to an incomplete file.

When we try to use this file on a prestine wallet (`import_outputs <outputs_file>`), the command fails with the following error message:

`Error: Failed to import outputs outputs_file: Failed to import outputsImported outputs omit more outputs that we know of`

#5418 apparently solved this **for RPC**. However, for **CLI**, the issue remains.

I would also argue that exporting all outputs should be the *default* for CLI.


# Discussion History
## moneromooo-monero | 2019-07-01T12:56:08+00:00
The default should be incremental, since that's what most people will need. I'll add an option to export all.

## moneromooo-monero | 2019-07-02T19:43:29+00:00
https://github.com/monero-project/monero/pull/5722

## hokkjoy | 2019-07-15T09:56:54+00:00
> The default should be incremental, since that's what most people will need.

How come and how do you know?

## moneromooo-monero | 2019-07-15T14:13:33+00:00
It takes a lot of time to duplicate that work for large wallets, and files get big.

## hokkjoy | 2019-08-09T09:58:25+00:00
I suppose with "large" you refer to one with many tx's. My cold wallet is always freshly opened from seed in a live OS environment with no previous files available. That tends to be the safest way and is a sensible default for individual users (the majority). Exchanges (probably those with "large" wallets - the minority) will not have much trouble to find out that an optional `incremental` switch may make their live easier.

## dnaleor | 2019-08-23T10:16:06+00:00
Tend to agree with hokkjoy here. If you see a command called "export_outputs" you would expect that all outputs are exported. I use a similar system for my cold storage, I always use a fresh clean OS and wallet.

## moneromooo-monero | 2019-09-02T11:18:01+00:00
Any other opinions here ?

## moneromooo-monero | 2019-09-16T20:48:44+00:00
After thinking about this, I think it may be best to change this as requested. Along with a message telling you whether the export was full or partial, so the user can redo if necessary.

## Adreik | 2020-06-17T23:50:23+00:00
How does one export a particular owned output?

The help simply states "export_outputs [all] <filename>" is the usage.

For example, say I want to export an output associated with a specific pubkey?

## moneromooo-monero | 2020-06-20T15:48:40+00:00
You can't.

## jonathancross | 2020-11-07T21:23:44+00:00
Seems this can be closed now?

## jonathancross | 2020-12-14T14:06:09+00:00
> After thinking about this, I think it may be best to change this as requested. Along with a message telling you whether the export was full or partial, so the user can redo if necessary.

@moneromooo-monero Sorry, I mistakingly thought this was already implemented (default to "all") based on your comment.
Personally I think this would be a very useful change and would avoid some confusing behavior for users.
Larger files for those who are too lazy to specify "incremental" seems like a fine tradeoff.

# Action History
- Created by: hokkjoy | 2019-07-01T12:38:20+00:00
- Closed at: 2020-12-11T17:24:06+00:00
