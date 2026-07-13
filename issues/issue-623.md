---
title: Use a readline implementation for the interactive command loop
source_url: https://github.com/Cuprate/cuprate/issues/623
author: redsh4de
assignees: []
labels:
- C-proposal
created_at: '2026-05-28T22:11:46+00:00'
updated_at: '2026-07-11T19:07:38+00:00'
type: issue
status: closed
closed_at: '2026-07-11T19:07:38+00:00'
---

# Original Description
## What
I propose using a readline-style line editor for the interactive command loop.

This also can bring command history, and if the library supports it - a stable prompt that log output renders above, instead of cutting through what the user types. Opens the door for tab autocomplete and other non-essential UX improvements down the line. 

## Why
Better UX in interactive terminals. monerod supports GNU Readline for this

## Where
cuprated's command listener and stdout logging path.

## How
Two capabilities are needed: line editing with history, and a external writer for async output (logs and command results) above the prompt so it isn't corrupted by it.

From the options i looked at, [rustyline](https://github.com/kkawakam/rustyline) is a solid choice for this, due to its maturity (since 2015, active maintenance), and minimal new deps, aside from rustyline itself:
| Platform | Transitive deps added |
|---|---|
| Unix | `nix`, `unicode-width`, `utf8parse` |
| Windows | `clipboard-win`, `error-code`, `unicode-width` |

Should probably be feature-flagged the same way Arti currently is

# Discussion History
## redsh4de | 2026-07-11T19:07:38+00:00
Not planned, in favor of a full fledged TUI as a seperate binary, embedding the cuprate lib.

# Action History
- Created by: redsh4de | 2026-05-28T22:11:46+00:00
- Closed at: 2026-07-11T19:07:38+00:00
