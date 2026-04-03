import os
import git
import yaml
from datetime import datetime
from github import Github
from pathlib import Path

TARGET_REPO = "PyXMR2025/monero-community-archive"
SOURCE_REPOS = [
    "monero-project/monero",
    "monero-project/monero-docs",
    "monero-project/monero-gui",
    "monero-project/monero-site",
    "monero-project/meta",
    "monero-project/research-lab"
]
GH_TOKEN = os.getenv("GH_TOKEN")

g = Github(GH_TOKEN)
repo = git.Repo(".")
origin = repo.remote("origin")

def safe_filename(text: str) -> str:
    """生成安全的文件名"""
    return text.replace("/", "_").replace("\\", "_").replace(":", "_").replace(" ", "_")

def parse_github_object(obj):
    """提取Issue/PR通用元数据"""
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
    """保存MD文件（YAML头+正文）"""
    file_path.parent.mkdir(exist_ok=True, parents=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("---\n")
        yaml.dump(frontmatter, f, sort_keys=False, allow_unicode=True)
        f.write("---\n\n")
        f.write(content)

def sync_issues(repo_full_name: str, branch_name: str):
    """同步Issue"""
    print(f"同步 {repo_full_name} Issues...")
    source_repo = g.get_repo(repo_full_name)
    save_dir = Path("issues")
    
    for issue in source_repo.get_issues(state="all"):
        if hasattr(issue, "pull_request"):
            continue
            
        fm = parse_github_object(issue)
        fm["type"] = "issue"
        fm["status"] = issue.state
        fm["closed_at"] = issue.closed_at.isoformat() if issue.closed_at else None
        
        content = f"# 原始描述\n{issue.body or '无描述'}\n\n# 讨论记录\n"
        for comment in issue.get_comments():
            time_str = comment.created_at.isoformat()
            content += f"## {comment.user.login} | {time_str}\n{comment.body or '无内容'}\n\n"
        content += "# 处理记录\n"
        content += f"- {issue.user.login} opened this issue on {fm['created_at']}\n"
        if issue.state == "closed":
            content += f"- 关闭时间: {fm['closed_at']}\n"
        
        file_path = save_dir / f"issue-{issue.number}.md"
        save_md(file_path, fm, content)

def sync_pull_requests(repo_full_name: str, branch_name: str):
    """同步PR"""
    print(f"同步 {repo_full_name} Pull Requests...")
    source_repo = g.get_repo(repo_full_name)
    save_dir = Path("pull_requests")
    
    for pr in source_repo.get_pulls(state="all"):
        fm = parse_github_object(pr)
        fm["type"] = "pull_request"
        fm["status"] = "merged" if pr.merged else pr.state
        fm["closed_at"] = pr.closed_at.isoformat() if pr.closed_at else None
        fm["merged_at"] = pr.merged_at.isoformat() if pr.merged_at else None
        
        content = f"# 原始描述\n{pr.body or '无描述'}\n\n# 讨论记录\n"
        for comment in pr.get_comments():
            time_str = comment.created_at.isoformat()
            content += f"## {comment.user.login} | {time_str}\n{comment.body or '无内容'}\n\n"
        content += "# 处理记录\n"
        content += f"- {pr.user.login} opened this PR on {fm['created_at']}\n"
        if pr.merged:
            content += f"- 合并时间: {fm['merged_at']}\n"
        elif pr.state == "closed":
            content += f"- 关闭时间: {fm['closed_at']}\n"
        
        file_path = save_dir / f"pr-{pr.number}.md"
        save_md(file_path, fm, content)

def sync_releases(repo_full_name: str, branch_name: str):
    """同步Releases"""
    print(f"同步 {repo_full_name} Releases...")
    source_repo = g.get_repo(repo_full_name)
    save_dir = Path("releases")
    
    for release in source_repo.get_releases():
        fm = {
            "title": release.title or release.tag_name,
            "type": "release",
            "source_url": release.html_url,
            "author": release.author.login if release.author else "unknown",
            "tag_name": release.tag_name,
            "created_at": release.created_at.isoformat() if release.created_at else None,
            "published_at": release.published_at.isoformat() if release.published_at else None,
        }
        
        content = f"# 版本信息\n标签: {release.tag_name}\n\n# 发布说明\n{release.body or '无说明'}"
        
        file_path = save_dir / f"release-{safe_filename(release.tag_name)}.md"
        save_md(file_path, fm, content)

def switch_branch(branch_name: str):
    """切换到对应分支，不存在则创建"""
    if branch_name in repo.branches:
        repo.git.checkout(branch_name)
    else:
        repo.git.checkout("-b", branch_name)
    origin.pull(branch_name)

def main():
    repo.config_writer().set_value("user", "name", "github-actions[bot]").release()
    repo.config_writer().set_value("user", "email", "github-actions[bot]@users.noreply.github.com").release()
    
    for repo_full_name in SOURCE_REPOS:
        branch_name = repo_full_name.split("/")[-1]
        print(f"\n===== 开始同步 {repo_full_name} → 分支 {branch_name} =====")
        
        switch_branch(branch_name)
        
        sync_issues(repo_full_name, branch_name)
        sync_pull_requests(repo_full_name, branch_name)
        sync_releases(repo_full_name, branch_name)
        
        if repo.is_dirty():
            repo.git.add(".")
            repo.index.commit(f"同步 {repo_full_name} 数据 | {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}")
            origin.push(branch_name)
            print(f"✅ 推送 {branch_name} 分支成功")
        else:
            print(f"ℹ️ {branch_name} 分支无变更，无需推送")

if __name__ == "__main__":
    main()