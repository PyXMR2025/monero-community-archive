---
title: 'read error: "connection reset by peer" ,no active pools, stop mining'
source_url: https://github.com/xmrig/xmrig/issues/2118
author: downystreet
assignees: []
labels: []
created_at: '2021-02-18T21:13:47+00:00'
updated_at: '2021-04-12T14:12:08+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:12:08+00:00'
---

# Original Description
I am occasionally getting the error "read error: "connection reset by peer" ,no active pools, stop mining" in the xmrig miners when mining to the monero daemon. Today the error lasted for about 30 minutes until mining resumed without any intervention. They run 24/7 and I've seen this happen before but it only happens once and then it is maybe a day or so before it happens again. I don't have a record of the logs unless there is a default path so I can't say for certain how often it is happening. I am running miners through the xmrig proxy and connected to the Monero daemon on my own system. The xmrig-proxy also displayed an error of "#000 no active pools, stop" during this time. I just recently started mining through the monero daemon instead of a pool and I also updated xmrig from github recently as well. I have not had this problem in the past as far as I know so I'm not sure if this is related to an xmrig update, the proxy, or the Monero daemon. Any insights would be helpful.

Edit: The 30 minute time may not be correct as I forgot certain systems sleep for 30 minutes so that's what causes that message on some, but I did see the proxy give error "#000 no active pools,stop" printed several times today at the top of the output. The proxy is on a machine that runs 24/7. I will run a log file and see if I can catch it again.

Update: Recorded a 17 minute time out.

# Discussion History
## downystreet | 2021-02-19T22:36:12+00:00
Here are the logs. Usually the disconnect is occuring for approximately 1-2 minutes. I have seen it happen more than once today. This is happening on xmrig proxy. Should I post in the xmrig proxy github as well?
![proxy](https://user-images.githubusercontent.com/63488055/108568832-ce070100-72d8-11eb-96de-45c01c03599c.png)
![proxy2](https://user-images.githubusercontent.com/63488055/108568848-d4957880-72d8-11eb-8aa2-826a1b0cf5b3.png)


# Action History
- Created by: downystreet | 2021-02-18T21:13:47+00:00
- Closed at: 2021-04-12T14:12:08+00:00
