---
title: 'Major GUI Redesign. Goal: Intuitive and beautiful.'
source_url: https://github.com/monero-project/monero-gui/issues/2306
author: ghost
assignees: []
labels: []
created_at: '2019-07-21T19:23:27+00:00'
updated_at: '2019-07-25T11:55:51+00:00'
type: issue
status: closed
closed_at: '2019-07-23T08:54:53+00:00'
---

# Original Description
_!!! This does **not** claim to be beautiful (yet). It's just **intuitive**. (Beautiful comes later.) !!!_
_It aggregates/fixes #2024 #2208 #2293 #2298 #2304._

This is what the user should see directly after starting the GUI:
![image](https://user-images.githubusercontent.com/46682965/61594710-25ba2380-abef-11e9-9f60-2247f984f0b9.png)
Nothing more!

Getting started is self-explaining:
![image](https://user-images.githubusercontent.com/46682965/61594892-08865480-abf1-11e9-9983-192b9e480a42.png)

If you wish, you also can go online without opening a wallet! Let's try that:
![image](https://user-images.githubusercontent.com/46682965/61625739-bd655380-ac7b-11e9-88a8-54a9d969ecab.png)
Of course "Local Node" is preselected :)  And nobody will get angry because a 70 GB download silently starts in the background :)

![image](https://user-images.githubusercontent.com/46682965/61668720-e0c0ea80-acdd-11e9-8c1e-ea7dadee62cc.png)
Looks like we are online :) And nobody gets bothered with geeky words like "daemon".

Now let's see a wallet:
![image](https://user-images.githubusercontent.com/46682965/61872545-e6881d00-aee3-11e9-87b7-f88cedf3b985.png)
Why should we bother the user with 2 balances? In case some funds are locked, it's enough to tell him on the `Send` page. :)

Let's see another wallet!
![image](https://user-images.githubusercontent.com/46682965/61668268-7f4c4c00-acdc-11e9-8c4d-a5abe5f38fd6.png)
Oh, it doesn't know the balance yet! How self-explaining! And the user doesn't get shocked with a wrong XMR amount!

In the settings there's a checkbox, which is not checked by default:
![image](https://user-images.githubusercontent.com/46682965/61668289-8ecb9500-acdc-11e9-9cdd-ccae970f5057.png)
If multiple accounts are detected, the checkbox is auto-checked.

Other features:
- No more separate "Welcome"-screen! This helps so much to understand how the GUI works! Now you can see it at a glance! And don't you hate it when you are trying a new software, but the software won't let you to the main screen?
- No more 3 wallet modes, which were confusing, and you had to select a mode before opening a wallet. Now you can enable the advanced features in the settings per checkbox at any time you like :)

If there's consensus between veterans that we want to go in this direction (please tell me), I'd be looking for a team to make the proposal more detailed and beautiful.



# Discussion History
## rating89us | 2019-07-21T20:36:55+00:00
I believe the wallet could support different themes/skins, so that users could choose what they like most.

## selsta | 2019-07-23T08:41:26+00:00
A full redesign is currently out of scope. Small improvements (statusbar, smaller network card, ...) are something we are looking into.

Also, the proposed design seems simpler because it is missing a lot of options the current design offers. Once you add everything the design will get more complex.

## ghost | 2019-07-23T08:54:53+00:00
> A full redesign is currently out of scope.

I understand that.

> Also, the proposed design seems simpler because it is missing a lot of options

That misses the point. 90% of the proposal is improvement by rearrangement. 10% is dropping stuff, like the door symbol, that closes the wallet, and causes anxiety for those who don't know what it does, or the symbol to change the theme, that is also placed on the main window, as if people changed every morning to day mode and every night to night mode.

## ghost | 2019-07-23T09:51:28+00:00
> @Realchacal
> GUI wallet will eventually die of user experience if dose not break and changes.

You mean we would need a redesign like this? 

## ghost | 2019-07-23T09:56:59+00:00
@maogo Do you think veterans said "it's out of scope" because of the development effort or because they think the GUI is good like it is?

## dEBRUYNE-1 | 2019-07-23T11:41:28+00:00
>because of the development effort

This. A full redesign takes a lot of development effort (a full redesign may take six to twelve months of work) and we cannot even be certain that the majority of users will like it. A full redesign currently has an unattractive risk reward ratio in my opinion. 

# Action History
- Created by: ghost | 2019-07-21T19:23:27+00:00
- Closed at: 2019-07-23T08:54:53+00:00
