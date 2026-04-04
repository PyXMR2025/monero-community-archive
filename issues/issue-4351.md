---
title: '[RYO Backport] Proper Unicode support on Windows'
source_url: https://github.com/monero-project/monero/issues/4351
author: fireice-uk
assignees: []
labels: []
created_at: '2018-09-09T11:49:00+00:00'
updated_at: '2018-10-06T19:00:52+00:00'
type: issue
status: closed
closed_at: '2018-10-06T19:00:52+00:00'
---

# Original Description
The approach that you took to read UCS2 glyphs from Windows command line doesn't work. Just try to create and restore a wallet with a Russian seed. The description of the problem is here https://github.com/ryo-currency/ryo-currency/pull/102 

Let me know if you want us to open source the fix.

# Discussion History
## moneromooo-monero | 2018-09-09T12:06:48+00:00
If it doesn't come with strings, sure. We've been waiting for a Windows coder to show up for ages.


## moneromooo-monero | 2018-09-09T15:32:39+00:00
BTW, I had a quick look at the repo you linked, and it looks like one of your contributors is PRing some of our patches with attribution removed. Very not nice at all:
https://github.com/ryo-currency/ryo-currency/commit/aac5f3b1ddfd0555034ff14cfe138d264ad8949b


## moneromooo-monero | 2018-09-09T15:37:29+00:00
Hmm, the patch is actually a bit different, though it does point to our patch. Hopefully most patches aren't that way.

## fireice-uk | 2018-09-09T19:33:57+00:00
> BTW, I had a quick look at the repo you linked, and it looks like one of your contributors is PRing some of our patches with attribution removed. Very not nice at all: ryo-currency/ryo-currency@aac5f3b

Would you like us to add the relevant person as a co-author next time? Cherry-picking between the project is actually impossible since we use different code styling rules.

## moneromooo-monero | 2018-09-09T20:19:59+00:00
I suppose it depends how much the patch is changed so it can get subjective. Just conflict resolution does not warrant stripping out authorship IMHO, though this particular patch does seem to have more changes than just conflict resolution so it's not a good example after all. I try to keep authorship when I can, but I know it's easy to let one slip from time to time, but in general, I'd try to keep it for patches mostly applied as is.


## psychocrypt | 2018-09-10T06:10:43+00:00
`ash on my main` I added each time the original pull request to the commit description but have not used the co-author feature. I will do it next time more clean, sry.

## moneromooo-monero | 2018-09-10T09:26:45+00:00
If you PR this, can you please put the line input in util directly (moved from simplewallet) ? It's useful for other bits.

## moneromooo-monero | 2018-10-06T18:20:58+00:00
+resolved

# Action History
- Created by: fireice-uk | 2018-09-09T11:49:00+00:00
- Closed at: 2018-10-06T19:00:52+00:00
