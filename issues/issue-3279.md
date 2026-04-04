---
title: 'Broken file: translations/monero.ts  from simplewallet.cpp'
source_url: https://github.com/monero-project/monero/issues/3279
author: ordtrogen
assignees: []
labels: []
created_at: '2018-02-16T21:09:38+00:00'
updated_at: '2018-03-05T22:56:35+00:00'
type: issue
status: closed
closed_at: '2018-03-05T22:56:35+00:00'
---

# Original Description
(I'm pasting a screen pic as I don't know how angle brackets and whatnot are handled in this edit field)

On rows 530 and 964, "<payment_id>" should be "&amp;lt;payment_id&amp;gt;", otherwise it breaks the XML. I have looked at the corresponding place in ../src/simplewallet/simplewallet.cpp and how this may have happened. 

![image](https://user-images.githubusercontent.com/15184875/36329235-8ee68e44-1365-11e8-8af7-987e75a50d0f.png)


# Discussion History
## iDunk5400 | 2018-02-16T21:31:32+00:00
#3275

## ordtrogen | 2018-02-17T09:30:55+00:00
Thanks, @iDunk5400 
I only checked if any issue had been reported and forgot to look for any PR in progress.

Will make a few comments to that PR and then close this issue

## moneromooo-monero | 2018-03-05T22:34:35+00:00
+resolved

# Action History
- Created by: ordtrogen | 2018-02-16T21:09:38+00:00
- Closed at: 2018-03-05T22:56:35+00:00
