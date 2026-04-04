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

# ===================== Issue 同步（100%抓取） =====================
def sync_issues(repo_full_name: str):
    print(f"🔍 开始同步 {repo_full_name} Issues (所有状态)")
    source_repo = g.get_repo(repo_full_name)
    count = 0

    for issue in source_repo.get_issues(state="all"):
        # 精准过滤PR
        if hasattr(issue, 'pull_request') and issue.pull_request is not None:
            continue

        count += 1
        print(f"✅ 捕获Issue #{issue.number} | 状态: {issue.state}")
        
        fm = parse_github_object(issue)
        fm.update({
            "type": "issue",
            "status": issue.state,
            "closed_at": issue.closed_at.isoformat() if issue.closed_at else None
        })

        content = f"# 原始描述\n{issue.body or '无描述'}\n\n# 讨论记录\n"
        for comment in issue.get_comments():
            user = comment.user.login if comment.user else "deleted_user"
            time = comment.created_at.isoformat() if comment.created_at else "无时间"
            content += f"## {user} | {time}\n{comment.body or '无内容'}\n\n"

        content += "# 处理记录\n"
        content += f"- 创建者: {fm['author']} | {fm['created_at']}\n"
        if issue.state == "closed":
            content += f"- 关闭时间: {fm['closed_at']}\n"

        save_md(Path(f"issues/issue-{issue.number}.md"), fm, content)

    print(f"🎉 同步完成！共抓取纯 Issue: {count} 个\n")

# ===================== PR 同步 =====================
def sync_pull_requests(repo_full_name: str):
    print(f"🔍 开始同步 {repo_full_name} Pull Requests")
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

        content = f"# 原始描述\n{pr.body or '无描述'}\n\n# 讨论记录\n"
        for comment in pr.get_comments():
            user = comment.user.login if comment.user else "deleted_user"
            time = comment.created_at.isoformat() if comment.created_at else "无时间"
            content += f"## {user} | {time}\n{comment.body or '无内容'}\n\n"

        content += "# 处理记录\n"
        content += f"- 创建者: {fm['author']} | {fm['created_at']}\n"
        if pr.merged:
            content += f"- 合并时间: {fm['merged_at']}\n"
        elif pr.state == "closed":
            content += f"- 关闭时间: {fm['closed_at']}\n"

        save_md(Path(f"pull_requests/pr-{pr.number}.md"), fm, content)

    print(f"🎉 同步完成！共抓取 PR: {count} 个\n")

# ===================== Releases 同步 =====================
def sync_releases(repo_full_name: str):
    print(f"🔍 开始同步 {repo_full_name} Releases")
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
        content = f"# 版本: {release.tag_name}\n\n# 发布说明\n{release.body or '无说明'}"
        save_md(Path(f"releases/release-{safe_filename(release.tag_name)}.md"), fm, content)
    
    print(f"🎉 同步完成！共抓取 Release: {len(releases)} 个\n")

# ===================== 分支管理 =====================
def switch_branch(branch_name):
    try:
        repo.git.checkout(branch_name)
        repo.git.fetch("origin", branch_name)
    except:
        repo.git.checkout("-b", branch_name)
        print(f"🆕 创建分支: {branch_name}")

    # 强制创建README
    readme = Path("README.md")
    if not readme.exists():
        with open(readme, "w", encoding="utf-8") as f:
            f.write(f"# {branch_name}\n归档源: https://github.com/{repo_full_name}\n自动同步\n")

# ===================== 主函数（修复Git配置！） =====================
def main():
    # ✅ 修复核心错误：Git配置语法
    repo.config_writer().set_value("user", "name", "github-actions[bot]").release()
    repo.config_writer().set_value("user", "email", "github-actions[bot]@users.noreply.github.com").release()

    for repo_full_name in SOURCE_REPOS:
        branch = repo_full_name.split("/")[-1]
        print(f"\n========================================")
        print(f"同步仓库: {repo_full_name} -> 分支: {branch}")
        print(f"========================================\n")
        
        switch_branch(branch)
        sync_issues(repo_full_name)
        sync_pull_requests(repo_full_name)
        sync_releases(repo_full_name)
        
        # 提交推送
        repo.git.add(".")
        try:
            repo.index.commit(f"更新 {branch} | {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}")
            repo.git.push("--set-upstream", "origin", branch)
            print(f"✅ 推送成功: {branch}")
        except Exception as e:
            print(f"ℹ️ 数据已最新: {branch}")

if __name__ == "__main__":
    main()
