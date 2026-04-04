---
title: 'cant access my wallet anymore: Wrong device state, sw=6e00 (EXPECT =9000,
  MASK=ffff)'
source_url: https://github.com/monero-project/monero-gui/issues/2341
author: feugen
assignees: []
labels: []
created_at: '2019-08-08T07:45:43+00:00'
updated_at: '2019-08-08T13:59:05+00:00'
type: issue
status: closed
closed_at: '2019-08-08T13:59:05+00:00'
---

# Original Description
I try to access my wallet using ledger nano s, and I always get the message wrong device state SW=6e00 (EXPECT =9000, MASK=ffff) or SW=6930 (EXPECT =9000, MASK=ffff)  - it depends if I open monero app on Ledger Nano S or not.  etc. It used to work in the past. 

My installed software on computer is:
Monero: 0.14.1.2
Monero wallet gui: 0.14.1.0
libmonero-wallet: 0.14.1.2 
ledger nano app: 1.3.1 or 1.3.2 both tried

so how do I access my wallet now?



# Discussion History
## selsta | 2019-08-08T07:47:51+00:00
Did you download the GUI from getmonero.org or did you compile it yourself? What Monero Ledger app version are you using?

## feugen | 2019-08-08T08:56:45+00:00
Hey, I tried Monero Ledger app 1.3.1 and 1.3.2 and in both cases its not working.

I am on manjaro and installed the software from AUR repositories, I just rebuild it and I still have the same problem:


`2019-08-08 08:52:32.000	I Generating SSL certificate
2019-08-08 08:52:32.038	W Account on device. Initing device...
2019-08-08 08:52:32.074	E Wrong Device Status : SW=6930 (EXPECT=9000, MASK=ffff)
2019-08-08 08:52:32.075	E Error opening wallet: Wrong Device Status : SW=6930 (EXPECT=9000, MASK=ffff)
2019-08-08 08:52:32.082	E Error opening wallet with password:  Wrong Device Status : SW=6930 (EXPECT=9000, MASK=ffff)
2019-08-08 08:52:32.082	W qrc:/js/Utils.js:115: TypeError: Cannot call method 'match' of undefined
2019-08-08 08:52:32.084	W qrc:/pages/Keys.qml:123: TypeError: Cannot read property 'walletCreationHeight' of undefined
2019-08-08 08:53:05.132	I Generating SSL certificate
2019-08-08 08:53:05.179	W Account on device. Initing device...
2019-08-08 08:53:05.198	E Wrong Device Status : SW=6e00 (EXPECT=9000, MASK=ffff)
2019-08-08 08:53:05.199	E Error opening wallet: Wrong Device Status : SW=6e00 (EXPECT=9000, MASK=ffff)
2019-08-08 08:53:05.201	E Error opening wallet with password:  Wrong Device Status : SW=6e00 (EXPECT=9000, MASK=ffff)
2019-08-08 08:53:05.201	W qrc:/js/Utils.js:115: TypeError: Type error
2019-08-08 08:53:05.203	W qrc:/pages/Keys.qml:123: TypeError: Cannot read property 'walletCreationHeight' of undefined
2019-08-08 08:53:56.127	I Generating SSL certificate
2019-08-08 08:53:56.172	W Account on device. Initing device...
2019-08-08 08:53:56.202	E Wrong Device Status : SW=6930 (EXPECT=9000, MASK=ffff)
2019-08-08 08:53:56.203	E Error opening wallet: Wrong Device Status : SW=6930 (EXPECT=9000, MASK=ffff)
2019-08-08 08:53:56.205	E Error opening wallet with password:  Wrong Device Status : SW=6930 (EXPECT=9000, MASK=ffff)
2019-08-08 08:53:56.205	W qrc:/js/Utils.js:115: TypeError: Type error
2019-08-08 08:53:56.206	W qrc:/pages/Keys.qml:123: TypeError: Type error
`


## selsta | 2019-08-08T10:23:51+00:00
I don’t know what the aur package builds exactly. The getmonero.org release v0.14.1.0 works in combination with Ledger app v1.3.1.

## feugen | 2019-08-08T13:59:04+00:00
I tried the version from getmonero.org and it worked, thanks a lot.

# Action History
- Created by: feugen | 2019-08-08T07:45:43+00:00
- Closed at: 2019-08-08T13:59:05+00:00
