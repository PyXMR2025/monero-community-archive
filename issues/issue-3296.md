---
title: Wallet crashing on GUI wallet v. 0.17.1.9 when attempting to send from a Trezor
  T.
source_url: https://github.com/monero-project/monero-gui/issues/3296
author: ghost
assignees: []
labels: []
created_at: '2021-01-10T18:19:15+00:00'
updated_at: '2021-01-13T13:58:38+00:00'
type: issue
status: closed
closed_at: '2021-01-10T21:13:38+00:00'
---

# Original Description
Monero wallet version: 0.17.1.9

OS: Ubuntu 20.04.1, kernel release=5.8.0-36-generic

Using a Trezor Model T with Bridge v. 2.0.27

I am able to open my Monero Wallet GUI, and the terminal output looks fine:

----------

user@user:monero-wallet-gui

2021-01-10 16:37:19.722 W Qt:5.15.2 GUI:0.17.1.9-3ca5f10 | screen: 1920x1080 - dpi: 96 - ratio:0.997092

2021-01-10 15:55:51.532 W Logging to "/home/[redacted]/.bitmonero/monero-wallet-gui.log"

2021-01-10 15:55:51.533 W qrc:/qt-project.org/imports/QtQuick/Controls/ApplicationWindow.qml:259:9: QML ContentItem: Binding loop detected for property "implicitWidth"

2021-01-10 15:56:00.241 W Account on device. Initing device...

2021-01-10 15:56:22.181 W Device inited...

2021-01-10 15:56:22.269 W Loaded wallet keys file, with public address: [redacted]

----------

After the wallet opens, it syncs to my local node (I am not using a remote node for security). All of the blocks are successfully synced and my I see my full wallet balance displayed. I have been able to successfully receive Monero up until this point, but this is my first attempt at sending Monero from this wallet. When I attempt to send Monero, a prompt appears to confirm the send with the text of:

----------

Confirm Send: X.X XMR

From: Trezor [redacted]

To: Monero address: [redacted]

Fee: See on device

Creating transaction...

----------

The fee does not appear on the device, and the wallet crashes shortly afterwards with the following output in Terminal:

----------

2021-01-10 16:13:35.506 W WARNING: no two valid DNS TXT records were received

2021-01-10 16:13:35.581 W amount=[redacted], real_output=1, real_output_in_tx_index=0, indexes: redacted

2021-01-10 16:13:35.585 W amount=[redacted], real_output=1, real_output_in_tx_index=0, indexes: [redacted]

2021-01-10 16:13:35.590 W WARNING: no two valid DNS TXT records were received

2021-01-10 16:13:35.640 W amount=[redacted], real_output=1, real_output_in_tx_index=0, indexes: [redacted]

2021-01-10 16:13:35.641 W amount=[redacted], real_output=2, real_output_in_tx_index=1, indexes: [redacted]

2021-01-10 16:13:35.648 W amount=[redacted], real_output=1, real_output_in_tx_index=0, indexes: [redacted]

2021-01-10 16:13:35.649 W amount=[redacted], real_output=2, real_output_in_tx_index=1, indexes: [redacted]

2021-01-10 16:13:35.657 W amount=[redacted], real_output=1, real_output_in_tx_index=0, indexes: [redacted]

2021-01-10 16:13:35.657 W amount=[redacted], real_output=2, real_output_in_tx_index=1, indexes: [redacted]

munmap_chunk(): invalid pointer

Aborted (core dumped)

----------

Since this is a Trezor wallet, my secret spend key is not listed, so I cant move the monero to another wallet that is working. Please help. Thanks.

# Discussion History
## selsta | 2021-01-10T18:20:21+00:00
Can you try the CLI wallet? The wallets are compatible.

Also did this happen once or every time?

## ghost | 2021-01-10T18:52:33+00:00
I haven't tried the CLI wallet yet, but I prefer to use GUI, so if CLI works I'm just going to put my funds back in Exodus wallet until GUI is more stable. The crash occurs every time I attempt to send Monero to any address. I'll crank up the log level to 3 and post the output after one more attempt.

## ghost | 2021-01-10T19:03:57+00:00
Here is the log dump at logging level 3 after the last send attempt:

