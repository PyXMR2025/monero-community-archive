---
title: 'how to run monero-wallet-rpc background in Ubuntu server? '
source_url: https://github.com/monero-project/monero/issues/4149
author: navneetboghani
assignees: []
labels: []
created_at: '2018-07-19T06:30:56+00:00'
updated_at: '2018-07-19T17:49:00+00:00'
type: issue
status: closed
closed_at: '2018-07-19T17:49:00+00:00'
---

# Original Description
I want to run monero-wallet-rpc in background. i am using now below command

./monero-wallet-rpc --wallet-file monero22 --password Monero11 --rpc-bind-port 18083 --rpc-bind-ip 0.0.0.0 --daemon-host 0.0.0.0 --disable-rpc-login --confirm-external-bind

# Discussion History
## shopglobal | 2018-07-19T06:34:43+00:00
That command is not safe

On Thu, Jul 19, 2018, 2:31 AM Navneet Boghani <notifications@github.com>
wrote:

> I want to run monero-wallet-rpc in background. i am using now below command
>
> ./monero-wallet-rpc --wallet-file monero22 --password Monero11
> --rpc-bind-port 18083 --rpc-bind-ip 0.0.0.0 --daemon-host 0.0.0.0
> --disable-rpc-login --confirm-external-bind
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/4149>, or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AMMA52TVUt46xOlGxuwtgVJyAJCYAkWbks5uICeogaJpZM4VV0ph>
> .
>


## shopglobal | 2018-07-19T06:39:33+00:00
The monero-wallet-rpc should safely be run locally. Running the monero
wallet or RPC API open node commands with a 'hot wallet' could very well
leave you open to attack.

Try this instead
./monero-wallet-rpc --wallet-file monero22 --password Monero11
--rpc-bind-port 18083 --rpc-bind-ip 127.0.0.1 --disable-rpc-login



Look into making use of PM2 or something like forever for Ubuntu to run
monerod and utilities in the background.


On Thu, Jul 19, 2018, 2:34 AM Mark Evans Jr. <president@worldvaporexpo.com>
wrote:

> That command is not safe
>
> On Thu, Jul 19, 2018, 2:31 AM Navneet Boghani <notifications@github.com>
> wrote:
>
>> I want to run monero-wallet-rpc in background. i am using now below
>> command
>>
>> ./monero-wallet-rpc --wallet-file monero22 --password Monero11
>> --rpc-bind-port 18083 --rpc-bind-ip 0.0.0.0 --daemon-host 0.0.0.0
>> --disable-rpc-login --confirm-external-bind
>>
>> —
>> You are receiving this because you are subscribed to this thread.
>> Reply to this email directly, view it on GitHub
>> <https://github.com/monero-project/monero/issues/4149>, or mute the
>> thread
>> <https://github.com/notifications/unsubscribe-auth/AMMA52TVUt46xOlGxuwtgVJyAJCYAkWbks5uICeogaJpZM4VV0ph>
>> .
>>
>


## navneetboghani | 2018-07-19T06:44:00+00:00
yes monerod is ruing in background in Ubuntu. so tell me how to access monero wallet rpc call to another server. for that i want to command to run wallet in background? 

## shopglobal | 2018-07-19T06:53:48+00:00
To run the local rpc or cli wallet from a daemon on another server you may
utilize the --daemon-host or --daemon-address flag and add
connection to a remote node.

Suppose then node is moneroworld.com:18090

You can run the wallet with --daemon-address http://moneroworld.com:18090

You can run alternatively run a full node monerod and then connect wallet
or RPC to it in the way you're describing.

Hope this helps.

On Thu, Jul 19, 2018, 2:44 AM Navneet Boghani <notifications@github.com>
wrote:

> yes monerod is ruing in background in Ubuntu. so tell me how to access
> monero wallet rpc call to another server. for that i want to command to run
> wallet in background?
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/4149#issuecomment-406171745>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AMMA5wXK8VoT9WqEAp7TpXC8V4Mp6b1dks5uICq2gaJpZM4VV0ph>
> .
>


## navneetboghani | 2018-07-19T07:00:25+00:00
you are right. but i am saying that if server is close then wallet rpc is not ruining in background. so i want to solution for run wallet rpc in background.

## jtgrassie | 2018-07-19T14:46:32+00:00
Please keep GitHub issues to bug tracking not general usage questions. This question is already answered on the Monero StackExchange site. https://monero.stackexchange.com/a/3481/7493

## dEBRUYNE-1 | 2018-07-19T17:43:25+00:00
+resolved

# Action History
- Created by: navneetboghani | 2018-07-19T06:30:56+00:00
- Closed at: 2018-07-19T17:49:00+00:00
