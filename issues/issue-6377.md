---
title: Download of new version 0.15.0.4-Carbon Chamaeleon
source_url: https://github.com/monero-project/monero/issues/6377
author: Fenix2013
assignees: []
labels: []
created_at: '2020-03-08T11:08:47+00:00'
updated_at: '2020-11-17T23:59:11+00:00'
type: issue
status: closed
closed_at: '2020-11-17T23:59:11+00:00'
---

# Original Description
Yesterday I downloaded, verified the signature, hashes and binary codes and then installed the latest version of Monero GUI Wallet 0.15.0.4-Carbon Chamaeleon(I use Windows 10 Home version 1909 and I installed the version monero-gui-install-win-x64-v0.15.0.4.exe).But after successful installation, I can't run the application, it doesn't work, I can't open it. I checked all files, everything is fine installed (e.g. monerod, monero-daemon, etc.), I also checked my antivirus program to see if it accidentally blocked something (firewall, quarantine, virus chest, etc.), but everything is fine, but I still can't open the wallet and it doesn't **work.** Previously, I was using version 0.15.0.2-Carbon Chamaeleon and it worked normally with no problems with it (I use it at a local node). I tried to reinstall it and it works fine, but when I reinstall 0.15.0.4, it doesn't work again. Please, can anyone tell me where or what is the problem?
Thank you

# Discussion History
## selsta | 2020-03-08T12:39:09+00:00
What happens when you open it? Can you open monerod.exe?

There are no other reports with problems on Windows yet so I would guess anti virus blocking the program.

## Fenix2013 | 2020-03-08T16:31:03+00:00
Hellow,
when I open my wallet, a small popup wallet window appears for a moment in
the taskbar (photo n°1), but it doesn't open and disappears immediately
(sometimes a large black popup window appears on the desktop that also
disappears immediately - photo n°2).
I can open monerod without any problem(photo n°3).

Like I said before,I checked all files and everything is fine
installed(photo n°4).I also checked my antivirus program(firewall,virus
chest,quarantine,etc. - photos n°5,n°6 and n°7,),but despite of this I
can't open my Monero GUI Wallet version 0.15.0.4-Carbon Chamaeleon.

I wondered if it happened to be related to the latest KB4535996 Windows 10
update, because there were a lot of articles in the press about users'
problems with it...🙄
https://www.forbes.com/sites/gordonkelly/2020/03/07/microsoft-windows-10-warning-crashes-boot-audio-slowdown-problems-upgrade-windows-10-free/


## Fenix2013 | 2020-03-08T16:31:08+00:00
When I open my wallet, a small popup wallet window appears for a moment in the taskbar (photo n°1), but it doesn't open and disappears immediately (sometimes a large black popup window appears on the desktop that also disappears immediately - photo n°2).
I can open monerod without any problem(photo n°3).

Like I said before,I checked all files and everything is fine installed(photo n°4).I also checked my antivirus program(firewall,virus chest,quarantine,etc. - photos n°5,n°6 and n°7,),but despite of this I can't open my Monero GUI Wallet version 0.15.0.4-Carbon Chamaeleon.

