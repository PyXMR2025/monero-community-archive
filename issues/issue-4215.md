---
title: Monero crashing while syncing or won't sync
source_url: https://github.com/monero-project/monero-gui/issues/4215
author: Cottonwoodhill
assignees: []
labels: []
created_at: '2023-09-03T11:10:31+00:00'
updated_at: '2023-09-03T22:09:11+00:00'
type: issue
status: closed
closed_at: '2023-09-03T22:09:11+00:00'
---

# Original Description
Hi,

Hi, I am using the latest version of Monero GUI 0.18.2.2-unknown (At. 5.15.10) on Whonix 17. Every time I try to sync my wallet it crashes a few blocks before the end. I tried to delete my wallet and restoring it with the paraphrase, deleting all the files in .bitmonero direcrory, etc No success... Would somebody please help ? Thanks

In addition here is the terminal log : 

user@host:~$ flatpak run org.getmonero.Monero

(monero-wallet-gui:2): dbind-WARNING **: 11:04:15.886: AT-SPI: Error retrieving accessibility bus address: org.freedesktop.DBus.Error.ServiceUnknown: org.freedesktop.DBus.Error.ServiceUnknown
Qt: Session management error: Authentication Rejected, reason : None of the authentication protocols specified are supported and host-based authentication failed
2023-09-03 11:04:17.274	W Qt:5.15.10 GUI:- | screen: 1920x977 - available: QSize(1920, 946) - dpi: 96.0926 - ratio:0.750724
2023-09-03 11:04:27.348	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2023-09-03 11:04:27.348	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2023-09-03 11:04:27.348	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
20
2023-09-03 11:04:28.608	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2023-09-03 11:04:28.608	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2023-09-03 11:04:28.608	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2023-09-03 11:04:28.609	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2023-09-03 11:04:29.046	W Logging to "/home/user/.bitmonero/monero-wallet-gui.log"
2023-09-03 11:04:29.051	W file:///usr/lib/qml/QtQuick/Controls/ApplicationWindow.qml:259:9: QML ContentItem: Binding loop detected for property "implicitWidth"
2023-09-03 11:04:42.327	W Loaded wallet keys file, with public address: 
xxx
2023-09-03 11:05:00.654	I Monero 'Fluorine Fermi' (v0.18.2.2-unknown)
Forking to background...
2023-09-03 11:05:19.563	E daemonBlockChainHeight: Failed to connect to daemon
2023-09-03 11:06:19.832	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2023-09-03 11:06:20.048	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2023-09-03 11:06:20.049	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2023-09-03 11:06:52.105	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2023-09-03 11:06:52.105	E pull_blocks failed, try_count=3
2023-09-03 11:06:52.107	E daemonBlockChainHeight: Failed to connect to daemon
2023-09-03 11:06:52.107	E daemonBlockChainTargetHeight: Failed to connect to daemon
user@host:~$ flatpak run org.getmonero.Monero

(monero-wallet-gui:2): dbind-WARNING **: 11:04:15.886: AT-SPI: Error retrieving accessibility bus address: org.freedesktop.DBus.Error.ServiceUnknown: org.freedesktop.DBus.Error.ServiceUnknown
Qt: Session management error: Authentication Rejected, reason : None of the authentication protocols specified are supported and host-based authentication failed
2023-09-03 11:04:17.274	W Qt:5.15.10 GUI:- | screen: 1920x977 - available: QSize(1920, 946) - dpi: 96.0926 - ratio:0.750724
2023-09-03 11:04:28.608	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2023-09-03 11:04:28.608	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2023-09-03 11:04:28.608	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2023-09-03 11:04:28.608	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2023-09-03 11:04:28.608	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2023-09-03 11:04:28.609	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2023-09-03 11:04:29.046	W Logging to "/home/user/.bitmonero/monero-wallet-gui.log"
2023-09-03 11:04:29.051	W file:///usr/lib/qml/QtQuick/Controls/ApplicationWindow.qml:259:9: QML ContentItem: Binding loop detected for property "implicitWidth"
2023-09-03 11:04:42.327	W Loaded wallet keys file, with public address: 

