---
title: 'Kovri: nightly/branch-tip static builds'
source_url: https://github.com/monero-project/meta/issues/35
author: anonimal
assignees: []
labels: []
created_at: '2017-01-02T00:24:42+00:00'
updated_at: '2017-03-16T17:21:52+00:00'
type: issue
status: closed
closed_at: '2017-03-16T17:21:52+00:00'
---

# Original Description
The idea is to use [makeself](https://github.com/megastep/makeself) on a per-platform basis (currently, we'll need to use msys2 on windows) though this does not substitute real packaging (and windows users will eventually not be be expected to have msys2 installed).

Once cloned, we'd run something like this with buildbot:

```bash
./makeself.sh ~/kovri-install ~/kovri-install.sh "Kovri Static Nightly Installer" ./install.sh  # preferably, the title will be appended with git revision hash
```

Where `~/kovri-install` has all contents of `kovri/pkg`, the binary `kovri/build/kovri`, and custom `install.sh` (will PR). Currently, that looks something like this:
```
$ ls -lha
total 96M
drwxr-xr-x  4 4.0K Jan  1 16:36 client
drwxr-xr-x  2 4.0K Jan  1 16:36 config
-rwxr-xr-x  1 1.3K Jan  2 00:19 install.sh
-rwxr-xr-x  1 96M Jan  1 15:41 kovri
```
Once complete, `kovri-install.sh` will be a single self-installable executable that can easily be distributed.

Note: I'll have to adjust the kovri Makefile to build static with coverage (I should probably open a separate issue for that). PR is on the way for the install script.

# Discussion History
## danrmiller | 2017-01-09T19:57:24+00:00
Why isn't install.sh included in the kovri repo instead of separately in this meta repo?

## anonimal | 2017-01-09T21:25:01+00:00
Because it's only useful with makeself (it will destroy a user's directory otherwise and wouldn't do any actual installation because the repo itself needs to be built statically). Since makeself is a separate script, I don't want to count on people *not* reading documentation on how to use makeself. I can foresee things like: *"but I ran install.sh, why did all my home directory contents disappear?"*, etc. Also, why would we do this since backend/static distribution is entirely our responsibility?

We could possibly bundle makeself and throw into the contrib directory along with install.sh. Would that be easier?

## danrmiller | 2017-01-09T21:57:14+00:00
It's fine as it is, I'll just have the buildbot job check out the installer from the meta repo. We certainly don't want to clobber a user's home directory. 

## anonimal | 2017-01-23T18:40:55+00:00
The static setup is coming along great, thanks @danrmiller. I think we need to resolve the following issues before announcing that we have nightly builds available:
- [x] Win32/64 is *not* building release-static
- [x] Ensure install scripts are set to executable (not all are +x right now)
- [x] We may be ok with using clang for both ARM builds, but more external testing is needed. We'll also need to verify that openssl is built statically with clang on ARM (ubuntu 32 + gcc is confirmed fixed) - now that https://gitlab.kitware.com/cmake/cmake/issues/16547#note_220657 is resolved. The latest ARMv8 install script shows that this is resolved (though locally, for me, it wasn't resolved)
- [x] ARMv7 build machine is having boost issues https://build.getmonero.org/builders/kovri-static-ubuntu-arm7/builds/2/steps/compile/logs/stdio
- [x] [QUESTION] should we move kovri binary into the data dir? For uninstall, a user can simply remove the data directory, adjust install script as necessary. For non-nightly release distributions, we could consider alternate options (less work is better though). ~~I'm *for* moving into data dir but only for the purpose of uninstalling. Otherwise, what we have now makes the most sense (IMHO).~~ **Edit**: on 2nd thought, I'm *for* moving the binary into `$(KOVRI_DATA_DIR)/bin` for the purpose of uninstalling and to house any other binaries https://github.com/monero-project/kovri/issues/399
- [x] I need to update the makeself install script and also consider the above question. I'll PR when that's finished
- [x] Create symlinks/URL's to the "latest" nightly build for the purpose of adding to the README/website and to aid scripts with fetching the latest build. Ideally this would also done for dynamic/PR/commit builds too so we can easily run clusterssh, run a download script, and do testing

