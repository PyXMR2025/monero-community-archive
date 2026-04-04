---
title: 'Importing Blockchain user guide '
source_url: https://github.com/monero-project/monero-site/issues/311
author: KeeJef
assignees: []
labels: []
created_at: '2017-07-10T11:28:20+00:00'
updated_at: '2017-10-20T22:13:20+00:00'
type: issue
status: closed
closed_at: '2017-08-27T08:01:02+00:00'
---

# Original Description
# Importing the Blockchain to Monero GUI wallet (Windows)

### Step 1

Download the Current bootstrap from https://downloads.getmonero.org/blockchain.raw, you can skip this step if you are importing the Blockchain from another source.

### Step 2

Find the Path of your Monero wallet (the folder where you extracted your wallet) for example mine is.

`D:\monero-gui-0.10.3.1-beta2`

Yours might be different depending on where you decided to download your wallet and what version of the Monero wallet you have.

![importingblockchain1](https://user-images.githubusercontent.com/27277414/28016023-f2ace62a-65b5-11e7-9d3f-29e87731feb2.png)


### Step 3

Find the path of your downloaded Blockchain for example mine was. 

`C:\Users\KeeJef\Downloads\blockchain.raw`

Yours might be different depending on where you downloaded the Blockchain to.

### Step 4

Open a Command Prompt window. You can do this by pressing the Windows key + R, and then typing in the popup box `CMD`

![importingblockchain2](https://user-images.githubusercontent.com/27277414/28015951-ab11e022-65b5-11e7-985b-7f1b5cc4a0ad.png)


### Step 5

Now you need to navigate using the CMD window to the path of your Monero wallet. You can do this by typing. 

`cd THE PATH OF YOUR MONERO WALLET HERE` 

It should look something like.

 `cd D:\monero-gui-0.10.3.1-beta2`

If for some reason your Monero wallet is on another drive you can use `DriveLetter:` for example if your Monero wallet was on your D drive then before using the cd command you would do `D:`

![importingblockchain3](https://user-images.githubusercontent.com/27277414/28016124-60935886-65b6-11e7-9835-72039ab4c220.png)


### Step 6

Now type in your command prompt window.

`monero-blockchain-import --verify 1 --input-file YOUR BLOCKCHAIN FILE PATH HERE`

For example I would type.

`monero-blockchain-import --verify 1 --input-file C:\Users\KeeJef\Downloads\blockchain.raw`

If you downloaded the Blockchain from a trusted, reputable source you may set `verify 0` this will reduce the amount of time to sync the Blockchain.  

### Step 7

After the the Blockchain has finished syncing up you can open your monero wallet normally. Your downloaded blockchain.raw can be deleted. 


Author: Kee Jefferys

# Discussion History
## KeeJef | 2017-07-10T11:29:18+00:00
Wasnt sure if pictures were allowed. Hope someone can put this in the user guides section for me i dont really know how to make pull requests 

## erciccione | 2017-07-10T15:40:14+00:00
Hi @KeeJef You can use [this instructions](https://github.com/monero-project/monero-site#50-how-to-make-a-user-guide) to set up you user guide, and something like [this](http://blog.udacity.com/2015/06/a-beginners-git-github-tutorial.html) should be useful to get started with git, github or both. It's quite easy to understand once you got the mechanism

# Action History
- Created by: KeeJef | 2017-07-10T11:28:20+00:00
- Closed at: 2017-08-27T08:01:02+00:00
