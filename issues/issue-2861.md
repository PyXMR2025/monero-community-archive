---
title: I compiled my wallet address into XMRig, is there a way to restore the wallet
  address?
source_url: https://github.com/xmrig/xmrig/issues/2861
author: kgggggb
assignees: []
labels: []
created_at: '2022-01-11T17:17:02+00:00'
updated_at: '2022-01-31T07:56:43+00:00'
type: issue
status: closed
closed_at: '2022-01-31T07:55:43+00:00'
---

# Original Description
I compiled my wallet address into XMRig, is there a way to restore the wallet address?

# Discussion History
## Spudz76 | 2022-01-11T18:22:49+00:00
you could try `strings` command on the xmrig excecutable, if it's in there as plaintext (I think it is).

`strings xmrig | grep user`

## kgggggb | 2022-01-11T22:51:22+00:00
> you could try `strings` command on the xmrig excecutable, if it's in there as plaintext (I think it is).
> 
> 
> 
> `strings xmrig | grep user`

What if it runs in the Windows？

## Spudz76 | 2022-01-11T22:59:01+00:00
Essentially, one of the techniques [from this thread then](https://superuser.com/questions/124081/is-there-a-windows-equivalent-of-the-unix-strings-command)

I already have cygwin64 installed which includes the same `strings` command from UNIX.  But one of the other methods are a lighter download (and in case the embedded config got encoded up to Unicode the Sysinternals Strings tool may work better).

## kgggggb | 2022-01-23T11:17:55+00:00
> Essentially, one of the techniques [from this thread then](https://superuser.com/questions/124081/is-there-a-windows-equivalent-of-the-unix-strings-command)
> 
> I already have cygwin64 installed which includes the same `strings` command from UNIX. But one of the other methods are a lighter download (and in case the embedded config got encoded up to Unicode the Sysinternals Strings tool may work better).

yeah, it didn't quite work out, showing bunch of craps.
![aaaaaaaaaaaaaaaaaaaaaa](https://user-images.githubusercontent.com/47137779/150675821-43e30285-1178-4e2b-bf1b-cba15c073a54.png)



## koitsu | 2022-01-31T04:59:18+00:00
> yeah, it didn't quite work out, showing bunch of craps.

Try doing `strings64.exe -a xmrig.exe > %USERPROFILE%\Desktop\results.txt`.  The `-a` flag means only match against ASCII strings (default is both ASCII and Unicode, and public wallet addresses are always within ASCII byte range).  You will end up with a file called `results.txt` on your desktop.  Now open that file in Notepad and manually go through every single line to try and find something that resembles an address.  There will be a "bunch of craps" in there, but that's just how it works.  You have to do this analysis process by hand; there is no foolproof quick way to find what you want.

However, if you know what coin you were mining, you might be able to use `findstr /B "D"` in combination with the above to narrow down the search.  For example, Dogecoin public wallet addresses tend to start with `D`, so `findstr /B "D"` would get you only lines that start with the letter `D`.  See `findstr /?` for help/usage, as there are other flags (including `/R`) that could help you.  If you aren't familiar with CLIs and using pipes, this is what you'd do:

> `strings64.exe -a xmrig.exe | findstr /B "D" > %USERPROFILE%\Desktop\results.txt`

It all depends on the coin and if you can remember anything at all about your address; for example, if you knew it had the letters (in sequential order) "c3a" in it, you could do `strings64.exe -a xmrig.exe | findstr /I "c3a"` and see what you get.

You could alternately upload `results.txt` to someplace like [pastebin.com](https://pastebin.com/) and provide a link to the results here, and someone else could try sifting through it for you.

## kgggggb | 2022-01-31T07:55:32+00:00
> > yeah, it didn't quite work out, showing bunch of craps.
> 
> Try doing `strings64.exe -a xmrig.exe > %USERPROFILE%\Desktop\results.txt`. The `-a` flag means only match against ASCII strings (default is both ASCII and Unicode, and public wallet addresses are always within ASCII byte range). You will end up with a file called `results.txt` on your desktop. Now open that file in Notepad and manually go through every single line to try and find something that resembles an address. There will be a "bunch of craps" in there, but that's just how it works. You have to do this analysis process by hand; there is no foolproof quick way to find what you want.
> 
> However, if you know what coin you were mining, you might be able to use `findstr /B "D"` in combination with the above to narrow down the search. For example, Dogecoin public wallet addresses tend to start with `D`, so `findstr /B "D"` would get you only lines that start with the letter `D`. See `findstr /?` for help/usage, as there are other flags (including `/R`) that could help you. If you aren't familiar with CLIs and using pipes, this is what you'd do:
> 
> > `strings64.exe -a xmrig.exe | findstr /B "D" > %USERPROFILE%\Desktop\results.txt`
> 
> It all depends on the coin and if you can remember anything at all about your address; for example, if you knew it had the letters (in sequential order) "c3a" in it, you could do `strings64.exe -a xmrig.exe | findstr /I "c3a"` and see what you get.
> 
> You could alternately upload `results.txt` to someplace like [pastebin.com](https://pastebin.com/) and provide a link to the results here, and someone else could try sifting through it for you.

I removed findstr because I don't know what it included, then I used Notepad++ to find the pool address and found it was there! around line 165389, thanks for your help! Hope ya all have a nice day!
![Snipaste_2022-01-31_15-51-18](https://user-images.githubusercontent.com/47137779/151757282-fd5a9221-cca4-44ed-8ebb-036503472c66.png)



# Action History
- Created by: kgggggb | 2022-01-11T17:17:02+00:00
- Closed at: 2022-01-31T07:55:43+00:00
