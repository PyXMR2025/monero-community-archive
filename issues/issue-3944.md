---
title: source contains PNG file with embedded non-free ICC profile
source_url: https://github.com/monero-project/monero/issues/3944
author: jonassmedegaard
assignees: []
labels: []
created_at: '2018-06-06T11:59:13+00:00'
updated_at: '2018-06-25T22:01:07+00:00'
type: issue
status: closed
closed_at: '2018-06-25T22:01:07+00:00'
---

# Original Description
Hi,

File contrib/snap/setup/gui/icon.png contains an embedded color calibration (ICC) profile which is copyright Hewlett Packard but lack license.

Please strip that ICC profile (since it is used to declare the sRGB colorspace which is commonly assumed by default for graphics files omitting any ICC profiles).

One way to examine metadata of embedded ICC profiles is by use of the commandline tool "exiftool", part of Perl module Image::ExifTool.

# Discussion History
## moneromooo-monero | 2018-06-06T13:38:53+00:00
If you know how to do that, a patch is welcome. 

## jonassmedegaard | 2018-06-06T14:18:44+00:00
This should work: `optipng -force -strip all contrib/snap/setup/gui/icon.png`.

Alternatively pngcrush should work too.

Sorry, I won't do a PR as a principle due to Github terms of service. I can put up a git clone elsewhere but guess it is far less work to run above command compared to fetching from a remote git.

## moneromooo-monero | 2018-06-06T14:20:04+00:00
OK, thanks. I have that tool in my distro's repo, I'll do that.

What terms of service in particular, out of curiosity ?


## moneromooo-monero | 2018-06-06T14:31:00+00:00
https://github.com/monero-project/monero/pull/3947

## jonassmedegaard | 2018-06-06T14:33:08+00:00
This (arguably only an ambiguity, but still chilling) is my reason for not doing PRs on Github: https://anarc.at/blog/2017-03-22-github-tos-update/

## moneromooo-monero | 2018-06-06T14:51:19+00:00
Thanks, informative.

## jonassmedegaard | 2018-06-08T07:05:00+00:00
Also, more generally, I believe Free softare needs Free tools (see https://mako.cc/writing/hill-free_tools.html and https://www.youtube.com/watch?v=U_nK6nP_RCY ) so keep my interactions with non-free tools to a limit.

## moneromooo-monero | 2018-06-25T21:57:17+00:00
+resolved

# Action History
- Created by: jonassmedegaard | 2018-06-06T11:59:13+00:00
- Closed at: 2018-06-25T22:01:07+00:00
