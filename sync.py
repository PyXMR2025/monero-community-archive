import os
import git
import yaml
from datetime import datetime
from github import Github, Auth
from pathlib import Path

# ===================== 配置项 =====================
# 目标归档仓库（你的GitHub用户名/仓库名）
TARGET_REPO = os.getenv("GITHUB_REPOSITORY")
# 需要同步的源仓库列表
SOURCE_REPOS = [
    "PyXMR2025/blog"
]
# GitHub令牌（从环境变量读取，由Actions自动注入）
GH_TOKEN = os.getenv("GH_TOKEN")
# ==================================================

# 初始化GitHub客户端（修复弃用警告）
auth = Auth.Token(GH_TOKEN)
g = Github(auth=auth)
# 初始化Git仓库
repo = git.Repo(".")
# 远程仓库
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

def sync_issues(repo_full_name: str):
    """同步Issue"""
    print(f"同步 {repo_full_name} Issues...")
    source_repo = g.get_repo(repo_full_name)
    save_dir = Path("issues")
    
    for issue in source_repo.get_issues(state="all"):
        # 跳过PR（PR会单独同步）
        if hasattr(issue, "pull_request"):
            continue
            
        # 元数据
        fm = parse_github_object(issue)
        fm["type"] = "issue"
        fm["status"] = issue.state
        fm["closed_at"] = issue.closed_at.isoformat() if issue.closed_at else None
        
        # 正文内容
        content = f"# 原始描述\n{issue.body or '无描述'}\n\n# 讨论记录\n"
        # 抓取评论 ✅ 修复用户空指针
        for comment in issue.get_comments():
            time_str = comment.created_at.isoformat()
            comment_user = comment.user.login if comment.user else "unknown"
            content += f"## {comment_user} | {time_str}\n{comment.body or '无内容'}\n\n"
        # 抓取处理记录 ✅ 修复用户空指针
        content += "# 处理记录\n"
        issue_user = issue.user.login if issue.user else "unknown"
        content += f"- {issue_user} opened this issue on {fm['created_at']}\n"
        if issue.state == "closed":
            content += f"- 关闭时间: {fm['closed_at']}\n"
        
        # 保存文件
        file_path = save_dir / f"issue-{issue.number}.md"
        save_md(file_path, fm, content)

def sync_pull_requests(repo_full_name: str):
    """同步PR"""
    print(f"同步 {repo_full_name} Pull Requests...")
    source_repo = g.get_repo(repo_full_name)
    save_dir = Path("pull_requests")
    
    for pr in source_repo.get_pulls(state="all"):
        # 元数据
        fm = parse_github_object(pr)
        fm["type"] = "pull_request"
        fm["status"] = "merged" if pr.merged else pr.state
        fm["closed_at"] = pr.closed_at.isoformat() if pr.closed_at else None
        fm["merged_at"] = pr.merged_at.isoformat() if pr.merged else None
        
        # 正文内容
        content = f"# 原始描述\n{pr.body or '无描述'}\n\n# 讨论记录\n"
        # 抓取评论 ✅ 修复用户空指针（核心报错点）
        for comment in pr.get_comments():
            time_str = comment.created_at.isoformat()
            comment_user = comment.user.login if comment.user else "unknown"
            content += f"## {comment_user} | {time_str}\n{comment.body or '无内容'}\n\n"
        # 处理记录 ✅ 修复用户空指针
        content += "# 处理记录\n"
        pr_user = pr.user.login if pr.user else "unknown"
        content += f"- {pr_user} opened this PR on {fm['created_at']}\n"
        if pr.merged:
            content += f"- 合并时间: {fm['merged_at']}\n"
        elif pr.state == "closed":
            content += f"- 关闭时间: {fm['closed_at']}\n"
        
        # 保存文件
        file_path = save_dir / f"pr-{pr.number}.md"
        save_md(file_path, fm, content)

def sync_releases(repo_full_name: str):
    """同步Releases"""
    print(f"同步 {repo_full_name} Releases...")
    source_repo = g.get_repo(repo_full_name)
    save_dir = Path("releases")
    
    for release in source_repo.get_releases():
        # 元数据
        fm = {
            "title": release.title or release.tag_name,
            "type": "release",
            "source_url": release.html_url,
            "author": release.author.login if release.author else "unknown",
            "tag_name": release.tag_name,
            "created_at": release.created_at.isoformat() if release.created_at else None,
            "published_at": release.published_at.isoformat() if release.published_at else None,
        }
        
        # 正文内容
        content = f"# 版本信息\n标签: {release.tag_name}\n\n# 发布说明\n{release.body or '无说明'}"
        
        # 保存文件
        file_path = save_dir / f"release-{safe_filename(release.tag_name)}.md"
        save_md(file_path, fm, content)

def switch_branch(branch_name: str):
    """
    修复分支切换逻辑：
    1. 不存在则创建本地分支
    2. 仅远程存在对应分支时才拉取，避免首次运行报错
    """
    try:
        # 切换到已有分支
        repo.git.checkout(branch_name)
        # 拉取远程更新（仅远程存在时执行）
        repo.git.fetch("origin", branch_name)
        repo.git.pull("origin", branch_name)
    except git.GitCommandError:
        # 分支不存在 → 创建新分支
        repo.git.checkout("-b", branch_name)
        print(f"🆕 创建本地分支: {branch_name}")

def main():
    # 配置Git用户
    repo.config_writer().set_value("user", "name", "github-actions[bot]").release()
    repo.config_writer().set_value("user", "email", "github-actions[bot]@users.noreply.github.com").release()
    
    # 配置Git认证（解决推送权限问题）
    origin.set_url(f"https://{GH_TOKEN}@github.com/{TARGET_REPO}.git")

    for repo_full_name in SOURCE_REPOS:
        branch_name = repo_full_name.split("/")[-1]
        print(f"\n===== 开始同步 {repo_full_name} → 分支 {branch_name} =====")
        
        # 切换/创建分支
        switch_branch(branch_name)
        
        # 同步数据
        sync_issues(repo_full_name)
        sync_pull_requests(repo_full_name)
        sync_releases(repo_full_name)
        
        # 提交推送
        if repo.is_dirty():
            repo.git.add(".")
            commit_msg = f"Sync {repo_full_name} | {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}"
            repo.index.commit(commit_msg)
            repo.git.push("--set-upstream", "origin", branch_name)
            print(f"✅ 推送成功: {branch_name}")
        else:
            print(f"ℹ️ 无变更，跳过推送: {branch_name}")

if __name__ == "__main__":
    main()