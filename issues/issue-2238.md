---
title: v0.14.x.x High CPU Usage on Linux
source_url: https://github.com/monero-project/monero-gui/issues/2238
author: EmbeddedAndroid
assignees: []
labels: []
created_at: '2019-06-29T19:05:51+00:00'
updated_at: '2020-05-01T18:19:21+00:00'
type: issue
status: closed
closed_at: '2019-06-30T20:03:15+00:00'
---

# Original Description
Every since upgrading from the v0.13.x.x  to the v0.14.x.x GUI release, I've noticed very high CPU utilization when running the GUI. On an Intel quad core i7, I'm seeing constant 80% CPU utilization on each of the four cores.

![Screenshot 2019-06-29 at 11 55 24 AM](https://user-images.githubusercontent.com/1061011/60388348-dc017180-9a64-11e9-8d42-a6d29bf4f994.png)

![Screenshot 2019-06-29 at 11 56 20 AM](https://user-images.githubusercontent.com/1061011/60388355-08b58900-9a65-11e9-9bd8-c00956e0d6e6.png)

I'm using a fully sync'd local daemon, configured as a remote node in the GUI. Installed using the prebuilt binaries, and the start-gui.sh script. 

Please let me know what information about the running process that would be helpful to have to debug!





# Discussion History
## selsta | 2019-06-29T19:21:25+00:00
Weird, normally CPU usage shoudn’t be noticeable. Is your wallet refreshing? Does this also happen while being inside the wizard? Does this happen with a fresh wallet? Is this inside a virtual machine?

## sanderfoobar | 2019-06-30T14:32:14+00:00
Currently you benchmark both `monero-wallet-gui` and `monerod` at the same time. This makes little sense, from a bug reporting perspective, as we now don't know if the reported CPU usage is due to the GUI or the local node :)

Please kill `monerod` and try again.

## sanderfoobar | 2019-06-30T14:33:08+00:00
In addition, please note `monerod` *could* be doing a database migration.

## EmbeddedAndroid | 2019-06-30T15:56:30+00:00
Sorry if I wasnt clear but ```monerod``` is running on another machine and I'm using the GUI to connect to over a local network.

## sanderfoobar | 2019-06-30T17:27:12+00:00
Ok, thanks for clarification.

1. Is your wallet refreshing blocks?
2. Does this also happen inside the Wizard? (the main menu, wallet closed)
3. Are you using a virtual machine?
4. Do you have a graphics card + drivers installed? (GUI uses hardware acceleration via OpenGL)
    - If not, try launching the GUI like this: `QMLSCENE_DEVICE=softwarecontext ./monero-wallet-gui`
5. Please state your exact CPU model and Linux distribution version.

## EmbeddedAndroid | 2019-06-30T20:03:15+00:00
Thanks for the help, it seems ```QMLSCENE_DEVICE=softwarecontext ./monero-wallet-gui``` was the trick here. 

I'm now seeing less than 2% CPU utilization on all four cores. 

I'll admit my setup is a bit unconventional, running a Chromebook, using crostini (kvm + oci runtime) providing a Debian vm/container and running the GUI from that. So there is no GPU available to the host that is running the GUI, makes sense why it was running up the CPU now.

If anyone is curious, here is the repo for running the GUI on a Chromebook with crostini: https://github.com/fnodes/monero-gui-crostini

I'm going to close this now, thanks again for the help!


## adrelanos | 2020-05-01T18:06:05+00:00
This wasn't fixed. Please re-open.

I also have 100% CPU using monero GUI `v0.15.0.4` in a VirtualBox VM (Whonix-Workstation). It's just the first screen (language selection screen). No monero installed ever in that VM before.

`QMLSCENE_DEVICE=softwarecontext ./monero-wallet-gui` helps as a workaround but it's not a solution. Users shouldn't be required to figure that out the hard way. Should be the default or some other fix.

Also my CPU use is now down to 30% which still seems to much for just an idle language selection screen.

## adrelanos | 2020-05-01T18:19:21+00:00
Thanks!

(Looks like a new ticket was created instead of re-opening the old one: https://github.com/monero-project/monero-gui/issues/2878 )

# Action History
- Created by: EmbeddedAndroid | 2019-06-29T19:05:51+00:00
- Closed at: 2019-06-30T20:03:15+00:00
