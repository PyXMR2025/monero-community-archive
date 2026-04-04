---
title: Can't create transaction
source_url: https://github.com/monero-project/monero/issues/4206
author: Cryptoxylx
assignees: []
labels:
- invalid
created_at: '2018-08-01T12:41:36+00:00'
updated_at: '2018-08-30T15:01:09+00:00'
type: issue
status: closed
closed_at: '2018-08-30T15:01:09+00:00'
---

# Original Description
Can't create transaction: not enough money to transfer, available only 0.00000000
I have unlocked balance of over 10,000

# Discussion History
## moneromooo-monero | 2018-08-01T13:14:23+00:00
How much are you trying to transfer, and how many outputs to you have ?

## Cryptoxylx | 2018-08-01T16:45:48+00:00
I can't even transfer 1 monero

On Wed, Aug 1, 2018, 14:14 moneromooo-monero <notifications@github.com>
wrote:

> How much are you trying to transfer, and how many outputs to you have ?
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/4206#issuecomment-409570172>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AcmgY9mcZ2F3IdHaA0NrTGMSkz2kbK96ks5uManDgaJpZM4VqbF9>
> .
>


## moneromooo-monero | 2018-08-01T18:14:49+00:00
Start monero-wallet-cli with --log-level 2, do it again, then paste the resulting log (monero-wallet-cli.log).
If you want to keep it private, you can GPG encrypt it with my public key in utils/gpg_keys/moneromooo.asc


## moneromooo-monero | 2018-08-01T18:16:08+00:00
Also, paste the output of "incoming_transfers". Encrypted if you want too.


## alexmateescu | 2018-08-08T21:17:47+00:00
i have the same issue with another coin but with exactly the same wallet as monero. log below.


root@wallet:~/mutex/build/release/bin# tail -n 500 mutex-wallet-cli.log 

