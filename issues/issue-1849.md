---
title: Easy to paste only the first words of a seed when restoring
source_url: https://github.com/monero-project/monero/issues/1849
author: moneromooo-monero
assignees: []
labels: []
created_at: '2017-03-06T10:49:21+00:00'
updated_at: '2017-06-27T09:00:25+00:00'
type: issue
status: closed
closed_at: '2017-06-27T09:00:25+00:00'
---

# Original Description
Since the wallet displays the seed as three lines, people tend to paste the three lines when restoring, causing the wallet to parse only a third of the seed.
Either mention it needs to be on one line, or (since poeple won't read) continue parsing till we have 24 or 25 words.

# Discussion History
## ghost | 2017-03-08T18:37:48+00:00
Related to #1170 ?

## moneromooo-monero | 2017-03-08T20:53:43+00:00
No. That is a terminal bug editing a line.

## moneromooo-monero | 2017-04-16T10:57:18+00:00
https://github.com/monero-project/monero/pull/1984

## binaryFate | 2017-06-25T19:20:48+00:00
Why is it still open if fix is merged?

## moneromooo-monero | 2017-06-27T09:00:25+00:00
True. I'm not used to being the one filing a bug :)

# Action History
- Created by: moneromooo-monero | 2017-03-06T10:49:21+00:00
- Closed at: 2017-06-27T09:00:25+00:00
