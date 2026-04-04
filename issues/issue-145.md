---
title: '[Minor design] Buttons inconsistent'
source_url: https://github.com/monero-project/monero-gui/issues/145
author: tficharmers
assignees: []
labels: []
created_at: '2016-11-10T15:54:27+00:00'
updated_at: '2017-12-11T12:30:17+00:00'
type: issue
status: closed
closed_at: '2017-12-11T12:30:17+00:00'
---

# Original Description
It looks like the form elements have a smaller font tracking (space between each letters). I guess this is probably due to the long Monero addresses. Anyway, it would be better to not have this on the form buttons as the text is quite compressed.

Another issue is the consistency in font size and capitalization. Should be more consistent IMO.

# Discussion History
## ghost | 2016-11-11T07:34:56+00:00
I think a minimal design guide would be practical, since there are various committers, having different ideas how the GUI should look like. I recommend to specify at least:
- Font size and color of the page header
- Page margin (the transfer and receive page have different margins)
- Button text uppercase vs. lowercase ("Generate" vs. "CHECK")
- Grouping of form elements (for example see the Sign/Verify page)
- Text size and color of major and minor input elements in the wizard

The New Wallet Setup wizard page has 6 paragraphs, each having a different font-size and font-decoration. This page feels at least for me very nervous.

Some more questions:
- What does the colored circles mean left to the menu item text?
- Why is the "Filter" button the only button colored different?
- Why is there a lock icon next to the balance?

Not a big issue for a alpha or beta release. Functionality is much more important.


## tficharmers | 2016-11-11T09:45:12+00:00
I agree with all that. I noticed more things but didn't want to swamp the Issues list. Yes, I agree these types of enhancements should be made to a later release.

I have experience creating style guides. I could put one together with some recommendations/critique of the current GUI design if people think that would be useful?

I suspect that also a User Guide would be useful in the future too. I can imagine a lot of questions from users and it would save time to just refer people to it than (re)answering queries.


## ghost | 2016-11-11T12:48:03+00:00
A design guide would be very valuable, should we ask a core dev?

One more thing to notice:

The labels of the inputs are placed sometimes left and sometimes above the input. I think it's much better to place them above the inputs, because:
1. There is more space for the labels, especially if it comes to localization.
2. The input can gain more space. Addresses and tx-ids need a lot of space.

my 2¢


## taushet | 2016-11-12T07:46:57+00:00
Just make the style guide as a new file in the root directory as a PR. A style guide would be a great and very welcome addition.


## Jaqueeee | 2016-11-12T11:47:16+00:00
A style guide would be very appreciated @tficharmers!


## jonathancross | 2017-06-03T23:37:03+00:00
Hi @tficharmers, any interest in getting the styleguide idea started?

Related: [Design concepts for discussion #419](/monero-project/monero-core/issues/419)

# Action History
- Created by: tficharmers | 2016-11-10T15:54:27+00:00
- Closed at: 2017-12-11T12:30:17+00:00