2023-09-03 11:05:00.654	I Monero 'Fluorine Fermi' (v0.18.2.2-unknown)
Forking to background...
2023-09-03 11:05:19.563	E daemonBlockChainHeight: Failed to connect to daemon
2023-09-03 11:06:19.832	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2023-09-03 11:06:20.048	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2023-09-03 11:06:20.049	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2023-09-03 11:06:52.105	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2023-09-03 11:06:52.105	E pull_blocks failed, try_count=3
2023-09-03 11:06:52.107	E daemonBlockChainHeight: Failed to connect to daemon
2023-09-03 11:06:52.107	E daemonBlockChainTargetHeight: Failed to connect to daemon
user@host:~$ 


# Discussion History
## selsta | 2023-09-03T11:12:44+00:00
Try to use the binaries from getmonero.org instead of flatpak.

## Cottonwoodhill | 2023-09-03T11:14:11+00:00
Hi,
What would be the procedure to use them ? 
I'm not so expereienced....
Thanks 

## selsta | 2023-09-03T11:15:19+00:00
You download the Linux GUI, extract it and then open `./monero-wallet-gui` from the command line.

## Cottonwoodhill | 2023-09-03T11:22:31+00:00
user@host:~$ flatpak run org.getmonero.Monero

(monero-wallet-gui:2): dbind-WARNING **: 11:20:20.235: AT-SPI: Error retrieving accessibility bus address: org.freedesktop.DBus.Error.ServiceUnknown: org.freedesktop.DBus.Error.ServiceUnknown
Qt: Session management error: Authentication Rejected, reason : None of the authentication protocols specified are supported and host-based authentication failed
2023-09-03 11:20:21.485	W Qt:5.15.10 GUI:- | screen: 1920x977 - available: QSize(1920, 946) - dpi: 96.0926 - ratio:0.750724
2023-09-03 11:20:30.240	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2023-09-03 11:20:30.241	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2023-09-03 11:20:30.241	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.


2023-09-03 11:24:15.984	W Transaction extra has unsupported format: <2ad602c5f8f0c7118ec7cebe473d5f90d8c8d63407ec36d2a93e67709eaec317>
2023-09-03 11:24:15.984	W Transaction extra has unsupported format: <c6f82b8ff746eadd1fdca2a845c41bc1b8f8701e68069c4b35c84779d9b5c676>
2023-09-03 11:24:15.984	W Transaction extra has unsupported format: <7847647ae92787d3352bd9195aa606f992f8aeaa203b0e34ed238fec34ad2cdb>
2023-09-03 11:24:15.984	W Transaction extra has unsupported format: <8df45aa8d4a49bfe19286178403473be287ca0637a1721adf02ad2692e4ac966>
2023-09-03 11:24:15.985	W Transaction extra has unsupported format: <8917dd6288336d809c6c9a28edc7328d897de7b0dca77158549ec1c077a19314>


2023-09-03 11:24:30.292	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2023-09-03 11:24:30.526	E daemonBlockChainTargetHeight: Failed to connect to daemon
2023-09-03 11:24:30.526	E daemonBlockChainHeight: Failed to connect to daemon
2023-09-03 11:25:20.686	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2023-09-03 11:25:20.776	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2023-09-03 11:25:20.777	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2023-09-03 11:25:20.778	E pull_blocks failed, try_count=3

