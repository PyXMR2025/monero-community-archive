---
title: 'gitian: CA certs are out of date'
source_url: https://github.com/monero-project/monero/issues/7147
author: hyc
assignees: []
labels: []
created_at: '2020-12-14T00:47:22+00:00'
updated_at: '2022-02-19T00:53:55+00:00'
type: issue
status: closed
closed_at: '2022-02-19T00:53:55+00:00'
---

# Original Description
The server for the depends/packages/native_cdrkit.mk https://distro.ibiblio.org has a new server certificate, whose issuer cert isn't present in /etc/ssl/certs on the gitian build image. As such, curl refuses to connect and is unable to fetch this package. People who are building for the first time, and don't already have this in their cache, will be unable to build.

Seems like it may be time to update our base image from Ubuntu Bionic. Or we figure out how to insert an updated CA cert package onto the build image.

# Discussion History
## setuidroot | 2020-12-17T04:10:04+00:00
I don't know anything about *Gitian* or your build system.  But I do know Ubuntu.  Do you have (root) shell access to the Ubuntu build system?

If you have root (sudo) shell access, then this is an easy *partial* fix.  There are 2 potential problems here; but the second issue is with the website's certificate chain.  We can't fix that, but you can update Ubuntu's trusted certificate list.  To do that, you need to update Ubuntu's *ca-certificates* package.

First, update all of Ubuntu's APT packages:

````
sudo apt update
````

Then update/install ca-certificates:

````
apt install -y ca-certificates
````

You should really upgrade all packages as well (but this is optional as it could break something that depends on older versions of a certain package):

````
sudo apt upgrade
````

The important thing here is to install and/or update the *ca-certificates* package.  This package updates Ubuntu's SSL certificates.

By installing *ca-certificates* package, Ubuntu will update the outdated "AddTrust_External_Root.pem" (expired May 30 2020) certificate with the newest "USERTrust_RSA_Certification_Authority.pem" certificate.  These are both located in /etc/ssl/certs.

````
ls -A /etc/ssl/certs/AddTrust_External_Root.pem
````
If the above command finds a certificate, that's the expired one that will be replaced by installing *ca-certificates* package.  It's replaced with "USERTrust_RSA_Certification_Authority.pem"

````
ls -A /etc/ssl/certs/USERTrust_RSA_Certification_Authority.pem
````
^ This certificate should be found, not the expired AddTrust one.

Updating the expired AddTrust certificate makes curl work about 50% of the time.  It will work when it gets the correctly signed certificate chain.  Sometimes they send a certificate chain that's expired or sent out of order, which will be rejected.

You can see this in action with wget --spider "https://distro.ibiblio.org".  Sometimes it works, sometimes it doesn't work.  [See what I mean.](https://user-images.githubusercontent.com/32213080/102440902-b9f80800-3fe6-11eb-9bd4-0a9c9e22e6b9.png)


I actually just tested this to confirm.  With the old expired AddTrust certificate, it never worked.  With the updated *ca-certificates*, it works about 50% of the time.  This is because distro.ibiblio.org's cert chain is messed up.  They have a chain with an expired trusted root certificate and they have a cert chain that is out of order.  Only 1 out of 3 of their cert chains are actually valid and working.  [See here.](https://user-images.githubusercontent.com/32213080/102440628-34745800-3fe6-11eb-95d4-117310f48e3a.png)  Actually 2 out of 3 will work with the updated *ca-certificates* package because the expired AddTrust cert is automatically replaced by the updated USERTrust cert.

Do you need to use "distro.ibiblio.org"?  Can you not use a different Ubuntu package mirror?  I don't know... just trying to help.

You could take distro.ibiblio.org's untrusted locally signed certificate and add it to your trusted certificates by putting it in the */usr/local/share/ca-certificates* directory.  This is generally something you don't do for OpSec reasons.  They need to fix their certificate chain.

Just FYI Ubuntu keeps these certificates updated by default with unattended-upgrades (unless you've disabled that.)  So I think this issue is entirely with distro.ibiblio.org and not your build system.  But I recommend updating to Ubuntu 20.04 (focal) anyways because why not?  Oh the 5.4.x Linux Kernels are so much nicer than the older ones on Bionic.  Mostly I like the colored *dmesg* output and some other pretty CLI things lol.  Plus *lscpu* shows you a list of all the known major hardware vulnerabilities (Meltdown, Spectre, etc) and the kernel's mitigation steps put in place for them.  You can optionally disable these vulnerability mitigations for *possibly* some hardware performance gain... but I wouldn't recommend doing that on any production server or any server facing the public internet (without NAT protection.)

To be honest, I don't fully understand what you mean when you said *"People who are building for the first time, and don't already have this in their cache, will be unable to build."*  🤔  Umm...

````
git clone --recursive https://github.com/monero-project/monero && cd monero && make release
````
Works every time for me.  I guess you have a public build server or something?  Oh huh... Gitian I read lets you make binaries that are identical for cross checking.  I suck with programming, but I would probably make a good dev for Gitian.  I know Ubuntu very well and I'm rather anal about security.  I guess I'll look into Gitian a bit when I have time... I just post this hoping it'll help.  🤔  Can Gitian be put in Docker or snap?  I assume it's just a consistent build image with the same compilers and dependency versions?  Oh I'll search and answer my own questions.

## setuidroot | 2020-12-17T06:43:55+00:00
[This](https://gist.github.com/9ab7d6fe563b8d71932863371e195c24) is the issuer cert that would need to be added locally so that when distro.ibiblio.org's cert chain comes out of order from their server, it will still work for you.  It's an issuer cert from USERTrust that signs the InCommon RSA Server CA that verifies distro.ibiblio.org's local web cert (it's not ibiblio's local certificate itself; using that one doesn't work and is less secure IMHO.)  I think adding this one is fine because it's a valid certificate that just verifies the authenticity of ibiblio's cert chain (when it is sent out of order.)

It's rather easy to add this.  You should add it as root because the file owner and group should be root, standard permissions (-rw-r--r--) for the file.  Basically...

Login as root:
````
sudo su
````
Wget download the certificate file and write it into */usr/local/share/ca-certificates* :
````
wget "https://gist.githubusercontent.com/setuidroot/9ab7d6fe563b8d71932863371e195c24/raw/7cc94915fa0947ef4a070220ad6a3de0f07df2ed/distro_ibiblio_org.crt" -O /usr/local/share/ca-certificates/distro_ibiblio_org.crt
````
Now run *update-ca-certificates* (also as root) and it will add this certificate into the trusted list as a symlink at */etc/ssl/certs/distro_ibiblio_org.pem*
````
update-ca-certificates
````

Now it will work 100% of the time (I tested to confirm this.)

~~I can write a simple shell script to do this if that would help.~~  It would also not be difficult to add this certificate into the source code of the build image so the distro is built with it already in the trusted certificate chain.

I wrote a bash script to do this automatically here: https://github.com/setuidroot/gitian-sslfix

Easy to run (as root or with a user that has sudo privileges) with this one line command:

````
wget -O - https://raw.githubusercontent.com/setuidroot/gitian-sslfix/main/gitian-sslfix.sh | bash
````

Hope this helps somebody.

## hyc | 2022-02-19T00:53:55+00:00
We no longer depend on the offending package so this is no longer occurring.

# Action History
- Created by: hyc | 2020-12-14T00:47:22+00:00
- Closed at: 2022-02-19T00:53:55+00:00
