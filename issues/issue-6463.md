---
title: CLI availability countdown timer does not take into account unlock_time
source_url: https://github.com/monero-project/monero/issues/6463
author: Mitchellpkt
assignees: []
labels: []
created_at: '2020-04-18T20:43:55+00:00'
updated_at: '2020-05-09T01:52:16+00:00'
type: issue
status: closed
closed_at: '2020-05-09T01:52:16+00:00'
---

# Original Description
I sent myself a [test transaction](https://xmrchain.net/tx/609cb352dd224e205797683cb303d7d42907c559c9671ccea7b7a613684a2605/1) yesterday, and the CLI wallet automatically started the 10-block availability countdown without taking into account the transaction's `unlock_time` field.

The "7 blocks to unlock" shown below is misleading, because all of the outputs in that wallet (both change and received) are locked for another 500 billion years or so. This might be confusing for users who expect that funds will always be spendable as soon as the counter hits 0 blocks.

```
[wallet 49ysqi]: balance
Currently selected account: [0] Primary account
Tag: (No tag assigned)
Balance: 0.000000030000, unlocked balance: 0.000000000000 (7 block(s) to unlock)
```

**Note: my intended scope for this issue is specifically the "N block(s) to unlock" message.** The general question of alerting on long lock times has been previously [previously discussed](https://hackerone.com/reports/417515).

# Discussion History
## sumogr | 2020-04-18T21:41:36+00:00
IMHO i guess this can be solved (mitigated would be me a more proper word) with something like the below 
```
  uint64_t blocks_to_unlock;
  uint64_t unlocked_balance = m_wallet->unlocked_balance(m_current_subaddress_account, false, &blocks_to_unlock);
  std::string unlock_time_message;
  if (blocks_to_unlock > 0 && blocks_to_unlock <= CRYPTONOTE_DEFAULT_TX_SPENDABLE_AGE) {
  unlock_time_message = (boost::format(" (%lu block(s) to unlock)") % blocks_to_unlock).str();
  success_msg_writer() << tr("Balance: ") << print_money(m_wallet->balance(m_current_subaddress_account, false)) << ", "
    << tr("unlocked balance: ") << print_money(unlocked_balance) << unlock_time_message;
  }
  else {
  success_msg_writer() << tr("Balance: ") << print_money(m_wallet->balance(m_current_subaddress_account, false)) << ", "
  << tr("unlocked balance: ") << print_money(unlocked_balance)\n 
  << tr("You have received funds (outputs) that will unlock beyond the default tx spendable age");
  }
```
The problem persists though if in the meantime another output "arrives" that is not locked beyond the default tx spendable age. 
I cant think of a way of keeping this message while completely solving this as well, but that's just me :)
(edit: a printout of all locked transfers along with blocks_to_unlock, for each account, maybe upon `balance detail` , would ease this out)


## moneromooo-monero | 2020-04-19T12:50:16+00:00
Works for me. Make sure you actually put a correct unlock_time.

## sumogr | 2020-04-19T12:56:51+00:00
> Works for me. Make sure you actually put a correct unlock_time.

@moneromooo-monero i have a feeling he means the countdown starts always from 10 no matter the locked blocks number picked on `transfer_locked` (which i think is the case). can you check that?

## moneromooo-monero | 2020-04-19T13:04:48+00:00
I have. Did you ?

## moneromooo-monero | 2020-04-19T13:27:26+00:00
I see what the problem is. If you select a UNIX time rather than a block number, it cannot know how many blocks till unlocking, so it doesn't mention it in that case.

## moneromooo-monero | 2020-04-19T16:05:35+00:00
#6467

## moneromooo-monero | 2020-05-09T01:52:16+00:00
Fixed

# Action History
- Created by: Mitchellpkt | 2020-04-18T20:43:55+00:00
- Closed at: 2020-05-09T01:52:16+00:00
