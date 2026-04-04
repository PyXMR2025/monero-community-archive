---
title: 'Error: failed to generate new wallet: failed to save file "./home/wallet1.keys"'
source_url: https://github.com/monero-project/monero/issues/3394
author: kevingwang
assignees: []
labels: []
created_at: '2018-03-13T07:43:42+00:00'
updated_at: '2022-03-16T15:36:02+00:00'
type: issue
status: closed
closed_at: '2022-03-16T15:36:02+00:00'
---

# Original Description
So many issues about  "failed to save  file ..." , but no body solve this problem , why ?

root@VM-0-2-ubuntu:/snap/bin# pwd
/snap/bin
root@VM-0-2-ubuntu:/snap/bin# ll -t
total 12
drwxrwxrwx 3 root root 4096 Mar 13 10:25 ./
drwxrwxrwx 2 root root 4096 Mar 13 10:25 home/
lrwxrwxrwx 1 root root   13 Mar 13 09:21 monero.monero-wallet-cli -> /usr/bin/snap*
lrwxrwxrwx 1 root root   13 Mar 13 09:21 monero.monero-wallet-rpc -> /usr/bin/snap*
drwxr-xr-x 5 root root 4096 Mar 13 09:21 ../


root@VM-0-2-ubuntu:/snap/bin# ./monero.monero-wallet-cli --log-level 3 --generate-new-wallet home/wallet1
Monero 'Helium Hydra' (v0.11.1.0-release)
Logging to /root/snap/monero/3
Enter new wallet password: ******
Confirm Password: ******
List of available languages for your wallet's seed:
0 : Deutsch
1 : English
2 : Español
3 : Français
4 : Italiano
5 : Nederlands
6 : Português
7 : русский язык
8 : 日本語
9 : 简体中文 (中国)
10 : Esperanto
Enter the number corresponding to the language of your choice: 1
Error: failed to generate new wallet: failed to save file "home/wallet1.keys"
root@VM-0-2-ubuntu:/snap/bin# 
root@VM-0-2-ubuntu:/snap/bin# 
root@VM-0-2-ubuntu:/snap/bin# ./monero.monero-wallet-cli --log-level 3 --generate-new-wallet /home/wallet1
Monero 'Helium Hydra' (v0.11.1.0-release)
Logging to /root/snap/monero/3
Enter new wallet password: ******
Confirm Password: ******
List of available languages for your wallet's seed:
0 : Deutsch
1 : English
2 : Español
3 : Français
4 : Italiano
5 : Nederlands
6 : Português
7 : русский язык
8 : 日本語
9 : 简体中文 (中国)
10 : Esperanto
Enter the number corresponding to the language of your choice: 1
Error: failed to generate new wallet: failed to save file "/home/wallet1.keys"
root@VM-0-2-ubuntu:/snap/bin# 
root@VM-0-2-ubuntu:/snap/bin# ./monero.monero-wallet-cli --log-level 3 --generate-new-wallet ./home/wallet1
Monero 'Helium Hydra' (v0.11.1.0-release)
Logging to /root/snap/monero/3
Enter new wallet password: ******
Confirm Password: ******
List of available languages for your wallet's seed:
0 : Deutsch
1 : English
2 : Español
3 : Français
4 : Italiano
5 : Nederlands
6 : Português
7 : русский язык
8 : 日本語
9 : 简体中文 (中国)
10 : Esperanto
Enter the number corresponding to the language of your choice: 1
Error: failed to generate new wallet: failed to save file "./home/wallet1.keys"




# Discussion History
## moneromooo-monero | 2018-03-13T09:38:41+00:00
You probably don't have a home directory in snap/bin, so path not found. Either give a path to somewhere you have write permissions to, or run the wallet from somewhere you do.

## kevingwang | 2018-03-14T00:58:40+00:00
I have home directory in snap/bin and the permission is 777.

root@VM-0-2-ubuntu:/snap/bin# pwd
/snap/bin
root@VM-0-2-ubuntu:/snap/bin# ll -t
total 12
drwxrwxrwx 3 root root 4096 Mar 13 10:25 ./
drwxrwxrwx 2 root root 4096 Mar 13 10:25 home/
lrwxrwxrwx 1 root root 13 Mar 13 09:21 monero.monero-wallet-cli -> /usr/bin/snap*
lrwxrwxrwx 1 root root 13 Mar 13 09:21 monero.monero-wallet-rpc -> /usr/bin/snap*
drwxr-xr-x 5 root root 4096 Mar 13 09:21 ../

## kevingwang | 2018-03-14T00:59:51+00:00
I try to use 
home/wallet1
or
/home/wallet1
or
./home/wallet1

, it doesn't work.

## kevingwang | 2018-03-14T01:00:52+00:00
Could you please it on Ubuntu ? Thanks!

## kevingwang | 2018-03-14T03:42:34+00:00
Always  failed to save file

root@VM-0-2-ubuntu:/snap/bin# ./monero.monero-wallet-cli --log-level 3 --generate-new-wallet  wallet1
Monero 'Helium Hydra' (v0.11.1.0-release)
Logging to /root/snap/monero/3
Enter new wallet password: ******
Confirm Password: ******
List of available languages for your wallet's seed:
0 : Deutsch
1 : English
2 : Español
3 : Français
4 : Italiano
5 : Nederlands
6 : Português
7 : русский язык
8 : 日本語
9 : 简体中文 (中国)
10 : Esperanto
Enter the number corresponding to the language of your choice: 1
Error: failed to generate new wallet: failed to save file "wallet1.keys"


## moneromooo-monero | 2018-03-14T09:38:30+00:00
Can you with with strace:

strace -o OUT ./monero.monero-wallet-cli --log-level 3 --generate-new-wallet wallet1

Then check what syscall fails with what error code in the OUT file.
Or paste the last 100 lines of OUT.


## kevingwang | 2018-03-15T02:28:37+00:00
I  downloaded another one from 
https://getmonero.org/downloads/#linux
and now it works normally.

That one with "failed to save file" bugs was downloaded from github:
https://github.com/monero-project/monero

## moneromooo-monero | 2018-03-15T09:18:25+00:00
OK,so a new bug.
Can you try with the github version, but reverting one patch:
git revert 430268224d71bfc6a359f20c6db712462ce0bb25

## bigjay4465 | 2018-10-31T23:05:59+00:00
Trying to login and this is what I am getting ERROR : Failed to upgrade to HD and save wallet Please help me with solution so I can pay  my school fees please thanks jk1070460@gmail.com

## moneromooo-monero | 2020-05-02T18:10:01+00:00
Doesn't looks like a monero error message. Report to whatever software you're using,

# Action History
- Created by: kevingwang | 2018-03-13T07:43:42+00:00
- Closed at: 2022-03-16T15:36:02+00:00
