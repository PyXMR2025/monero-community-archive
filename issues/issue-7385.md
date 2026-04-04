---
title: 'Mining to Daemon Gives Occasional Error read error: "connection reset by peer"
  no active pools, stop mining'
source_url: https://github.com/monero-project/monero/issues/7385
author: downystreet
assignees: []
labels: []
created_at: '2021-02-18T21:39:14+00:00'
updated_at: '2022-05-25T10:03:26+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Daemon Version: 0.17.1.9

When mining to the Monero Daemon on my own system from the xmrig miners I am occasionally getting an error and the miners will stop mining for a large amount of time. For example, today I saw the error and it lasted 30 minutes. This only happens maybe once every 1 or 2 days for a certain amount of time and then the miners resume without any intervention. The miners connect to the daemon through the xmrig proxy which also gives an error, "#000 no active pools, stop." I just recently started mining through the daemon and have not seen this error when mining through pools. Xmrig was just recently updated so I'm not sure if it's an xmrig problem or a Monero problem, any incite would be helpful.

Edit: The 30 minute time may not be correct as I forgot certain systems sleep for 30 minutes so that's what causes that message on some, but I did see the proxy give error "#000 no active pools,stop" printed several times today. The proxy is on a machine that runs 24/7. I will run a log file and see if I can catch it again.

Update 03/23/21: I had a connection timeout on xmrig proxy last approximately 17 minutes while solo mining to the daemon today.

# Discussion History
## downystreet | 2021-02-19T17:34:35+00:00
Ok it just happened again as I was posting about upload limits not being honored by the daemon. The disconnect lasted about 2 minutes and resumed without any intervention, here is a screen shot from the log. I'm wondering if there is some connection between the massive uploading that is going on and the disconnect of the miners from the monero daemon?
![proxy](https://user-images.githubusercontent.com/63488055/108540033-b581f100-72ae-11eb-9aae-7b9611e1f788.png)


## downystreet | 2021-02-19T22:05:13+00:00
Here it is again happening 4 hours later.
![proxy2](https://user-images.githubusercontent.com/63488055/108566552-9f872700-72d4-11eb-8327-7b17263da451.png)


## downystreet | 2021-02-19T23:00:45+00:00
I just happened again 1 hour later and this time lasted for 4 minutes.
![proxy3](https://user-images.githubusercontent.com/63488055/108570614-5fc43d80-72dc-11eb-9316-7fb3c6ec2732.png)
![proxy4](https://user-images.githubusercontent.com/63488055/108570619-60f56a80-72dc-11eb-9b59-a6fc89c6fb4b.png)


## selsta | 2022-02-19T00:28:53+00:00
Do you still have this issue?

Can you try to run your daemon with `--rpc-ssl disabled` and check if the issue is remaining?

# Action History
- Created by: downystreet | 2021-02-18T21:39:14+00:00
