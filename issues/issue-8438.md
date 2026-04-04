---
title: Scalar not reduced in tx e4b7982b081a17892525f1b1d3011ec06a0820cbf451d3a64f8ea998104a753c
source_url: https://github.com/monero-project/monero/issues/8438
author: DangerousFreedom1984
assignees: []
labels: []
created_at: '2022-07-16T16:20:54+00:00'
updated_at: '2023-06-06T01:36:11+00:00'
type: issue
status: closed
closed_at: '2023-06-06T01:36:11+00:00'
---

# Original Description
Hello,
While scanning the blockchain with my own tools, I found some strange scalars that are not reduced, i.e. they are not mod 'l' where l = 2^252 + 27742317777372353535851937790883648493. These scalars are very rare to find in the blockchain but they exist. One example is in the transaction e4b7982b081a17892525f1b1d3011ec06a0820cbf451d3a64f8ea998104a753c. You can see that the scalar  cb2be144948166d0a9edb831ea586da0c376efa217871505ad77f6ff80f203f8 is not reduced. Otherwise it should be stored as e8c079d208b352a71abd36a5deb45c67c276efa217871505ad77f6ff80f20308. My question is simple: why?
I have checked the 'sc_reduce32' function in C and it is working for this number also. I have also checked the functions to generate and manipulate the bb.s0 like skGen and sc_mulsub and they all include the sc_reduce32 in their operations. Can someone explain me what is happening and the implications of it?
Thank you very much in advance!

# Discussion History
## UkoeHB | 2022-07-16T17:02:32+00:00
This is an oversight in the verifier code. MLSAG and CLSAG both include `sc_check()` calls for tighter semantics (it may also be necessary depending which crypto ops you are calling - the documentation isn't very good on these).

You could try reducing scalars with `sc_reduce32()` and check if the proofs are still valid using the reduced versions (reduce after computing challenges if the scalars are part of the hash content).

## Mitchellpkt | 2022-07-17T17:19:20+00:00
Great find @DangerousFreedom1984 - this is a very subtle fingerprint. Do you have a sense of how many transactions exhibit this fungibility defect?

## DangerousFreedom1984 | 2022-07-17T17:35:31+00:00
So far I found three times in Borromean Signatures (which I believe that was all) and none in Bulletproofs (but I am very far from scanning the whole bulletproofs transactions).

## DangerousFreedom1984 | 2022-07-17T18:12:27+00:00
@Mitchellpkt but I will give an update by the middle of the week. I was hoping that someone would precisely answer that so I would spare a bit of time :p. Maybe @UkoeHB 's answer is what is happening but I have not verified myself yet.

## DangerousFreedom1984 | 2022-07-20T20:55:44+00:00
 **Wrong signatures in the blockchain**

While scanning the blockchain with my reliable Python tools, as I am using the LibSodium library for all the crypto operations, I found a mismatch between a signature and its expected value. So basically, a wrong signature. At the time I was not sure if it was a bug in my code or Monero's code. After analyzing carefully every multiplication I found out that Monero was performing a wrong operation. More precisely, there is a function called addKeys2(res,a,b,B) that does res = aG+bB and the result of this function is wrong for certain non reduced scalars. You can check by yourself running the snippet below in C++ using the Monero libraries:

```
rct::key P1,bbee,bbs0,b2,res;
rct::key C,D,E1,E2,P1bbee,Base;

epee::string_tools::hex_to_pod("1a7112a70bf953ce7061693f145add80fea7cfaf50456e1440622cc7a986e2a1", P1);
epee::string_tools::hex_to_pod("cb2be144948166d0a9edb831ea586da0c376efa217871505ad77f6ff80f203f8", bbs0);
epee::string_tools::hex_to_pod("e8c079d208b352a71abd36a5deb45c67c276efa217871505ad77f6ff80f20308", b2);
epee::string_tools::hex_to_pod("a29635109c80c54623a8a63e412daec9bc4646fdad9ac5db006d7c541b645302", bbee);


C = scalarmultBase(bbs0);
D = scalarmultBase(b2);


scalarmultKey(P1bbee,P1,bbee);
addKeys(E1, C, P1bbee);
addKeys(E2, D, P1bbee);


std::cout << "Result of scakarmultBase C: " << std::endl;
std::cout << epee::string_tools::pod_to_hex(C) << std::endl;

std::cout << "Result of scakarmultBase D: " << std::endl;
std::cout << epee::string_tools::pod_to_hex(D) << std::endl;

std::cout << "Result of C + P1: " << std::endl;
std::cout << epee::string_tools::pod_to_hex(E1) << std::endl;

std::cout << "Result of D + P1: " << std::endl;
std::cout << epee::string_tools::pod_to_hex(E2) << std::endl;

addKeys2(res, b2, bbee, P1);
std::cout << "Result of multiplication reduced: " << std::endl;
std::cout << epee::string_tools::pod_to_hex(res) << std::endl;

addKeys2(res, bbs0, bbee, P1);
std::cout << "Result of multiplication not reduced: " << std::endl;
std::cout << epee::string_tools::pod_to_hex(res) << std::endl;
```

And the result is the following:

```
Result of scakarmultBase C: 
4014ab9200745ab76fab92fb92c6ba162372c8449b8cbd5485f4676c2d823a0d
Result of scakarmultBase D: 
4014ab9200745ab76fab92fb92c6ba162372c8449b8cbd5485f4676c2d823a0d
Result of C + P1: 
101713c9e5f1184343eaf50c6626bb4fddd90a9886a99ff337d101ed2dd62433
Result of D + P1: 
101713c9e5f1184343eaf50c6626bb4fddd90a9886a99ff337d101ed2dd62433
Result of multiplication reduced: 
101713c9e5f1184343eaf50c6626bb4fddd90a9886a99ff337d101ed2dd62433
Result of multiplication not reduced: 
97a2c482e50176969a66683609c4aea719b5c3ab4535ae4b33b01307c4fbf1a6
```

Which should be the same no matter if reduced or not! What is happening is that Monero is interpreting a, in the equation res = aG+bB, as another scalar different from its reduced form. Generating, therefore, a wrong signature and it also accepts (verify as correct) a wrong signature as it doing the same mistake to interpret these different scalars.

**Why that is happening?**

So far, the best explanation is because of a pre-requisite in the function ge_double_scalarmult_base_vartime which requires a[31]<=127.

**How bad is that?**

It is clear now that Monero has stored wrong rangeproofs signatures (Borromean signatures) that do not correspond to the stored value in the blockchain to be verified, an easy way to see it is by performing res = aG+bB using two different methods as shown above. It is not so bad though as it is also making a mistake in interpreting these scalars so instead of that being exploited it is a kind of malleability issue.

**Implications**

A full research is being conducted by me (and now I invite everyone else too) to answer the extend and possible vulnerabilities coming from this mistake. As I have proved, the function addKeys2 is wrong for certain inputs and therefore it should be replaced or we should make sure that the inputs obey certain conditions, like being reduced (get the mod of the order of the curve). After a fruitful discussion with Koe, Moneromooo and Luigi, which I am very thankful for their replies, I believe it will be done soon but we are not really concerned as all CLSAG and Bulletproofs functions already make sure of that. There are other minor functions that don't yet though.

So far I have only logged three transactions that presents this behaviour but I have also neglected some as I was thinking that my code was buggy :p I'm pretty sure that there are more than three that presents wrong Borromean signatures in the blockchain, which does not directly reads as inflation has happened.

The funky transactions are:

>     e4b7982b081a17892525f1b1d3011ec06a0820cbf451d3a64f8ea998104a753c
>     d5d725e7a76dab7e2ca97d941403936a0fbf5e8874e9ef3becd973e4598a8cb1
>     0647d386365f6bfd312b0fbe966f5c85f19159ccf9003af8387f332451e6c94c

**What can we do?**

I am still digging deeper into this issue and looking for possible vulnerabilities, which I did not find any so far. It is still an open issue for me and I cannot fully explain all the implications and reasons for this to be happening as I do not fully understand all the lines that the C libraries are doing (yet :p). Meanwhile, I suggested to double check the inputs of the functions using addKeys2. Specially genC, which seems to me a vulnerable point but not exploitable though as it would be pretty hard to find any relation between G and H.

If you try to exploit it alone at home, please share your results like I am doing so we can achieve a consensus faster :)

