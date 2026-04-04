---
title: 'Feature request: Working with key images (export unsigned / import unsigned)'
source_url: https://github.com/monero-project/monero/issues/1236
author: JollyMort
assignees: []
labels: []
created_at: '2016-10-18T22:55:49+00:00'
updated_at: '2016-10-31T07:42:25+00:00'
type: issue
status: closed
closed_at: '2016-10-31T07:42:25+00:00'
---

# Original Description
I understand that there's some [confusion](http://monero.stackexchange.com/questions/2396/how-can-we-view-the-balance-of-a-cold-wallet-storage-and-keep-it-cold) around as to how the process with key images works, and what it can be used for.

For now, there are the 2 commands (export_key_images, import_key_images). The export is done from the full-wallet, but the wallet needs to have record of all the outputs as to generate them so it has to be online (or blockchain db copied over, which is cumbersome). They are then imported into the view-wallet, which will then show the correct ballance. This is all nice for auditing etc., but not for cold storage.

For cold storage, I believe we need another 2 commands:
export_unsigned_key_images
import_unsigned_key_images

The first would be called from a fully-synced view-wallet, and the unsigned key images would be copied over to the cold wallet and imported using the 2nd function. Then, export_key_images would be called, the signed key images copied over to the view-walet, imported using import_key_images, and voila, you have the correct balance.

Any takers?


# Discussion History
## moneroexamples | 2016-10-19T02:52:57+00:00
Why current setup is not good for cold storage? 


## expez | 2016-10-19T06:04:51+00:00
Check this explanation out @JollyMort: http://monero.stackexchange.com/questions/2160/how-do-i-use-cold-transaction-signing


## JollyMort | 2016-10-19T08:45:25+00:00
I'm aware of the cold transaction signing, _but_.

As I understand it, current process for cold wallet monitoring / spending is as follows:
0. Initial status: cold wallet never refreshed, watch wallet fully synced
1. **copy** the blockchain db (or .raw file) to the cold wallet
2. refresh cold wallet
3. export key images
4. **copy** them to the watch wallet
5. import key images
--- stop here if we only want to monitor the balance, goto 1. after each newly received funds ---
6. export unsigned transaction
7. **copy** them to the cold wallet
8. sign
9. export signed transaction
10. **copy** it to the watch wallet
11. broadcast
12. goto 1. because you need the signed key image for the change output

So, depending on what we're doing, we need to copy 10GB+ at least 1 time initially, then 1 more time for each update, and 2 more times for each spending. Doesn't seem reasonable. Today, 10GB+ is still a pain to copy to a pen drive.
I understand you don't need to follow all the steps, but in some cases it could result in an error (i.e. you skip 1. to 5. but some output had been spent by other means and now the wallet is attempting a double-spend because it couldn't have known that it can't use a certain output)
Making step 1. copy only what it really needs to copy (outputs belonging to the wallet) would make the process lighter and would enable some other means of transport feasible (bluetooth?).
Also, what if the user is connecting to a remote node? Then, he doesn't have the db to copy.

Am I missing something?


## moneroexamples | 2016-10-20T06:10:02+00:00
This can be done "almost" now using other tools than simplewallet. Namely using `transaction-export` tool: https://github.com/moneroexamples/transactions-export

The tool is not finished, as I work on other things now, but it could be modified, rather easily, to what you are trying to achieve. At least if I understand it correctly.

But something like that build into simpelwallet, could be useful as well.


## moneromooo-monero | 2016-10-20T18:12:47+00:00
That makes sense. I didn't realize this part was missing for that use case :)
I'd make the functions more like "export_outputs" and "import_outputs", since we'll need a bit more data, and the cold wallet cab check the outputs really belong to it  (I've  not looked at the code yet).


## moneromooo-monero | 2016-10-30T19:54:00+00:00
https://github.com/monero-project/monero/pull/1281


## JollyMort | 2016-10-31T07:42:25+00:00
Awesome, thank you!


# Action History
- Created by: JollyMort | 2016-10-18T22:55:49+00:00
- Closed at: 2016-10-31T07:42:25+00:00
