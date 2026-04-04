---
title: monerod writing 1TiB on disk for a 50GiB (pruned) blockchain
source_url: https://github.com/monero-project/monero/issues/9965
author: hustlerone
assignees: []
labels:
- question
created_at: '2025-06-23T14:33:05+00:00'
updated_at: '2025-11-07T21:06:19+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
How do I avoid this? This seems like a mistake

# Discussion History
## nahuhh | 2025-06-23T15:02:26+00:00
More info needed.
- OS
- Install method
- monerod, monero-wallet-gui

note: the pruned chain is approximately 100gb

## hustlerone | 2025-06-23T17:47:47+00:00
> More info needed.
> 
>     * OS
> 
>     * Install method
> 
>     * monerod, monero-wallet-gui
> 
> 
> note: the pruned chain is approximately 100gb

I'm using NixOS, whose nixpkgs rev is 9e83b64f727c88a7711a2c463a7b16eedb69a84c.

I am using [monero-wallet-gui](https://github.com/NixOS/nixpkgs/blob/9e83b64f727c88a7711a2c463a7b16eedb69a84c/pkgs/by-name/mo/monero-gui/package.nix). Version would be 0.18.4.0


## hustlerone | 2025-06-25T18:43:47+00:00
Filesystem is XFS.

## nahuhh | 2025-06-25T19:45:59+00:00
Are you referring to total write amount, or size on disk?
Are you using any startup flags, such as --db-sync-mode? 

## hustlerone | 2025-06-26T14:18:08+00:00
Total write amount, flags field in monero GUI is left empty

## hustlerone | 2025-06-26T14:21:46+00:00
> Total write amount, flags field in monero GUI is left empty

I use [GNOME Resources](https://apps.gnome.org/en/Resources/) to monitor disk I/O. It seems to be somewhat accurate with readings

## oooo-ps | 2025-09-28T08:59:04+00:00
to prune the last blocks in a chain, you should read the earlier ones first, lol

## hustlerone | 2025-09-29T12:34:36+00:00
reads are NOT writes. I get the same amount of writes when pruning or not. This is unacceptable.

## oooo-ps | 2025-09-29T15:46:20+00:00
Read bytes from stream requires write destination: into the memory or into the disk.
Prune operation goes after that.

## hustlerone | 2025-11-07T21:06:19+00:00
> Read bytes from stream requires write destination: into the memory or into the disk. Prune operation goes after that.

There is absolutely no reason to write it back to the disk. I am not going to get my SSD killed because monerod wants to still support NT(dogshit)FS

# Action History
- Created by: hustlerone | 2025-06-23T14:33:05+00:00
