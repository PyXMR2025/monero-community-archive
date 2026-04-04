---
title: '[Ledger] Rejecting view key export'
source_url: https://github.com/monero-project/monero-gui/issues/2027
author: roudaille
assignees: []
labels:
- invalid
created_at: '2019-03-21T15:43:30+00:00'
updated_at: '2019-03-28T09:00:39+00:00'
type: issue
status: closed
closed_at: '2019-03-28T09:00:39+00:00'
---

# Original Description
choosing this option from the hardware wallet doesn't work resulting in a sync loop.
Got the wallet sync with Approving view key export but less secure.
![Capture du 2019-03-21 11-48-57](https://user-images.githubusercontent.com/30194066/54764566-574ac000-4bf8-11e9-90ed-6b0a4ce264ec.png)


# Discussion History
## selsta | 2019-03-21T15:45:24+00:00
Can you explain the sync loop in more detail? If you aren’t exporting the view key, it’ll take time.

## roudaille | 2019-03-21T16:00:20+00:00
Hey,

when rejecting view key export, locking/unlocking the device is ending up
with an error (few hours before that). In the mean time, no sync for the
daemon and wallet.
The logs show:

2019-03-21 15:56:27.437     7fb942188700 DEBUG device.ledger
src/device/device_ledger.cpp:216 Ask for LOCKING for device Ledger in
thread
2019-03-21 15:56:27.437     7fb9218e9700 DEBUG device.ledger
src/device/device_ledger.cpp:260 CMD  : 02 32 00 00 41
006029751925d3e8fe55633b3c6eb53e194bbe439a3ac8b7b2f593dd98575f9e1a0000000000000000000000000000000000000000000000000000000000000000
2019-03-21 15:56:27.649     7fb9218e9700 DEBUG device.ledger
src/device/device_ledger.cpp:270 RESP : 9000
1654e6287de7461b45787fc6fb2d223610325ddd6c7fae7ec0626fe01a7f4e44
2019-03-21 15:56:27.649     7fb9218e9700 DEBUG device.ledger
src/device/device_ledger.cpp:236 Ask for UNLOCKING for device Ledger in
thread
2019-03-21 15:56:27.649     7fb9218e9700 DEBUG device.ledger
src/device/device_ledger.cpp:240 Device Ledger UNLOCKed
2019-03-21 15:56:27.649     7fb9218e9700 DEBUG device.ledger
src/device/device_ledger.cpp:216 Ask for LOCKING for device Ledger in
thread
2019-03-21 15:56:27.649     7fb94943d700 DEBUG device.ledger
src/device/device_ledger.cpp:218 Device Ledger LOCKed
2019-03-21 15:56:27.649     7fb94943d700 DEBUG device.ledger
src/device/device_ledger.cpp:260 CMD  : 02 32 00 00 41
003ed56cc25d1bdee187981e45282d848436cc17eae2fd2b0f0d61f6c77b7fe7760000000000000000000000000000000000000000000000000000000000000000
2019-03-21 15:56:27.861     7fb94943d700 DEBUG device.ledger
src/device/device_ledger.cpp:270 RESP : 9000
2843ccecb8d2023d71bc9dee95afc1fcf16a022ae2d1c3d322f6e366a0cc1b13
2019-03-21 15:56:27.861     7fb94943d700 DEBUG device.ledger
src/device/device_ledger.cpp:236 Ask for UNLOCKING for device Ledger in
thread
2019-03-21 15:56:27.861     7fb94943d700 DEBUG device.ledger
src/device/device_ledger.cpp:240 Device Ledger UNLOCKed
2019-03-21 15:56:27.861     7fb94943d700 DEBUG device.ledger
src/device/device_ledger.cpp:216 Ask for LOCKING for device Ledger in
thread
2019-03-21 15:56:27.861     7fb948c3c700 DEBUG device.ledger
src/device/device_ledger.cpp:218 Device Ledger LOCKed
2019-03-21 15:56:27.861     7fb948c3c700 DEBUG device.ledger
src/device/device_ledger.cpp:260 CMD  : 02 32 00 00 41
008b808ed8c56a4af57489850c638b70177f57f8b4638998c0734751d93570fae30000000000000000000000000000000000000000000000000000000000000000
2019-03-21 15:56:28.074     7fb948c3c700 DEBUG device.ledger
src/device/device_ledger.cpp:270 RESP : 9000
8968ad1349afb79ace535a9b401faa7f3f3ed199694f745996aed3695442cdba
2019-03-21 15:56:28.074     7fb948c3c700 DEBUG device.ledger
src/device/device_ledger.cpp:236 Ask for UNLOCKING for device Ledger in
thread
2019-03-21 15:56:28.074     7fb948c3c700 DEBUG device.ledger
src/device/device_ledger.cpp:240 Device Ledger UNLOCKed
2019-03-21 15:56:28.074     7fb948c3c700 DEBUG device.ledger
src/device/device_ledger.cpp:216 Ask for LOCKING for device Ledger in
thread
2019-03-21 15:56:28.074     7fb922ced700 DEBUG device.ledger
src/device/device_ledger.cpp:218 Device Ledger LOCKed
2019-03-21 15:56:28.074     7fb922ced700 DEBUG device.ledger
src/device/device_ledger.cpp:260 CMD  : 02 32 00 00 41
00ea87c840e0ff4448ea81083f8a2d83f8e5bc3bc8b5ce91bd153a7c6cbe2326260000000000000000000000000000000000000000000000000000000000000000
2019-03-21 15:56:28.287     7fb922ced700 DEBUG device.ledger
src/device/device_ledger.cpp:270 RESP : 9000
f12812095d46363cf20a2ee92195433d43c32de10279840



Le jeu. 21 mars 2019 à 16:45, selsta <notifications@github.com> a écrit :

> Can you explain the sync loop in more detail? If you aren’t exporting the
> view key, it’ll take time.
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero-gui/issues/2027#issuecomment-475284707>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/Acy5khXIhbQ5sFfH6ZvKcRcpN0bmTpd9ks5vY6kWgaJpZM4cBvpu>
> .
>


## dEBRUYNE-1 | 2019-03-21T18:58:40+00:00
A few tips:

1. Make sure you use Ledger Monero app v1.2.2

2. Make sure you use Ledger Live firmware v1.5.5

3. Make sure you use GUI v0.14.0.0

4. Make sure Ledger live is closed. 

## roudaille | 2019-03-21T20:25:34+00:00
tips 1 to 4 are ok on my side.
I am using GUI on Linux. May it be some udev rules not working with this mode? 

## dEBRUYNE-1 | 2019-03-22T07:12:27+00:00
Did you properly set them up?

https://github.com/LedgerHQ/udev-rules/blob/master/add_udev_rules.sh

## roudaille | 2019-03-22T07:37:59+00:00
yep, used this:
wget -q -O -
https://raw.githubusercontent.com/LedgerHQ/udev-rules/master/add_udev_rules.sh
| sudo bash

Le ven. 22 mars 2019 à 08:12, dEBRUYNE-1 <notifications@github.com> a
écrit :

> Did you properly set them up?
>
> https://github.com/LedgerHQ/udev-rules/blob/master/add_udev_rules.sh
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero-gui/issues/2027#issuecomment-475516649>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/Acy5kmOiO0MznqPEand_gNoUgq0V4nxXks5vZIJegaJpZM4cBvpu>
> .
>


## selsta | 2019-03-22T07:38:34+00:00
Can you try the CLI wallet? This doesn’t seem GUI related.

## roudaille | 2019-03-27T21:03:24+00:00
Hi,

same result with the CLI: ./monero-wallet-cli
--wallet-file=/home/X/Monero/wallets/X/X --daemon-address=
192.168.0.210:18081 --trusted-daemon --log-level=4

2019-03-27 21:01:13.669     7ffae1c92700 DEBUG device.ledger
src/device/device_ledger.cpp:270 RESP : 9000
6b90f144ff95a1649a2e53761f482321d2b7e5d4a6c9dd1bdaffc7bea408e472
2019-03-27 21:01:13.669     7ffae1c92700 DEBUG device.ledger
src/device/device_ledger.cpp:236 Ask for UNLOCKING for device Ledger in
thread
2019-03-27 21:01:13.669     7ffae1c92700 DEBUG device.ledger
src/device/device_ledger.cpp:240 Device Ledger UNLOCKed
2019-03-27 21:01:13.669     7ffae1c92700 DEBUG device.ledger
src/device/device_ledger.cpp:216 Ask for LOCKING for device Ledger in
thread
2019-03-27 21:01:13.669     7ffae1290700 DEBUG device.ledger
src/device/device_ledger.cpp:218 Device Ledger LOCKed
2019-03-27 21:01:13.669     7ffae1290700 DEBUG device.ledger
src/device/device_ledger.cpp:260 CMD  : 02 32 00 00 41
0091d6308eaefaecfa0a40ab849aeaf7a158ca285f0f3116961504d54e444f11c70000000000000000000000000000000000000000000000000000000000000000
2019-03-27 21:01:13.882     7ffae1290700 DEBUG device.ledger
src/device/device_ledger.cpp:270 RESP : 9000
14b78221007f8eb797787ec1d72a3b6aea9638ecaad9c6786a05b7be30fd4c62
2019-03-27 21:01:13.882     7ffae1290700 DEBUG device.ledger
src/device/device_ledger.cpp:236 Ask for UNLOCKING for device Ledger in
thread
2019-03-27 21:01:13.882     7ffae1290700 DEBUG device.ledger
src/device/device_ledger.cpp:240 Device Ledger UNLOCKed
2019-03-27 21:01:13.882     7ffae1290700 DEBUG device.ledger
src/device/device_ledger.cpp:216 Ask for LOCKING for device Ledger in
thread
2019-03-27 21:01:13.882     7ffae5c54bc0 DEBUG device.ledger
src/device/device_ledger.cpp:218 Device Ledger LOCKed
2019-03-27 21:01:13.883     7ffae5c54bc0 DEBUG device.ledger
src/device/device_ledger.cpp:260 CMD  : 02 32 00 00 41
0055795f9031da9392f1737570d45db89359f3595728d04413cf45a2fc9e1706500000000000000000000000000000000000000000000000000000000000000000
2019-03-27 21:01:14.095     7ffae5c54bc0 DEBUG device.ledger
src/device/device_ledger.cpp:270 RESP : 9000
86c70e59ba16c48ade9ba9cecb51f02a504162bb3633199e1c3cbcbeac1be433
2019-03-27 21:01:14.095     7ffae5c54bc0 DEBUG device.ledger
src/device/device_ledger.cpp:236 Ask for UNLOCKING for device Ledger in
thread
2019-03-27 21:01:14.095     7ffae5c54bc0 DEBUG device.ledger
src/device/device_ledger.cpp:240 Device Ledger UNLOCKed
2019-03-27 21:01:14.095     7ffae5c54bc0 DEBUG device.ledger
src/device/device_ledger.cpp:216 Ask for LOCKING for device Ledger in
thread
2019-03-27 21:01:14.096     7ffae2b95700 DEBUG device.ledger
src/device/device_ledger.cpp:218 Device Ledger LOCKed
2019-03-27 21:01:14.096     7ffae2b95700 DEBUG device.ledger
src/device/device_ledger.cpp:260 CMD  : 02 32 00 00 41
001b521e0809d6daa8da210139679c44c6f434dfde84b518a145f45d4ca358e2000000000000000000000000000000000000000000000000000000000000000000
2019-03-27 21:01:14.310     7ffae2b95700 DEBUG device.ledger
src/device/device_ledger.cpp:270 RESP : 9000
9f76a3c49cea29cba639b099b7761e6fe5de6c04e0de6b7278de7856f314eea3
2019-03-27 21:01:14.310     7ffae2b95700 DEBUG device.ledger
src/device/device_ledger.cpp:236 Ask for UNLOCKING for device Ledger in
thread
2019-03-27 21:01:14.310     7ffae2b95700 DEBUG device.ledger
src/device/device_ledger.cpp:240 Device Ledger UNLOCKed
2019-03-27 21:01:14.310     7ffae2694700 DEBUG device.ledger
src/device/device_ledger.cpp:218 Device Ledger LOCKed
2019-03-27 21:01:14.310     7ffae2694700 DEBUG device.ledger
src/device/device_ledger.cpp:260 CMD  : 02 32 00 00 41
00cb2f14eb3e631062a8a80d18eded69d74eefb6ba918274417de2ad084ad0a2150000000000000000000000000000000000000000000000000000000000000000

Le ven. 22 mars 2019 à 08:38, selsta <notifications@github.com> a écrit :

> Can you try the CLI wallet? This doesn’t seem GUI related.
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero-gui/issues/2027#issuecomment-475522139>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/Acy5kvdxkEaxScMwOn-eUscnhsPgyxjrks5vZIh8gaJpZM4cBvpu>
> .
>


## selsta | 2019-03-28T08:56:43+00:00
Thank you for clarifying. As this isn’t GUI related, I’ll close this. You can open an new issue here:

https://github.com/monero-project/monero/issues/

+invalid

# Action History
- Created by: roudaille | 2019-03-21T15:43:30+00:00
- Closed at: 2019-03-28T09:00:39+00:00
