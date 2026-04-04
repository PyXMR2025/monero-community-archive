---
title: 'airportd[1857]: SecTaskLoadEntitlements failed error=22'
source_url: https://github.com/monero-project/monero-gui/issues/1459
author: Afron-Lysias
assignees: []
labels:
- resolved
created_at: '2018-06-14T08:31:38+00:00'
updated_at: '2019-05-05T07:00:42+00:00'
type: issue
status: closed
closed_at: '2019-05-05T07:00:42+00:00'
---

# Original Description
MacOS 10.11.6 • monero-wallet-gui.app (0.12.0.0) As soon as app starts, I get in system.log almost every 3 sec the following message:
airportd[1857]: SecTaskLoadEntitlements failed error=22
When I quit the gui app and leave the deamon running, the error stops.

I tried to run monero-wallet-gui app with Wi-Fi turned off. The error message didn't appear this time. So I turned Wi-Fi back on, to check again. The following message appeared in system.log:
airportd[74]: WARNING: monero-wallet-gui (28316) is not entitled for com.apple.wifi.scan, temporarily allowing request with background priority —— all entitlement requirements will be strictly enforced in a future release
And the previous error message (airportd[xxxx]: SecTaskLoadEntitlements failed error=22) fills system.log again.

# Discussion History
## pazos | 2018-06-14T13:00:06+00:00
monero-wallet-gui is not a signed osx app. Did you disable the gatekeeper?

## Afron-Lysias | 2018-06-14T13:36:15+00:00
Gatekeeper disabled. Whenever I use ethernet instead of wifi for internet access, there is no similar message in the logs.

## Afron-Lysias | 2018-06-14T13:39:47+00:00
In console.app under the "Diagnostic and Usage Messages" section the following message keeps appearing every few seconds:

14/6/18 16:31:04,783 airportd[65]: com.apple.message.domain: com.apple.wifi.internal.scanning
com.apple.message.error: No Error
com.apple.message.duration: 3
com.apple.message.process_name: monero-wallet-gui
com.apple.message.mac_address: 90:...
SenderMachUUID: 4586AFEE-...


## pazos | 2018-06-21T01:34:58+00:00
I wouldn't care about those verbose messages as long as the application works fine. The gui doesn't need any special entitlements or a entitlement.plist at all and doesn't try to scan your wifi ssids at all.

~~Anyways I can't find  those messages in 10.12.06~~, so it can be related to your system. In that case I would expect any other qt app (that uses the network) firing those messages. In fact any non signed app will fire those messages, see: https://apple.stackexchange.com/questions/237465/what-means-sectaskloadentlitlements-failed-error-22

It can also be any of the system frameworks --or an antivirus-- :p. Check http://newosxbook.com/ent.jl?osVer=OSX&ent=com.apple.wifi.scan 

## selsta | 2019-05-05T01:11:14+00:00
+resolved according to https://github.com/monero-project/monero-gui/issues/2139#issuecomment-489353297

## dEBRUYNE-1 | 2019-05-05T06:51:50+00:00
+resolved

# Action History
- Created by: Afron-Lysias | 2018-06-14T08:31:38+00:00
- Closed at: 2019-05-05T07:00:42+00:00
