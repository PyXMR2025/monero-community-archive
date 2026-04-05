---
title: Memory 512bit alignment
source_url: https://github.com/xmrig/xmrig/issues/2546
author: ghost
assignees: []
labels: []
created_at: '2021-08-18T21:18:59+00:00'
updated_at: '2021-08-18T21:18:59+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
xmrig::VirtualMemory::VirtualMemory(size_t size, bool hugePages, bool oneGbPages, bool usePool, uint32_t node, size_t alignSize) :
    m_size(alignToHugePageSize(size)),
    m_node(node),
    m_capacity(m_size)
{
...
m_scratchpad = static_cast<uint8_t*>(_mm_malloc(m_size, alignSize));
}

alignSize = 512bit ? Because aligns memory to 512bit and 256bit and 128bit and 64bit and 32bit and ...  

# Discussion History
# Action History
- Created by: ghost | 2021-08-18T21:18:59+00:00
