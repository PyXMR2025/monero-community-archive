---
title: General slowness and erratic behavior with local node (Debian 11)
source_url: https://github.com/monero-project/monero-gui/issues/4173
author: Animal-Machine
assignees: []
labels: []
created_at: '2023-05-08T01:08:31+00:00'
updated_at: '2023-05-11T15:59:58+00:00'
type: issue
status: closed
closed_at: '2023-05-11T15:57:54+00:00'
---

# Original Description
This problem concerns both the flatpak version and the AppImage version. I chose "Advanced Mode" and chose to store the blockchain on an USB stick but Monero GUI and my keys are on my computer.

I downloaded without problems the first 2.2 GB of the blockchain but since I exited the software and restarted, it's been a struggle and I'm only at 2.3 GB for about the same period of time, with monitoring...

Nothing strange appears in the "log" tab of the GUI. I have no firewall and no general network problems.

The issues I experiment are:

- everything very slow, but especially "Closing wallet" (which I had to do many times because of the other issues...) It takes between 20 and 40 minutes! Unchecking the box "Ask to stop local node during program exit" did not improve this. I also noted 30 minutes for "Network status: Starting the node" after which I restarted the GUI. The first start does not take so long.
- random disconnections. _Network status_ shifts from "Synchronizing" to "Connecting" or worse, "Disconnected" (worse because I have to start the daemon manually).
- when at least my network status is "Synchronizing", sometimes the progress bar appears full and says my node is synchronized, which is absurd.
- when everything seems apparently fine, the download remains very slow. This may be normal but still, `data.mdb` is modified about once every 10 minutes or less. This would not be a problem if I could just wait for my computer do the job, but with all of the above, I need to be behind my screen and intervene each time something malfunctions: this is impossible.
- bonus: while Monero GUI is running, some applications can take a dozen of minutes to launch (but not the ones you think: e.g. an image viewer opens after 15 minutes, but a web browser opens instantly)

# Discussion History
## selsta | 2023-05-08T10:32:02+00:00
Do you have the same issues when connecting to a remote node? You can specify one in Settings -> Node. Make sure to stop your local node first.

## Animal-Machine | 2023-05-08T12:33:51+00:00
I'm going to test that as soon as I can. I still need to learn about remote nodes to know a little what I'm doing, and I need an operational computer for other tasks, but I hope the following information will help you in the meantime:

I wanted to do it right after your comment, so I closed the app (took a while), clicked on "Monero GUI" and waited... forgot that I had launched it... and it popped in almost an hour later, asking for my password. My image viewer popped in too because I tried to open images during this period. I think that at this point, the node hasn't even started yet.

I just looked at my `syslog` and found this:
```
May  8 13:31:06 computername monero-wallet-g[39197]: Failed to load module "canberra-gtk-module"
May  8 13:31:06 computername monero-wallet-g[39197]: Failed to load module "canberra-gtk-module"
May  8 13:31:06 computername org.getmonero.Monero.desktop[39197]: Qt: Session management error: None of the authentication protocols specified are supported
May  8 13:31:06 computername org.getmonero.Monero.desktop[39197]: 2023-05-08 11:31:06.937#011W Qt:5.15.9 GUI:- | screen: 1920x1080 - available: QSize(1920, 1053) - dpi: 96 - ratio:1.35008
May  8 13:31:07 computername systemd[1569]: app-flatpak-org.gnome.gThumb-38111.scope: Succeeded.
May  8 13:31:08 computername org.gnome.Nautilus[39203]: Error: XMP Toolkit error 102: Unknown namespace prefix for qualified name
May  8 13:31:10 computername org.getmonero.Monero.desktop[39197]: 2023-05-08 11:31:10.724#011W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
May  8 13:31:10 computername org.getmonero.Monero.desktop[39197]: 2023-05-08 11:31:10.724#011W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
```
followed by about 35 lines like that, then:
```
May  8 13:31:11 computername org.getmonero.Monero.desktop[39197]: 2023-05-08 11:31:11.961#011W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
May  8 13:31:12 computername org.getmonero.Monero.desktop[39197]: 2023-05-08 11:31:12.226#011W Logging to "/home/username/.bitmonero/monero-wallet-gui.log"
May  8 13:31:12 computername org.getmonero.Monero.desktop[39197]: 2023-05-08 11:31:12.229#011W file:///usr/lib/qml/QtQuick/Controls/ApplicationWindow.qml:259:9: QML ContentItem: Binding loop detected for property "implicitWidth"
May  8 13:31:12 computername systemd[1569]: app-flatpak-org.gnome.gThumb-38122.scope: Succeeded.
May  8 13:31:12 computername systemd[1569]: app-flatpak-org.gnome.gThumb-38122.scope: Consumed 3.427s CPU time.
```
gThumb is my default image viewer, I have another one that worked without delay.
I found nothing around the time I have actually clicked on the Monero GUI desktop launcher.

