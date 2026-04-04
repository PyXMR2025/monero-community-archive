---
title: GUI appears to Download but won't run
source_url: https://github.com/monero-project/monero/issues/9261
author: 1James-Bond
assignees: []
labels:
- more info needed
created_at: '2024-03-25T16:13:20+00:00'
updated_at: '2025-12-19T14:53:17+00:00'
type: issue
status: closed
closed_at: '2025-12-19T14:53:17+00:00'
---

# Original Description
Attempted to restore wallet using the seed phrase. I had no problem previously performing this. It appears to download the files but there's no initialization or start up. Currently using Linux Zorin.

# Discussion History
## selsta | 2024-03-25T16:16:58+00:00
> It appears to download the files but there's no initialization or start up. Currently using Linux Zorin.

Where exactly are you stuck? Were you able to open the GUI and restore the wallet from seed?

## 1James-Bond | 2024-03-25T16:42:31+00:00
 I can go to the site and download the files for Linux. They just stay in my downloads folder. Nothing happens after that. I've tried opening the files individually, but I never get to the initial start page to access the restore tab.Last time I had no issue.As a side note I have cleaned my machine out to a great extent. After my last restore loading the blockchain left me low on memory so I had to dump a lot of what I had. 
    On Monday, March 25, 2024 at 12:17:21 PM EDT, selsta ***@***.***> wrote:  
 
 



It appears to download the files but there's no initialization or start up. Currently using Linux Zorin.


Where exactly are you stuck? Were you able to open the GUI and restore the wallet from seed?

—
Reply to this email directly, view it on GitHub, or unsubscribe.
You are receiving this because you authored the thread.Message ID: ***@***.***>
  

## 1James-Bond | 2024-03-25T17:04:27+00:00
It never gets to the screen that ask the Restore/ Start up selection. It never even gets the initial select language screen.

## selsta | 2024-03-25T17:59:05+00:00
It's a binary, how do you usually start binaries on your operating system? on Ubuntu for example you can double click on monero-wallet-gui.AppImage, but I don't know if that works Zorin. Maybe you have to start monero-wallet-gui from the command line.

# Action History
- Created by: 1James-Bond | 2024-03-25T16:13:20+00:00
- Closed at: 2025-12-19T14:53:17+00:00