## danrmiller | 2017-01-26T06:03:31+00:00
> Win32/64 is not building release-static

Static windows builds should work now.

> Ensure install scripts are set to executable (not all are +x right now)

This is now set.

> We may be ok with using clang for both ARM builds, but more external testing is needed. 

Clang, at least on ARM is not building kovri recently. As we discussed on irc, we'll build with GCC for now. I'll make additional clang build jobs and discuss with you or post github issues for whatever comes up.


> ARMv7 build machine is having boost issues

This is part of the issue clang has linking kovri right now.

> [QUESTION] should we move kovri binary into the data dir? 

I'll leave this up to you. I don't like that the current script creates a new hidden directory ~/.bin instead of what I consider more appropriate and standard ~/bin. I don't see a lot of benefit from makeself. I don't see any benefit in having installers for nightly test builds. For windows it is a barrier to entry. If we just provided a tarball, any windows user could test, with makeself, a bash shell (at least) is also required.
> Create symlinks/URL's to the "latest" nightly build for the purpose of adding to the README/website and to aid scripts with fetching the latest build.

We can make the latest build link to /downloads/kovri-$PLATFORM-latest or something. 
>  Ideally this would also done for dynamic/PR/commit builds too so we can easily run clusterssh, run a download script, and do testing

So you do want binaries built for PRs? Static builds? The github pull request number is a property available to the build job so we could make a way to include it in a download URL instead of the revision hash.


## anonimal | 2017-01-27T21:49:07+00:00
> Ensure install scripts are set to executable (not all are +x right now)

Pulling https://build.getmonero.org/builders/kovri-static-ubuntu-amd64/builds/7 shows otherwise. Will the new changes kick-in for the next build?

> I don't like that the current script creates a new hidden directory ~/.bin instead of what I consider more appropriate and standard ~/bin.

`~/bin` is a BSD thing. For Linux, usually a hidden directory or `/usr/local/bin`. Until we get proper packaging, I'm agree with should remove `~/.bin` and replacing with `~/.kovri/bin`.

Why not `/usr/local/bin`? Because I'm not counting on future packaging to remove anything that we do now and I want to avoid time-sucks when debugging for end-users who ended up using the wrong binary by mistake.

As such, I think we should keep things as centralized as possible - even if it does seem unorthodox (note: `~/.kovri/bin/` would *not* be unorthodox on Linux). As for OSX, we don't even have to keep the data directory in `~/Library/Application\ Support/` but I think it will do for now. And Windows is Windows.

>I don't see a lot of benefit from makeself. I don't see any benefit in having installers for nightly test builds.

I don't believe I ever asked for makeself self-installers for the dynamic builds, we only need them for the static build because they are *Nightly Releases* for public consumption. I don't see much benefit to having makeself for development builds because I have complete access to everything that's needed for development and know how to manually install needed files. And even though it would save time on re-builds or building of PR's I haven't tested, the costs of maintenance and disk-space don't justify the need IMHO. So,

- Dynamic builds ▶️  Development only ▶️ makeself **not** needed 
- Static nightly builds ▶️ End-user only ▶️  makeself **yes** needed

The installation *and* release process (for us, devops-wise) needs to be as simple as possible so, the less moving parts (or workarounds) - the better. Tarballs alone won't work because you need to A) expect a user to install the correct files into the correct directory and B) do that after doing correct uninstallation procedures; otherwise their config files are overwritten and they could be running the latest binary against a bad netdb, etc. Yes, we can solve these issues by having a tarball + install script but makeself handles this automatically:
- decompression
- uninstallation
- integrity checking
- installation
- user-feedback

all in one file; without user intervention. So, why not makeself?

