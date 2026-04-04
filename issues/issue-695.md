---
title: Use transifex for translations
source_url: https://github.com/monero-project/monero-gui/issues/695
author: snaggen
assignees: []
labels:
- resolved
created_at: '2017-04-25T08:00:19+00:00'
updated_at: '2018-10-16T12:45:24+00:00'
type: issue
status: closed
closed_at: '2018-10-16T12:45:24+00:00'
---

# Original Description
I suggest moving translations to 
https://www.transifex.com/ since that would make things a lot easier for translators. Transifex is free for non-commercial open source projects, so I think Monero would fit that description. 

Here is some information on how to set it up
https://docs.transifex.com/integrations/github/ 


# Discussion History
## Jaqueeee | 2017-04-25T15:02:03+00:00
Good idea. I think we applied for a non-commercial account months ago. Any updates on this @fluffypony?

## jonathancross | 2017-06-06T00:30:42+00:00
Yes, this would be great (many translations are coming in, but translators are having trouble with git, merge conflicts, PRs, etc... there is no reason they should have to learn that stuff).

@fluffypony, any info about a Transifex account?

## snaggen | 2017-08-14T08:56:38+00:00
Is there anything we can do to get this to happen? I found the transifex monero page
https://www.transifex.com/monero-open-source-project/monero-gui/

The current github pullrequest based translation system is not really optimal for translations. 

## scottAnselmo | 2017-08-23T08:51:01+00:00
I whole heartedly agree. I'm going to try to follow up with fluffypony later this week since he seems to be the owner of that group on Transifex and try to start adding the initial base strings and then update the other languages to where they are presently. While it won't be useful for this upcoming release, hopefully it should help speed up translation work for the next release!

## scottAnselmo | 2017-09-03T22:20:22+00:00
FYI going off of conversation in IRC in #monero-community it looks like weblate might be used over Transifex although various options are still being explored at this point. If you want to help and contribute to the conversation I suggest parking an IRC session on #monero-translations.

## erciccione | 2017-09-16T14:32:04+00:00
We tried to set up a weblate instance but had many problems. We are now checking more alternatives, seems like a good one might be Pootle. Ongoing discussion at `#monero-translations`

## snaggen | 2018-10-16T11:33:21+00:00
What are the problems with weblate? I managed to get it "up and running" using their docker setup, and got as far as I could start doing translations on it. But that said, I wouldn't consider my test production ready, hence my question what the problems were for you?

## erciccione | 2018-10-16T11:54:22+00:00
This discussion was made one year ago, i honestly don't remember what was the problem with weblate. Anyway, we  already set up Pootle on translate.getmonero.org, it only needs to be tweaked and then we can start to use it for translations

## erciccione | 2018-10-16T12:40:34+00:00
+resolved

# Action History
- Created by: snaggen | 2017-04-25T08:00:19+00:00
- Closed at: 2018-10-16T12:45:24+00:00
