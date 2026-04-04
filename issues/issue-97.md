---
title: Monero dev meeting summary
source_url: https://github.com/monero-project/monero-site/issues/97
author: Gingeropolous
assignees: []
labels: []
created_at: '2016-01-31T22:16:49+00:00'
updated_at: '2016-02-10T11:45:11+00:00'
type: issue
status: closed
closed_at: '2016-02-10T11:45:11+00:00'
---

# Original Description
# Dev meeting summary by gingeropolous, 20160131
## Use of dev branch

First thing discussed is the dev branch. Contributors have fell back into the habbit of merging stuff to master. All hacking should be done onto dev branch.

Apparently this is because of bugs. A new point release to fix the v1/v2 stuck transaction bugs is coming.

The thing holding up general move to development branch is that CZMQ/0MQ hasn't been bundled in source, so its a pain to compile. Everyone agrees to bundle CZMQ/0MQ into dev branch. Fluffypony will get it in the source tree. 

There is more talk about minor tweaks that should or shouldn't go into the upcoming point release. 
## Style guide

In kovri they've been working with [a style guide](https://github.com/monero-project/kovri/blob/master/CONTRIBUTING.md#style), and fluffypony suggests implementing one in Monero. Basically, this is the way the code is formatted (human formatted). 

Its agreed to use the new style with new code, and restyle-as-you-go with old code. Restyling for the sake of restyling is though to be unnecessary. Key points:

> we assume from this point on the code is indented like the majority of the code so far - 2 spaces, not tabs, not 4 spaces.
> 
>  push harder on "code should go in a .cpp not .h"
## Collective Code Construction Contract (c4)

As used in 0MQ as [described here](http://rfc.zeromq.org/spec:22)

The idea is to merge every PR as long as it doesn't break the build. Aim is to avoid PR-hell where everyone comments on a PR for days and weeks and it never gets merged, because its never "perfect." Merge-everything is done so that contributors establish a history, and they can be banned if they are repeat offenders. 

In general, the idea is agreed upon. However, there is concern and uncertaintly regarding the roles of the various branches and how the contract applies to which branches. The conversation bleeds into ringCT implementation and timeframe and how the c4 would affect this process. The fact that 0MQ-dev branch is currently unusable is brought up regarding how the c4 would function. It is noted that 0MQ was pushed to dev because the original contributor couldn't continue working on it. Ultimately the 0MQ situation will not happen again.

Ultimately, this issue will be brought up at the next meeting. 
## Keep hacking around things or dump stuff for things that are easier

This is a lot of meta-code stuff. The thing that was salient to me was the doxygen-compatible approach, which would allow newcomers to the code to become acquainted more efficiently. 
## Thanks!

Fluffypony extends his gratitude to all contributors, and everyone makes their way to the reception hall for bacon wrapped shrimp, pigs in blankets, and all other sorts of tiny foods that hover on discs. 


# Discussion History
## fluffypony | 2016-02-10T11:45:11+00:00
Done, credited you as the post author: https://getmonero.org/2016/01/31/overview-and-logs-for-the-dev-meeting-held-on-2016-01-31.html


# Action History
- Created by: Gingeropolous | 2016-01-31T22:16:49+00:00
- Closed at: 2016-02-10T11:45:11+00:00