Per-platform/distribution installations require package maintainers - which we don't have. makeself is the best we can do for now until some better ideas are proposed or maintainers are found. snapcraft, as great as it is with Linux, does not work for OSX (afaict), so makeself minimizes that dependency.  And because we don't have maintainers, a *unified installation setup* for ARM/Linux/OSX ultimately saves time on overhead

>For windows it is a barrier to entry. If we just provided a tarball, any windows user could test, with makeself, a bash shell (at least) is also required.

Like I've said before many times, makeself is obviously not a solution with Windows end-users but @livinginformation is working on a windows installer, so that will help. In the meantime, if you want to create a windows batch script combined with a zip file then be my guest. That solution could work enough for Windows and also not require msys2 but end-users would have to go to length to verify, etc.

>So you do want binaries built for PRs? Static builds?

I think I answered above. Binaries not needed for PR's, binaries + makeself needed for static builds.

>The github pull request number is a property available to the build job so we could make a way to include it in a download URL instead of the revision hash.

While we're here, could we also add build date to the filename?

## danrmiller | 2017-01-27T22:24:28+00:00
> Pulling https://build.getmonero.org/builders/kovri-static-ubuntu-amd64/builds/7 shows otherwise. Will the new changes kick-in for the next build?

I just tried that link and the install.sh within the makeself archive is +x. When previously it was not, running the kovri-%(gitversion)s-%(platform)s-install.sh would return an error indicating this. Can you confirm exactly what you are asking. If you are asking for us to somehow force the executable bit on the newly created .sh file on the downloading client users' filesystem, I don't think that's possible.

> ~/bin is a BSD thing. For Linux, usually a hidden directory or /usr/local/bin.

All the linux machines I'm looking at now have the following in the default ~/.profile for newly created users:
```
# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi
```

At least on the debian-based machines that I just looked into a little more closely, that is the shipped default. But XDG standard would be ~/.local/bin. My personal preference is still ~/bin/

> I think I answered above. Binaries not needed for PR's, binaries + makeself needed for static builds.

OK, I asked because it seems like you asked for binaries to be available for PRs here:

> Create symlinks/URL's to the "latest" nightly build for the purpose of adding to the README/website and to aid scripts with fetching the latest build. Ideally this would also done for dynamic/PR/commit builds too so we can easily run clusterssh, run a download script, and do testing

> While we're here, could we also add build date to the filename?

Yes, will do.

## anonimal | 2017-01-27T23:12:07+00:00
>I just tried that link and the install.sh within the makeself archive is +x

The final distributable file needs to be +x, not just install.sh. Example: https://build.getmonero.org/downloads/kovri-f0dcaae-linux-amd64-install.sh

>All the linux machines I'm looking at now have the following in the default ~/.profile for newly created users:

Not on Arch Linux, and the others require sourcing the profile (at least over ssh) for $PATH to be set accordingly.

Having the binary in the data directory is the most advantageous because it's the easiest to maintain across all platforms and easiest to uninstall. I agree that anything in $PATH is ideal, but even $PATH doesn't apply across all distros. Any other solutions?

## danrmiller | 2017-01-27T23:21:48+00:00
> The final distributable file needs to be +x, not just install.sh. Example: https://build.getmonero.org/downloads/kovri-f0dcaae-linux-amd64-install.sh

I just tried that too and the downloaded file on my system has the same exact permissions as the other file you linked. Just for fun I tried setting them +x on the server side, but it confirmed that of course this does not affect the new file the user's http client process creates on the user's filesystem. 

We could distribute a gzip archive containing the .sh instead of a .sh file, and the user's unarchiver should respect the permissions for the files it extracts. Otherwise the information about these attributes is not transmitted over http.

## anonimal | 2017-01-27T23:48:56+00:00
> If you are asking for us to somehow force the executable bit on the newly created .sh file on the downloading client users' filesystem, I don't think that's possible.

