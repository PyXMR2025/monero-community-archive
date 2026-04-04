---
title: why CLI cannot  display Chinese character for me
source_url: https://github.com/monero-project/monero/issues/6738
author: ghost
assignees: []
labels: []
created_at: '2020-08-02T12:19:10+00:00'
updated_at: '2021-08-15T03:54:51+00:00'
type: issue
status: closed
closed_at: '2021-08-15T03:54:51+00:00'
---

# Original Description
HI:
I use simplified Chinese OS(Windows 10),  I have a wallet is create by GUI use Chinese seed.   I open it on CLI and  type in “seed” command but  no seed display?
  
![ssssss](https://user-images.githubusercontent.com/69109612/89123052-05f65480-d4ff-11ea-9bc0-02568a9d6ba0.jpg)
 
and   create wallet on CLI  will be messy code and looks like The output is interrupted:
![image](https://user-images.githubusercontent.com/69109612/89122658-8f0b8c80-d4fb-11ea-9bd6-7fc2e5c81bc6.png)

Ps.   I tested it on two PC  the same problem . i try runing others console program Chinese characters are normal， so i dont konw  what is wrong?

sorry for poor english!




# Discussion History
## moneromooo-monero | 2020-08-02T12:45:23+00:00
monero-wallet-cli outputs in UTF-8. IIRC Windows uses a little endian variant of UCS-2. A patch was recently made to display UTF-8 on Windows (https://github.com/monero-project/monero/pull/6488), a similar thing needs to be done for seed display.

## iDunk5400 | 2020-08-02T12:45:42+00:00
There is not proper support for UTF-8 in Monero CLI apps on Windows currently. There was an opportunity to fix this in #6488, but then other things broke (having to do with #3313, IIRC), so the PR was modified to only do what it said in the title.

I think English is the only reliable seed language on Windows.

## ghost | 2020-08-02T12:51:37+00:00
thank you , got it.

## moneromooo-monero | 2020-08-02T13:00:03+00:00
The code seems safe wrt filesystem. It'd be interesting to try the latest QR code mode changing code now. Might work as is.

## iDunk5400 | 2020-08-02T13:10:08+00:00
`c24095d` was the commit version that fixed everything, including seeds, except it broke paths/filenames with wide characters when loading wallet files.

## moneromooo-monero | 2020-08-02T13:37:24+00:00
Ah, and IIRC using cout leaves traces of the printed data in memory, so switching to the PRINT_UTF8 macro isn't so great. Guess we'd need someone to check whether sending partial multibyte UTF-8 characters via putchar works, once WTEXTON is called :)

## moneromooo-monero | 2020-08-02T14:14:47+00:00
```
#include <stdio.h>

#ifdef _WIN32
#include <windows.h>
#define PRINT_UTF8(pre, x) std::wcout << pre ## x
#define WTEXTON() _setmode(_fileno(stdout), _O_WTEXT)
#define WTEXTOFF() _setmode(_fileno(stdout), _O_TEXT)
#else
#define PRINT_UTF8(pre, x) std::cout << x
#define WTEXTON()
#define WTEXTOFF()
#endif

int main()
{
  WTEXTON();
  putchar(0x4d);
  putchar(0x0a);
  putchar(0xe2);
  putchar(0x96);
  putchar(0x88);
  putchar(0x0a);
  puts("\u2588");
  putchar(0x0a);
  WTEXTOFF();
  return 0;
}
```

What does this print on Windows ?

## moneromooo-monero | 2020-08-02T14:17:47+00:00
Bonus points if you pipe it through some hexadecimal dumper like xxd :)

## apertamono | 2020-09-09T11:18:21+00:00
As a Windows user, I open WSL whenever I need to compile something. I installed Visual Studio to test this in a native Windows compiler. I did manage to build something, but couldn't run it successfully. Maybe this build warning gives a clue:

> warning C4566: character represented by universal-character-name '\u2588' cannot be represented in the current code page (1252)

There were no warnings for other characters. If anyone else wants to try this, you'll need to include more dependencies to use _setmode:

```
#include <io.h>
#include <stdlib.h>
```

## selsta | 2020-09-17T17:10:04+00:00
Which QR code scanner are you using? Mine was recognized with various wallets and scanners.

Edit: The comment I replied to was deleted.

## ghost | 2020-09-17T17:19:23+00:00
> Which QR code scanner are you using? Mine was recognized with various wallets and scanners.

I delete this comment，because I test it on wechat and some browser's scanner  is not recognizes ,but Alipay can be recognizes

edit: for clarity, I am on debian 10 and cli-wallet v0.17
test QR:

![jt](https://user-images.githubusercontent.com/69109612/93505957-257dfb00-f94e-11ea-803d-6b370e61f3eb.png)


## selsta | 2021-08-15T03:54:50+00:00
Issue seems resolved.

# Action History
- Created by: ghost | 2020-08-02T12:19:10+00:00
- Closed at: 2021-08-15T03:54:51+00:00
