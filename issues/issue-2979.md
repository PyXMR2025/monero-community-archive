---
title: Multiple blake256_update calls can be inconsistent with a single call
source_url: https://github.com/monero-project/monero/issues/2979
author: saleemrashid
assignees: []
labels: []
created_at: '2017-12-20T21:58:40+00:00'
updated_at: '2018-01-18T23:56:29+00:00'
type: issue
status: closed
closed_at: '2018-01-18T23:56:29+00:00'
---

# Original Description
Multiple `blake256_update` calls are not always consistent with a single `blake256_update` call over all of the data.

Below is a test program to demonstrate the issue that I found when using your implementation.

```bash
$ gcc test.c -o test -DBLAKE256_MONERO -Imonero/src/crypto monero/src/crypto/blake256.c
$ ./test
8592800bcc3c229c447fdc8c0ae998705904892ec1acbc53b155a9536b887324 # Multiple blake256_update
e88db3c1d542bad912d6fad016c658ba1c0a0144837efa6554f8a309fb581bc7 # One blake256_update
```

However, if you use the implementation from https://github.com/trezor/trezor-crypto/pull/125 which I replaced the Monero implementation with.

```bash
$ gcc test.c -o test -Itrezor-crypto trezor-crypto/blake256.c
$ ./test
e88db3c1d542bad912d6fad016c658ba1c0a0144837efa6554f8a309fb581bc7
e88db3c1d542bad912d6fad016c658ba1c0a0144837efa6554f8a309fb581bc7
```

Here are the contents of `test.c`

```c
#include <stdio.h>
#include <string.h>

#include "blake256.h"

#if BLAKE256_MONERO
#define blake256_Init                 blake256_init
#define blake256_Update(S, in, inlen) blake256_update(S, in, (inlen) * 8);
#define blake256_Final                blake256_final

static state S;
#else
static BLAKE256_CTX S;
#endif

static uint8_t buffer[128];
static size_t length = 0;

static void test_update(const uint8_t *in, size_t inlen) {
	blake256_Update(&S, in, inlen);

	memcpy(&buffer[length], in, inlen);
	length += inlen;
}

static void print_hash(void) {
	uint8_t hash[32];
	blake256_Final(&S, hash);

	for (size_t i = 0; i < sizeof(hash); i++) {
		printf("%02hhx", hash[i]);
	}
	printf("\n");
}

int main(int argc, char **argv) {
	static const uint8_t A[] = { 0x01, 0x00, 0x03, 0x00 };
	static const uint8_t B[] = { 0x02 };
	static const uint8_t C[] = { 0x00 };
	static const uint8_t D[] = { 0x69 };
	static const uint8_t E[] = { 0x52, 0x21, 0x03, 0x33, 0x4d, 0xd6, 0xc5, 0x8f, 0xae, 0x3d, 0x46, 0x2f, 0x35, 0x91, 0x25, 0xf0, 0xd6, 0x83, 0x5e, 0x57, 0xad, 0x88, 0x5e, 0x50, 0x58, 0xb4, 0x17, 0xf2, 0x17, 0xde, 0xcc, 0x21, 0xfd, 0xbb, 0xa4, 0x21, 0x03, 0x92, 0xaf, 0x36, 0xb8, 0xa6, 0x5e, 0xa0, 0xbb, 0x6f, 0x0a, 0xcd, 0xec, 0x90, 0x69, 0xa0, 0xb5, 0xb7, 0x5b, 0x00, 0xd9, 0x66, 0x7b, 0x89, 0xe2, 0xa7, 0x7f, 0x92, 0xd4, 0xef, 0xc9, 0x2b, 0x98, 0x21, 0x02, 0x59, 0x45, 0xb9, 0xf1, 0x1a, 0x71, 0x54, 0x6a, 0xfe, 0x4a, 0xf2, 0x8c, 0xd2, 0x91, 0x83, 0x0f, 0xd7, 0x7c, 0xb1, 0x84, 0x00, 0x6a, 0x90, 0x22, 0x3d, 0xe1, 0xb2, 0xc2, 0x65, 0x02, 0xbf, 0xc3, 0x53, 0xae };

	blake256_Init(&S);
	test_update(A, sizeof(A));
	test_update(B, sizeof(B));
	test_update(C, sizeof(C));
	test_update(D, sizeof(D));
	test_update(E, sizeof(E));
	print_hash();

	blake256_Init(&S);
	blake256_Update(&S, buffer, length);
	print_hash();

	return 0;
}
```

# Discussion History
## moneromooo-monero | 2017-12-20T23:18:30+00:00
Fixed by:

```
diff --git a/src/crypto/blake256.c b/src/crypto/blake256.c
index 1e43f9c..95b2a69 100644
--- a/src/crypto/blake256.c
+++ b/src/crypto/blake256.c
@@ -157,7 +157,7 @@ void blake256_update(state *S, const uint8_t *data, uint64_t datalen) {
     int left = S->buflen >> 3;
     int fill = 64 - left;
 
-    if (left && (((datalen >> 3) & 0x3F) >= (unsigned) fill)) {
+    if (left && (((datalen >> 3)) >= (unsigned) fill)) {
         memcpy((void *) (S->buf + left), (void *) data, fill);
         S->t[0] += 512;
         if (S->t[0] == 0) S->t[1]++;
```

from comparing with the source at https://github.com/veorq/BLAKE/blob/master/blake256.c

However, I don't know why that is put here. I've not checked whether this still syncs the chain.



## saleemrashid | 2017-12-21T09:08:51+00:00
@moneromooo-monero It shouldn't change anything as `left == S->buflen == 0` when Monero uses `blake256_update` (`hash_extra_blake` is the only place it is called from and that uses `blake256_hash`).

## stoffu | 2017-12-21T09:34:10+00:00
I reproduced the reported issue, confirmed that the above patch fixes it, and confirmed that the patch doesn't affect the blockchain verification.

@saleemrashid 
I'm not familiar with this algorithm at all, but the patch does seem to make a difference. Maybe you're overlooking some code path?

## saleemrashid | 2017-12-21T09:49:06+00:00
@stoffu It should not make a difference for the **first call** to `blake256_update`. Monero uses `hash_extra_blake` which uses `blake256_hash` which makes a **single call** to `blake256_update`.

To be clear, I don't doubt it fixes my problem. I'm saying that it shouldn't break Monero.

## stoffu | 2017-12-21T11:20:30+00:00
Makes sense, thank you.

## moneromooo-monero | 2017-12-22T12:14:42+00:00
I made a PR in https://github.com/monero-project/monero/pull/2988 then. Thanks for the detailed repro case.

## saleemrashid | 2017-12-22T13:24:34+00:00
> However, I don't know why that is put here.

@veorq confirmed on Twitter that it was a bug present in a previous version of the implementation.

> Thanks for the detailed repro case.

Thanks for fixing it so quickly!

## moneromooo-monero | 2017-12-22T14:21:05+00:00
Good, I had searched for blake update 0x3f but hadn't found anything, so that explanation is satisfying.

## moneromooo-monero | 2018-01-18T23:33:12+00:00
+resolved

# Action History
- Created by: saleemrashid | 2017-12-20T21:58:40+00:00
- Closed at: 2018-01-18T23:56:29+00:00
