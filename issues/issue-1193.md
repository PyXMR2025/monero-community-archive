---
title: 'ERROR C:/msys64/DISTRIBUTION-BUILD/src/p2p/net_node.inl:524 UPNP_AddPortMapping
  failed, error: ConflictInMappingEntry'
source_url: https://github.com/monero-project/monero/issues/1193
author: Gannicus1987
assignees: []
labels: []
created_at: '2016-10-08T09:40:10+00:00'
updated_at: '2016-10-09T13:16:56+00:00'
type: issue
status: closed
closed_at: '2016-10-09T13:16:56+00:00'
---

# Original Description
I've attached my logfile. 
Probably something to do with binding 0.0.0.0:18080 ?

Do i need to delete, and re download the blockchain?

-G


# Discussion History
## Gannicus1987 | 2016-10-08T09:44:40+00:00
I'm trying to upload the .zip but it claims " We don't support that file type" ...
So here is a screenshot from my log.
![screenshot_1](https://cloud.githubusercontent.com/assets/22705295/19212179/957b161c-8d4c-11e6-9d80-7ccc63e7ef7b.png)


## ghost | 2016-10-08T09:50:23+00:00
You can just copy and paste the relevant part of the log but make sure to put it in 'code mode' - google how to paste code into GitHub. 

And make sure you're at log level 2 or 3. 


## Gannicus1987 | 2016-10-08T10:01:34+00:00
Okay will do. But what do you mean with log levels ?

-G


## ghost | 2016-10-08T13:02:57+00:00
Run monerod with --log-level=2


## Gannicus1987 | 2016-10-08T14:57:26+00:00
I ran it with --log-level=2 

But it kept going nuts..... is this normal....


## anonimal | 2016-10-08T15:44:33+00:00
`ConflictInMappingEntry - The port mapping entry specified conflicts with a mapping assigned previously to another client`

@Gannicus1987 are you running other monerd instances? What arguments did you pass on startup?


## Gannicus1987 | 2016-10-08T15:57:35+00:00
No only running one. Does it have anything to do with the port = 18080 not being open. 
I checked online and it says closed, but on my modem its Enabled.
![screenshot_1](https://cloud.githubusercontent.com/assets/22705295/19214335/ac4b7498-8d80-11e6-8bad-8b4359197cc6.png)


## ghost | 2016-10-09T11:26:57+00:00
What's the 0.0.0.0 in that screen shot?

It looks to me like your monero node has used upnp to ask the router to assign it an IP address, and has been assigned 192.168.1.35, but for some reason it's still putting itself on 0.0.0.0.

Create a file called `bitmonero.conf` in your `bitmonero` directory, and put in the following:

```
log-file=./monero.log
log-level=0
p2p-bind-ip=192.168.1.35 
p2p-bind-port=18080
max-concurrency=1
out-peers=64
```

Adjust log name, level and out-peers as necessary.


## Gannicus1987 | 2016-10-09T13:16:52+00:00
Yes, exactly node got ip 192.168.1.35 assigned, but my i have dynamic IP with my provider. And IP has changed to .37 in stead of .35
So i had opened a different port 47783 for my node, on bind-ip .37. And the issue got resolved.

No i decided to make a static ip for .35 and use port 18080. And everything is fine aswell.

So anyway, problem is resolved. 


# Action History
- Created by: Gannicus1987 | 2016-10-08T09:40:10+00:00
- Closed at: 2016-10-09T13:16:56+00:00
