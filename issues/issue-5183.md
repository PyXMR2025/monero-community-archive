---
title: Always tag correctly latest release on github
source_url: https://github.com/monero-project/monero/issues/5183
author: gituser
assignees: []
labels: []
created_at: '2019-02-22T14:10:13+00:00'
updated_at: '2019-02-26T14:12:30+00:00'
type: issue
status: closed
closed_at: '2019-02-26T14:12:29+00:00'
---

# Original Description
Seems it is a regular pattern that you release a new version and don't tag it on github as the latest release.

![example](https://i.imgur.com/5CAys6Y.png)

Here are older examples: https://github.com/monero-project/monero/issues/4497#issuecomment-428337922

Right now the situation is the same:
* Latest release is `v0.14.0.0`
* But on releases page and via API: latest release is `v0.13.0.4` - https://github.com/monero-project/monero/releases

As a good practice please **ALWAYS** make sure to match latest release to the latest available tag (of course matching should be done only if tag is considered to be stable, otherwise you could also use beta functionality on github).

I'm sure many users are using Github's API to poll latest release info and might miss it, because you never tag it properly.

Thanks!

# Discussion History
## dEBRUYNE-1 | 2019-02-22T15:48:13+00:00
Paging @fluffypony.

## gituser | 2019-02-23T10:58:30+00:00
Basically you've just created empty tag without description and release assets, that's why it's not marked as the latest release.

Here is a guide in case you're having an issue with resolving this:

https://help.github.com/en/articles/creating-releases 
https://help.github.com/en/articles/creating-releases#automatically-creating-releases
(you can use automatic section of that guide)

https://github.community/t5/How-to-use-Git-and-GitHub/Why-last-release-is-not-marked-as-quot-latest-release-quot/td-p/1762

## fluffypony | 2019-02-23T16:03:01+00:00
@gituser the release isn't ready. Creating the tag is the first step in making sure the release is ready. Unfortunately, due to the sensitive nature of security software, building and ensuring that nothing is tampered with is not instantaneous.

## gituser | 2019-02-23T19:43:15+00:00
@fluffypony cheers for the explanation.

The reason I've asked because earlier you've announced that there will be new release available and I only noticed new version once I've visited the github's releases page.

Usually I just grab the latest release via API call and check if there is one.

Thank you.

## moneromooo-monero | 2019-02-25T14:05:30+00:00
monerod will tell you when an update is ready (assuming your DNSSEC works).


## gituser | 2019-02-25T14:14:32+00:00
@moneromooo-monero when and where?

## moneromooo-monero | 2019-02-25T15:18:31+00:00
Whenever binaries are ready, and in the monerod stdout.

## moneromooo-monero | 2019-02-25T21:10:23+00:00
Binaries are ready, and monerod should now tell you about it. It checks every 12 hours, so it will take up to 12 hours from now to notify.

## gituser | 2019-02-26T14:12:29+00:00
OK, I can see the latest release has been tagged on github. 

Thanks!

Regarding checking via monerod I also found in the logs:
```
2019-02-26 01:52:12.778	[P2P8]	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:1573	Version 0.14.0.0 of monero for source is available: https://downloads.getmonero.org/source/monero-source-v0.14.0.0.tar.bz2, SHA256 hash 0e8d3ec9b3412a2d0bf36cd545c6b9c53b1628745eba9095f45cd08cc787498
```

but it's not really convinient to parse huge log files in order to find if there is a new release available, instead I check every day via cronjob via Github API.

OK, I'm closing this issue as it has been solved and it seems you're following correct practice.

Thanks again!

# Action History
- Created by: gituser | 2019-02-22T14:10:13+00:00
- Closed at: 2019-02-26T14:12:29+00:00
