---
title: Undefined symbols on OpenBSD for monero-wallet-cli
source_url: https://github.com/monero-project/monero/issues/8596
author: yuuwe-n
assignees: []
labels: []
created_at: '2022-09-25T17:04:15+00:00'
updated_at: '2022-11-24T04:58:29+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Most symbols aren't rendered for the wallet cli. English is selected. Xterm is used. 

![image](https://user-images.githubusercontent.com/55438165/192155771-21adbbda-3af5-4304-86a3-f6880aad65ba.png)

Is this related to #7815? Am I missing some package for viewing different charsets?

# Discussion History
## yuuwe-n | 2022-09-25T17:13:18+00:00
Nevermind, I needed to set my locale(1)

## yuuwe-n | 2022-09-26T15:38:24+00:00
Even with my locale set, I am still having undefined symbols in some places. 

![image](https://user-images.githubusercontent.com/55438165/192319852-f1eb5385-ae7a-46e5-8b7b-5cf21258b818.png)
![image](https://user-images.githubusercontent.com/55438165/192319882-2af00856-21f9-481c-aa95-749b7cc76a97.png)

With the help command, everything is rendered correctly after the locale was set. I am not sure what I am missing

![image](https://user-images.githubusercontent.com/55438165/192320063-ed09cfd4-335f-4880-9e9a-f9c251da3dea.png)


## selsta | 2022-09-26T16:57:14+00:00
The PR you linked is for undefined symbols in regards to the linker, not literal symbols displayed on the display.

## offshoremonero | 2022-11-24T00:38:39+00:00
It has to do with GNU readline on OpenBSD's base being ancient. I think readline might have changed their licence at some point so the base version is stuck in the past.

There are two ways to fix this. You can turn readline off and compile it again. You will lose autocomplete in the wallet cli, but everything else works perfectly.

The second way to fix this (probably the best long-term fix) is to pkg_add readline and somehow fix the cmake stuff to link it correctly. I have investigated fixing this off and on over the last 2 years, but I don't have the time to track it down. I know it has to do with the package putting readline into /usr/local and calling the libs a different name.

Edit: my patch pasted horribly. I'll create a pull request.


## hyc | 2022-11-24T01:17:00+00:00
Last time I checked, BSD systems don't package readline. They ship libedit, with a "readline compatibility" wrapper that apparently isn't compatible enough. Make sure you're actually using the real readline library too.

## offshoremonero | 2022-11-24T01:37:10+00:00
Please excuse my ham-fisted stupidity. I grew up using CVS.

Please see pull request #8651 

## offshoremonero | 2022-11-24T04:58:29+00:00
> Last time I checked, BSD systems don't package readline. They ship libedit, with a "readline compatibility" wrapper that apparently isn't compatible enough. Make sure you're actually using the real readline library too.

I looked into this a bit more. OpenBSD ships the base operating system with both Readline and libedit.

Monero, by default, correctly links against /usr/lib/libreadline.so.4.0 but the above described issues occur.

OpenBSD ships with Readline version 4.3. OpenBSD refuses to ship their operating system with anything licensed with GPL 3.0. It's just how they do things.

Sadly, for now the best fix is to turn it off.

If I get something better working I'll open another pull  request later on.


# Action History
- Created by: yuuwe-n | 2022-09-25T17:04:15+00:00
