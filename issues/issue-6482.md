---
title: 'start monero-wallet-rpc.exe command report a error with" No message store
  file found: testwallet.mms"'
source_url: https://github.com/monero-project/monero/issues/6482
author: niukouMan
assignees: []
labels: []
created_at: '2020-04-27T14:01:08+00:00'
updated_at: '2020-06-01T11:50:55+00:00'
type: issue
status: closed
closed_at: '2020-06-01T11:50:55+00:00'
---

# Original Description
start monero-wallet-rpc.exe command in windows environmentreport a error with" No message store file found: testwallet.mms" 

**Execute the command as follows** :
D:\softwar\wallet\monero-win-x64-v0.15.0.5\monero-x86_64-w64-mingw32-v0.15.0.5> .\monero-wallet-rpc.exe --stagenet --rpc-bind-ip 0.0.0.0 --rpc-bind-port 38089 --confirm-external-bind --rpc-login test:123456 --daemon-address monero-stagenet.exan.tech:38081 --password 123 --wallet-file testwallet
This is the RPC monero wallet. It needs to connect to a monero
daemon to work correctly.

Monero 'Carbon Chamaeleon' (v0.15.0.5-release)
Logging to D:\softwar\wallet\monero-win-x64-v0.15.0.5\monero-x86_64-w64-mingw32-v0.15.0.5\monero-wallet-rpc.log
2020-04-27 10:07:43.219 W Loading wallet...
2020-04-27 10:07:43.228 I Generating SSL certificate
2020-04-27 10:07:44.091 I Generating SSL certificate
2020-04-27 10:07:44.997 W Loaded wallet keys file, with public address: 57XTcQx7eVmGm8AMWs3fWNTBTQ8W1kukt9hGicdge8sCZk3cB752YYCNmWWsVmjRwpfBe3E6gHuAA8xJzPNTTvB37vGKyiS
2020-04-27 10:07:45.028 E No message store file found: testwallet.mms



# Discussion History
## selsta | 2020-04-27T15:02:39+00:00
You can ignore the `No message store file found` error message.

I don’t see a relevant error in the logs. What is the exact problem?
Can you try a different stagenet node? E.g. from here https://community.xmr.to/nodes.html

## niukouMan | 2020-04-27T15:16:02+00:00

./monero-wallet-rpc.exe --stagenet  --rpc-bind-port 38089 --confirm-external-bind --rpc-login test:123456 --daemon-address node.xmr.to:38081  --password 123 --wallet-file testwallet

This is the RPC monero wallet. It needs to connect to a monero
daemon to work correctly.
Monero 'Carbon Chamaeleon' (v0.15.0.5-release)
Logging to F:\Collin\monero-win-x64-v0.15.0.5\monero-x86_64-w64-mingw32-v0.15.0.5\monero-wallet-rpc.log
2020-04-27 15:13:42.853 W Loading wallet...
2020-04-27 15:13:43.169 I Generating SSL certificate
2020-04-27 15:13:43.653 I Generating SSL certificate
2020-04-27 15:13:45.015 W Loaded wallet keys file, with public address: 59kGwHD7XxHjarpCvp7i4dSeErRRQaXA7dwvSZSQQpFH54dDB3V4KzCh2fsKXHJK1SLV88S7yAP7xUPgLx8QphyD65WQezw
2020-04-27 15:13:45.114 E ****No message store file found: testwallet.mms**


![QQ截图20200427231354](https://user-images.githubusercontent.com/18626089/80388900-04ecd000-88dd-11ea-9d28-263c7c95aeb9.png)
**


## niukouMan | 2020-04-27T15:16:39+00:00
@selsta 

## selsta | 2020-04-27T15:27:46+00:00
What is your exact goal with monero-wallet-rpc? I don’t see any relevant errors in the logs.

## niukouMan | 2020-04-27T15:35:42+00:00
There was an error in execution _monero-wallet-rpc.exe_ command 
the error is " No message store file found: testwallet.mms"
i do not known the file **.mms is for
his file was not generated when execute _monero-wallet-cli.exe_ command to created the wallet 
![QQ截图20200427233456](https://user-images.githubusercontent.com/18626089/80391030-c9073a00-88df-11ea-8324-be039aaaed0c.png)
@selsta 

## moneromooo-monero | 2020-04-27T15:42:25+00:00
Is your report just "there is this line that gets printed" or "there is this line that gets printed and something does not work" ? The mms file is used for high level mulisig ops, it gets created if you use these ops.

## rbrunner7 | 2020-05-02T13:04:23+00:00
I think the confusing thing is that it is output as an **error**. I see this as a mistake now that I take responsibility for. It should be a warning at most, as in 99% of all cases there won't be a `.mms` file because people don't do multisig with the help of the MMS, and that missing file is perfectly ok.

I will make a PR to change that.

## moneromooo-monero | 2020-05-02T17:11:23+00:00
There is already one.

## moneromooo-monero | 2020-06-01T11:50:55+00:00
Fixed.

# Action History
- Created by: niukouMan | 2020-04-27T14:01:08+00:00
- Closed at: 2020-06-01T11:50:55+00:00
