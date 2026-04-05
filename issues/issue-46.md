---
title: Disk location
source_url: https://github.com/Cuprate/cuprate/issues/46
author: hinto-janai
assignees: []
labels:
- C-discussion
created_at: '2023-12-13T01:42:47+00:00'
updated_at: '2024-05-27T00:57:07+00:00'
type: issue
status: closed
closed_at: '2024-02-28T22:51:37+00:00'
---

# Original Description
## What
Where will Cuprate store files on disk?

Closes https://github.com/monero-project/monero/pull/8202 in spirit ❤️

## Most likely
OS standards are settled and are available in the widely used https://docs.rs/dirs.

Reference:
- [XDG base directory](https://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html) and the [XDG user directory](https://www.freedesktop.org/wiki/Software/xdg-user-dirs/) specifications on Linux
- [Known Folder](https://msdn.microsoft.com/en-us/library/windows/desktop/bb776911(v=vs.85).aspx) system on Windows
- [Standard Directories](https://developer.apple.com/library/content/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/FileSystemOverview/FileSystemOverview.html#//apple_ref/doc/uid/TP40010672-CH2-SW6) on macOS
- [List of XDG supporting software](https://wiki.archlinux.org/title/XDG_Base_Directory#Supported)

Examples:
| OS      | PATH                                                            |
|---------|-----------------------------------------------------------------|
| Windows | `C:\Users\Alice\AppData\Roaming\Cuprate\cuprate.toml`           |
| macOS   | `/Users/Alice/Library/Application Support/Cuprate/cuprate.toml` |
| Linux   | `/home/alice/.config/cuprate/cuprate.toml`                      |

## What else
There are some remaining questions:
- on macOS, the XDG standard could also be considered, leading to `~/.config/cuprate/cuprate.toml` there as well
- should the heavy separation of files (`~/.config`, `~/.cache`, `~/.local/share`) be skipped?
- should global files be supported (`/etc/cuprate.toml`)?

Supporting user override PATHs will also need to be supported, for all file types (config, cache, database, etc).

# Discussion History
## rbrunner7 | 2023-12-13T18:36:32+00:00
Hopefully Rust left behind stupid bugs in its file and path name handling for good! The standard C++ library that Monero uses on Windows does not support Unicode in the stream classes. Names with Unicode characters mostly occur of course if the user's name has some "special" character in it.

## hinto-janai | 2023-12-13T21:57:52+00:00
Rust's [`std::path`](https://doc.rust-lang.org/stable/std/path) abstracts over ASCII, UTF-8, and UTF-16 :)

## SyntheticBird45 | 2023-12-18T14:12:42+00:00
> should global files be supported (`/etc/cuprate.toml`)?

Yes, a flexible systemd/initd script would otherwise be difficult to setup. Monerod systemd service use by default the `--config /etc/monerod.conf` and I think it is great

>  should the heavy separation of files (`~/.config`, `~/.cache`, `~/.local/share`) be skipped?

From a user experience, I hate searching through different folders. Cuprate can split files but then it should be clearly explained in the wiki or other accessible documentation.

> on macOS, the XDG standard could also be considered, leading to `~/.config/cuprate/cuprate.toml` there as well

This one is up to anyone natural language interpretation. Is cuprate.toml more of a *config file* or an *application support file*. It is more a settings file than anything else. I think `~/.config/cuprate/cuprate.toml` is better

## hinto-janai | 2024-02-04T13:50:26+00:00
> Cuprate can split files but then it should be clearly explained in the wiki or other accessible documentation

I think:
- The main `cuprate.toml` -> `~/.config`
- All non-essential cache files -> `~/.cache`
- Everything else -> `~/.local/share`

> This one is up to anyone natural language interpretation

I meant that macOS has 2 locations for files. Looking at this again, I think we should just stick to Apple's [standard](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/FileSystemOverview/FileSystemOverview.html), using `~/Library/Application Support`; this is used by most applications and is actually what [`dirs::config_dir()`](https://docs.rs/dirs/latest/dirs/fn.config_dir.html) returns.

## SyntheticBird45 | 2024-02-04T14:39:00+00:00
> I meant that macOS has 2 locations for files. Looking at this again, I think we should just stick to Apple's [standard](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/FileSystemOverview/FileSystemOverview.html), using ~/Library/Application Support; this is used by most applications and is actually what [dirs::config_dir()](https://docs.rs/dirs/latest/dirs/fn.config_dir.html) returns.

Makes sense indeed. Let's go for Application Support then

> I think:

I'm not sure if the `~/.local/share` `~/.cache` and `~/.config` is a linux consensus or an XDG standard ?
I could imagine people would make cuprate runs on a server with just a chowned folder with the cuprate user. Not sure there will be these folders by default (at least using `adduser`). The paths look good for me but then we'll have to set fallback if these folders don't exist

## hinto-janai | 2024-02-04T16:03:15+00:00
XDG is the defacto Linux standard.

Every program I've ever used calls `std::fs::create_dir_all()` or equivalent on missing folders.

## hinto-janai | 2024-02-28T22:51:37+00:00
Implemented in https://github.com/Cuprate/cuprate/pull/67 with the standards in the original post.

# Action History
- Created by: hinto-janai | 2023-12-13T01:42:47+00:00
- Closed at: 2024-02-28T22:51:37+00:00
