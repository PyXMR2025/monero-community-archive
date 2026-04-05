---
title: Run xmrig automatically at startup, using register
source_url: https://github.com/xmrig/xmrig/issues/293
author: Zelecktor
assignees: []
labels: []
created_at: '2017-12-25T00:22:50+00:00'
updated_at: '2018-11-05T07:05:06+00:00'
type: issue
status: closed
closed_at: '2018-11-05T07:05:06+00:00'
---

# Original Description
On windows 7
In simple words i want to make xmrig run automatically when i turn on my computer. (on this case, the computer is conected to internet, but no users logged in, just in the stand by windows, obviusly in background).

Also i want to make an easy and fast setup install, for example to leave the files in C:/program files/any folder but also in the install setup do it to run automatically when i turn on my computer (as a windows service)

# Discussion History
## ManOfFlash | 2018-01-01T16:18:13+00:00
I use standard windows task scheduler for that. Program windows not shown by this way. Because of low priority of mining process i need manually stop it only when going to play 3D game.

## Gill1000 | 2018-01-07T05:46:29+00:00
I m too finding this out...have you guys sort out this ..?? @zelecktor 
 @manOfFlash   ...i was thinking can we put  AUTO STARTUP CODE  available on net in xmrig.cpp ..i hope you get my point!!

## Zelecktor | 2018-01-08T01:26:22+00:00
I made an install setup to make a register but not always works.
I want to make something similar as the software minergate, that allows to include the software as "System PATH" and works everytime the machine starts up.

## merkjinx | 2018-01-24T03:16:16+00:00
copy bat/xmrig.exe into startup folder.
find it in run: shell:startup
also see https://github.com/xmrig/xmrig/issues/286

## Zelecktor | 2018-01-24T03:28:54+00:00
@merkjinx
Your method doesnt work on standby. An user needs to login to make it work and it doesnt what i want. 

Already im using the register route.
HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Run

And works perfectly.

## Gill1000 | 2018-01-24T12:33:14+00:00
Bro,
@Zelecktor or plz share how you successfully start xmrig on statup by registry..step by step will be appreciated:)

## Zelecktor | 2018-02-02T16:22:49+00:00
Main register to startup with the machine in stand by (no users log in)

`HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Run`

Extra register, an user must to log in to run the software
As admin user, use this
`HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`

As normal user use this (need specify)
`HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`


Name of the register = you can put wherever you want, ex. `test`
type of register = `REG_SZ`
Value = route of the file, ex. `"C:\program files\file folder lalala\xmrig.exe"` (dont forget use "")

## Gill1000 | 2018-02-02T16:50:21+00:00
Thanks :) and I m not making any  virus..I m tired of double clicking xmrig.exe everyday!! So i want to do something new!! @Zelecktor 

## sergneo | 2018-02-02T17:41:05+00:00
I use xmrig installed as a service using nssm ( http://nssm.cc/download ) . It is very easy to use program.

## Zelecktor | 2018-02-04T06:56:32+00:00
@Gill1000

found what you want, just add an option to run that script. maybe @xmrig can make a pull request and comit this feature at the main source code.
Im not expert on visual basics but maybe we can rewrite on C++. hope we dont need an external dependency

```
    Public Sub StartWithWindows()

        Dim regKey As Microsoft.Win32.RegistryKey
        Dim KeyName As String = "XmrigName"
        Dim KeyValue As String = System.Windows.Forms.Application.StartupPath & "\xmrig.exe"
        regKey = Microsoft.Win32.Registry.CurrentUser.OpenSubKey("Software\Microsoft\Windows\CurrentVersion\Run", True)
        If start_with_windows = True Then
            'create key if it doesn't already exist
            If regKey.GetValue(KeyName) = Nothing Then
                regKey.SetValue(KeyName, KeyValue, Microsoft.Win32.RegistryValueKind.String)
            End If
        Else
            'Delete key if it exists
            If Not regKey.GetValue(KeyName) = Nothing Then
                regKey.DeleteValue(KeyName, False)
            End If
        End If

    End Sub
```

## merkjinx | 2018-02-04T07:05:24+00:00
@Zelecktor 
you could make a setup wizard that guides you through the process of setting up a miner. have an option to run automatically on startup. adding it to the source seems a little much.

## Zelecktor | 2018-02-04T18:22:10+00:00
@merkjinx
Yes I use an install setup wizard to add those register (to make more easy) see on top

> I made an install set up

But what @Gill1000 wants is to add them to the source code, which is possible and we can use other miners source code that got this feature (there are lots of them)

# Action History
- Created by: Zelecktor | 2017-12-25T00:22:50+00:00
- Closed at: 2018-11-05T07:05:06+00:00
