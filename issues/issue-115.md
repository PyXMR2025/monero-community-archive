---
title: Class Group-based ZK SNARKs
source_url: https://github.com/monero-project/research-lab/issues/115
author: kayabaNerve
assignees: []
labels: []
created_at: '2024-01-17T19:48:24+00:00'
updated_at: '2024-09-09T08:58:45+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Class groups of unknown order have trustless setups, offer an elliptic-curve-esque API, yet are a couple orders of magnitude larger/slower (~2 KB elements for 128-bit security). They do not offer multiplicative inverses over the scalar field, and have a few interesting properties.

[Dew](https://eprint.iacr.org/2022/419) is a constant-sized logarithmic-time-to-verify ZK-SNARK based on class groups of unknown order.

[CL15](https://eprint.iacr.org/2015/047) additionally describes a way to create elements in a subgroup of an arbitrary prime, letting class groups be used for operations over existing fields used in elliptic curves, albeit with the discrete log problem being easy.

If we have a class group-based SNARK offering native arithmetic for Monero's elliptic curve, we'd have the option to feasibly use it. In practice, this will hammering a square peg into a round hole using class groups due to how much more expensive they are to compute over. If they fundamentally offer better complexity though, that may be a worthwhile trade off.

I'm personally more interested in ECC with a cycle. While there are no logarithmic-time-to-verify proofs for isolate programs, IVC proofs do exist which offer such performance when running the same program multiple times. That, combined with the overhead of class groups, likely makes ECC options the sane path forward.

# Discussion History
## narodnik | 2024-09-09T08:58:44+00:00
Class groups based off binary quadratic forms are secure. See the Chia project for an implementation. However they are close to RSA in performance.

Genus 3 hyperelliptic curves are much faster. Indeed genus 2 curves actually outperform normal EC. However there's debate on their security. https://asz.ink/2020/03/08/jacobians-of-hyperelliptic-curves/

# Action History
- Created by: kayabaNerve | 2024-01-17T19:48:24+00:00
