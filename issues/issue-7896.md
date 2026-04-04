---
title: RFC 9101 implementation
source_url: https://github.com/monero-project/monero/issues/7896
author: AAH20
assignees: []
labels: []
created_at: '2021-08-26T17:49:22+00:00'
updated_at: '2022-02-19T00:11:31+00:00'
type: issue
status: closed
closed_at: '2022-02-19T00:11:31+00:00'
---

# Original Description
Check the latest RFC 9101 which contains information about JSON Web Algorithms, Encryption,signatures and tokens ,that would ease the implementation and integration of the most secure 3rd party wallets , unlike the vulnerable cakewallet app with its new domain name resolver , 
protect monero's title as the most secure privacy coin before its too late.

# Discussion History
## AAH20 | 2021-08-26T17:53:51+00:00
https://www.rfc-editor.org/rfc/rfc9101

## selsta | 2021-08-26T17:55:21+00:00
Maybe better to report this to cake wallet? Monero itself has no integration with unstoppable domains (I assume you refer to that).

## cirocosta | 2021-08-26T20:46:17+00:00
I _think_ they're referring to the use of Digest-based auth when using `--rpc-login` (which is true, `cake` uses if specified: https://github.com/cake-tech/cake_wallet/blob/a14ea3c3aaf31140985dc7b17133dc3f5f6d7b82/lib/entities/node.dart#L101-L106).

Would you mind elaborating, @AAH20? What is the suggestion here?

## selsta | 2021-08-26T20:50:41+00:00
> with its new domain name resolver

I assume they are referring to https://github.com/cake-tech/cake_wallet/commit/c7777daa95792b68e734635ae961127004b5e7e1

## AAH20 | 2021-08-27T20:27:48+00:00
Its about the idea of a mobile app connecting to a remote node ,that generates an extra attack surface , even if you are connecting with a remote rpc from your secure computer you are vulnerable to man in the middle attacks , must be a way to trust remote nodes internationally, by certificate authority using asymmetric encryption in their signatures.

## AAH20 | 2021-08-27T20:32:28+00:00
@cirocosta thats need an extensive demonstration of the hashmap in dart risk assessment , but briefly hashmaps in general are known for collisions so to prevent that you have to sign in a trustable certificate authority which generates the asymmetric encryption algorithms keys , so your objective is to apply encryption algorithms on the api endpoints before or after the hash algorithms of the message digest functions 

## AAH20 | 2021-08-27T20:41:19+00:00
> Maybe better to report this to cake wallet? Monero itself has no integration with unstoppable domains (I assume you refer to that).

Thats a case that should be supported by the whole monero project , cause if you are betting on monero's security , privacy and anonymity, then you have to raise the public situational awareness in all aspects of their operational security , KYC , legal identity and law enforcement cases transperency , etc. , hence monero supporting wallets , exchange platforms and latest regulations should be upgraded as soon as possible.

## selsta | 2022-02-19T00:11:31+00:00
It isn't clear what you are suggesting. monerod RPC supports SSL, see

```
  --rpc-ssl arg (=autodetect)           Enable SSL on RPC connections: 
  --rpc-ssl-private-key arg             Path to a PEM format private key
  --rpc-ssl-certificate arg             Path to a PEM format certificate
  --rpc-ssl-ca-certificates arg         Path to file containing concatenated 
  --rpc-ssl-allowed-fingerprints arg    List of certificate fingerprints to 
  --rpc-ssl-allow-chained               Allow user (via --rpc-ssl-certificates)
  --rpc-ssl-allow-any-cert              Allow any peer certificate
```

# Action History
- Created by: AAH20 | 2021-08-26T17:49:22+00:00
- Closed at: 2022-02-19T00:11:31+00:00
