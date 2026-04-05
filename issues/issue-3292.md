---
title: Remove XMRig window when using embedded config.
source_url: https://github.com/xmrig/xmrig/issues/3292
author: LFL38
assignees: []
labels: []
created_at: '2023-06-27T19:22:04+00:00'
updated_at: '2025-06-18T22:46:56+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:46:56+00:00'
---

# Original Description
I was making a custom build of XMRig with VS and I was wondering if it is possible to remove the window that says this:
![image](https://github.com/xmrig/xmrig/assets/122199312/9e3da5e8-d0b6-4150-b2e4-e6b68c711d47)

I can remove the actual error codes by removing this part of code:
```
bool xmrig::JsonChain::addFile(const char *fileName)
{
    using namespace rapidjson;
    Document doc;
    if (Json::get(fileName, doc)) {
        m_fileName = fileName;

        return add(std::move(doc));
    }

    if (doc.HasParseError()) {
        const size_t offset = doc.GetErrorOffset();

        size_t line = 0;
        size_t pos  = 0;
        std::vector<std::string> s;

        if (Json::convertOffset(fileName, offset, line, pos, s)) {
            for (const auto& t : s) {
                LOG_ERR("%s", t.c_str());
            }

            std::string t;
            if (pos > 0) {
                t.assign(pos - 1, ' ');
            }
            t += '^';
            LOG_ERR("%s", t.c_str());

            LOG_ERR("%s<line:%zu, position:%zu>: \"%s\"", fileName, line, pos, GetParseError_En(doc.GetParseError()));
        }
        else {
            LOG_ERR("%s<offset:%zu>: \"%s\"", fileName, offset, GetParseError_En(doc.GetParseError()));
        }
    }
    else {
        LOG_ERR("unable to open \"%s\".", fileName);
    }

    return false;
}
```

But I can't actually remove the window that opens.

Thanks in advance!



# Discussion History
# Action History
- Created by: LFL38 | 2023-06-27T19:22:04+00:00
- Closed at: 2025-06-18T22:46:56+00:00
