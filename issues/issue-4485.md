---
title: Incorrect sha256 hash for binary verification Monero GUI fedora Linux
source_url: https://github.com/monero-project/monero-gui/issues/4485
author: hungrydragon1234
assignees: []
labels: []
created_at: '2025-08-07T16:20:47+00:00'
updated_at: '2025-08-07T19:22:53+00:00'
type: issue
status: closed
closed_at: '2025-08-07T19:22:53+00:00'
---

# Original Description
Hi
I am trying to verify my monero gui software on fedora Linux and successfully verified and imported the signing key and downloaded and verified the hash file but when I got to the binary the sha256 sum I got perfectly matched that for the the binary file called ‘Linux-risc64-v0.18.4.1.tar.bz2’ however, the binary that I installed was called ‘Linux-x64-v0.18.4.1.tar.bz2’ and the hashes file shows a different hash under that one which is very similar as it is also Linux??? What’s going on? Could it be an accidental mixup? I am of course refraining from using the software on Linux until I am certain of what the situation is? 
Thanks

# Discussion History
## nahuhh | 2025-08-07T17:11:29+00:00
You mean `monero-linux-x64-v0.18.4.1.tar.bz2`?

## hungrydragon1234 | 2025-08-07T17:26:59+00:00
Yes that is what i mean


## hungrydragon1234 | 2025-08-07T17:30:55+00:00
On the hashes.txt file it says this: l

monero-linux-riscv64-v0.18.4.1.tar.bz2
702ccb799c24160c0c76676d7a5b21a7e3432be47294d20e0a75451592f591b2  

monero-linux-x64-v0.18.4.1.tar.bz2
a36f57f7eeee15513cd51716a2f727fd84c7c1e5a8f48b30d69dd0b31aab4ee2 

Even thoughthe one i am verifying is monero-linux-x64-v0.18.4.1.tar.bz2 in the terminal I get the the sha256 sum 702ccb799c24160c0c76676d7a5b21a7e3432be47294d20e0a75451592f591b2 which corresponds to the riscv file


## hungrydragon1234 | 2025-08-07T17:33:10+00:00
What is going on please? It seems to me like a mix up on the part of the developers unless i am mistaken? because if there truly was something nefarious going on it would be unlikely that the signing keys and hash files would be successfully verified..

## selsta | 2025-08-07T17:40:47+00:00
Can you add more information? How did you download the updated monero-gui?

## hungrydragon1234 | 2025-08-07T17:48:30+00:00
I just went on getmonero.org and clicked on the linux link for the monero gui to download it. Then i followed the instructions for verification for the software. 
I then installed the signing key and verified it successfully.
I then verified the hash file successfully.
Then (as per the verification instructions) I ran the following in the terminal: shasum -a 256 monero-linux-x64-v0.18.4.1.tar.bz2                                     and got the following output:
702ccb799c24160c0c76676d7a5b21a7e3432be47294d20e0a75451592f591b2  monero-linux-x64-v0.18.4.1.tar.bz2
shasum -a 256 monero-linux-x64-v0.18.4.1.tar.bz2

If you look at the hashes.txt file you will see that this corresponds to the  monero-linux-riscv64-v0.18.4.1.tar.bz2   file.

Could someone let me know if they have this issue too? thanks

## selsta | 2025-08-07T17:49:47+00:00
I'm just confused because you said you wanted to update monero-gui but you are downloading CLI tools.

## hungrydragon1234 | 2025-08-07T17:50:01+00:00
I just went on getmonero.org and clicked on the linux link for the monero gui to download it. Then i followed the instructions for verification for the software.
I then installed the signing key and verified it successfully.
I then verified the hash file successfully.
Then (as per the verification instructions) I ran the following in the terminal: shasum -a 256 monero-linux-x64-v0.18.4.1.tar.bz2 and got the following output:
702ccb799c24160c0c76676d7a5b21a7e3432be47294d20e0a75451592f591b2 

If you look at the hashes.txt file you will see that this corresponds to that of the monero-linux-riscv64-v0.18.4.1.tar.bz2 file.

Could someone let me know if they have this issue too? thanks

## selsta | 2025-08-07T17:52:44+00:00
You seem to be looking at the wrong line. The format is `hash  filename`, and it correctly states

```
702ccb799c24160c0c76676d7a5b21a7e3432be47294d20e0a75451592f591b2  monero-linux-x64-v0.18.4.1.tar.bz2
```

## hungrydragon1234 | 2025-08-07T17:55:16+00:00
Hi Where did you get that? my hashes file doesnt say that

## selsta | 2025-08-07T17:56:26+00:00
https://www.getmonero.org/downloads/hashes.txt

Try to increase the width of your browser to see it more clearly.

## hungrydragon1234 | 2025-08-07T17:57:39+00:00
AHHH its fine now. Thank you so much god bless you

## hungrydragon1234 | 2025-08-07T17:58:16+00:00
Although i still dont get why having downloaded the monero gui wallet the shasum corresponds to that of a cli wallet??


