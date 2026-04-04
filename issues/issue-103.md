---
title: 'User and label list for Label-bot access on monero-site repo '
source_url: https://github.com/monero-project/meta/issues/103
author: danrmiller
assignees: []
labels: []
created_at: '2017-08-07T16:24:21+00:00'
updated_at: '2023-12-18T14:35:04+00:00'
type: issue
status: closed
closed_at: '2023-12-18T14:35:04+00:00'
---

# Original Description
Which labels need to be used for the monero-site repo?

Which users should be allowed to label and close issues?


# Discussion History
## anonimal | 2017-09-23T21:07:55+00:00
Does [this list](https://github.com/monero-project/meta/issues/62#issuecomment-313512337) still apply? If so, should we PR the list for easy reference?

## anonimal | 2017-09-23T21:15:43+00:00
Opened https://github.com/monero-project/meta/issues/119.

## QuickBASIC | 2017-09-26T19:05:58+00:00
>Which labels need to be used for the monero-site repo?

@danrmiller 

```
bug
feature
improvement
question
critical
important
low priority
in progress
resolved
duplicate
wontfix

merchant
merchant removal
guide
blog
moneropedia
wrong repo
grammar
discussion
stale
```
* see: monero-project/monero-site#401 for example of something we `wontfix`, (identified scam site) so maintainer can identify and close these.
* `merchant`s currently open 1 issue per request. It would be helpful so they could be identified quickly
* Some users are comfortable creating `guide`s, but don't know how to add them to the user guide landing page (It's mostly HTML and kind of intimidating for new users). This would enable a contributor to identify guides that can be created and imported into the site. This also can be used requests for guides to be written.
* Many users will open an issue for `merchant removal` (see monero-project/monero-site#283) generally we want to leave these open for a time so that others can comment on whether or not they agree with the assessment of the merchant being scammy before we remove it and we can mention the merchant if they're on github, so they can comment.
* Many `blog` posts and missives notes and transcriptions get dumped into issues until someone makes them a blog post. (see monero-project/monero-site#17)
* The `moneropedia` is still relatively sparse, many users make requests to create a moneropedia entry (see monero-project/monero-site#106). Contributors that feel equipped to can identify missing entries and write them.
* As big as the monero-project is many users open issues in the `wrong repo` (see monero-project/monero-site#109) and should probably should be closed immediately.
* Many users open issues to report `grammar` or spelling issues (see monero-project/monero-site#349 (these are probably going to be similar to `easy` on `monero-project/monero` repo.
* Sometimes there needs to be `discussion` on certain things that are being written for consistency and it's not always expedient for contributors to make a PR and they discuss the ramifications of the changes. (see monero-project/monero-site#165).

EDIT: adding one more 

* `stale` - sometimes users open vague issues and don't reply to contributor's queries or merchants don't provide enough info to add their site and don't reply, we can always reopen these if they come back but I don't think it beneficial to keep them open indefinitely. Our general policy for closing PRs that aren't rebased or edits that aren't made to PRs is 30 days and we should probably do the same for issues (obviously keeping open anything that will be fixed even older than that though) see monero-project/monero-site#346


## danrmiller | 2017-10-11T17:37:33+00:00
@anonimal wrote:
> Does [this list](https://github.com/monero-project/meta/issues/62#issuecomment-313512337) still apply? If so, should we PR the list for easy reference?

The list will always be the labels existing for the repo, in this case https://github.com/monero-project/monero-site/labels

@QuickBASIC Since there were no other comments, I will configure the labelbot to start checking the monero-site repo and get the labels you requested setup.



## QuickBASIC | 2017-10-11T18:15:48+00:00
@danrmiller 

Awesome. Thank you. Do you know who is or is going to be tagged for permission to use the labels on the monero-site repo?

## danrmiller | 2017-10-11T18:38:42+00:00
Oh good point. I won't activate the label bot for the monero-site repo until we know who will have permissions to tag and close issues.

## danrmiller | 2017-10-11T18:39:16+00:00
Also, I am going to use "invalid" instead of "wrong repo" for consistency with the other projects.

## QuickBASIC | 2017-10-11T19:19:01+00:00
> Also, I am going to use "invalid" instead of "wrong repo" for consistency with the other projects.

Roger, makes sense... Not a developer, so I didn't know what ones were being used on the other repos.

> Oh good point. I won't activate the label bot for the monero-site repo until we know who will have permissions to tag and close issues.

I don't know who everyone is, but the most active contributors over the last several months from what I see are:
@rehrar (4 PRs merged+ site redesign so it's a given he'd be included)
@bigreddmachine (6 PRs merged)
@dEBRUYNE-1 (20 PRs merged + he posts the meetings, so it's probably a given he'd be included.)
@SamsungGalaxyPlayer (10 PRs merged)
@mattcode55 (12 PRs merged)
@erciccione (5 PRs merged)
@QuickBASIC (10 PRs merged)
@anonimal (10 PRs merged)
@MaxXor (2 PRs merged, but is active in reviewing other PRs and posting comments in issues)
@tyrionmcmaster (6 PRs merged) 
@qertoip (6 PRs merged)
@jonathancross (5 PRs merged)

I'm sure there are better metrics than merged PRs, but these are all people that are active in maintaining the site and comment on issues and review PRs, that I've seen. Obviously should include core developers, etc. If I've excluded anyone, it's certainly not on purpose, these are just my observations.

Special mention: @erciccione and @mattcode55 are always some of the first to answer issues on the monero-site repo or review PRs. I wouldn't mind being included as well.

I'm not certain that I'd expect whole list to have access to the label-bot, but I believe most of these people would be interested in that discussion, so I've tagged them.

## rehrar | 2017-10-11T21:14:56+00:00
Yeah, I'd be down if community agrees. 

## erciccione | 2017-10-12T10:10:50+00:00
Thanks for the mention @QuickBASIC , happy to do it if needed

## jonathancross | 2017-10-12T18:45:21+00:00
ACK

## QuickBASIC | 2017-10-18T14:33:59+00:00
@danrmiller 

It's been 7 days since I tagged the most frequent contributors to the monero-site repo and also created an issue there to link to this discussion. Since there doesn't seem to be anyone adding any further information or acknowledging the mentions, I propose we move forward by assigning permission to those who have acknowledged interest (and any core contributors you feel is appropriate) and activate the label bot.

@rehrar 
@erciccione 
@jonathancross 
@mattcode55
@QuickBASIC

## danrmiller | 2017-10-20T22:13:59+00:00
Done. I don't follow the -site repo so let me know here or on irc (pigeons) if it doesn't work.

## QuickBASIC | 2017-10-21T00:20:05+00:00
Awesome. Thank you. Tried to label monero-project/monero-site#441 doesn't seem to be working atm.

## erciccione | 2017-10-21T15:27:20+00:00
same for me monero-project/monero-site#449

## danrmiller | 2017-10-21T21:05:33+00:00
OK, I need to handle temporary 412 errors from gitlab api, should be fine for now

## mattcode55 | 2017-10-21T21:38:40+00:00
For something like monero-project/monero-site#401, should `+wontfix` close the issue?

## QuickBASIC | 2017-10-21T21:44:49+00:00
I'm also wondering if `stale` should close an issue too since it's not `resolved` nor `wontfix`. We probably don't want to keep those issues open forever if the OP isn't responding or providing needed information.

## mattcode55 | 2017-12-20T17:29:47+00:00
Ping @danrmiller 

## danrmiller | 2017-12-21T01:01:10+00:00
wontfix and stale will now close the issue. Let me know if there is anything else.

## erciccione | 2018-02-28T14:48:44+00:00
Now that the website is multilingual, would be good to have a `Localizations` label . Can you add it @danrmiller ?

## danrmiller | 2018-02-28T15:49:44+00:00
The ```localizations``` label has been added to monero-site.

## jonathancross | 2018-03-01T17:33:31+00:00
@danrmiller Thanks for setting this up!  I tested and works well.
Is this going to be setup for `monero-gui` repo as well?  Would be very useful there.

## erciccione | 2018-03-01T19:56:02+00:00
At this point, also for `monero` :)

## QuickBASIC | 2018-03-04T10:31:05+00:00
@danrmiller 

Sir, when you get a chance can you look at monero-project/monero-site#635 and monero-project/monero-site#636. The bot doesn't seem to be closing the issues for wontfix or resolved.

## mattcode55 | 2018-03-04T10:34:55+00:00
It doesn't close issues tagged with `+invalid` either

## jonathancross | 2018-03-04T17:38:19+00:00
**Edit:** Seems to be a user-specific problem.  I can open and close using `wontfix`, but some others cannot.
This one for example (https://github.com/monero-project/monero-site/issues/635) could not be closed by @QuickBASIC or by @mattcode55, but worked fine for me.


## plowsof | 2023-12-18T06:32:47+00:00
can this be closed as completed @erciccione?

## erciccione | 2023-12-18T11:18:24+00:00
@plowsof yeah definitley. The label bot doesn't even exist anymore iirc.

# Action History
- Created by: danrmiller | 2017-08-07T16:24:21+00:00
- Closed at: 2023-12-18T14:35:04+00:00
