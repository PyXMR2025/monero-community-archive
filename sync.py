import os
import git
import yaml
from datetime import datetime
from github import Github, Auth, GithubException
from pathlib import Path
import time

# ===================== Config =====================
# 1. 源仓库列表（不变）
SOURCE_REPOS = [
    "PyXMR2025/blog"
]

# 2. TOKEN配置（兼容单/双TOKEN，解决环境变量报错）
GH_TOKEN = os.getenv("GH_TOKEN")
GH_TOKEN1 = os.getenv("GH_TOKEN1")
GH_TOKEN2 = os.getenv("GH_TOKEN2")

# 3. 固定目标仓库（关键修改！直接修改这里固定仓库）
FIXED_TARGET_REPO = "PyXMR2025/monero-community-archive"  # 你的固定目标仓库
# 优先级：环境变量 > 固定值（方便CI环境覆盖）
TARGET_REPO = os.getenv("GITHUB_REPOSITORY", FIXED_TARGET_REPO)
# ==================================================

# ===================== TOKEN 自动轮询管理器 =====================
TOKENS = []
# 自动加载可用TOKEN
if GH_TOKEN1 and GH_TOKEN2:
    TOKENS = [GH_TOKEN1, GH_TOKEN2]
elif GH_TOKEN:
    TOKENS = [GH_TOKEN]
else:
    raise ValueError("错误：请配置至少一个GitHub Token（GH_TOKEN 或 GH_TOKEN1+GH_TOKEN2）")

current_token_idx = 0
request_count = 0
# GitHub Token 每小时限额5000，设置4800自动切换（留缓冲）
RATE_LIMIT_BUFFER = 4800

def get_current_token() -> str:
    """获取当前活跃TOKEN"""
    return TOKENS[current_token_idx]

def switch_token() -> None:
    """自动切换下一个TOKEN（支持单/双TOKEN）"""
    global current_token_idx, request_count
    if len(TOKENS) == 1:
        print("⚠️ 仅配置单个TOKEN，无法切换，等待10秒后重试...")
        time.sleep(10)
        return
    # 切换TOKEN + 重置请求计数
    current_token_idx = (current_token_idx + 1) % len(TOKENS)
    request_count = 0
    print(f"🔄 自动切换TOKEN → 第 {current_token_idx + 1} 个")

def get_github_client() -> Github:
    """创建API客户端（统一入口，自动使用当前TOKEN）"""
    global request_count
    request_count += 1
    # 请求数达标，提前切换TOKEN
    if request_count >= RATE_LIMIT_BUFFER:
        print(f"📊 请求数达到{RATE_LIMIT_BUFFER}，自动切换TOKEN...")
        switch_token()
    return Github(auth=Auth.Token(get_current_token()))

def mask_token(token: str) -> str:
    """TOKEN脱敏"""
    return token[:4] + "****" + token[-4:] if len(token) > 8 else "****"
# ============================================================

# 初始化Git
repo = git.Repo(".")
origin = repo.remote("origin")

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

# ===================== 带自动重试/切TOKEN的同步函数 =====================
def fetch_with_retry(func, *args, **kwargs):
    """自动捕获API限制，切TOKEN并重试"""
    try:
        return func(*args, **kwargs)
    except GithubException as e:
        # 捕获GitHub速率限制错误
        if e.status == 403 and "rate limit" in str(e).lower():
            print(f"🚨 触发API速率限制！{e.data.get('message', '')}")
            switch_token()
            return func(*args, **kwargs)
        else:
            raise e

# ===================== Sync Issues =====================
def sync_issues(repo_full_name: str):
    print(f"🔍 Starting to sync Issues for {repo_full_name} (all states)")
    g = get_github_client()
    source_repo = fetch_with_retry(g.get_repo, repo_full_name)
    count = 0

    issues = fetch_with_retry(source_repo.get_issues, state="all")
    for issue in issues:
        # 跳过PR
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
        comments = fetch_with_retry(issue.get_comments)
        for comment in comments:
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
    g = get_github_client()
    source_repo = fetch_with_retry(g.get_repo, repo_full_name)
    count = 0

    pulls = fetch_with_retry(source_repo.get_pulls, state="all")
    for pr in pulls:
        count += 1
        fm = parse_github_object(pr)
        fm.update({
            "type": "pull_request",
            "status": "merged" if pr.merged else pr.state,
            "closed_at": pr.closed_at.isoformat() if pr.closed_at else None,
            "merged_at": pr.merged_at.isoformat() if pr.merged else None
        })

        content = f"# Original Description\n{pr.body or 'No description'}\n\n# Discussion History\n"
        comments = fetch_with_retry(pr.get_comments)
        for comment in comments:
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
    g = get_github_client()
    source_repo = fetch_with_retry(g.get_repo, repo_full_name)
    releases = fetch_with_retry(source_repo.get_releases)
    
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
def switch_branch(branch_name: str, repo_full_name: str):
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
    # Git配置
    repo.config_writer().set_value("user", "name", "github-actions[bot]").release()
    repo.config_writer().set_value("user", "email", "github-actions[bot]@users.noreply.github.com").release()

    print(f"🎯 目标仓库已固定: {TARGET_REPO}")  # 显示当前目标仓库

    for repo_full_name in SOURCE_REPOS:
        branch = repo_full_name.split("/")[-1]
        print(f"\n========================================")
        print(f"Syncing repo: {repo_full_name} -> Branch: {branch}")
        print(f"当前TOKEN: {mask_token(get_current_token())} | 可用TOKEN数: {len(TOKENS)}")
        print(f"========================================\n")
        
        # Git推送使用当前TOKEN
        origin.set_url(f"https://{get_current_token()}@github.com/{TARGET_REPO}.git")
        switch_branch(branch, repo_full_name)
        
        # 同步数据（自动切TOKEN）
        sync_issues(repo_full_name)
        sync_pull_requests(repo_full_name)
        sync_releases(repo_full_name)
        
        # 提交推送
        repo.git.add(".")
        try:
            repo.index.commit(f"Update {branch} | {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}")
            repo.git.push("--set-upstream", "origin", branch)
            print(f"✅ Push successful: {branch}")
        except Exception as e:
            print(f"ℹ️ Data is already up to date: {branch}")

if __name__ == "__main__":
    main()