## selsta | 2025-08-07T17:59:25+00:00
You did not download the monero-gui wallet. The monero-gui wallet file name should be `monero-gui-linux-x64-v0.18.4.1.tar.bz2`. You downloaded the CLI tools.

## hungrydragon1234 | 2025-08-07T18:00:57+00:00
but im looking at my download file now and it definitely says monero-gui-linux-x64-v0.18.4.1.tar.bz2

## hungrydragon1234 | 2025-08-07T18:02:43+00:00
could it be that i input something wrong in the terminal? because i followed what the verification instructions said on the site

## hungrydragon1234 | 2025-08-07T18:03:25+00:00
The heading of the page on getmonero.org is: How to use the command line to verify your Monero CLI/GUI software is safe (advanced)

## selsta | 2025-08-07T18:04:16+00:00
15 minutes ago you wrote in your comment that you entered the following command

```
shasum -a 256 monero-linux-x64-v0.18.4.1.tar.bz2
```

which is not the `monero-gui` file as you can see from the filename and the missing `gui`. Please double check everything you are doing.

## hungrydragon1234 | 2025-08-07T18:06:44+00:00
Ah ok- because i was just following the instructions on the getmonero.org page. I did not realise that it wasnt a gui file

## hungrydragon1234 | 2025-08-07T18:07:38+00:00
So what input am i supposed to put to verify the shasum of the monerogui wallet?

## hungrydragon1234 | 2025-08-07T18:10:39+00:00
Its my first time doing this i didnt realise that the command related to CLI. But surely they should put what input is required to verify the shasum of a gui wallet not just CLI in the instructions?

## selsta | 2025-08-07T18:11:46+00:00
There are different operating systems, you have to input the correct filename. The guide can't take into account all different operating systems.

First you have to download monero-gui for Linux from here https://www.getmonero.org/downloads/

and then enter

shasum -a 256 monero-linux-x64-v0.18.4.1.tar.bz2

## hungrydragon1234 | 2025-08-07T18:14:13+00:00
I definitely downloaded monero gui from getmonero.org though? i can see it in my donwloads folder both unextracted and also extracted

## hungrydragon1234 | 2025-08-07T18:14:55+00:00
ill donwload it agaiinn and see what happens

## hungrydragon1234 | 2025-08-07T18:17:16+00:00
so i deleted the gui that was donwloaded and redownloaded the gui wallet and immediately ran the shasum verification in the terminal but it say NO SUCH FILE OR DIRECTORY


## hungrydragon1234 | 2025-08-07T18:17:38+00:00
I ran shasum -a 256 monero-linux-x64-v0.18.4.1.tar.bz2


## selsta | 2025-08-07T18:18:59+00:00
Please try to read the commands you are entering. You entered the filename for CLI and not GUI

```
shasum -a 256 monero-linux-x64-v0.18.4.1.tar.bz2
```

you have to enter instead

```
shasum -a 256 monero-gui-linux-x64-v0.18.4.1.tar.bz2
```

## hungrydragon1234 | 2025-08-07T18:27:17+00:00
Can i just check? if it says donwload the binary it just means download the actual monero gui file which do not have to do via the terminal andi can just do by clikcing on download?

## hungrydragon1234 | 2025-08-07T18:32:02+00:00
Ok so i just entered:                                                                                                                                            wget -O monero-gui-linux-x64-v0.18.4.1.tar.bz2 https://downloads.getmonero.org/cli/linux64

Once its done i will verify the shasum and see what happens. perhaps it is necessary to download the binary via the terminal lnot just by clicking in order to download it in order to verify the shawsum

## hungrydragon1234 | 2025-08-07T18:34:46+00:00
I appreciate your patience and help btw

## hungrydragon1234 | 2025-08-07T18:43:21+00:00
PLEASE can you tell me- is this the correct wget command to download the gui binary via terminal:                                                                                                                          wget -O monero-gui-linux-x64-v0.18.4.1.tar.bz2 https://downloads.getmonero.org/gui/linux64

because when i input it it says command not found?




## selsta | 2025-08-07T18:47:10+00:00
Yes, that is one way to download the software. Can you tell me which command is not found?

## hungrydragon1234 | 2025-08-07T18:48:32+00:00
this 

wget -O monero-gui-linux-x64-v0.18.4.1.tar.bz2 https://downloads.getmonero.org/gui/linux64


## hungrydragon1234 | 2025-08-07T18:48:52+00:00
it says ~$: command not found...



## hungrydragon1234 | 2025-08-07T18:50:04+00:00
Ok for some reason it works now

## hungrydragon1234 | 2025-08-07T18:50:24+00:00
i closed and reopened the terminall and now it is downloading

## hungrydragon1234 | 2025-08-07T19:09:09+00:00
Finally it worked!!!

## hungrydragon1234 | 2025-08-07T19:09:20+00:00
Thank you so much

## selsta | 2025-08-07T19:22:53+00:00
Glad to hear that you resolved the issue.

# Action History
- Created by: hungrydragon1234 | 2025-08-07T16:20:47+00:00
- Closed at: 2025-08-07T19:22:53+00:00
