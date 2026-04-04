---
title: '[UX] Add a tray icon for the GUI'
source_url: https://github.com/monero-project/monero-gui/issues/2038
author: ghost
assignees: []
labels: []
created_at: '2019-03-27T11:59:15+00:00'
updated_at: '2019-03-27T15:25:46+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
On Windows-64 there is no tray icon in the system tray for the GUI. Currently if I completely close the GUI I can’t easily open the program again, I have to go into the file I downloaded and launch it from the .exe file.

<sub>Sent with <a href="http://githawk.com">GitHawk</a></sub>

# Discussion History
## selsta | 2019-03-27T12:18:33+00:00
Same here, did you try the Windows installer?

## ghost | 2019-03-27T12:27:00+00:00

>Same here, did you try the Windows installer?

@selsta No tray icon on either versions, why is there an installer and the other GUI download? Shouldn’t we just have the installer and that’s it? Seems unnecessary. 

<sub>Sent with <a href="http://githawk.com">GitHawk</a></sub>

## selsta | 2019-03-27T12:30:14+00:00
Sorry, I’m not a Windows user. If you close a program, why should it stay open inside the system tray?

> Shouldn’t we just have the installer and that’s it? Seems unnecessary.

Some people prefer the portable version.

## sanderfoobar | 2019-03-27T13:00:30+00:00
> why is there an installer and the other GUI download? Shouldn’t we just have the installer and that’s it?

I don't mind having the two around, but like Selsta mentioned one should be called portable.

## ghost | 2019-03-27T13:59:06+00:00

>Sorry, I’m not a Windows user. If you close a program, why should it stay open inside the system tray? ...

@selsta a lot of programs do on windows. 

Okay so the first download is the portable version, this needs to be clarified on the downloads page on the website. The installer should be listed first in the list as it’s more of a common option people will click. 

The whole download page needs some work tbh. 


<sub>Sent with <a href="http://githawk.com">GitHawk</a></sub>

## sanderfoobar | 2019-03-27T15:04:40+00:00
On the topic of Windows and system trays - I'd like to see `monerod` becoming a Windows service first. Service active? -> tray visible. From here you can also launch the GUI (if installed via installer).

## ghost | 2019-03-27T15:25:46+00:00
I’m going to do a mock up design for the downloads page to reflect things more clearly. I’ll post it in the website repo when done

<sub>Sent with <a href="http://githawk.com">GitHawk</a></sub>

# Action History
- Created by: ghost | 2019-03-27T11:59:15+00:00
