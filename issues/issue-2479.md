---
title: 'monero-gui-v0.15.0.1 "E Device not found in registry: ''Trezor''. Known devices:"'
source_url: https://github.com/monero-project/monero-gui/issues/2479
author: redmac68
assignees: []
labels:
- resolved
created_at: '2019-11-24T11:38:26+00:00'
updated_at: '2020-03-20T14:31:54+00:00'
type: issue
status: closed
closed_at: '2019-12-19T04:36:38+00:00'
---

# Original Description
OS: Linux Mint Debian Edition 3 (LMDE3)
-monero-gui-v14.1.0 running correctly with hardware wallet using trezor model T
-installed monero-gui-v0.15.0.1 to new folder
-ran monero-wallet-gui
-get message on gui "Couldn't open wallet:device not found: Trezor"

-terminal shows:
neil@xps13-mint-neil ~/monero-gui-v0.15.0.1 $ ./monero-wallet-gui
2019-11-24 11:20:33.118	W app startd (log: /home/neil/.bitmonero/monero-wallet-gui.log)
2019-11-24 11:20:33.119	W Qt:5.9.7 GUI:v0.15.0.1 | screen: 1920x1080 - dpi: 96 - ratio:1.2996
2019-11-24 11:20:35.594	W qrc:/qt-project.org/imports/QtQuick/Controls/ApplicationWindow.qml:240:9: QML ContentItem: Binding loop detected for property "implicitWidth"
2019-11-24 11:20:50.346	I [PARSE URI] regex not matched for uri: ^((.*?)://)?(\[(.*)\](:(\d+))?)(.*)?
2019-11-24 11:20:50.347	I Generating SSL certificate
2019-11-24 11:20:50.350	I ringdb path set to /home/neil/.shared-ringdb
2019-11-24 11:20:50.525	W Account on device. Initing device...
**2019-11-24 11:20:50.526	E Device not found in registry: 'Trezor'. Known devices: 
2019-11-24 11:20:50.526	E  - Ledger
2019-11-24 11:20:50.526	E  - default
2019-11-24 11:20:50.526	E Error opening wallet: device not found: Trezor
2019-11-24 11:20:50.530	E Error opening wallet with password:  device not found: Trezor**

Double checked that monero-gui-v14.1.0 still works correctly with Trezor.

# Discussion History
## xiphon | 2019-11-24T12:51:33+00:00
Seems release binaries are accidentally compiled without Trezor support.
Would you like to test the new ones?

## redmac68 | 2019-11-24T13:12:51+00:00
I would be honoured. Thanks.


On Sun 24 Nov 2019, 12:51 xiphon, <notifications@github.com> wrote:

> Seems release binaries are accidentally compiled without Trezor support.
> Would you like to test the new ones?
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero-gui/issues/2479?email_source=notifications&email_token=ALPMIZVTJHHCZW6USGVK3PDQVJ2FLA5CNFSM4JQ6VDR2YY3PNVWWK3TUL52HS4DFVREXG43VMVBW63LNMVXHJKTDN5WW2ZLOORPWSZGOEFAKQUA#issuecomment-557885520>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ALPMIZRZCAHCVYQP3NUM4WDQVJ2FLANCNFSM4JQ6VDRQ>
> .
>


## xiphon | 2019-11-24T13:43:44+00:00
DELETED

## redmac68 | 2019-11-24T14:26:41+00:00
Hi, that looks good .. Trezor device is found. 
Testing limited as I am using a remote node and have "Network status: Wrong version" and "Connected daemon is not compatible with GUI. Please upgrade or connect to another daemon".

 I have tried the remote node "uwillrunanodesoon.moneroworld.com:18089", but I still get the same errors. 

Is there any trusted remote node running 15.0.1 daemon or does this have to wait for 30th Nov?

## selsta | 2019-11-24T14:27:24+00:00
Please try node.xmr.to:18081

## redmac68 | 2019-11-24T14:52:42+00:00
Hi, thanks again. That node works. 

I tried to send and got an error
"Can't create transaction: unexpected error: Call method failed"

.. but I guess this is to be expected until all nodes are updated. If there is something else that I should check, let me know.

## selsta | 2019-11-24T14:53:39+00:00
Please install the beta firmware from https://beta-wallet.trezor.io and try again.

## redmac68 | 2019-11-24T15:23:50+00:00
Hi, the Trezor has the latest firmware version already installed (2.1.8). 
I don't see any other version available.
The message in a terminal window when the send fails is like:

2019-11-24 14:50:27.702	I Decrypted payment ID: <0000000000000000>
2019-11-24 14:50:27.760	E Failed to invoke http request to  /call/21, wrong response code: 400 Response Body: {"error":"session not found"}
2019-11-24 14:50:27.766	E Can't create transaction:  unexpected error: Call method failed

I re-tested sending a small amount to my own address .. and this was successful.

## schulzemic | 2019-11-24T17:13:46+00:00
I also tried this now. Updated the firmware to 2.1.8, and sent to my own subaddress, using my own remote note. It worked, thank you!

## selsta | 2019-11-24T19:24:22+00:00
We will release a v0.15.0.2 point release in the next days to fix this.

## xiphon | 2019-11-24T19:46:59+00:00
Removed the link to binary i posted above. It was uploaded just for testing purposes (to be sure that Trezor support issue is fixed). Is not a good idea to let users download random binaries,

Please wait for v0.15.0.2 point release in a few days.

@redmac68 @schulzemic thanks for testing.

## redmac68 | 2019-11-25T16:16:36+00:00
@xiphon @selsta @schulzemic thanks for your support .... beyond awesome. 

## selsta | 2019-12-19T04:24:53+00:00
+resolved

## redmac68 | 2020-03-20T14:26:48+00:00
Monero Gui Linux x64 v 0.15.0.4 now gives message "Couldn't open wallet: device not found: Trezor"

This from terminal window ..

2020-03-20 14:18:02.868	W app startd (log: /home/neil/.bitmonero/monero-wallet-gui.log)
2020-03-20 14:18:02.869	W Qt:5.9.7 GUI:v0.15.0.4 | screen: 1920x1080 - dpi: 96 - ratio:1.2996
2020-03-20 14:18:07.090	W qrc:/qt-project.org/imports/QtQuick/Controls/ApplicationWindow.qml:240:9: QML ContentItem: Binding loop detected for property "implicitWidth"
2020-03-20 14:18:38.191	I [PARSE URI] regex not matched for uri: ^((.*?)://)?(\[(.*)\](:(\d+))?)(.*)?
2020-03-20 14:18:38.191	I Generating SSL certificate
2020-03-20 14:18:38.192	I ringdb path set to /home/neil/.shared-ringdb
2020-03-20 14:18:38.301	W Account on device. Initing device...
2020-03-20 14:18:38.301	E Device not found in registry: 'Trezor'. Known devices: 
2020-03-20 14:18:38.301	E  - Ledger
2020-03-20 14:18:38.301	E  - default
2020-03-20 14:18:38.306	E Error opening wallet: device not found: Trezor
2020-03-20 14:18:38.315	E Error opening wallet with password:  device not found: Trezor

Can someone please check/re-open?

## selsta | 2020-03-20T14:28:34+00:00
@redmac68 Known issue, will be fixed with v0.15.0.5. Should be out soon. I’ve also added the Trezor dependency to the README so that this doesn’t happen again.

https://github.com/monero-project/monero-gui/pull/2796

## redmac68 | 2020-03-20T14:31:54+00:00
Great news, thanks again.

On Fri, 20 Mar 2020 at 14:28, selsta <notifications@github.com> wrote:

> @redmac68 <https://github.com/redmac68> Known issue, will be fixed with
> v0.15.0.5. Should be out soon. I’ve also added the Trezor dependency to the
> README so that this doesn’t happen again.
>
> #2796 <https://github.com/monero-project/monero-gui/pull/2796>
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero-gui/issues/2479#issuecomment-601729338>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ALPMIZUK4K5HVIPC6CMBD3DRIN4SFANCNFSM4JQ6VDRQ>
> .
>


# Action History
- Created by: redmac68 | 2019-11-24T11:38:26+00:00
- Closed at: 2019-12-19T04:36:38+00:00
