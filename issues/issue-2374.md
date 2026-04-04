---
title: 'Consider switching from Jekyll to Hugo '
source_url: https://github.com/monero-project/monero-site/issues/2374
author: plowsof
assignees: []
labels:
- 💬 discussion
created_at: '2024-09-26T19:57:29+00:00'
updated_at: '2024-10-29T21:10:37+00:00'
type: issue
status: closed
closed_at: '2024-10-29T21:10:37+00:00'
---

# Original Description
please read #2140 . this is a continuation of that issue.

# Discussion History
## rottenwheel | 2024-09-26T20:10:42+00:00
+1 change backend to Astro (personally prefer Hugo but whatever.) Can even keep current Jekyll theme, just be ported to Hugo, like we did for Revuo. Digilol can help with this. 

## rehrar | 2024-09-26T20:27:59+00:00
Copied from the previous Issue:

There have been several meetings in the Monero Website channels (IRC #monero-site, and the bridged Matrix room). In one of the meetings, and several discussion thereafter, the pros and cons of a new backend were discussed. I summarize them below:

Pros:

 1. The current stack is fragile, with comments from people who work on it such as "held together by duct tape" and "glued together cluster fuk".
 2. Building off of the above, Jekyll (in which the current site is coded) is ageing and not receiving many updates. It is written in Ruby, a language that is also declining from its heyday. This means fewer contributors in the case of custom code needed.
 3. Doing anything seemingly simple for a modern Static Site Generator (such as adding dark mode) requires custom plugins and work. Most modern SSGs have built-in functionality for things like this.
 4. None of the current maintainers enjoy working with Jekyll very much, or at the least are neutral to a backend change.

Cons:

1. Current site works. May not be pretty (design and/or backend), but it works.
2. We don't really plan to add a ton of features anyways, besides maybe dark mode, so all of this newfangled stuff may not be necessary.
3. Money and time will be needed to make the change. These resources could potentially be used better elsewhere?

This said, the framework that was decided upon in these meetings was Astro rather than Hugo, but that can be a different discussion. I am merely summarizing the arguments for and against a new backend at all.

## HardenedSteel | 2024-09-26T20:28:47+00:00
All the cons are pointing to same thing. It seems we eventually have to change the backend which means our choices are postpone or fix now.

## HardenedSteel | 2024-10-29T20:02:47+00:00
We're switching to Astro.

issue can be closed @plowsof 

# Action History
- Created by: plowsof | 2024-09-26T19:57:29+00:00
- Closed at: 2024-10-29T21:10:37+00:00
