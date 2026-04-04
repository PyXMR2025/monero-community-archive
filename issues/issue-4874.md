---
title: git submodule status is missing in the tar.gz source code
source_url: https://github.com/monero-project/monero/issues/4874
author: lcgogo
assignees: []
labels:
- invalid
created_at: '2018-11-20T08:08:35+00:00'
updated_at: '2018-11-25T19:00:59+00:00'
type: issue
status: closed
closed_at: '2018-11-25T19:00:59+00:00'
---

# Original Description
I want to build from source code https://github.com/monero-project/monero/archive/v0.13.0.4.tar.gz

git submodule status
shows nothing
and git submodule init and update failed.

I tried to download the .gitmodules from https://github.com/monero-project/monero/blob/master/.gitmodules but no works.

I can find there are 4 submodules git clone && git submodule status

root@sv:~/monero-build/monero# git submodule status
-6b9b73a567e351b844f96c077f7b752ea92e298a external/miniupnp
-129d19ba7f496df5e33658527a7158c79b99c21c external/rapidjson
-588f8e03f5ac111adf719f0a437de67481a26aed external/trezor-common
-7f23967954736dcaa366806b9eaba7e2bdfede11 external/unbound

If I use git submodule add the 4 submodules, the submodule commits are not same with 
git clone && git submodule status

root@sv:~/monero-build/monero-0.13.0.4# git submodule status
 27d34098a331e4468a02adf65108bf74cae39ed7 external/miniupnp (heads/master)
 67fac85e96220f69076121d569abd15471abb6bf external/rapidjson (v1.1.0-434-g67fac85)
 016a71c6d0df190bec3cbd4eb26e09a1ab748c73 external/trezor-common (heads/master)
 6af71187373ac87cbb84e123263058e418ed62fe external/unbound (heads/master)

Is there any method to get the git submodule status from https://github.com/monero-project/monero/archive/v0.13.0.4.tar.gz

# Discussion History
## moneromooo-monero | 2018-11-20T10:10:26+00:00
I don't get it. If you want the git machinery, why do you specifically get the one without it ?


## moneromooo-monero | 2018-11-25T18:52:24+00:00
It's not supposed to have it.
If you want the git metadata, use git.

+invalid


# Action History
- Created by: lcgogo | 2018-11-20T08:08:35+00:00
- Closed at: 2018-11-25T19:00:59+00:00
