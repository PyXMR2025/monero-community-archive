---
title: Warning "Invalid DNSSEC TXT record signature for updates.moneropulse.org"
source_url: https://github.com/monero-project/monero/issues/8452
author: stmax82
assignees: []
labels: []
created_at: '2022-07-21T22:35:59+00:00'
updated_at: '2026-02-09T22:51:10+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I'm getting the following warning soon after starting monerod since I updated to v0.18:

```
W Invalid DNSSEC TXT record signature for updates.moneropulse.org: validation failure <updates.moneropulse.org. TXT IN>: no DNSKEY rrset from 127.0.0.11 for trust anchor . while building chain of trust
```

Not sure what it's trying to tell me.

Tested on Ubuntu 18.04 and 22.04 in Docker.

# Discussion History
## selsta | 2022-07-22T10:56:42+00:00
From IRC

```
09:49 <@fluffypony> "no DNSKEY rrset for trust anchor . while building chain of trust"
09:49 <@fluffypony> ok so that's the root domain
09:49 <@fluffypony> the way DNSSEC works is it only has one key hardcoded, the one for .
09:50 <@fluffypony> then it checks the trust anchor for .net based on the trust anchor for .
09:50 <@fluffypony> then the trust anchor for moneropulse.net, and then for updates.moneropulse.net
09:50 <@fluffypony> so if it's failing on . that means that either your ISP isn't serving DNSSEC records when requested, OR the utility is busted
```

At the moment it's unclear if this is a monero bug or if it's an ISP issue. You can ignore it for now.

## OrvilleRed | 2022-07-26T20:12:51+00:00
I also got this same DNSSEC warning upon running v18.0

Debugged a little on IRC with moo.

`dig -t TXT updates.moneropulse.org` returned success: `; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 20843`

I ran monerod with --log-level 4 and pared down the log to what I think are the relevant bits; saved here https://paste.debian.net/1248443/

I do see that after the initial warning, monerod is "falling back to TCP with well known DNSSEC resolvers". It's not 100% clear from the log whether that fallback worked, but afterwards I do see further messages like "Performing DNSSEC TXT record query for updates.moneropulse.fr" that are not followed by any error.

I'm happy to provide more debug info as requested


I'm happy to provide any other debug output to help

## sanderfoobar | 2022-07-26T23:02:31+00:00
This error is reproducible with my (possibly stupid) router, `/etc/resolv.conf` having the common value of:

```text
nameserver 127.0.0.53
```

And the following code:

```c
// gcc main.cpp -lunbound -o main
#include <stdio.h>
#include <string.h>
#include <unbound.h>

static struct ub_ctx *uctx = NULL;
#define TYPE_TXT 16

int main() {
  struct ub_result *result;
  char domain[] = "updates.moneropulse.org";

  if (uctx == NULL) { uctx = ub_ctx_create(); }
  ub_ctx_add_ta(uctx, ". IN DS 20326 8 2 E06D44B80B8F1D39A95C0B0D7C65D08458E880409BBC683457104237C7F8EC8D\n");

  ub_ctx_resolvconf(uctx, NULL);
  ub_resolve(uctx, domain, TYPE_TXT, 1, &result);

  if (result->secure)
    fprintf(stdout, "DNSSEC validation successful for domain %s.\n", domain);
  else
    fprintf(stdout, "DNSSEC validation failed: %s\n", result->why_bogus);

  if (result->bogus)
    fprintf(stdout, "Possible attack on this domain :(\n");

  if (result->data[0] != NULL)
    fprintf(stdout, "DNS reply received: %s\n", result->data[0]);
 else
    fprintf(stdout, "DNS empty :(");
  return 1;
}
```

