---
title: Labeling Bot
source_url: https://github.com/monero-project/meta/issues/62
author: medusadigital
assignees: []
labels:
- task
- in progress
created_at: '2017-04-18T09:09:20+00:00'
updated_at: '2020-03-09T21:45:44+00:00'
type: issue
status: closed
closed_at: '2020-03-09T21:45:43+00:00'
---

# Original Description
The Monero Core Team does not have time to lable the Issues (especially in monero-core Repo).

This increases workload for everybody and with rising complexity, neees to be changed in my view. Labeling and Filteing Issues is a powerfull tool which will help support planing and at the same time increases transparency. 


The idea has been coming up during discussions on how to enable certain people to label issues, but withiout giving them full repo access. since github does not support selective permissioning, the idea of a labeling bot came up. 

the bot could ideally be controlled via IRC or similar. 




# Discussion History
## danrmiller | 2017-07-06T20:37:24+00:00
@medusadigital , the bot will label the issue in this "meta" repository if you make a comment in this form:

```
@issue-helper label:NAME_OF_LABEL
```

These are the currently supported labels:

bug
feature
improvement
question
task
blocker
critical
important
low_priority
in_progress
resolved

To start testing you and I are the authorized users the bot will listen to.

## danrmiller | 2017-07-06T20:37:54+00:00
@issue-helper label:in_progress

## medusadigital | 2017-07-06T20:58:16+00:00
@issue-helper label:improvement

## anonimal | 2017-07-10T21:14:10+00:00
@danrmiller can you please add `proposal` https://github.com/monero-project/meta/issues/81#issuecomment-314244961 and give me authorization?

## danrmiller | 2017-07-10T21:42:26+00:00
Thanks anonimal. Will roll this out shortly with the unlabelling and issue closing additions.

## anonimal | 2017-07-10T21:46:53+00:00
Awesome, thanks 😄 

## danrmiller | 2017-07-22T00:01:30+00:00
I've switched to using https://github.com/aljungberg/cappbot which has our required features of access control lists, labeling, unlabeling, closing and re-opening issues via comments.

You no longer need to ping the @issue-helper. To add or remove a label, preface the label name with + or - on a line all by itself.
To close an issue, add the resolved or duplicate label. To re-open a closed issue, remove the resolved or duplicate tag.

For example:

+task

-in_progress

+in progress

Label Changes: By request, "proposal" and "duplicate" and "invalid" have been added,
low_priority and in_progress have been changed to "low priority" and "in progress".

The current list of labels, to be determined in https://github.com/monero-project/meta/issues/90


```
bug
feature
question
task
blocker
critical
important
low priority
in progress
resolved
proposal
duplicate
invalid
```

Please excuse this spam below so I can use the legacy bot to create the labels needed. The new bot will not add a label that doesn't already exist.


@issue-helper label:feature
@issue-helper label:blocker
@issue-helper label:critical
@issue-helper label:important
@issue-helper label:low priority
@issue-helper label:in progress
@issue-helper label:resolved

## danrmiller | 2017-07-22T00:08:25+00:00
-bug
-feature
-improvement
-question
task
-blocker
-critical
-important
-low priority
in progress
-resolved
-proposal

## selsta | 2020-03-09T21:45:43+00:00
Labeling bot has been replaced by Github triage user role.

# Action History
- Created by: medusadigital | 2017-04-18T09:09:20+00:00
- Closed at: 2020-03-09T21:45:43+00:00
