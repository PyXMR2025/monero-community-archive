---
title: 50 character password works in cli wallet but not in gui
source_url: https://github.com/monero-project/monero-gui/issues/653
author: tikwanleap
assignees: []
labels:
- bug
- resolved
created_at: '2017-03-30T22:44:16+00:00'
updated_at: '2018-11-11T16:09:21+00:00'
type: issue
status: closed
closed_at: '2018-11-11T16:09:21+00:00'
---

# Original Description
I have a 50 character password that works in cli wallet but not in gui.

I tested in the latest versions of both cli and gui (0.10.3.1) on Windows 10 64-bit.

# Discussion History
## medusadigital | 2017-08-07T21:19:01+00:00
sounds like a possible bug. needs investigation

+bug

## dEBRUYNE-1 | 2017-12-13T11:09:43+00:00
Does it contain a space?

## tikwanleap | 2017-12-13T22:24:49+00:00
It does not. But it does contain accented characters (non-ASCII).

## dEBRUYNE-1 | 2017-12-14T14:57:30+00:00
Does it contain parentheses as well?

## tikwanleap | 2017-12-14T17:43:54+00:00
Yes it contains parentheses.

## sanderfoobar | 2018-01-11T13:15:48+00:00
Related to #199 #758 #820 and eventually/possibly https://github.com/monero-project/monero/issues/1390

## medusadigital | 2018-01-11T13:44:16+00:00
will be directly fixed in wallet2 API: https://github.com/monero-project/monero/issues/1390

closing here. 

thanks for report 

EDIT: my bad, this is not the same as https://github.com/monero-project/monero/issues/1390, which is about wallet paths, while this issue is about **wallet password**

## sanderfoobar | 2018-01-11T14:12:57+00:00
Using GUI **Monero 'Helium Hydra' (v0.11.1.0-release)**:

- Create wallet
- Password `Á' ` (accented, parenthesis, space)
- Close GUI

Testing in the CLI:

- `./monero-wallet-cli --testnet --wallet-file="/home/dsc/Monero/wallets/accent_test5/accent_test5.keys"`
- password works, wallet opened

Testing in the GUI:
- `./monero-wallet-gui --testnet`
- Enter password `Á' `
- password works, wallet opened

Can't reproduce bug.

## medusadigital | 2018-01-11T14:16:49+00:00
+invalid 

## tikwanleap | 2018-01-11T21:24:12+00:00
I just tested again with v0.11.1.0 and it's still not working. The password is 50 characters long so skftn's test case may need to be modifed to use a 50 character long password with accents, parenthsis, brackets etc.

## tikwanleap | 2018-01-11T21:31:27+00:00
Ok, here is a test case where I was able to use the password in the CLI but still not working in the GUI. This is all using v0.11.1.0 for both.

password:
¥mùh§I¡|

Also, I created the wallet in CLI. This is different from skftn's test case where it is created in the GUI.

## danrmiller | 2018-04-05T20:02:31+00:00
-invalid

## xiphon | 2018-11-06T01:14:54+00:00
> Ok, here is a test case where I was able to use the password in the CLI but still not working in the GUI. This is all using v0.11.1.0 for both.
> 
> password:
> ¥mùh§I¡|
> 
> Also, I created the wallet in CLI. This is different from skftn's test case where it is created in the GUI.

Can't reproduce this one. @tikwanleap , could you check the latest build?

## dEBRUYNE-1 | 2018-11-11T16:00:50+00:00
+resolved

# Action History
- Created by: tikwanleap | 2017-03-30T22:44:16+00:00
- Closed at: 2018-11-11T16:09:21+00:00
