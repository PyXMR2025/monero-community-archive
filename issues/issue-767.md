---
title: Sign/verify 'Signature' input box broken on latest build monero-core-osx-10.12
source_url: https://github.com/monero-project/monero-gui/issues/767
author: tficharmers
assignees: []
labels: []
created_at: '2017-06-15T11:10:41+00:00'
updated_at: '2017-09-04T15:16:29+00:00'
type: issue
status: closed
closed_at: '2017-09-04T15:16:29+00:00'
---

# Original Description
The attached screenshot shows the 'Signature' box for the Verify form to be broken/squashed. This was from build #778.

![screen shot 2017-06-15 at 11 49 13](https://user-images.githubusercontent.com/23356013/27178810-9fd3a23c-51c3-11e7-9169-54912c6bd13b.PNG)


# Discussion History
## jonathancross | 2017-06-16T20:48:44+00:00
Description says OSX, but screenshot looks more like Linux maybe?
Is it always squashed or are there steps to reproduce?

## tficharmers | 2017-06-19T09:34:33+00:00
Definitely macOS. I just went to the sign/verify tab and it was just like that. It was from build #778, not the official beta release. I got it from the [buildbot page](https://build.getmonero.org/builders/monero-core-osx-10.12). Can't test later builds yet as they have failed.

## jonathancross | 2017-06-19T15:53:40+00:00
Thanks for confirming platform and build, I am also seeing this issue on OSX.
I'll look into this and see if I can determine what is causing it to collapse.
**edit:** Got sidetracked with current Mac build issues :-(

## Jaqueeee | 2017-06-21T10:12:58+00:00
I'm also seeing it. i'll look into it soon^tm

## MaxXor | 2017-08-31T12:11:43+00:00
This issue is platform-wide, not OSX specific. Fixed it in the referenced PR.

# Action History
- Created by: tficharmers | 2017-06-15T11:10:41+00:00
- Closed at: 2017-09-04T15:16:29+00:00
