---
title: '[Ledger] Rejecting view key export'
source_url: https://github.com/monero-project/monero/issues/5361
author: roudaille
assignees: []
labels: []
created_at: '2019-03-28T10:08:46+00:00'
updated_at: '2019-04-02T10:01:15+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
when rejecting view key export, locking/unlocking the device is ending up with an error (few hours before that). In the mean time, no sync for the daemon and wallet.
The logs show:

2019-03-21 15:56:27.437	    7fb942188700	DEBUG	device.ledger	src/device/device_ledger.cpp:216	Ask for LOCKING for device Ledger in thread 
2019-03-21 15:56:27.437	    7fb9218e9700	DEBUG	device.ledger	src/device/device_ledger.cpp:260	CMD  : 02 32 00 00 41 006029751925d3e8fe55633b3c6eb53e194bbe439a3ac8b7b2f593dd98575f9e1a0000000000000000000000000000000000000000000000000000000000000000
2019-03-21 15:56:27.649	    7fb9218e9700	DEBUG	device.ledger	src/device/device_ledger.cpp:270	RESP : 9000 1654e6287de7461b45787fc6fb2d223610325ddd6c7fae7ec0626fe01a7f4e44
2019-03-21 15:56:27.649	    7fb9218e9700	DEBUG	device.ledger	src/device/device_ledger.cpp:236	Ask for UNLOCKING for device Ledger in thread 
2019-03-21 15:56:27.649	    7fb9218e9700	DEBUG	device.ledger	src/device/device_ledger.cpp:240	Device Ledger UNLOCKed
2019-03-21 15:56:27.649	    7fb9218e9700	DEBUG	device.ledger	src/device/device_ledger.cpp:216	Ask for LOCKING for device Ledger in thread 
2019-03-21 15:56:27.649	    7fb94943d700	DEBUG	device.ledger	src/device/device_ledger.cpp:218	Device Ledger LOCKed
2019-03-21 15:56:27.649	    7fb94943d700	DEBUG	device.ledger	src/device/device_ledger.cpp:260	CMD  : 02 32 00 00 41 003ed56cc25d1bdee187981e45282d848436cc17eae2fd2b0f0d61f6c77b7fe7760000000000000000000000000000000000000000000000000000000000000000
2019-03-21 15:56:27.861	    7fb94943d700	DEBUG	device.ledger	src/device/device_ledger.cpp:270	RESP : 9000 2843ccecb8d2023d71bc9dee95afc1fcf16a022ae2d1c3d322f6e366a0cc1b13
2019-03-21 15:56:27.861	    7fb94943d700	DEBUG	device.ledger	src/device/device_ledger.cpp:236	Ask for UNLOCKING for device Ledger in thread 
2019-03-21 15:56:27.861	    7fb94943d700	DEBUG	device.ledger	src/device/device_ledger.cpp:240	Device Ledger UNLOCKed
2019-03-21 15:56:27.861	    7fb94943d700	DEBUG	device.ledger	src/device/device_ledger.cpp:216	Ask for LOCKING for device Ledger in thread 
2019-03-21 15:56:27.861	    7fb948c3c700	DEBUG	device.ledger	src/device/device_ledger.cpp:218	Device Ledger LOCKed
2019-03-21 15:56:27.861	    7fb948c3c700	DEBUG	device.ledger	src/device/device_ledger.cpp:260	CMD  : 02 32 00 00 41 008b808ed8c56a4af57489850c638b70177f57f8b4638998c0734751d93570fae30000000000000000000000000000000000000000000000000000000000000000
2019-03-21 15:56:28.074	    7fb948c3c700	DEBUG	device.ledger	src/device/device_ledger.cpp:270	RESP : 9000 8968ad1349afb79ace535a9b401faa7f3f3ed199694f745996aed3695442cdba
2019-03-21 15:56:28.074	    7fb948c3c700	DEBUG	device.ledger	src/device/device_ledger.cpp:236	Ask for UNLOCKING for device Ledger in thread 
2019-03-21 15:56:28.074	    7fb948c3c700	DEBUG	device.ledger	src/device/device_ledger.cpp:240	Device Ledger UNLOCKed
2019-03-21 15:56:28.074	    7fb948c3c700	DEBUG	device.ledger	src/device/device_ledger.cpp:216	Ask for LOCKING for device Ledger in thread 
2019-03-21 15:56:28.074	    7fb922ced700	DEBUG	device.ledger	src/device/device_ledger.cpp:218	Device Ledger LOCKed
2019-03-21 15:56:28.074	    7fb922ced700	DEBUG	device.ledger	src/device/device_ledger.cpp:260	CMD  : 02 32 00 00 41 00ea87c840e0ff4448ea81083f8a2d83f8e5bc3bc8b5ce91bd153a7c6cbe2326260000000000000000000000000000000000000000000000000000000000000000
2019-03-21 15:56:28.287	    7fb922ced700	DEBUG	device.ledger	src/device/device_ledger.cpp:270	RESP : 9000 f12812095d46363cf20a2ee92195433d43c32de10279840

# Discussion History
## cslashm | 2019-04-02T10:01:15+00:00
I donot see the error i the log. Could you provide more details? 

# Action History
- Created by: roudaille | 2019-03-28T10:08:46+00:00
