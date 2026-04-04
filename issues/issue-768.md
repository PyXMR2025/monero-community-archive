---
title: Running monero gui 2 on tails does not display text
source_url: https://github.com/monero-project/monero-gui/issues/768
author: KushGoyal
assignees: []
labels:
- resolved
created_at: '2017-06-17T17:11:45+00:00'
updated_at: '2017-08-07T17:35:07+00:00'
type: issue
status: closed
closed_at: '2017-08-07T17:35:07+00:00'
---

# Original Description
On running monero gui 2 on tails the text is not displayed. To correct this I included this line in the start-gui.sh file.

```bash
export QT_QPA_FONTDIR=/usr/share/fonts/truetype/unifont/
```

Perhaps a specific font file can be included in the distribution files.

Another issue is that the gui screens are not scrollable. On my tails os screen I was not able to access the advanced option buttons on the send transaction screen.


# Discussion History
## jonathancross | 2017-06-18T15:29:07+00:00
Hi @KushGoyal can you please test and review #769 ?

## KushGoyal | 2017-06-19T16:15:06+00:00
@jonathancross sure. I will test this and reply back.

## Jaqueeee | 2017-06-19T16:31:33+00:00
The Linux32 builds from buildbot has working fonts in tails and whonix. Without any system env variables. Problem was that fluffypony didn't have fontconfig installed when he built QT and gui beta 2.

## dontbuymonero | 2017-06-19T17:54:21+00:00
Is Tails 3.0 being used? Was released 2 days ago I believe.

## Jaqueeee | 2017-06-19T20:42:53+00:00
We have tested 64 bit Linux gui on tails 3 beta without any issues iirc.

## jonathancross | 2017-06-21T20:01:38+00:00
> fluffypony didn't have fontconfig installed when he built QT and gui beta 

Thanks @Jaqueeee. Would it make sense to check for `fontconfig` in build.sh so builds don't have this issue in the future?

## Jaqueeee | 2017-06-24T21:33:52+00:00
@jonathancross: no, the issue appears when you've built Qt from source without fontconfig installed. Which was the case on the linux32 build machine used by buildbot and fluffy.

## dEBRUYNE-1 | 2017-08-07T17:30:10+00:00
+resolved

# Action History
- Created by: KushGoyal | 2017-06-17T17:11:45+00:00
- Closed at: 2017-08-07T17:35:07+00:00
