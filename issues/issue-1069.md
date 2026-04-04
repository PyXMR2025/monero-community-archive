---
title: No way in GUI to switch from testnet to mainnet?
source_url: https://github.com/monero-project/monero-gui/issues/1069
author: ordtrogen
assignees: []
labels:
- resolved
created_at: '2018-01-09T22:36:28+00:00'
updated_at: '2018-03-30T01:18:18+00:00'
type: issue
status: closed
closed_at: '2018-03-30T01:18:18+00:00'
---

# Original Description
First wallet I created was on testnet. Now I can't find any way in GUI to switch to mainnet. Have looked through all settings. When I start GUI, displays testnet even before I have entered the password for the most recently opened wallet

![skarmbild_2018-01-09_23-35-39](https://user-images.githubusercontent.com/15184875/34746826-e3398e3a-f595-11e7-9ef9-42a5a8024561.png)



# Discussion History
## stoffu | 2018-01-10T02:02:44+00:00
You need to go back to the wizard window by either closing the current wallet or cancelling the password dialog. There's a check box "Testnet" in the wizard window.

## ordtrogen | 2018-01-10T05:36:15+00:00
Ok thanks.

Now the problem is that the wizard step with testnet checkbox is skipped, i.e when I get to it, it is displayed briefly but then wizard automatically moves to the next step and doesn't give me time to unselect testnet

(I'll try to make a screen recording)




## sanderfoobar | 2018-01-11T13:07:35+00:00
First of all, make sure that when you want to switch to mainnet, kill/close the `monerod --testnet` process and start it for mainnet: `./monerod`. I then do:

- Settings -> Manage Wallet -> Close wallet
- Choose language dialog -> English
- Open a wallet from file (disable checkbox 'testnet' here)

And you're good to go.

## ordtrogen | 2018-01-11T17:54:11+00:00
Here's a video showing what happens, and as I recorded it, I realized what the problem is

https://youtu.be/PxrBcFfXVxM

At the page in the Wizard where the button "Create a new wallet" is displayed, there is a check box which allows you to select (or unselect) "Testnet", but because it is outside the screen (10" in my case), you can't see the check box. When you click the "Create a new wallet" button, the window content is shifted upward slightly and you get to see the check box for a brief second before the Wizard moves to the next step.

Maybe I should change the issue title to something like "Testnet checkbox not visible on smaller screens"?



## sanderfoobar | 2018-01-11T22:22:09+00:00
Ah, thanks for the video. I can see how it hides the checkbox. 

Can I ask what kind of device/laptop you have?

## ordtrogen | 2018-01-12T07:58:04+00:00
Details are in first part of issue
Brand is Compaq or HP (can't check, am at work now)
Or did you refer to sth else?

Den 11 jan. 2018 23:22 skrev "Sander Ferdinand" <notifications@github.com>:

> Ah, thanks for the video. I can see how it hides the checkbox.
>
> Can I ask what kind of device/laptop you have?
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero-gui/issues/1069#issuecomment-357080861>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AOez6_GpL9yNE7tWJDt3i1GfyN-c2IKZks5tJomSgaJpZM4RYi1f>
> .
>


## ordtrogen | 2018-01-12T08:00:43+00:00
Sorry, wrong thread ...
see #1066


## sanderfoobar | 2018-03-30T00:43:59+00:00
I'm closing this issue in favor of #1066 for now. Lets continue there!

## sanderfoobar | 2018-03-30T00:44:05+00:00
+resolved

# Action History
- Created by: ordtrogen | 2018-01-09T22:36:28+00:00
- Closed at: 2018-03-30T01:18:18+00:00
