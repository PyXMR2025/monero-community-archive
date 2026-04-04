---
title: '[FEATURE REQUEST] User Help via Tiptext'
source_url: https://github.com/monero-project/monero-gui/issues/684
author: medusadigital
assignees: []
labels:
- feature
- in progress
- resolved
created_at: '2017-04-18T10:30:53+00:00'
updated_at: '2018-11-18T13:36:27+00:00'
type: issue
status: closed
closed_at: '2018-11-18T13:36:27+00:00'
---

# Original Description
Every application needs some help for new users. The idea isnt really to explain to the user how cryptocurrencies work in general, but to shed some additional light in some of the most confusing parts of Monero. This is probabaly the PaymentId, Integrated Address, Unlock Time, Smart Mining and so forth. 

personally i am in favour of using classical Tiptext to display this additional Information. not only its convenient but the implementation of tiptext could help also solve other issues without overloading the layout (for example https://github.com/monero-project/monero-core/issues/142)

This issue should be the placeholder for all this work and related discussion. 

some points worth talking about (and there are sure more) :

- should it be possible to activate/deavtivate the help ?
- is tiptext the right choice to do this ?

+feature

# Discussion History
## ghost | 2017-04-18T20:15:09+00:00
Also a fan of tiptext. And I think I've seen some initial implementations of it in the code.

## jonathancross | 2017-04-24T00:11:48+00:00
In some views (like the **Receive** tab) there is an orange "help" link that opens a modal.
This should be factored into the decision... do we want 2 systems for help text?

The current modal works well for larger amounts of text and keeps the UI fairly clean otherwise, but breaks the user out of current activity with this jarring modal which is awkward.


## fresheneesz | 2017-05-24T04:49:35+00:00
Also need a tooltip for "Sign tx file" - what is a "transaction file" ? Is it just signing any file with your wallet or does it have to be some file in a valid "transaction file" format?

Also "Unlocked Balance". Shouldn't you be able to spend sent money whenever you want no matter how many confirmations it has? 

## medusadigital | 2017-08-07T19:31:42+00:00
+feature
+in progress

might probably still not make it for next release 


## erciccione | 2018-11-18T13:32:18+00:00
We now have some tiptexts in the new theme, some new shall be added in future. If still valid, please reopen @medusadigital 

+resolved

# Action History
- Created by: medusadigital | 2017-04-18T10:30:53+00:00
- Closed at: 2018-11-18T13:36:27+00:00
