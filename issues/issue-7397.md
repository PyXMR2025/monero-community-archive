---
title: Miners Receive 50 New Jobs In 1 Minute Multiple Times Per Day Solo Mining To
  Daemon
source_url: https://github.com/monero-project/monero/issues/7397
author: downystreet
assignees: []
labels: []
created_at: '2021-02-23T07:14:12+00:00'
updated_at: '2022-02-19T00:29:07+00:00'
type: issue
status: closed
closed_at: '2022-02-19T00:29:07+00:00'
---

# Original Description
Monerod Version: 0.17.1.9

I am solo mining to the daemon through xmrig proxy all within the same network. I recently started keeping a log of mining activity on 2 machines and was going through the logs and noticed that the xmrig miners are reporting approximately 50 or more new jobs in the span of a minute or 2 a couple of times per day. I was thinking that when solo mining to the daemon a new job corresponded with a new block being found. Correct me if I'm wrong about this. Every instance of the mass new jobs occurred at the same times on both machines. I have reported this to xmrig as well. The mass of new jobs appear to be happening on the same block and usually lasts 1-4 minutes. Here is a picture of the log.
![proxy5](https://user-images.githubusercontent.com/63488055/108812135-95875180-757c-11eb-9372-5881c72ec9a2.png)


# Discussion History
## downystreet | 2021-02-26T00:24:39+00:00
The mass of new jobs are corresponding to the same time when the xmrig proxy is giving the error connection error: connect error: "connection timed out", #000 no active pools, stop ,connect error: "connection timed out". So when the xmirg proxy is giving the connect error the miners are getting lots of new jobs for the same block. I posted about the connection error in #7385.

Update: The same thing happens when not using the xmrig proxy. I set 2 miners to connect directly to the daemon and not go through xmrig proxy and the same thing happens. They get the connection timeout at certain times followed by a mass of new jobs for the same block.

## selsta | 2022-02-19T00:29:07+00:00
Let's keep it to one issue.

# Action History
- Created by: downystreet | 2021-02-23T07:14:12+00:00
- Closed at: 2022-02-19T00:29:07+00:00
