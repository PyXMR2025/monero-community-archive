---
title: 'Question:  I''m about to look into removing the code bits that are adding
  Windows Registry keys.  Anything else I should be aware of?'
source_url: https://github.com/xmrig/xmrig/issues/2456
author: Entreprenerdz
assignees: []
labels: []
created_at: '2021-06-25T19:15:08+00:00'
updated_at: '2021-06-29T19:12:01+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
As the title states, I'm about to dig into the code and see about removing any and all traces of registry key modifications.  My reason for doing so is they are causing TrendMicro to flag xmrig.exe as a virus.  There are other reasons I'm sure, but these are the tangible ones that I think I can handle while getting comfortable with the code.

I know there's one in there that is something to the effect of DoNotUpdate and it may be the same one but it's No SP3, which I believe is referencing Windows XP???? So that one should be able to go for sure.

So I'm hoping that anyone that reads this may be able to add any of the following questions:

1.  Are there any registry modifications for Windows that NEED to be in there for it to run properly?
2. Are there any other reg keys that need to be removed?
3. Has anyone attempted to clean XMRig up in the past in order for it to not trigger virus scanners?
4. Any other history that you feel I should know about.

That's it!  Thanks for your time and effort in checking this post out.  I'm hoping to get this done ASAP and will do a pull request if I have any success!

# Discussion History
## SChernykh | 2021-06-25T19:22:35+00:00
XMRig doesn't use Windows registry.

## Lonnegan | 2021-06-26T00:08:20+00:00
> XMRig doesn't use Windows registry.

Sure? Right click "run as administrator" at the first start to activate huge pages doesn't write into the registry?

## Spudz76 | 2021-06-26T01:04:29+00:00
> activate huge pages doesn't write into the registry?


Nope, it uses LSA subsystem to change permissions.  Which might write to registry somewhere else but there are no direct registry accesses at all anywhere in the code.
```
static BOOL ObtainLockPagesPrivilege() {
    HANDLE token;
    PTOKEN_USER user = nullptr;

    if (OpenProcessToken(GetCurrentProcess(), TOKEN_QUERY, &token)) {
        DWORD size = 0;

        GetTokenInformation(token, TokenUser, nullptr, 0, &size);
        if (size) {
            user = (PTOKEN_USER) LocalAlloc(LPTR, size);
        }

        GetTokenInformation(token, TokenUser, user, size, &size);
        CloseHandle(token);
    }

    if (!user) {
        return FALSE;
    }

    LSA_HANDLE handle;
    LSA_OBJECT_ATTRIBUTES attributes;
    ZeroMemory(&attributes, sizeof(attributes));

    BOOL result = FALSE;
    if (LsaOpenPolicy(nullptr, &attributes, POLICY_ALL_ACCESS, &handle) == 0) {
        LSA_UNICODE_STRING str = StringToLsaUnicodeString(_T(SE_LOCK_MEMORY_NAME));

        if (LsaAddAccountRights(handle, user->User.Sid, &str, 1) == 0) {
            LOG_NOTICE("Huge pages support was successfully enabled, but reboot required to use it");
            result = TRUE;
        }

        LsaClose(handle);
    }   

    LocalFree(user);
    return result;
}
```

## Spudz76 | 2021-06-26T01:10:45+00:00
1. No it doesn't do any, already
2. There are no reg keys, only calls to LSA security subsystem
3. Impossible since they are triggering on the actual mining kernels heuristically.  Guess you could strip all the mining kernels and it would be safe from virus scanners (but also no longer a miner...).  UPX and friends don't help since Windows inspects the heuristics after it's unpacked into memory (thus identifiable).
4. Botnets used to be a larger issue when the algorithm didn't require 3GB and a bunch of other stuff which worms would find trouble finding (unallocated) in exposed targets anyway.  When it was all cache and no real system memory load, botnets were lucrative and most of the hashrate for Monero.

## SChernykh | 2021-06-26T07:45:12+00:00
> Sure? Right click "run as administrator" at the first start to activate huge pages doesn't write into the registry?

Sure. It's not windows registry, these settings are stored in the Windows Security Database at `%windir%\security\database\secedit.sdb`

## garrylachman | 2021-06-29T19:12:01+00:00
Few years ago i got some success cleaning xmrig to avoid the AntiVirusus bus its endless race, its take few days until more & more antivirus found it.
What I done?
1. Obfuscation of all string (all  strings) with a key that changed on every compile (example: https://github.com/andrivet/ADVobfuscator)
2. Change all functions name, namespaces and variables that contains xmrig, xmr, monero, cryptonight and etc...
3. Remove all metadata from the exe include the icon.
4. Check if the exe runs in VM, sandbox or got parent process - if true - exit.
5. Check for debuggers (example: https://github.com/ThomasThelen/Anti-Debugging)
6. remove any stdout output.
7. delay the startup with random intervals.
8. don't use tools like UPX - you will be flagged only for using this.
9. done few experiments with virtualization tools - I remember that I got some success with tools like boxedapp, enigmaprotector.com, vmpsoft.com.
10. Indirect call to suspicious functions (like the workers, jobs, hashing etc...) example: https://github.com/andrivet/ADVobfuscator/blob/master/Examples/ObfuscatedCalls/main.cpp
11. Libs that add junk code, example: http://www.sourceformat.com/code-obfuscator-cpp.htm
12. Remove compiler optimizations - we don't want to remove unnecessary code, we don't want a clean app.

I don't know what I feel about this, 1 thing for sure - DON'T USE THIS OR OTHER RESOURCES TO CREATE ILLEGAL MALWARES. Do your experiments for education only !!!!

# Action History
- Created by: Entreprenerdz | 2021-06-25T19:15:08+00:00
