---
title: Trouble installing Monero gui on Linux 32bit.
source_url: https://github.com/monero-project/monero-gui/issues/735
author: Justin435
assignees: []
labels:
- resolved
created_at: '2017-05-19T03:10:40+00:00'
updated_at: '2017-08-07T17:30:09+00:00'
type: issue
status: closed
closed_at: '2017-08-07T17:30:09+00:00'
---

# Original Description
After downloading and extracting the Linux 32 GUI fil I opened the start-gui.sh file and it loads the program but there are no words anywhere. Images are there and everything seems to function fine I just can't see any instructions anywhere. I can highlight and copy paste the 25 words into a text document and see them there so things are working just not visible. It might just be a corrupt file or something but I have downloaded it several times with the same results. Any idea what this could be? Also I am fairly new to Linux so the more details the better. 

# Discussion History
## jonathancross | 2017-05-19T18:37:48+00:00
We'll need more info to help...

- Please provide a screenshot.
- Platform you are using.
- Exact link to the file you downloaded.
- Clarification of details below.

> ...there are no words anywhere....
> I can highlight and copy paste the 25 words into a text document and see them there so things are working just not visible.

Sounds like you are having an issue specifically with generating a new 25 word seed then?
Are you saying you can select & copy the 25 words, but they are not visible until pasted elsewhere?

## Jaqueeee | 2017-05-23T10:32:52+00:00
This is a known issue with the linux 32-bit build. I have updated the buildbot build environment to fix this issue. Could you please try https://build.getmonero.org/downloads/monero-core-0093624-linux-i686.tar.gz 

btw, if you don't have a really good reason for running 32-bit linux, I recommend switching to a 64-bit distro. Will make your life easier. 

## dEBRUYNE-1 | 2017-08-07T17:29:09+00:00
+resolved

# Action History
- Created by: Justin435 | 2017-05-19T03:10:40+00:00
- Closed at: 2017-08-07T17:30:09+00:00
