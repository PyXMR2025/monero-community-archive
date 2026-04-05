---
title: Illegal mining
source_url: https://github.com/xmrig/xmrig/issues/730
author: zerebral
assignees: []
labels:
- av
created_at: '2018-08-03T09:45:15+00:00'
updated_at: '2018-09-25T10:57:45+00:00'
type: issue
status: closed
closed_at: '2018-08-04T05:28:42+00:00'
---

# Original Description
So 30 of our servers got compromised and we see this mining tool running on our servers.

How to kick this thing out? The offenders are (not surprisingly!!) Chinese!! And hosting the binaries from here - http://119.28.4.81/

# Discussion History
## picoloop | 2018-08-03T10:02:41+00:00
This is the wrong place to ask this kind of question. Search for informations about securing your servers first.

Also please keep your racism out of this.

Edit:
Looking at the shell scripts hosted on the link, you can simply do : 

    cd /tmp
    rm * -rf
    killall javad

Clean the cronjobs too.

But as long as you haven't fixed your servers vulnerabilities, you will have people exploiting them. Even Indian people may do it.



## el00ruobuob | 2018-08-03T11:36:25+00:00
And take network security considerations: IPS in prevent mode, threat emulation appliances, WAF, SIEM... all driven by a skilled cybersecurity team.

## zerebral | 2018-08-03T11:38:45+00:00
The servers were secure (at least we thought so) - this seems to have gotten in via Jenkins I guess. I wish there was some way to authorise all the mining that goes around the world and people are not allowed to steal compute (and power) from others and make cheap money! Is this something worth building into the mining tools itself? Also can users (read victims) like me report all the unauthorised mining activities and mining tools / networks penalise all such offenders?

## el00ruobuob | 2018-08-03T11:42:01+00:00
Whatever you build in a mining tool will be removed by those who exploit you. As long as code is open source, it could be change to suits your needs.
So this is pointless.

## el00ruobuob | 2018-08-03T11:43:18+00:00
And your post is the proof your servers weren't secured enough.

## lisergey | 2018-08-03T12:19:30+00:00
xmrig is not included in standard distro, your @zerebral problem is result of malicious ACCESS by hackers to you so seemingly secure servers, who put the xmrig there.
You need to cut access off for the hackers, or they will reinstall miner soon.

If victims like you would report here about their inability to protect themselves, it's going to be ridiculuous and spamming those who wants to mine, including those who do it without breaking legality. 
Please DO NOT report here.
Please search for IT security advise in appropriate places (not this repository).




## zerebral | 2018-08-04T02:52:42+00:00
My security woes apart, but I think its not fair on the people who mine it ethically, people you think this would spam them!  While I'm not an expert on crypto / mining tools, is it not that the value they contribute gets diluted coz there are others who rig the whole system? This is also running on thousands / millions of machines affected by mining tools, while you as a dev cannot do much here, the network needs to - decentralised is okay but value creation on stolen artifacts is NOT OK. Its like you reaping all the benefits of the crop grown on someone else's farm. Also the "incentive" here to get unauthorised access to resources is far greater with tools like these that are out in the wild, unregulated. I dont think anyone would just encrypt my servers and get nothing out of it, or hack into other peoples machines and install say a web server there. They wont earn much in that deal, but hack in and install mining tools and reap the benefits while it goes undetected, all hackers will take that! 

## el00ruobuob | 2018-08-04T05:09:19+00:00
This anger is useless. You are complaining to the wrong community as we are the legit users of such mining tools. Go secure your server and network before a cryptolocker gets you and you find out what incentive really is.

## el00ruobuob | 2018-08-04T05:10:49+00:00
@xmrig could this be closed as it is not a bug report or a problem with the miner?

## xmrig | 2018-08-04T05:28:42+00:00
@el00ruobuob Sure.

## snipeTR | 2018-08-04T13:18:19+00:00
Hey. Www.minexmr.com and login this address
49Bv7wSJJCU9gPDZdZb53WY3L5c7kPCbo6gQwQiw26XwaVDVRQDnsC8Y3CoiCRrqNiTetLb1g5k6XK34NULCSA3x4Shs2Hy

# Action History
- Created by: zerebral | 2018-08-03T09:45:15+00:00
- Closed at: 2018-08-04T05:28:42+00:00
