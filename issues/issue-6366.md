---
title: Cannot sync with monerod
source_url: https://github.com/monero-project/monero/issues/6366
author: EasyDing
assignees: []
labels: []
created_at: '2020-03-02T12:30:12+00:00'
updated_at: '2022-02-19T04:36:46+00:00'
type: issue
status: closed
closed_at: '2022-02-19T04:36:46+00:00'
---

# Original Description
I want to create a private node, But the connection always fails when synchronizing in mainnet. Is there any other way I can synchronize.
COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT) 


# Discussion History
## vtnerd | 2020-03-03T01:32:43+00:00
What flags were used on the command line? Do you have any logs?

## Fenix2013 | 2020-03-08T11:30:18+00:00
Hi,
have you checked your files to see if monerod is stored there correctly?The problem can be caused by your antivirus program, which has rated the monerod as potentially dangerous and harmful application, and placed it in a virus chest where it was blocked.
If this is the cause of your problem,then the solution to this problem is simple, you need to locate in your antivirus program where the monerod file is stored (it will be quarantined or put in the virus chest, it depending on the type of antivirus program you are using), then unblock it and add it to the exclusion list, and return it back to the application Monero GUI or CLI Walet (it is likely that there will be other Monero GUI or CLI Wallet files that your antivirus program has identified as potential threats, they need to be handled in the same way as a monerod). Finally, after you do that,you only have to open your wallet and run the daemon again.This time it should connect seamlessly to the monerod and should start the blockchain download process (if it fails to connect, it needs to be restarted, because sometimes the connection fails, but this time you start it).
That's all, and I hope my advice has helped you and you'll be able to enjoy your wallet running at a local node.

# Action History
- Created by: EasyDing | 2020-03-02T12:30:12+00:00
- Closed at: 2022-02-19T04:36:46+00:00
