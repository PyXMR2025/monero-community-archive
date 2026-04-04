---
title: Add monero 'man' (manual) pages
source_url: https://github.com/monero-project/monero/issues/2516
author: jonathancross
assignees: []
labels: []
created_at: '2017-09-23T01:42:32+00:00'
updated_at: '2020-05-01T13:48:16+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Per #985 - We need to do a better job documenting how monero command line tools work and providing basic examples.  `man` pages are the most appropriate place for this.

Might consider adding website link(s) eg: https://getmonero.org/resources/user-guides/ (which need more info on cli tools, but that is another issue)


# Discussion History
## ghost | 2018-01-03T19:34:40+00:00
Fixed (partially) with #2832 ?

## jonathancross | 2018-01-19T19:18:16+00:00
It's a great start, but still feels like we need more detailed configuration info (there are many subtle configuration options and incompatible combinations / options).  Examples with explanation would be good too.

## adrelanos | 2020-05-01T13:48:15+00:00
I suggest to write man pages in markdown and then convert them to `.roff` using `ronn`, which is a markdown to roff converter. That's imo a lot easier to create and maintain than hand written `.roff` files.

* https://packages.debian.org/buster/ronn
* https://github.com/apjanke/ronn-ng

# Action History
- Created by: jonathancross | 2017-09-23T01:42:32+00:00
