from collections import defaultdict
from github import Github
from dotenv import load_dotenv
import os
from datetime import datetime
from tzlocal import get_localzone


def main():
    # ========== 1. Load Configuration ==========
    load_dotenv()
    TOKEN = os.getenv("GITHUB_TOKEN")
    USERNAME = os.getenv("USERNAME")

    g = Github(TOKEN)
    user = g.get_user()

    print(f"Current user: {user.login}")

    # ========== 2. Scan all organizations for repos that have committed ==========
    orgs = user.get_orgs()
    contributed_repos = []

    print(f"Organizations ({orgs.totalCount}): {[org.login for org in orgs]}")
    print("\nScanning for Repo's that you have contributed to in the organization...\n")

    for org in orgs:
        try:
            repos = org.get_repos()
            for repo in repos:
                try:
                    commits = repo.get_commits(author=USERNAME)
                    if commits.totalCount > 0:
                        contributed_repos.append(repo.full_name)
                        print(f"[O] {repo.full_name} - {commits.totalCount} commits")
                except Exception as e:
                    print(f"[!!!] unreadable {repo.full_name} submit information: {e}")
        except Exception as e:
            print(f"[X] Unable to access organization {org.login}: {e}")

    print(f"\nTotal findings {len(contributed_repos)} that you have contributed to the organization's repo.\n")

    # ========== 3. Iterate through these repositories and count the number of language bytes ==========
    language_count = defaultdict(int)

    for repo_full_name in contributed_repos:
        try:
            repo = g.get_repo(repo_full_name)
            repo_languages = repo.get_languages()
            for lang, count in repo_languages.items():
                language_count[lang] += count
        except Exception as e:
            print(f"[X] Unable to read language information: {repo_full_name}: {e}")

    # ========== 4. Exporting Markdown files ==========
    local_tz = get_localzone()
    now = datetime.now(local_tz)
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S %Z")

    with open("lang-summary.md", "w", encoding="utf-8") as f:
        f.write("### 💻 My Contributions (Across Organizations)\n\n")
        f.write(f"_Last scan: **{formatted_time}**_\n\n")
        f.write("| Language | Bytes |\n")
        f.write("|----------|--------|\n")
        for lang, total_bytes in sorted(language_count.items(), key=lambda x: -x[1]):
            f.write(f"| {lang} | {total_bytes:,} |\n")
        f.write("\n_Powered by [github-org-stats](https://github.com/TheHQ98/github-org-stats)_\n")

    print("Language statistics saved：lang-summary.md")


if __name__ == "__main__":
    main()
