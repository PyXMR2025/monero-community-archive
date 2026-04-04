---
title: 'Failed to generate new wallet '
source_url: https://github.com/monero-project/monero/issues/193
author: netmonk
assignees: []
labels: []
created_at: '2014-12-01T21:25:20+00:00'
updated_at: '2016-04-01T08:50:21+00:00'
type: issue
status: closed
closed_at: '2016-04-01T08:50:21+00:00'
---

# Original Description
netmonk@plonky:~/bm/bm2/bitmonero/build/release/bin$ ./simplewallet --daemon-address xmr1.coolmining.club:5012 
bitmonero wallet v0.8.8.4-e1555fd
Specify wallet file name (e.g., wallet.bin). If the wallet doesn't exist, it will be created.
Wallet file name: ~/donation.bin
The wallet doesn't exist, generating new one
password: ********
List of available languages for your wallet's seed:
0 : English
1 : Spanish
2 : Portuguese
3 : Japanese
Enter the number corresponding to the language of your choice: 0
Error: failed to generate new wallet: failed to save file "~/donation.bin.keys"

When asked for wallet name, it seems "~/"  in the name of wallet to instruct wich path to save the file makes the whole process fail on linux.


# Discussion History
## fluffypony | 2014-12-01T21:34:39+00:00
Do you have write permissions in that folder? On Linux, ~ just means "current folder", so ~/whatever.bin.keys just means "create that in the current folder", which is the correct and expected behaviour.


## netmonk | 2014-12-01T21:36:14+00:00
"~/" means home directory so /home/netmonk and yes i have the write right as far as i run under netmonk user 


## netmonk | 2014-12-01T21:38:01+00:00
netmonk@plonky:~$ touch toto
netmonk@plonky:~$ ls -altr toto
-rwxr-xr-x 1 netmonk netmonk 7269 Dec  1 22:37 toto
netmonk@plonky:~$ pwd
/home/netmonk
netmonk@plonky:~$ cd -
/home/netmonk/bm/bm2/bitmonero/build/release/bin
netmonk@plonky:~/bm/bm2/bitmonero/build/release/bin$ ./simplewallet --daemon-address xmr1.coolmining.club:5012  
bitmonero wallet v0.8.8.4-e1555fd
Specify wallet file name (e.g., wallet.bin). If the wallet doesn't exist, it will be created.
Wallet file name:  
The wallet doesn't exist, generating new one
password: 
netmonk@plonky:~/bm/bm2/bitmonero/build/release/bin$ ./simplewallet --daemon-address xmr1.coolmining.club:5012 
bitmonero wallet v0.8.8.4-e1555fd
Specify wallet file name (e.g., wallet.bin). If the wallet doesn't exist, it will be created.
Wallet file name: ~/test.bin
The wallet doesn't exist, generating new one
password: ********
List of available languages for your wallet's seed:
0 : English
1 : Spanish
2 : Portuguese
3 : Japanese
Enter the number corresponding to the language of your choice: 0
Error: failed to generate new wallet: failed to save file "~/test.bin.keys"
netmonk@plonky:~/bm/bm2/bitmonero/build/release/bin$ 


## netmonk | 2014-12-01T21:48:21+00:00
netmonk@plonky:~/bm/bm2/bitmonero/build/release/bin$ ./simplewallet --daemon-address xmr1.coolmining.club:5012 
bitmonero wallet v0.8.8.4-e1555fd
Specify wallet file name (e.g., wallet.bin). If the wallet doesn't exist, it will be created.
Wallet file name: ~/plop.bin
The wallet doesn't exist, generating new one
password: 
netmonk@plonky:~/bm/bm2/bitmonero/build/release/bin$ ./simplewallet --daemon-address xmr1.coolmining.club:5012 
bitmonero wallet v0.8.8.4-e1555fd
Specify wallet file name (e.g., wallet.bin). If the wallet doesn't exist, it will be created.
Wallet file name: /home/netmonk/plop.bin
password: 
netmonk@plonky:~/bm/bm2/bitmonero/build/release/bin$ 

It seems that providing full path instead of "~/" is working 


## fluffypony | 2014-12-01T21:50:44+00:00
Oh fail, in my brain I read it as ./

Sorry

I'll take a looks and see what I can see :)


## netmonk | 2014-12-01T21:52:06+00:00
I forgive you :)


## fluffypony | 2014-12-01T21:52:33+00:00
hah hah - you're too kind ;)


## benma | 2015-12-25T01:01:20+00:00
I have the same issue. No matter what name or path I enter, it fails. Some files are generated, though:

mywallet.address.txt  mywallet.keys  mywallet.new


## fhirschmann | 2016-01-09T18:16:33+00:00
Can you try it again with `--wallet-file=/home/$USER/.bitmonero/wallet.dat` instead of `~/.bitmonero/wallet.dat`?

Simplewallet does not seem to expand `~` to `/home/$USER`.

Normally this should be done by the shell, but expansion only works if the parameter reads `--wallet-file ~/.bitmonero/wallet.dat` and not `--wallet-file=~/.bitmonero/wallet.dat`.


## moneromooo-monero | 2016-03-20T12:47:00+00:00
As said above, ~ is a shell thing, so ~/something would save in a relative directory called ~, which you probably don't have. This can probably be closed. For the general case, I don't think we want to create directories if they don't exist, but I could be persuaded otherwise.


# Action History
- Created by: netmonk | 2014-12-01T21:25:20+00:00
- Closed at: 2016-04-01T08:50:21+00:00
