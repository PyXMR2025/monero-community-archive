---
title: Change default transaction priority and privacy
source_url: https://github.com/monero-project/monero-gui/issues/742
author: fresheneesz
assignees: []
labels:
- resolved
created_at: '2017-05-24T06:48:54+00:00'
updated_at: '2018-11-18T16:54:33+00:00'
type: issue
status: closed
closed_at: '2018-11-18T16:54:33+00:00'
---

# Original Description
I'd like to be able to change the default transaction priority and privacy. Would save me clicks. 

# Discussion History
## medusadigital | 2017-08-07T20:24:02+00:00
yes but it would also load up the whole user interface.

also it is unclear if in the future, only one certain ring size will be allowed (lets say 10)

therefore i would recmmend doing other thing instead.

however, leaving this open for other comments

## fresheneesz | 2017-08-07T21:28:01+00:00
> therefore i would recmmend doing other thing instead

What is "the other thing"?

And what do you mean it would "load up the whole user interface"? It would just be an option in the settings users would almost never see.

## medusadigital | 2017-08-08T14:21:47+00:00
the "other things" is the 116 other open tickets. 

regarding loading up the user Interface: even if this stuff is small, it takes up place. ofc we still have some space left in the settings page, but we also might need to add more checkboxes (like this one for example https://github.com/monero-project/monero-core/issues/720)


a worthy compromise could maybe be to make the application "remember" the last values of ringsize/fee.

so every time you launch up monero-core, it starts with the last used ringsize/fee settings. 8if you launch it the first time it has the current default values)

it would be possible to place those values in the settings file. we also store other stuff there, like last used wallet, etc. 

more opinions welcome 





## fresheneesz | 2017-08-08T18:50:10+00:00
Oh i see. Sure of course feel free to prioritize this appropriately. Not urgent. 

>  still have some space left in the settings page

This I don't understand. This is a digital interface. There is literally unlimited space on the settings page. 

> a worthy compromise could maybe be to make the application "remember" the last values of ringsize/fee.

I like that idea. I'd say that might be better/easier/more-intuitive than an option in the settings. 


## erciccione | 2018-11-18T13:37:11+00:00
+resolved

# Action History
- Created by: fresheneesz | 2017-05-24T06:48:54+00:00
- Closed at: 2018-11-18T16:54:33+00:00
