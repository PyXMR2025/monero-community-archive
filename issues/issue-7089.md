---
title: Update Wallet SSL Policies
source_url: https://github.com/monero-project/monero/issues/7089
author: vtnerd
assignees: []
labels: []
created_at: '2020-12-07T05:21:45+00:00'
updated_at: '2023-10-18T00:05:05+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The current default SSL security policy of the `monero-wallet-cli` and `monero-wallet-rpc` is to autodetect whether the daemon RPC has SSL enabled. A root-CA check against the domain is attempted, but only a warning is logged if it fails. The root-CA validation is not mandatory with autodect because an attacker can mitm the connection to downgrade to cleartext. A connection must be SSL mandatory for peer authentication; DANE/TLSA was created to solve the opportunistic encryption failures of SMTP.

@Gingeropolous @binaryFate @Snipa22 

**Proposal 1:** If a wallet user enters a domain (i.e. not an IP) without additional security options, upgrade autodetect to mandatory SSL with root-CA check. Its better than the current (no check), but will generate errors to users unless popular domains get a signed SSL certificate.

**Propsal 2:** [Add DANE/TLSA support](https://github.com/monero-project/monero/commit/af252c0849121264d048e8e39811c6b8e49e9f81) to the wallet autodetect mode. Its basically completed, for better or worse. Domains can "opt-in" by putting SHA256 or SHA512 fingerprints of their self-signed certificates in DNSSEC records. Domains that do not have this DNSSEC record have no change. The fingerprint could also be cached locally in the wallet data for an improved trust-on-first-use mode. The domain can set an expiry longer than 3 months for $0. The security is based on the TLD, registrar, and ICANN. So not nation-state proof, but average miscreant proof. Hopefully more difficult than root-CA shenanigans, but subjective.

**Proposal 3**: Same as (2) but make TLSA DNSSEC record opt-out. User must specify fingerprint or request skipped verification if domain has no valid TLSA record.

**Proposal 4:** I close another issue no one cares about.

# Discussion History
## vtnerd | 2020-12-07T05:24:02+00:00
One important thing - the eventual destination port is leaked over DNS when using DANE/TLSA. In many scenarios, this doesn't matter because the domain is monero only RPC. But it may matter in some other contexts. I think this is small for when users aren't providing any security information, but perhaps not.

## moneromooo-monero | 2020-12-07T22:17:07+00:00
I don't like the CA check stuff, because it basically means any fuckwit with a cert signed by something along the root can pwn you. This includes any govt, any company that preinstalls your OS, etc. Does proposal 1 include this (ie, root CA includes anything derived from anything signed by the root CA) ?

## vtnerd | 2020-12-08T04:36:33+00:00
>  Does proposal 1 include this (ie, root CA includes anything derived from anything signed by the root CA) ?

Yes. Currently a hostname with no security options is performing no validation. So this would be to defend against average bad guys. 

The DNSSEC approach relies on a root-anchor embedded in our codebase - certificates installed by other applications or hardware vendor have no effect. Governments and sophisticated bad guys can probably manipulate records in some situations. The domain owner can do self-signed with longer expiration.

In either scenario, the certificate fingerprint (or perhaps entire cert) would be cached with wallet data for trust-on-first-use like behavior, requiring user intervention if certificate changes. Hopefully this won't be too noisy.

Last option: force users to specify a fingerprint, no verification mode, or no SSL on CLI.

## garlicgambit | 2021-02-16T19:33:46+00:00
> Proposal 4: I close another issue no one cares about.

For the record: there are people that deeply care about these kind of topics. Some just don't respond (in public) and/or it takes time for these things to get peoples attention. The Monero community is also still relatively small. Please keep doing what you are doing.  
  
The following paragraph may be off-topic:  
Are there any arguments against requiring (opportunistically) encrypted RPC connections by default? Set 'safe/sane' defaults and require action if you want to disable encrypted connections.  
  
Would prefer to see trust on first use (TOFU) type schemes like SSH. Only require user intervention or show a warning message if a fingerprint has changed. TOFU is fairly simple to implement, pretty secure if used correctly and easy to explain to users. A lot of chat applications use TOFU and provide an option to authenticate contacts/fingerprints. Monero can implement a similar UX/UI.

## Jayd603 | 2023-10-15T19:02:13+00:00
I'm still trying to figure out how SSL works at all with monero.  I configured a letsencrypt certificate on my node using    --rpc-ssl-private-key and --rpc-ssl-certificate - but is that used for all connections? What about typical P2P? trying to connect with monero-wallet-cli doesn't show anything suggesting SSL is being used.  The monero-gui-wallet has nothing.  I do get this in the monero gui wallet:

2023-10-15 18:07:43.842	    7f19d4e2ec80	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO

So it has net.ssl somewhere in the code at least.

I try to set SSL on monero-wallet-cli and get this error:
Error: failed to load wallet: Enabling --daemon-ssl requires --daemon-ssl-allow-any-cert or --daemon-ssl-ca-certificates or --daemon-ssl-allowed-fingerprints or use of a .onion/.i2p domain.  Shouldn't this just use some sane defaults and check system CA certs without any configuration?

I'd like clients connecting to my remote node to be able to use SSL and verify with letsencrypt CA and get a notice its authentic at least according to CA.  I realize monero already encrypts, but I guess this could verify the hostname at least, disguise traffic a little better maybe and possibly prevent some mitm attacks.  Maybe someone can explain the state of Monero ssl a little better to me.

@vtnerd I like your first 3 proposals.  I think if SSL is enabled by the daemon and a CA check fails, the connection should fail and a warning should be issued.  The daemon can default to no SSL to avoid confusion for people who don't care about SSL. Why wasn't that done?  Is it generating a self signed cert and using SSL when it is on autodetect even when a user doesn't configure their own cert and key?

## vtnerd | 2023-10-18T00:05:05+00:00
> I'm still trying to figure out how SSL works at all with monero. I configured a letsencrypt certificate on my node using --rpc-ssl-private-key and --rpc-ssl-certificate - but is that used for all connections?

The certificate is used for `monerod` RPC and nothing else.

> What about typical P2P? trying to connect with monero-wallet-cli doesn't show anything suggesting SSL is being used. The monero-gui-wallet has nothing.

PR #8996 adds SSL to P2P, but the behavior but it may different than what you want. There is no CA checks involved, and instead everything is based on fingerprints (or just auto-accepts the certificate in the worse case).

> I think if SSL is enabled by the daemon and a CA check fails, the connection should fail and a warning should be issued.

The majority of users are using IP addresses, so a CA check is not possible. We can add a failure mode to domains, but this changes current behavior (which doesn't require a valid CA). I think its worth doing, but this has been put on the back-burner for now (with subaddresses in LWS being the highest priority atm).

# Action History
- Created by: vtnerd | 2020-12-07T05:21:45+00:00
