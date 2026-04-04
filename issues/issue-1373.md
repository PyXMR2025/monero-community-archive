---
title: Better explain how to find a remote node
source_url: https://github.com/monero-project/monero-gui/issues/1373
author: GBKS
assignees: []
labels: []
created_at: '2018-05-06T12:44:53+00:00'
updated_at: '2018-05-07T09:23:15+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
![monero-wallet-settings-node-remote-2-gbks-180506](https://user-images.githubusercontent.com/695901/39673296-bedc0824-5139-11e8-8b78-7d25887de3c0.png)

Issue #1361 turned into a discussion about the setup of remote nodes being hard for new users. Ideally, users could just press a button and a remote node would be found for them. However, that would not be in the spirit of decentralization, since it would favor certain nodes.

My suggestion here is to better explain to users how to find a remote node. The current UI doesn't explain anything, it just shows a series of buttons and input fields. So users probably don't even know where to begin. A first step forward could be to tell people that they can find this information by searching online. Second, we can add a link to the tutorial about remote nodes on getmonero.org. It might be good then to revise that tutorial and make it as practical as possible (it should also not include any node addresses). The design above is simply an addition of a text paragraph that explains the two points. From my experience, a little bit of extra information can make a big difference in helping users understand things better.

This is totally open for discussions and ideas, I am just here to help find a solution that makes both sides of the argument happy.




# Discussion History
## erciccione | 2018-05-06T13:05:34+00:00
> The current UI doesn't explain anything, it just shows a series of buttons and input fields. So users probably don't even know where to begin 

Keep in mind that from next release there will be a guide for the GUI available for all users, which will be downloadable from the website and will be embedded with the binaries. Guide already available (still need some small fixes tho) here: https://github.com/monero-ecosystem/monero-GUI-guide

Btw i like this new design, but will we be able to implement it before next release? which should happen very soon? i would wait for the next one so we don't rush things

## GBKS | 2018-05-06T18:38:48+00:00
@erciccione thanks for the info, I didn't know about this new guide. Great work. Will the various "Help" buttons in the UI link to it? Or how will this be accessible for users?

The guide currently does not explain how to find a remote node (unless I missed it). Is that something that will be added?

There's no rush with this tweak, or the settings nav. I am just looking to start conversations around things that could be improved, with practical design proposals (which helps make decisions, estimate dev time, etc). Whether those get implemented or prioritized is fully up to the community and dev team.

## erciccione | 2018-05-07T09:23:15+00:00
>Will the various "Help" buttons in the UI link to it? Or how will this be accessible for users?

There are no links from the GUI to the guide at the moment, but the guide itself will be embedded with the binaries and probably downloadable from the website (i say probably because i proposed this only during the last dev meeting, but it shouldn't be a problem).

>The guide currently does not explain how to find a remote node (unless I missed it). Is that something that will be added?

There is explained how to make remote nodes work but not where to find some. I agree we should give some infos about that, will add. Thanks for your suggestions.

# Action History
- Created by: GBKS | 2018-05-06T12:44:53+00:00
