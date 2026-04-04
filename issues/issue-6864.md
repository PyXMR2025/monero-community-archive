---
title: Cannot import keyimage format version 2
source_url: https://github.com/monero-project/monero/issues/6864
author: muff1nman
assignees: []
labels: []
created_at: '2020-10-07T03:59:45+00:00'
updated_at: '2020-10-14T16:16:22+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
```
[wallet XXXXXX]: import_key_images keyimages.dat
Error: Failed to import key images: Bad key image export file magic in keyimages.dat
```
```
$ dd if=keyimages.dat bs=24 count=1 of=/dev/stdout status=none | hexdump -C
00000000  4d 6f 6e 65 72 6f 20 6b  65 79 20 69 6d 61 67 65  |Monero key image|
00000010  20 65 78 70 6f 72 74 02                           | export.|
00000018
```
https://github.com/monero-project/monero/commit/8d71b2b1b3714a13d46247ed7342a1ad292c488d#diff-9d580668dab930045943902048e2ac22L116-R116

1. Why can't I import a keyimages v2 format?
2. Can I at least get an error message saying that the keyimage file is an older format?

# Discussion History
## moneromooo-monero | 2020-10-07T16:38:25+00:00
Are the two wallets not running the same version ?
The file format changed to prevent possible exploits since the boost format we used has a few buffer overflows.


## muff1nman | 2020-10-07T17:08:15+00:00
No the offline wallet was using an older version (and still is until I can recompile to deal with a glibc incompatibility). Since these are key image files I trust, I'm not worried about buffer overflows. 

## hyc | 2020-10-07T17:28:36+00:00
>  glibc incompatibility

Is it this one due to lgamma/signgam, or yet another one? #6862

## muff1nman | 2020-10-07T21:51:46+00:00
2.23 Was the glibc version complained about but haven't looked into it beyond that.

## muff1nman | 2020-10-11T20:19:30+00:00
I don't think its reasonable to prevent people from loading old keyimage files as it makes it *impossible* (correct me if I'm wrong) to restore an offline wallet completely without being able to import old saved keyimages.

## moneromooo-monero | 2020-10-12T15:58:58+00:00
It's not preventing you from loading old format. It's preventing you from loading a new format.

## muff1nman | 2020-10-14T16:16:22+00:00
Sure, but regardless one would still be stuck as if you setup a new offline wallet with the newest verison of monero you cannot get back to your previous state without being able to import older formats. 

# Action History
- Created by: muff1nman | 2020-10-07T03:59:45+00:00
