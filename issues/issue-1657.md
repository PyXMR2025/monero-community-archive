---
title: 'Feature Request: Add basic authentication'
source_url: https://github.com/monero-project/monero/issues/1657
author: hamiltino
assignees: []
labels:
- proposal
created_at: '2017-01-31T11:24:50+00:00'
updated_at: '2021-11-24T09:56:49+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Multiple people are having issues with using digest as the authentication method for monero-rpc-wallet,
For example myself: https://monero.stackexchange.com/questions/3523/help-me-with-digest-authentication-using-java
And this guy: https://monero.stackexchange.com/questions/3514/wallet-rpc-call-login-parameter-format-please
It would make life easier for developers if the authentication method was switched to Basic. We are not getting any detailed answers as to how to authenticate using java or python.
Bitcoin uses Basic authentication, so i would assume it is perfectly secure to switch to it or have it as an option.

# Discussion History
## vtnerd | 2017-01-31T18:07:57+00:00
Basic authentication sends the username/password in clear text. While no one should be opening the RPC server to external connections, and therefore reading the password "off-the-wire" should not be possible, I intentionally omitted basic authentication as a "hedge" against misconfiguration. If a user configured `monero-wallet-rpc` to allow remote RPC connections directly, digest authentication will prevent an attacker from learning the password which would allow for the issuance of arbitrary commands. Digest authentication also prevents against replay attacks, so an attacker cannot manipulate a previous completed request. There is also another extreme pessimistic case - if a user gives permissions for a local account to "sniff" packets (wireshark, etc), an attacker that has gained access to this account can see the passwords going to the local RPC server even when it is running as a different local user.

Admittedly digest mode is not perfect - the fields and body are not authenticated so an attacker could MitM and modify a not-yet-processed request - it still provides some additional protections that basic mode does not provide. This standard has been around for years and there are libraries in various languages supporting this mode, so the reduction in convenience seems minimal in this situation.

Edit for typo.

## hamiltino | 2017-01-31T23:58:36+00:00
For those who prefer convenience and ease of use over added security is it possible to include basic authentication as an option?

## jinglics | 2017-12-28T16:06:28+00:00
I cannot use nodejs request to connect JOSN RPC API with digest auth. Is that still a problem?

## dEBRUYNE-1 | 2018-01-08T12:36:46+00:00
+proposal

## saurabhprasadsah | 2021-11-24T09:56:49+00:00
how to add basic authentication in xmr

# Action History
- Created by: hamiltino | 2017-01-31T11:24:50+00:00
