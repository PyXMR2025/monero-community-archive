import os
import git
import yaml
from datetime import datetime
from github import Github, Auth
from pathlib import Path

# ===================== Config =====================
SOURCE_REPOS = [
    "Cuprate/cuprate"
]
GH_TOKEN3 = os.getenv("GH_TOKEN3")
TARGET_REPO = os.getenv("GITHUB_REPOSITORY")
# ==================================================

auth = Auth.Token(GH_TOKEN3)
g = Github(auth=auth)

repo = git.Repo(".")
origin = repo.remote("origin")
origin.set_url(f"https://{GH_TOKEN3}@github.com/{TARGET_REPO}.git")

def safe_filename(text: str) -> str:
    return text.replace("/", "_").replace("\\","_").replace(":","_").replace(" ","_")

def parse_github_object(obj):
    return {
        "title": obj.title,
        "source_url": obj.html_url,
        "author": obj.user.login if obj.user else "unknown",
        "assignees": [a.login for a in obj.assignees],
        "labels": [l.name for l in obj.labels],
        "created_at": obj.created_at.isoformat() if obj.created_at else None,
        "updated_at": obj.updated_at.isoformat() if obj.updated_at else None,
    }

def save_md(file_path: Path, frontmatter: dict, content: str):
    file_path.parent.mkdir(exist_ok=True, parents=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("---\n")
        yaml.dump(frontmatter, f, sort_keys=False, allow_unicode=True)
        f.write("---\n\n")
        f.write(content)

# ===================== Sync Issues =====================
def sync_issues(repo_full_name: str):
    print(f"🔍 Starting to sync Issues for {repo_full_name} (all states)")
    source_repo = g.get_repo(repo_full_name)
    count = 0

    for issue in source_repo.get_issues(state="all"):
        if hasattr(issue, 'pull_request') and issue.pull_request is not None:
            continue

        count += 1
        print(f"✅ Captured Issue #{issue.number} | Status: {issue.state}")
        
        fm = parse_github_object(issue)
        fm.update({
            "type": "issue",
            "status": issue.state,
            "closed_at": issue.closed_at.isoformat() if issue.closed_at else None
        })

        content = f"# Original Description\n{issue.body or 'No description'}\n\n# Discussion History\n"
        for comment in issue.get_comments():
            user = comment.user.login if comment.user else "deleted_user"
            time = comment.created_at.isoformat() if comment.created_at else "No time"
            content += f"## {user} | {time}\n{comment.body or 'No content'}\n\n"

        content += "# Action History\n"
        content += f"- Created by: {fm['author']} | {fm['created_at']}\n"
        if issue.state == "closed":
            content += f"- Closed at: {fm['closed_at']}\n"

        save_md(Path(f"issues/issue-{issue.number}.md"), fm, content)

    print(f"🎉 Sync completed! Total pure Issues captured: {count}\n")

# ===================== Sync Pull Requests =====================
def sync_pull_requests(repo_full_name: str):
    print(f"🔍 Starting to sync Pull Requests for {repo_full_name}")
    source_repo = g.get_repo(repo_full_name)
    count = 0

    for pr in source_repo.get_pulls(state="all"):
        count += 1
        fm = parse_github_object(pr)
        fm.update({
            "type": "pull_request",
            "status": "merged" if pr.merged else pr.state,
            "closed_at": pr.closed_at.isoformat() if pr.closed_at else None,
            "merged_at": pr.merged_at.isoformat() if pr.merged else None
        })

        content = f"# Original Description\n{pr.body or 'No description'}\n\n# Discussion History\n"
        for comment in pr.get_comments():
            user = comment.user.login if comment.user else "deleted_user"
            time = comment.created_at.isoformat() if comment.created_at else "No time"
            content += f"## {user} | {time}\n{comment.body or 'No content'}\n\n"

        content += "# Action History\n"
        content += f"- Created by: {fm['author']} | {fm['created_at']}\n"
        if pr.merged:
            content += f"- Merged at: {fm['merged_at']}\n"
        elif pr.state == "closed":
            content += f"- Closed at: {fm['closed_at']}\n"

        save_md(Path(f"pull_requests/pr-{pr.number}.md"), fm, content)

    print(f"🎉 Sync completed! Total PRs captured: {count}\n")

# ===================== Sync Releases =====================
def sync_releases(repo_full_name: str):
    print(f"🔍 Starting to sync Releases for {repo_full_name}")
    source_repo = g.get_repo(repo_full_name)
    releases = list(source_repo.get_releases())
    
    for release in releases:
        fm = {
            "title": release.title or release.tag_name,
            "type": "release",
            "source_url": release.html_url,
            "author": release.author.login if release.author else "unknown",
            "tag_name": release.tag_name,
            "published_at": release.published_at.isoformat() if release.published_at else None
        }
        content = f"# Version: {release.tag_name}\n\n# Release Notes\n{release.body or 'No notes'}"
        save_md(Path(f"releases/release-{safe_filename(release.tag_name)}.md"), fm, content)
    
    print(f"🎉 Sync completed! Total Releases captured: {len(releases)}\n")

# ===================== Branch Management =====================
def switch_branch(branch_name):
    try:
        repo.git.checkout(branch_name)
        repo.git.fetch("origin", branch_name)
    except:
        repo.git.checkout("-b", branch_name)
        print(f"🆕 Created branch: {branch_name}")

    readme = Path("README.md")
    if not readme.exists():
        with open(readme, "w", encoding="utf-8") as f:
            f.write(f"# {branch_name}\nArchive Source: https://github.com/{repo_full_name}\nAuto Sync\n")

# ===================== Main Function =====================
def main():
    repo.config_writer().set_value("user", "name", "github-actions[bot]").release()
    repo.config_writer().set_value("user", "email", "github-actions[bot]@users.noreply.github.com").release()

    for repo_full_name in SOURCE_REPOS:
        branch = repo_full_name.split("/")[-1]
        print(f"\n========================================")
        print(f"Syncing repo: {repo_full_name} -> Branch: {branch}")
        print(f"========================================\n")
        
        switch_branch(branch)
        sync_issues(repo_full_name)
        sync_pull_requests(repo_full_name)
        sync_releases(repo_full_name)
        
        repo.git.add(".")
        try:
            repo.index.commit(f"Update {branch} | {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}")
            repo.git.push("--set-upstream", "origin", branch)
            print(f"✅ Push successful: {branch}")
        except Exception as e:
            print(f"ℹ️ Data is already up to date: {branch}")

if __name__ == "__main__":
    main()
