---
title: Decentralize Community Development
source_url: https://github.com/monero-project/meta/issues/237
author: anonimal
assignees: []
labels: []
created_at: '2018-06-06T06:30:37+00:00'
updated_at: '2018-06-06T20:22:03+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The workgroups are becoming too centralized. The infrastructure continues to be built entirely upon Monero Project core team resources. We've reached a point where one has to essentially "ask permission" in order to join a project on taiga.getmonero.org. These are huge red flags.

I'm not suggesting that the project remove getmonero.org services. I'm suggesting that the community continue to build-out our infrastructure so we A) don't over-burden the core team B) don't allow regular contributors to have decision making influence over other contributors C) keep things decentralized.

Essentially, we need more of what we already have. More buildbots/CI, more GitLabs (#236), more Taigas, more outreach from people with differing views of the project and codebase, more decentralization.

# Discussion History
## fluffypony | 2018-06-06T06:36:09+00:00
The whole point of workgroups is that they’re self-assembling. If someone doesn’t like the way the malware response workgroup is responding, or the way Kovri is being developed, they shouldn’t try join in, they should start their own project on Taiga and present an alternative to the community at large.

Self-assembling workgroups have every right to be as open or as closed as they want to be, and I don’t see value in trying to force my idea of how it should work on a particular group or groups.

## anonimal | 2018-06-06T07:18:06+00:00
>Self-assembling workgroups have every right to be as open or as closed as they want to be, and I don’t see value in trying to force my idea of how it should work on a particular group or groups.

But, ironically, you just enforced your idea of how it should work :smile: 

Also, A) that solution is overkill for something as simple as a minor kanban correction and B) this doesn't solve the fact that taiga is under the control of a single entity who can silence on a whim.

This is why we need more of everything.

## rehrar | 2018-06-06T15:10:55+00:00
What do you mean by "ask permission in order to join a project". There was indeed a bug with Taiga recently that didn't allow new user sign up, but pigeons pulled in a fix, and now anyone can sign up again. 

As to the individual projects, you have to ask the leader of that project to send you an invite to that project. If this is your meaning (that asking a leader of a workgroup to join the workgroup rather than a natural flow in and out of a workgroup without permission), then I don't disagree. 

Of course, anyone is able to spin up a VPS and host their own Taiga, Pootle, or anything else. 

In fact, the PR, O&E workgroup is doing just that. They are using Taiga, but decided they needed collab on documents and file sharing stuff. Rather than use Google Drive, and rather than asking the core team to do it for them, they decided to self-host a NextCloud instance themselves. It's up and running, and they're happily using it.

So, you are correct in a senses and we can even encourage people to create and host their own resources, but the core team ones are there to encourage naturally forming groups with minimal headache needed to get started. From there, they can indeed Branch out on their own and host other resources as need be. 

## anonimal | 2018-06-06T20:22:03+00:00
@rehrar You've completed side-stepped addressing the issue of project centralization while reiterating what I've already said. What a waste of time to read.

>There was indeed a bug with Taiga recently that didn't allow new user sign up, but pigeons pulled in a fix, and now anyone can sign up again.

Not sign-up, project permissions.

>Rather than use Google Drive, and rather than asking the core team to do it for them, they decided to self-host a NextCloud instance themselves.

https://yourlogicalfallacyis.com/anecdotal

@fluffypony hasn't hosted nextcloud for a reason. Even if asked, he wouldn't host nextcloud because doing so opens up at least several new attack vectors unseen in every other service. For example, hosted files on nextcloud are private by default and anyone with an account can upload illegal content. He nor anyone else here has the time to police file uploads. Even if no one uploads illegal content, a warrant issued on suspicion is enough to at least take down the server temporarily.

>So, you are correct in a senses and we can even encourage people to create and host their own resources, but the core team ones are there to encourage naturally forming groups with minimal headache needed to get started. 

Get started, ...within the confines of a centralized project that enforces "the idea of how it should work on a particular group or groups".

https://yourlogicalfallacyis.com/middle-ground

>But, ironically, you just enforced your idea of how it should work

I understand why you are both championing project centralization but if Monero Project were true stewards of decentralization, they wouldn't be running our existing infrastructure as it is today. Ideally, they wouldn't host anything but a website on getmonero.org. On this website would be various tutorials (or links to tutorials) on how anyone can create their own buildbot/taiga/mattermost/nextcloud/repro builds etc. and how to interconnect with other instances. As of now, this is not the case and, symptomatically, groups are using the getmonero brand to create an official centralized presence of something that is supposedly decentralized and unofficial.

More than 50% of project infrastructure is owned by a single person / entity. This is dangerous but not nearly as dangerous as the fact that we don't have other solutions in place.

Solutions aren't easy! This issue is tricky to solve but is also the perfect opportunity for innovation.

# Action History
- Created by: anonimal | 2018-06-06T06:30:37+00:00