One other thing I remarked is that the client seems to download some blocks (50 - 100 GB) right at the start, then nothing. `data.mdb` timestamps correspond to the moments when the software is launched and when it is stopped (if not killed, e.g the current timestamp is 13:31, GNOME told me it wasn't responding and incited me to terminate it, sometimes it doesn't and I use command line).

## Animal-Machine | 2023-05-11T14:08:10+00:00
I executed Monero GUI on LXDE. It starts, and stops, within seconds. It's disproportionate to the dozens of minutes I experienced with GNOME.

The local node still doesn't work, but the error messages are now consistent. What I get now is:

> **Daemon failed to start**
> 
> Timed out, local node isn't responding after 120 seconds.
> 
> Please check your wallet and daemon log for errors. You can also try to stard monerod manually.

So, it seems there are more than one problems here. We may need to address the issues separately. There are at least two of them:

- Extreme slowness and display errors with GNOME
- Daemon failing to start

I could rename the current issue to address the GNOME one and create a separated issue for the deamon but I prefer to wait for advice on this because I don't know what would be better for developers to keep track on things.

I'm going to give you what I found in `bitmonero.log` and I should also be able to try out and use a remote node today.

## selsta | 2023-05-11T14:10:58+00:00
Can you try to start `monerod` manually from the command line and post the output here? If you have a custom blockchain directory set you can use the `--data-dir` flag.

## selsta | 2023-05-11T14:14:19+00:00
Regarding GNOME, I'm not aware of any issues with it. We have never received a similar report even though most Linux users run on Ubuntu with GNOME.

Is it possible that you can update your desktop environment?

## Animal-Machine | 2023-05-11T14:28:28+00:00
`./monerod --data-dir=/media/username/myencryptedkey/Monero` :

```
2023-05-11 14:19:44.906	I Monero 'Fluorine Fermi' (v0.18.2.2-release)
2023-05-11 14:19:44.906	I Initializing cryptonote protocol...
2023-05-11 14:19:44.906	I Cryptonote protocol initialized OK
2023-05-11 14:19:44.907	I Initializing core...
2023-05-11 14:19:44.907	I Stopping cryptonote protocol...
2023-05-11 14:19:44.907	I Cryptonote protocol stopped successfully
2023-05-11 14:19:44.907	E Exception in main! boost::filesystem::create_directories: Permission denied: "/media/username/myencryptedkey"
```

`sudo ./monerod --data-dir=/media/username/myencryptedkey/Monero` :

```
2023-05-11 14:20:23.465	I Monero 'Fluorine Fermi' (v0.18.2.2-release)
2023-05-11 14:20:23.465	I Initializing cryptonote protocol...
2023-05-11 14:20:23.465	I Cryptonote protocol initialized OK
2023-05-11 14:20:23.466	I Initializing core...
2023-05-11 14:20:23.467	I Loading blockchain from folder /media/username/myencryptedkey/Monero/lmdb ...
2023-05-11 14:20:23.569	I Loading checkpoints
2023-05-11 14:20:23.570	I Core initialized OK
2023-05-11 14:20:23.571	I Initializing p2p server...
2023-05-11 14:20:23.574	I p2p server initialized OK
2023-05-11 14:20:23.574	I Initializing core RPC server...
2023-05-11 14:20:23.577	I Binding on 127.0.0.1 (IPv4):18081
2023-05-11 14:20:24.328	I core RPC server initialized OK on port: 18081
2023-05-11 14:20:24.338	I Starting core RPC server...
2023-05-11 14:20:24.338	I core RPC server started ok
2023-05-11 14:20:24.339	I Starting p2p net loop...
2023-05-11 14:20:25.340	I 
2023-05-11 14:20:25.340	I **********************************************************************
2023-05-11 14:20:25.340	I The daemon will start synchronizing with the network. This may take a long time to complete.
2023-05-11 14:20:25.340	I 
2023-05-11 14:20:25.340	I You can set the level of process detailization through "set_log <level|categories>" command,
2023-05-11 14:20:25.340	I where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2023-05-11 14:20:25.340	I 
2023-05-11 14:20:25.340	I Use the "help" command to see the list of available commands.
2023-05-11 14:20:25.341	I Use "help <command>" to see a command's documentation.
2023-05-11 14:20:25.341	I **********************************************************************
2023-05-11 14:20:45.616	I [109.190.247.5:18080 OUT] Sync data returned a new top block candidate: 1 -> 2883566 [Your node is 2883565 blocks (9.0 years) behind] 
2023-05-11 14:20:45.616	I SYNCHRONIZATION started
2023-05-11 14:20:46.054	I Synced 101/2883566 (0%, 2883465 left)
2023-05-11 14:20:46.148	I Synced 201/2883566 (0%, 2883365 left)
2023-05-11 14:20:46.233	I Synced 301/2883566 (0%, 2883265 left)
```

