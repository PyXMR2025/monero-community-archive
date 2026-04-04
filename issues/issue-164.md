---
title: 'VRP: clarify Email resolution strategy + enforce appropriate PGP keys for
  respective addresses'
source_url: https://github.com/monero-project/meta/issues/164
author: anonimal
assignees: []
labels: []
created_at: '2018-01-21T13:38:03+00:00'
updated_at: '2024-05-29T18:47:32+00:00'
type: issue
status: closed
closed_at: '2024-05-29T18:47:32+00:00'
---

# Original Description
As noted in https://github.com/monero-project/meta/pull/163:

>When explicitly mentioning the acceptance of emails for vulnerability reports, you should also try to handle them.

>In fact, all three PGP keys for Monero mentioned here (this goes to @fluffypony, @luigi1111, @moneromooo-monero) are not linked to the email address provided, making it even harder to grasp how to properly report a vulnerability by email. (My mail app doesn't allow to encrypt mails to A using a key for B, if B is not linked to A).

See #163 for details.

# Discussion History
## plowsof | 2024-05-25T18:26:32+00:00
Issue 1:    

Note the lack of an 'Email' @ https://github.com/monero-project/meta/blob/master/VULNERABILITY_RESPONSE_PROCESS.md#vii-resolutions 

- what email(s) should be used? e.g. 'incident.resolution AT getmonero dot org ? which would be forwarded to the hacker one team

Issue 2:  

>enforce appropriate PGP keys for respective addresses 

when we import keys of persons listed here:

- >gpg: key F4ACA0183641E010: public key "luigi1111 <luigi1111w@gmail.com>" imported
- >gpg: key 686F07454D6CEFC3: "moneromooo-monero <moneromooo-monero@users.noreply.github.com>" not changed

OP seems to be saying that their [unknown] pgp email client will not allow you to e.g. he can not email luigi AT getmonero DOT org because his gpg key isnt tied to that address.

To remedy this he needs to follow steps @ https://docs.github.com/en/authentication/managing-commit-signature-verification/associating-an-email-with-your-gpg-key  

So we need the relevant people to each individually add their getmonero emails (or watever we recommend to contact them on) to their pgp key as another uuid to satisfy the maker of this issue following the above steps, and presumably uploading their pub key which contains the new uuid.

>luigi must add a uuid to his key pair with luigi1111@getmonero.org as its email

[a pgp key pair can have multiple UID's](https://help.gnome.org/users/seahorse/stable/pgp-userid-add.html) 



## plowsof | 2024-05-29T18:40:48+00:00
if luigi doesn't consider this a compelling reason: (to allow the [unknown email/pgp client] to send a pgp encrypted email to `luigi1111@getmonero.org` with `luigi1111`'s pgp public key (which is only registered to a gmail account) to begin messing with his pgp key pair to add another uuid, then we can close this issue.  

# Action History
- Created by: anonimal | 2018-01-21T13:38:03+00:00
- Closed at: 2024-05-29T18:47:32+00:00
