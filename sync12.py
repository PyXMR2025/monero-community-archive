import os
import git
import yaml
from datetime import datetime
from pathlib import Path
import gitlab

# ===================== Config =====================
SOURCE_REPOS = [
    "monero-project/ccs-proposals"
]
GITLAB_TOKEN = os.getenv("GITLAB_TOKEN")
GITLAB_URL = "https://repo.getmonero.org"
TARGET_REPO = os.getenv("GITHUB_REPOSITORY")
# ==================================================

gl = gitlab.Gitlab(GITLAB_URL, private_token=GITLAB_TOKEN)

repo = git.Repo(".")
origin = repo.remote("origin")
origin.set_url(f"https://{os.getenv('GH_TOKEN3')}@github.com/{TARGET_REPO}.git")

def safe_filename(text: str) -> str:
    return text.replace("/", "_").replace("\\","_").replace(":","_").replace(" ","_")

def parse_gitlab_object(obj):
    return {
        "title": obj.title,
        "source_url": obj.web_url, 
        "author": obj.author["username"] if hasattr(obj, "author") else "unknown",  
        "assignees": [a["username"] for a in obj.assignees] if obj.assignees else [],
        "labels": obj.labels or [],
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
    source_project = gl.projects.get(repo_full_name)
    count = 0

    for issue in source_project.issues.list(all=True, state="all"):
        count += 1
        print(f"✅ Captured Issue #{issue.iid} | Status: {issue.state}")
        
        fm = parse_gitlab_object(issue)
        fm.update({
            "type": "issue",
            "status": issue.state,
            "closed_at": issue.closed_at.isoformat() if issue.closed_at else None
        })

        content = f"# Original Description\n{issue.description or 'No description'}\n\n# Discussion History\n"
        for comment in issue.notes.list(all=True):
            user = comment.author["username"] if hasattr(comment, "author") else "deleted_user"
            time = comment.created_at.isoformat() if comment.created_at else "No time"
            content += f"## {user} | {time}\n{comment.body or 'No content'}\n\n"

        content += "# Action History\n"
        content += f"- Created by: {fm['author']} | {fm['created_at']}\n"
        if issue.state == "closed":
            content += f"- Closed at: {fm['closed_at']}\n"

        save_md(Path(f"issues/issue-{issue.iid}.md"), fm, content)

    print(f"🎉 Sync completed! Total pure Issues captured: {count}\n")

# ===================== Sync Merge Requests =====================
def sync_merge_requests(repo_full_name: str):
    print(f"🔍 Starting to sync Merge Requests for {repo_full_name}")
    source_project = gl.projects.get(repo_full_name)
    count = 0

    for mr in source_project.mergerequests.list(all=True, state="all"):
        count += 1
        fm = parse_gitlab_object(mr)
        fm.update({
            "type": "merge_request", 
            "status": "merged" if mr.state == "merged" else mr.state,
            "closed_at": mr.closed_at.isoformat() if mr.closed_at else None,
            "merged_at": mr.merged_at.isoformat() if mr.merged_at else None
        })

        content = f"# Original Description\n{mr.description or 'No description'}\n\n# Discussion History\n"
        for comment in mr.notes.list(all=True):
            user = comment.author["username"] if hasattr(comment, "author") else "deleted_user"
            time = comment.created_at.isoformat() if comment.created_at else "No time"
            content += f"## {user} | {time}\n{comment.body or 'No content'}\n\n"

        content += "# Action History\n"
        content += f"- Created by: {fm['author']} | {fm['created_at']}\n"
        if mr.state == "merged":
            content += f"- Merged at: {fm['merged_at']}\n"
        elif mr.state == "closed":
            content += f"- Closed at: {fm['closed_at']}\n"

        save_md(Path(f"merge_requests/mr-{mr.iid}.md"), fm, content)

    print(f"🎉 Sync completed! Total Merge Requests captured: {count}\n")

# ===================== Sync Releases =====================
def sync_releases(repo_full_name: str):
    print(f"🔍 Starting to sync Releases for {repo_full_name}")
    source_project = gl.projects.get(repo_full_name)
    releases = source_project.releases.list(all=True)
    
    for release in releases:
        fm = {
            "title": release.name or release.tag_name,
            "type": "release",
            "source_url": release._links["self"],  
            "author": release.author["username"] if hasattr(release, "author") else "unknown",
            "tag_name": release.tag_name,
            "published_at": release.released_at.isoformat() if release.released_at else None
        }
        content = f"# Version: {release.tag_name}\n\n# Release Notes\n{release.description or 'No notes'}"
        save_md(Path(f"releases/release-{safe_filename(release.tag_name)}.md"), fm, content)
    
    print(f"🎉 Sync completed! Total Releases captured: {len(releases)}\n")

# ===================== Branch Management =====================
def switch_branch(branch_name, repo_full_name):
    try:
        repo.git.checkout(branch_name)
        repo.git.fetch("origin", branch_name)
    except:
        repo.git.checkout("-b", branch_name)
        print(f"🆕 Created branch: {branch_name}")

    readme = Path("README.md")
    if not readme.exists():
        with open(readme, "w", encoding="utf-8") as f:
            f.write(f"# {branch_name}\nArchive Source: https://repo.getmonero.org/{repo_full_name}\nAuto Sync\n")

# ===================== Main Function =====================
def main():
    repo.config_writer().set_value("user", "name", "github-actions[bot]").release()
    repo.config_writer().set_value("user", "email", "github-actions[bot]@users.noreply.github.com").release()

    for repo_full_name in SOURCE_REPOS:
        branch = repo_full_name.split("/")[-1]
        print(f"\n========================================")
        print(f"Syncing GitLab repo: {repo_full_name} -> Branch: {branch}")
        print(f"========================================\n")
        
        switch_branch(branch, repo_full_name)
        sync_issues(repo_full_name)
        sync_merge_requests(repo_full_name)
        sync_releases(repo_full_name)
        
        repo.git.add(".")
        try:
            commit_msg = f"Update {branch} | {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}"
            repo.index.commit(commit_msg)
            repo.git.push("--set-upstream", "origin", branch)
            print(f"✅ Push successful: {branch}")
        except Exception as e:
            print(f"ℹ️ Data is already up to date: {branch}")

if __name__ == "__main__":
    main()