----------
2021-01-10 19:00:42.864	D sanity_check: 1 txes, 1 destinations
2021-01-10 19:00:42.864	D Adding [redacted] expected change
2021-01-10 19:00:42.866	D Total received by [redacted]: [redacted], expected [redacted]
2021-01-10 19:00:42.869	D Total received by [redacted]: [redacted], expected [redacted]
2021-01-10 19:00:42.869	T Ask for UNLOCKING for device  in thread 
2021-01-10 19:00:42.869	T Device  UNLOCKed
2021-01-10 19:00:42.870	I Decrypted payment ID: <redacted>
2021-01-10 19:00:42.870	D Using v13 rules
2021-01-10 19:00:42.870	T READ ENDS: Success. bytes_tr: 479
2021-01-10 19:00:42.870	T http_stream_filter::parse_cached_header(*)
2021-01-10 19:00:42.871	T READ ENDS: Success. bytes_tr: 211
2021-01-10 19:00:42.871	T http_stream_filter::parse_cached_header(*)
2021-01-10 19:00:42.871	E Failed to invoke http request to  /call/232, wrong response code: 400 Response Body: {"error":"session not found"}
munmap_chunk(): invalid pointer
Aborted (core dumped)
----------

## ghost | 2021-01-10T19:04:37+00:00
I am trying the CLI wallet now.

## selsta | 2021-01-10T19:04:43+00:00
Are you using the latest Trezor firmware?

## ghost | 2021-01-10T19:14:38+00:00
Ok, so I just attempted to send using the CLI wallet. It failed as well. Here is the output:

----------
[wallet [redacted]]: transfer [address redacted] [amount redacted]
Wallet password: 

Transaction 1/1:
Spending from address index 0
Sending [amount redacted].  The transaction fee is [amount redacted]

Is this okay?  (Y/Yes/N/No): Y
Please confirm the transaction on the device
double free or corruption (out)
Aborted (core dumped)
----------

I was not prompted to confirm the transaction on my Trezor.

## selsta | 2021-01-10T19:21:31+00:00
Please confirm if you are using the latest Trezor firmware. (not Bridge)

## ghost | 2021-01-10T19:22:26+00:00
Ok. I'll check on this shortly

## ghost | 2021-01-10T19:26:32+00:00
I am running the Trezor T firmware v. 2.3.4, which is the latest version on their firmware changelog: https://wiki.trezor.io/Firmware_changelog

## selsta | 2021-01-10T19:29:01+00:00
Just to confirm, you are using the official binaries from getmonero.org ?

There are currently no known Trezor issues so I would try the following

- Restore your Trezor wallet to a new file (Your balance will show up again correctly)
- Try a different computer

Also pinging @ph4r05 (Trezor dev), maybe he has an idea.

## ghost | 2021-01-10T19:31:06+00:00
Yes, I am using the official GUI and CLI binaries for Monero wallet v. 0.17.1.9 from getmonero.org. To restore my Trezor wallet to a new file, do I just delete the wallet file and import the wallet back from the Trezor? I'm not sure of how to do this.

## selsta | 2021-01-10T19:33:07+00:00
You don't have to delete anything.

Just go to the GUI main menu, click on "Create a new wallet from hardware" and then enter an unique name and select "Restore a wallet..."

Enter a restore height / date that was before you first received a transaction.

## ghost | 2021-01-10T19:40:51+00:00
Ok. I've already downloaded the blockchain. Where is the default blockchain location on Ubuntu?

## selsta | 2021-01-10T19:42:08+00:00
Just click on next, you don't have to set the blockchain location if you use default location.

It is ~/.bitmonero

## ghost | 2021-01-10T19:44:27+00:00
Ok, that worked. I'm synching the new wallet with the blockchain now. I'll test another transfer again and post my results.

## ph4r05 | 2021-01-10T19:49:51+00:00
The log indicates the Bridge is used (http requests). Is Libusb device listed in the log? Should be close after starting the wallet. Pls use Loglevel 4.

I would rather avoid using the bridge as it is another extra part that needs updating.

