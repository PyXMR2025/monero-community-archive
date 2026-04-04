---
title: Windows x64 is misnamed in latest release assets
source_url: https://github.com/monero-project/monero/issues/6261
author: SomaticFanatic
assignees: []
labels: []
created_at: '2019-12-22T01:54:40+00:00'
updated_at: '2019-12-23T08:27:26+00:00'
type: issue
status: closed
closed_at: '2019-12-23T05:54:10+00:00'
---

# Original Description
Windows x64 zip has a file name of 15.0.1.1 not as it should be 15.0.1 (extra .1)

# Discussion History
## selsta | 2019-12-22T02:50:28+00:00
Where did you download the .zip ?

## SomaticFanatic | 2019-12-22T03:49:10+00:00
From GitHub. The assets list the Windows x64 file with an extra .1 but the GPG signed list of hashes doesn’t 

## selsta | 2019-12-22T07:26:16+00:00
ping @luigi1111 

https://github.com/monero-project/monero/releases/tag/v0.15.0.1

## SomaticFanatic | 2019-12-23T04:07:48+00:00
Not to FUD, but the current file should be checked against coin stealing like previous binaries had 

## luigi1111 | 2019-12-23T05:54:10+00:00
@selsta thanks, fixed.

## selsta | 2019-12-23T08:27:26+00:00
> Not to FUD, but the current file should be checked against coin stealing like previous binaries had

I confirmed that the hash was matching, just a typo in the filename.

# Action History
- Created by: SomaticFanatic | 2019-12-22T01:54:40+00:00
- Closed at: 2019-12-23T05:54:10+00:00
