---
title: monero-wallet-gui running very slow on Debian
source_url: https://github.com/monero-project/monero-gui/issues/3821
author: b3K1ndRw1nd
assignees: []
labels: []
created_at: '2022-01-15T21:53:46+00:00'
updated_at: '2022-01-16T20:40:36+00:00'
type: issue
status: closed
closed_at: '2022-01-16T20:39:47+00:00'
---

# Original Description
I installed `monero-wallet-gui` 0.17.3.0 on my debian 11.2 using the instructions at https://gitlab.com/whonix/monero-gui#how-to-install-monero-using-apt-get and I have set it up with the simple mode and let it run for more than an hour and I still see only
![Screenshot from 2022-01-15 13-43-39](https://user-images.githubusercontent.com/84428257/149638785-b5145b8e-82cb-45bf-8ffc-42028ef73aa7.png)


There is no indication of any progress to let me know if anything is happening in the background 

These are my settings:
```
GUI version: 0.17.3.0-release (Qt 5.15.2)
Embedded Monero version: 0.17.3.0-release
Wallet path: /home/b3_k1nd_rw1nd/1_Home/wallets/samaritan/samaritan.keys
Wallet restore height: 2504788
Wallet log path: /home/b3_k1nd_rw1nd/.bitmonero/monero-wallet-gui.log
Wallet mode: Simple mode
Graphics mode: OpenGL
```

and this is what I see in the logs

```
$ monero-wallet-gui
2022-01-15 19:42:17.468	W Qt:5.15.2 GUI:- | screen: 1920x1080 - available: QSize(1920, 1080) - dpi: 96 - ratio:0.689038
2022-01-15 19:42:21.269	W Logging to "/home/b3_k1nd_rw1nd/.bitmonero/monero-wallet-gui.log"
2022-01-15 19:42:21.278	W qrc:/qt-project.org/imports/QtQuick/Controls/ApplicationWindow.qml:259:9: QML ContentItem: Binding loop detected for property "implicitWidth"
2022-01-15 19:42:33.922	W Model size of -42 is less than 0
2022-01-15 19:42:33.922	W Model size of -43 is less than 0
2022-01-15 19:42:53.259	W Account on device. Initing device...
2022-01-15 19:42:58.844	W Device inited...
2022-01-15 19:42:59.752	W Loaded wallet keys file, with public address: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
2022-01-15 19:43:04.846	I Monero 'Oxygen Orion' (v0.17.3.0-release)
Forking to background...
2022-01-15 19:43:14.411	W qrc:/main.qml:733: TypeError: Cannot call method 'connected' of undefined
2022-01-15 19:43:32.664	W Logging to "/home/b3_k1nd_rw1nd/.bitmonero/monero-wallet-gui.log"
2022-01-15 19:43:54.694	W Account on device. Initing device...
2022-01-15 19:43:57.643	W Device inited...
2022-01-15 19:43:58.607	W Loaded wallet keys file, with public address: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
2022-01-15 19:44:03.834	I Monero 'Oxygen Orion' (v0.17.3.0-release)
Forking to background...
2022-01-15 19:46:32.025	W Transaction extra has unsupported format: <c911c383f8b1b3f84404793016a623409e69846b4e55ff0a0265065021de47cc>
2022-01-15 19:46:32.029	W Transaction extra has unsupported format: <87f72708c6a008f88c1752e174bdb4fd85a5628d4e204bbe30698a5fb1667f07>
2022-01-15 19:46:32.030	W Transaction extra has unsupported format: <e08972f0b83609e8e19ae253fbdb4a65dd1546edaddeeb3afa66fc6110fae023>
2022-01-15 19:46:32.030	W Transaction extra has unsupported format: <77dbef04e7d6be0f78cd571b574a46b234963c75ff8f0432293c016c9a99df2c>
2022-01-15 19:46:32.030	W Transaction extra has unsupported format: <115ce61e4aff16ff4a3a2925e68dfe17f7839e30fea5999cb65defa64746cb67>
2022-01-15 19:46:32.031	W Transaction extra has unsupported format: <698b164f64c127ee638429366d2ecc068ac5d4cb8eb215125ae44174f0fcd415>
2022-01-15 19:46:32.031	W Transaction extra has unsupported format: <241c940119fb68498dfb1f3c1c3deba4266e0fec3c8b60f08d38e4490397176c>
2022-01-15 19:46:32.033	W Transaction extra has unsupported format: <d33686f9f145aae2231c69ac34cbbf306c98af9e31232e7ace7abd066eff6df7>
2022-01-15 19:46:32.033	W Transaction extra has unsupported format: <430f9846f1c285a406572b697870558490780ebc55318f246a59e74255f17457>
2022-01-15 19:46:32.036	W Transaction extra has unsupported format: <dfd787507ccdba1ee0c0f61b8233240b34d387165cf51f43bcf232f115948a50>
2022-01-15 19:46:32.043	W Transaction extra has unsupported format: <ba69997bc2d87ea8537ae32ccb086757c590a6c7653d077654bbf77e35c21726>
2022-01-15 19:46:32.055	W Transaction extra has unsupported format: <8668a4a0ccfc69a0c3880ab3e8614b59c77405d8f77869f7f8896b40fa55f3ce>
2022-01-15 19:46:32.057	W Transaction extra has unsupported format: <fc847d80a8adb162052bc116431478553c2da4833bb0c874546170ece745417f>
2022-01-15 19:46:32.058	W Transaction extra has unsupported format: <cd634d3b37bd31c83696e134c29efa384480ce710305579e8872556585bb0567>
2022-01-15 19:46:32.061	W Transaction extra has unsupported format: <47e39aeab38ac266f144a1e2fa32fba71004358e9f7b027c6c747fee90adadd0>
2022-01-15 19:46:32.064	W Transaction extra has unsupported format: <18f5109210d33c2252708e05fb439051a8dc97a1eed32a485b53bc356c39c173>
2022-01-15 19:46:32.065	W Transaction extra has unsupported format: <5c19cd21f7a01d253c9de56a994907498d19fab53de5cc98304eb8ed9231bb64>
2022-01-15 19:46:32.067	W Transaction extra has unsupported format: <02de6a6121e9d0d96e1d1a16c2b12c4a531f233710272b16ec969df19af064d3>
2022-01-15 19:46:32.068	W Transaction extra has unsupported format: <4dae71b6600b5d7cfa8c4db46670f3b6e7ad2ee22ad307691f8d114c877eb3de>
2022-01-15 19:46:32.070	W Transaction extra has unsupported format: <ec829323a0b15b32160ee87de84ebf8694f44545099c9b3c26c4269d31fcf39e>
2022-01-15 19:46:32.071	W Transaction extra has unsupported format: <ec86240843fc37e782c600f0ee7f5b6123b44ad8837b8fe83c3c31fc68d3978a>
2022-01-15 19:46:32.071	W Transaction extra has unsupported format: <243d255af1085d47bcaef1593cb1302a35c75e48ed1bba048a479dbcf4d0645d>
2022-01-15 19:46:32.072	W Transaction extra has unsupported format: <705c138a0437575d0527b7d218e1cd14d116a650d64f02bd4561257d9e2cc94f>
2022-01-15 19:46:32.073	W Transaction extra has unsupported format: <0245b2b313d4850671fd6aa639250e83ce2e8069771e1c80cea9d3faf65416e9>
2022-01-15 19:46:32.073	W Transaction extra has unsupported format: <ddc2a6d9ea8b4ea9b22a672e7415b8e98705be607b48dcd16681ed1da5e90abd>
2022-01-15 19:46:32.077	W Transaction extra has unsupported format: <088dc22278d7e2ddbc1d3fc7939d828e7668ff3204d67b8f8b7dc27bd78c9934>
2022-01-15 19:46:32.078	W Transaction extra has unsupported format: <1eb710836eace0086b03f5e5af7a7104fd09e2dd6913215a5e22749deaec7cc9>
2022-01-15 19:46:32.079	W Transaction extra has unsupported format: <03fcecd5a505529e168e7ffa676a53aff508b34f42e9d978d56f2ed8fd97d114>
2022-01-15 19:46:32.080	W Transaction extra has unsupported format: <650baf443d8281b9d7acaad99c3d255c97039cb47a40dd88987e810185e991aa>
2022-01-15 19:46:32.080	W Transaction extra has unsupported format: <ccfb0b26667b39564019eb094e64d1865dd18cafacdef73d51077633ff344190>
2022-01-15 19:46:32.081	W Transaction extra has unsupported format: <3e02060cf1caf91bdae8e838e5581549fe74b4ef44b3464c3484a299e44fcf88>
2022-01-15 19:46:32.081	W Transaction extra has unsupported format: <d11ed5fb8b9599db22b1eb7c122ade56d63d89d77a7c8cad66db8721834595b0>
2022-01-15 19:46:32.083	W Transaction extra has unsupported format: <f12f4c866cfa6a0f43dfa2690be35008e7238442f792f005bfe72bb30c5e3438>
2022-01-15 19:46:32.083	W Transaction extra has unsupported format: <dd801e85d973f4422a3ec27e3adc08736929951f50a0b6a0dd634938d7c0f9c6>
2022-01-15 19:46:32.087	W Transaction extra has unsupported format: <7f119b65332b25674883f1a82361febb42f64039e5115ce34d8e6d910f715b96>

```

# Discussion History
## selsta | 2022-01-15T22:02:42+00:00
Can you try clicking on the two arrows in the bottom left corner to connect to a new node?

If you still have issues then try connecting to a remote node, you can follow the steps here:

https://github.com/monero-project/monero-gui/issues/3140#issuecomment-706440354

## b3K1ndRw1nd | 2022-01-16T01:58:42+00:00
>Can you try clicking on the two arrows in the bottom left corner to connect to a new node?

Trying that just got me this below screen which is incorrect cause I know I did 2 deposits that are not showing.
![Screenshot from 2022-01-15 17-35-19](https://user-images.githubusercontent.com/84428257/149644327-e0329366-b376-4ce6-8f9d-293fbab4c1fd.png)

> If you still have issues then try connecting to a remote node, you can follow the steps here:
> https://github.com/monero-project/monero-gui/issues/3140

I can't even do that cause when I click the Exit Symbol, I have just been stuck with this screen for the past 20 minutes.

![Screenshot from 2022-01-15 17-57-45](https://user-images.githubusercontent.com/84428257/149644364-20d564c4-b99a-49ab-a341-60be8eea647b.png)

## selsta | 2022-01-16T02:00:48+00:00
It waits for the refresh to finish, but your refresh is stuck so it doesn't exit. Kill the program and then follow the steps.

Do you use a Ledger hardware wallet?

## b3K1ndRw1nd | 2022-01-16T04:16:45+00:00
>It waits for the refresh to finish, but your refresh is stuck so it doesn't exit. Kill the program and then follow the steps.

So I did that and tried the first node and it did not work, but when I went to the settings to try the next node, the GUI just froze, which happens often btw. I find the GUI has alot of lag.

Also, I saw this in the logs (I believe when I switched to the remote node), not sure if its a cause of concern
`2022-01-16 02:16:57.417	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon`

>Do you use a Ledger hardware wallet?

Yes

## selsta | 2022-01-16T04:18:55+00:00
Did you export the view key on wallet opening?

## b3K1ndRw1nd | 2022-01-16T19:13:29+00:00
No

## selsta | 2022-01-16T19:14:43+00:00
Well that's the problem. The Ledger isn't strong enough to do everything on device, you have to export the view key. Then your issues with lag will go away and everything should work fine.

## b3K1ndRw1nd | 2022-01-16T20:29:55+00:00
well how about that? thanks for the help.

any chance you can explain what was going on there that is the problem in layman's term or link me to something that can explain what was going on? still new to crypto and would love to learn more :smile: 

## selsta | 2022-01-16T20:31:54+00:00
Basically if you don't export the view key it tries to verify the transactions on the Ledger, which is too slow hardware wise so everything starts to lag. If you export the view key it does it on your computer.

The spend key stays on your Ledger so no malware can spend your monero.

## b3K1ndRw1nd | 2022-01-16T20:37:27+00:00
and I assume the trade-off is that if you do choose to export the view key so that the transactions are verified faster on the computer, you run the risk of compromising the key if you can't trust that the computer is secure?

## rating89us | 2022-01-16T20:38:06+00:00
If you export the private view key from the device to Monero GUI, your blockchain scan for incoming transactions will be faster. Only your incoming transactions will be send to the hardware wallet device for decryption.

If you do not export the private view key, all transactions, even those not for your wallet, will be sent to the device. This is more confidential but also a lot slower.

## b3K1ndRw1nd | 2022-01-16T20:39:47+00:00
alright. thank you for the info :+1: 

## selsta | 2022-01-16T20:40:36+00:00
> you run the risk of compromising the key if you can't trust that the computer is secure

Only the view key can get compromised, which means they can see your incoming transactions but they can't make any new transactions. But if your machine is compromised someone could see your balance anyway.

> If you do not export the private view key, all transactions, even those not for your wallet, will be sent to the device. This is more confidential but also a lot slower.

As far as I know, it doesn't work at all, not just a lot slower.

# Action History
- Created by: b3K1ndRw1nd | 2022-01-15T21:53:46+00:00
- Closed at: 2022-01-16T20:39:47+00:00
