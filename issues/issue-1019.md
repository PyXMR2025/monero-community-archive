---
title: Requesting a getmonero.org subdomain for Librejo
source_url: https://github.com/monero-project/meta/issues/1019
author: SyntheticBird45
assignees: []
labels: []
created_at: '2024-06-04T17:05:25+00:00'
updated_at: '2024-06-14T23:18:03+00:00'
type: issue
status: closed
closed_at: '2024-06-14T23:18:02+00:00'
---

# Original Description
I'll try to be short.

I've recently setup a [Forgejo](https://forgejo.org/) instance at http://librejojyvetb6pwx3r23yigq5eeuwhhev2vm5hkfomhgdn7g4xpx3ad.onion in an attempt to provide a public mirror and backups for all monero projects. 

There has been discussions around github takedown at some point and I didn't found any complete answer. Gitlab free tier is apparently unable to make pulling mirrors. So repo.getmonero.org can't serve as a public backup. At  the end I decided to make a forgejo instance directly myself. 

Currently, only monero-project organization and cuprate is mirrored. I plan on adding more organization and repositories but what I would prefer is devs personal repositories being mirrors (to save ongoing work). In order to do so, I need to setup Github Oauth2 on the instance, which requires me to have a domain name and TLS certificate. This way core devs or community devs can quickly log in with their github account and configure their mirrors themselves

Since I can't buy one I'm requesting a subdomain here, in the hope that this project does interest the community.

More infos:
- Repositories are synced every 8 hours
- I can discuss the server hardening in private
- I plan on also hosting it on i2p

# Discussion History
## SyntheticBird45 | 2024-06-14T23:18:02+00:00
Update: Librejo is now up and running at librejo.monerodevs.org.

# Action History
- Created by: SyntheticBird45 | 2024-06-04T17:05:25+00:00
- Closed at: 2024-06-14T23:18:02+00:00
