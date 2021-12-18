import os
from github_backup.client import Client


def do_backup():
    client = Client.from_env()
    client.login()
    repos = client.list_repos()
    for repo in repos:
        client.clone_repo(repo)
