---
title: No message when seed is not valid in Recovery wizard
source_url: https://github.com/monero-project/monero-gui/issues/331
author: ClementJnc
assignees: []
labels:
- resolved
created_at: '2016-12-22T12:18:25+00:00'
updated_at: '2017-12-13T13:00:20+00:00'
type: issue
status: closed
closed_at: '2017-12-13T13:00:20+00:00'
---

# Original Description
If I enter an invalid sequence of 25 words in the Recovery wizard, there is no message indicating that I need to correct the sequence.

# Discussion History
## Jaqueeee | 2016-12-22T20:48:17+00:00
Additional info: GUI hangs on mac when trying to move forward with invalid seed #339

## dternyak | 2016-12-22T20:50:24+00:00
@Jaqueeee Sorry, shouldn't have used the term 'hangs'. It simply does nothing when you click continue, you can still back out / try a different mnemonic. 

## Jaqueeee | 2016-12-22T20:51:33+00:00
OK. Thanks for clarification!

## ghost | 2016-12-23T00:23:10+00:00
What do you mean by 'invalid'? Do you mean words that aren't in the standard seed word dictionary, or it's a sequence with the wrong final word checksum, or it's a sequence that isn't your key but is still a valid selection of words?

## medusadigital | 2017-08-07T21:20:56+00:00
can we close this ? 

## dEBRUYNE-1 | 2017-12-13T11:00:30+00:00
+resolved

# Action History
- Created by: ClementJnc | 2016-12-22T12:18:25+00:00
- Closed at: 2017-12-13T13:00:20+00:00
