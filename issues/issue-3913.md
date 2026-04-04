---
title: Missing licenses of previous copyright holders
source_url: https://github.com/monero-project/monero/issues/3913
author: jonassmedegaard
assignees: []
labels: []
created_at: '2018-06-03T08:08:10+00:00'
updated_at: '2021-09-26T13:44:08+00:00'
type: issue
status: closed
closed_at: '2018-06-03T08:22:15+00:00'
---

# Original Description
Commit https://github.com/monero-project/monero/commit/6fc995f was described as "License updated to BSD 3-clause".

The change involved not only code authored as part of this project, but also code originating from external projects with different copyright holders.  The license issued by these different copyright holders did not include a permission to change license, and there seems to be no documentation of them granting this new license. On the contrary, one copyright holder contacted the project to point out this lack of permission to relicense, and the change was reverted - for that copyright holder only: #108

Example: src/simplewallet/simplewallet.cpp seems to originalte from https://github.com/cryptonotefoundation/cryptonote, licensed as MIT - a license which does not include permission to relicense as BSD-3-clause (but both licenses are permitted to co-exist).

I suspect the proper thing to do is to revive the original copyright and licensing header, effectively (not relicensing externally licensed code but instead only) _adding_ your new license for the parts of the code that you later contributed to those same files.

Alternatively, if you *did* get permission from the original authors to relicense their works, then I recommend that you document that - e.g. include verbatim an email from the original authors where they state their consent to that change of license for their code.

# Discussion History
## fluffypony | 2018-06-03T08:22:15+00:00
Not true; the MIT license is permissive and allows for relicensing to another permissive license. The copyright was maintained, as is appropriate, and the relicensing on Epee was reverted per that author’s request. The original authors are welcome to test the relicensibility of the MIT license in an appropriate forum.

## jonassmedegaard | 2018-06-03T08:24:57+00:00
The MIT explicitly requires that "The above copyright notice and this permission notice shall be included
 in all copies or substantial portions of the Software."

## jonassmedegaard | 2018-06-03T08:40:38+00:00
Seems I am not alone in my interpretation of the MIT license: https://opensource.stackexchange.com/questions/6838/how-to-properly-re-license-code-released-under-the-mit-license

## fluffypony | 2018-06-03T16:12:46+00:00
@jonassmedegaard you might entirely be right; on the other hand, since the BSD 3-clause license contains a compatible clause, the original agreement continues to be enforced, and neither the spirit nor the letter of the law is diminished. Ultimately, we're not lawyers, and there isn't much value in us not-lawyers wasting time revisiting a decision from half-a-decade ago. The original authors have had ample time to challenge the change, and as mentioned Epee's author did indeed challenge it in his code at the time it occurred.

Thus, given the seeming ambiguity, coupled with the fact that the original authors have not cared enough to raise an issue in many years, the appropriate forum for this to be tested is a court of law.

## jonassmedegaard | 2021-09-26T13:44:08+00:00
@fluffypony if you are not lawyers, then how do you reach the conclusion that a licensing requirement of "this permission notice shall be included" is satisfied by replacing it with another (arguably similarly intended but certainly differently worded) permission notice?

My (layman!) understanding of "compatible" licenses is that they contain no conflicting clauses and therefore can be used together - certainly not that the introduction of one compatible license is permitted to ignore an explicit clause of another compatible license.

I believe that by replacing the original license grant, you loose the permission to freely incorporate that code into yours.

Please add it back.

# Action History
- Created by: jonassmedegaard | 2018-06-03T08:08:10+00:00
- Closed at: 2018-06-03T08:22:15+00:00
