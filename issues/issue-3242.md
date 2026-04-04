---
title: incorrect index and label output by "address" command when switched to a subaddress
  account
source_url: https://github.com/monero-project/monero/issues/3242
author: nasaWelder
assignees: []
labels: []
created_at: '2018-02-08T04:50:03+00:00'
updated_at: '2018-02-08T05:33:31+00:00'
type: issue
status: closed
closed_at: '2018-02-08T05:27:37+00:00'
---

# Original Description
(with monero-static-ubuntu-amd64 | buildnumber | 3496)
The "address" command displays incorrect index and label when I've switched to a subaddress.
I would've expected:

> 1  8BZUjeuFQKS7ZQifMakLqM9B6ZtRLQRgd3Mo6cgQVSm9aLPeiMVQMaGTkn4L9tJB65P2Z7qXwoGdNDSUhoM6tqqpKn7TSXD  lorem ipsum

but I got:

> 0  8BZUjeuFQKS7ZQifMakLqM9B6ZtRLQRgd3Mo6cgQVSm9aLPeiMVQMaGTkn4L9tJB65P2Z7qXwoGdNDSUhoM6tqqpKn7TSXD  Primary address 

    [wallet 88FfPT (no daemon)]: account switch 1
     Currently selected account: [1] lorem ipsum
     Tag: adult
     Balance: 0.000000000000, unlocked balance: 0.000000000000
 
     [wallet 8BZUje (no daemon)]: address
     0 8BZUjeuFQKS7ZQifMakLqM9B6ZtRLQRgd3Mo6cgQVSm9aLPeiMVQMaGTkn4L9tJB65P2Z7qXwoGdNDSUhoM6tqqpKn7TSXD  Primary address 




# Discussion History
## stoffu | 2018-02-08T05:01:25+00:00
That's a correct behavior because you issued the `address` command after switching to an account index 1. The original wallet address corresponds to the 0-th address of the 0-th account.

## nasaWelder | 2018-02-08T05:23:34+00:00
@stoffu so sounds like plain old user error? accounts are not subaddresses? when I do "address new" it doesn't show up under accounts, there are now two (sub?)addresses with a number 1 associated with them, one under "address all" (1  887SVTj), and one under "accounts" (1 8BZUje)

    [wallet 42gxST (no daemon)]: address new wtf
    1  887SVTj8Gbr27fy8mixWSSLhocJ8hg2Dx6VcYnQMvVu1LUhWMZ8MAaGfRJ8eAVzbfdNKZwej1Us3d5FKRcH9appb6ygBKeR  wtf 
    [wallet 42gxST (no daemon)]: account
    Accounts with tag: adult
    Tag's description: 
              Account               Balance      Unlocked balance                 Label
             1 8BZUje        0.000000000000        0.000000000000           lorem ipsum
    ----------------------------------------------------------------------------------
              Total        0.000000000000        0.000000000000

    Accounts with tag: family
    Tag's description: mouths to feed
              Account               Balance      Unlocked balance                 Label   
             2 88FfPT        0.000000000000        0.000000000000       shopping budget
    ----------------------------------------------------------------------------------
          Total        0.000000000000        0.000000000000

    Untagged accounts:
          Account               Balance      Unlocked balance                 Label
     *       0 42gxST        0.000000000000        0.000000000000          the main one
             3 8BKb9Q        0.000000000000        0.000000000000             subofsub?
    ----------------------------------------------------------------------------------
              Total        0.000000000000        0.000000000000

    Grand total:
      Balance: 0.000000000000, unlocked balance: 0.000000000000
    [wallet 42gxST (no daemon)]: address all 
    0  42gxSTkWrC7UbTTQAAW2yGVY4hSmrkBqGQ13ukSjoep9JrEcNbgrERnjd6FptzLrEuCWGkwYpdS2K7UVLNmvCS922ngKS94  Primary address 
    1  887SVTj8Gbr27fy8mixWSSLhocJ8hg2Dx6VcYnQMvVu1LUhWMZ8MAaGfRJ8eAVzbfdNKZwej1Us3d5FKRcH9appb6ygBKeR  wtf 



## nasaWelder | 2018-02-08T05:27:37+00:00
looks like I misunderstood. appears each account can have subaddresses. Hadn't seen that mentioned.

## stoffu | 2018-02-08T05:33:31+00:00
The documentation is admittedly insufficient; for now, you'd have to refer to the original PR #2056 for a full explanation.

# Action History
- Created by: nasaWelder | 2018-02-08T04:50:03+00:00
- Closed at: 2018-02-08T05:27:37+00:00
