---
title: cleanup folders. only have the executable in root folder and 1 or 2 subdirectories
  to make it easier for beginners
source_url: https://github.com/monero-project/monero-gui/issues/1363
author: krtschmr
assignees: []
labels:
- resolved
created_at: '2018-04-30T04:03:36+00:00'
updated_at: '2019-07-04T06:54:44+00:00'
type: issue
status: closed
closed_at: '2019-07-04T06:54:44+00:00'
---

# Original Description
just introduced monero to 2 different friends who are not tech-savy. both had headaches with all the folders and files. one even asked me which file he needs to copy because he wants to delete all others.

suggestion:

having a folder structure where we only have the executable as a file in the root tree and all other files are in 1 (max 2) subfolder. 

    /monero-gui-v0.12.0.0
      - wallets (directory for our wallets)
      - monero (monerod, monerowalletcli, monerorpc and blockchainimport can be in there)
      - misc (all files that are now in root can go into )
      - monero-wallet-gui.exe



now it would be clear and easy for everybody to start with monero

# Discussion History
## rbrunner7 | 2018-05-06T06:39:49+00:00
That "mess" of directories mostly comes from Qt and its deploy mechanism. Changing it would be probably dangerous and error-prone.

I don't think there is much to delete, most of those files are probably needed, and for the rest nearly impossible to prove conclusively that under no circumstances occuring while using the GUI wallet those files are needed. (Qt loads some files not already at startup, but dynamically when needed, as far as I know.)

IMHO the right way to make life easier for beginners is finally bringing the Windows installer into service that I built and that is waiting already for quite some time ...

## dEBRUYNE-1 | 2019-07-04T06:41:25+00:00
GUI v0.14.1.0 now contains a single executable and no other files (except for one DLL that is needed for the graphic fallback and a script that can be used as last resort (with respect to graphic fallback)). I am thus going to mark this as resolved. 

## dEBRUYNE-1 | 2019-07-04T06:41:30+00:00
+resolved

# Action History
- Created by: krtschmr | 2018-04-30T04:03:36+00:00
- Closed at: 2019-07-04T06:54:44+00:00
