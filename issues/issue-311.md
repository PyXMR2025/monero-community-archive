---
title: Sandboxing support
source_url: https://github.com/Cuprate/cuprate/issues/311
author: SyntheticBird45
assignees: []
labels:
- C-discussion
- P-low
- A-binaries
created_at: '2024-10-11T22:33:44+00:00'
updated_at: '2024-10-14T15:45:41+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## What

This is issue is for discussing sandboxing capabilities built-in Cuprate.
It has been a [feature proposed at the beginning of the project](https://github.com/Cuprate/cuprate/commit/58a076f3aa44c4a19c6758308a8336d48861ae17#diff-5a831ea67cf5cf8703b0de46901ab25bd191f56b320053be9332d9a3b0d01d15L51-L55)

## Why

Some sandboxing API in operating system requires the running process to setup the jail itself or through the help of a helper.
Integrating the use of these API into Cuprate will help at mitigating the damage of a potential bug or exploit if it ever happens, by attempting to enforce a more precise execution of the [Principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege).

## How

If available on the platform, Cuprate will use the native OS API to sandbox itself. Cuprate will attempt to restrict iself to only
access and interact with the resources it needs (Configuration, database and network) and nothing else.

### Linux

Linux have a wide variety of options to enable a process isolation:

| Method      | Benefits   | Min.Version | Potential crates | Notes |
|-------------|------------|-------------|------------------|-------|
| [seccomp-bpf](https://www.kernel.org/doc/html/latest/userspace-api/seccomp_filter.html) | syscall filtering | Linux kernel 3.17 | [seccompiler](https://crates.io/crates/seccompiler) | [A lot of software uses this method](https://en.wikipedia.org/wiki/Seccomp#Software_using_seccomp_or_seccomp-bpf) |
| [landlock](https://www.kernel.org/doc/html/latest/userspace-api/landlock.html) | File access control | Linux kernel 5.13 | [landlock](https://crates.io/crates/landlock) | Landlock have recently received the ability the restrict unix socket (which was impossible before). But we cannot count on very recent feature for compatibility purposes |
| [user namespaces](https://www.man7.org/linux/man-pages/man7/user_namespaces.7.html) | Resources/File access control | Linux kernel 3.8 | libc | Double-edged sword. While many praises user namespaces for its isolation capabilities, it is also a trivial way to acquire significantly more kernel attack surface. It is also very difficult to implement |

#### Apparmor&SELinux

These are external access control that requires a policy. Cuprate process have no involvements in setting up these access controls methods.
An example Apparmor/SELinux policy could be maintained if wished.

#### SUID helper

Some software have historically made great use of SUID binary to setup new chroot and other kernel namespaces to sandbox their application. This is bad for security:
- It requires to build another binary.
- It should absolutely be safe from any vulnerability (impossible). (as SUID bit will immediately elevate the binary as root).
For more informations on why Chromium has been transitioning to unprivileged namespaces: https://issues.chromium.org/issues/40338793

#### Additional options

`yama_ptrace` could apparently be used to mitigate compromised processes from inspecting other processes memory (of the same user).

### Windows

The only available option is using built-in permissions system in Windows API. See [Chromium Windows sandbox architecture](https://chromium.googlesource.com/chromium/src/+/HEAD/docs/design/sandbox.md#Sandbox-Windows-architecture)

### MacOS

There is an [available API for Swift and Objective-C program](https://developer.apple.com/documentation/security/app-sandbox) to enable a permission sandbox. However, whether this can be used
by other programming languages is unknown.

# Discussion History
## SyntheticBird45 | 2024-10-11T22:35:26+00:00
My take is that Cuprate should at the very least implements `seccomp_filter` (`seccomp-bpf`).

## dimalinux | 2024-10-12T21:27:24+00:00
Would providing good docker documentation/scripts and possibly even a container as well as telling users not to run as root fall in the scope of this issue? Docker provides seccomp syscall filtering. If filtering is done via docker, end users don't have to trust us developers. With modern compiler features and Rust, injecting syscalls into cuprated is fairly low when ordering attack vectors by viability. If we are worried about 3rd party libraries turning malicious, we'll need to make sure that any security code we run gets executed before any 3rd party code runs.

## SyntheticBird45 | 2024-10-14T15:45:40+00:00
> Would providing good docker documentation/scripts and possibly even a container as well as telling users not to run as root fall in the scope of this issue? Docker provides seccomp syscall filtering. If filtering is done via docker, end users don't have to trust us developers. With modern compiler features and Rust, injecting syscalls into cuprated is fairly low when ordering attack vectors by viability. If we are worried about 3rd party libraries turning malicious, we'll need to make sure that any security code we run gets executed before any 3rd party code runs.

I doesn't fall into the scope of this issue since it is something external to Cuprate. As explained with Apparmor and SELinux
> These are external access control that requires a policy. Cuprate process have no involvements in setting up these access controls methods.
An example Apparmor/SELinux policy could be maintained if wished.

I wouldn't be against setting up a script(+ seccomp policy) and documentation file regarding containers (dockers/podman). However, I'm not particularly fan relying exclusively on this method as it forces users to rely on user namespaces for sandboxing, which as explained in its own paragraph:
> it is also a trivial way to acquire significantly more kernel attack surface.

I'm part of the paranoid users that disable this kernel feature.

But yeah I'm not against documenting and providing policies for containers. (I will open another issue at some point)

# Action History
- Created by: SyntheticBird45 | 2024-10-11T22:33:44+00:00