## UkoeHB | 2022-07-20T21:52:36+00:00
Nonreduced scalars passed to `ge_double_scalarmult_base_vartime()` are effectively treated as 'some other scalar'. This means, in practice, that nonreduced scalars recorded in the chain data for Borromean signatures have a nonstandard serialization.

You can recover the actual scalar used by running this function (add it to `src/crypto/crypto-ops.c`). To verify that the recovered scalar is accurate, run `ge_double_scalarmult_base_vartime()` with both the nonreduced and recovered scalars - you should get the same results.

```
void ge_scalarmult_vartime_nonreduced_recover(unsigned char *scalar_recovered, const unsigned char *b)
{
  signed char bslide[256];
  int i;

  slide(bslide, b);

  for (i = 255; i >= 0; --i) {
    if (bslide[i]) break;
  }

  unsigned char scalars_precomputed[8][32];
  for (unsigned char j = 0; j < 8; ++j)
  {
    sc_0(scalars_precomputed[j]);
    scalars_precomputed[j][0] = j*2 + 1;
  }

  sc_0(scalar_recovered);

  for (; i >= 0; --i) {
    sc_add(scalar_recovered, scalar_recovered, scalar_recovered);

    if (bslide[i] > 0) {
      sc_add(scalar_recovered, scalar_recovered, scalars_precomputed[bslide[i]/2]);
    } else if (bslide[i] < 0) {
      sc_sub(scalar_recovered, scalar_recovered, scalars_precomputed[(-bslide[i])/2]);
    }
  }
}
```

## DangerousFreedom1984 | 2022-07-20T21:55:03+00:00
Yes, but I don't understand where the error originates. Do you know? Why and where exactly this happens?

## UkoeHB | 2022-07-20T21:57:00+00:00
The error comes from the `slide()` function, which has an undocumented precondition that the input scalar must be reduced if you want the output to be accurate. I guess if you violate that precondition, then you get 'some other scalar'. There is no deeper meaning to it.

## DangerousFreedom1984 | 2022-07-20T21:59:18+00:00
Ok. Yeah, I don't see then how it could be exploited if it is deterministic. Thank you!

## DangerousFreedom1984 | 2022-09-03T14:56:05+00:00
[Here](https://www.moneroinflation.com/static/data_py/report_scalars_df.pdf) is an update containing all the transactions presenting this behaviour.

## selsta | 2023-06-06T01:36:11+00:00
Closing as this issue was fully researched.

# Action History
- Created by: DangerousFreedom1984 | 2022-07-16T16:20:54+00:00
- Closed at: 2023-06-06T01:36:11+00:00
