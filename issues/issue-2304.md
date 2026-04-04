---
title: Inconsistencies around the status bars
source_url: https://github.com/monero-project/monero-gui/issues/2304
author: ghost
assignees: []
labels: []
created_at: '2019-07-21T00:08:05+00:00'
updated_at: '2020-04-04T13:44:51+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
[Updated!]

1. In advanced mode, when starting a local node for the first time, it looks like this for half a minute:
![image](https://user-images.githubusercontent.com/46682965/61584947-32883a00-ab51-11e9-8a25-cd19cc715d10.png)
   - The orange bar shouldn't be filled, since it hasn't even started yet.
   - It shouldn't say 0 blocks remaining, while actually all blocks are remaining.
   - It shouldn't say "Synchronizing" while it's obviously not synchronizing, since it hasn't even found out that there are more than 0 blocks. Proposal: "Connecting..."

   For veterans these points may be laughable, but for a new user it's a "WTF!?"-situation. Next thing the new user does is clicking randomly on things that might "fix" it, like "start daemon" / "switch node" / "connect to remote node" and likes. Hint: Things just get worse by doing so.

2. In bootstrap mode, while the blockchain is downloading, it looks like this:
![image](https://user-images.githubusercontent.com/46682965/61584848-72e6b880-ab4f-11e9-95fa-aff9769519a5.png)
   - Do we really want to call the scan for transactions a "synchronization"? That is not a synchronization!
   - It says "Daemon is synchronized", but that's wrong because actually the daemon is running in the background doing heavy synchronization work and loading gigabytes of data without telling the user anything about it.
   - It says "Network status: Connected". How is a user supposed to know that right now the wallet is connected to a (unsafe) remote node? If the user would be using the simple mode (without bootstrap), it would tell him "Network status: Remote node". But here it doesn't. And the mode selection window didn't even explain him what the bootstrap mode does (since we didn't yet adopt #2208 or better #2320).

3. Synchronizing the local node looks like this:
![image](https://user-images.githubusercontent.com/46682965/61585053-5cdaf700-ab53-11e9-9232-aed707c10a8a.png)
   - The 2 bars should be exchanged: What is done first should be in first row, what is done second should be in second row.
   - It shouldn't say "Waiting for daemon to sync" while waiting for daemon to sync. Reason:
   ![image](https://user-images.githubusercontent.com/46682965/61589330-b6214580-aba8-11e9-922f-ec46b09f5ffd.png)

  
4. Simple mode looks like this directly after the status "Searching remote node" disappears:
  ![image](https://user-images.githubusercontent.com/46682965/63254509-2a1c3f80-c274-11e9-995d-46e257e4e319.png)
When finished, it loos like this:
![image](https://user-images.githubusercontent.com/46682965/61585128-f8209c00-ab54-11e9-9ac0-2110b3151897.png)
   - It shouldn't say "Synchronizing daemon" / "Daemon is synchronized" because the daemon is not used in remote node operation.
   - As already mentioned, we shouldn't call the scan for transactions a "synchronization".

 

5. The term "daemon" should not be used at all. That's just the technical way things are solved - but the user is not interested in that, so we should hide such technical details from the user. A daemon might be the most normal thing for you, but for 99% of users it's not. **Imagine, Windows would bother the user with a daemon whenever updates are done in the background. Seems ridiculous, right?**

![image](https://user-images.githubusercontent.com/46682965/61996051-51765700-b090-11e9-9d88-1489f1f9bf6c.png)
Example **local node**:
![image](https://user-images.githubusercontent.com/46682965/63258031-6e5f0e00-c27b-11e9-97b2-4c037583cd91.png)

Example **remote node**:
![image](https://user-images.githubusercontent.com/46682965/63258049-761eb280-c27b-11e9-894c-82ba900a2168.png)

Example **bootstrap phase** (scanning for funds finished):
![image](https://user-images.githubusercontent.com/46682965/64270217-7c7b8280-cf3b-11e9-9980-390b00ed8d82.png)
Please note that this proposal doesn't use any technical terms like "local node", "remote node", "daemon" or "bootstrap"! They are absolutely not necessary. They just confuse our beloved noobs.

- All possible network statuses:

| Local node | Remote node | Bootstrap phase |
| ------------ | --------------- | ------------------ |
| Offline | Offline | Offline |
| Connecting… | Connecting via third party… | Connecting via third party… |
| Connected | Connected via third party | Connected via third party (temporarily) |

- All possible blockchain statuses:

| Connected | Not connected |
| ------------ | --------------- |
| Blockchain 3 weeks behind  \|  ~20 min | Blockchain 3 weeks behind (estimated) |
| Blockchain up to date (1779001) | Blockchain less than 1 day behind |

This proposal is in accordance with #2321:
![image](https://user-images.githubusercontent.com/46682965/64263338-c8282f00-cf2f-11e9-83be-46e179ccf091.png)
As you can see: You really don't need to introduce terms like "local node", "remote node" and likes.



# Discussion History
# Action History
- Created by: ghost | 2019-07-21T00:08:05+00:00
