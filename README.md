# monero-community-archive
This project conducts structured archiving and daily automatic synchronization of Issues, Pull Requests, and Releases from the core repositories under [monero-project](https://github.com/monero-project), providing the Monero community with an offline-accessible, long-term preserved mirror of discussion and development records.(And it used on [Jackie's Repo](https://repo.openenet.cn))

## Project Description
This repository is used to archive non-code collaboration information from publicly available repositories under the monero-project organization, including but not limited to: requirement discussions, bug reports, PR reviews, version release notes, and incident handling records. All content is automatically captured via the GitHub API and saved in a standardized Markdown format. No original code is modified, and this project does not participate in code merging or development decision-making.

## Synchronization Scope
Synchronize all Issues, PRs, Releases, and complete records from the following repositories:
- [monero-project/monero](https://github.com/monero-project/monero)
- [monero-project/monero-docs](https://github.com/monero-project/monero-docs)
- [monero-project/monero-gui](https://github.com/monero-project/monero-gui)
- [monero-project/monero-site](https://github.com/monero-project/monero-site)
- [monero-project/meta](https://github.com/monero-project/meta)
- [monero-project/research-lab](https://github.com/monero-project/research-lab)

## Repository Structure
This repository uses **branches to correspond to source repositories**, with a unified structure within each branch:
```
├── issues/          # Complete Issue archive
├── pull_requests/   # PR discussion and handling records
└── releases/        # Version release information
```

Each entry is an independent MD file containing:
- YAML metadata: title, source URL, participants, status, timestamps, etc.
- Complete body description
- All comments and discussion records
- Opening/closing or merging and other handling history

## Synchronization Mechanism
- Automatic synchronization: Incremental updates are performed **every 3 days at 02:00 to 23:00 UTC**.
- Synchronization method: GitHub Actions + Python
- Update strategy: Only pull newly added or changed content while retaining historical versions

## Usage Instructions
1. Switch to the corresponding repository branch (e.g., monero, monero-gui)
2. Browse the corresponding MD files in the issues / pull_requests / releases directories
3. Supports local cloning, in-site search, and external referencing

## Data Source and Disclaimer
All data is obtained from GitHub's public APIs, and copyright belongs to the original authors and [monero-project](https://github.com/monero-project).
This project is solely for archiving and backup purposes and does not claim ownership of the original content.
If there is any infringement or a need to remove content, please submit an Issue for contact and handling.
