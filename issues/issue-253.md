---
title: Feature request
source_url: https://github.com/monero-project/monero/issues/253
author: Gingeropolous
assignees: []
labels: []
created_at: '2015-04-03T11:40:56+00:00'
updated_at: '2016-02-15T07:44:51+00:00'
type: issue
status: closed
closed_at: '2016-02-15T07:44:51+00:00'
---

# Original Description
Simplewallet checks the transfer string to see if there's a payment ID. If there's not, it displays "You are currently sending this payment without a payment ID. The recipient will not be able to identify that you have sent this payment. Would you like to add a payment ID?"

yes/no

"Would you like to add a random payment ID, or encode a message in hexadecimal? (limited to 32 characters)"

random / encode

random -> inserts random payment ID, executes transaction

Encode ->

"Please enter your message. Your message will be clipped at 32 characters or padded with 0's to reach 32 characters"

User enters message, hits return, executes transaction.


# Discussion History
## tewinget | 2015-04-03T14:56:25+00:00
This seems like a cool idea, but more geared toward a GUI setup than the
cli.

On Fri, Apr 3, 2015 at 7:40 AM, Gingeropolous notifications@github.com
wrote:

> Simplewallet checks the transfer string to see if there's a payment ID. If
> there's not, it displays "You are currently sending this payment without a
> payment ID. The recipient will not be able to identify that you have sent
> this payment. Would you like to add a payment ID?"
> 
> yes/no
> 
> "Would you like to add a random payment ID, or encode a message in
> hexadecimal? (limited to 32 characters)"
> 
> random / encode
> 
> random -> inserts random payment ID, executes transaction
> 
> Encode ->
> 
> "Please enter your message. Your message will be clipped at 32 characters
> or padded with 0's to reach 32 characters"
> 
> User enters message, hits return, executes transaction.
> 
> —
> Reply to this email directly or view it on GitHub
> https://github.com/monero-project/bitmonero/issues/253.

## 

Thomas Winget
Computer Engineering
Purdue University '12


## ghost | 2015-04-04T06:02:55+00:00
no obtrusive msg boxes like that pls, some of us actually know what they are doing, a bold red-lettered warning on the payID box in the GUI would suffice.


## Gingeropolous | 2015-04-08T01:24:31+00:00
well, until this is implemented somehow, newbies are just going to continue losing their funds. 

Maybe a seperate, modified wallet package then called NoobWallet


## sammy007 | 2015-04-08T08:21:20+00:00
Maybe it's good idea to introduce <code>--expert</code> option in simplewallet and make warning by default in normal mode, experts can create an alias in Unix-like system or .cmd file with <code>--expect</code> option to avoid warnings. In rpc server mode <code>--expert</code> should be forced indeed.


## generalizethis | 2015-09-04T05:41:45+00:00
A check box (check if you do not want to see this message again) could work also. One time annoyance  is better than one time losing all your funds


## iamsmooth | 2016-02-15T01:55:53+00:00
seems largely addressed by integrated addresses


## fluffypony | 2016-02-15T07:44:51+00:00
Agreed - closing due to integrated addresses


# Action History
- Created by: Gingeropolous | 2015-04-03T11:40:56+00:00
- Closed at: 2016-02-15T07:44:51+00:00
