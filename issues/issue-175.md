---
title: 'Dev Meeting: February 25th, 2018, 16:00 UTC'
source_url: https://github.com/monero-project/meta/issues/175
author: rehrar
assignees: []
labels: []
created_at: '2018-02-14T05:31:17+00:00'
updated_at: '2018-03-05T22:09:11+00:00'
type: issue
status: closed
closed_at: '2018-03-05T22:09:11+00:00'
---

# Original Description
### Location
- [Freenode](https://webchat.freenode.net/) | [OFTC](https://webchat.oftc.net/) | [Slack](https://monero.slack.com/) | Irc2P | [Mattermost](https://mattermost.getmonero.org)
  - #monero-dev

### Time

Use the [timezone converter](https://www.timeanddate.com/worldclock/converter.html?iso=20180225T160000&p1=tz_gmt&p2=tz_et&p3=28&p4=111&p5=49&p6=179&p7=70&p8=224&p9=48) to see when the meeting is for you.

### Proposed Meeting Items
1. Greetings
2. Brief review of what's been completed since the previous meeting
3. March hardfork items + code freeze
4. Code + ticket discussion / Q & A
5. Hash changes & stance on ASIC miners
6. Any additional meeting items
7. Confirm next meeting date/time

*Notes:*
- Given that workgroups are starting to hold their own meetings, we will no longer be relaying between channels. Please make an effort to attend all meetings relevant to you.
- Meeting log will be posted to [https://getmonero.org/blog/tags/dev%20diaries](https://getmonero.org/blog/tags/dev%20diaries)

# Discussion History
## scottAnselmo | 2018-02-19T17:37:13+00:00
I would like to propose that [the ring size portion of issue 3035](https://github.com/monero-project/monero/issues/3035) is brought up in light of recent events (the hostile MoneroV chain split), namely increasing the default to 8-10 before our hard fork. 

As we've seen in the past with the optional, but default RingCT where roughly 99.98% stuck with the default people will likely use the default, but if they want to cut down on tx size (and consequently fees) and use the min ring size they can. Upping the default will better protect general users against hostile chain splits while still allowing for a presumably small set of users who are more concerned about tx cost than privacy to use the current min ring size. The change in code itself should be relatively trivial and nonimpactive to the codebase.

# Action History
- Created by: rehrar | 2018-02-14T05:31:17+00:00
- Closed at: 2018-03-05T22:09:11+00:00
