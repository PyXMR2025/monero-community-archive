---
title: Dockerfile not working with git submodule init
source_url: https://github.com/monero-project/monero/issues/5687
author: VisionsOfDrifting
assignees: []
labels: []
created_at: '2019-06-22T21:12:30+00:00'
updated_at: '2019-09-12T09:57:27+00:00'
type: issue
status: closed
closed_at: '2019-08-31T06:16:30+00:00'
---

# Original Description
Not sure if I'm the only one still running into these problems. I've just done a fresh clone of the repo and ran the docker file as in the instructions
`cd monero && docker build -t monero .`

I am running in branch "release-v0.14". I have tried in master as well, but I get the same error.

My build fails towards the end of the file
`Step 47/57 : RUN set -ex &&     git submodule init && git submodule update &&     rm -rf build &&     if [ -z "$NPROC" ] ;     then make -j$(nproc) release-static ;     else make -j$NPROC release-static ;     fi
 ---> Running in d493bbfb76a7
+ git submodule init
+ git submodule update
fatal: Not a git repository: /home/user/monero/.git/modules/external/miniupnp
Unable to find current revision in submodule path 'external/miniupnp'
`

Wondering if anyone else is experiencing this and if there are any solutions? I don't have much experience with git submodules.

# Discussion History
## jtgrassie | 2019-06-24T05:02:09+00:00
I have seen a similar error before and fixed with a `git submodule sync`. I don't use the Docker image so not sure how it fix it via docker.

## jtgrassie | 2019-06-25T19:11:59+00:00
> It's essentially the same within docker (just a virtual-machine, created on-the-fly)

If it's being created fresh, on-the-fly as you say, then a sync should not be needed. This is what I'm trying to get at.

I have needed to do a sync before, but not w.r.t. docker. And the docker file itself should not require a sync, if its a fresh run that is. This is because I assume it's created from scratch, thus a submodule init & update would never have a problem. You only need to sync when your making changes in a submodule already pulled. There must be some way of blitzing whatever state the user has and doing a fresh build (which should succeed) or a way of fixing the current build by running git submodule sync.

## hyc | 2019-06-25T19:49:33+00:00
Agree with @jtgrassie there should be no need for a submodule sync here.

## VisionsOfDrifting | 2019-06-26T15:17:22+00:00
I tried adding the git submodule sync and I get the same error "fatal: Not a git repository"

I'm trying to run this on my laptop. Linux Mint 18.2 (Basically ubuntu 16.04), Intel i7, Docker version 18.09.6, build 481bc77

If I try running the last temporary container before the docker build fails and then running the commands manually I get the same error:

root@bd290d0b53e4:/src# ls -a
.               
.gitmodules
CONTRIBUTING.md  
README.i18n.md  
external  
translations
..              
.travis.yml           
 Dockerfile      
 README.md      
 include  
 utils
.git            
ANONYMITY_NETWORKS.md  
Doxyfile        
build
.gitattributes  
CMakeLists.txt         
LICENSE          
cmake           
src
.gitignore      
CMakeLists_IOS.txt     
Makefile         
contrib         
tests
root@bd290d0b53e4:/src# git init
Reinitialized existing Git repository in /src/.git/
root@bd290d0b53e4:/src# git submodule update
fatal: Not a git repository: /home/user/Desktop/Software/monero/.git/modules/external/miniupnp
Unable to find current revision in submodule path 'external/miniupnp'
root@bd290d0b53e4:/src# 


## ghost | 2019-06-27T19:32:48+00:00
You typed `git init` instead of `git submodules init`.

Anyway, can you copy the output, like this (this is from a ubuntu 18.04 VirtualBox instance, where again it works)

```
Step 47/57 : RUN set -ex &&     git submodule init && git submodule update &&     rm -rf build &&     if [ -z "$NPROC" ] ;     then make -j$(nproc) release-static ;     else make -j$NPROC release-static ;     fi
 ---> Running in af70c4576acc
+ git submodule init
Submodule 'external/miniupnp' (https://github.com/monero-project/miniupnp) registered for path 'external/miniupnp'
Submodule 'external/rapidjson' (https://github.com/Tencent/rapidjson) registered for path 'external/rapidjson'
Submodule 'external/trezor-common' (https://github.com/trezor/trezor-common.git) registered for path 'external/trezor-common'
Submodule 'external/unbound' (https://github.com/monero-project/unbound) registered for path 'external/unbound'
+ git submodule update
Cloning into 'external/miniupnp'...
Submodule path 'external/miniupnp': checked out '4c700e09526a7d546394e85628c57e9490feefa0'
Cloning into 'external/rapidjson'...
Submodule path 'external/rapidjson': checked out '129d19ba7f496df5e33658527a7158c79b99c21c'
Cloning into 'external/trezor-common'...
Submodule path 'external/trezor-common': checked out 'cb238cb1f134accc4200217d9511115a8f61c6cb'
Cloning into 'external/unbound'...
Submodule path 'external/unbound': checked out '0f6c0579d66b65f86066e30e7876105ba2775ef4'
+ rm -rf build
```

## toints | 2019-09-12T09:57:27+00:00
rm -rf external/miniupnp
git submodule update

# Action History
- Created by: VisionsOfDrifting | 2019-06-22T21:12:30+00:00
- Closed at: 2019-08-31T06:16:30+00:00
