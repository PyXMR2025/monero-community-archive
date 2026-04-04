---
title: funds are missing once the wallet is synchonized
source_url: https://github.com/monero-project/monero-gui/issues/2030
author: ghost
assignees: []
labels:
- resolved
created_at: '2019-03-23T07:10:14+00:00'
updated_at: '2019-03-27T17:53:48+00:00'
type: issue
status: closed
closed_at: '2019-03-27T07:27:33+00:00'
---

# Original Description
I had to reinstall my MacOS this week. After a fresh install, I downloaded the latest version of monero-gui, synchronized the chain from scratch and imported my backed up wallet.key.

The key was originally created before the gui was released maybe in 2016, and the wallet was last opened in 2018 with Monero 'Lithium Luna' (v0.12.3.0-release).

When I import the key I see the correct balance at first, but once the wallet finishes synchronizing the balance drops.

I've tried resyncing the chain, resyncing the wallet, using the gui, using the cli, using mymonero web client, following the instructions on [debruyne stackexchange solution](https://monero.stackexchange.com/questions/6640/i-am-missing-not-seeing-a-transaction-to-in-the-gui-zero-balance).

Did I make some horrible mistake? or maybe just missed a step?

![the case of the missing monero](https://user-images.githubusercontent.com/43562133/54862924-09af8e00-4d85-11e9-8a26-7423f97239eb.gif)



# Discussion History
## selsta | 2019-03-23T07:12:22+00:00
Can you look into the History tab? Did someone transfer some XMR out?

## ghost | 2019-03-23T07:20:37+00:00
The history seems incomplete as well. I've tried deleting everything and using the backed up bitmonero folder, but it's the same result

![Screen Shot 2019-03-23 at 16 14 17](https://user-images.githubusercontent.com/43562133/54863085-264cc580-4d87-11e9-99f4-d80eeed1d510.jpg)


## ghost | 2019-03-23T07:36:26+00:00
huh, I'm looking at my records and I have one entry for +9.765 that appeared out of thin air at the end of 2017. The balance has been 9.99596 for a while so I just assumed it was correct, but perhaps it was broken before and it finally corrected.

## sanderfoobar | 2019-03-27T02:32:55+00:00
Could you try [the command line interface](https://downloads.getmonero.org/cli/win64) (monero-wallet-cli) and report if you see your funds there? I doubt this is an issue with the GUI but just making sure.

## ghost | 2019-03-27T02:51:01+00:00
I did try the cli previously with the same result. It's strange because I don't remember buying the 9+ monero, and in my record there is just "???". But since 2017 I've reinstalled my OS multiple times and synced the chain from scratch each time and the balance was always remained the same, 9.99596.

Strangely, I put my recovery words in the mymonero.com wallet, and my balance was reported as 0... so, I have no idea. I've since sold the 0.23 so now it really is 0.

It was a magical mystery gain, so I'm not too worried about the loss... just surprised.

## dEBRUYNE-1 | 2019-03-27T07:20:17+00:00
>and my balance was reported as 0

MyMonero requires an import fee of 0.1 XMR in order to show the proper balance. This import fee cannot be subtracted of the wallet you are trying to restore. Put differently, it has to be send from a different wallet.

>It was a magical mystery gain, so I'm not too worried about the loss... just surprised.

I am going to mark this as resolved then. 

## dEBRUYNE-1 | 2019-03-27T07:20:21+00:00
+resolved

# Action History
- Created by: ghost | 2019-03-23T07:10:14+00:00
- Closed at: 2019-03-27T07:27:33+00:00
