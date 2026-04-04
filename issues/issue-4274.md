---
title: Device not found. Trezor
source_url: https://github.com/monero-project/monero-gui/issues/4274
author: stoicvig
assignees: []
labels: []
created_at: '2024-02-05T22:51:19+00:00'
updated_at: '2024-02-06T03:45:36+00:00'
type: issue
status: closed
closed_at: '2024-02-06T03:45:36+00:00'
---

# Original Description
Hello all, I am not a tech person and would like some help identifying why my trezor wont connect to the monero gui anymore. I have had it working before but recently tried to open it and got the error message after putting in my password - devise not found. Trezor.  I use the recent update on both. Thanks 

# Discussion History
## selsta | 2024-02-05T22:54:03+00:00
Do you use flatpak?

## stoicvig | 2024-02-06T00:13:08+00:00
Not sure what that is. It rings a bell 


## stoicvig | 2024-02-06T00:13:58+00:00
How can I check this?


## selsta | 2024-02-06T00:17:28+00:00
How did you install monero-gui?

## stoicvig | 2024-02-06T00:18:51+00:00
I installed it from the monero site. linux64-bit I believe
. 

## selsta | 2024-02-06T00:30:17+00:00
What you posted means monero-gui is compiled without Trezor support but that's not possible when downloaded from getmonero.org

Are you 100% sure it's not installed from a package manager?

## stoicvig | 2024-02-06T00:35:06+00:00
Im sorry but I am not sure. I do know I had it working with Trezor before as I transferred monero to the wallet and from using trezor. But now I cant access it. 

Is there a way to find out the information you need?

## selsta | 2024-02-06T00:39:04+00:00
You can try to go to getmonero.org, download the Linux GUI and then start exactly that binary and check if it works.

If it doesn't work please post the exact error message.

## stoicvig | 2024-02-06T00:45:15+00:00
Would I need to create a new wallet from hardware or restore from seed? 

Another thing I noticed is that I never had a seed with the GUI only for the trezor.  Is the trezor seed the one I would use?

## selsta | 2024-02-06T00:46:11+00:00
No, you would not need to create a new wallet, just open the existing one.

## stoicvig | 2024-02-06T00:57:17+00:00
It has been stuck on the opening wallet page for 10 minutes now. 


## selsta | 2024-02-06T00:58:27+00:00
What does it say on the Trezor? Is it asking you to enter a passphrase?

## stoicvig | 2024-02-06T00:59:11+00:00
Nothing on the Trezor


## stoicvig | 2024-02-06T01:02:01+00:00
Ok sorted. There were 2 options for me to choose from monero gui and monero gui applmage. It has worked with Applmage


# Action History
- Created by: stoicvig | 2024-02-05T22:51:19+00:00
- Closed at: 2024-02-06T03:45:36+00:00
