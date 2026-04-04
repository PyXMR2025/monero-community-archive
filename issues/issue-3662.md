---
title: XMR balance remaining zero and not showing recent deposit on GUI wallet
source_url: https://github.com/monero-project/monero-gui/issues/3662
author: RSKmain
assignees: []
labels: []
created_at: '2021-08-09T16:01:43+00:00'
updated_at: '2021-08-15T07:37:23+00:00'
type: issue
status: closed
closed_at: '2021-08-15T02:37:57+00:00'
---

# Original Description
Hi,
I’ve recently withdrawn a small amount of XMR from an exchange to my monero gui wallet (linked with Ledger) but unfortunately the balance remains zero and not acknowledging the withdrawal recently completed.
I am running a local node (prune blockchain), advanced fully synced wallet mode. I tried restoring wallet height to a day prior to my withdrawal (2401108) but the balance remains zero.
Could you help?

# Discussion History
## rating89us | 2021-08-09T16:36:17+00:00
Does the transaction appear on a block explorer? You can verify this by entering your transaction ID (txid) in a block explorer (like https://www.exploremonero.com/).

## rating89us | 2021-08-09T16:39:03+00:00
What number do you see here?
![image](https://user-images.githubusercontent.com/45968869/128741806-82a4e0cd-6235-4876-bddf-66455b3c481d.png)

And what number do you see here (Settings > Info page)?
![image](https://user-images.githubusercontent.com/45968869/128741967-5a44d289-5c3a-4ab4-9128-9bd3dfbd2df0.png)



## RSKmain | 2021-08-11T18:20:15+00:00
Hi there,

Thank you so much for your reply.

I did try to to verify the transaction as you suggested but noted that the secret key is a list of zeros.

I also noted that the daemon is fully synchronised (Synced 2424923) but the wallet is not and seems to be stuck (not even starting).

I tried to change the wallet restore height (2401108) to a day prior to my initial test transaction from the exchange but the balance remains at 0.

Update:
Daemon synchronized at 2424923 (from 2 days ago);
Wallet restore height: 2401108. 

I am running a local node on win10 x64 and my wallet is on advanced mode and linked with Ledger Nano S.

Would you be able to advise me further?

Thank you for your time and help.

Regards,
R



‐‐‐‐‐‐‐ Original Message ‐‐‐‐‐‐‐
On Monday, August 9th, 2021 at 5:36 PM, rating89us ***@***.***> wrote:

> Does the transaction appear on a block explorer? You can verify this by entering your transaction ID (txid) in a block explorer (like https://www.exploremonero.com/).
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, [view it on GitHub](https://github.com/monero-project/monero-gui/issues/3662#issuecomment-895370138), or [unsubscribe](https://github.com/notifications/unsubscribe-auth/AUVZV66HQJ452FGPIYKOH3DT377YZANCNFSM5B2KGPLQ).
> Triage notifications on the go with GitHub Mobile for [iOS](https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675) or [Android](https://play.google.com/store/apps/details?id=com.github.android&utm_campaign=notification-email).

## rating89us | 2021-08-13T12:47:48+00:00
> Hi there, Thank you so much for your reply. I did try to to verify the transaction as you suggested but noted that the secret key is a list of zeros.

You did it wrong. Please folow these steps:

1) Go to your exchange website, and search for history of transactions, withdrawal history or something similar.

2) Copy the transaction id (also known as txid, tx hash, or transaction hash) of your withdrawal transaction.

3) Paste the transaction ID in the search bar of exploremonero.com and press Enter:
![image](https://user-images.githubusercontent.com/45968869/129358554-20b5d162-d1ed-4974-ad25-85b972be7f83.png)

If you see a page with all transaction details (like the one below), the transaction was sent and the problem is that your Monero GUI wallet is not detecting it. Please inform us what number is displayed on "Block" (red circle below):
![image](https://user-images.githubusercontent.com/45968869/129359219-f7bfd077-8863-464b-b3a9-4efe03883602.png)

If you see a page with no transaction details, the problem was on your exchange wallet (transaction failed) and you should contact their support:
![image](https://user-images.githubusercontent.com/45968869/129358685-d8b0af67-b167-4465-addd-f3e2391eb297.png)

## RSKmain | 2021-08-13T18:51:06+00:00
Hi Rating89us,

Many thanks for getting back to me.
You were right - I was not using exploremonero correctly.
Using the transaction ID in the search bar, it gave the following block number: [2,422,574](https://www.exploremonero.com/block/2422574).

Hope this can help resolving the issue with the wallet.

Thank you,
R

Sent with [ProtonMail](https://protonmail.com/) Secure Email.

‐‐‐‐‐‐‐ Original Message ‐‐‐‐‐‐‐
On Friday, August 13th, 2021 at 1:47 PM, rating89us ***@***.***> wrote:

>> Hi there, Thank you so much for your reply. I did try to to verify the transaction as you suggested but noted that the secret key is a list of zeros.
>
> You did it wrong. Please folow these steps:
>
> -
>
> Go to your exchange website, and search for history of transactions, withdrawal history or something similar.
>
> -
>
> Copy the transaction id (also known as txid, tx hash, or transaction hash) of your withdrawal transaction.
>
> -
>
> Paste the transaction ID in the search bar of exploremonero.com and press Enter: [image](https://user-images.githubusercontent.com/45968869/129358554-20b5d162-d1ed-4974-ad25-85b972be7f83.png)
>
> If you see a page with all transaction details (like the one below), the transaction was sent and the problem is that your wallet is not detecting it. Please inform us what number is displayed on "Block" (red circle below): [image](https://user-images.githubusercontent.com/45968869/129359219-f7bfd077-8863-464b-b3a9-4efe03883602.png)
>
> If you see a page with no transaction details, the problem was on your exchange and you should contact their support: [image](https://user-images.githubusercontent.com/45968869/129358685-d8b0af67-b167-4465-addd-f3e2391eb297.png)
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, [view it on GitHub](https://github.com/monero-project/monero-gui/issues/3662#issuecomment-898434350), or [unsubscribe](https://github.com/notifications/unsubscribe-auth/AUVZV66W3WTIWY5Y6GXZORDT4UH75ANCNFSM5B2KGPLQ).
> Triage notifications on the go with GitHub Mobile for [iOS](https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675) or [Android](https://play.google.com/store/apps/details?id=com.github.android&utm_campaign=notification-email).

## rating89us | 2021-08-14T03:13:37+00:00
Ok, so the issue seems to be on your wallet.

Did you allow Ledger to export the private view key to you computer when asked?

On the lower left corner, are both orange bars (daemon and wallet) synchronized?

## RSKmain | 2021-08-14T11:43:04+00:00
Hi,

Everytime I open the wallet, I decline for the keys to be exported to the computer - The link with instructions that I used to connect the GUI wallet with Ledger suggested not to allow the keys to be exported.

Only the daemon is fully synchronised. The wallet synchronisation bar remains empty/no orange colour at all.

Thank you and hope to hear from you soon.

Sent with [ProtonMail](https://protonmail.com/) Secure Email.

‐‐‐‐‐‐‐ Original Message ‐‐‐‐‐‐‐
On Saturday, August 14th, 2021 at 4:13 AM, rating89us ***@***.***> wrote:

> Ok, so the issue seems to be on your wallet.
>
> Did you allow Ledger to export the private view key to you computer when asked?
>
> On the lower left corner, are both orange bars (daemon and wallet) synchronized?
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, [view it on GitHub](https://github.com/monero-project/monero-gui/issues/3662#issuecomment-898807675), or [unsubscribe](https://github.com/notifications/unsubscribe-auth/AUVZV62XB2SUANY6PD7SVMTT4XNOZANCNFSM5B2KGPLQ).
> Triage notifications on the go with GitHub Mobile for [iOS](https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675) or [Android](https://play.google.com/store/apps/details?id=com.github.android&utm_campaign=notification-email).

## rating89us | 2021-08-14T13:16:02+00:00
> Everytime I open the wallet, I decline for the keys to be exported to the computer 

This is your problem. You should always allow your Ledger to export the private view key to your computer, otherwise it will not work (in some cases it will work, but really slow).

It's safe to export the private view key to your computer, since it only allows Monero GUI to see the incoming transactions. You are not exporting the seed or the private spend key, therefore your computer won't be able to spend the funds without a connected Ledger.

Read this paragraph in Monero GUI guide which comes with Monero GUI:
![image](https://user-images.githubusercontent.com/45968869/129447344-5dbbda1a-9da0-4cc5-b483-fc04736a699b.png)

We will contact Ledger so they can update the instructions on their website. Some users are reporting that they are afraid of allowing the exporting of the private view key because they've read those instructions on Ledger website.

## selsta | 2021-08-15T02:37:57+00:00
Closing at is seems a user error (declining view key). I will reopen if the issue continues to persist.

## RSKmain | 2021-08-15T07:37:22+00:00
Thank you for the support!
Wallet is now synced, balance is now correct and wallet is working perfectly!

Sent with [ProtonMail](https://protonmail.com/) Secure Email.

‐‐‐‐‐‐‐ Original Message ‐‐‐‐‐‐‐
On Saturday, August 14th, 2021 at 2:16 PM, rating89us ***@***.***> wrote:

>> Everytime I open the wallet, I decline for the keys to be exported to the computer
>
> This is your problem. You should always allow your Ledger to export the private view key to your computer, otherwise it will not work (in some cases it will work, but really slow).
>
> It's safe to export the private view key to your computer, since it only allows Monero GUI to see the incoming transactions. You are not exporting the seed or the private spend key, therefore your computer won't be able to spend the funds without a connected Ledger.
>
> Read this paragraph in Monero GUI guide which comes with Monero GUI:
> [image](https://user-images.githubusercontent.com/45968869/129447344-5dbbda1a-9da0-4cc5-b483-fc04736a699b.png)
>
> We will contact Ledger so they can update the instructions on their website. Some users are reporting that they are afraid of allowing the exporting of the private view key because they've read those instructions on Ledger website.
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, [view it on GitHub](https://github.com/monero-project/monero-gui/issues/3662#issuecomment-898893459), or [unsubscribe](https://github.com/notifications/unsubscribe-auth/AUVZV6ZZTGVL3ZDPPNWOK6DT4ZUB3ANCNFSM5B2KGPLQ).
> Triage notifications on the go with GitHub Mobile for [iOS](https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675) or [Android](https://play.google.com/store/apps/details?id=com.github.android&utm_campaign=notification-email).

# Action History
- Created by: RSKmain | 2021-08-09T16:01:43+00:00
- Closed at: 2021-08-15T02:37:57+00:00
