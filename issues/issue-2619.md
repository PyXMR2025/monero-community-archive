---
title: 'Feature request: "Don''t ask me again" for keeping daemon running when closing
  GUI'
source_url: https://github.com/monero-project/monero-gui/issues/2619
author: Wegerich
assignees: []
labels: []
created_at: '2019-12-16T13:37:39+00:00'
updated_at: '2022-02-05T17:32:38+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I prefer to leave the GUI closed almost all the time while I am working on my computer. Occasionally I open it to check for payments, then close it again. It is unnecessary to prompt me about keeping the daemon open every time I close the software.

I would like to see an option in settings 

> **What should happen to the transaction monitoring node after the wallet GUI is closed?**
> - Keep the node running so that my wallet is always ready to use **(recommended)**
> - Always disable the node when closing. (Will require blockchain to synchronize when re-opened)
> - Ask me what to do each time I close the wallet GUI


When the "ask me" prompt comes up, there could also be an option "don't ask me again" to check before selecting. Also on this page it could be worth describing the significance of "force stop" and "keep it running" so that the best option is more clear to novices.

# Discussion History
## rating89us | 2019-12-16T14:45:01+00:00
I agree.

But when running in the background, monerod should be displayed as an icon in the notification area of the taskbar. 

I was recently having problems connecting my GUI to monerod, and couldn't figure out what was the problem. Then only after Ctrl+Alt+Del I realised that monerod.exe was already running, and after closing it the GUI started to work again.

## sanderfoobar | 2020-07-09T12:58:15+00:00
I don't think the GUI should be responsible for starting, stopping, and managing the daemon. It should only be a client that can connect to a RPC port, whether that's on localhost or over the internet (remote node) is unimportant. So I would instead opt for a system service that manages the daemon with a taskbar icon and all. 

## Wegerich | 2020-07-09T13:00:22+00:00
> I don't think the GUI should be responsible for starting, stopping, and managing the daemon. It should only be a client that can connect to a RPC port, whether that's on localhost or over the internet (remote node) is unimportant. So I would instead opt for a system service that manages the daemon with a taskbar icon and all.

My proposal is a minor change to the current operation of the GUI. 

I feel that your suggestion is a major change to how the GUI interacts with the daemon and would be better suited to being its own separate GitHub issue. 

## sanderfoobar | 2020-07-09T14:37:18+00:00
@Wegerich Yeah it's def. out of the scope for this issue, I agree that the prompt when closing is probably unneeded and could use a "Remember my decision" or so.

## ITwrx | 2022-02-05T17:32:38+00:00
Yes, i always want my node closed when i close the GUI and find these questions and clicks fairly annoying. If a user hasn't initiated an action, they shouldn't be asked to work for the GUI, especially every time they want to use the GUI. It can feel like passive aggressive punishment instead of the helpful option it was intended to be. Like "oh, you wanted a GUI huh? well you won't mind if i ask you tons of questions then" :) Or "One doesn't simply make a GUI!"

# Action History
- Created by: Wegerich | 2019-12-16T13:37:39+00:00
