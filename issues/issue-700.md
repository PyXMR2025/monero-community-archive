---
title: Moneropedia localization
source_url: https://github.com/monero-project/monero-site/issues/700
author: el00ruobuob
assignees: []
labels: []
created_at: '2018-04-22T16:55:35+00:00'
updated_at: '2018-08-25T05:19:49+00:00'
type: issue
status: closed
closed_at: '2018-08-25T05:19:49+00:00'
---

# Original Description
Hi everyone,

I wonder how Moneropedia works, so that i could work on the localization correctly.
First, i can see that links to moneropedia articles are done with \"\@article-name\" and shows as \"\@article name\". I'm i correct?
On each article, the Entry is the title (as shown in the index and article), and to me the terms seems to be what is looked up by the script to generate the links. I'm i correct?

So the terms should be always \"minus\", \"dash\" or `\"hippen\" joined? as in \"unlock-time\" for instance? I'm i correct?

Thanks for clarifications.

# Discussion History
## el00ruobuob | 2018-04-22T16:58:45+00:00
Any clues @rehrar and @erciccione ?

## el00ruobuob | 2018-04-22T17:06:25+00:00
And should we keep the original terms for upward compatibility? (i mean if a new guide is added, which refer to the term in english...)
So kinda \[\"translated-term-1\", \"translated-term-2\", \"original-term-1\", \"original-term-2\"\]

## erciccione | 2018-04-22T18:05:33+00:00
@el00ruobuob Avoid the translations of the moneropedia for now. We need to fix the script who manage that part, because all links in the new translations will result broken (and would be necessary to fix them one by one)

## el00ruobuob | 2018-04-22T18:28:49+00:00
Ok, i put it in standby for the moment.
However, when doing this script fix, please consider having apostrophes in the items, like in \"\@clef-d\'audit\" for \"\@view-key\"

## el00ruobuob | 2018-04-25T12:21:19+00:00
@erciccione May we help in anyway with the script update? Is it located within the repo?

Edit: found. Simply moneropedia.rb
So basically it is about getting the current language code and adding it to the href(s).

Edit2: Is it more about changing the links to "Permalinks and Translating Links" as explained in https://github.com/Anthony-Gaudino/jekyll-multiple-languages-plugin?

## erciccione | 2018-04-30T09:59:09+00:00
We still need to find a rubyst able to fix that

+bug
+localizations

## el00ruobuob | 2018-07-06T08:40:20+00:00
I'm not a rubyist, but after diving into the script, and thinking, rethinking, overthinking, i am testing something.
I do not say it will work for sure, but at least my new ruby script does not crash and site is building.

## el00ruobuob | 2018-07-06T09:30:56+00:00
first tests are satisfying...

## el00ruobuob | 2018-07-06T15:54:31+00:00
I respond to my OP:

- The terms **must** be hyphened, always
- The english terms **must** be kept before adding the localized terms

## el00ruobuob | 2018-07-06T15:55:04+00:00
to be put +improvement +in progress @erciccione 

## erciccione | 2018-07-10T13:25:12+00:00
Will review it and test it tomorrow or the day after. Thanks @el00ruobuob 

+in progress
+improvement

## el00ruobuob | 2018-08-25T05:18:51+00:00
This could be closed

## el00ruobuob | 2018-08-25T05:19:49+00:00
Fixed

# Action History
- Created by: el00ruobuob | 2018-04-22T16:55:35+00:00
- Closed at: 2018-08-25T05:19:49+00:00