Currently syncing, at 7%!

How to allow Monero GUI to access external storage now?

## selsta | 2023-05-11T14:29:57+00:00
Why does it need sudo? Seems to be a permission issue, that's why monerod fails to start.

monerod should work without sudo if setup correctly.

Also is /media a network drive?

## Animal-Machine | 2023-05-11T14:37:30+00:00
No it's local, `myencryptedkey` is a USB stick.

I don't know why it needs sudo, it's the fist time I execute `monerod` manually, I had this idea and it worked.

This is the AppImage version of Monero GUI. I had to give an explicit authorization to the flatpak version, with Flatseal, so that it can access all files on the filesystem. It worked, as I could see that `data.mdb` was growing in size.

## selsta | 2023-05-11T14:40:33+00:00
Can you share the permission of data.mdb and lock.mdb file?

## Animal-Machine | 2023-05-11T14:47:45+00:00
```
-rw------- 1 username username 2431107072 10 mai   12:51 data.mdb
-rw------- 1 username username       8192 11 mai   15:51 lock.mdb
```

This is wrong. `data.mdb` should not be dated on May 10th but on May 11th. Also it still weights 2.3 GB.

## selsta | 2023-05-11T15:07:23+00:00
Which user are you logged into? username?

Can you also share the permissions for `/media/username/myencryptedkey`

## Animal-Machine | 2023-05-11T15:08:00+00:00
Yes, I'm logged into "username" (I changed the name of course)

## selsta | 2023-05-11T15:11:28+00:00
The "Daemon failed to start" message won't go away as long as running the following command from command line doesn't work without sudo.

`./monerod --data-dir=/media/username/myencryptedkey/Monero`

I updated my previous comment, can you also reply to that in case you didn't see it?

## Animal-Machine | 2023-05-11T15:14:57+00:00
> Can you also share the permissions for `/media/username/myencryptedkey`

Oh I'm sorry, I discovered a mistake made earlier. Because of a spelling mistake in "myencryptedkey" (not the real name), I executed ./monerod with the wrong file path. With `sudo`, I created a new folder under /media/username/ ...

I hid all my comment coming out of this mistake, marking them as "resolved".

So, to go back to this:

> Can you try to start monerod manually from the command line and post the output here? If you have a custom blockchain directory set you can use the --data-dir flag.

Here is the actual result:

```
2023-05-11 15:09:30.830	I Monero 'Fluorine Fermi' (v0.18.2.2-release)
2023-05-11 15:09:30.830	I Initializing cryptonote protocol...
2023-05-11 15:09:30.830	I Cryptonote protocol initialized OK
2023-05-11 15:09:30.836	I Initializing core...
2023-05-11 15:09:30.837	I Loading blockchain from folder /media/username/myencryptedkey/Monero/lmdb ...
2023-05-11 15:09:30.839	W The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
2023-05-11 15:09:30.840	W Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-05-11 15:09:30.853	E Error opening database: Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-05-11 15:09:30.854	I Stopping cryptonote protocol...
2023-05-11 15:09:30.854	I Cryptonote protocol stopped successfully
2023-05-11 15:09:30.855	E Exception in main! Failed to initialize core
```

## Animal-Machine | 2023-05-11T15:41:30+00:00
I learned that it could mean a corrupted database. I just deleted `data.mdb` and re-launched Monero GUI. It is currently synchronizing, but very slow again



## selsta | 2023-05-11T15:43:03+00:00
Syncing to an external USB stick is going to be really slow and not the best experience, internal SSD is preferred. I would recommend a remote node if you don't want to wait for it to sync.

## Animal-Machine | 2023-05-11T15:48:39+00:00
Is external SSD okay?

## selsta | 2023-05-11T15:49:51+00:00
Better than USB stick but still worse than internal SSD. A pruned node is around 60GB, but if you don't have enough space than using an external SSD should work.

## Animal-Machine | 2023-05-11T15:57:54+00:00
I will try these solutions and come back if I still have problems. Thank you for your time.

# Action History
- Created by: Animal-Machine | 2023-05-08T01:08:31+00:00
- Closed at: 2023-05-11T15:57:54+00:00
