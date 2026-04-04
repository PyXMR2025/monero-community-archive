---
title: Design concepts for discussion
source_url: https://github.com/monero-project/monero-gui/issues/419
author: tficharmers
assignees: []
labels: []
created_at: '2017-01-18T19:21:36+00:00'
updated_at: '2017-12-11T12:30:38+00:00'
type: issue
status: closed
closed_at: '2017-12-11T12:30:38+00:00'
---

# Original Description
Hello. I raised a few issues back in November about consistency in design. I have been away since then, but have seen the beta release and played around with it a bit. Now I'm back and over the last weekend I put some thoughts together and whilst these are quite substantial changes for the current beta, I thought they might provide some food for thought and promote discussion for ideas for the future.

I'm not a Monero software developer so there may be impossible things. It also isn't extensive as there was no point in designing each screen/element for a concept.

[monero-gui-ideas-v1.pdf](https://github.com/monero-project/monero-core/files/714805/monero-gui-ideas-v1.pdf)

**Edit**
So I got bored and decided to implement some of the style updates into the current layout of the GUI. Again, this is purely for generating discussion and potentially some new ideas. I don't have time to write notes to these (off on my hols), but it should hopefully be self explanatory.

[monero-gui-ideas-v2.pdf](https://github.com/monero-project/monero-core/files/721259/monero-gui-ideas-v2.pdf)


# Discussion History
## ghost | 2017-01-19T05:14:47+00:00
This is great! Lots of great suggestions.

## ghost | 2017-01-23T17:57:15+00:00
@tficharmers Two suggestions for your design sheet. 1) To add handles to the privacy/priority sliders. It isn't immediately apparent to the user that they can be moved. 2). To add recent transactions on the same page as the "Check payment" tool, so people can automatically fill in the fields rather than tediously copy/pasting three items (address, tx id, tx key) from one page to another.

## ghost | 2017-01-23T18:48:29+00:00
Also the up and down arrows in transaction history could be colored red and green? What do you think?

## ghost | 2017-01-23T18:55:23+00:00
Also, try and integrate the full 12 places past the decimal point in your design. Certainly a balance of 128.0837 XMR looks nice. But how will the design look when the wallet has a balance of 128.083738275317 XMR?

## tficharmers | 2017-03-03T16:01:02+00:00
Hi @xmr-eric. Just to let you know that I've not forgotten about this. I've been away and busy and now looking forward to the beta 2. I'll see where that is up to and we can discuss whether it is worth me applying some design direction like I did above, or in a more direct manner (issues, PRs, coding, etc). Either way, I'm still available to help out cc: @Jaqueeee 

## jonathancross | 2017-06-03T23:33:10+00:00
Hi @tficharmers any updates for us?

## tficharmers | 2017-08-11T14:53:35+00:00
@jonathancross Sorry, completely missed this. I have spoken with the core devs again this week and planning to do more on this from now on. Watch this space I guess :)

# Action History
- Created by: tficharmers | 2017-01-18T19:21:36+00:00
- Closed at: 2017-12-11T12:30:38+00:00
