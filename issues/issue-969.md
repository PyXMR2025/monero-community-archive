---
title: 'Seraphis wallet workgroup meeting #58 - Monday, 2024-02-19, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/969
author: rbrunner7
assignees: []
labels: []
created_at: '2024-02-16T18:13:15+00:00'
updated_at: '2024-02-19T18:51:46+00:00'
type: issue
status: closed
closed_at: '2024-02-19T18:51:45+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/967

# Discussion History
## rbrunner7 | 2024-02-19T18:51:46+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/969
<j​effro256> Howdy!
<d​angerousfreedom> Hi
<r​brunner7> Anything to report from last week?
<d​angerousfreedom> I did some PRs to ghostway key_container and koe's seraphis_lib
<d​angerousfreedom> I would like that we could agree on the minimum necessary features for the key_container.cpp and jamtis_keys.cpp soon
<j​effro256> I'm happy to say that @UkoeHB is back. And he has started reviewing the Jamtis changes to the "Implementing Serpaphis" paper
<rbrunner7> +1
<jeffro256> +1
<tobtoht> +1
<d​angerousfreedom> Great! I have some questions for Koe too :p
<d​angerousfreedom> Basically it is about notation...
<d​angerousfreedom> 1) To derive the view_balance key we should use [KeyDerive2](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024#332-ed25519) instead of [KeyDerive1](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024#331-curve25519) as [stated](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024#431-standard-wallets), right?
<d​angerousfreedom> 2) In jamtis at [3.3.1](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024#331-curve25519) it is stated that "All Curve25519 private keys are therefore multiples of the cofactor 8, which ensures that all public keys are in the prime-order subgroup." Is it accurate since we dont talk about reducing to mod l ? Since skGen already reduces the scalar to order l then is t<clipped 
<d​angerousfreedom> hat knowledge implicit on that phrase? Otherwise we could land at large subgroups of order 2l,4l,8l right?
<d​angerousfreedom> 3) The private keys that are Ed25519 won't be clamped but just reduced ( %mod l), right? If not, are there problems that could arise? I read [this](https://doc.libsodium.org/advanced/point-arithmetic#scalar-multiplication-without-clamping) phrase here and I'm trying to build my understand on these cases.
<r​brunner7> dangerousfreedom: Is anything from you already in a form ready for final review and merge afterwards?
<d​angerousfreedom> I made a PR to ghostway PR on the key container. I would say that if he agrees with the changes, I would be satisfied with the state for a review.
<r​brunner7> And, jeffro256 , is the rebase of the Seraphis libary to Monero master complete?
<j​effro256> dangerousfreedom: yes you want keyderive2 since `k_vb` is a ed25519 key, not a X25519 key
<d​angerousfreedom> I believe that the key_container and the jamtis_keys are currently doing what they are supposed to (in a basic sense since much more functions will certainly be added in the future)
<r​brunner7> Alright, let's see what ghostway will do. What is the state of this here? https://github.com/seraphis-migration/monero/pull/17
<j​effro256> rbrunner7: It's all done except for that one android build issue, but @tobtoht said he/she would PR something to monero-project/master that ends up fixing later, so I would just go ahead and rebase seraphis_wallet against seraphis_lib
<d​angerousfreedom> This is ready for a review.
<jeffro256> +1
<r​brunner7> That should be within my reach to review, other than stuff that has too much "crypto" in it :)
<r​brunner7> Ok, I will try what happens if I try to update our repository with that.
<j​effro256> dangerousfreedom: IIRC, "clamping" means that the scalar has a factor of 8, which means that we don't have to reduce mod l for the point to fall within a group of order l
<d​angerousfreedom> Clamping means basically multiplying by 8. But that does not guarantee a canonical (reduced) scalar. So if I understand correctly, the reduction should always be done. But I think it was implicit on that phrase
<d​angerousfreedom> Also almost all the operation with scalars do that. For example a*b = a*b (mod l)
<d​angerousfreedom> It is not a big deal I guess to have Points outside the main subgroup. It is just important for the key_images, right?
<moneromoooo> I'm just randonly here but *8 is (in monero) used on points, not scalars. To place them in the main subgroup. Nothing to do with reducing.
<j​effro256> Well since a = a + l (mod l), it shouldn't make a difference to the result mathematically unless the EC library has a bug (or documented issue) such that any scalar greater than or equal to l will cause the computation to come up with a different result. But you're right that it's probably best practice to do so for the best interoperability
<moneromoooo> Unless this is something specific to seraphis, in which case I'll show myself out...
<j​effro256> Shouldn't be specific to Seraphis IIUC
<d​angerousfreedom> Yes, not to do with reducing. But if you clamp scalars (as proposed by tevador) in the private X25519 keys, you make sure that the points generated by them land on the prime subgroup (if they are reduced I guess). Right?
<r​brunner7> By the way, after dangerousfreedom mentioned in last week's meeting that everybody could freely edit our wiki, I have reconfigured it now. That's this here: https://github.com/seraphis-migration/strategy/wiki/Seraphis-Wallet-Workgroup
<r​brunner7> Now only people who get granted write access can edit. I have done that for all active members of the organisation. jeffro256 and jberman are not yet members.
<r​brunner7> I think they should be. Care for some invite? :)
<r​brunner7> GitHub anyway reminds me that the organisation should have at least 2 admins. Bus factor and all ...
<j​effro256> Yes, should be. Since for any point P in ed25519, 8P will be on the prime order subgroup. And 8P is equal to (8 * p) * G, so if p has a divisor mod 8, then, P should be on the prime order subgroup IIUC. Again, you don't HAVE to reduce the private key mod l to be on the subgroup theoretically, but it's good practice when using real code. Plz don't quote me tho
<j​effro256> s/mod 8/8 mod l
<j​effro256> rbrunner7: got the error message "Sorry, we couldn't find that repository invitation. It is possible that the invitation was revoked or that you are not logged into the invited account. "
<r​brunner7> I try again.
<j​effro256> @UkoeHB if you are on right now, would you like to discuss auxiliary enote records in the paper? https://github.com/UkoeHB/Seraphis/pull/6#discussion_r1493615501
<d​angerousfreedom> jeffro256: I don't think I agree. There are 8L points on the curve where L = 2**252 + ... There are only L points in the main subgroup. If you pick one of these points on the 2L,4L, 8L subgroup and multiply by 8, they will not land on the main subgroup. Right?
<r​brunner7> Seems we are a bit stuck. UkoeHB does not seem to be online and free.
<d​angerousfreedom> My understanding may be wrong also. I have to study more :p
<jeffro256> +1
<d​angerousfreedom> I will try to look at your changes on the view_key and your PR regarding the blockchain modifications jeffro256 . I will send you some message if I dont understand something ;)
<j​effro256> It's a bit counterintuitive, but multiplying by 8 puts the point OUTSIDE of the 8 or 8l subgroups, much like multiplying by l puts us OUTSIDE of the l subgroup, which is why use multiplying by l gives us the point at infinity and why we use that as a test for being in the subgroup in regards to the key images
<t​obtoht> #9182
<jeffro256> +1
<j​effro256> If you think about it using integer groups, say mod n, multiplying by n is the same as multiplying by zero
<r​brunner7> Alright. Food for thought and research :) Anything else to discuss in this meeting right now?
<r​brunner7> Doesn't look like it. Think we can close for today. Thanks for attending, read you again next week!
<j​effro256> Thanks everyone
<dangerousfreedom> Thanks
````


# Action History
- Created by: rbrunner7 | 2024-02-16T18:13:15+00:00
- Closed at: 2024-02-19T18:51:45+00:00
