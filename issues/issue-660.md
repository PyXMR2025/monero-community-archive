---
title: GUI has become unusable since last update. Everything too large
source_url: https://github.com/monero-project/monero-gui/issues/660
author: t4777sd
assignees: []
labels:
- resolved
created_at: '2017-04-04T03:31:13+00:00'
updated_at: '2017-08-07T18:20:13+00:00'
type: issue
status: closed
closed_at: '2017-08-07T18:20:13+00:00'
---

# Original Description
Since the last release the GUI has become unusable on ubuntu. Everything is enlarged such as the software becomes useless. The left hand menu gets cut off the screen due to the enlarged. Attached is a screenshot
![monero](https://cloud.githubusercontent.com/assets/2925965/24640523/ee53cb5a-18cd-11e7-8c5d-f3be18e686c5.png)


# Discussion History
## medusadigital | 2017-04-04T11:01:20+00:00
hi,

does this build solve the issue ? 

https://build.getmonero.org/downloads/monero-core-0508442-linux-amd64.tar.gz

## t4777sd | 2017-04-04T18:06:41+00:00
Yes, that build resolves the issue. Is there any way to resolve the issue with the existing build (chanage config or something)?

## Jaqueeee | 2017-04-04T18:32:26+00:00
Good to hear. Yes, you should be able to set the QT_SCALE_FACTOR environment variable. 
i.e to make it half the size:
`QT_SCALE_FACTOR=0.5 ./start-gui.sh`

Please let us know if this works for you.



## amiuhle | 2017-04-04T20:12:43+00:00
Related: https://github.com/monero-project/monero-core/issues/343#issuecomment-285881929

Running the Beta 2 with a scale factor of 0.6 works best for me, @medusadigital's build is too small (tiny, as was Beta 1). Both solve the missing bullets when entering a password.

## medusadigital | 2017-04-05T10:23:15+00:00
thanks a lot for your feedback guys ! 

## t4777sd | 2017-04-06T22:51:28+00:00
The QT_SCALE_FACTOR made existing builds usable. However the build provided by medusadigital was the best looking

## Jaqueeee | 2017-05-03T14:14:44+00:00
fixed in #647 

## dEBRUYNE-1 | 2017-08-07T18:02:46+00:00
+resolved

# Action History
- Created by: t4777sd | 2017-04-04T03:31:13+00:00
- Closed at: 2017-08-07T18:20:13+00:00
