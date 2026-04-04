import os
import git
import yaml
from datetime import datetime
from github import Github, Auth
from pathlib import Path

# ===================== 配置项 =====================
SOURCE_REPOS = [
    "PyXMR2025/blog"
]
GH_TOKEN = os.getenv("GH_TOKEN")
TARGET_REPO = os.getenv("GITHUB_REPOSITORY")
# ==================================================

# 认证
auth = Auth.Token(GH_TOKEN)
g = Github(auth=auth)

# Git 初始化
repo = git.Repo(".")
origin = repo.remote("origin")
origin.set_url(f"https://{GH_TOKEN}@github.com/{TARGET_REPO}.git")

# 工具函数
def safe_filename(text: str) -> str:
    return text.replace("/", "_").replace("\\", "_").replace(":", "_").replace(" ", "_")

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
    file_path = Path.cwd() / file_path
    file_path.parent.mkdir(exist_ok=True, parents=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("---\n")
        yaml.dump(frontmatter, f, sort_keys=False, allow_unicode=True)
        f.write("---\n\n")
        f.write(content)

# ===================== 修复：Issue 同步（无无效参数） =====================
def sync_issues(repo_full_name: str):
    print(f"🔍 同步 {repo_full_name} Issues...")
    source_repo = g.get_repo(repo_full_name)
    
    # ✅ 修复：删除错误参数 type="issue"，GitHub API 不支持！
    issues = list(source_repo.get_issues(state="all"))
    print(f"✅ 找到 {len(issues)} 个 Issue/PR 总数")
    
    count = 0
    for issue in issues:
        # ✅ 官方正确方式：过滤 PR，只保留纯 Issue
        if hasattr(issue, "pull_request"):
            continue
            
        count += 1
        fm = parse_github_object(issue)
        fm["type"] = "issue"
        fm["status"] = issue.state
        fm["closed_at"] = issue.closed_at.isoformat() if issue.closed_at else None
        
        content = f"# 原始描述\n{issue.body or '无描述'}\n\n# 讨论记录\n"
        for comment in issue.get_comments():
            time_str = comment.created_at.isoformat() if comment.created_at else ""
            comment_user = comment.user.login if comment.user else "deleted_user"
            content += f"## {comment_user} | {time_str}\n{comment.body or '无内容'}\n\n"
        
        content += "# 处理记录\n"
        content += f"- {fm['author']} 创建于 {fm['created_at']}\n"
        if issue.state == "closed":
            content += f"- 关闭于 {fm['closed_at']}\n"
        
        save_md(Path(f"issues/issue-{issue.number}.md"), fm, content)
        print(f"📄 已生成 Issue 文件: issue-{issue.number}.md ({issue.state})")
    print(f"✅ 最终同步纯 Issue 数量: {count}")

# ===================== PR 同步（正常） =====================
def sync_pull_requests(repo_full_name: str):
    print(f"🔍 同步 {repo_full_name} Pull Requests...")
    source_repo = g.get_repo(repo_full_name)
    prs = list(source_repo.get_pulls(state="all"))
    print(f"✅ 找到 {len(prs)} 个 PR")
    
    for pr in prs:
        fm = parse_github_object(pr)
        fm["type"] = "pull_request"
        fm["status"] = "merged" if pr.merged else pr.state
        fm["closed_at"] = pr.closed_at.isoformat() if pr.closed_at else None
        fm["merged_at"] = pr.merged_at.isoformat() if pr.merged else None
        
        content = f"# 原始描述\n{pr.body or '无描述'}\n\n# 讨论记录\n"
        for comment in pr.get_comments():
            time_str = comment.created_at.isoformat() if comment.created_at else ""
            comment_user = comment.user.login if comment.user else "deleted_user"
            content += f"## {comment_user} | {time_str}\n{comment.body or '无内容'}\n\n"
        
        content += "# 处理记录\n"
        content += f"- {fm['author']} 创建于 {fm['created_at']}\n"
        if pr.merged:
            content += f"- 合并于 {fm['merged_at']}\n"
        elif pr.state == "closed":
            content += f"- 关闭于 {fm['closed_at']}\n"
        
        save_md(Path(f"pull_requests/pr-{pr.number}.md"), fm, content)
        print(f"📄 生成 PR 文件: pr-{pr.number}.md")

# ===================== Releases 同步（修复笔误） =====================
def sync_releases(repo_full_name: str):
    print(f"🔍 同步 {repo_full_name} Releases...")
    source_repo = g.get_repo(repo_full_name)
    releases = list(source_repo.get_releases())
    print(f"✅ 找到 {len(releases)} 个 Release")
    
    for release in releases:
        release_author = release.author.login if release.author else "unknown"
        fm = {
            "title": release.title or release.tag_name,
            "type": "release",
            "source_url": release.html_url,
            "author": release_author,
            "tag_name": release.tag_name,
            "created_at": release.created_at.isoformat() if release.created_at else None,
            "published_at": release.published_at.isoformat() if release.published_at else None,
        }
        content = f"# 版本信息\n标签: {release.tag_name}\n\n# 发布说明\n{release.body or '无说明'}"
        save_md(Path(f"releases/release-{safe_filename(release.tag_name)}.md"), fm, content)

# ===================== 分支创建（正常） =====================
def switch_branch(branch_name: str):
    try:
        repo.git.checkout(branch_name)
        repo.git.fetch("origin", branch_name)
    except git.GitCommandError:
        repo.git.checkout("-b", branch_name)
        print(f"🆕 创建分支: {branch_name}")
    
    # 强制创建README保证分支推送
    readme = Path.cwd() / "README.md"
    if not readme.exists():
        with open(readme, "w", encoding="utf-8") as f:
            f.write(f"# {branch_name}\n归档仓库: https://github.com/{repo_full_name}\n自动同步时间: {datetime.utcnow()} UTC\n")

# ===================== 主函数 =====================
def main():
    repo.config_writer().set_value("user", "name", "github-actions[bot]").release()
    repo.config_writer().set_value("user", "email", "github-actions[bot]@users.noreply.github.com").release()

    for repo_full_name in SOURCE_REPOS:
        branch_name = repo_full_name.split("/")[-1]
        print(f"\n===== 开始同步 {repo_full_name} → 分支 {branch_name} =====")
        
        switch_branch(branch_name)
        sync_issues(repo_full_name)
        sync_pull_requests(repo_full_name)
        sync_releases(repo_full_name)
        
        # 强制提交推送
        repo.git.add("-A")
        try:
            repo.index.commit(f"同步 {repo_full_name} 数据 | {datetime.utcnow()} UTC")
            repo.git.push("--set-upstream", "origin", branch_name)
            print(f"✅ 成功推送分支: {branch_name}")
        except Exception as e:
            print(f"ℹ️ 无需更新: {str(e)}")

if __name__ == "__main__":
    main()
