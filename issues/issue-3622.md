---
title: Monero GUI unable to recognize Ledger Nano S on MacOS 11.4
source_url: https://github.com/monero-project/monero-gui/issues/3622
author: iostonykraft
assignees: []
labels: []
created_at: '2021-07-13T20:23:41+00:00'
updated_at: '2025-05-23T14:51:01+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
When attempting to create a new wallet from hardware, I get an error message saying that it is unable to find a hardware device. I am on the latest everything, MoneroGUI, Ledger Live firmware and Ledger device firmware. I have found at least one other report on reddit claiming to have the same issue and have been unable to find a fix or workaround. 


Possibly related to #3482

Error is "Error writing wallet from hardware device. Check application logs." 

Log states 
`2021-07-13 20:30:02.307	  0x70000b30d000	ERROR	device.io	src/device/device_io_hid.cpp:112	No device found`

Device can be found by my Mac and Ledger Live.

# Discussion History
## selsta | 2021-07-13T22:16:04+00:00
Do you have an Anti Virus on your system?

If no please try the following:

- Make sure you downloaded the GUI from getmonero.org
- Restart your computer
- Use a different USB port
- Only open Monero GUI, don't open any other program that accesses the Ledger
- Check if it works

## iostonykraft | 2021-07-13T22:37:56+00:00
I realized I was on a developer beta version of MacOS 11.4. Updating to the official release fixed this issue. This can thread can be deleted by a mod.

## iostonykraft | 2021-12-01T20:20:38+00:00
Reopened because i still struggle with this issue every day, i was wrong about it being fixed.

## mphelp | 2022-01-19T16:02:24+00:00
@iostonykraft Still having issues? I had this issue. My solution: make sure the Monero app is open on my Nano S when creating a wallet and NOT just the Nano S main menu open. Everything works flawlessly once I do this.

This helped the person in #3057 too.

## morgankeating | 2022-04-30T20:13:57+00:00
error writing wallet from device and
failed to generate new wallet; no device found
from:  https://support.ledger.com/hc/en-us/articles/360006352934-Monero-XMR-?docs=true
Set up with Ledger device
Unlock your Ledger device and open the Mon
![IMG_0078](https://user-images.githubusercontent.com/104695561/166121125-a11353b9-b8cb-4712-b4c7-16252aa04b4d.jpg)
ero app.
"Open Monero app" means on the Ledger device.  i.e. select by pressing both Ledger buttons when display shows "Monero"
After that "Please check your hardware wallet, your input may be required"
Ledger then displays "Export View Key"
After responding to Ledger with a selection (pressing button) hardware wallet gets created.



## Philippe734 | 2022-08-11T06:59:34+00:00
Same issue with Linux Ubuntu Mate 20.04 + release v 0.18.0 + Ledger Monera app v 1.7.8 ; the GUI can't connect to the Ledger device. So instead, I'm using the previous release 0.17.3.2 with success.
![image](https://user-images.githubusercontent.com/24923693/184079964-66502fab-dc5b-48ca-9a05-aad41460aee1.png)
![image](https://user-images.githubusercontent.com/24923693/184080075-c3c31540-e76f-42d4-b162-88c807427fe8.png)


## selsta | 2022-09-29T17:00:19+00:00
@Philippe734 sounds more like a different issue, v0.18.1.1 and v0.18.1.0 were built using the exact same build script in a docker container and nothing Ledger related was changed.

## Philippe734 | 2022-10-09T17:34:08+00:00
@selsta : correct, I delete my comment. The issue was to start monero app on Ledger before start monero gui. Because start monero's ledger app after start monero gui don't allow to connect ledger to monero gui.

## Jaston-byte | 2023-11-27T23:58:20+00:00
> @selsta : correct, I delete my comment. The issue was to start monero app on Ledger before start monero gui. Because start monero's ledger app after start monero gui don't allow to connect ledger to monero gui.

Thank you for the help. Resolved the issue.

## macdabby | 2025-05-23T14:50:59+00:00
Same issue on linux with 0.18.4.0.
Ledger had a script to run to apply udev rules for it to access the device.

https://raw.githubusercontent.com/LedgerHQ/udev-rules/master/add_udev_rules.sh

This worked on the ledger app but not tthe monero app. i wonder if its a similar issue though. i recall something about appimages having permission restrictions.

# Action History
- Created by: iostonykraft | 2021-07-13T20:23:41+00:00
