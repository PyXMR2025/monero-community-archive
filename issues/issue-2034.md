---
title: 'Compiling the Monero GUI from source: On OS X: brew install boost --c++11
  error'
source_url: https://github.com/monero-project/monero-gui/issues/2034
author: akseeker
assignees: []
labels:
- resolved
created_at: '2019-03-26T02:53:41+00:00'
updated_at: '2019-03-27T06:55:31+00:00'
type: issue
status: closed
closed_at: '2019-03-27T02:36:32+00:00'
---

# Original Description
Newb here, trying to follow the OS X compile steps.

When I copy/paste "brew install boost --c++11" I get "Install formula.", a list of options, and "Error: invalid option: --c++11"

Is there a step missing?

Thanks!

macOS High Sierra, version 10.13.6 (17G5019), Xcode Version 9.0 (9A235)

# Discussion History
## selsta | 2019-03-26T06:33:16+00:00
`brew install boost` should be enough.

## akseeker | 2019-03-26T08:31:37+00:00
Thanks, that appears to be working.

Curious, why was the --c++11 used?

## selsta | 2019-03-26T11:27:55+00:00
It has been like this since the beginning, see here: https://github.com/monero-project/monero-gui/commit/5b1ab69d70a29c4ddf66d5f107f621ed3340d066

I’ve updated the README in #2035.

## sanderfoobar | 2019-03-27T02:34:24+00:00
+resolved

## akseeker | 2019-03-27T06:53:15+00:00
thanks, were the instructions on https://github.com/monero-project/monero-gui going to be changed too? (they read the same as of this email…)

Thanks

On Mar 26, 2019, at 03:28 AM, selsta <notifications@github.com> wrote:

It has been like this since the beginning, see here: 5b1ab69
I’ve updated the README in #2035.
—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub, or mute the thread.

## selsta | 2019-03-27T06:55:31+00:00
Yes, the instructions will change once #2035 is merged.

# Action History
- Created by: akseeker | 2019-03-26T02:53:41+00:00
- Closed at: 2019-03-27T02:36:32+00:00
