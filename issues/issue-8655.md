---
title: 'Can''t create transaction: unexpected error: Call method failed'
source_url: https://github.com/monero-project/monero/issues/8655
author: Janaka-Steph
assignees: []
labels: []
created_at: '2022-11-29T08:58:30+00:00'
updated_at: '2022-12-20T18:36:11+00:00'
type: issue
status: closed
closed_at: '2022-12-20T18:36:11+00:00'
---

# Original Description
I get this error popup `Can't create transaction: unexpected error: Call method failed` when trying to send from Monero GUI (0.18.1.2-release (Qt 5.12.8) / Simple mode) connected to Trezor model T (firmware 2.5.3), on Mac M1.

# Discussion History
## selsta | 2022-11-29T10:15:26+00:00
Can you try to change to advanced mode and manually select a remote node? Here is a tutorial: https://github.com/monero-project/monero-gui/issues/3989#issuecomment-1214412781

Also how many characters does the receiver address have?

## Janaka-Steph | 2022-11-29T11:56:09+00:00
Ok I tried with your node selsta2.featherwallet.net but same error.
The receiver address has 95 chars.

## selsta | 2022-11-29T11:56:58+00:00
When was the last time you were able to transact successfully?

## Janaka-Steph | 2022-11-29T11:58:49+00:00
80 days ago. In the meantime I did a Trezor firmware update and I updated GUI version so it should work if I downgrade as it was, hopefully.

## selsta | 2022-11-29T12:00:38+00:00
monero-gui itself is definitely bug free in this regard, if there are issues it's in the Trezor firmware

You might want to downgrade from firmware 2.5.3 to 2.5.2 and see if it helps.

## Janaka-Steph | 2022-11-29T12:54:00+00:00
I have the same error with 2.5.2 

## selsta | 2022-11-29T12:57:39+00:00
Ok, then the bug likely isn't firmware related.

Try to install or update to the latest version of the Trezor bridge here: https://suite.trezor.io/web/bridge/ and then try again.

## Janaka-Steph | 2022-11-29T13:09:39+00:00
I am on latest version of bridge already.
I was just able to transact using 2.5.2 and reinstalling the same version of Monero GUI 0.18.1.2, BUT not at the first attempt. First I got the same error. Then I have been to settings to check logs, it was empty, log level set to 4. I changed to log level 0 and tried again, and this time it worked. 
I know it's weird but this is what happened. 

My logs are still empty though, making the tx with log level 0 didn't log anything.

## Janaka-Steph | 2022-11-29T13:33:11+00:00
Ok on 2.5.2 it doesn't matter going to Settings before sending the tx. But to send it successfully I have to try multiple times, usually 3 times.

## selsta | 2022-11-29T13:35:39+00:00
Something doesn't add up here.

Only 2.5.2 and 2.5.3 are supported for v0.18. 2.5.1 can't construct transactions that pass the current network rules.

## Janaka-Steph | 2022-11-29T13:36:07+00:00
Sorry that was a typo mistake, I used 2.5.2

## selsta | 2022-11-29T13:36:49+00:00
And when you try to send a smaller amount? Does it work more consistently?

## Janaka-Steph | 2022-11-29T13:49:37+00:00
I was able to transact with 2.5.3 but I have to try a bit more, like 5 or 6 times. Changing the amount doesn't seem to have an effect.
Maybe the device fails to compute some random value? Maybe my device or its cable is damaged? Even tough it's the orginal cable, I did nothing crazy with the device. 

## Janaka-Steph | 2022-11-29T13:50:59+00:00
I would be happy to debug it further but I don't see any logs. Should I try with the CLI ?

## selsta | 2022-11-29T13:53:19+00:00
> I would be happy to debug it further but I don't see any logs.

Try to start monero-wallet-gui from the command line and then set log level 4 by using this command, assuming the app is in your applications folder:

```
/Applications/monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui
```

Also another question, do you have a custom background image set on your Trezor?

## Janaka-Steph | 2022-11-29T14:08:05+00:00
The background image is the original Trezor logo.

Running the GUI from cli, without making any txs I see a bunch of warnings and errors.
```
2022-11-29 13:56:45.093	W Transaction extra has unsupported format: <4057cd06c................56adc>
2022-11-29 13:56:45.297	E Error parsing blocks: Call method failed
```

