---
title: Support multiple destinations in make_uri and parse_uri
source_url: https://github.com/monero-project/monero/issues/7731
author: woodser
assignees: []
labels: []
created_at: '2021-05-20T16:36:41+00:00'
updated_at: '2026-02-19T14:12:09+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
monero-wallet-rpc supports [make_uri](https://www.getmonero.org/resources/developer-guides/wallet-rpc.html#make_uri) and [parse_uri](https://www.getmonero.org/resources/developer-guides/wallet-rpc.html#parse_uri) which can be used to create a request for payment which the sender can parse to pay.

These calls currently only support a single destination address and amount.

This issue requests supporting multiple destination addresses and amounts to accommodate multi-output requests which can be used in a variety of applications or to prepare wallets with available outputs.

An encoding scheme is needed to support multiple addresses and amounts.  The format should be small in order to accommodate limited capacity of QR codes.

# Discussion History
## erciccione | 2021-05-25T13:14:49+00:00
There is a **$500 bounty** on this issue. See https://github.com/haveno-dex/haveno/issues/83 for details.

## benevanoff | 2021-05-25T15:20:05+00:00
I’ll take a stab :p

## woodser | 2021-05-25T18:15:13+00:00
Example encoding scheme supported on IRC (originally proposed by @benevanoff):

`monero:46BeWrHpwXmHDpDEUmZBWZfoQpdc6HaERCNmx1pEYL2rAcuwufPN9rXHHtyUA4QVy66qeFQkn6sfK8aHYjA3jk3o1Bv16em,46BeWrHpwXmHDpDEUmZBWZfoQpdc6HaERCNmx1pEYL2rAcuwufPN9rXHHtyUA4QVy66qeFQkn6sfK8aHYjA3jk3o1Bv16em?amount=239.39014,123.55423&description=donation,example` (note description text needs escaped).

For backward compatibility, `make_uri` should produce the old format if using a single destination and address and this new format for multiple destinations and addresses.

## trasherdk | 2021-05-26T00:10:27+00:00
Positional parameters, description field optional.

`monero:<addr1>,piconero,base64(desc):<addr2>,piconero,base64(desc)` 


## benevanoff | 2021-05-26T00:36:58+00:00
I like @trasherdk 's suggestion better

## selsta | 2021-05-26T00:38:17+00:00
@trasherdk's solution will use more characters overall because you will have e.g. "?amount=" multiple times.

## trasherdk | 2021-05-26T01:59:16+00:00
I would not use `?`, `amount`, `description` and `=`.

Using `:` as delimiter for separate transactions. `monero:<transaction1>:<transaction2>`
where a transaction is `<addr1>,piconero,base64(desc)` making `description` optional.

## selsta | 2021-05-26T02:05:09+00:00
@trasherdk Ok I understand now. Your proposed format is nicer than what we currently have, though it wouldn't be backwards compatible as far as I can see.

```
19:24 <moneromooo> In any case, it'd be nice if it was backward compatible.
19:24 <moneromooo> ie, passing one address/amount with the new rules yields an URI that old rules parse correctly.
```

I guess it can be discussed if having backwards compatibility is more important than a cleaner format.

## benevanoff | 2021-05-26T02:42:10+00:00
I’m personally in favor of just biting the bullet and changing it. The payment ID field should already be deprecated iirc so I’d think that can go and having a recipient tag as well as a transaction description tag seems rather redundant since they’re both just free forms.

## benevanoff | 2021-05-26T03:00:12+00:00
Actually now that I think about it more, it’d probably be a headache for 3rd part wallets so maybe not the best idea

## trasherdk | 2021-05-26T03:54:51+00:00
I would think it would be easier (less code) to parse my version :question: 

## woodser | 2021-05-26T06:03:27+00:00
Long payment IDs should still be supported afaik.

The old call should be backward compatible for a single address/amount, but it could produce the new format for multiple addresses/amounts, or we could create new RPC calls like 'create_payment_request' and 'parse_payment_request'.

## selsta | 2021-05-26T06:04:44+00:00
> Long payment IDs should still be supported afaik.

Integrated addresses are fine. No need for external payment id field.

## hyc | 2021-05-26T11:53:01+00:00
> Using `:` as delimiter for separate transactions. `monero:<transaction1>:<transaction2>`
> where a transaction is `<addr1>,piconero,base64(desc)` making `description` optional.

URI syntax only allows for '?' and ';' as delimiters within a single URI. Please let's not invent
solutions that would break all existing URI-processing software.

## elibroftw | 2022-01-26T00:36:16+00:00
The tricky part is that the bade of the Uri is an address. This makes processing additional addresses that much more annoying. The problem with the solution I'm about to propose is that wallets will have to append a query to the base address list. Which is 2 lines of code.


monero:addr1? 
addr=addr2&amt=val1&addr=addr3&amt=val2

Any competent Uri parser should be able to retrieves values as a list from a Uri. 

## selsta | 2022-01-26T00:42:46+00:00
@elibroftw there is a PR for it already https://github.com/monero-project/monero/pull/7737

## elibroftw | 2022-01-26T00:43:33+00:00
> @elibroftw there is a PR for it already https://github.com/monero-project/monero/pull/7737

Yeah I realized. Too late for me 😅

## erciccione | 2022-04-13T14:42:25+00:00
#7737 has been abandoned. Anyone willing to recover it can claim part of the bounty: https://github.com/haveno-dex/haveno/issues/83

## woodser | 2022-12-02T10:20:30+00:00
@darkdrag00n It's no longer needed in Haveno, but multiple destinations in Monero payment URIs is still a valid use case that would be good to support long term. We would still honor the bounty.*

*Reduced the bounty to $350.

## NorrinRadd | 2024-04-06T13:44:08+00:00
I will take this @woodser 

## jeffro256 | 2025-08-31T06:40:18+00:00
I support a format similar to [the one used in Bitcoin Cash](https://github.com/BitcoinUnlimited/BUIP/blob/master/086.md) for multiple outputs. it is very much in line with @elibroftw's and @trasherdk's proposals. Although, I will say that I hate the "indexing notation" in Bitcoin Cash; that could be dropped. Our grammer (in ABNF syntax) would be something along the lines of:

```
monero-uri = "monero:" monero-address [ "?" first-param { "&" monero-param } ]
monero-address = main-address / sub-address / integrated-address
first-param = version-param / monero-param
monero-param = address-param / legacy-amount-param / amount-param / label-param / tx-desc-param
address-param = "address=" monero-address
legacy-amount-param = "tx_amount=" amount
amount-param = "amount=" amount
label-param = "label=" label-string
tx-desc-param = "tx_description=" label-string
version-param = "version=" version
amount = decimal-number [amount-unit]
amount-unit = xmr-unit / crypto-unit / fiat-unit
decimal-number = *DIGIT ["." *DIGIT]
version = "2.0"
label-string = *(unreserved / pct-encoded / ":" / "@")
xmr-unit = "XMR"
crypto-unit = "BTC" / "ETH"
fiat-unit = "USD" / "EUR"
```

Where `unreserved` and `pct-encoded` are defined in [RFC 3986](https://www.rfc-editor.org/rfc/rfc3986). And `main-address`, `sub-address`, and `integrated-address` are exactly what they sound like. This URI scheme is backwards compatible with the current Monero URI scheme for a single recipient if using the `tx_amount=` parameter (using `amount=` is also an option, but not backwards compatible).

The attributes (address, amount, label) specified in the URI are grouped into outputs delineated at the start of an `address-param`. Note that the version param always comes first if present. Consider the following URI (newlines added for clarity):

```
monero:888tNkZrPN6JsEgekjMnABU4TBzc2Dt29EPAvkRxbANsAnjyPbb3iQ1YBRk1UXcdRsiKc9dhwMVgN5S9cQUiyoogDavup3H
?version=2.0
&amount=1XMR
&label=General%20Fund%20Donation
&address=8AR4NqB9AacVWQkLNw3sA1jjNC1gQxVPtJHz7He3B1jrafUDH4u2p9VG34PhQo3sCQBGbrg6UFSNGgdbpr8qijt87aD4afg
&label=MAGIC%20Monero%20Fund%20Donation
&tx_description=Big%20Donator
```

This would create 2 outputs: one to the General fund for 1 XMR, and one to the MAGIC Monero Fund for a to-be-user-supplied amount. The whole transaction would be labeled "Big Donator".

I'm okay with deprecating long payment IDs and not supporting them in the new URI spec.

## EgeBalci | 2026-02-19T13:59:32+00:00
Is anyone actively working on this?

This would be an extremely useful addition, and I believe it is highly anticipated by many. Based on the long discussions in the existing [PR](https://github.com/monero-project/monero/pull/9830), I assume this needs to be re-implemented from scratch.

If there’s consensus on the URI scheme specification (field naming, ordering, encoding rules, edge-case handling, etc.), I would be willing to help implement this.

(PS: I strongly agree that the encoding scheme needs to be compact, especially given QR code size constraints.)

## pptrace | 2026-02-19T14:12:09+00:00
Simply accepting multiple URIs with a delimiter on the GUI Wallet may also solve this issue. 

Such as one URI per line
```
monero:888tNkZrPN6JsEgekjMnABU4TBzc2Dt29EPAvkRxbANsAnjyPbb3iQ1YBRk1UXcdRsiKc9dhwMVgN5S9cQUiyoogDavup3H?amount=1.25
monero:84EgZVjXKF4d1JkEhZSxm4LQQEx64AvqQEwkvWPtHEb5JMrB1Y86y1vCPSCiXsKzbfS9x8vCpx3gVgPaHCpobPYqQzANTnC?amount=0.001
```
or simply comma seperated URIs

```
monero:888tNkZrPN6JsEgekjMnABU4TBzc2Dt29EPAvkRxbANsAnjyPbb3iQ1YBRk1UXcdRsiKc9dhwMVgN5S9cQUiyoogDavup3H?amount=1.25,monero:84EgZVjXKF4d1JkEhZSxm4LQQEx64AvqQEwkvWPtHEb5JMrB1Y86y1vCPSCiXsKzbfS9x8vCpx3gVgPaHCpobPYqQzANTnC?amount=0.001
```

This is probably the best option in terms of backward compatibility and the easiest to implement. No changes needed on the `parse_uri` or `make_uri`. 

# Action History
- Created by: woodser | 2021-05-20T16:36:41+00:00