When getting rid of the function [ub_ctx_resolvconf](https://nlnetlabs.nl/documentation/unbound/doxygen/libunbound_8c.html#abe77a2db0e90b3c548de4f232ba49146) the error goes away. In the Monero codebase this function is called [here](https://github.com/monero-project/monero/blob/b6a029f222abada36c7bc6c65899a4ac969d7dee/src/common/dns_utils.cpp#L284) and can be 'skipped' by setting an env. var:

```bash
DNS_PUBLIC="tcp://8.8.8.8" ./monerod 
```

Or you can modify `/etc/resolv.conf` such that it includes `nameserver 8.8.8.8`

In my case `127.0.0.53` goes to systemd-resolved which in turn is configured by my router via DHCP. Not sure where exactly this DNSSEC query breaks.

## side-note

Unrelated to this issue, I believe the DS on the first line here is outdated (since 2019):

https://github.com/monero-project/monero/blob/b6a029f222abada36c7bc6c65899a4ac969d7dee/src/common/dns_utils.cpp#L105-L106

You can confirm this by using [get_trust_anchor.py](https://raw.githubusercontent.com/iana-org/get-trust-anchor/master/get_trust_anchor.py) or looking at [root-anchors.xml](https://data.iana.org/root-anchors/root-anchors.xml)

## sanderfoobar | 2022-07-26T23:15:14+00:00
The naming of `DNS_PUBLIC` env. var is a bit 'weird' here because it kind of implies a bool switch that will make unbound use public server(s). Indeed, if we call [ub_resolve](https://nlnetlabs.nl/documentation/unbound/doxygen/libunbound_8c.html#aeb73245888a3c93392375bf29c4738a8) *without* using [ub_ctx_resolvconf](https://nlnetlabs.nl/documentation/unbound/doxygen/libunbound_8c.html#abe77a2db0e90b3c548de4f232ba49146), libunbound's default behavior is to use [some internally defined public servers.](https://github.com/NLnetLabs/unbound/blob/11f2e7e6ae4e4f728616bfeb35dc422d40585548/iterator/iter_hints.c#L130)

Maybe an env. var by the name of `DNS_ADDRESS` (or some such) is better suited should one feel the need to supply their own DNS.

## sanderfoobar | 2022-07-28T09:43:08+00:00
To conclude, I think my default DNS server (and OPs) do not handle DNSSEC correctly. Monero operates in 2 ways:

1. it either respects the network config (`/etc/resolv.conf`)
2. or you manually supply it an alternative via e.g `DNS_PUBLIC`

Monero cannot automatically fallback on alternatives [like the DNS servers provided by unbound](https://github.com/NLnetLabs/unbound/blob/11f2e7e6ae4e4f728616bfeb35dc422d40585548/iterator/iter_hints.c#L130) because that would be considered a privacy leak.

So make sure your network infra is up to spec. Issue can be closed if someone agrees with this conclusion.

## OrvilleRed | 2022-07-28T16:45:15+00:00
Yes, my resolv.conf was also using the "special" systemd-resolved address (127.0.0.53); it seems my current VPS mandates this.

I've verified that after setting DNS_PUBLIC to a more reliable DNS, I no longer get the DNSSEC warning

How about adding some info to the existing warning message? For example:

```
WARNING Invalid DNSSEC TXT record signature for ...
WARNING Your DNS server isn't behaving well. You can tell monerod to use an alternate via env variable DNS_PUBLIC. Example: DNS_PUBLIC="tcp://9.9.9.9" 
```

BTW, 9.9.9.9 is the IP address for [Quad9](https://www.quad9.net/), a Swiss public-benefit, not-for-profit foundation which purports to be privacy-respecting. It's probably a better example suggestion that Google's 8.8.8.8


## flipkickmedia | 2022-08-20T23:21:48+00:00
I'm also seeing this.  IMO this is a highly worrying message as it suggests there is an issue with the validity of the DNS records being provided to your monerod.

https://dnsviz.net/d/updates.moneropulse.org/dnssec/

This shows the chain of trust is correct.  There shouldn't be any problems with this record, as its just another DNS entry which should be supported by all DNS providers.

Furthermore, it appears that the DS record is stored inside some code:
https://github.com/monero-project/monero/issues/8474

This is even more worrying.  If a dev can provide a good explanation of why this is so.  I cant think of any scenario where you would store a DS record in code. 

These records should be checked live and the chain of trust should come from the TLD provider, not some record in code which can be modified.



## selsta | 2022-08-20T23:30:41+00:00
> If a dev can provide a good explanation of why this is so

This is the commit where it got added, doesn't really say _why_, just that it should not be hardcoded in the future: https://github.com/monero-project/monero/pull/244/commits/dbf46a721af5d54792bca80fc1c439c1badc9069

## qrhfz | 2022-08-23T13:20:22+00:00
i have the same problem. what is updates.moneropulse.org? i can't access it from browser.

## flguy76 | 2022-09-27T19:11:16+00:00
> 

did you notice what IP monerod is falling back to?  is it a root server or a public run server like googles?

## flguy76 | 2022-09-27T19:20:15+00:00
> 

storing a non authoritive server inside code can lead to dangerous outcomes.  and if someone wants to redirect all our traffic by changing the IP address of that record thats on the server embedded in the code things can get pretty nasty for your solo server quickly.   thats why security on DNS servers and the records that you server and are authorities for its important because you could be routed to some script kiddies home based DNS server and theres a lot that can go wrong from there.  esp for the windows guys..  I kind of want some form of explaination why this made it from the development tree into the production release tree.  thats the point of having one tree you develop in and another you release from.  so you can double and tripple check in a lab environment before it ever goes into production.   I have been a system engineer for 25 years and never once have we embedded DNS servers in release code.  its just not safe.  Makes us the lab rat not the end user. 

## sanderfoobar | 2022-09-27T19:53:25+00:00
@flguy76

> storing a non authoritive server inside code can lead to dangerous outcomes.

If you actually [read (or understood) my replies](https://github.com/monero-project/monero/issues/8452#issuecomment-1197911764) you would find that Monero does not "store non-authoritative servers inside the code". It doesn't even fallback on any DNS servers, as [unbound's default behavior is actively disabled](https://github.com/monero-project/monero/issues/8452#issuecomment-1196073692). Monero simply follows the network configuration of the OS it runs on. 

In fact, Monero is probably 'stricter' than most applications because it refuses to fallback - instead it screams at the user, which is why this thread exists.

## uyriq | 2023-03-07T16:57:56+00:00
> ```shell
> DNS_PUBLIC="tcp://8.8.8.8" 
> ```

are the variants tls (DOT), https (DOH) possible, in addition to simple tcp?

## OrvilleRed | 2023-03-27T05:00:30+00:00
> are the variants tls (DOT), https (DOH) possible, in addition to simple tcp?

No; the format and protocol must be "tcp".
`sscanf(s, "tcp://%u.%u.%u.%u%c"`

## blackzbr4 | 2023-10-28T07:18:18+00:00
i figured out that my blockchain got somehow corrupted. 
After removing it of course daemon  starts to download the chain again. Other then before it now started to do so immediately. However, after the first few messages about the status of the update the "invalid dnssec txt..." message appeared couple times but then I did not got it any more after i downloaded 1% of the chain or so. But importantly the daemon keeped updating.
i think the damage accrued when i started the daemon and it was updating my blockchain when suddenly the grid went down. when turning the computer back on i had this message the first time. 

## DiagonalArg | 2025-03-19T11:04:27+00:00
Same problem with version 0.18.3.4 on Ubuntu 22.04 running on bare metal.

## KernelTruth | 2025-07-27T14:10:56+00:00
###  GitHub Comment Draft

> I would like to report that this DNSSEC validation warning still occurs as of Monero `v0.18.4.0` and `v0.18.4.1`.
>
> ```
> W Invalid DNSSEC TXT record signature for updates.moneropulse.org: validation failure <updates.moneropulse.org. TXT IN>: no DNSKEY rrset for trust anchor . while building chain of trust
> ```
>
> ####  Setup details:
>
> * Monero daemon (`monerod`) is run via Docker on an OpenMediaVault 7 server (Debian-based).
> * Docker image is built manually using the static `monerod` binary from the official Monero GUI AppImage.
> * Monerod works correctly otherwise: syncs fully, GUI wallet connects via LAN, and mining operates without issue.
>
> ####  DNS Configuration:
>
> * My home network runs OpenWRT with `dnsmasq` as the resolver.
> * DNS is forwarded to **CZ.NIC's ODVR** service: [https://www.nic.cz/odvr/](https://www.nic.cz/odvr/) — a public recursive resolver that **fully supports DNSSEC validation**.
> * No other external resolvers are used — I explicitly avoid Google, Cloudflare, or Quad9 due to privacy preferences.
>
> ####  Behavior:
>
> * The warning appears *consistently on every `monerod` startup*, regardless of daemon version.
> * There are no other connectivity issues; all blockchain activity and peer communications function as expected.
> * DNSSEC for other queries (tested via `dig +dnssec`) validates correctly through my DNS pipeline.
>
> ####  Questions:
>
> 1. Is this expected behavior due to limitations in how `monerod` handles DNSSEC internally (e.g., fallback handling)?
> 2. Should I be ignoring this warning, or is there something misconfigured in `monerod`'s DNS logic when used behind a validating forwarder like CZ.NIC?
> 3. Would you recommend bypassing local DNS altogether and specifying `DNS_PUBLIC=tcp://...`, or does that undermine `monerod`'s intended secure lookup design?
>
> I’d be happy to assist in testing specific builds, toggling DNS flags, or generating detailed logs if needed. Thanks for all your work maintaining Monero.



## nahuhh | 2025-07-27T14:16:54+00:00
Have you tried another dns resolver by setting environment variable like 

```DNS_PUBLIC="tcp://9.9.9.9" ./monerod ...```
?

## KernelTruth | 2025-07-27T15:12:23+00:00
**Update:**

The issue appears to be resolved after explicitly setting the DNS server inside the Docker Compose file for `monerod`.

**Fix:**
I've added this to the service definition:

```yaml
dns:
  - 192.168.1.1
```

This points to my local OpenWRT router running `dnsmasq`. Once applied and the container restarted, the error:

```
W Invalid DNSSEC TXT record signature for updates.moneropulse.org: validation failure <updates.moneropulse.org. TXT IN>: no DNSKEY rrset for trust anchor . while building chain of trust
```

**no longer appears in the logs**, and Monero seems to perform the update check correctly.

**However**, calling:

```bash
docker exec -it monerod getent hosts updates.moneropulse.org
```

still returns **no result**, which suggests that Monero might not be using the system resolver or `getent`, but possibly a bundled resolver (like c-ares) or performing raw DNS queries internally.

The key takeaway: setting the `dns:` option in Docker Compose resolved the DNS resolution issue for Monero, even if `getent` still fails to resolve that domain.

## MoneroArbo | 2025-08-23T13:44:51+00:00
> This error is reproducible with my (possibly stupid) router, `/etc/resolv.conf` having the common value of:
> 
> ```
> nameserver 127.0.0.53
> ```
> 
> And the following code:
> 
> // gcc main.cpp -lunbound -o main
> #include <stdio.h>
> #include <string.h>
> #include <unbound.h>
> 
> static struct ub_ctx *uctx = NULL;
> #define TYPE_TXT 16
> 
> int main() {
>   struct ub_result *result;
>   char domain[] = "updates.moneropulse.org";
> 
>   if (uctx == NULL) { uctx = ub_ctx_create(); }
>   ub_ctx_add_ta(uctx, ". IN DS 20326 8 2 E06D44B80B8F1D39A95C0B0D7C65D08458E880409BBC683457104237C7F8EC8D\n");
> 
>   ub_ctx_resolvconf(uctx, NULL);
>   ub_resolve(uctx, domain, TYPE_TXT, 1, &result);
> 
>   if (result->secure)
>     fprintf(stdout, "DNSSEC validation successful for domain %s.\n", domain);
>   else
>     fprintf(stdout, "DNSSEC validation failed: %s\n", result->why_bogus);
> 
>   if (result->bogus)
>     fprintf(stdout, "Possible attack on this domain :(\n");
> 
>   if (result->data[0] != NULL)
>     fprintf(stdout, "DNS reply received: %s\n", result->data[0]);
>  else
>     fprintf(stdout, "DNS empty :(");
>   return 1;
> }
> 
> When getting rid of the function [ub_ctx_resolvconf](https://nlnetlabs.nl/documentation/unbound/doxygen/libunbound_8c.html#abe77a2db0e90b3c548de4f232ba49146) the error goes away. In the Monero codebase this function is called [here](https://github.com/monero-project/monero/blob/b6a029f222abada36c7bc6c65899a4ac969d7dee/src/common/dns_utils.cpp#L284) and can be 'skipped' by setting an env. var:
> 
> DNS_PUBLIC="tcp://8.8.8.8" ./monerod 
> 
> Or you can modify `/etc/resolv.conf` such that it includes `nameserver 8.8.8.8`
> 
> In my case `127.0.0.53` goes to systemd-resolved which in turn is configured by my router via DHCP. Not sure where exactly this DNSSEC query breaks.


I had this same issue ("no signatures from 127.0.0.53") because my Ubuntu installation also had 127.0.0.53 for resolv.conf

Fwiw, my other issue getting it working was that  /etc/systemd/resolved.conf was set to `DNSSEC=no`. To correct, I set `DNSSEC=allow-downgrade` which led to the above error, though dnssec appeared to be working at that point using dig. Setting the DNS server in resolved.conf did NOT overwrite the setting in /etc/resolv.conf

## NevDevB4 | 2026-02-09T22:51:10+00:00
Hey guys. Dont let the name fool you. Nice to meet you. Just recently became interested in crypto and Monero was, after some extential research, my choice to contribute to. Recently began running the node and also received this same Error. 

Invalid DNSSEC TXT record signature for updates.moneropulse.org:
validation failure <updates.moneropulse.org. TXT IN>:
no signatures from XXX . XXX . XX . X for DS org. while building chain of trust

THIS "ERROR" is ACTUALLY isn't a bad thing at all. I can understand why you would feel otherwise but let me explain. 

Monero is actually proving itself by this error from time to time. That warning is actually a good sign: your node is doing exactly what an operator‑safe Monero setup should do — refusing to trust a DNSSEC chain that doesn’t validate.

Moneo uses DNS TXT records for update checks, seed node discovery and sometimes for remote node lists. The DNS resolver you're using failed to provide a valid DNSSEC chain. The key part to this is "no signatures.. for DS org. While building chain of trust."

Meaning:

Your resolver did not return the DNSSEC signatures needed to prove asuthenticity. So monerod correctly rejected the record.

This is NOT a Monero problem, it's a DNSSEC resolver problem.
Our local resolver (likely any one of your router, Pi-Hole, or a local DNS forwarder<the more realistic reason>) is not performing DNSSEC validations correctly and Monero is behaving as it should: fail closed.

Why it happens could be any of the aforementioned points of possible faillure just does not support DNSSEC ( many consumer routers DO actually strip DNSSEC or simply dont validate it to begin with)

If this happens every so often the more likely reason is that the DNS server is doing DNSSEC but the upstream resolver as I mentioned isn't. 

Example:
Pi-Hole > ISP DNS (no DNSSEC)
Pi-Hole > Tries to validate > Fails

One other possible likelihood is that DNSSEC is enabled but the resolver is actually misconfigured. Commonly with Unbound, dnsmasq, and systemd-resolved instances when involved.

If you are running Unbound
Ensure these are set

<Code>
auto-trust-anchor-file: "/var/lib/unbound/root.key"
trust-anchor-signaling: yes
val-clean-additional: yes

Then Restart:

<Code>
sudo systemctl restart unbound

If you are using your router as DNS, Stop doing that
routers almost never handle DNSSEC correctly:
switch your system DNS to:

CLOUDFARE DNSSEC
1.1.1.1
1.0.0.1

QUAD9 DNSSEC
9.9.9.9
149.112.112.112

Both fully support DNSSEC and work prefectly with Monero

BE SURE TO RUN A CONFIRMATION TEST 
After switching DNS, run:

<code>
dig TXT updates.moneropulse.org +dnssec

You should see:
"ad" flag (authenticated data)
RRSIG records present

If you see either of those then DNSSEC is working

BUT bottonline

The node is fine.
The DNS resolver is not providing a valid DNSSEC chain.
Fix the resolver> the warning disappears.

If you want further help switching to a DNSSEC clean resolver, Im more than happy to assist. 

Anyway, i hope this puts some of your minds at ease and gives you a clear path of resolution moving forward. Happy mining guys 👍 


# Action History
- Created by: stmax82 | 2022-07-21T22:35:59+00:00
