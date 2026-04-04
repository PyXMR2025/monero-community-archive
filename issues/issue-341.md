---
title: GUI password strength meter turns green but meter not moved to "high" when
  pasting long password
source_url: https://github.com/monero-project/monero-gui/issues/341
author: taky2
assignees: []
labels:
- resolved
created_at: '2016-12-22T19:55:32+00:00'
updated_at: '2017-08-07T19:00:15+00:00'
type: issue
status: closed
closed_at: '2017-08-07T19:00:15+00:00'
---

# Original Description
There seems to be some character threshold here where when pasting in a long password the strength meter does not move, but it turns green. 

After some testing I have discovered that anything over 18 characters the bar/meter will turn green but not move to the full position (when pasting a new password on the creation screen) 

Here is a picture:
![image](https://cloud.githubusercontent.com/assets/7447137/21438391/d88b6ab8-c845-11e6-93d4-0bb957507f8e.png)

(I am using the mac version)





# Discussion History
## moneromooo-monero | 2016-12-22T20:11:39+00:00
If you type more, does it never move ?

## taky2 | 2016-12-22T23:16:43+00:00
**Typing more characters does not move the bar, but deleting characters until you are at or below the threshold will update the bar correctly.**

Revisiting this, I am having some issues with consistency testing it. 

Under specific circumstances this bug is occurring: 

There actually seems like there might be some variance. Pasting 19 or 20 characters (only letters and numbers) will currently update the strength meter correctly.

22 characters the issue still exists.
21 characters the strength bar updates correctly when pasting.

With 22 characters typing additional characters does not update the status bar. Deleting 1 character WILL update it. It appears this is an issue for any number of character greater than 21, while 21 or less characters works fine. 

The OP (bug report) refers to passwords with special characters. As I am testing this, I am realizing that when symbols are involved, the bug occurs with at a lower character threshold. This threshold might have some variance depending on the special characters involved, (specifically the quantity). 

Testing right now with 3 special characters appears to be reliably working with 20 or less characters. It appears this threshold is directly proportional to the quantity of special characters used in the password. 

Currently when using a password over 20 characters (including 3 symbols) adding additional characters will not move the strength meter. When deleting characters it will not move until there are 20 characters or less. Furthermore, if there are less than 20 characters and characters are added (by typing) it will update the meter bar. 

## moneromooo-monero | 2016-12-23T13:47:39+00:00
Since you're mentioning length of the password a lot, beware that if you type aaaaaaaaaaaaaaaaaaa, the strength of the password will not increase much at all even if you type 200 a, since crackers will try repeated things.

## medusadigital | 2016-12-23T15:26:47+00:00
sounds similar: https://www.reddit.com/r/Monero/comments/5jr7r4/monero_core_gui_beta_1_released/dbjojiv/

## taky2 | 2016-12-23T15:53:26+00:00
I am using a randomized password generator. I am not testing with intentional consecutive characters.

## moneromooo-monero | 2016-12-25T23:00:08+00:00
Thanks for the report, fixed in https://github.com/monero-project/monero-core/pull/359

## ghost | 2017-03-29T03:47:31+00:00
@taky2 Can this issue be closed?

## taky2 | 2017-03-29T04:21:43+00:00
@xmr-eric not sure, I only see the original beta for download still, hence I haven't been doing any further testing. I see something released 10 hrs ago, but it looks like it needs to be built from source.

## medusadigital | 2017-04-18T09:31:06+00:00
GUI beta 2 is out with fix included.

this Issue can be closed

## dEBRUYNE-1 | 2017-08-07T17:44:11+00:00
+resolved

# Action History
- Created by: taky2 | 2016-12-22T19:55:32+00:00
- Closed at: 2017-08-07T19:00:15+00:00
