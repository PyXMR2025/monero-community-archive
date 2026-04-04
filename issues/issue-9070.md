---
title: 'WRONG DATA CONVERSION: from type=d to type m '
source_url: https://github.com/monero-project/monero/issues/9070
author: whitevoid90
assignees: []
labels:
- invalid
created_at: '2023-11-18T15:36:16+00:00'
updated_at: '2023-12-07T22:21:20+00:00'
type: issue
status: closed
closed_at: '2023-12-07T22:21:20+00:00'
---

# Original Description
im running a monero node with rpc wallet . everything was working fine but suddenly im getting an error on the rpc wallet .
can anyone explain what this error is ?

E WRONG DATA CONVERSION: from type=d to type m 
E Exception on unserializing: WRONG DATA CONVERSION: from type=d to type m

# Discussion History
## selsta | 2023-11-18T15:37:23+00:00
When exactly does this error happen?

## whitevoid90 | 2023-11-18T15:41:51+00:00
thr rpc is connected to one of my website . it has escrow system , when i release the money it game me this error . i made another rpc wallet that is working fine , but on the first wallet im still getting this error

## selsta | 2023-11-18T15:43:45+00:00
Is it multisig? Can you share the full error message, I'm curious if it says where exactly this error occurs in the source code.

## jeffro256 | 2023-11-18T15:49:20+00:00
What action are you taking that causes the error to trigger?

