---
title: Incorrect password
source_url: https://github.com/monero-project/monero/issues/8370
author: MadelineProtoFan
assignees: []
labels: []
created_at: '2022-05-31T21:52:42+00:00'
updated_at: '2022-05-31T23:14:13+00:00'
type: issue
status: closed
closed_at: '2022-05-31T23:14:12+00:00'
---

# Original Description
I entered the wallet with password, recieved the money tried to send it - but password incorrect



# Discussion History
## selsta | 2022-05-31T21:55:05+00:00
Maybe you simply mistyped the wallet password?

Can you still open the wallet? Do you have the seed?

## MadelineProtoFan | 2022-05-31T21:56:54+00:00
i can enter the same _viewonly wallet with my password. But the normal one - invalid password
I dont have the seed
I am sure in this password 100%
Are there any variants how to open my wallet?

## selsta | 2022-05-31T21:59:04+00:00
What is the file size of wallet_name.keys?
When was it last changed?

Do you have a backup? Which OS are you using?

## MadelineProtoFan | 2022-05-31T22:04:39+00:00
Size: 2 kb
Last change : 21:06
Time now : 1:04

Windows 10. No backups :(

It is not the same problem?
https://www.reddit.com/r/monerosupport/comments/hxqv2m/monero_gui_and_ledger_invalid_password/

## selsta | 2022-05-31T22:05:16+00:00
Do you use a Ledger? I assume no?

## MadelineProtoFan | 2022-05-31T22:05:29+00:00
No i dont use ledger

## selsta | 2022-05-31T22:06:51+00:00
Can you try to open the wallet with monero-wallet-cli?

The problem is files can get corrupted, so it's super important to write down the seed. That's the only way to guarantee access in all cases. Which isn't helpful right now.

## selsta | 2022-05-31T22:07:20+00:00
Did you maybe use the change wallet password feature and forgot? Did you try an empty password?

## MadelineProtoFan | 2022-05-31T22:08:15+00:00
Is it possible that i was hacked by some malware and somebody changed the key wallet password (while i was in the wallet with open session). And there is no record about it in the log file?

Can you say how to open the key file in monero-wallet-cli?

## MadelineProtoFan | 2022-05-31T22:08:33+00:00
100% do not changed the password

## selsta | 2022-05-31T22:11:24+00:00
What did you do at 21:06? Something was changed there.

## MadelineProtoFan | 2022-05-31T22:12:58+00:00
https://mega.nz/file/yXoQFSpb#svUNwb8Vwld8g1brrsxmJGex_A41kFom6Avz8BRyTmQ
I was in the wallet waiting for the money
Can you look at my log?

## selsta | 2022-05-31T22:14:19+00:00
Download monero-wallet-cli from here: https://downloads.getmonero.org/cli/win64

Then open cmd.exe, drag and drop monero-wallet-cli.exe into it and then add `--wallet-file` and then drag and drop the `wallet_name.keys` file into it. It should look something like this:

```
C:\Downloads\monero-wallet-cli.exe --wallet-file C:\Monero\wallets\wallet.keys
```

Then enter your password and check if it starts.

## MadelineProtoFan | 2022-05-31T22:23:49+00:00
Password incorrect :(

## selsta | 2022-05-31T22:26:46+00:00
I did not see anything interesting in the logs. Did you force shutdown your computer / did you have a power loss?

## MadelineProtoFan | 2022-05-31T22:29:12+00:00
did not do this

## MadelineProtoFan | 2022-05-31T22:31:28+00:00
Now i cannot enter _viewonly wallet! I can do it before 

## selsta | 2022-05-31T22:45:05+00:00
From the file size it does not seem (visibly) corrupted. And there is no known issue of what you are describing. Do you have a second PC? Can you copy wallet on USB stick and try on a different PC?

Also are you typing the password manually or do you use a password manager?

This here was unrelated and fixed: https://www.reddit.com/r/monerosupport/comments/hxqv2m/monero_gui_and_ledger_invalid_password/

## MadelineProtoFan | 2022-05-31T23:12:48+00:00
What a great support selsta! 5 stars!
So i installed GUI on the second laptop and put all passwords i know. And there was no password at all
The problem that on my first PC empty password - was incorrect password, I deleted GUI and restared my PC. And it works
Thanks you very much!!! Big pleasure that monero have such dev!

## selsta | 2022-05-31T23:14:12+00:00
Make sure to write down the seed now. Otherwise if your hard drive has issues you lose your funds.

> The problem that on my first PC empty password - was incorrect password, I deleted GUI and restared my PC. And it works
Thanks you very much!!! Big pleasure that monero have such dev!

Still not really sure what happened here but glad it's resolved.

# Action History
- Created by: MadelineProtoFan | 2022-05-31T21:52:42+00:00
- Closed at: 2022-05-31T23:14:12+00:00
