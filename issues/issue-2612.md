---
title: HTTP API changes/Query to @xmrig
source_url: https://github.com/xmrig/xmrig/issues/2612
author: vpts1202
assignees: []
labels: []
created_at: '2021-10-01T06:03:36+00:00'
updated_at: '2021-10-16T07:49:54+00:00'
type: issue
status: closed
closed_at: '2021-10-16T07:49:54+00:00'
---

# Original Description
For the time being HTTP API is workable (out of LAN) if IPs workers are statics only. Can you bind it instead of IPs  to access tokens(that’s quick and easy in my opinion) or to the wallet?

HTTP API is very demanded and in fact what you have done is really great, but the absence possibility to use it for dynamic IPs makes it useless.
Thanks


# Discussion History
## Spudz76 | 2021-10-01T14:54:56+00:00
Use a free DDNS provider and an automatic ip-change event script to update your endpoints by name, packages for that are everywhere, every DHCP client knows how to run event hooks.

Or, use OpenVPN to export a virtual LAN then everything has fixed private IPs (192.168.x.x or 10.x or etc) and it will reconnect regardless what real IP the rig has, then hit API through that virtual LAN address.

Probably a few other ways to accomplish it in a BYO method, this isn't the first app where there was extra user-exercise to get it exported to a known endpoint when your networking is wacky (dynamic/portable/proxy IP).

## vpts1202 | 2021-10-02T04:10:44+00:00
Thanks mate. 
Have you ever tried any of your advised s-c. methods by yourself? 

I did.  Not all but “no-ip” service providers and virtual LAN export. At the best it works stochastically with huge hashing native losses and at the worst does not work at all. 

With all my respect to you, all your advises are just theory based on your thoughts and ideas=)

The simplest way if this app devs( most trusted is @xmrig , since this app is their baby) will just replace bind from IPs to  access token. Or just to look around for alternative miner app that is provide fully workable API.



## Spudz76 | 2021-10-02T04:32:39+00:00
Nah, I manage a couple entire mining farms remotely on dynamic IP (although it never really changes unless the cable modem reboots?).  It's been the same IP for like 3 years which is hardly "dynamic" even though it technically is.

And merged two LANs across an OpenVPN bridge over wifi 180ft to another building.  Would be essentially identical, replacing the wifi link with some static IP VPN endpoint/concentrator (cheap VPS shell somewhere).

Could also be done with routing rather than full bridging depending how noisy your lans are with bcast and garbage.

## vpts1202 | 2021-10-03T17:06:32+00:00
> 
> 
> Nah, I manage a couple entire mining farms remotely on dynamic IP (although it never really changes unless the cable modem reboots?). It's been the same IP for like 3 years which is hardly "dynamic" even though it technically is.
> 
> And merged two LANs across an OpenVPN bridge over wifi 180ft to another building. Would be essentially identical, replacing the wifi link with some static IP VPN endpoint/concentrator (cheap VPS shell somewhere).
> 
> Could also be done with routing rather than full bridging depending how noisy your lans are with bcast and garbage.

Good for you=)
However I am looking for practicable solution, therefore I am addressing this query to devs @xmrig



## Spudz76 | 2021-10-03T23:45:10+00:00
Haha good luck with that.  It's cleanly accomplished with existing software and won't be a feature.

## DeeDeeRanged | 2021-10-14T18:28:42+00:00
@vpts1202  Or get a domain name, nowadays dirt cheap, I've got 2 for 10 years for less than €.300. Makes life a lot easier for a lot of things. And bytheway how often does your ISP change your internet IP? Using OpenVPN is not so difficult there are plenty examples on the internet to find depending on your OS.

## vpts1202 | 2021-10-14T20:27:46+00:00
> 
> 
> Haha good luck with that. It's cleanly accomplished with existing software and won't be a feature.

@Spudz76:Finally I have managed to resolve the dynamic IPs issue=)
There is other question arises and I think you should have the answer:
Would it be workable if I will add several workers IPs to http://workers.xmrig.info/ ,in one line separated by commas or underscore,etc., or its workable one-by-one only?

Logically based on this Enhancement : https://github.com/xmrig/xmrig/issues/1772 to add IPs of several workers at once should work, but I think you should know for sure whether it yes/no.
Thanks. 




## Spudz76 | 2021-10-14T20:46:24+00:00
Not that I know of, it does have an export/import feature (to backup your list, for when the browser forgets cookies).  But that provides an encoded blob which is not hand-editable either.

Also I have had lots of problems with recent Chrome and CORS junk, and workers.xmrig.info can't access "local zone" (LAN) hosts because the site is "from the wild Internet zone".  There is no fix other than not use Chrome, new CORS policy has no override for cross-zones.

## vpts1202 | 2021-10-16T07:49:07+00:00
The issue is resolved by @ludufre
Look at his great work: https://github.com/ludufre/xmworkers
	


# Action History
- Created by: vpts1202 | 2021-10-01T06:03:36+00:00
- Closed at: 2021-10-16T07:49:54+00:00
