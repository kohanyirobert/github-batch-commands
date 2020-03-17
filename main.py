import os
from github import Github

g = Github(os.environ['GITHUB_ACCESS_TOKEN'])

for r in g.get_user().get_repos():
    print(r)
