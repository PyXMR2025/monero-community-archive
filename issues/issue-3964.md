---
title: Builtin Tor Routing
source_url: https://github.com/monero-project/monero-gui/issues/3964
author: nickname76
assignees: []
labels: []
created_at: '2022-07-09T12:54:48+00:00'
updated_at: '2022-08-07T19:45:54+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Add builtin tor routing as a switch in settings (at least for simple mode, or any mode when using remote node)

# Discussion History
## fugbixer | 2022-08-01T12:00:54+00:00
like wasabi

would add more dependencies but I*m in favor of this suggestion as optional feature.
most remote nodes are legit community members but the traffic too them shall still be obfuscated if wished.
i mean your isp knows it, your gov knows it, the remote node knows it. where the money goes: no one knows it.
monero is plug and play private and adding tor as optional feature for noobs who can't enable it on their own might benefit.
okay this is arguable, we know everyone gets flagged as dangerous when the person is using freedom preserving tech.

building tor into monero could make users who use it more suspicious than before when they are no tech wizards
therefore a build in warning and disclaimer shall be served as well as an option to request a bridge.

(still the tor bridges are low on number and every gov can pay a brainlet to solve 100 captcha a day to get all tor bridges)

the on going censorship is quite heavy , turkey for example is also increasing pressure on vpns and isp's for limiting the internet access for years now.

but i guess using a free currency is at least  as dangerous as using the free web for fascists in control (and the few legit concerns like cp , fraud etc but i would try solving these issues over other levers being a cop than building a huge prison and we all know there are no drugs nor violence  in prison...)

https://fraserinstitute.org/studies/economic-freedom-of-the-world-2021-annual-report

Russian users for example are not allowed to use crypto nor tor - so depends on detection rate
Indian users - tor is allowed i guess but crypto is banned? 

best joke i heard is  that cops can distinguish a toaster from a floppy disk drive 

still honest good acting people get busted for non violent usage of freedom preserving tech.

sad that people in power tighten their grip around their citizens property thinking they deserve a portion of it for violating human rights and providing a stable and more moderate environment of injustice ...

## nickname76 | 2022-08-01T13:09:51+00:00
As Tor is blocked in several countries, this feature should also include settings for obsf4, snowflake etc. for mitigation of Tor blocking

## nickname76 | 2022-08-01T13:11:04+00:00
And also, this feature would help monero apps and stuff work if someone tries to block monero

## boldsuck | 2022-08-07T19:45:01+00:00
[Feather](https://featherwallet.org/) is already a XMR Tor wallet with Monero .onion nodes.

- Socks5 proxy button has been in the GUI for a very long time.
- A builtin tor would mean monero-gui almost always has an outdated tor daemon. It is always better to use the current one from the Tor Project repository.
- obfs4proxy & snowflake-client are another 2 extra packages, not from the Tor Project.

# Action History
- Created by: nickname76 | 2022-07-09T12:54:48+00:00