:(
`

## selsta | 2023-09-03T11:28:10+00:00
Did you post the correct logs? You are again starting flatpak instead of the release binaries manually.

1. Download the Linux GUI: https://downloads.getmonero.org/gui/linux64
2. Extract the .zip
3. Open the command line, `cd` to the folder
4. Start the binary with `./monero-wallet-gui`

There is no flatpak involved here.

## Cottonwoodhill | 2023-09-03T11:30:58+00:00
You are correct.

Let's see for now I get : 

user@host:~/Monero/monero-gui-v0.18.2.2$ ./monero-wallet-gui
2023-09-03 11:29:22.879	W Qt:5.15.8 GUI:- | screen: 1920x977 - available: QSize(1920, 946) - dpi: 96.0926 - ratio:0.750724
2023-09-03 11:29:28.921	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2023-09-03 11:29:28.921	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2023-09-03 11:29:28.921	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2023-09-03 11:29:28.921	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2023-09-03 11:29:30.267	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2023-09-03 11:29:30.267	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2023-09-03 11:29:30.267	W Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
2023-09-03 11:29:30.646	W Logging to "/home/user/.bitmonero/monero-wallet-gui.log"
2023-09-03 11:29:30.650	W qrc:/qt-project.org/imports/QtQuick/Controls/ApplicationWindow.qml:259:9: QML ContentItem: Binding loop detected for property "implicitWidth"
2023-09-03 11:30:11.730	W Loaded wallet keys file, with public address: 

2023-09-03 11:30:26.895	I Monero 'Fluorine Fermi' (v0.18.2.2-release)
Forking to background...





## selsta | 2023-09-03T11:31:53+00:00
The logs don't show anything interesting. Does it crash to the point where the GUI closes itself?

## Cottonwoodhill | 2023-09-03T11:32:40+00:00
It doesn't start syncing at the present moment

And again : 
023-09-03 11:32:24.452	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2023-09-03 11:32:28.265	E daemonBlockChainTargetHeight: Failed to connect to daemon
2023-09-03 11:32:28.314	E daemonBlockChainHeight: Failed to connect to daemon
2023-09-03 11:32:28.459	E daemonBlockChainTargetHeight: Failed to connect to daemon
2023-09-03 11:32:28.459	E daemonBlockChainHeight: Failed to connect to daemon
2023-09-03 11:32:28.493	E daemonBlockChainHeight: Failed to connect to daemon
2023-09-03 11:32:28.494	E daemonBlockChainTargetHeight: Failed to connect to daemon
2023-09-03 11:32:28.494	E daemonBlockChainHeight: Failed to connect to daemon
2023-09-03 11:32:28.496	E daemonBlockChainTargetHeight: Failed to connect to daemon
2023-09-03 11:32:28.497	E daemonBlockChainHeight: Failed to connect to daemon
2023-09-03 11:32:28.498	E daemonBlockChainTargetHeight: Failed to connect to daemon
2023-09-03 11:32:28.498	E daemonBlockChainHeight: Failed to connect to daemon
2023-09-03 11:32:28.499	E daemonBlockChainTargetHeight: Failed to connect to daemon
2023-09-03 11:32:28.499	E daemonBlockChainHeight: Failed to connect to daemon
2023-09-03 11:32:28.501	E daemonBlockChainTargetHeight: Failed to connect to daemon
2023-09-03 11:32:28.501	E daemonBlockChainHeight: Failed to connect to daemon
2023-09-03 11:32:28.501	E daemonBlockChainTargetHeight: Failed to connect to daemon
2023-09-03 11:32:28.502	E daemonBlockChainHeight: Failed to connect to daemon
2023-09-03 11:32:28.503	E daemonBlockChainTargetHeight: Failed to connect to daemon
2023-09-03 11:32:28.503	E daemonBlockChainHeight: Failed to connect to daemon
2023-09-03 11:32:28.504	E daemonBlockChainTargetHeight: Failed to connect to daemon
2023-09-03 11:32:28.505	E daemonBlockChainHeight: Failed to connect to daemon
2023-09-03 11:32:29.550	E daemonBlockChainHeight: Failed to connect to daemon
2023-09-03 11:32:59.821	I Monero 'Fluorine Fermi' (v0.18.2.2-release)
Forking to background...
2023-09-03 11:33:39.131	I Monero 'Fluorine Fermi' (v0.18.2.2-release)
Forking to background...



## Cottonwoodhill | 2023-09-03T11:44:45+00:00
Deleted again my wallet and restored it.

Also deleted /.bitmonero folder again

launched `monero-gui-v0.18.2.2$ ./monero-wallet-gui
`

Syncing...

Let's wait but I suppose it will crash again soon or later... 

## selsta | 2023-09-03T11:45:54+00:00
Can you go to Settings -> Info and share your Wallet mode?

## Cottonwoodhill | 2023-09-03T11:46:49+00:00
Wallet mode: Simple mode
Graphics mode: Low graphics mode

## selsta | 2023-09-03T11:54:03+00:00
Try to use advanced mode and set a custom remote node. You can go to the main menu by clicking on the exit symbol in the top left corner.

Then click on "Change wallet mode" and select "Advanced mode". Afterwards open your wallet again, go to Settings -> Node, select "Remote node" and enter the following node:

address: `selsta2.featherwallet.net`
port: `18081`

This should resolve your issue for now. No extra hard disk space required and no issues with monerod not starting.

----------

Other remote node in case the above has issues:

address: `selsta1.featherwallet.net `
port: `18081`

address: `node.community.rino.io`
port: `18081`

More nodes: nodes.monero.com

After that try to change the height again and do a full rescan. If you still have issues afterwards I will give you further steps.

## Cottonwoodhill | 2023-09-03T12:00:09+00:00
Connected.... syncing...

Will update !

Thanks for your assistance 👍

## Cottonwoodhill | 2023-09-03T14:46:08+00:00
Acutually I have the following : 

```
2023-09-03 13:44:14.027	W Failed to generate key derivation from tx pubkey, skipping
2023-09-03 13:45:41.136	W Failed to generate key derivation from tx pubkey, skipping
2023-09-03 14:17:13.716	E Failed to derive subaddress public key
2023-09-03 14:19:28.699	W Failed to generate key derivation from tx pubkey, skipping
2023-09-03 14:19:28.880	E Failed to derive subaddress public key
2023-09-03 14:20:34.361	W Failed to generate key derivation from tx pubkey, skipping
2023-09-03 14:22:39.803	W Failed to generate key derivation from tx pubkey, skipping
2023-09-03 14:22:48.246	E Failed to derive subaddress public key
2023-09-03 14:22:51.099	E Failed to derive subaddress public key
2023-09-03 14:23:07.992	W Failed to generate key derivation from tx pubkey, skipping
2023-09-03 14:23:08.469	E Failed to derive subaddress public key
```

![Capture](https://github.com/monero-project/monero-gui/assets/37047745/644dfb16-2075-477f-8ba2-e98886874ae4)


Keep wainting... 


## selsta | 2023-09-03T14:47:27+00:00
When was the first time you received XMR into this wallet?

## Cottonwoodhill | 2023-09-03T14:57:15+00:00
> When was the first time you received XMR into this wallet?

Some years ago

EDIT : let's wait a few more time
EDIT 2 : **years** instead of months


## Cottonwoodhill | 2023-09-03T16:01:19+00:00
Still syncing but :

2023-09-03 15:37:23.562	W Transaction extra has unsupported format: <f6cff1edd1a7861ed13d494dd4ae7c4a7f42b5c3bf91457310d2166722c1316f>
2023-09-03 15:37:23.878	W Failed to generate key derivation from tx pubkey, skipping
2023-09-03 15:42:11.671	W Failed to generate key derivation from tx pubkey, skipping
2023-09-03 15:58:39.919	W Transaction extra has unsupported format: <97ef64005b33f2ff9764b5537ad565159bc95419b07a3070e90a63ac7f5c9988>
2023-09-03 15:58:39.923	W Transaction extra has unsupported format: <58013973b0ccbf74d2d4ecca6d46356655bc27d1ef7649a02212ee670f853048>

😣


## selsta | 2023-09-03T16:02:53+00:00
Is this a view only wallet? Also I would let it sync up first, these messages are just warnings and don't necessarily indicate that something is wrong.

## Cottonwoodhill | 2023-09-03T16:04:57+00:00
Yes it is. Agree with you, let's finish the synchronization 👍

EDIT : if that finishes, but fingers crossed 🤞

## Cottonwoodhill | 2023-09-03T21:37:55+00:00
Achieved 🙏🚀💪🥂

![Capture](https://github.com/monero-project/monero-gui/assets/37047745/6fa95c3c-a4a6-4cf2-b7a9-2c181b50b600)

Thank you so much for your help @selsta 🥳


## selsta | 2023-09-03T22:09:11+00:00
Great :) Now make a backup of the wallet file and you can also try flatpak again if you prefer that. Closing as the issue seems resolved.

# Action History
- Created by: Cottonwoodhill | 2023-09-03T11:10:31+00:00
- Closed at: 2023-09-03T22:09:11+00:00
