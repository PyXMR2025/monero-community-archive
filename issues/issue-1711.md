---
title: No incoming connections - check firewalls/routers allow port
source_url: https://github.com/monero-project/monero-gui/issues/1711
author: ghost
assignees: []
labels: []
created_at: '2018-10-29T10:48:46+00:00'
updated_at: '2023-01-14T08:14:18+00:00'
type: issue
status: closed
closed_at: '2018-10-30T12:15:46+00:00'
---

# Original Description
OS: Windows 10
GUI version: Monero GUI v0.13.0.3

I have successfully synchronised daemon and wallet blocks are now syncing:
![2018-10-29 4](https://user-images.githubusercontent.com/14051589/47645155-df81e780-dbbb-11e8-888e-6f22c6a04292.png)

However, while wallet blocks sync I am having the below notification when running Monero GUI:
2018-10-29 10:31:29.394 [P2P3] WARN global src/p2p/net_node.inl:1338 [1;31mNo incoming connections - check firewalls/routers allow port 18080[0m

Screenshot: 
![2018-10-29 1](https://user-images.githubusercontent.com/14051589/47644938-4783fe00-dbbb-11e8-9461-2e10f0995722.png)

I am using Windows Defender and I have allowed the port as requested (18080) - and whitelisted Monero GUI.

Screenshot (Port):
![2018-10-29 2](https://user-images.githubusercontent.com/14051589/47644989-697d8080-dbbb-11e8-813d-539b934ba02d.png)

Screenshot (Whitelist):
![2018-10-29 3](https://user-images.githubusercontent.com/14051589/47645062-a0539680-dbbb-11e8-88cc-9aaf8eb0b178.png)

Thanks for any advice, which would be greatly appreciated.


# Discussion History
## dEBRUYNE-1 | 2018-10-29T14:41:49+00:00
First note that the GUI (and the integrated daemon (monerod)) will still function properly without any incoming connections. Now, to open port 18080 properly, you have to forward / open it in your router too. 

## ghost | 2018-10-29T15:04:13+00:00
Thanks 👍 Are you able to assist with what I need to fill in here:

![2018-10-30](https://user-images.githubusercontent.com/14051589/47658981-b2473080-dbdf-11e8-9cb8-6ce8cd8139aa.png)


## sanderfoobar | 2018-10-30T12:01:17+00:00
Opening port 18080 allows incoming P2P connections. Like @dEBRUYNE-1 mentioned; your daemon works fine without port forwarding. Personally I sometimes get this error - I ignore it.

As for actually configuring your router to forward port 18080 to the machine on your local network; try to find some guides and/or your router's manual concerning port forwarding. In addition: Windows can block these requests so make sure the Windows firewall allows such connections (TCP and UDP).

From the screenshot you posted I can give some insight:

Service: other
External host: (leave empty if you can)
External port: 18080
Internal host: (the IP address of your machine on your local network; it will start with `192.168.1...`
Internal port: 18080

Protocol should probably be UDP (?) but if you can, choose 'Both' from the dropdown menu. `print_cn` will help you verify your incoming connections are working.

## ghost | 2018-10-30T12:15:36+00:00
Thanks so much for the help! It seems to be working.

## hajes | 2023-01-14T08:14:18+00:00
source IP or 0.0.0.0
source port any (because no network socket connects with two same ports, source port 51456 destination port 1844)

same goes for Monero node

# Action History
- Created by: ghost | 2018-10-29T10:48:46+00:00
- Closed at: 2018-10-30T12:15:46+00:00
