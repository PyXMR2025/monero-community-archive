---
title: Update to be compatible with Node.js 18 LTS
source_url: https://github.com/monero-project/monero/issues/8646
author: woodser
assignees: []
labels: []
created_at: '2022-11-18T21:40:07+00:00'
updated_at: '2022-12-08T09:14:50+00:00'
type: issue
status: closed
closed_at: '2022-12-08T09:14:50+00:00'
---

# Original Description
This issue requests updating monero-project to be compatible with NodeJS 18 LTS so that downstream clients may update to the latest LTS version.

Currently, monero-project is incompatible with NodeJS 17+ LTS due to the way IPv4 and IPv6 addresses are handled. [See related issue](https://github.com/nodejs/node/issues/40702#issuecomment-958143154).

# Discussion History
## jeffro256 | 2022-11-21T01:25:31+00:00
How is the current Monero C++ code affected by this? The `monero` core repo uses `libunbound` for DNS resolution which (correct me if I'm wrong) is unrelated to whatever Node.js is doing. 

## woodser | 2022-11-21T12:06:40+00:00
If I understand correctly from [this comment](https://github.com/nodejs/node/issues/40702#issuecomment-958143154), Node 16's DNS lookup returns IPv4 addresses, which works with localhost in monero-project, but Node 17+'s DNS lookup switches to IPv6, which breaks with localhost since upstream monero-project binds to IPv4 127.0.0.1. In that case, the resolution would be to improve IPv6 support in monero-project, but I'm not clear what code this affects.

## jtgrassie | 2022-11-26T22:24:43+00:00
@woodser this is a nodejs issue (a change to the default resolution), not a Monero issue. Monero binds to 127.0.0.1 by default for RPC, but you can always bind to a specific IPv6 address with `--rpc-bind-ipv6-address`. Alternatively, in your nodejs code, use 127.0.0.1 as the host (instead of trying to resolve "localhost") or change your nodejs code to specifically lookup the IPv4 address.

## Spederan | 2022-12-01T02:12:15+00:00
> @woodser this is a nodejs issue (a change to the default resolution), not a Monero issue. Monero binds to 127.0.0.1 by default for RPC, but you can always bind to a specific IPv6 address with `--rpc-bind-ipv6-address`. Alternatively, in your nodejs code, use 127.0.0.1 as the host (instead of trying to resolve "localhost") or change your nodejs code to specifically lookup the IPv4 address.

i disagree that this is a "nodejs issue". 

It should be the job of Monero-Project to be compatible with NodeJS, not the job of NodeJS to be compatible with Monero-Project. Ipv4 addresses are also becoming old news, everyone should be making plans to switch to ipv6.



## jtgrassie | 2022-12-01T02:35:02+00:00
@Spederan
> It should be the job of Monero-Project to be compatible with NodeJS

Monero _is already_ compatible with nodejs (and anything else which wants to call it's RPC interface). That's the point. Monero RPC listens on (by default) 127.0.0.1. Regardless of you local setup (which defines what the domain name "localhost" resolves to), and regardless of how anything else (like nodejs) chooses to resolve "localhost". 

nodejs changed its preference to return the IPv6 (if both are defined), but you can still ask for resolution to return the IPv4 address instead. Hence this is absolutely NOT a Monero compatibility issue. Your (and woodser's) complaint is essentially "I want to use 'localhost' in nodejs, instead of '127.0.0.1', but nodejs has started to prefer to return the IPv6 address for localhost, instead of the IPv4 address like it used to. Please fix Monero", which is wrong. Change your code, or change you system config, or change your Monero default config.

## woodser | 2022-12-01T09:24:42+00:00
> Monero is already compatible with nodejs (and anything else which wants to call it's RPC interface). That's the point. Monero RPC listens on (by default) 127.0.0.1. Regardless of you local setup (which defines what the domain name "localhost" resolves to), and regardless of how anything else (like nodejs) chooses to resolve "localhost".

Makes sense to me.

@Spederan You should be able to upgrade to latest Node.js LTS either by using 127.0.0.1 explicitly or by passing the `-no-experimental-fetch` flag to Node.js, in which case this issue can be closed. Basically, monero-project should not assume localhost resolves to 127.0.0.1.

## Spederan | 2022-12-07T19:50:23+00:00
> @Spederan
> 
> > It should be the job of Monero-Project to be compatible with NodeJS
> 
> Monero _is already_ compatible with nodejs (and anything else which wants to call it's RPC interface). That's the point. Monero RPC listens on (by default) 127.0.0.1. Regardless of you local setup (which defines what the domain name "localhost" resolves to), and regardless of how anything else (like nodejs) chooses to resolve "localhost".
> 
> nodejs changed its preference to return the IPv6 (if both are defined), but you can still ask for resolution to return the IPv4 address instead. Hence this is absolutely NOT a Monero compatibility issue. Your (and woodser's) complaint is essentially "I want to use 'localhost' in nodejs, instead of '127.0.0.1', but nodejs has started to prefer to return the IPv6 address for localhost, instead of the IPv4 address like it used to. Please fix Monero", which is wrong. Change your code, or change you system config, or change your Monero default config.

I am literally following the example listed on the github repository. Nowhere am I using localhost. I have no idea where you are getting that from.

![monero2](https://user-images.githubusercontent.com/117870702/206281260-d793b0a0-73a7-456f-aa79-962622221313.png)

![monero1](https://user-images.githubusercontent.com/117870702/206281287-b1ae2f50-cc10-44ce-bb4b-099759077d02.png)


## jtgrassie | 2022-12-08T02:59:58+00:00
@Spederan 
> I am literally following the example listed on the github repository....

You're literally relying on the _defaults_, which use localhost. Your issue has nothing to do with _this_ project but rather your lack of understanding how to use another project.

## jtgrassie | 2022-12-08T03:00:49+00:00
This issue needs closing as invalid.

## woodser | 2022-12-08T09:14:49+00:00
@Spederan I can investigate the issue of creating a keys-only wallet with Node 18 separately.

In the meantime, you reported success using the `-no-experimental-fetch` passed to Node.

Either way, closing this issue as unrelated to monero-project itself. If we identify something specific which needs updated, we can open a new issue for that.

# Action History
- Created by: woodser | 2022-11-18T21:40:07+00:00
- Closed at: 2022-12-08T09:14:50+00:00
