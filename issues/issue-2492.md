---
title: Using command line options is it possible to enable `huge-pages-jit`?
source_url: https://github.com/xmrig/xmrig/issues/2492
author: Joe23232
assignees: []
labels:
- bug
created_at: '2021-07-24T04:30:07+00:00'
updated_at: '2023-12-10T10:18:14+00:00'
type: issue
status: closed
closed_at: '2021-12-19T15:39:57+00:00'
---

# Original Description
https://xmrig.com/docs/miner/command-line-options

Through the command line options is it possible to enable `huge-pages-jit`?

can't seem to find it

# Discussion History
## xmrig | 2021-07-24T05:28:44+00:00
Fixed in dev branch.
Thank you.

## Joe23232 | 2021-07-24T05:36:55+00:00
No worries and thank you mate =D

## Joe23232 | 2021-07-24T06:45:47+00:00
@xmrig 

You may want to add it in the man pages

https://xmrig.com/docs/miner/command-line-options

Also how would I exactly specify as a command-line option?

## xmrig | 2021-07-24T09:42:40+00:00
Website will be updated later. Anyway config file is the preferred way to configure the miner, pure command line configuration or mixed configuration for people who know exactly what they want or for simplicity in some cases: e.g. generate sample command line by https://xmrig.com/wizard and add required option.
Thank you.

## Joe23232 | 2021-07-24T09:52:35+00:00
@xmrig Hi, I understand the config file is the way to go, however I have a good reason why I want to use CLI instead of json files. And I understand that you have a config sample generator, however I don't see an option to enable `"huge-pages-jit": true,`.

I just wanted to know what the argument is for CLI to enable `huge-pages-jit`?

## xmrig | 2021-07-24T09:57:05+00:00
It will be `--huge-pages-jit` in next release or now in dev branch if you don't want to wait https://github.com/xmrig/xmrig/commit/d24581c9633cb60c3c588975a32bc969e7c6a5b3 Current release doesn't have the option.
Thank you.



## Joe23232 | 2021-07-24T11:06:07+00:00
@xmrig Thanks mate I have got dev version now mate =D

## DeeDeeRanged | 2021-08-03T00:07:25+00:00
What does it actually do? I see it is set to false in the json file?

## Joe23232 | 2021-08-03T00:15:58+00:00
@DeeDeeRanged It optimises the performance but I don't know what it actually does to optimise everything.

## Spudz76 | 2021-08-03T10:21:14+00:00
@DeeDeeRanged The main RandomX dataset (2080+256MB) can be allocated one of three ways: with no hugepages (slow) 2MB hugepages (faster) or 1GB hugepages (Linux only, even faster than 2MB on some CPUs, not slower on any).

This reduces the number of page references in the CPUs memory controller (TLB) which can cause memory access to be faster due to smaller lookup-table.  1GB pages there are 3 pages (3072MB); 2MB gets 1168 pages (2336MB); 4KB (no hugepages) gets 1196032 pages (2336MB).

The regular scratchpads, RandomX or not, use 2MB hugepages.  So if you use 1GB ones you still need a few 2MB ones, but many less.

Hugepages also keep memory contiguous which optimizes transfers.  Vs everything in 4KB chunks that could be anywhere, not that there is a seek penalty such as on a disk, but cache transfers have to gather-collate (opposite of scatter-gather) rather than more of a one-shot range copy.

## DeeDeeRanged | 2021-08-21T11:46:42+00:00
Ok. But was is the difference between hugepages and hugepages-jit? I do get it that hugepages improve performance I have hugepages enabled (they are supported). Just call me ignorant if I don't get it all my brain does sometimes get fuzzy ;)

## ghost | 2021-12-19T18:39:04+00:00
@xmrig I don't understand why this issue has been closed. Can you please be more specific about why it has been closed?

## Spudz76 | 2021-12-19T19:46:23+00:00
Because it was fixed 5 months ago, probably.

## ghost | 2021-12-19T20:20:31+00:00
> Because it was fixed 5 months ago, probably.

`--huge-pages-jit` is printed by `xmrig --help`, but it is missing from https://xmrig.com/docs/miner/command-line-options which was mentioned in 1st post of this issue.

## Spudz76 | 2021-12-19T20:47:30+00:00
Sure, the docs weren't updated, but that wouldn't be the first thing wrong with the docs.  `--help` are the only true docs.

The actual feature is complete, and did not exist, so this is fixed.

I suppose if the web site was on a repo, we could suggest bugs fixes for the web site.  But this is for the application itself.

## xmrig | 2021-12-20T03:31:30+00:00
I just updated mentioned page too.
Thank you.

## dchmelik | 2023-12-10T03:47:40+00:00
> But was is the difference between hugepages and hugepages-jit?

Yes: what's the difference?

## Spudz76 | 2023-12-10T10:18:13+00:00
JIT requires slightly insecured CPU where a data page can also be executable.  So that the randomx VM can generate and execute the mutations without an extra memory copy.

Doesn't work on paranoid platforms like Apple M1 and some others where security or design forces data pages to be non-exec.  May not add much speed on others where it works (non-AES...)

# Action History
- Created by: Joe23232 | 2021-07-24T04:30:07+00:00
- Closed at: 2021-12-19T15:39:57+00:00