Try pls also updating the Bridge. Disconnect Trezor, kill the bridge process, then reconnect and try again.

Missing session can be a bridge issue. Everytime that happens, Bridge restart is needed.

Meanwhile, I take a look on the crash. It should throw an exception instead.

## ghost | 2021-01-10T19:52:02+00:00
I have to use Bridge in order to connect my Trezor with my Exodus wallet. It won't work without it. However, this does make sense. I had my Exodus wallet open at the time, which was using the Bridge.

## ghost | 2021-01-10T19:53:13+00:00
I did check and I'm using the latest version of Trezor Bridge (2.0.27)

## ph4r05 | 2021-01-10T20:00:46+00:00
@prometheus-aflame OK great! 

I think the access to the device has to be exclusive, to be on the safe side.

It is safer to close all other wallets that may interfere with the Bridge session. If an error happens, restart the bridge and reconnect.

So it works now?

## ghost | 2021-01-10T20:42:33+00:00
Not yet. The newly created wallet crashed again trying to synch the blockchain. If it crashes again, I'll reboot and try again.

## ph4r05 | 2021-01-10T20:59:59+00:00
OK, in case of a crash, post pls logs with loglevel 4

## ghost | 2021-01-10T21:13:37+00:00
Ok, the transaction was sent successfully this time. Steps taken:

1. Closed all applications using Trezor Bridge (Brave Browser, Exodus Wallet)
2. Deleted local XMR wallet that failed to send.
3. Loaded a new wallet from the Trezor into the Monero Wallet GUI.
4. Waited for the wallet to synch.

My assessment is that this was caused by either a Trezor Bridge session, a corrupted wallet file, or both. The steps taken above assumed both were the case. Done!

## selsta | 2021-01-10T21:15:23+00:00
Glad you resolved it, it sounds like the bridge was the issue.

## ph4r05 | 2021-01-11T00:05:27+00:00
pls @moneromooo-monero - I am thinking about this app crash.

Do you think it can be because of calling `wipe()` https://github.com/monero-project/monero/blob/964ad0e51a9b034311d9b341f0d8926cc5cc3ec7/contrib/epee/include/net/http_base.h#L205 when HTTP response returns 400 error code? Body is then empty. Do you think that calling `memwipe(&m_body[0], m_body.size());` on an empty string causes core dump?

## moneromooo-monero | 2021-01-11T00:14:53+00:00
m_body[0] should dereference a pointer that's probably NULL, it's bad. But in practice, it might just play with LEA and not acrtually dereference it, it does look dodgy though. I'd replace &m_body[0] with m_body.data(), though IIRC vtnerd says that's also invalid for other reasons.  It seems much simpler to just test whether empty first. The memwipe code itself won't break anything there.

## moneromooo-monero | 2021-01-11T00:18:28+00:00
ASAN and valgrind don't complain on this, but then s[1] = 0 on an empty std::string doesn't faze them either so they can't be trusted here :)

## ph4r05 | 2021-01-11T00:30:36+00:00
@moneromooo-monero thanks for fast response! I've just realized the body is not empty in this case as log shows:

```
2021-01-10 19:00:42.871 E Failed to invoke http request to /call/232, wrong response code: 400 Response Body: {"error":"session not found"}
```

So this was probably not it. But to be sure, I will add the PR with empty check. Thanks!

## moneromooo-monero | 2021-01-11T00:54:54+00:00
Looks like data() is not NULL for an empty string. In retrospect, it must be, since c_str() must return a NUL terminated string, so it has to have at least that NUL. So it can't be that and &s[0] is fine.

## ph4r05 | 2021-01-13T13:58:38+00:00
@prometheus-aflame thanks for the report anyway. We found code that might cause the crashes:
-  https://github.com/monero-project/monero/pull/7306 
- https://github.com/monero-project/monero/pull/7317

We should also more emphasise in the Troubleshooting that it is better to use Trezor exclusively, i.e., close all other wallets which may be using it to avoid problems and add info on restarting Trezor Bridge.

Thanks!

# Action History
- Created by: ghost | 2021-01-10T18:19:15+00:00
- Closed at: 2021-01-10T21:13:38+00:00
