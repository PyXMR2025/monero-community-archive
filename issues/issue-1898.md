---
title: Default action upon launching GUI when a wallet already exists - request for
  improvements
source_url: https://github.com/monero-project/monero-gui/issues/1898
author: kayront
assignees: []
labels:
- resolved
created_at: '2019-01-15T11:10:47+00:00'
updated_at: '2020-01-16T02:54:47+00:00'
type: issue
status: closed
closed_at: '2020-01-16T02:54:47+00:00'
---

# Original Description
(breaking down #1864 as requested)

After going through a successful wallet creation, closing the program and starting it again immediately prompts for the password of the wallet that was opened before the program was previously closed.

While this is not an unreasonable default, what comes next could, in my opinion, be improved.

The only options available at this point are to either input the password and click Ok, or Cancel.

Clicking Cancel brings the UI back to the language selection screen, and only after that can the user select whether to create a wallet, open an existing one, etcetera.

Let's focus on opening an existing one. I clicked that, and now there's a file dialog that defaults to the home directory, rather than the directory where monero saves wallets to disk.

On this subject, here's what I think could be improved:

  - Present the option to open any recently opened wallets, straight from the initial password dialog (could be a collapsible that reads "Open recent..").

  - If not the above, then at the very least the following: remember the language selection and avoid going back to that screen (but have a back button to go back there if needed), and jump straight to the second screen where creating/opening/restoring a wallet is possible - **and on the file dialog that follows, default to the directory where wallets are saved** - anything else is confusing for newbies, not everyone nontechnical understands directory structures.



# Discussion History
## xiphon | 2019-01-16T02:01:09+00:00
> If not the above, then at the very least the following: remember the language selection and avoid going back to that screen (but have a back button to go back there if needed), and jump straight to the second screen where creating/opening/restoring a wallet is possible

#1893 

## sanderfoobar | 2019-02-08T14:13:38+00:00
> Present the option to open any recently opened wallets, straight from the initial password dialog (could be a collapsible that reads "Open recent..").

I like this suggestion and it might make it into #1909, since I already made a 'Recently opened wallets' screen there.

## selsta | 2020-01-16T02:30:27+00:00
> If not the above, then at the very least the following: remember the language selection and avoid going back to that screen (but have a back button to go back there if needed), and jump straight to the second screen where creating/opening/restoring a wallet is possible - and on the file dialog that follows, default to the directory where wallets are saved - anything else is confusing for newbies, not everyone nontechnical understands directory structures.

This is now implemented with the new wizard.

+resolved

# Action History
- Created by: kayront | 2019-01-15T11:10:47+00:00
- Closed at: 2020-01-16T02:54:47+00:00