Logs of a failed tx
```
2022-11-29 14:03:52.181	T Ask for UNLOCKING for device  in thread
2022-11-29 14:03:52.181	T Device  UNLOCKed
2022-11-29 14:03:52.182	I Decrypted payment ID: <0000000000000000>
2022-11-29 14:03:52.182	D Using v15 rules
2022-11-29 14:03:52.223	T READ ENDS: Success. bytes_tr: 479
2022-11-29 14:03:52.223	T http_stream_filter::parse_cached_header(*)
2022-11-29 14:03:52.223	T READ ENDS: Connection err_code 2
2022-11-29 14:03:52.223	T Connection err_code eof.
2022-11-29 14:03:52.223	T Returning false because of wrong state machine. state: 5
2022-11-29 14:03:52.224	E Failed to invoke http request to  /call/85
2022-11-29 14:03:52.224	D startRefresh: refresh started/resumed...
2022-11-29 14:03:52.224	T refreshThreadFunc: refresh lock acquired...
2022-11-29 14:03:52.224	T refreshThreadFunc: m_refreshEnabled: 1
2022-11-29 14:03:52.224	T refreshThreadFunc: m_status: 1
2022-11-29 14:03:52.224	T refreshThreadFunc: m_refreshShouldRescan: 0
2022-11-29 14:03:52.224	T refreshThreadFunc: refreshing...
2022-11-29 14:03:52.224	T doRefresh: doRefresh, rescan = 0
2022-11-29 14:03:52.224	T update_pool_state start
2022-11-29 14:03:52.224	D Transaction created
2022-11-29 14:03:52.225	E Can't create transaction:  unexpected error: Call method failed
2022-11-29 14:03:52.226	W "Could not convert argument 0 at"
2022-11-29 14:03:52.226	W 	 "onTransactionCreated@qrc:/main.qml:822"
2022-11-29 14:03:52.226	W "Passing incompatible arguments to C++ functions from JavaScript is dangerous and deprecated."
2022-11-29 14:03:52.226	W "This will throw a JavaScript TypeError in future releases of Qt!"
2022-11-29 14:03:52.266	T READ ENDS: Success. bytes_tr: 794
2022-11-29 14:03:52.267	T http_stream_filter::parse_cached_header(*)
2022-11-29 14:03:52.267	T update_pool_state got pool
2022-11-29 14:03:52.267	T update_pool_state done first loop
2022-11-29 14:03:52.267	T update_pool_state done second loop
```


## selsta | 2022-11-29T14:14:01+00:00
```
2022-11-29 14:03:52.223	T READ ENDS: Connection err_code 2
2022-11-29 14:03:52.223	T Connection err_code eof.
2022-11-29 14:03:52.223	T Returning false because of wrong state machine. state: 5
2022-11-29 14:03:52.224	E Failed to invoke http request to  /call/85
```
Could be relevant. @ph4r05 any idea here?

## Janaka-Steph | 2022-11-29T14:19:26+00:00
I noticed a difference in the json between a failed tx and successful one. 

The failed one has
```
2022-11-29 14:13:23.547	I   "rctsig_prunable": {
2022-11-29 14:13:23.547	I     "nbp": 1,
2022-11-29 14:13:23.547	I     "bpp": [ {
2022-11-29 14:13:23.547	I         "A": "0100000000000000000000000000000000000000000000000000000000000000",
2022-11-29 14:13:23.548	I         "A1": "0100000000000000000000000000000000000000000000000000000000000000",
2022-11-29 14:13:23.548	I         "B": "0100000000000000000000000000000000000000000000000000000000000000",
2022-11-29 14:13:23.548	I         "r1": "0100000000000000000000000000000000000000000000000000000000000000",
2022-11-29 14:13:23.548	I         "s1": "0100000000000000000000000000000000000000000000000000000000000000",
2022-11-29 14:13:23.548	I         "d1": "0100000000000000000000000000000000000000000000000000000000000000",
2022-11-29 14:13:23.548	I         "L": [ "0100000000000000000000000000000000000000000000000000000000000000", "0100000000000000000000000000000000000000000000000000000000000000", "0100000000000000000000000000000000000000000000000000000000000000", "0100000000000000000000000000000000000000000000000000000000000000", "0100000000000000000000000000000000000000000000000000000000000000", "0100000000000000000000000000000000000000000000000000000000000000", "0100000000000000000000000000000000000000000000000000000000000000"
2022-11-29 14:13:23.548	I         ],
2022-11-29 14:13:23.548	I         "R": [ "0100000000000000000000000000000000000000000000000000000000000000", "0100000000000000000000000000000000000000000000000000000000000000", "0100000000000000000000000000000000000000000000000000000000000000", "0100000000000000000000000000000000000000000000000000000000000000", "0100000000000000000000000000000000000000000000000000000000000000", "0100000000000000000000000000000000000000000000000000000000000000", "0100000000000000000000000000000000000000000000000000000000000000"
2022-11-29 14:13:23.548	I         ]
2022-11-29 14:13:23.548	I       }
2022-11-29 14:13:23.548	I     ],
2022-11-29 14:13:23.548	I     "CLSAGs": [ {
2022-11-29 14:13:23.548	I         "s": [ "0100000000000000000000000000000000000000000000000000000000000000", "0100000000000000000000000000000000000000000000000000000000000000", "0100000000000000000000000000000000000000000000000000000000000000", "0100000000000000000000000000000000000000000000000000000000000000", "0100000000000000000000000000000000000000000000000000000000000000", "0100000000000000000000000000000000000000000000000000000000000000", "0100000000000000000000000000000000000000000000000000000000000000", "0100000000000000000000000000000000000000000000000000000000000000", "0100000000000000000000000000000000000000000000000000000000000000", "0100000000000000000000000000000000000000000000000000000000000000", "0100000000000000000000000000000000000000000000000000000000000000", "0100000000000000000000000000000000000000000000000000000000000000", "0100000000000000000000000000000000000000000000000000000000000000", "0100000000000000000000000000000000000000000000000000000000000000", "0100000000000000000000000000000000000000000000000000000000000000", "0100000000000000000000000000000000000000000000000000000000000000"],
2022-11-29 14:13:23.548	I         "c1": "0100000000000000000000000000000000000000000000000000000000000000",
2022-11-29 14:13:23.548	I         "D": "0100000000000000000000000000000000000000000000000000000000000000"
2022-11-29 14:13:23.548	I       }],
```

