---
title: Connection to remote nodes should support TLS
source_url: https://github.com/monero-project/monero/issues/3402
author: monero-hax123
assignees: []
labels: []
created_at: '2018-03-14T14:55:02+00:00'
updated_at: '2019-04-15T12:17:41+00:00'
type: issue
status: closed
closed_at: '2019-04-15T12:17:41+00:00'
---

# Original Description
Currently, JSON-RPC connections from client to remote node are not authenticated or encrypted. This could enable network attackers to insert corrupted data, which could potentially lead to tracing transaction inputs. Connecting over HTTPS rather than HTTP would improve the situation. 

See also: https://www.reddit.com/r/Monero/comments/84810s/psa_tracing_attacks_could_be_possible_when_using/

# Discussion History
## moneromooo-monero | 2018-03-15T12:12:06+00:00
This was discussed several times, and the general idea was that this would be mooted with kovri being added. It looks like it might be in a while though. There were other arguments against TLS, I think vtnerd was well acquainted with the arguments.

## hyc | 2018-03-15T15:28:56+00:00
Certificate management is always a pain. We'd need to add params to monerod to configure CAcert, serverCert, and serverKey, and params to wallet to configure CAcert (and maybe, optionally, userCert and userKey). And maybe, for ease of use, write a tool to generate a CA and server cert/key pairs.

Something something node fingerprinting mumble mumble...

## anonimal | 2018-03-15T16:05:00+00:00
...and CA != decentralized but rather a hacky attempt at trust.

@monero-hax123 TLS also doesn't protect users from malicious nodes. A malicious node will execute the tracing attack regardless of whether TLS in place. AFAICT, depending on the TLS implementation, you could also do a similar attack with an artificial short read. In fact, until the client/daemon can guarantee otherwise, the problem may always exist regardless of whether the connection is authenticated or not because killing a handshake can always be a risk (someone please correct me if otherwise).

In the end, I don't see how TLS is a solution nor is relying on a node outside of one's authority.

Pinging @vtnerd.

## monero-hax123 | 2018-03-15T16:40:57+00:00
These are good points, I don't have too many ideas to contribute.

One option is to do opportunistic encryption without authentication. This would at least raise the effort for a network attacker to pull off attacks. For sure, even authenticated TLS doesn't provide any defense against a malicious remote node, but on the other hand even if you connect to your own trusted remote node, the unencrypted traffic would currently be easy to snoop.

It's nice how in ethereum, the connection ID comes with a public key like  `enode://6f8a80d14311c39f35f516fa664deaaaa13e85b2f7493f37f6144d86991ec012937307647bd3b9a82abe2974e1407241d54947bbb39763a4cac9f77166ad92a0@10.3.58.6:30303?discport=30301`.
I could imagine something similar, like `74e1407241d54947bbb39763a4cac9f77166ad92a0@mytrustednode.net:18001` which would make it safe/easy to connect to your own trusted node.

Not sure how something like this would pan out for the node.moneroworld.com gateway though.

## anonimal | 2018-03-15T17:12:10+00:00
>node outside of one's authority

This implies *any* remote node, unless one can become quantum entangled into two different locations.

>connection ID

So, hypothetically, even with something akin to cookie-like authentication, whether stored or not, if the server generates the key (or even the client), they can still generate a usable key while having illegitimately killed the previous connection ~~mid~~ **edit: post**-handshake. When the next key is generated, the server can simply observe the identical (real) input from the previous session.

I have *not* looked at ethereum's connection ID impl so I don't know how (or if) they avoid this problem.

## vtnerd | 2018-03-17T04:00:18+00:00
@moneromooo-monero @anonimal my arguments were to encourage people to run a separate process for encryption/authentication. Primarily for the reasons cited already - to prevent added complexity to the monero processes. These "public" facing encryption/authentication processes could be run as a separate user than the monero processes too, if it was thought TLS is more dangerous/complex than parsing monero P2P data.

As for opportunistic encryption - I'm not sure it would be beneficial in this environment. If a user is connecting to a RPC server in the "clear" over the internet, there is already too much trust placed in that connection (a wallet could be provided bogus data, etc). Adding encryption to that connection is giving a false sense of security. However, It would automatically hide that the two endpoints were doing monero related activities (assuming no one tried to hijack the comms).

BIP 151 is a proposal for opportunistic encryption that uses chacha20+poly1305. It was designed for P2P links, not RPC links IIRC.

## hyc | 2018-03-17T08:21:41+00:00
In that case we should just point people to stunnel and forget about it.

## vtnerd | 2018-03-31T04:22:26+00:00
@DaveWK There are already tools for this -> stunnel, hitch, nginx. And there's also SSH or even spiped. The server cannot automagically determine a certificate (the user has to provide a certificate OR manually copy/move an auto-generated self-signed certifcate), so this feature requires manual setup by a user. There isn't a magic "go encrypt/authenticate correctly button", so it's feature creep.

Adding SSL to the client was probably a bad idea too (unnecessary feature creep, see stunnel), but at least it requires no configuration if the server certificate is signed by a default root authority.

## DaveWK | 2018-03-31T13:30:41+00:00
deleted previous comment; v true; nginx/stunnel etc -- can be added on top.. i was hoping for monerod -> rpc to be secured more but I guess I have to make sure those are in the same location.

## moneromooo-monero | 2018-03-31T15:24:57+00:00
A good way to get an encrypted connection is to help with kovri :)

## moneromooo-monero | 2018-06-20T09:03:57+00:00
Actually, I've just done it. Optional and enabled by default, and you can restrict access to a set of known certificates so you're sure you're talking to the right server/client. No trusted CA nonsense.
https://github.com/monero-project/monero/commit/3fd2b80001dc5192de5d0c06de59e571d9df89c6
People who are familiar with SSL, please report any bugs/holes in the way SSL is setup, I don't know much about it.


## hyc | 2018-06-20T14:42:37+00:00
I thought this wasn't necessary, given the availability of stunnel etc.

Trusted root CAs are probably unnecessary here, sure. But IMO it's still best practice for server installations to be based on a trusted CA cert and then a CA-signed server cert. I.e., create your own self-signed CA cert and use that for any server and/or client certs you're going to use. It's more secure in the long run since the CA cert/keypair can be squirreled away on an offline machine, apart from the actual server and client machines. And server/client certs can be revoked/replaced securely in the event of a breach.


## moneromooo-monero | 2018-06-21T08:50:15+00:00
Yes, but it ends up similar to the log discussion. Most people will not know how to use those, and we'll end up with pretty much no SSL anywhere. Moreover, I don't think you could do that for P2P since it'd rely on both sides cooperating to setup a tunnel somehow. 

## moneromooo-monero | 2019-03-21T13:59:53+00:00
It was done in the end. Default is SSL autodetection, clients and servers can switch to mandatory.

I'll close this in a few days if no more comments about it.

## moneromooo-monero | 2019-04-15T12:15:12+00:00
+resolved

# Action History
- Created by: monero-hax123 | 2018-03-14T14:55:02+00:00
- Closed at: 2019-04-15T12:17:41+00:00
