---
title: Socks5 proxy being bypassed + Other weirdness
source_url: https://github.com/monero-project/monero-gui/issues/4180
author: unrealumbreallaaaaa
assignees: []
labels: []
created_at: '2023-05-22T05:00:15+00:00'
updated_at: '2025-03-19T17:07:04+00:00'
type: issue
status: closed
closed_at: '2023-05-23T08:35:26+00:00'
---

# Original Description
I have defined a socks5 proxy in the GUI, the one that fetches prices and updates and such.

In my firewall, I see the connections being made by the `monero-wallet-gui` binary to my socks proxy.

However, I also see connections being made by both the `monerod` and `monero-wallet-gui` binaries to `updates.moneropulse.org:53`, without going through the proxy.

I suppose that I thought that these checks would also go through the proxy, and I think it's very wrong that they don't.

Additionally, immediately when I start the GUI, the `monero-wallet-gui` binary begins making dozens of connections to random IP address, sort of like `monerod` does when it's working. But it does this before I even click the button to start the daemon. It does this for about 30 seconds, then stops.

So I have these questions:

1. Why do these binaries make update requests when I've specified a proxy? Is this intentional, or a bug?
2. How can I mitigate this? Ideally i want to force the update checks from the gui through the proxy and shut off the checks from `monerod` altogether
3. Why is the wallet binary connecting to all these random IPs on startup?

I'm on Linux and using OpenSnitch firewall.I have defined a socks5 proxy in the GUI, the one that fetches prices and updates and such.

In my firewall, I see the connections being made by the `monero-wallet-gui` binary to my socks proxy.

However, I also see connections being made by both the `monerod` and `monero-wallet-gui` binaries to `updates.moneropulse.org:53`, without going through the proxy.

Additionally, immediately when I start the GUI, the `monero-wallet-gui` binary begins making dozens of connections to random IP address, sort of like `monerod` does when it's working. But it does this before I even click the button to start the daemon. It does this for about 30 seconds, then stops.

I suppose that I thought that these checks would also go through the proxy, and I think it's very wrong that they don't.

So I have these questions:

1. Why do these binaries make update requests when I've specified a proxy? Is this intentional, or a bug?
2. How can I mitigate this? Ideally i want to force the update checks from the gui through the proxy and shut off the checks from `monerod` altogether
3. Why is the wallet binary connecting to all these random IPs on startup?

I'm on Linux and using OpenSnitch firewall.

# Discussion History
## selsta | 2023-05-22T05:32:54+00:00
> However, I also see connections being made by both the monerod and monero-wallet-gui binaries to updates.moneropulse.org:53, without going through the proxy.

monerod and monero-wallet-gui are separate programs. The proxy settings in the GUI don't apply to the daemon.

> Why do these binaries make update requests when I've specified a proxy? Is this intentional, or a bug?

Intentional, we use DNS to check if updates are available and the SOCKS proxy we use does not support DNS requests. The update itself would be downloaded through the proxy.

The same behavior happens when you compile from source, this isn't something we have specifically added to the binaries.

> How can I mitigate this? Ideally i want to force the update checks from the gui through the proxy and shut off the checks from monerod altogether

This is not possible, you have to disable updates altogether. You can either start monero-wallet-gui with `--disable-check-updates`, or do this in Settings -> Interface.

On the daemon side you have to add `--check-updates disabled` to the daemon startup flags in Settings -> Node.

> Why is the wallet binary connecting to all these random IPs on startup?

The program checks for updates after startup. We have multiple domains and it's required that the majority of DNS records update to indicate that a new version is available.

## unrealumbreallaaaaa | 2023-05-23T08:35:26+00:00
@selsta, thank you so much for your detailed response. I really do appreciate it. I disabled updates through the GUI, and it seems that it disables update checks from the GUI binary as well as the Daemon binary, as long as you start the daemon through the GUI (meaning that it adds the `--check-updates=disabled` to the monerod command automatically).

Thanks again. I will close this issue.

## selsta | 2023-05-23T10:24:40+00:00
> I disabled updates through the GUI, and it seems that it disables update checks from the GUI binary as well as the Daemon binary

It does not add `--check-updates disabled` to the daemon automatically, you have to add it manually on the Settings -> Node page to "Daemon Startup Settings".

## Antiwh0re | 2025-03-19T17:07:02+00:00
Oh really? So everything's fine? Like hell! Your whole project is intended for privacy protection and you are are making a fake feature with fine print at the bottom which jeopardizes that privacy! In fact there's even no fine print - you didn't bother to describe this feature in the manual, although it's present on the screenshots there. You've thrown us under the bus - go and fix that shit now!

# Action History
- Created by: unrealumbreallaaaaa | 2023-05-22T05:00:15+00:00
- Closed at: 2023-05-23T08:35:26+00:00
