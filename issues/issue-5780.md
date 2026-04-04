---
title: monero-wallet-cli "bug/error" v0.14.1.2
source_url: https://github.com/monero-project/monero/issues/5780
author: lh1008
assignees: []
labels: []
created_at: '2019-07-28T19:13:14+00:00'
updated_at: '2022-02-19T04:51:02+00:00'
type: issue
status: closed
closed_at: '2022-02-19T04:51:02+00:00'
---

# Original Description
Hey everyone,

Operating system Ubuntu 18.04.2 LTS

Yesterday I updated to v0.14.1.2 for the `monero-wallet-cli`. I was about to use it and found something funny happening using the terminal. 

I will try to be as clear as I can. I opened the wallet, as usual, the wallet is completely synced, no problems at all, all the information shows up as always. 

![wallet_1](https://user-images.githubusercontent.com/7443480/62011668-ff413e80-b140-11e9-8de1-ef24697411c6.png)

![wallet_4](https://user-images.githubusercontent.com/7443480/62011704-6a8b1080-b141-11e9-9857-7677ee4afc94.png)


When I'm about to make a transfer or use any command, `balance`, `refresh`, `help`, etc., when pressing `enter` to make the call, the lines jumps. When using the `back-space` key, instead of deleting it goes forward (I opened several other terminals and only while having the `monero-wallet-cli` opened this happens). Here are the images:

![bugs_1](https://user-images.githubusercontent.com/7443480/62011519-fc454e80-b13e-11e9-83b7-9dfe0f82cf5e.png)

If I continue on and try to make a transfer it just gets worse. The XMR address doesn't show up completely but only half of it. When I try to `back-space` it just keeps in an endless party:

![bugs_3](https://user-images.githubusercontent.com/7443480/62011616-23505000-b140-11e9-9d0f-9cd62d258825.png)


I used this reddit thread to update the CLI https://www.reddit.com/r/Monero/comments/cg3zih/cli_v01412_boron_butterfly_released/. I also checked the integrity of the binaries and everything was normal as always, didn't have any issues in the past. 

Not sure if anyone has encountered any issues but I did. Any help or recommendation will be really appreciated.  Wasn't able to make the transfer because I don't know if it will go through with this error. 

Thanks

# Discussion History
## lh1008 | 2019-07-28T19:23:22+00:00
Got this invalid last argument with the first part of the transfer while trying to exit the wallet:

![error](https://user-images.githubusercontent.com/7443480/62011817-1bde7600-b143-11e9-8999-19c368394956.png)

The `exitexxsdwdwwexit` was me trying to exit the wallet.

## lh1008 | 2019-07-28T22:09:40+00:00
One more thing, I rebooted my pc, turned it off and the issue keeps on showing up only in the `monero-wallet-cli`.

## selsta | 2019-07-29T15:21:23+00:00
Same issue for me on macOS.

## jtgrassie | 2019-07-29T15:25:08+00:00
This seems to be an issue with the reproducible builds and readline. Building from source doesn't show this issue. 

## lh1008 | 2019-07-29T19:31:47+00:00
Thank you @jtgrassie for your answer. @selsta you could go back to v0.14.1.0, it seems there is a readline bug.

Closing this issue. Here is @dEBRUYNE-1 answer from reddit:

https://www.reddit.com/r/Monero/comments/cj9c2d/maam_monero_ask_anything_monday_july_29_2019/evcf28f?utm_source=share&utm_medium=web2x

Thank you community

>:)

## jtgrassie | 2019-08-01T03:49:24+00:00
This should be reopened. The bug exists in the current release binaries.

## lh1008 | 2019-08-01T22:34:59+00:00
@jtgrassie reopened

## dougEfresh | 2019-08-13T15:38:09+00:00
I can confirm that this happens when I compile from source. 
`stty -a`
`speed 38400 baud; rows 59; columns 213; line = 0;
intr = ^C; quit = ^\; erase = ^?; kill = ^U; eof = ^D; eol = <undef>; eol2 = <undef>; swtch = <undef>; start = ^Q; stop = ^S; susp = ^Z; rprnt = ^R; werase = ^W; lnext = ^V; discard = ^O; min = 1; time = 0;
-parenb -parodd -cmspar cs8 -hupcl -cstopb cread -clocal -crtscts
-ignbrk -brkint -ignpar -parmrk -inpck -istrip -inlcr -igncr icrnl ixon -ixoff -iuclc -ixany -imaxbel iutf8
opost -olcuc -ocrnl onlcr -onocr -onlret -ofill -ofdel nl0 cr0 tab0 bs0 vt0 ff0
isig icanon iexten echo echoe echok -echonl -noflsh -xcase -tostop -echoprt echoctl echoke -flusho -extproc
` 
`echo $TERM `
`xterm-256color`


## wartjugger | 2019-10-03T04:51:22+00:00
Is it possible to make a point release fixing that? where does one even go to get the 0.14.1.0 binaries?

## erciccione | 2019-10-03T11:23:42+00:00
> Is it possible to make a point release fixing that?

We have a major release in one month, no need for a point release. We only need somebody to work on this before the code freeze.

## selsta | 2022-02-19T04:51:02+00:00
Readline works properly in release binaries now.

# Action History
- Created by: lh1008 | 2019-07-28T19:13:14+00:00
- Closed at: 2022-02-19T04:51:02+00:00
