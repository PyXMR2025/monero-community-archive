---
title: 'Seraphis wallet workgroup meeting #22 - Monday, 2023-05-15, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/836
author: rbrunner7
assignees: []
labels: []
created_at: '2023-05-13T14:26:17+00:00'
updated_at: '2023-05-15T18:26:38+00:00'
type: issue
status: closed
closed_at: '2023-05-15T18:26:38+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: #826 

With the last meeting nearly 1 month ago let's see where we stand in the meantime.

# Discussion History
## rbrunner7 | 2023-05-15T18:22:25+00:00
````
<rbrunner7[m]> Meeting time. Hello! https://github.com/monero-project/meta/issues/836
<UkoeHB> hi
<rbrunner7[m]> I hope this room works now, I have a message from Matrix from earlier today that "19 people left the room" ...
<dangerousfreedom> Hello
<jberman[m]> hello
<rbrunner7[m]> Alright, nice to be here again. So, what are the reports what happened during the last month?
<rbrunner7[m]> In any case, I didn't have much to read up in this particular room :)
<jberman[m]> I completed a mock implementation of the async scanner that points to a live daemon.  When scanning via a remote daemon, I observed a speedup of 20-30% on my machine. When scanning via a local daemon, I observed a speedup of ~5-10% on my machine
<jberman[m]> I'm in discussion with selsta to test it in conditions closer to production. It's possible (imo probable) the speedup will be more significant for most people scanning via remote daemons, since I'm throttled by a proxy service I'm using in my setup
<jberman[m]> The code is in this branch: https://github.com/j-berman/monero/tree/seraphis_lib_scanner
<jberman[m]> I wrote a monero-blockchain-scanner utility program so anyone can test the scanner and compare it with wallet2 like this: ./monero-blockchain-scanner --daemon-address localhost:18081 --start-height 2840000 --wallet-file ./test_wallet
<UkoeHB> do you want me to review it?
<dangerousfreedom> Last weeks I have been working on the moneroinflation (for monerokon). I will restart working on the wallet this week. I havent been following the developments here for the past month basically. I will catch up from now on.
<jberman[m]> UkoeHB: I'd say not yet. there's a decent amount of cleanup changes I still want to make to it
<UkoeHB> ok
<UkoeHB> I don't have anything to report. Over the next couple weeks I will be working on multisig stuff for monerokon (which I decided to attend in person this year).
<rbrunner7[m]> Nice, jberman . What would you quickly estimate, how many work weeks of implementing did it take to reach that point?
<dangerousfreedom> UkoeHB: Have you been working on any aspect of the wallet lately? Our discussion about the transaction history still relevant or you had some new ideas?
<UkoeHB> dangerousfreedom: I have not
<UkoeHB> and no new ideas
<jberman[m]> rbrunner7: I'd say around 6 weeks, more if we count the original scanner I implemented using the seraphis lib that used wallet2's async structure. There was a lot of back and forth + testing various components + bug fixing on my end to get to this point
<rbrunner7[m]> Ok, that does not sound too bad for such pioneering work
<rbrunner7[m]> And with such a result
<rbrunner7[m]> It seems that shalit and ghostway also didn't have much opportunities to work on the wallet in the last weeks, I assume
<rbrunner7[m]> Maybe everybody will go back to work almost at the same time
<ghostway[m]> I'll be able to work in about a week probably 
<rbrunner7[m]> Sounds good!
<rbrunner7[m]> Anybody having something to discuss or report further in this meeting?
<UkoeHB> not me
<rbrunner7[m]> Alright then, thanks for attending, and read you again in 1 week at the latest
<dangerousfreedom> Thanks.
<UkoeHB> Thanks rbrunner7[m]
<jberman[m]> Thank you :) figured this is worth sharing too: I'm planning to wrap up my current CCS and open another to make this scanner production ready and continue wallet work from there
````


# Action History
- Created by: rbrunner7 | 2023-05-13T14:26:17+00:00
- Closed at: 2023-05-15T18:26:38+00:00
