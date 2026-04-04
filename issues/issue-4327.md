---
title: 'Invalid last argument: xxxxxx '
source_url: https://github.com/monero-project/monero-gui/issues/4327
author: JsonAndrx
assignees: []
labels: []
created_at: '2024-06-22T21:39:51+00:00'
updated_at: '2024-06-25T19:28:45+00:00'
type: issue
status: closed
closed_at: '2024-06-22T22:09:44+00:00'
---

# Original Description
Hi, I am trying to make a transfer through wallet cli of monero with a payment id but when I do it I get the error Invalid last argument, the structure I use to make the transfer is as follows:

transfer <address> <amount> <payment_id>
transfer xxxxxxxx 0.3 xxxxxxx

the version I use is: Monero 'Fluorine Fermi' (v0.18.3.3.3-release)

# Discussion History
## selsta | 2024-06-22T21:42:47+00:00
Try sending to the integrated address directly instead of separately specifying the payment id.

## JsonAndrx | 2024-06-22T21:48:08+00:00
> Try sending to the integrated address directly instead of separately specifying the payment id.

without in the payment_id if I can make the transfer, but the problem is when I want to attach a payment_id

## selsta | 2024-06-22T21:53:20+00:00
You have to be more clear what you are doing, I don't really understand it from your post. To do it correctly you have to enter

```
integrated_address
```

to get an payment id and integrated address

and then

```
transfer 4JtkiNvoi3iSPHHvcfXPPyj66zHQ9h1X9hmLCjDZ6kbNUhtYwDhAMm79p9GZ1iPCUhDMEvKMkMJdgb7JURAkCZUuhr8aQWw7q9r2h8juTv 0.1
```

## JsonAndrx | 2024-06-22T22:04:49+00:00
> You have to be more clear what you are doing, I don't really understand it from your post. To do it correctly you have to enter
> 
> ```
> integrated_address
> ```
> 
> to get an payment id and integrated address
> 
> and then
> 
> ```
> transfer 4JtkiNvoi3iSPHHvcfXPPyj66zHQ9h1X9hmLCjDZ6kbNUhtYwDhAMm79p9GZ1iPCUhDMEvKMkMJdgb7JURAkCZUuhr8aQWw7q9r2h8juTv 0.1
> ```
ok I got it, I was just getting my bearings from old resources for the payments_id payment, sorry for the newbie issue but I couldn't find any information on how to do this process, thanks a lot.


# Action History
- Created by: JsonAndrx | 2024-06-22T21:39:51+00:00
- Closed at: 2024-06-22T22:09:44+00:00
