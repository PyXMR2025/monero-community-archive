---
title: Wrong SKEIN function selection for cryptonight implementation
source_url: https://github.com/monero-project/monero/issues/2001
author: remagpie
assignees: []
labels: []
created_at: '2017-04-24T03:17:57+00:00'
updated_at: '2017-04-24T10:54:40+00:00'
type: issue
status: closed
closed_at: '2017-04-24T10:52:37+00:00'
---

# Original Description
According to [this document](https://cryptonote.org/cns/cns008.txt), hash function should select SKEIN-256 at certain situation.
However, according to [crypto/skein.c](https://github.com/monero-project/monero/blob/master/src/crypto/skein.c#L20), SKEIN-256 is turned off.
Instead, [SKEIN-512 with block size 256](https://github.com/monero-project/monero/blob/master/src/crypto/skein.c#L1942) is turned on.
Is there any specific reason for this?

# Discussion History
## fluffypony | 2017-04-24T07:53:31+00:00
@Kais-DkM I wouldn't trust documents on the CryptoNote website, as they were created after-the-fact. With inherited code like this we veer more towards "the documentation is the code", and tend not to change things unless they have been found dodgy in practice or there is some suspicion of brokenness.

## remagpie | 2017-04-24T09:47:12+00:00
@fluffypony
Then is it document's fault for this case?
Code is reference for actively maintained project like here, but in my thought, document should be valid at same time.

## fluffypony | 2017-04-24T09:58:40+00:00
@Kais-DkM we aren't connected to CryptoNote, and are far divorced from our CryptoNote origins. The inherited bits of code that still remain in the source tree are slowly being phased out (e.g. wire protocol is being replaced with ZMTP). I wouldn't rely on CryptoNote documentation to be a reflection of anything in Monero, because it isn't:)

## remagpie | 2017-04-24T10:52:37+00:00
@fluffypony 
Oh, then maybe I should reopen issue in CryptoNote's repository.
Closing this issue, and thank you for your response.

## fluffypony | 2017-04-24T10:54:40+00:00
@Kais-DkM no problem, any time:)

# Action History
- Created by: remagpie | 2017-04-24T03:17:57+00:00
- Closed at: 2017-04-24T10:52:37+00:00
