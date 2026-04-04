---
title: Constant-value fees
source_url: https://github.com/monero-project/monero/issues/3766
author: zawy12
assignees: []
labels: []
created_at: '2018-05-06T20:25:40+00:00'
updated_at: '2018-05-09T13:13:07+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I'm told Monero is interested in stable-valued fees.  If POW's were not changed, and if Moore's law has mostly died out, there is a good approximate measure of real-world price already on the block chain.  

constant-value-fee = F2 = F1 * D1 / D2 * R2 / R1 * M(time)

Where F1 is the fee you've selected today that is implicitly based on a current external world dollar amount per coin.  F2 is what the transaction fee should at some time in the future.  D and R are difficulty and reward per block.  M(time) is an adjustment factor that is a function of time and makes some assumption about how Moore's law will change from here on out. It gets larger with time.

But don't be a moocher.  Send me a donation if you use this idea.

# Discussion History
## Gingeropolous | 2018-05-08T03:26:19+00:00
yeah, i've been talking about this kind of thing for a while. I would posit you need to include the blocksize in the fee... the difficulty is the perceived value of the coin (a lot of people hopping on to mine), whereas the blocksize is the actual value - a lot of people are transacting. Both parameters capture an aspect of value that can be used to serve a proxy for external blockchain value. 

I think the question is figuring out your magic number M. 

## zawy12 | 2018-05-08T08:23:21+00:00
If the number of people transaction goes up, it supposedly increases price via velocity of money, but that would be reflected in the difficulty increase already.  There are fees for transactions that motivate a difficulty increase in the same way price does, so my equation is missing it.  I think it is possible to do a POW that maximally wastes electricity without regard to mining hardware but is dependent on line resolution of the underlying processor which is known the next 10 years (the true Moore's law in terms of transistors per area). Beyond that is anyone's guess.

## zawy12 | 2018-05-08T15:14:16+00:00
This is the general equation that relates future coin price to future difficulty:

```P1*(R1 + nb1*Fb1 + total1*Fp1) / D1 * M1 = P2*(R2 + nb2*Fb2 + total2*Fp2) / D2 * M2 ```

Where
1 and 2  = measures at time 1 (now) and time 2 (future)
P = USD price / coin
R = coins/block reward
D = difficulty  ( D = hashes\*T / 2^x where x is leading zeros in maxTarget)
Fb = coin fee per byte
nb = number of bytes per block
Fp = Percent fee per coin transferred (for a more general equation)
total = total coins transferred per block. 
M = "Moore's law" adjustment = hashes per USD mining expense.

If the relative rate of Fb and Fp does not change, Fp = k\*Fb, so you can easily solve for the future Fb2 and Fp2 given a beginning Fb1.  

To show it from a bigger perspective, the above is:

(P=USD/block) / (D=hashes/block) * (M=hashes/USD)  = a unit-less constant ratio

USD here is a substitute for constant value.  The fees in this equation are constant value even if USD value changes because USD cancels.   If the POW can be made where mining is mostly an electrical expense (see my POW idea), then this constant value metric is based on electricity which is the best single-commodity metric of constant value.  

This can be used to create a constant-value coin, but I haven't written the white paper yet.

# Action History
- Created by: zawy12 | 2018-05-06T20:25:40+00:00