## whitevoid90 | 2023-11-18T16:44:22+00:00
2023-11-18 16:15:11.681	D handle_accept
2023-11-18 16:15:11.681	D New server for RPC connections, SSL autodetection
2023-11-18 16:15:11.681	D Spawned connection #21 to 0.0.0.0 currently we have sockets count:2
2023-11-18 16:15:11.684	T New connection from host 127.0.0.1: 0
2023-11-18 16:15:11.684	D  connection type 1 127.0.0.1:18083 <--> 127.0.0.1:55202 (via 127.0.0.1:55202)
2023-11-18 16:15:11.684	D SSL detection buffer, 9 bytes: 80 79 83 84 32 47 106 115 111
2023-11-18 16:15:11.684	T Moving counter buffer by 1 second 0 < 2748 (last time 0)
2023-11-18 16:15:11.685	T Throttle throttle_speed_in: packet of ~136b  (from 136 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [136 0 0 0 0 0 0 0 0 0 ]
2023-11-18 16:15:11.685	T Moving counter buffer by 1 second 2687 < 2748 (last time 2687.33)
2023-11-18 16:15:11.685	T Moving counter buffer by 1 second 2688 < 2748 (last time 2688.33)
2023-11-18 16:15:11.685	T Moving counter buffer by 1 second 2689 < 2748 (last time 2689.33)
2023-11-18 16:15:11.686	T Moving counter buffer by 1 second 2690 < 2748 (last time 2690.33)
2023-11-18 16:15:11.686	T Moving counter buffer by 1 second 2691 < 2748 (last time 2691.33)
2023-11-18 16:15:11.687	T Moving counter buffer by 1 second 2692 < 2748 (last time 2692.33)
2023-11-18 16:15:11.687	T Moving counter buffer by 1 second 2693 < 2748 (last time 2693.33)
2023-11-18 16:15:11.687	T Moving counter buffer by 1 second 2694 < 2748 (last time 2694.33)
2023-11-18 16:15:11.687	T Moving counter buffer by 1 second 2695 < 2748 (last time 2695.33)
2023-11-18 16:15:11.687	T Moving counter buffer by 1 second 2696 < 2748 (last time 2696.33)
2023-11-18 16:15:11.687	T Moving counter buffer by 1 second 2697 < 2748 (last time 2697.33)
2023-11-18 16:15:11.687	T Moving counter buffer by 1 second 2698 < 2748 (last time 2698.33)
2023-11-18 16:15:11.687	T Moving counter buffer by 1 second 2699 < 2748 (last time 2699.33)
2023-11-18 16:15:11.688	T Moving counter buffer by 1 second 2700 < 2748 (last time 2700.33)
2023-11-18 16:15:11.688	T Moving counter buffer by 1 second 2701 < 2748 (last time 2701.33)
2023-11-18 16:15:11.688	T Moving counter buffer by 1 second 2702 < 2748 (last time 2702.33)
2023-11-18 16:15:11.688	T Moving counter buffer by 1 second 2703 < 2748 (last time 2703.33)
2023-11-18 16:15:11.688	T Moving counter buffer by 1 second 2704 < 2748 (last time 2704.33)
2023-11-18 16:15:11.688	T Moving counter buffer by 1 second 2705 < 2748 (last time 2705.33)
2023-11-18 16:15:11.688	T Moving counter buffer by 1 second 2706 < 2748 (last time 2706.33)
2023-11-18 16:15:11.688	T Moving counter buffer by 1 second 2707 < 2748 (last time 2707.33)
2023-11-18 16:15:11.688	T Moving counter buffer by 1 second 2708 < 2748 (last time 2708.33)
2023-11-18 16:15:11.688	T Moving counter buffer by 1 second 2709 < 2748 (last time 2709.33)
2023-11-18 16:15:11.688	T Moving counter buffer by 1 second 2710 < 2748 (last time 2710.33)
2023-11-18 16:15:11.689	T Moving counter buffer by 1 second 2711 < 2748 (last time 2711.33)
2023-11-18 16:15:11.689	T Moving counter buffer by 1 second 2712 < 2748 (last time 2712.33)
2023-11-18 16:15:11.689	T Moving counter buffer by 1 second 2713 < 2748 (last time 2713.33)
2023-11-18 16:15:11.689	T Moving counter buffer by 1 second 2714 < 2748 (last time 2714.33)
2023-11-18 16:15:11.689	T Moving counter buffer by 1 second 2715 < 2748 (last time 2715.33)
2023-11-18 16:15:11.689	T Moving counter buffer by 1 second 2716 < 2748 (last time 2716.33)
2023-11-18 16:15:11.689	T Moving counter buffer by 1 second 2717 < 2748 (last time 2717.33)
2023-11-18 16:15:11.689	T Moving counter buffer by 1 second 2718 < 2748 (last time 2718.33)
2023-11-18 16:15:11.690	T Moving counter buffer by 1 second 2719 < 2748 (last time 2719.33)
2023-11-18 16:15:11.690	T Moving counter buffer by 1 second 2720 < 2748 (last time 2720.33)
2023-11-18 16:15:11.690	T Moving counter buffer by 1 second 2721 < 2748 (last time 2721.33)
2023-11-18 16:15:11.690	T Moving counter buffer by 1 second 2722 < 2748 (last time 2722.33)
2023-11-18 16:15:11.690	T Moving counter buffer by 1 second 2723 < 2748 (last time 2723.33)
2023-11-18 16:15:11.690	T Moving counter buffer by 1 second 2724 < 2748 (last time 2724.33)
2023-11-18 16:15:11.690	T Moving counter buffer by 1 second 2725 < 2748 (last time 2725.33)
2023-11-18 16:15:11.690	T Moving counter buffer by 1 second 2726 < 2748 (last time 2726.33)
2023-11-18 16:15:11.690	T Moving counter buffer by 1 second 2727 < 2748 (last time 2727.33)
2023-11-18 16:15:11.691	T Moving counter buffer by 1 second 2728 < 2748 (last time 2728.33)
2023-11-18 16:15:11.691	T Moving counter buffer by 1 second 2729 < 2748 (last time 2729.33)
2023-11-18 16:15:11.691	T Moving counter buffer by 1 second 2730 < 2748 (last time 2730.33)
2023-11-18 16:15:11.691	T Moving counter buffer by 1 second 2731 < 2748 (last time 2731.33)
2023-11-18 16:15:11.691	T Moving counter buffer by 1 second 2732 < 2748 (last time 2732.33)
2023-11-18 16:15:11.691	T Moving counter buffer by 1 second 2733 < 2748 (last time 2733.33)
2023-11-18 16:15:11.691	T Moving counter buffer by 1 second 2734 < 2748 (last time 2734.33)
2023-11-18 16:15:11.691	T Moving counter buffer by 1 second 2735 < 2748 (last time 2735.33)
2023-11-18 16:15:11.691	T Moving counter buffer by 1 second 2736 < 2748 (last time 2736.33)
2023-11-18 16:15:11.691	T Moving counter buffer by 1 second 2737 < 2748 (last time 2737.33)
2023-11-18 16:15:11.691	T Moving counter buffer by 1 second 2738 < 2748 (last time 2738.33)
2023-11-18 16:15:11.692	T Moving counter buffer by 1 second 2739 < 2748 (last time 2739.33)
2023-11-18 16:15:11.692	T Moving counter buffer by 1 second 2740 < 2748 (last time 2740.33)
2023-11-18 16:15:11.692	T Moving counter buffer by 1 second 2741 < 2748 (last time 2741.33)
2023-11-18 16:15:11.692	T Moving counter buffer by 1 second 2742 < 2748 (last time 2742.33)
2023-11-18 16:15:11.692	T Moving counter buffer by 1 second 2743 < 2748 (last time 2743.33)
2023-11-18 16:15:11.692	T Moving counter buffer by 1 second 2744 < 2748 (last time 2744.33)
2023-11-18 16:15:11.692	T Moving counter buffer by 1 second 2745 < 2748 (last time 2745.33)
2023-11-18 16:15:11.692	T Moving counter buffer by 1 second 2746 < 2748 (last time 2746.33)
2023-11-18 16:15:11.693	T Moving counter buffer by 1 second 2747 < 2748 (last time 2747.33)
2023-11-18 16:15:11.693	T Throttle <<< global-IN: packet of ~136b  (from 136 b) Speed AVG=   0[w=9.795]    0[w=9.795] /  Limit=16 KiB/sec  [136 0 0 0 0 0 0 0 0 0 ]
2023-11-18 16:15:11.693	T HTTP HEAD:
2023-11-18 16:15:11.693	T Host: 127.0.0.1:18083
2023-11-18 16:15:11.693	T Accept: */*
2023-11-18 16:15:11.693	T Accept-Encoding: gzip,deflate
2023-11-18 16:15:11.693	T Content-type: application/json
2023-11-18 16:15:11.693	T Content-Length: 0
2023-11-18 16:15:11.693	T 
2023-11-18 16:15:11.693	I HTTP [127.0.0.1] POST /json_rpc
2023-11-18 16:15:11.693	T HTTP_RESPONSE_HEAD: << 
2023-11-18 16:15:11.693	T HTTP/1.1 200 Ok
2023-11-18 16:15:11.693	T Server: Epee-based
2023-11-18 16:15:11.693	T Content-Length: 111
2023-11-18 16:15:11.693	T Content-Type: application/json
2023-11-18 16:15:11.693	T Last-Modified: Sat, 18 Nov 2023 16:15:11 GMT
2023-11-18 16:15:11.693	T Accept-Ranges: bytes
2023-11-18 16:15:11.693	T 
2023-11-18 16:15:11.693	T Moving counter buffer by 1 second 0 < 2748 (last time 0)
2023-11-18 16:15:11.693	T Throttle throttle_speed_out: packet of ~271b  (from 271 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [271 0 0 0 0 0 0 0 0 0 ]
2023-11-18 16:15:11.693	T Moving counter buffer by 1 second 2687 < 2748 (last time 2687.34)
2023-11-18 16:15:11.693	T Moving counter buffer by 1 second 2688 < 2748 (last time 2688.34)
2023-11-18 16:15:11.693	T Moving counter buffer by 1 second 2689 < 2748 (last time 2689.34)
2023-11-18 16:15:11.693	T Moving counter buffer by 1 second 2690 < 2748 (last time 2690.34)
2023-11-18 16:15:11.693	T Moving counter buffer by 1 second 2691 < 2748 (last time 2691.34)
2023-11-18 16:15:11.693	T Moving counter buffer by 1 second 2692 < 2748 (last time 2692.34)
2023-11-18 16:15:11.693	T Moving counter buffer by 1 second 2693 < 2748 (last time 2693.34)
2023-11-18 16:15:11.693	T Moving counter buffer by 1 second 2694 < 2748 (last time 2694.34)
2023-11-18 16:15:11.698	T Moving counter buffer by 1 second 2695 < 2748 (last time 2695.34)
2023-11-18 16:15:11.698	T Moving counter buffer by 1 second 2696 < 2748 (last time 2696.34)
2023-11-18 16:15:11.698	T Moving counter buffer by 1 second 2697 < 2748 (last time 2697.34)
2023-11-18 16:15:11.698	T Moving counter buffer by 1 second 2698 < 2748 (last time 2698.34)
2023-11-18 16:15:11.698	T Moving counter buffer by 1 second 2699 < 2748 (last time 2699.34)
2023-11-18 16:15:11.698	T Moving counter buffer by 1 second 2700 < 2748 (last time 2700.34)
2023-11-18 16:15:11.698	T Moving counter buffer by 1 second 2701 < 2748 (last time 2701.34)
2023-11-18 16:15:11.698	T Moving counter buffer by 1 second 2702 < 2748 (last time 2702.34)
2023-11-18 16:15:11.699	T Moving counter buffer by 1 second 2703 < 2748 (last time 2703.34)
2023-11-18 16:15:11.699	T Moving counter buffer by 1 second 2704 < 2748 (last time 2704.34)
2023-11-18 16:15:11.699	T Moving counter buffer by 1 second 2705 < 2748 (last time 2705.34)
2023-11-18 16:15:11.699	T Moving counter buffer by 1 second 2706 < 2748 (last time 2706.34)
2023-11-18 16:15:11.699	T Moving counter buffer by 1 second 2707 < 2748 (last time 2707.34)
2023-11-18 16:15:11.699	T Moving counter buffer by 1 second 2708 < 2748 (last time 2708.34)
2023-11-18 16:15:11.699	T Moving counter buffer by 1 second 2709 < 2748 (last time 2709.34)
2023-11-18 16:15:11.699	T Moving counter buffer by 1 second 2710 < 2748 (last time 2710.34)
2023-11-18 16:15:11.699	T Moving counter buffer by 1 second 2711 < 2748 (last time 2711.34)
2023-11-18 16:15:11.699	T Moving counter buffer by 1 second 2712 < 2748 (last time 2712.34)
2023-11-18 16:15:11.699	T Moving counter buffer by 1 second 2713 < 2748 (last time 2713.34)
2023-11-18 16:15:11.699	T Moving counter buffer by 1 second 2714 < 2748 (last time 2714.34)
2023-11-18 16:15:11.700	T Moving counter buffer by 1 second 2715 < 2748 (last time 2715.34)
2023-11-18 16:15:11.700	T Moving counter buffer by 1 second 2716 < 2748 (last time 2716.34)
2023-11-18 16:15:11.700	T Moving counter buffer by 1 second 2717 < 2748 (last time 2717.34)
2023-11-18 16:15:11.700	T Moving counter buffer by 1 second 2718 < 2748 (last time 2718.34)
2023-11-18 16:15:11.700	T Moving counter buffer by 1 second 2719 < 2748 (last time 2719.34)
2023-11-18 16:15:11.700	T Moving counter buffer by 1 second 2720 < 2748 (last time 2720.34)
2023-11-18 16:15:11.700	T Moving counter buffer by 1 second 2721 < 2748 (last time 2721.34)
2023-11-18 16:15:11.700	T Moving counter buffer by 1 second 2722 < 2748 (last time 2722.34)
2023-11-18 16:15:11.700	T Moving counter buffer by 1 second 2723 < 2748 (last time 2723.34)
2023-11-18 16:15:11.700	T Moving counter buffer by 1 second 2724 < 2748 (last time 2724.34)
2023-11-18 16:15:11.700	T Moving counter buffer by 1 second 2725 < 2748 (last time 2725.34)
2023-11-18 16:15:11.701	T Moving counter buffer by 1 second 2726 < 2748 (last time 2726.34)
2023-11-18 16:15:11.701	T Moving counter buffer by 1 second 2727 < 2748 (last time 2727.34)
2023-11-18 16:15:11.701	T Moving counter buffer by 1 second 2728 < 2748 (last time 2728.34)
2023-11-18 16:15:11.701	T Moving counter buffer by 1 second 2729 < 2748 (last time 2729.34)
2023-11-18 16:15:11.701	T Moving counter buffer by 1 second 2730 < 2748 (last time 2730.34)
2023-11-18 16:15:11.701	T Moving counter buffer by 1 second 2731 < 2748 (last time 2731.34)
2023-11-18 16:15:11.702	T Moving counter buffer by 1 second 2732 < 2748 (last time 2732.34)
2023-11-18 16:15:11.702	T Moving counter buffer by 1 second 2733 < 2748 (last time 2733.34)
2023-11-18 16:15:11.703	T Moving counter buffer by 1 second 2734 < 2748 (last time 2734.34)
2023-11-18 16:15:11.703	T Moving counter buffer by 1 second 2735 < 2748 (last time 2735.34)
2023-11-18 16:15:11.703	T Moving counter buffer by 1 second 2736 < 2748 (last time 2736.34)
2023-11-18 16:15:11.703	T Moving counter buffer by 1 second 2737 < 2748 (last time 2737.34)
2023-11-18 16:15:11.703	T Moving counter buffer by 1 second 2738 < 2748 (last time 2738.34)
2023-11-18 16:15:11.703	T Moving counter buffer by 1 second 2739 < 2748 (last time 2739.34)
2023-11-18 16:15:11.703	T Moving counter buffer by 1 second 2740 < 2748 (last time 2740.34)
2023-11-18 16:15:11.703	T Moving counter buffer by 1 second 2741 < 2748 (last time 2741.34)
2023-11-18 16:15:11.703	T Moving counter buffer by 1 second 2742 < 2748 (last time 2742.34)
2023-11-18 16:15:11.703	T Moving counter buffer by 1 second 2743 < 2748 (last time 2743.34)
2023-11-18 16:15:11.703	T Moving counter buffer by 1 second 2744 < 2748 (last time 2744.34)
2023-11-18 16:15:11.706	T Moving counter buffer by 1 second 2745 < 2748 (last time 2745.34)
2023-11-18 16:15:11.706	T Moving counter buffer by 1 second 2746 < 2748 (last time 2746.34)
2023-11-18 16:15:11.706	T Moving counter buffer by 1 second 2747 < 2748 (last time 2747.34)
2023-11-18 16:15:11.706	T Throttle >>> global-OUT: packet of ~271b  (from 271 b) Speed AVG=   0[w=9.804]    0[w=9.804] /  Limit=16 KiB/sec  [271 0 0 0 0 0 0 0 0 0 ]
2023-11-18 16:15:11.707	T Throttle throttle_speed_in: packet of ~474b  (from 474 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [610 0 0 0 0 0 0 0 0 0 ]
2023-11-18 16:15:11.707	T Throttle <<< global-IN: packet of ~474b  (from 474 b) Speed AVG=   0[w=9.817]    0[w=9.817] /  Limit=16 KiB/sec  [610 0 0 0 0 0 0 0 0 0 ]
2023-11-18 16:15:11.707	T HTTP HEAD:
2023-11-18 16:15:11.707	T Host: 127.0.0.1:18083
2023-11-18 16:15:11.707	T Accept: */*
2023-11-18 16:15:11.707	T Accept-Encoding: gzip,deflate
2023-11-18 16:15:11.707	T Content-type: application/json
2023-11-18 16:15:11.708	T Content-Length: 327
2023-11-18 16:15:11.708	T 
2023-11-18 16:15:11.708	I HTTP [127.0.0.1] POST /json_rpc
2023-11-18 16:15:11.708	E WRONG DATA CONVERSION: from type=d to type m
2023-11-18 16:15:11.708	E Exception on unserializing: WRONG DATA CONVERSION: from type=d to type m
2023-11-18 16:15:11.708	T HTTP_RESPONSE_HEAD: << 
2023-11-18 16:15:11.708	T HTTP/1.1 200 Ok
2023-11-18 16:15:11.708	T Server: Epee-based
2023-11-18 16:15:11.708	T Content-Length: 110
2023-11-18 16:15:11.708	T Content-Type: application/json
2023-11-18 16:15:11.709	T Last-Modified: Sat, 18 Nov 2023 16:15:11 GMT
2023-11-18 16:15:11.709	T Accept-Ranges: bytes

## whitevoid90 | 2023-11-18T16:48:43+00:00
its an ecommerce site . where people can buy with escrow . when the buyer release the fund thats where im getting this error . it used to wrok fine before . after making a new rpc wallet its working fine . but its not working with the first wallet 

## vtnerd | 2023-11-19T00:10:20+00:00
The error is about converting a `double` to type `unsigned long`.

Make sure your client is _not_ sending a decimal point (not certain what field there isn't enough information).

## 0xFFFC0000 | 2023-12-07T22:20:43+00:00
After talking to @vtnerd it seems the problem is not in our end. I am closing this issue. Please feel free to reopen or ask questions if you still had any problems. 

# Action History
- Created by: whitevoid90 | 2023-11-18T15:36:16+00:00
- Closed at: 2023-12-07T22:21:20+00:00
