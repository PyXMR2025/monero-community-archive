---
title: SpendProof "Invalid signature size" / no further documentations
source_url: https://github.com/monero-project/monero/issues/3761
author: codexx420
assignees: []
labels: []
created_at: '2018-05-06T11:44:50+00:00'
updated_at: '2018-05-12T10:28:40+00:00'
type: issue
status: closed
closed_at: '2018-05-08T16:45:37+00:00'
---

# Original Description
Hello!
I'm working a lot with the monero cli/rpc tools. Recently, the beautiful developers added a function to prove spent transaction without the need of the tx key/view key. Sadly, all of the generated SpendProofs are not working. I'm getting "Error: incorrect signature size" when I check the spendproofs with the check_spend_proof cli command.
I'm **not getting this error** if I generate the spent proof with the same wallet binaries and local bitmonero files (e.g. chain data).
But when I use separate local bitmonero files, it won't work.  (Incorrect signature size). 

Are there any documentations or informtion to that or am I missing something? 

# Discussion History
## stoffu | 2018-05-06T12:02:53+00:00
Admittedly it's not documented well; the code is the only documentation at the moment.

The most likely cause of your problem is that you put some additional character (probably newline) to the file that stores the signature data (the equivalent of `monero_spend_proof` file generated with the CLI wallet). The file must not contain any additional characters.

## itssteven | 2018-05-06T14:13:35+00:00
As far as I can see, this happens if you check a different txid than the one which was used to create the signature.

I'm using this temporary fix to overcome the issue when working with monerophp: https://github.com/monero-integrations/monerophp/pull/74

It's as if the code checks what the valid length for the signature would be with the txid you provide and returns an error rather than a signature=bad return.

the error is "incorrect signature size", not "invalid signature size". 8379 of wallet2.cpp

## stoffu | 2018-05-06T23:27:00+00:00
@itssteven 
> As far as I can see, this happens if you check a different txid than the one which was used to create the signature.

Yes, the signature size is in proportion to the number of inputs and the ring size, which means it can become quite large sometimes, which is why the CLI writes the signature to a file instead of displaying it on the console.


## codexx420 | 2018-05-08T16:45:18+00:00
Hello,
thanks for the fast answers! you're awesome. of course it was that issue:
> The most likely cause of your problem is that you put some additional character (probably newline) to the file that stores the signature data (the equivalent of monero_spend_proof file generated with the CLI wallet). The file must not contain any additional characters.

A small note: using nano (even by deleting the last line) and ```echo "SpendProofV1..." > file ``` creates a newline char at the end of the file. 
Now it works!

**Edit:**
Helpful shortcut: ```truncate -s -1 file```

## itssteven | 2018-05-12T10:26:57+00:00
@stoffu 
> Yes, the signature size is in proportion to the number of inputs and the ring size, which means it can become quite large sometimes, which is why the CLI writes the signature to a file instead of displaying it on the console.

No, that's not my issue. When checking the spend proof, if it's checked with a txid the spendproof wasn't signed with, it returns an error rather than a "signature=bad" as it would if you checked an invalid spendproof. This is fine for the CLI because it makes no difference to the user, but when using the RPC you will get an error rather than a "signature=bad" return. There should be no error, as far as I can see.

Edit: I see you've approved my fix, so ignore this I guess. Thanks!

# Action History
- Created by: codexx420 | 2018-05-06T11:44:50+00:00
- Closed at: 2018-05-08T16:45:37+00:00