Yay http, I forgot about that. `umask` could technically restore our intended metadata but that is beyond silly.

>We could distribute a gzip archive containing the .sh instead of a .sh file

So, we're back to where we started. makeself was supposed to make things easier, not trickier.

Should we A) simply zip/tarball the installer and keep the installer B) throw out the makeself installer and ask the user to run the install script in the archive (which they'd do with every new download)? If B, where would we post checksums to verify integrity?

## anonimal | 2017-01-29T06:04:05+00:00
For windows, Inno Setup is looking like a good option for both nightlies and regular releases.  More details on IRC.

## anonimal | 2017-02-21T10:57:57+00:00
Re: #50:
```
&anonimal       pigeons: this will work with or without makeself as long as the same resources are copied into a staging directory https://github.com/monero-project/meta/pull/50
&anonimal       We can remove makeself now and finally tarball. What I think we should also do is upload a `sha256sum --tag` of the tarball as well. 
&anonimal       Signed releases will be a must though. This will be good enough for bare-minimum for nightlies though.
&anonimal       As for windoze, I'll see if a similar batch script or Inno Setup is easier.
&anonimal       Until then, we may as well continue what we're doing (tested/works with msys2).
```

Also to consider, now that we have flexibility (as you mentioned [here](https://github.com/monero-project/meta/issues/35#issuecomment-271390480)):
```
&anonimal       Hmm, with some tweaking we can throw this into the kovri repo and finalize our `make install` and maybe create a `--nightly` option that does everything you want buildbot to do with tarballing, etc.
```

## anonimal | 2017-02-22T16:35:24+00:00
@danrmiller #50 is finalized for now. Testing is successful on all platforms. Move live testing will help improve the overall experience though. I think that can come with time after we get these builds going (officially) live.

## anonimal | 2017-02-25T08:51:49+00:00
@danrmiller https://github.com/monero-project/meta/pull/50#issuecomment-282470676

## danrmiller | 2017-03-10T03:27:58+00:00
@anonimal I don't think the -f argument to kovri-install.sh works with -c and -p or I may not be using it correctly:

See https://build.getmonero.org/builders/kovri-static-ubuntu-amd64/builds/66/steps/package/logs/stdio

> bash -x ./pkg/kovri-install.sh -p -c -f kovri-latest-linux-amd64.tar.bz2
...
> Creating staging pathmkdir: missing operand
> Try 'mkdir --help' for more information.
> + catch 'could not create staging directory'
> + [[ 1 -ne 0 ]]
> + echo ' [ERROR] Failed to install: '\''could not create staging directory'\'' (B'

It seems to work fine without the -f.

## anonimal | 2017-03-11T21:24:28+00:00
Should be fixed in now-merged https://github.com/monero-project/kovri/pull/586

## danrmiller | 2017-03-13T21:20:19+00:00
@anonimal looks like something similar with DragonflyBSD:

https://build.getmonero.org/builders/kovri-static-dragonflybsd-amd64/builds/30/steps/package/logs/stdio

## anonimal | 2017-03-13T22:18:48+00:00
For the time being, can you install rsync on that machine? I'll simply extend #586 to dragonfly.

Ideally, that area should just be rewritten. For now I think these patches are fine because this is for packaging only and not end-user install. Open to ideas though.

## danrmiller | 2017-03-13T22:29:25+00:00
rsync has now been installed on the dragonflybsd build machine.

## danrmiller | 2017-03-13T23:00:50+00:00
The nightly kovri static builds now include packaging and upload steps. I've tested it out a little on linux amd64. See #56 

## anonimal | 2017-03-13T23:17:34+00:00
Fixed. Merged in https://github.com/monero-project/kovri/pull/589

## anonimal | 2017-03-16T17:21:52+00:00
Issue resolved! We did it! 👍 🍰 🎉

# Action History
- Created by: anonimal | 2017-01-02T00:24:42+00:00
- Closed at: 2017-03-16T17:21:52+00:00
