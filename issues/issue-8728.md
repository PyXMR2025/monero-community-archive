---
title: Monero wallet RPC sends all balance from subadress when transfer function called
source_url: https://github.com/monero-project/monero/issues/8728
author: rayorole
assignees: []
labels: []
created_at: '2023-02-02T18:45:03+00:00'
updated_at: '2023-03-10T16:59:10+00:00'
type: issue
status: closed
closed_at: '2023-03-10T16:59:10+00:00'
---

# Original Description
```php

function send_xmr($from, $to, $xmr)
{

  $piconero = bcmul($xmr, '1000000000000');
  $ch = curl_init();

  curl_setopt($ch, CURLOPT_URL, "http://localhost:28085/json_rpc");
  curl_setopt($ch, CURLOPT_USERPWD, 'xxxx:xxxxxx');
  curl_setopt($ch, CURLOPT_HTTPAUTH, CURLAUTH_DIGEST);
  curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));
  curl_setopt($ch, CURLOPT_POSTFIELDS, '{"jsonrpc": "2.0","id": "0","method": "transfer","params": {"destinations": [{"amount": ' . $piconero . ',"address": "' . $to . '"}],
  "unlock_time": 0,"account_index": 0,"subaddr_indices": [' . $from . '],"priority": 3,"ring_size": 16}}');
  curl_setopt($ch, CURLOPT_POST, 1);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
  curl_setopt($ch, CURLOPT_HEADER, 0);
  $output = curl_exec($ch);

  if ($output === FALSE) {
    echo 'cURL Error';
  }

  curl_close($ch);
  $txObj = json_decode($output);

  if (isset($txObj->error->code)) {
    $code = $txObj->error->code;
    if ($code == -17) {
      return 'insufficient-balance';
    } elseif ($code == -2) {
      return 'invalid-address';
    } else {
      return $txObj->error->message;
    }
  } else {
    die(var_dump($txObj));
    return 'Ok';
  }
}


// This is how I call the function
send_xmr(2, "8BW.......3EjuE", 0.5);
```

### Description

You can see that I want to transfer 0.5 XMR from subaddress 2 to address: 8BW.......3EjuE
When I call the function, the transaction was submitted successfully. But all remaining balance of the subaddress is also gone.

The receiving address gets the 0.5 XMR but the other funds belonging to subaddress are gone.
Maybe they get sent to primary address of the wallet, but why would that be?

I don't see how this is a problem with my code, I tried using the monerophp library but this gives me the same bug.

I have an active monerod and wallet rpc (successfully synced with blockchain)


### So basically, to summarize my problem:

**Alice** has a subaddress with a balance of 5 XMR
**Bob** has a subaddress with a balance of 0 XMR

**Alice** wants to send 1 XMR to **Bob**
When **Alice** calls the transfer function with her address index as sender and an amount of 0.5 XMR (converted to piconero),
Bob gets the 1 XMR, but **Alice** loses all her funds, this is an error because **Alice** actually must have a remaining balance of 4 XMR.

I already asked this question on Monero Stack Exchange but I don't seem to be getting a valid solution
[link to question](https://monero.stackexchange.com/questions/13857/monero-wallet-rpc-deducts-10-xmr-from-address-when-i-call-the-transfer-function)

What am I doing wrong?

# Discussion History
## selsta | 2023-02-02T18:53:46+00:00
Did you read https://monero.stackexchange.com/questions/11426/when-constructing-a-change-output-does-it-have-to-be-sent-to-the-main-public-ad ?

## selsta | 2023-03-10T16:59:10+00:00
No reply from issue creator, closing. Can be reopened if there are questions remaining.

# Action History
- Created by: rayorole | 2023-02-02T18:45:03+00:00
- Closed at: 2023-03-10T16:59:10+00:00