2018-08-08 21:13:41.681	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:6629	constructed tx, r=1
2018-08-08 21:13:41.681	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:6686	gathering key images
2018-08-08 21:13:41.681	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:6695	gathered key images
2018-08-08 21:13:41.681	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:6722	transfer_selected_rct done
2018-08-08 21:13:41.682	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7685	Made a 13529 bytes (14 kB) tx, with 512.920000000 available for fee (0.459434640 needed)
2018-08-08 21:13:41.682	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7716	We made a tx, adjusting fee and saving it, we need 0.459434640 and we have 0.459434640
2018-08-08 21:13:41.682	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7731	Made a final 13529 bytes (14 kB) tx, with 0.459434640 fee  and 512.460565360 change
2018-08-08 21:13:41.682	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7742	We have more to pay, starting another tx
2018-08-08 21:13:41.682	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7551	Start of loop with 20 0
2018-08-08 21:13:41.682	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7552	unused_transfers_indices: 194 141 316 179 226 245 260 149 150 152 292 317 286 250 157 210 204 220 193 203
2018-08-08 21:13:41.682	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7553	unused_dust_indices: 
2018-08-08 21:13:41.682	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7554	dsts size 1, first 12425.296165530
2018-08-08 21:13:41.682	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7555	adding_fee 0, use_rct 1
2018-08-08 21:13:41.682	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7597	Picking output 179, amount 513.420000000, ki <c04610350490a82e5a8503097381bcbba0d1777efcfda3d54a91282bc7c2d23c>
2018-08-08 21:13:41.682	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 1 with ring size 7 and 1: 1386 (512 saved)
2018-08-08 21:13:41.682	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7629	We can partially pay ZYZXZgatLjtFycXKri3YpjJ3fp42XYd3UURcMJ4rBVTVhv49hiiUdEcPrRhEMUVaB1MVyQz7xuKQTUsT7HL1gHRxewvn7BaBeKg for 513.420000000/12425.296165530
2018-08-08 21:13:41.682	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7638	Considering whether to create a tx now, 1 inputs, tx limit 19400
2018-08-08 21:13:41.682	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 1 with ring size 7 and 2: 2195 (544 saved)
2018-08-08 21:13:41.682	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7551	Start of loop with 19 0
2018-08-08 21:13:41.682	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7552	unused_transfers_indices: 194 141 316 203 226 245 260 149 150 152 292 317 286 250 157 210 204 220 193
2018-08-08 21:13:41.682	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7553	unused_dust_indices: 
2018-08-08 21:13:41.682	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7554	dsts size 1, first 11911.876165530
2018-08-08 21:13:41.682	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7555	adding_fee 0, use_rct 1
2018-08-08 21:13:41.682	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7597	Picking output 149, amount 507.210000000, ki <084c39c74769fc0291430510311ce58699bddf3d6a1da087489d9cc3ff2a4d04>
2018-08-08 21:13:41.682	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 2 with ring size 7 and 2: 2760 (1024 saved)
2018-08-08 21:13:41.682	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7629	We can partially pay ZYZXZgatLjtFycXKri3YpjJ3fp42XYd3UURcMJ4rBVTVhv49hiiUdEcPrRhEMUVaB1MVyQz7xuKQTUsT7HL1gHRxewvn7BaBeKg for 507.210000000/11911.876165530
2018-08-08 21:13:41.682	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7638	Considering whether to create a tx now, 2 inputs, tx limit 19400
2018-08-08 21:13:41.682	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 2 with ring size 7 and 2: 2760 (1024 saved)
2018-08-08 21:13:41.682	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7551	Start of loop with 18 0
2018-08-08 21:13:41.682	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7552	unused_transfers_indices: 194 141 316 203 226 245 260 193 150 152 292 317 286 250 157 210 204 220
2018-08-08 21:13:41.682	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7553	unused_dust_indices: 
2018-08-08 21:13:41.682	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7554	dsts size 1, first 11404.666165530
2018-08-08 21:13:41.682	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7555	adding_fee 0, use_rct 1
2018-08-08 21:13:41.682	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7597	Picking output 250, amount 515.390000000, ki <bbc27394b7143b80cc5863a620de532b0d48cb2ebb6f5e21be4ad0ca6eeef5d2>
2018-08-08 21:13:41.682	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 3 with ring size 7 and 2: 3325 (1504 saved)
2018-08-08 21:13:41.682	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7629	We can partially pay ZYZXZgatLjtFycXKri3YpjJ3fp42XYd3UURcMJ4rBVTVhv49hiiUdEcPrRhEMUVaB1MVyQz7xuKQTUsT7HL1gHRxewvn7BaBeKg for 515.390000000/11404.666165530
2018-08-08 21:13:41.683	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7638	Considering whether to create a tx now, 3 inputs, tx limit 19400
2018-08-08 21:13:41.683	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 3 with ring size 7 and 2: 3325 (1504 saved)
2018-08-08 21:13:41.683	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7551	Start of loop with 17 0
2018-08-08 21:13:41.683	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7552	unused_transfers_indices: 194 141 316 203 226 245 260 193 150 152 292 317 286 220 157 210 204
2018-08-08 21:13:41.683	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7553	unused_dust_indices: 
2018-08-08 21:13:41.683	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7554	dsts size 1, first 10889.276165530
2018-08-08 21:13:41.683	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7555	adding_fee 0, use_rct 1
2018-08-08 21:13:41.683	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7597	Picking output 292, amount 511.040000000, ki <47ae235502064719484c271e25eb291584919a089b2f48ce5e4a44cd9c4522b0>
2018-08-08 21:13:41.683	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 4 with ring size 7 and 2: 3890 (1984 saved)
2018-08-08 21:13:41.683	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7629	We can partially pay ZYZXZgatLjtFycXKri3YpjJ3fp42XYd3UURcMJ4rBVTVhv49hiiUdEcPrRhEMUVaB1MVyQz7xuKQTUsT7HL1gHRxewvn7BaBeKg for 511.040000000/10889.276165530
2018-08-08 21:13:41.683	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7638	Considering whether to create a tx now, 4 inputs, tx limit 19400
2018-08-08 21:13:41.683	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 4 with ring size 7 and 2: 3890 (1984 saved)
2018-08-08 21:13:41.683	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7551	Start of loop with 16 0
2018-08-08 21:13:41.683	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7552	unused_transfers_indices: 194 141 316 203 226 245 260 193 150 152 204 317 286 220 157 210
2018-08-08 21:13:41.683	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7553	unused_dust_indices: 
2018-08-08 21:13:41.683	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7554	dsts size 1, first 10378.236165530
2018-08-08 21:13:41.683	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7555	adding_fee 0, use_rct 1
2018-08-08 21:13:41.683	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7597	Picking output 226, amount 513.640000000, ki <3fca608cdf7fc6d47e6ab30907f12a582218a6c1a52320e0637c1498f1889a5d>
2018-08-08 21:13:41.683	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 5 with ring size 7 and 2: 4455 (2464 saved)
2018-08-08 21:13:41.683	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7629	We can partially pay ZYZXZgatLjtFycXKri3YpjJ3fp42XYd3UURcMJ4rBVTVhv49hiiUdEcPrRhEMUVaB1MVyQz7xuKQTUsT7HL1gHRxewvn7BaBeKg for 513.640000000/10378.236165530
2018-08-08 21:13:41.683	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7638	Considering whether to create a tx now, 5 inputs, tx limit 19400
2018-08-08 21:13:41.683	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 5 with ring size 7 and 2: 4455 (2464 saved)
2018-08-08 21:13:41.683	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7551	Start of loop with 15 0
2018-08-08 21:13:41.683	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7552	unused_transfers_indices: 194 141 316 203 210 245 260 193 150 152 204 317 286 220 157
2018-08-08 21:13:41.683	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7553	unused_dust_indices: 
2018-08-08 21:13:41.683	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7554	dsts size 1, first 9864.596165530
2018-08-08 21:13:41.683	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7555	adding_fee 0, use_rct 1
2018-08-08 21:13:41.683	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7597	Picking output 157, amount 544.250000000, ki <26f588005593a3d9feb9a9df8c8e3bfe84657c610109de52ca75cffe913f4fce>
2018-08-08 21:13:41.683	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 6 with ring size 7 and 2: 5020 (2944 saved)
2018-08-08 21:13:41.683	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7629	We can partially pay ZYZXZgatLjtFycXKri3YpjJ3fp42XYd3UURcMJ4rBVTVhv49hiiUdEcPrRhEMUVaB1MVyQz7xuKQTUsT7HL1gHRxewvn7BaBeKg for 544.250000000/9864.596165530
2018-08-08 21:13:41.683	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7638	Considering whether to create a tx now, 6 inputs, tx limit 19400
2018-08-08 21:13:41.683	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 6 with ring size 7 and 2: 5020 (2944 saved)
2018-08-08 21:13:41.683	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7551	Start of loop with 14 0
2018-08-08 21:13:41.683	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7552	unused_transfers_indices: 194 141 316 203 210 245 260 193 150 152 204 317 286 220
2018-08-08 21:13:41.683	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7553	unused_dust_indices: 
2018-08-08 21:13:41.683	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7554	dsts size 1, first 9320.346165530
2018-08-08 21:13:41.683	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7555	adding_fee 0, use_rct 1
2018-08-08 21:13:41.683	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7597	Picking output 203, amount 500.300000000, ki <1205cfdf3f700fe15128984171a6d360d8e48d562b88e18644ddd1bfb8d2193a>
2018-08-08 21:13:41.684	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 7 with ring size 7 and 2: 5585 (3424 saved)
2018-08-08 21:13:41.684	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7629	We can partially pay ZYZXZgatLjtFycXKri3YpjJ3fp42XYd3UURcMJ4rBVTVhv49hiiUdEcPrRhEMUVaB1MVyQz7xuKQTUsT7HL1gHRxewvn7BaBeKg for 500.300000000/9320.346165530
2018-08-08 21:13:41.684	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7638	Considering whether to create a tx now, 7 inputs, tx limit 19400
2018-08-08 21:13:41.684	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 7 with ring size 7 and 2: 5585 (3424 saved)
2018-08-08 21:13:41.684	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7551	Start of loop with 13 0
2018-08-08 21:13:41.684	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7552	unused_transfers_indices: 194 141 316 220 210 245 260 193 150 152 204 317 286
2018-08-08 21:13:41.684	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7553	unused_dust_indices: 
2018-08-08 21:13:41.684	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7554	dsts size 1, first 8820.046165530
2018-08-08 21:13:41.684	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7555	adding_fee 0, use_rct 1
2018-08-08 21:13:41.684	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7597	Picking output 210, amount 517.930000000, ki <31274643fba3d55a7d0c217c07a21215b4f5bde86e94944eb50d61f421b38d24>
2018-08-08 21:13:41.684	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 8 with ring size 7 and 2: 6150 (3904 saved)
2018-08-08 21:13:41.684	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7629	We can partially pay ZYZXZgatLjtFycXKri3YpjJ3fp42XYd3UURcMJ4rBVTVhv49hiiUdEcPrRhEMUVaB1MVyQz7xuKQTUsT7HL1gHRxewvn7BaBeKg for 517.930000000/8820.046165530
2018-08-08 21:13:41.684	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7638	Considering whether to create a tx now, 8 inputs, tx limit 19400
2018-08-08 21:13:41.684	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 8 with ring size 7 and 2: 6150 (3904 saved)
2018-08-08 21:13:41.684	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7551	Start of loop with 12 0
2018-08-08 21:13:41.684	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7552	unused_transfers_indices: 194 141 316 220 286 245 260 193 150 152 204 317
2018-08-08 21:13:41.684	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7553	unused_dust_indices: 
2018-08-08 21:13:41.684	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7554	dsts size 1, first 8302.116165530
2018-08-08 21:13:41.684	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7555	adding_fee 0, use_rct 1
2018-08-08 21:13:41.684	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7597	Picking output 204, amount 500.510000000, ki <9aa5ede70b94583b6d6e9428bacf6b04d085e4b43f8f11c089b2a9f21b86f170>
2018-08-08 21:13:41.684	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 9 with ring size 7 and 2: 6715 (4384 saved)
2018-08-08 21:13:41.684	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7629	We can partially pay ZYZXZgatLjtFycXKri3YpjJ3fp42XYd3UURcMJ4rBVTVhv49hiiUdEcPrRhEMUVaB1MVyQz7xuKQTUsT7HL1gHRxewvn7BaBeKg for 500.510000000/8302.116165530
2018-08-08 21:13:41.684	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7638	Considering whether to create a tx now, 9 inputs, tx limit 19400
2018-08-08 21:13:41.684	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 9 with ring size 7 and 2: 6715 (4384 saved)
2018-08-08 21:13:41.684	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7551	Start of loop with 11 0
2018-08-08 21:13:41.684	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7552	unused_transfers_indices: 194 141 316 220 286 245 260 193 150 152 317
2018-08-08 21:13:41.684	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7553	unused_dust_indices: 
2018-08-08 21:13:41.684	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7554	dsts size 1, first 7801.606165530
2018-08-08 21:13:41.684	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7555	adding_fee 0, use_rct 1
2018-08-08 21:13:41.684	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7597	Picking output 286, amount 522.860000000, ki <8163fa5b37512aa00b50585b642d48d095fc789341343107c74361a1cf080c5a>
2018-08-08 21:13:41.684	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 10 with ring size 7 and 2: 7280 (4864 saved)
2018-08-08 21:13:41.684	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7629	We can partially pay ZYZXZgatLjtFycXKri3YpjJ3fp42XYd3UURcMJ4rBVTVhv49hiiUdEcPrRhEMUVaB1MVyQz7xuKQTUsT7HL1gHRxewvn7BaBeKg for 522.860000000/7801.606165530
2018-08-08 21:13:41.684	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7638	Considering whether to create a tx now, 10 inputs, tx limit 19400
2018-08-08 21:13:41.684	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 10 with ring size 7 and 2: 7280 (4864 saved)
2018-08-08 21:13:41.684	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7551	Start of loop with 10 0
2018-08-08 21:13:41.684	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7552	unused_transfers_indices: 194 141 316 220 317 245 260 193 150 152
2018-08-08 21:13:41.684	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7553	unused_dust_indices: 
2018-08-08 21:13:41.684	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7554	dsts size 1, first 7278.746165530
2018-08-08 21:13:41.684	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7555	adding_fee 0, use_rct 1
2018-08-08 21:13:41.685	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7597	Picking output 260, amount 506.600000000, ki <0715a49ff5576684dbffd2accc078d20b658b43575e49b2481df0d9e92c83c3c>
2018-08-08 21:13:41.685	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 11 with ring size 7 and 2: 7845 (5344 saved)
2018-08-08 21:13:41.685	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7629	We can partially pay ZYZXZgatLjtFycXKri3YpjJ3fp42XYd3UURcMJ4rBVTVhv49hiiUdEcPrRhEMUVaB1MVyQz7xuKQTUsT7HL1gHRxewvn7BaBeKg for 506.600000000/7278.746165530
2018-08-08 21:13:41.685	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7638	Considering whether to create a tx now, 11 inputs, tx limit 19400
2018-08-08 21:13:41.685	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 11 with ring size 7 and 2: 7845 (5344 saved)
2018-08-08 21:13:41.685	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7551	Start of loop with 9 0
2018-08-08 21:13:41.685	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7552	unused_transfers_indices: 194 141 316 220 317 245 152 193 150
2018-08-08 21:13:41.685	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7553	unused_dust_indices: 
2018-08-08 21:13:41.685	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7554	dsts size 1, first 6772.146165530
2018-08-08 21:13:41.685	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7555	adding_fee 0, use_rct 1
2018-08-08 21:13:41.685	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7597	Picking output 141, amount 513.400000000, ki <db1ccc9de79bc3406bd6f5574576b6939fbe52de08ad6fd4cb4e1e15ed3c8d94>
2018-08-08 21:13:41.685	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 12 with ring size 7 and 2: 8410 (5824 saved)
2018-08-08 21:13:41.685	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7629	We can partially pay ZYZXZgatLjtFycXKri3YpjJ3fp42XYd3UURcMJ4rBVTVhv49hiiUdEcPrRhEMUVaB1MVyQz7xuKQTUsT7HL1gHRxewvn7BaBeKg for 513.400000000/6772.146165530
2018-08-08 21:13:41.685	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7638	Considering whether to create a tx now, 12 inputs, tx limit 19400
2018-08-08 21:13:41.685	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 12 with ring size 7 and 2: 8410 (5824 saved)
2018-08-08 21:13:41.685	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7551	Start of loop with 8 0
2018-08-08 21:13:41.685	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7552	unused_transfers_indices: 194 150 316 220 317 245 152 193
2018-08-08 21:13:41.685	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7553	unused_dust_indices: 
2018-08-08 21:13:41.685	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7554	dsts size 1, first 6258.746165530
2018-08-08 21:13:41.685	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7555	adding_fee 0, use_rct 1
2018-08-08 21:13:41.685	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7597	Picking output 317, amount 262.048990560, ki <20aa67b0479a23f23677813ace555d71048ec51c00563eeb7f7ea972bdb780fa>
2018-08-08 21:13:41.685	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 13 with ring size 7 and 2: 8975 (6304 saved)
2018-08-08 21:13:41.685	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7629	We can partially pay ZYZXZgatLjtFycXKri3YpjJ3fp42XYd3UURcMJ4rBVTVhv49hiiUdEcPrRhEMUVaB1MVyQz7xuKQTUsT7HL1gHRxewvn7BaBeKg for 262.048990560/6258.746165530
2018-08-08 21:13:41.685	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7638	Considering whether to create a tx now, 13 inputs, tx limit 19400
2018-08-08 21:13:41.685	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 13 with ring size 7 and 2: 8975 (6304 saved)
2018-08-08 21:13:41.685	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7551	Start of loop with 7 0
2018-08-08 21:13:41.685	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7552	unused_transfers_indices: 194 150 316 220 193 245 152
2018-08-08 21:13:41.685	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7553	unused_dust_indices: 
2018-08-08 21:13:41.685	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7554	dsts size 1, first 5996.697174970
2018-08-08 21:13:41.685	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7555	adding_fee 0, use_rct 1
2018-08-08 21:13:41.685	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7597	Picking output 152, amount 505.390000000, ki <1b8d680ff91a37dd06c20936b9ff4fc8af990f752b2cf4b9f4892edf76157c39>
2018-08-08 21:13:41.685	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 14 with ring size 7 and 2: 9540 (6784 saved)
2018-08-08 21:13:41.685	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7629	We can partially pay ZYZXZgatLjtFycXKri3YpjJ3fp42XYd3UURcMJ4rBVTVhv49hiiUdEcPrRhEMUVaB1MVyQz7xuKQTUsT7HL1gHRxewvn7BaBeKg for 505.390000000/5996.697174970
2018-08-08 21:13:41.685	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7638	Considering whether to create a tx now, 14 inputs, tx limit 19400
2018-08-08 21:13:41.685	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 14 with ring size 7 and 2: 9540 (6784 saved)
2018-08-08 21:13:41.685	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7551	Start of loop with 6 0
2018-08-08 21:13:41.685	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7552	unused_transfers_indices: 194 150 316 220 193 245
2018-08-08 21:13:41.685	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7553	unused_dust_indices: 
2018-08-08 21:13:41.685	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7554	dsts size 1, first 5491.307174970
2018-08-08 21:13:41.685	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7555	adding_fee 0, use_rct 1
2018-08-08 21:13:41.686	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7597	Picking output 194, amount 515.470000000, ki <f694cd6a3c13113c3ddcf15a615659110ad834b0d96694da0ea4e3c48d357280>
2018-08-08 21:13:41.686	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 15 with ring size 7 and 2: 10105 (7264 saved)
2018-08-08 21:13:41.686	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7629	We can partially pay ZYZXZgatLjtFycXKri3YpjJ3fp42XYd3UURcMJ4rBVTVhv49hiiUdEcPrRhEMUVaB1MVyQz7xuKQTUsT7HL1gHRxewvn7BaBeKg for 515.470000000/5491.307174970
2018-08-08 21:13:41.686	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7638	Considering whether to create a tx now, 15 inputs, tx limit 19400
2018-08-08 21:13:41.686	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 15 with ring size 7 and 2: 10105 (7264 saved)
2018-08-08 21:13:41.686	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7551	Start of loop with 5 0
2018-08-08 21:13:41.686	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7552	unused_transfers_indices: 245 150 316 220 193
2018-08-08 21:13:41.686	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7553	unused_dust_indices: 
2018-08-08 21:13:41.686	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7554	dsts size 1, first 4975.837174970
2018-08-08 21:13:41.686	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7555	adding_fee 0, use_rct 1
2018-08-08 21:13:41.686	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7597	Picking output 245, amount 521.590000000, ki <072168aa5df67bfebde070d94b967eb4455d4c78d27cba6d508af4edd03bbab6>
2018-08-08 21:13:41.686	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 16 with ring size 7 and 2: 10670 (7744 saved)
2018-08-08 21:13:41.686	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7629	We can partially pay ZYZXZgatLjtFycXKri3YpjJ3fp42XYd3UURcMJ4rBVTVhv49hiiUdEcPrRhEMUVaB1MVyQz7xuKQTUsT7HL1gHRxewvn7BaBeKg for 521.590000000/4975.837174970
2018-08-08 21:13:41.686	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7638	Considering whether to create a tx now, 16 inputs, tx limit 19400
2018-08-08 21:13:41.686	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 16 with ring size 7 and 2: 10670 (7744 saved)
2018-08-08 21:13:41.686	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7551	Start of loop with 4 0
2018-08-08 21:13:41.686	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7552	unused_transfers_indices: 193 150 316 220
2018-08-08 21:13:41.686	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7553	unused_dust_indices: 
2018-08-08 21:13:41.686	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7554	dsts size 1, first 4454.247174970
2018-08-08 21:13:41.686	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7555	adding_fee 0, use_rct 1
2018-08-08 21:13:41.686	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7597	Picking output 150, amount 509.820000000, ki <bc38bad6eaa55cc3bb106e8274899c10463e7d3aac966e9020c38edef6ceb15c>
2018-08-08 21:13:41.686	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 17 with ring size 7 and 2: 11235 (8224 saved)
2018-08-08 21:13:41.686	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7629	We can partially pay ZYZXZgatLjtFycXKri3YpjJ3fp42XYd3UURcMJ4rBVTVhv49hiiUdEcPrRhEMUVaB1MVyQz7xuKQTUsT7HL1gHRxewvn7BaBeKg for 509.820000000/4454.247174970
2018-08-08 21:13:41.686	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7638	Considering whether to create a tx now, 17 inputs, tx limit 19400
2018-08-08 21:13:41.686	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 17 with ring size 7 and 2: 11235 (8224 saved)
2018-08-08 21:13:41.686	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7551	Start of loop with 3 0
2018-08-08 21:13:41.686	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7552	unused_transfers_indices: 193 220 316
2018-08-08 21:13:41.686	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7553	unused_dust_indices: 
2018-08-08 21:13:41.686	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7554	dsts size 1, first 3944.427174970
2018-08-08 21:13:41.686	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7555	adding_fee 0, use_rct 1
2018-08-08 21:13:41.686	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7597	Picking output 193, amount 518.600000000, ki <3968e9911901bdf0f3188569538a1678b3b8daa06af1bfafde63e4c9a4e53a94>
2018-08-08 21:13:41.686	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 18 with ring size 7 and 2: 11800 (8704 saved)
2018-08-08 21:13:41.686	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7629	We can partially pay ZYZXZgatLjtFycXKri3YpjJ3fp42XYd3UURcMJ4rBVTVhv49hiiUdEcPrRhEMUVaB1MVyQz7xuKQTUsT7HL1gHRxewvn7BaBeKg for 518.600000000/3944.427174970
2018-08-08 21:13:41.686	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7638	Considering whether to create a tx now, 18 inputs, tx limit 19400
2018-08-08 21:13:41.686	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 18 with ring size 7 and 2: 11800 (8704 saved)
2018-08-08 21:13:41.686	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7551	Start of loop with 2 0
2018-08-08 21:13:41.686	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7552	unused_transfers_indices: 316 220
2018-08-08 21:13:41.686	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7553	unused_dust_indices: 
2018-08-08 21:13:41.686	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7554	dsts size 1, first 3425.827174970
2018-08-08 21:13:41.686	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7555	adding_fee 0, use_rct 1
2018-08-08 21:13:41.687	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7597	Picking output 220, amount 516.340000000, ki <fb7594c809629c53777ef1c777e3d24d685e9f39e2446dd6e841187fbb04dfd5>
2018-08-08 21:13:41.687	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 19 with ring size 7 and 2: 12365 (9184 saved)
2018-08-08 21:13:41.687	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7629	We can partially pay ZYZXZgatLjtFycXKri3YpjJ3fp42XYd3UURcMJ4rBVTVhv49hiiUdEcPrRhEMUVaB1MVyQz7xuKQTUsT7HL1gHRxewvn7BaBeKg for 516.340000000/3425.827174970
2018-08-08 21:13:41.687	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7638	Considering whether to create a tx now, 19 inputs, tx limit 19400
2018-08-08 21:13:41.687	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 19 with ring size 7 and 2: 12365 (9184 saved)
2018-08-08 21:13:41.687	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7551	Start of loop with 1 0
2018-08-08 21:13:41.687	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7552	unused_transfers_indices: 316
2018-08-08 21:13:41.687	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7553	unused_dust_indices: 
2018-08-08 21:13:41.687	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7554	dsts size 1, first 2909.487174970
2018-08-08 21:13:41.687	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7555	adding_fee 0, use_rct 1
2018-08-08 21:13:41.687	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7597	Picking output 316, amount 409.028988800, ki <930fbaf001dc51424ceaf87e2b39e3039b2e471ead27bc400cc6a8be18c07fee>
2018-08-08 21:13:41.687	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 20 with ring size 7 and 2: 12930 (9664 saved)
2018-08-08 21:13:41.687	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7629	We can partially pay ZYZXZgatLjtFycXKri3YpjJ3fp42XYd3UURcMJ4rBVTVhv49hiiUdEcPrRhEMUVaB1MVyQz7xuKQTUsT7HL1gHRxewvn7BaBeKg for 409.028988800/2909.487174970
2018-08-08 21:13:41.687	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7638	Considering whether to create a tx now, 20 inputs, tx limit 19400
2018-08-08 21:13:41.687	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 20 with ring size 7 and 2: 12930 (9664 saved)
2018-08-08 21:13:41.687	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7551	Start of loop with 0 0
2018-08-08 21:13:41.687	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7552	unused_transfers_indices: 
2018-08-08 21:13:41.687	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7553	unused_dust_indices: 
2018-08-08 21:13:41.687	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7554	dsts size 1, first 2500.458186170
2018-08-08 21:13:41.687	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7555	adding_fee 0, use_rct 1
2018-08-08 21:13:41.687	    7f0bffa66780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7559	No more outputs to choose from
2018-08-08 21:13:41.687	    7f0bffa66780	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:7560	1. THROW EXCEPTION: error::tx_not_possible
2018-08-08 21:13:41.687	    7f0bffa66780	WARN 	net.http	src/wallet/wallet_errors.h:794	/root/mutex/src/wallet/wallet2.cpp:7560:N5tools5error15tx_not_possibleE: tx not possible, available = 75573.991813830, tx_amount = 75000.000000000, fee = 3.216042480
2018-08-08 21:13:41.687	    7f0bffa66780	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: tools::error::tx_not_possible
2018-08-08 21:13:41.687	    7f0bffa66780	INFO 	stacktrace	src/common/stack_trace.cpp:125	Unwound call stack:
2018-08-08 21:13:41.736	    7f0bffa66780	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [1] ./mutex-wallet-cli:__cxa_throw+0x10e [0x55a7e47d0b9e]
2018-08-08 21:13:41.736	    7f0bffa66780	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [2] ./mutex-wallet-cli:void tools::error::throw_wallet_ex<tools::error::tx_not_possible, unsigned long, unsigned long, unsigned long>(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&&, unsigned long const&, unsigned long const&, unsigned long const&)+0x1ef [0x55a7e46e583f]
2018-08-08 21:13:41.736	    7f0bffa66780	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [3] ./mutex-wallet-cli:tools::wallet2::create_transactions_2(std::vector<cryptonote::tx_destination_entry, std::allocator<cryptonote::tx_destination_entry> >, unsigned long, unsigned long, unsigned int, std::vector<unsigned char, std::allocator<unsigned char> > const&, unsigned int, std::set<unsigned int, std::less<unsigned int>, std::allocator<unsigned int> >, bool)+0x3629 [0x55a7e46aea59]
2018-08-08 21:13:41.736	    7f0bffa66780	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [4] ./mutex-wallet-cli:cryptonote::simple_wallet::transfer_main(int, std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&)+0x1a3e [0x55a7e456978e]
2018-08-08 21:13:41.736	    7f0bffa66780	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [5] ./mutex-wallet-cli:epee::command_handler::process_command_str(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)+0x2a5 [0x55a7e45c0145]
2018-08-08 21:13:41.736	    7f0bffa66780	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [6] ./mutex-wallet-cli:bool epee::async_console_handler::run<bool epee::async_console_handler::run<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > > >(boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > >, std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>)::{lambda(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)#1}>(std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool epee::async_console_handler::run<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > > >(boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::command_handler, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&>, boost::_bi::list2<boost::_bi::value<epee::console_handlers_binder*>, boost::arg<1> > >, std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>)::{lambda(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)#1} const&, std::function<void ()>)+0x886 [0x55a7e4597b36]
2018-08-08 21:13:41.736	    7f0bffa66780	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [7] ./mutex-wallet-cli:cryptonote::simple_wallet::run()+0x34e [0x55a7e45521de]
2018-08-08 21:13:41.736	    7f0bffa66780	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [8] ./mutex-wallet-cli:main+0x671 [0x55a7e451c781]
2018-08-08 21:13:41.736	    7f0bffa66780	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [9] /lib/x86_64-linux-gnu/libc.so.6:__libc_start_main+0xf0 [0x7f0bfca26830]
2018-08-08 21:13:41.736	    7f0bffa66780	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [10] ./mutex-wallet-cli:_start+0x29 [0x55a7e4528489]
2018-08-08 21:13:41.736	    7f0bffa66780	INFO 	stacktrace	src/common/stack_trace.cpp:163	
2018-08-08 21:13:41.756	    7f0bffa66780	WARN 	wallet.simplewallet	src/simplewallet/simplewallet.cpp:446	not enough money to transfer, available only 75573.991813830, transaction amount 75003.216042480 = 75000.000000000 + 3.216042480 (fee)
2018-08-08 21:13:41.756	    7f0bffa66780	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Failed to find a way to create transactions. This is usually due to dust which is so small it cannot pay for itself in fees, or trying to send more money than the unlocked balance, or not leaving enough for fees
2018-08-08 21:13:41.757	    7f0bf7b3e700	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:1670	Daemon is recent enough, asking for pruned blocks
2018-08-08 21:13:41.914	    7f0bf8a41700	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:1670	Daemon is recent enough, asking for pruned blocks
2018-08-08 21:13:41.914	    7f0bf7b3e700	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:1774	Block is already in blockchain: 3930ab6d9c3a4f430dc9ce83bd836a2a75189853c14b431d734c528954ba71a0
2018-08-08 21:13:41.915	    7f0bf7b3e700	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:1594	Processed block: <3bf0e13ad27c998b80f3e56d979054fdd825eedac619c7f689bdee4407017a3f>, height 157823, 0(0/0)ms
2018-08-08 21:13:41.917	    7f0bf7b3e700	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:1594	Processed block: <73ac5634cf261f470cb08fe6fd2f08a42df07df92f96d214910aaa4fa13825d1>, height 157824, 3(1/2)ms
2018-08-08 21:13:41.994	    7f0bf7b3e700	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:1887	update_pool_state start
2018-08-08 21:13:42.074	    7f0bf7b3e700	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:1898	update_pool_state got pool
2018-08-08 21:13:42.074	    7f0bf7b3e700	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:1955	update_pool_state done first loop
2018-08-08 21:13:42.074	    7f0bf7b3e700	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:1964	update_pool_state done second loop
2018-08-08 21:13:42.074	    7f0bf7b3e700	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:2101	update_pool_state end
2018-08-08 21:13:42.074	    7f0bf7b3e700	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:2333	Refresh done, blocks received: 2, balance (all accounts): 75573.991813830, unlocked: 75573.991813830
2018-08-08 21:13:53.264	    7f0bffa66780	DEBUG	wallet.wallet2	contrib/epee/include/console_handler.h:364	Read command: exit

## stoffu | 2018-08-09T03:19:16+00:00
@alexmateescu 
Most likely it's because the amount 75000 you tried to send is too high relative to the available outputs you have. The transfer needed to be split into multiple transactions, and some of your available balance would become locked as change in one of those split txes. The workaround is to simply specify some smaller amount for transfer so that the splitting won't occur.

## alexmateescu | 2018-08-09T05:43:14+00:00
ok that i understand. the issue is like this. on the pool i had the same issue and setting priority to 2 fixed the splitting and i can pay any amount no mater what the outputs are. biggest one was 230.000 coins. but with the cli wallet i can't set the priority and if i am correct the GUI does not have this option either. 

## stoffu | 2018-08-09T05:52:41+00:00
Adjusting priority is supported both in the CLI and the GUI.

## moneromooo-monero | 2018-08-30T14:59:11+00:00
No apparent bug.

+invalid


# Action History
- Created by: Cryptoxylx | 2018-08-01T12:41:36+00:00
- Closed at: 2018-08-30T15:01:09+00:00
