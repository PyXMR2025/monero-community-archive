---
title: '"Language: Italy"'
source_url: https://github.com/monero-project/monero-gui/issues/150
author: taushet
assignees: []
labels: []
created_at: '2016-11-10T22:14:03+00:00'
updated_at: '2016-11-13T17:57:31+00:00'
type: issue
status: closed
closed_at: '2016-11-13T17:57:31+00:00'
---

# Original Description
We are mixing adjectives and nouns! The horror!

We need to agree on either:

`Language: Italian`

or 

`Region: Italy`

I support the former (which is in keeping with conventions) and thus the list 'English (US)' vs 'English (UK)' vs 'Arabic (Palestine)' vs 'Norwegian (Bokmal)' vs 'Norwegian (Nynorsk)', etc., etc.

# Discussion History
## taushet | 2016-11-10T22:19:15+00:00
I can fix this, but will wait on the current PRs to be committed.


## dEBRUYNE-1 | 2016-11-10T22:49:23+00:00
See comments on #132.


## taushet | 2016-11-10T22:51:23+00:00
Agreed. So native language names then!


## ghost | 2016-11-11T07:37:01+00:00
Do we also need updates for the German translations?


## dEBRUYNE-1 | 2016-11-11T19:38:29+00:00
@maitscha Afaik, yes. 


## ghost | 2016-11-13T10:21:02+00:00
@dEBRUYNE-1 Is there a tool to update the existing translation file, or should I update it manually?


## dEBRUYNE-1 | 2016-11-13T12:49:51+00:00
You can regenerate the English file automatically as far as I know. From that you can easily translate the new strings manually. @Jaqueeee is probably able to explain how to exactly do this. 


## ghost | 2016-11-13T16:58:27+00:00
`lupdate monero-core.pro` did the trick ;)


## fluffypony | 2016-11-13T17:57:31+00:00
Closing as fixed


# Action History
- Created by: taushet | 2016-11-10T22:14:03+00:00
- Closed at: 2016-11-13T17:57:31+00:00
