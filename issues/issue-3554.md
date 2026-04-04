---
title: 'Feature request/discussion: historical price data'
source_url: https://github.com/monero-project/monero-gui/issues/3554
author: rating89us
assignees: []
labels: []
created_at: '2021-06-10T23:43:28+00:00'
updated_at: '2024-05-12T06:49:52+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Transactions page should display fiat conversion of past transactions using historical price data. To avoid compromising user privacy, we should not retrieve prices using an external API.

Therefore, I see two possible implementations:

**Option A**: save current XMR price on wallet cache every time a transaction is sent/received
- Easier to implement.
- Historical prices can be exported to other Monero (software) wallets.
- More precise. Current price can be updated just before saving a transaction on the wallet.
- Transactions sent/received before implementation of Option A will not have fiat price conversion (unless we also implement Option B).

**Option B**: import historical price data from an external source (like [this .csv file from Kraken](https://support.kraken.com/hc/en-us/articles/360047543791-Downloadable-historical-market-data-time-and-sales-))
- .csv file containing all XMRUSD trades of kraken (2017 until today) has ~80 MB.
- Requires an script to extract useful price information from this huge file. After selecting 2-3 price points for each day, I estimate it would have a size of less than 300 kB.
- How many price points will we use for each day? Should days with higher volatility have more price points? Should we use an average price for each day?
- Will this historical price data be small enough to be embedded in Monero GUI release? Or do we want extreme precision and offer the user to download 80 MB of data as an optional download?
- Will it only be updated on every GUI version release? Will an updated version of the .csv file be available between Monero GUI releases?

# Discussion History
## selsta | 2021-06-12T03:05:54+00:00
@tobtoht suggested me this API: https://www.coingecko.com/price_charts/monero/usd/max.json

This includes the price for every single day. We can approximate the price between two days depending on the time.

Also no more privacy issues than the normal API.

## smargold476 | 2023-04-18T09:01:53+00:00
I would really like to see that feature as by german law for example we need to know the € values for the time of each transaction.
It would be really useful for wider adoption of monero i guess.
I only see Option B as a real solution as we can avoid of a direct connection exposing the users activity. Maybe have an import-function to see the historical transactions on calculation based on imported csv-data like that file from kraken, i don't see the need to aggregate that, as the users just download and import it if necessary.

## kevcrumb | 2024-05-12T06:49:51+00:00
Price should not be a concern for official Monero releases.

The wallet already has `export_transfers`, so whoever is interested can go the other way around, get a CSV of transactions and then use whichever price data they want and make the necessary decisions like "average vs other" themselves.

# Action History
- Created by: rating89us | 2021-06-10T23:43:28+00:00
