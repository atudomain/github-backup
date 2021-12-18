import os
from github_backup.client import Client


def do_backup():
    client = Client.from_env()
    client.login()
    repos = client.list_repos()
    for repo in repos[:3]:
        client.clone_repo(repo)
