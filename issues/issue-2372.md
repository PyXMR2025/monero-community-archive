---
title: 'DNS error: "temporary failure" on a VPS'
source_url: https://github.com/xmrig/xmrig/issues/2372
author: MernGG
assignees: []
labels:
- question
created_at: '2021-05-13T15:45:00+00:00'
updated_at: '2021-06-04T15:03:33+00:00'
type: issue
status: closed
closed_at: '2021-05-14T05:17:10+00:00'
---

# Original Description
Mining on a VPS and receiving an error
I am mining on a CPU optimized vultr VPS and getting the error "us-west.minexmr.com:443 DNS error: "temporary failure"". To set up the rig I used the advanced ubuntu setup. 

How to reproduce:
Not sure but you could try the free trial on vultr since they offer a 100 dollar starter credit.

Expected Behavior: 
The rig to mine xmr as intended.

Data: 
![image](https://user-images.githubusercontent.com/46382789/118147156-27f10180-b3c4-11eb-90ff-d4bcf8c07729.png)
 - OS: Ubuntu

Additional Context: 
I used the exact same setup process on another VPS service and it works just fine so it might be a problem with the VPS provider.

# Discussion History
## xmrig | 2021-05-14T00:17:50+00:00
They blocked DNS requests to major pools, so you can switch to a smaller pool (better option) or add IP addresses to `/etc/hosts` file.
Thank you.

## MernGG | 2021-05-14T05:17:05+00:00
> They blocked DNS requests to major pools, so you can switch to a smaller pool (better option) or add IP addresses to `/etc/hosts` file.
> Thank you.

Thank you very much worked perfectly!

## avasantha | 2021-05-21T18:55:38+00:00
I am also trying the same with vultr with the free credits. Can you please let me know what would be the IP I need to add in the hosts file? May be you could show me how does the hosts file would look like. 

Thanks in advance.

## MernGG | 2021-05-21T22:23:15+00:00
> I am also trying the same with vultr with the free credits. Can you please let me know what would be the IP I need to add in the hosts file? May be you could show me how does the hosts file would look like.
> 
> Thanks in advance.

add this to the etc/hosts file
51.81.151.235 us-west.minexmr.com
147.135.37.31 us-west.minexmr.com

if you are planning on using an east pool open up cmd and do "ping (link)" and it will print the IP out.

also in advance don't use too many computers at once because they will limit your CPU and it won't be as profitable. 

## wule108 | 2021-06-04T13:21:21+00:00
Specifying the domain name as a fixed IP is a stupid practice，In order to prevent the mining pool from being ddos, multiple ips were resolved with dns，Therefore, the IP corresponding to the domain name will change，so the correct approach should be like this echo 'nameserver 8.8.8.8' >> /etc/resolv.conf. Don't add IP addresses to /etc/hosts file.

> Mining on a VPS and receiving an error
> I am mining on a CPU optimized vultr VPS and getting the error "us-west.minexmr.com:443 DNS error: "temporary failure"". To set up the rig I used the advanced ubuntu setup.
> 
> How to reproduce:
> Not sure but you could try the free trial on vultr since they offer a 100 dollar starter credit.
> 
> Expected Behavior:
> The rig to mine xmr as intended.
> 
> Data:
> ![image](https://user-images.githubusercontent.com/46382789/118147156-27f10180-b3c4-11eb-90ff-d4bcf8c07729.png)
> 
> * OS: Ubuntu
> 
> Additional Context:
> I used the exact same setup process on another VPS service and it works just fine so it might be a problem with the VPS provider.

Specifying the domain name as a fixed IP is a stupid practice，In order to prevent the mining pool from being ddos, multiple ips were resolved with dns，Therefore, the IP corresponding to the domain name will change，so the correct approach should be like this echo 'nameserver 8.8.8.8' >> /etc/resolv.conf. Don't add IP addresses to /etc/hosts file.

## xmrig | 2021-06-04T15:03:33+00:00
@wule108 When last time I checked, changing a nameserver didn't help, but I may remember it wrong, it was a few years ago or maybe they relaxed filtration. Right now changing a nameserver works fine.
Thank you.

# Action History
- Created by: MernGG | 2021-05-13T15:45:00+00:00
- Closed at: 2021-05-14T05:17:10+00:00