At last,I repeat,when I reinstall 0.15.0.2, it works without any problems.
I wondered if it happened to be related to the latest KB4535996 Windows 10 update, because there were a lot of articles in the press about users' problems with it...🙄
[https://www.forbes.com/sites/gordonkelly/2020/03/07/microsoft-windows-10-warning-crashes-boot-audio-slowdown-problems-upgrade-windows-10-free/](url)

![20200308_143841](https://user-images.githubusercontent.com/57800986/76166790-7fad3080-6161-11ea-9a6f-6a9a98c819a2.jpg)

![Snímka obrazovky (77)](https://user-images.githubusercontent.com/57800986/76166828-e7fc1200-6161-11ea-97fc-423476d76f91.png)

![Snímka obrazovky (78)](https://user-images.githubusercontent.com/57800986/76166842-fba77880-6161-11ea-90ed-c79ed3782a60.png)

![Snímka obrazovky (74)](https://user-images.githubusercontent.com/57800986/76166853-10840c00-6162-11ea-91c4-b26cec025e8c.png)

![Komentár 2020-03-08 145925](https://user-images.githubusercontent.com/57800986/76166863-43c69b00-6162-11ea-9a8d-32decf3f1fa2.jpg)

![Komentár 2020-03-08 142326](https://user-images.githubusercontent.com/57800986/76166875-59d45b80-6162-11ea-8f30-19e7eb20fbd0.jpg)

![Snímka obrazovky (75)](https://user-images.githubusercontent.com/57800986/76166893-796b8400-6162-11ea-8dc2-5080aad439c3.png)






## selsta | 2020-03-08T16:52:17+00:00
Can you try to following:

- Temporarily disable Avast Premium Security and Windows Defender.
- Try to open the GUI.
- If it does not work, open try double clicking `start-low-graphics-mode`. 

## Fenix2013 | 2020-03-08T16:59:59+00:00
I made it,it was first what I did(I disabled Avast Premium Security and
Windows Defender,but it doesn't work).I think about uninstalled the latest
Windows 10 Update and try it again.

Dňa ne 8. 3. 2020, 17:52 selsta <notifications@github.com> napísal(a):

> Can you try to following:
>
>    - Temporarily disable Avast Premium Security and Windows Defender.
>    - Try to open the GUI.
>    - If it does not work, open try double clicking start-low-graphics-mode
>    .
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/6377?email_source=notifications&email_token=ANY7SGSAQM2UOKLVO4DOAFDRGPEMDA5CNFSM4LDYO5AKYY3PNVWWK3TUL52HS4DFVREXG43VMVBW63LNMVXHJKTDN5WW2ZLOORPWSZGOEOE3AMQ#issuecomment-596226098>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ANY7SGS444XASVGWUTVGCL3RGPEMDANCNFSM4LDYO5AA>
> .
>


## selsta | 2020-03-08T17:06:01+00:00
So `start-low-graphics-mode` also does not work? I would wait a day or so before uninstalling the update, maybe someone else has a different idea.

## Fenix2013 | 2020-03-08T20:59:31+00:00
I start it in low-graphics-mode(I open start-low-graphics-mode - Photo n°1)
and at last the wallet works(Photo n°2).

Thank you for your help and assistance.

ne 8. 3. 2020 o 18:06 selsta <notifications@github.com> napísal(a):

> So start-low-graphics-mode also does not work? I would wait a day or so
> before uninstalling the update, maybe someone else has a different idea.
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/6377?email_source=notifications&email_token=ANY7SGUNITUVSUL2VEOQDQDRGPF7TA5CNFSM4LDYO5AKYY3PNVWWK3TUL52HS4DFVREXG43VMVBW63LNMVXHJKTDN5WW2ZLOORPWSZGOEOE3LRA#issuecomment-596227524>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ANY7SGQ6NNARFIYRMX3FR2TRGPF7TANCNFSM4LDYO5AA>
> .
>


## Fenix2013 | 2020-03-08T21:07:47+00:00
![Komentár 2020-03-08 192527](https://user-images.githubusercontent.com/57800986/76171215-13debe00-6189-11ea-904f-5d0c94a0bb34.jpg)

![Snímka obrazovky (83)](https://user-images.githubusercontent.com/57800986/76171236-37096d80-6189-11ea-8796-2991bcb5830b.png)


## selsta | 2020-03-08T21:08:54+00:00
Are you graphics drivers properly installed?

## Fenix2013 | 2020-03-08T22:18:13+00:00
Yes,they are.

ne 8. 3. 2020 o 22:08 selsta <notifications@github.com> napísal(a):

> Are you graphics drivers properly installed?
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/6377?email_source=notifications&email_token=ANY7SGWQGXO4MDHZBFTFKKTRGQCONA5CNFSM4LDYO5AKYY3PNVWWK3TUL52HS4DFVREXG43VMVBW63LNMVXHJKTDN5WW2ZLOORPWSZGOEOFBSBI#issuecomment-596252933>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ANY7SGSL4PYR7UFOYXIHMBTRGQCONANCNFSM4LDYO5AA>
> .
>


# Action History
- Created by: Fenix2013 | 2020-03-08T11:08:47+00:00
- Closed at: 2020-11-17T23:59:11+00:00
