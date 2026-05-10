---
title: 'security: unnecessary requirement for persistent root privilege for MSR'
source_url: https://github.com/xmrig/xmrig/issues/3813
author: amrfti
assignees: []
labels: []
created_at: '2026-05-08T03:43:32+00:00'
updated_at: '2026-05-08T08:33:49+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
# Current Problem:

Current XMRig documentation and internal messaging encourages users to run the entire process with root privileges. This is an unnecessary security risk because the requirement for root is transient, yet the application remains as root for its entire lifecycle.

From https://xmrig.com/docs/miner/randomx-optimization-guide/msr:
> If you use recent XMRig with root privileges (Linux) or admin privileges (Windows) the miner configure all MSR registers automatically.

As far as I'm aware this is the ***only*** reason to run XMRig as root.

By suggesting users run XMRig with elevated privileges, the project is advocating a violation of the principle of least privilege. When running XMRig as root it risks system compromise if a vulnerability is found in the Stratum protocol handling, HTTP API, or JSON-RPC components. It is a major unnecessary risk.

# Proposed solution:

I believe that in terms of UX, the best way to solve this problem would be to have the MSR modification as a separate program/process. Though, I believe this is unlikely to be done as it would break past behaviour.
Instead, the most realistic approach I see to solving this is XMRig adding a `--user` flag. If started as root then XMRig should perform the MSR setup then immediately drop to the specified unprivileged user using `setuid`/`setgid`.
To avoid breaking things for now I believe there should be a warning to the user when XMRig is run with `CAP_SYS_ADMIN` without providing an argument to `--user`. As many other programs do, running as root should be allowed, but discouraged.

# Discussion History
## amrfti | 2026-05-08T03:53:02+00:00
I missed the fact that root is also used to enable huge pages. Though this falls under the same scenario as the MSR mod of a transient root requirement.

## SChernykh | 2026-05-08T08:33:49+00:00
First, XMRig needs to restore the MSR registers at exit because the values it uses for mining are very bad for general application performance. Second, there is already a separate script to set up MSR registers, so you can run XMRig without sudo: https://github.com/xmrig/xmrig/blob/master/scripts/randomx_boost.sh

# Action History
- Created by: amrfti | 2026-05-08T03:43:32+00:00
