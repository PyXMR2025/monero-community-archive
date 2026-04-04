---
title: Error at startup monero-wallet-gui.exe
source_url: https://github.com/monero-project/monero-gui/issues/4009
author: mickhaorex
assignees: []
labels: []
created_at: '2022-08-19T09:51:58+00:00'
updated_at: '2022-08-20T01:41:41+00:00'
type: issue
status: closed
closed_at: '2022-08-20T01:41:41+00:00'
---

# Original Description
I downloaded the program to my computer. After the launch monero-wallet-gui.exe it turns out this error:
![Screen 18-08-2022 143737](https://user-images.githubusercontent.com/99164289/185593291-973e9900-093e-4628-96d3-31b01825db18.jpg)

What could be the problem and how to solve it?
The operating system is windows 7 x64.

# Discussion History
## selsta | 2022-08-19T10:45:45+00:00
- Did you use the .zip or the installer?
- Do you have an anti virus?
- Did you start as admin?

## mickhaorex | 2022-08-20T00:40:05+00:00
• I used the installer, but also tried the portable version.
• I turned off Avast antivirus before launching the program.
• I started the program as an administrator.

I guess the mistake is that my username is cyrillic "Администратор".

I also tried to run your program on my wife's laptop, with the same operating system, windows version and antivirus. But her username is called in English letters. On her laptop, the program started without any problems. But I need your program on my computer, because there is no permanent access to my wife's laptop.

## selsta | 2022-08-20T00:41:52+00:00
Yes, it is likely the same issue as #4002.

Can you save the wallet on C:/ folder? Then there should be no issues with cyrillic in path.

## mickhaorex | 2022-08-20T00:45:12+00:00
I have very little free space on the C:/ drive, since a 60 GB SSD is used. But if there are no other options, then I can try. Only it seems to me he will still get access to %userprofile%

## selsta | 2022-08-20T00:46:39+00:00
Saving a wallet file does not require much space. You can also save it somewhere else, just make sure that there's no cyrillic in the path.

## mickhaorex | 2022-08-20T01:04:32+00:00
Wallet in the root of the "C" disk:\" , Here are all screenshots during the installation of the program:
![Скриншот 20-08-2022 055211](https://user-images.githubusercontent.com/99164289/185723335-f8060e45-346a-49db-b61d-c8cb72498615.jpg)
![Скриншот 20-08-2022 055330](https://user-images.githubusercontent.com/99164289/185723414-0023b77b-c0e9-450b-aab6-b32071c85d5a.jpg)
![Скриншот 20-08-2022 055525](https://user-images.githubusercontent.com/99164289/185723345-7e33a1d3-77c0-488f-9929-d184e70d0db9.jpg)
![Скриншот 20-08-2022 055617](https://user-images.githubusercontent.com/99164289/185723347-08590ad1-72e4-453b-867a-5f74eb97fc21.jpg)
![Скриншот 20-08-2022 055709](https://user-images.githubusercontent.com/99164289/185723348-25027c66-1587-4f02-9583-635e3d5c580d.jpg)
![Скриншот 20-08-2022 055731](https://user-images.githubusercontent.com/99164289/185723349-af24cb3c-9dbc-4fc3-85dc-87cea5e6d000.jpg)



## selsta | 2022-08-20T01:06:44+00:00
Can you create a second Windows account? Or rename your existing one? That will be easiest solution until we solve this issue.

## mickhaorex | 2022-08-20T01:10:07+00:00
I'm afraid to rename an existing account. Suddenly there will be any problems with other programs, I have heard this happens. But I will create a new account with a Latin name now. I'll write as soon as I do. Thank you!

## mickhaorex | 2022-08-20T01:29:49+00:00
I created the user "test". Logged in as a new user. Now the program has started normally. So now I have to run monero-wallet-gui on behalf of another user all the time?

## selsta | 2022-08-20T01:34:17+00:00
No, you can copy the wallet created with the second account to a place in the first account without cyrillic in path. The issue with AppData is only relevant during wallet creation, if a wallet is created it should not happen anymore. Then you can delete the second Windows account again.

## mickhaorex | 2022-08-20T01:40:47+00:00
Thanks again for your help, everything is working now!

## selsta | 2022-08-20T01:41:41+00:00
Closing this in favor of #4002

# Action History
- Created by: mickhaorex | 2022-08-19T09:51:58+00:00
- Closed at: 2022-08-20T01:41:41+00:00
