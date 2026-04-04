---
title: Password specification through environment variable?
source_url: https://github.com/monero-project/monero/issues/5790
author: reardenlife
assignees: []
labels: []
created_at: '2019-08-02T14:21:34+00:00'
updated_at: '2019-08-03T13:48:06+00:00'
type: issue
status: closed
closed_at: '2019-08-03T13:48:06+00:00'
---

# Original Description
There seem to be only two options how the password can be specified:

```bash
$ monero-v0.14.1.2]# ./monero-wallet-rpc --help | grep pass
  --password arg                        Wallet password (escape/quote as
  --password-file arg                   Wallet password file
```

Yet there are problems with it:
1.) it would be unsecure to specify it as an argument, since it would be visible for all users of the server.  
2.) it would be unsecure to keep it in file, since if anyone will get an access to hdd of the server, he will get access to the password (which kept as a plaintext, I assume?)

So it would be great to specify in the command line something like name of the environmental variable from which rpc-wallet can read the password.  This way I will be able to keep the password only in RAM and not in the output of ps -aux.

# Discussion History
## vtnerd | 2019-08-02T16:56:13+00:00
See `--config-file` option which can load any argument directly from file. This will prevent it from showing with `ps -aux` but will store the password on disk. Preventing storage on disk will likely require the interactive mode, unless you've got some specialized scripting. In that case I think you can get the script to work with `stdin` but I haven't tested this in a while.

## vtnerd | 2019-08-02T16:59:09+00:00
And FWIW, environment variables can be read by `root` in `/proc/` but presumably this type of attack is beyond most threat models.

## reardenlife | 2019-08-03T02:04:58+00:00
Hm... well, alternatively, one can create a ramdisk and keep the file with password there.  I would assume that this is exacrly what developers of monero-wallet had in mind when they introduced --password-file option.

@vtnerd 
> "And FWIW, environment variables can be read by root in /proc/ but presumably this type of attack is beyond most threat models."

I am more worried about the scenario when the attacker has a physical access to the server.  Like in the various scenarios when authorities are confiscating the server and then hijacking the onipn domains, because the private keys where kept as a plaintext on the hdd. :)
So the files in /proc as far as I know, are virtual.  It should be safe to keep the passwords there.

## reardenlife | 2019-08-03T03:02:06+00:00
So the temporary solution is to create ramdisk then.

```bash
mkdir -p /tmp/ramdisk
chmod 700 /tmp/ramdisk
```

And this one goes to /etc/fstab:
```text
none    /tmp/ramdisk      tmpfs   rw,mode=0700,size=4M    0       0
```
Then
```bash
mount -a
```

I am not sure if one have to specify the mode into fstab or it just picks it up from the folder itself.

## vtnerd | 2019-08-03T04:21:01+00:00
> Hm... well, alternatively, one can create a ramdisk and keep the file with password there. I would assume that this is exacrly what developers of monero-wallet had in mind when they introduced --password-file option.

I wouldn't assume that since `--config-file` was added after the various pasword options. I'm not aware of any remants this method would leave on disk, but I have put very little thought into it as well.

> I am more worried about the scenario when the attacker has a physical access to the server. Like in the various scenarios when authorities are confiscating the server and then hijacking the onipn domains, because the private keys where kept as a plaintext on the hdd. :)

Your situation is somewhat rare - password prompt can't be used? And disk usage is unacceptable? Presumably the password material is on some external device that gets pushed/pulled in memory only? Don't answer that if you feel uncomfortable.

Adding environment variable support is probably painless, I'm just skeptical that many people have a valid use case for it.

## reardenlife | 2019-08-03T13:47:18+00:00
@vtnerd
> "Your situation is somewhat rare - password prompt can't be used? "

Well, it can, but it is somewhat uncomfortable to enter it each time I would decide to restart monero-wallet-rpc.

> "Presumably the password material is on some external device that gets pushed/pulled in memory only?"

Yeah, inside the cryptocontainer.

> "Adding environment variable support is probably painless, I'm just skeptical that many people have a valid use case for it."

I just would like to point out that in programs like duplicity ( https://linux.die.net/man/1/duplicity , see "Environmental Variables") the passwords are passed this way.  Therefore I would think it is a good practice.

# Action History
- Created by: reardenlife | 2019-08-02T14:21:34+00:00
- Closed at: 2019-08-03T13:48:06+00:00
