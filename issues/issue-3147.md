---
title: 'Add locked_sweep_all command '
source_url: https://github.com/monero-project/monero/issues/3147
author: dEBRUYNE-1
assignees: []
labels:
- proposal
- easy
created_at: '2018-01-17T15:05:26+00:00'
updated_at: '2024-09-22T05:44:03+00:00'
type: issue
status: closed
closed_at: '2018-10-12T20:40:57+00:00'
---

# Original Description
The current `locked_transfer` command will lock the change as well, i.e.,` locked_transfer` is per-transaction instead of per-output. We can't use per-output, because, if I recall correctly, it would be visible to an observer which output is locked and therefore also which output is the change. This, obviously, is detrimental to privacy. 

Now, to lock a certain amount of XMR, the best way would be to send the amount you want to lock from wallet A to wallet B (w/ subaddresses implemented this could be Account 0 -> Account 1 as well) using the generic `transfer` command. Subsequently, perform a `locked_sweep_all` back to wallet A. By using this method, only that output (and thus the amount you want to lock) will be locked.

In sum, I propose to add a new `locked_sweep_all` command. 

# Discussion History
## dEBRUYNE-1 | 2018-01-17T15:05:38+00:00
+proposal

## dEBRUYNE-1 | 2018-01-17T17:08:45+00:00
+easy

## moneromooo-monero | 2018-10-12T20:32:50+00:00
+resolved

## xmrrmxntom | 2024-09-22T05:44:02+00:00
@dEBRUYNE-1 @Cactii1 

<h1>A Plea to Restore a Crucial Feature in XMR</h1>
<p>As a computer science student and a long-time follower of XMR & Dr. Daniel Kim (sweetwater.consulting), I'm compelled to share my thoughts on a feature that I believe is <strong>important</strong> to the value proposition of XMR. I've created an account specifically to express my disappointment and frustration with the removal of the <code>locked_transfers</code> and <code>locked_sweep_all</code> feature.</p>
<h2>A Personal Journey with XMR</h2>
<p>I've been following the XMR project since 2018, and its value proposition was evident to me even back then. However, I wasn't technical enough to fully appreciate its features. This year, I became proficient enough to run a full node and use the CLI, which is when I discovered the <code>locked_transfers</code> and <code>locked_sweep_all</code> features. I immediately utilized them, and they have been <strong>invaluable</strong> to me.</p>
<p>As someone who has impulsively sold assets like NVIDIA, BTC, and TSLA before they reached their full potential, I've come to realize that XMR is a <strong>long-term play</strong> that will appreciate in value over the next 5-20 years. The ability to lock transactions for an extended period has been a <strong>game-changer</strong> for me, allowing me to make sacrifices that my future self will appreciate.</p>
<h2>The Value of Locked Transactions</h2>
<p>The <code>locked_transfers</code> and <code>locked_sweep_all</code> feature was a <strong>unique selling point</strong> for XMR, offering me the ability to make long-term commitments to the blockchain. By removing this feature, we're depriving users of a valuable tool that would help them appreciate the embedded on-chain hodl properties of the XMR blockchain.</p>
<h2>A Call to Action</h2>
<p>I urge the XMR community to reconsider the removal of this feature and to implement safeguards to prevent similar decisions in the future. Specifically, I request:</p>
<ol>
<li><strong>Reinstatement of the feature</strong>: Bring back the <code>locked_transfers</code> and <code>locked_sweep_all</code> feature to allow users to make long-term commitments to the blockchain.</li>
<li><strong>Safeguards for feature deprecation</strong>: Establish a formal, non-trivial process or procedure to determine whether a feature should be deprecated, ensuring that user feedback and concerns are taken into account and valued.</li>
<li><strong>Improvement or alternative</strong>: If the feature cannot be reinstated, explore alternative solutions that would provide similar functionality and benefits to users.</li>
</ol>
<h2>Conclusion</h2>
<p>As more users join the XMR community, they will come to appreciate the unique properties of the blockchain. I firmly believe that the <code>locked_transfers</code> and <code>locked_sweep_all</code> feature helps users <strong>HODL</strong> with the long-term success of XMR. I hope that my plea will be heard, and we can work together to restore this important feature.</p>
<h2>A Final Appeal</h2>
<p>I've gone from hearing about XMR as the real <strong>privacy-focused vision</strong> of BTC, to buying some XMR on an exchange, to self-custodying on Exodus wallet, and finally to downloading and running the CLI. XMR is <strong>beautiful</strong>, and it's <strong>idealistic</strong>. Please keep or reimplement this feature.</p>

https://reddit.com/r/Monero/comments/mwrm6g/how_to_lock_send_future_monero_to_yourself_with/

<p>This was the post and feature that motivated me to dedicate a weekend last semester to read the documentation, compile from source, and use the CLI.</p>
<p>…Please keep this feature…</p>

# Action History
- Created by: dEBRUYNE-1 | 2018-01-17T15:05:26+00:00
- Closed at: 2018-10-12T20:40:57+00:00
