---
title: '[Not an issue, just need clarification] An alternative to using Monero-GUI
  wallet over Tor'
source_url: https://github.com/monero-project/monero-gui/issues/4063
author: ch9PcB
assignees: []
labels: []
created_at: '2022-11-04T07:07:13+00:00'
updated_at: '2022-11-06T00:46:51+00:00'
type: issue
status: closed
closed_at: '2022-11-06T00:46:51+00:00'
---

# Original Description
I have the following software on my computer:

> Debian 11.5 (Linux kernel 5.10.149-2 (2022-10-21) x86_64 GNU/Linux), installed
> 
> torsocks 2.3.0-3 x86_64, installed
> 
> tor 0.4.7.10-1-bpo11+1 (bullseye-backports), installed
> 
> Monero GUI wallet version 0.18.1.2
> 
> Tor Browser 11.5.7


For some time now, I have been using the following command in a terminal to synchronize my GUI wallet over tor:

`DNS_PUBLIC=tcp://8.8.8.8 TORSOCKS_ALLOW_INBOUND=1 torsocks ./monerod --p2p-bind-ip 127.0.0.1 --no-igd --hide-my-port --ban-list block.txt --data-dir    /media/username/Storage/Monero`

I wonder if the above command would produce the same result if I made the following changes to the GUI version, that is:

```
Settings --> Node --> Bootstrap Address --> 127.0.0.1
Settings --> Node --> Bootstrap Port --> 9050 (if I use the installed tor package)
Settings --> Node --> Bootstrap Port --> 9150 (if I launch Tor Browser first)
```

`Settings --> Interface --> Tick/check the box "Socks5 proxy" --> IP address --> 127.0.0.1, Port: 9050 (if I use the installed tor package) or 9150 (if I use Tor Browser).`

I prefer to use Monero GUI wallet because I had been using Microsoft Windows for many years before switching to using Linux distros.

Thank you for your clarification/feedback


# Discussion History
## selsta | 2022-11-04T12:02:30+00:00
> I wonder if the above command would produce the same result if I made the following changes to the GUI version, that is:

No, this would not work. The bootstrap field is for specifying a bootstrap daemon, not a socks proxy. Setting socks proxy in Settings -> Interface is only relevant when using a remote node, something that would not apply to you if you use a local node.

You can add `--proxy 127.0.0.1:9050` (or 9150) to Settings -> Node -> Local node -> Daemon startup flags, this will make your daemon use Tor. There's no need for `torsocks`.

## ch9PcB | 2022-11-04T12:29:58+00:00
> No, this would not work.

Thanks for your clarification. I have been doing it wrong for the past several months and am glad that I asked about it in this forum.

> The bootstrap field is for specifying a bootstrap daemon, not a socks proxy. Setting socks proxy in Settings -> Interface is only relevant when using a remote node, something that would not apply to you if you use a local node.

I forgot to mention it in the original post that I do use a local node.
 
> You can add `--proxy 127.0.0.1:9050` (or 9150) to Settings -> Node -> Local node -> Daemon startup flags, this will make your daemon use Tor. There's no need for `torsocks`.

In the box under `Daemon startup flags`, I already have the following flags. They are:


`--prune-blockchain --ban-list block.txt
`

So, if I add the flag that you provided, there will be three flags in the box under `Daemon startup flags`:


`--prune-blockchain --ban-list block.txt --proxy 127.0.0.1:9050 (or 9150)
`

(a) Am I right to say that a blank space is used to separate flags?

(b) Is there a maximum limit to the number of flags that I can specify in the box under `Daemon startup flags`?

> There's no need for torsocks

Thanks for your clarification.





## selsta | 2022-11-04T12:35:38+00:00
You can add either

```
--prune-blockchain --ban-list block.txt --proxy 127.0.0.1:9050
```

or

```
--prune-blockchain --ban-list block.txt --proxy 127.0.0.1:9150
```

depending on what port you use. I don't think there is any character limit.

## ch9PcB | 2022-11-04T12:41:54+00:00
>  I don't think there is any character limit

Thank you.

My next question is not related to the original post. Please let me know if I need to open a new post.

My question is this: if I use a local node and Tor to synchronise Monero-GUI wallet with the servers, will I cause the Tor network to slow down or create bottlenecks to Tor traffic much like how some inconsiderate people use Tor to torrent stuff?



## selsta | 2022-11-04T12:44:46+00:00
If your node is already synced or mostly synced you can use `--proxy` without issues. If you want to sync your node from height 0 over Tor it will likely cause a lot of traffic. I don't think it will cause any issues for Tor but probably better to sync up over clearnet.

## ch9PcB | 2022-11-04T13:13:38+00:00
> I don't think it will cause any issues for Tor but probably better to sync up over clearnet.

OK, I shall heed your advice. There are times when I do not sync my local node for many days or weeks because I do not have access to my computer. In such cases, I shall sync my local node over clearnet so as not to jam up the Tor network.

Thank you and I shall close this post now.



## ch9PcB | 2022-11-05T11:39:25+00:00
@selsta

I have just reopened this original thread because some questions came to my mind a few minutes ago.

To recapitulate: my original post about 20 hours ago is about running a local node with Tor.

Now, I wish to know about using the remote node with Tor in Monero-GUI wallet.

`Settings --> Node --> Remote node`

There is a notice that states:

> Uses a third-party server to connect to the Monero network. Less secure, but easier on your computer.

_First question_: What is meant by "less secure"? Can you elaborate please?

If I use the remote node with Tor, then I must specify the following parameters such as:

```
Bootstrap Address: 127.0.0.1

Bootstrap Port: 9050
```

_Second question_: Is the above correct?

_Third question_: Will I achieve the same level of anonymity when I connect the local node using Tor compared with when I connect the remote node using Tor?

## selsta | 2022-11-05T14:46:13+00:00
> First question: What is meant by "less secure"? Can you elaborate please?

This is specifically about using a third party remote node over clearnet. They can record your IP address for example and link it with a transaction id.

> If I use the remote node with Tor, then I must specify the following parameters such as:

No, bootstrap address / port has nothing to do with Tor and entering 127.0.0.1:9050 into it is incorrect. You have to set Tor address / port in Settings -> Interface -> Socks Proxy field.

> Third question: Will I achieve the same level of anonymity when I connect the local node using Tor compared with when I connect the remote node using Tor?

Using a self hosted node is always preferred, doesn't matter if you host that node locally on the same machine or on a different machine.

## selsta | 2022-11-06T00:46:51+00:00
Closing this but you can still ask questions in the comments.

# Action History
- Created by: ch9PcB | 2022-11-04T07:07:13+00:00
- Closed at: 2022-11-06T00:46:51+00:00
