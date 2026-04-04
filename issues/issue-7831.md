---
title: Add flag to reject v2 onion addresses
source_url: https://github.com/monero-project/monero/issues/7831
author: cirocosta
assignees: []
labels: []
created_at: '2021-08-04T15:43:36+00:00'
updated_at: '2023-08-17T15:11:28+00:00'
type: issue
status: closed
closed_at: '2023-08-17T15:11:28+00:00'
---

# Original Description
According to Tor's deprecation timeline for onion v2 addresses:

```
  1) September 15th, 2020
     0.4.4.x: Tor will start warning onion service operators and clients that
              v2 is deprecated and will be obsolete in version 0.4.6

  2) July 15th, 2021
     0.4.6.x: Tor will no longer support v2 and will be removed from the code
              base.

  3) October 15th, 2021
     We will release new stable versions for all supported series that will
     disable v2.
```

_(^ https://lists.torproject.org/pipermail/tor-dev/2020-June/014365.html)_

we're just past having onion v2 not being supported anymore. 

The current stable release gives us back a warning

``` 
Aug 04 11:21:26.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
```

but the next stable will actually be an error:

```c
    /* If we get here, it's a request for a .onion address! */

    /* We don't support v2 onions anymore. Log a warning and bail. */
    if (addresstype == ONION_V2_HOSTNAME) {
      log_warn(LD_PROTOCOL, "Tried to connect to a v2 onion address, but this "
               "version of Tor no longer supports them. Please encourage the "
               "site operator to upgrade. For more information see "
               "https://blog.torproject.org/v2-deprecation-timeline.");
      control_event_client_status(LOG_WARN, "SOCKS_BAD_HOSTNAME HOSTNAME=%s",
                                  escaped(socks->address));
      /* Send back the 0xF6 extended code indicating a bad hostname. This is
       * mostly so Tor Browser can make a proper UX with regards to v2
       * addresses. */
      conn->socks_request->socks_extended_error_code = SOCKS5_HS_BAD_ADDRESS;
      connection_mark_unattached_ap(conn, END_STREAM_REASON_TORPROTOCOL);
      return -1;
```

_(^ https://gitlab.torproject.org/tpo/core/tor/-/blob/301ffb71a695e89f2e4905e2260fce15439259f1/src/core/or/connection_edge.c#L2528-2545)_

---

I propose that we include a flag (enabled by default? not sure) that would reject any v2 onion addresses if set.

```bash
monerod --disable-tor-onion-v2

# or ..

monerod --reject-tor-onion-v2

# ..?
```

or something similar

wdyt? thx

# Discussion History
## cirocosta | 2021-08-04T15:46:39+00:00
related: 

- https://github.com/bitcoin/bitcoin/issues/21351, implemented @ https://github.com/bitcoin/bitcoin/pull/22050

> [...] This patch removes support in Bitcoin Core for Tor v2 onions, which are already removed from the release of Tor 0.4.6.

sounds like there's precedence for actually completely removing it, which sounds good to me.

## xanoni | 2021-08-16T00:46:19+00:00
Agree, no to the switch. Whoever hasn't upgraded to Onion v3 after months (years?) of very clear communication from the Tor Project probably shouldn't be running a `monerod`.

# Action History
- Created by: cirocosta | 2021-08-04T15:43:36+00:00
- Closed at: 2023-08-17T15:11:28+00:00
