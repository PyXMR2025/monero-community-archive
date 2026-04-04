---
title: blockchain download obsolete?
source_url: https://github.com/monero-project/monero-site/issues/1011
author: Sunray-Nucleon
assignees: []
labels:
- performance
- wontfix
created_at: '2020-05-25T18:23:08+00:00'
updated_at: '2020-05-27T20:08:51+00:00'
type: issue
status: closed
closed_at: '2020-05-27T15:17:00+00:00'
---

# Original Description
It's a while ago i've been trying to download the blockchain at https://web.getmonero.org/downloads/#blockchain (https://downloads.getmonero.org/blockchain.raw) - I could never successfully download the whole file. It did not work (abort at some random point) with Firefox nor Chromium and also not with download-manager. I am the only one who can not download this whole file? If not, can we disable this option and save resources?

# Discussion History
## erciccione | 2020-05-26T08:58:34+00:00
There were some problems when downloading anything from the website not long ago, but the issue was fixed. Could you try to download the raw blockchain now and see if it fails?

## Sunray-Nucleon | 2020-05-26T14:05:53+00:00
It is still breaking.

## erciccione | 2020-05-26T15:01:44+00:00
Seems to be working fine for me. Are you sure it's not a connection problem? or something related to your browser? The file it's big and can be that it fails during the download, especially on slow connections.

## Sunray-Nucleon | 2020-05-26T15:21:30+00:00
I am on wired connection and more than 50 mBit connection, there was no connection abort, i am using internet/streaming parallel. Still i am surprised how fast it was breaking today already after 4GB. The last times, several month ago on a raspi it was usually breaking after more than 70%

## Samuel-Pedraza | 2020-05-26T16:58:48+00:00
Just to jump in here - I saw this issue yesterday and tested by downloading the entire blockchain from the provided link, and it downloaded completely over the period of about 12 hrs.

## Sunray-Nucleon | 2020-05-26T19:00:05+00:00
Thank you for this feedback, whats your location? Github says you are in USA. Can maybe someone try from central europe? I get repeatedly abortion and could never successful download the whole file.

## Samuel-Pedraza | 2020-05-27T03:10:36+00:00
Yes, I am US based, West Coast. I guess perhaps we can try using a VPN to try it from there.

## erciccione | 2020-05-27T07:27:23+00:00
I tried multiple tests and they all succeeded with no issues. I used two VPS from central europe. @Sunray-Nucleon I think the problem is on your side.

## Sunray-Nucleon | 2020-05-27T15:17:00+00:00
True, after installing a amplifier (house-distributor) in my room between wall and modem i could download it. (Data over cable - Docsis 3.1) Thanks for your efforts, glad to have it resolved. It was my end which i could'nt imagine after many attempts.

# Action History
- Created by: Sunray-Nucleon | 2020-05-25T18:23:08+00:00
- Closed at: 2020-05-27T15:17:00+00:00
