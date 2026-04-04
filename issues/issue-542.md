---
title: Settings page could use a "Restore localhost" button
source_url: https://github.com/monero-project/monero-gui/issues/542
author: ghost
assignees: []
labels:
- resolved
created_at: '2017-03-07T02:05:27+00:00'
updated_at: '2018-11-18T18:36:32+00:00'
type: issue
status: closed
closed_at: '2018-11-18T18:36:32+00:00'
---

# Original Description
I just read a question by a user of the GUI. He had previously connected to a remote node, and was asking about how to restore his GUI settings so it would use his local node. Ideally, there should just be a button that does this automatically.

# Discussion History
## ghost | 2017-03-14T01:52:58+00:00
It could also say "Restore default". That might be clearer, perhaps.

## QuickBASIC | 2017-05-31T05:46:39+00:00
It probably would be clearer to have radio buttons to select Remote it Local and allow you to edit the text box only if you select Remote otherwise it uses the default. (Would a local node ever not be localhost with 18018 port?)

It would serve to delineate between using local data and remote data and show for a tooltip [?] that explains what a remote node is and the risks.

## jonathancross | 2017-06-08T20:59:04+00:00
I agree there is a lot of room for improvement here.
* For a local daemon, new users don't need to see "Startup flags", "IP address", port, username or password.
* "Startup flags", "Start daemon" and "Stop daemon" are not applicable to remote.
* "Connect" seems redundant for a local daemon (if you already clicked "Start" it should always connect automatically... well ideally)

I'm considering a few options, but 3 tabs might be good:
1. **Default:** New users should have a very clean interface with only local daemon start / stop option. All local daemon config should be assumed and hidden.  The tab can explain this default state rather than having confusing settings.
2. **Custom local:** More advanced users can customize their local daemon and would look similar to what we now have.  Need to think carefully about what is hidden vs editable here.
3. **Remote:** The final tab for connecting to remote daemon would not have "Startup flags", "Start daemon" and "Stop daemon" buttons.

I'll try to think about this a bit more and create some mock ups.

## ghost | 2017-06-08T21:08:12+00:00
@jonathancross I think @jaqueeee may have addressed this already. I saw something like it in a recent build screenshot someone posted. Jaquee can you confirm?

## Jaqueeee | 2017-06-09T04:37:09+00:00
Yes. I'm remodelling most of this in the remote nodes pr and in the lightwallet Integration I'm currently working on. 

## jonathancross | 2017-06-11T11:37:23+00:00
Great to hear!  I'll not bother with mocks then  :-)

## erciccione | 2018-11-18T13:10:56+00:00
+resolved

# Action History
- Created by: ghost | 2017-03-07T02:05:27+00:00
- Closed at: 2018-11-18T18:36:32+00:00
