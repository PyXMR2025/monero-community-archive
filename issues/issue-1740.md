---
title: '[FR] explain any disabled options '
source_url: https://github.com/monero-project/monero-gui/issues/1740
author: ITwrx
assignees: []
labels:
- resolved
created_at: '2018-11-16T15:37:18+00:00'
updated_at: '2018-11-28T16:27:44+00:00'
type: issue
status: closed
closed_at: '2018-11-28T16:18:31+00:00'
---

# Original Description
i'm trying to send some xmr with monero gui 0.13.04 in arch linux and the send button is greyed out. i don't see anything wrong that would prevent this send action: balance is unlocked, wallet and daemon are synchronized, log shows no problems, etc. 

problems happen, but not telling the user why an option is disabled is infuriating and i don't think the experience we want people to have.

it would be much better, if anytime any option is disabled, the reason why, in plain english, is disclosed right beside the disabled option, just like a typical web form. if the gui can make the button grey and stop the user from submitting, it can show a tooltip or error.

the wallet is already not intuitive enough, imho, but disabling stuff without explanation or quick remedy is probably a deal breaker for many people. you have to be able to trust that the thing will work (or at least work with you) when you go to transfer funds.
thanks

i see #67 now but i don't have any red fields and i don't think a hint with a red field is good enough (without an explanation right there in the gui) anyways.

update: also with log level at 4 no problems are shown in the terminal.

# Discussion History
## dEBRUYNE-1 | 2018-11-16T18:28:08+00:00
Are you trying to send an amount below 1? 

## ITwrx | 2018-11-16T18:28:51+00:00
yes, i was trying to send .013 as a test. sorry i forgot to mention this.

## dEBRUYNE-1 | 2018-11-16T18:37:58+00:00
All right, please see this then:

https://monero.stackexchange.com/questions/10545/unable-to-send-amount-below-one-x-in-mac-os-and-windows-os-gui/

## ITwrx | 2018-11-16T19:12:02+00:00
yes, that was the problem. thanks for your help with my specific issue. i'll leave this FR open until either the FR is implemented or monero devs decide to close it.

in this instance, if monero devs wanted to keep with the "highlighting of form fields" plan, then the amount field should have been red. i would add an error message shown by that field, or a tooltip with all criteria for the field.

update: what i like to do instead of having help/info/tooltip icons all over the place is to just make the names of the fields have titles that show when you hover over them. this keeps clutter down, but still makes things easy.


## dEBRUYNE-1 | 2018-11-27T20:05:30+00:00
@ITwrx - I think the issue with the `Amount` field is covered by #1749 & #1750. 

## ITwrx | 2018-11-27T20:09:41+00:00
@dEBRUYNE-1 yeah, that works too. thanks for the info.

## dEBRUYNE-1 | 2018-11-28T16:12:54+00:00
All right. Going to mark this as resolved then. 

## dEBRUYNE-1 | 2018-11-28T16:12:58+00:00
+resolved


## ITwrx | 2018-11-28T16:27:43+00:00
@dEBRUYNE-1 if this was a bug report for my specific issue then it would be resolved, but i submitted it as a feature request for a more general situation. namely, that the gui explain why any options/buttons are disabled in the event of illegal input or other issue. the fact that devs changed the gui to compensate for .xxx amounts doesn't change the fact that the gui still would not explain why it wouldn't accept a different, hypothetical "illegal" input. it just accepts another format of input now. my FR is that the gui explain itself if it's going to deny some input or block execution of the user's commands. To me this is a mandatory function of a gui to be considered user friendly. therefore, i think this FR is not resolved.
thanks 

# Action History
- Created by: ITwrx | 2018-11-16T15:37:18+00:00
- Closed at: 2018-11-28T16:18:31+00:00