While a successful tx has proper data
 

## selsta | 2022-11-29T14:22:33+00:00
A couple things to possibly test

- Different USB port
- Different cable
- Different computer

## Janaka-Steph | 2022-11-29T14:24:23+00:00
Yes I will check that.

An other log with more details
`2022-11-29 14:22:59.251	E Failed to invoke http request to  /call/85, wrong response code: 400 Response Body: {"error":"session not found"}`

## Janaka-Steph | 2022-11-29T14:54:53+00:00
"session not found" error should be an other issue.

Also empty data in `rctsig_prunable` is not relevant. The json tx is logged three times, first two with empty data, and third one with proper data. 

Changing the port doesn't help.

## ph4r05 | 2022-11-29T15:25:42+00:00
Thanks for notif! I will check that out. For now, did you pls try the following?
- another usb cable (it is very common culprit)
- close all other apps that might be using Trezor, e.g., TrezorSuite. There can be similar sessions problems in case of more connected apps.

Sorry if this was mentioned already

## Janaka-Steph | 2022-12-12T22:16:50+00:00
I bought a new Model T device just for that issue but they sell it only with a USB C to USB A cable, and my macbook M1 only have USB C ports. Using a hub I get the same issue.

One other log I notice just now on failing txs is `Requested ring size 11 too low, using 16`

## selsta | 2022-12-12T22:17:51+00:00
> One other log I notice just now on failing txs is Requested ring size 11 too low, using 16

That's unrelated and can be ignored.

## Janaka-Steph | 2022-12-19T22:41:55+00:00
@selsta I bought a new quality usb C to usb C cable and I have the same issue. I was able to make a transaction after insisting a lot. So it's not the cable, not the device. Maybe the GUI has not been tested enough on M1? 

## selsta | 2022-12-19T23:06:00+00:00
I have a M1 Mac myself and never ran into this issue so far. What is the current error rate you have? How often does it fail out of 10 transactions?

Also did you make sure that no other Trezor related program is open that could interfere, like suggested by ph4r05?

## Janaka-Steph | 2022-12-19T23:12:55+00:00
It depends. Can be 1/20 or 1/3. It seems to help when I restart the GUI or just reload the wallet.

I always open Trezor Suite on passphrase protected wallet in addition the Monero GUI. I can't access the wallet otherwise. I get `Error opening wallet with password:  Could not connect to the device Trezor` 

## selsta | 2022-12-20T12:48:09+00:00
>I always open Trezor Suite on passphrase protected wallet in addition the Monero GUI.

That's likely the issue here, it will cause interference. Now we have to figure out why you can't open a wallet without having Trezor Suite open.

Can you confirm that Activity Monitor shows a `trezord` process?

## Janaka-Steph | 2022-12-20T13:19:15+00:00
Ok I will check the process. Maybe it's because of the passphrase but works fine without?

## selsta | 2022-12-20T13:39:28+00:00
I use a passphrase myself, it shouldn't be related to your issue.

## Janaka-Steph | 2022-12-20T18:04:01+00:00
trezord process is running only if Trezor Suite is running. Should it always run in the background?

## Janaka-Steph | 2022-12-20T18:36:11+00:00
Alright I installed Trezor Bridge (trezord) 2.0.27 from https://suite.trezor.io/web/bridge/, now it always run in the background and the GUI works flawlessly. That was the issue. 
The bridge is not the same version as the one included in Trezor Suite but doesn't seem to be a problem.
Thank you for your help, hopefully you didn't lose too much time on this :/

# Action History
- Created by: Janaka-Steph | 2022-11-29T08:58:30+00:00
- Closed at: 2022-12-20T18:36:11+00:00
