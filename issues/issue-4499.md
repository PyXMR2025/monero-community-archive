---
title: Rewrite with modern standards
source_url: https://github.com/monero-project/monero-gui/issues/4499
author: An-anonymous-coder
assignees: []
labels: []
created_at: '2025-09-04T01:08:44+00:00'
updated_at: '2025-10-04T15:50:38+00:00'
type: issue
status: closed
closed_at: '2025-09-29T14:00:36+00:00'
---

# Original Description
I'm opening Pandora's box.

To put it simply, Monero GUI has fallen behind on some modern standards. I propose that a separate repository should be created with a rewrite from the ground up. Some of the changes would include:
- Written in Rust (Monero nodes are [already getting the rewrite](https://cuprate.org/))
- Adwaita design language
- GTK 4
- Wayland (it currently uses insecure X11 by default, and the `QT_QPA_PLATFORM=wayland` flag needs to be manually set)
- Verified Flatpak (covered by https://github.com/monero-project/monero-gui/issues/4206)
- Split functionality across multiple apps (e.g. one for wallet management, one for mining, etc.)
- Remove deprecated features ([OpenAlias](https://github.com/openalias) hasn't seen any activity in over 6 months. By most accounts, it has been abandoned)
- Passkey support
- Export transactions to ODS instead of CSV, and automatically sort it
- etc.

Also, Monero still has no official mobile app. I would be willing to compromise on modern desktop development if Monero instead maintained a modern Android app:
- Written in Kotlin
- Material Design 3 Expressive design language
- Jetpack Compose
- Available to install from [Accrescent](https://accrescent.app/)
- NFC payments
- etc.

This would be a well needed breath of life into Monero usability, and would also greatly benefit performance and security.

P.S. While this issue mostly pertains to Linux and Android, other operating systems have their own standards that Monero GUI should follow. Apple devices use Swift and Liquid Glass, Windows devices use C# and Fluent Design System, etc. It's up to you whether or not you want to maintain separate repositories for those.

For other projects:

- Monero should host their projects on Forgejo, Codeberg, or GitLab, and mirror to other platforms
- If you haven't already, it would also be a good idea to switch your servers over to Qubes OS or [securecore](https://secureblue.dev/images#server)
- You can protect your website from bots using [Anubis](https://anubis.techaro.lol/)
- An I2P site should be available
- Atom feeds are more modern than RSS
- Monero should have a SimpleX Chat contact, especially for vulnerability reports
- The website should use SVGs for images (browsers that block images can still see SVGs and they have lossless quality)
- The videos on the websites are low quality (720x480) and use a proprietary format (M4V). It should use a free and open format and have quality at least 1920x1080.
- The website should dynamically switch to dark mode using [prefers-color-scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme)

# Discussion History
## Lovinoes | 2025-09-29T13:58:22+00:00
you funny 

## selsta | 2025-09-29T14:00:36+00:00
Thank you for the suggestions but this is not an actionable issue, more of general critiques on how you would prefer things. If you have specific bugs with monero-gui please open separate issues for it.

## An-anonymous-coder | 2025-09-30T20:39:18+00:00
> more of general critiques on how you would prefer things

Following these standards fixes numerous bugs and security issues. A verified Flatpak allows Monero GUI to be installed on hardened Linux distributions such as [secureblue](https://secureblue.dev/) without making a global security exception. GNOME plans to drop support for X11, because it is highly insecure, and Monero GUI should be using Wayland by default. Linux has [known insecurities](https://privsec.dev/posts/linux/linux-insecurities/), so having official support for a secure operating system like [GrapheneOS](https://grapheneos.org/) (based on Android) improves security and usability. Using [memory safe languages](https://media.defense.gov/2025/Jun/23/2003742198/-1/-1/0/CSI_MEMORY_SAFE_LANGUAGES_REDUCING_VULNERABILITIES_IN_MODERN_SOFTWARE_DEVELOPMENT.PDF) such as Rust reduces vulnerabilities that are introduced in languages like C, and can significantly improve performance. Passkey support ensures that the wallet can only be opened with something you have (e.g. a hardware security key) instead of something you know (e.g. a passphrase). The list goes on.

I agree that some of my suggestions are quality of life improvements, but Monero should heavily consider moving in that direction. 

## nahuhh | 2025-09-30T21:25:13+00:00

> Following these standards fixes numerous bugs and security issues. A verified Flatpak allows Monero GUI to be installed on hardened Linux distributions such as [secureblue](https://secureblue.dev/) without making a global security exception.

verified flatpaks are security theater, and is a WIP anyway. You still have to trust flathub

> GNOME plans to drop support for X11, because it is highly insecure, and Monero GUI should be using Wayland by default.

Monero gui doesn't do whatever gnome / systemd wants to do. It is multi-platform and works under wayland and x11. Also, aiui, x11 is not being dropped due to security, but due to politics.

> Linux has [known insecurities](https://privsec.dev/posts/linux/linux-insecurities/), so having official support for a secure operating system like [GrapheneOS](https://grapheneos.org/) (based on Android) improves security and usability.

This sounds like marketing garbage. You do know that graphene/android is linux, and based on an old linux kernels? And follows behind whatever google does?

> Using [memory safe languages](https://media.defense.gov/2025/Jun/23/2003742198/-1/-1/0/CSI_MEMORY_SAFE_LANGUAGES_REDUCING_VULNERABILITIES_IN_MODERN_SOFTWARE_DEVELOPMENT.PDF) such as Rust reduces vulnerabilities that are introduced in languages like C, and can significantly improve performance.

more marketing garbage. If you like rust, there is cuprate. Rust has memory safety, but brings its own set of issues such as supply chain.

is graphene written in rust? How about android? How about linux kernel? What about macos? Windows? Rust performance is neither inherently nor significantly better than C. 

> Passkey support ensures that the wallet can only be opened with something you have (e.g. a hardware security key) instead of something you know (e.g. a passphrase). The list goes on.

is this a feature request?

## An-anonymous-coder | 2025-10-01T03:37:51+00:00
> verified flatpaks are security theater, and is a WIP anyway. You still have to trust flathub

It's still better than unverified Flatpaks. Monero should have compatibility with hardened systems like secureblue.

> Also, aiui, x11 is not being dropped due to security, but due to politics.

This doesn't change that X11 is insecure and needs to be deprecated. Many systems use Wayland by default or disable X11 altogether (like secureblue). At the very least, Monero should use Wayland by default.

> This sounds like marketing garbage.

If providing examples of security focused projects in the context of security is marketing, then I'm sorry.

> You do know that graphene/android is linux,

Android (and by extension, GrapheneOS) are based on the Linux kernel, but it doesn't suffer the same insecurities I mentioned before. On top of that, many hardware and software security measures are put in place to further secure the system.

> and based on an old linux kernels

The kernel versions are still maintained. GrapheneOS uses the most up to date versions of Android, which come with reasonably new versions of the Linux kernel.

> And follows behind whatever google does?

Google is often good for security, but often bad for privacy. GrapheneOS doesn't include any Google Play Services by default, and removes the privacy invasive features Google has added to Android. 

> If you like rust, there is cuprate.

I know. I referenced it in my original issue. It doesn't affect the GUI.

> is graphene written in rust?

Many portions of GrapheneOS are written in Rust where possible, such as their network location feature.

> How about linux kernel?

Much of the Linux kernel is being rewritten in Rust.

> What about macos? Windows?

Providing counterexamples doesn't mean that Rust is insecure or shouldn't be used. I could easily say "Why use Monero if XYZ only accepts Bitcoin?" That doesn't mean Monero shouldn't be used or isn't private. 

> is this a feature request?

Many of my suggestions in this issue are feature requests. 

## An-anonymous-coder | 2025-10-04T13:56:41+00:00
Can this be reopened until it is sorted out?

## selsta | 2025-10-04T15:50:38+00:00
I closed this issue because I don't see this getting "sorted out". OpenAlias is not deprecated, Flatpak has a separate issue open and the rest is your personal preference or not realistically implementable (like for example Passkey). Some other things are unrelated to monero-gui.

# Action History
- Created by: An-anonymous-coder | 2025-09-04T01:08:44+00:00
- Closed at: 2025-09-29T14:00:36+00:00
