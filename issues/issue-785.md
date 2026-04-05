---
title: Multi lang cli support
source_url: https://github.com/xmrig/xmrig/issues/785
author: snipeTR
assignees: []
labels:
- wontfix
created_at: '2018-10-08T19:57:44+00:00'
updated_at: '2018-11-05T14:25:42+00:00'
type: issue
status: closed
closed_at: '2018-11-05T14:25:42+00:00'
---

# Original Description
If the multi-language substructure is prepared for the CLI interface, it can be run in many languages.

# Discussion History
## xmrig | 2018-10-08T20:05:23+00:00
Probably never, CLI has a lot of issues related with encoding, for Linux it't might be ok, since UTF-8 wide supported, but Windows with different encoding used for cmd and other whole system all this may big headache on technical level.
Thank you.

## snipeTR | 2018-10-08T20:14:06+00:00
You don't need utf8 support :). ascii enough.

## xmrig | 2018-10-08T20:36:06+00:00
As I know all current Linux use UTF-8 locales, itself it's good, UTF-8 is best option we ever had, so Linux is not issue.
For Windows UTF-16/UCS-2 should used it require change mode for console window, but it should work. https://en.wikipedia.org/wiki/Unicode_in_Microsoft_Windows#UTF-8

ANSII is not an option, it code pages hell, Windows use DOS code pages for cmd https://en.wikipedia.org/wiki/Code_page#DOS_code_pages but different for GUI https://en.wikipedia.org/wiki/Code_page#Windows_code_pages


# Action History
- Created by: snipeTR | 2018-10-08T19:57:44+00:00
- Closed at: 2018-11-05T14:25:42+00:00
