---
title: Can we talk about matrix.org ?
source_url: https://github.com/monero-project/meta/issues/1006
author: SyntheticBird45
assignees: []
labels: []
created_at: '2024-05-12T16:53:04+00:00'
updated_at: '2024-07-07T16:29:39+00:00'
type: issue
status: closed
closed_at: '2024-07-07T16:29:39+00:00'
---

# Original Description
We overall let people (and sometimes recommend) users to go over monero.social matrix instance.

Matrix.org has been delaying us since a little while now and it become unbearable sometimes:
- Discussion between monero.social, matrix.org and other instances quickly split because third-party instances can see messages of both but matrix.org users can't see messages from monero.social.
- Timeline is shuffled, with matrix.org messages from yesterday being brought in today's timeline. In meetings this can quickly become a clusterfuck.
- Direct messaging sometimes fail
- IRC relay is a monero.social users are therefore also delayed.

It's been at least a month we recommend at each meeting matrix.org users to follow on monerologs.net

Can we discuss a consensus on this ?
Defederate from matrix.org ?
Changing instance and praying for not being shadowbanned again ?

# Discussion History
## xmrscott | 2024-05-12T18:07:59+00:00
> Changing instance and praying for not being shadowbanned again ?

First and foremost, this issue is not a shadowban. Shadowban means it's intended. It's not; other reputable, long standing Matrix homeserver admins have also reported the issue both to New Vector Ltd and amongst themselves and found it to be an issue with how New Vector Ltd has set up their matrix.org Cloudflare Web Application Firewall. Further, messages can get through, but they can be delayed. Historically their infrastructure has had issues which is part of what led to their [provided LiberaChat bridge being shutdown](https://matrix.org/blog/2023/07/deportalling-libera-chat/) 

> Defederate from matrix.org ?

> Can we discuss a consensus on this ?

As of last week the homeservers experiencing the issue have escalated it to an entity above New Vector Ltd in an attempt to close out this issue.

Personally, I recommend other users switching to another homeserver besides Matrix.org. I don't think it makes sense to defederate from Matrix.org as messages can still get through nor does it make sense to use accounts on the homeserver causing the issue for multiple other homeservers

## Rucknium | 2024-05-21T21:53:31+00:00
> As of last week the homeservers experiencing the issue have escalated it to an entity above New Vector Ltd in an attempt to close out this issue.

Is there a public discussion thread of this? I want to track the progress.

## xmrscott | 2024-05-22T19:39:48+00:00
The closest thing to a public discussion I'm aware of is here: https://matrix.to/#/#foundation-office:matrix.org

## ghost | 2024-06-21T02:19:53+00:00
I know it doesn't offer as much privacy, but wouldn't using discord be a valid alternative since it's quite reliable, scales, is free & many people are familiar with it, plus it runs on most devices?

## xmrscott | 2024-07-06T16:57:39+00:00
Matrix.org has done some work behind the scenes and performance is now at an acceptable level based on my testing. Please close this issue @SyntheticBird45 if you too no longer encounter issues in the crosstalk between monerosocial and matrixorg.

## SyntheticBird45 | 2024-07-07T16:29:39+00:00
Yes. I felt these changes, everything is working smoothly now

# Action History
- Created by: SyntheticBird45 | 2024-05-12T16:53:04+00:00
- Closed at: 2024-07-07T16:29:39+00:00
