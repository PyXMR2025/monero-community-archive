---
title: 'Best miner yet : request for a additional featire'
source_url: https://github.com/xmrig/xmrig/issues/6
author: solaris7x
assignees: []
labels:
- enhancement
created_at: '2017-05-24T12:39:51+00:00'
updated_at: '2019-08-02T12:34:23+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:34:23+00:00'
---

# Original Description
Hello sir 
I am very thankful to you for creating this miner it's gives double the hashrate on av 2 mode with hugepages enabled tested on xeon processor 
Double hashrate compared to cpumulti ccminer xmr-stak-cpu 
About 25% extra compared to yam 
All testing done on xeon vm with exact same config 
Tho I request you to add in the http webpage like in xmr-stak-cpu miner 
It really is helpful and saves the effort of ssh into machine 
I hope you are it soon and sorry for being selfish 
Thank you 

# Discussion History
## xmrig | 2017-05-24T13:04:11+00:00
You right web interface it's good and useful feature, I will think about it.
Thank you.

## anandanand84 | 2017-08-10T13:16:12+00:00
@xmrig @Guilty-King I can help with webinterface. what should be done?

## fpgablr | 2017-08-10T13:19:47+00:00
Hi Anand,
I have been tracking this thread as well. Where are you based?

Regards

Ranganath

On Thu, Aug 10, 2017 at 6:46 PM, Anand Aravindan <notifications@github.com>
wrote:

> @xmrig <https://github.com/xmrig> @Guilty-King
> <https://github.com/guilty-king> I can help with webinterface. what
> should be done?
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/6#issuecomment-321547692>, or mute
> the thread
> <https://github.com/notifications/unsubscribe-auth/Ab02F-qXiPvht348W3xJLzEdA93wRIa4ks5sWwKdgaJpZM4NlDAh>
> .
>


## xmrig | 2017-08-10T14:02:42+00:00
I have idea for web interface;

* On miner side just REST API, no HTML/JS/CSS only pure data.
* Web interface will be a SPA React.js application, will be open sourced as well.

Benefits:
* Can monitor multiple miner in one page.
* Web interface updates, wont need miner update (until API comparable).
* Anybody can add own web interface/monitoring/etc.

## anandanand84 | 2017-08-10T14:06:28+00:00
@xmrig Is there a rest endpoint currently available in the released miners?

## xmrig | 2017-08-10T14:09:28+00:00
No, it currently not available.

## xmrig | 2017-09-03T03:04:50+00:00
In dev branch added HTTP API to both cpu and nvidia versions.
Working miners instances with publicly available API:
http://94.130.19.186:4455/
http://94.130.19.186:4456/

Sample HTML page to get data from API https://gist.github.com/xmrig/c75fdd1f8e0f3bac05500be2ab718f8e

Authorization supported by optional Bearer token.



## hetmann | 2017-12-17T14:08:41+00:00
@xmrig can you make a list of information for the web SPA interface or should we use the API information list?

## xmrig | 2019-08-02T12:34:23+00:00
http://workers.xmrig.info/

# Action History
- Created by: solaris7x | 2017-05-24T12:39:51+00:00
- Closed at: 2019-08-02T12:34:23+00:00
