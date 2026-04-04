---
title: 'Allow ringCT type 3 after V11 '
source_url: https://github.com/monero-project/monero/issues/5845
author: jtomtan
assignees: []
labels: []
created_at: '2019-08-23T10:37:43+00:00'
updated_at: '2019-08-26T09:00:08+00:00'
type: issue
status: closed
closed_at: '2019-08-26T08:48:05+00:00'
---

# Original Description
Hi,  I am from Ownbit Wallet team. 

I think ringCT type 3 should be allowed in V11 and later. We should always have the backward compatibility. If want the most TX upgrade to type4,  we can charge more fees for type 3. 

Now the existing JS implement for monero are only for type 3. It's difficult for all wallets upgrade to type 4 in short time. 

Bitcoin always have backward compatibility.  And I also recommend the Monero official team to provide a JS library for offline signing (with ringCT type 4)

# Discussion History
## moneromooo-monero | 2019-08-23T11:37:04+00:00
No good reason to, except cater for people who use custom code and don't update it. It's a fingerprinting vector, and adds unnecessary extra storage and verification time.

## jtomtan | 2019-08-23T11:41:53+00:00
> No good reason to, except cater for people who use custom code and don't update it. It's a fingerprinting vector, and adds unnecessary extra storage and verification time.

Is there any document or guide to describe how to implement type4. I have JS code for type3. What  change should I do to make it become type 4? 

As I understand, type 3 is bulletproof v1 and type 4 is bulletproof v2 , right? What's the detailed difference between them? Any detailed code to show me the difference? Thanks very much. 

## moneromooo-monero | 2019-08-23T16:51:00+00:00
There are three changes, one of them trivial, and the others fairly simple:
cdc3ccec5fd7925d93babff8a9a421c538f3cce0
99d946e6191056f747225d36a2408085624b516e
7d375981584e5ddac4ea6ad8879e2211d465b79d


## moneromooo-monero | 2019-08-25T18:34:32+00:00
While I'm not going to debug your javascript, one thing that jumps at me is that you seem to be using the salts as hex dumps, rather than raw. If this is indeed what is being done, this is wrong.

## jtomtan | 2019-08-26T07:50:42+00:00
> While I'm not going to debug your javascript, one thing that jumps at me is that you seem to be using the salts as hex dumps, rather than raw. If this is indeed what is being done, this is wrong.

When spending a bulletproof2 output, to generate the signature, a inSk is needed. As I understand, 
inSk {
x: --> the one time private key for the real_output
a: --> the mask
}
What is the mask for inSk of bulletproof2 to fill? Since now the mask is deterministic, what to fill here? 

## moneromooo-monero | 2019-08-26T08:21:07+00:00
```
    key genCommitmentMask(const key &sk)
    {
        char data[15 + sizeof(key)];
        memcpy(data, "commitment_mask", 15);
        memcpy(data + 15, &sk, sizeof(sk));
        key scalar;
        hash_to_scalar(scalar, data, sizeof(data));
        return scalar;
    }
```

sk is the result of derivation_to_scalar from the output's derivation.

## jtomtan | 2019-08-26T08:48:05+00:00
> ```
>     key genCommitmentMask(const key &sk)
>     {
>         char data[15 + sizeof(key)];
>         memcpy(data, "commitment_mask", 15);
>         memcpy(data + 15, &sk, sizeof(sk));
>         key scalar;
>         hash_to_scalar(scalar, data, sizeof(data));
>         return scalar;
>     }
> ```
> 
> sk is the result of derivation_to_scalar from the output's derivation.

Great, it works! Thanks a lot for the guidance. The first pure JS code for bulletproof2 is now working. We will first use it in the Ownbit wallet. And later we may open source it, thanks for the help!  

# Action History
- Created by: jtomtan | 2019-08-23T10:37:43+00:00
- Closed at: 2019-08-26T08:48:05+00:00
