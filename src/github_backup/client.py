import os
import requests
import json
import subprocess
from datetime import datetime


class Client:
    def __init__(
        self,
        user,
        token
    ) -> None:
        self.user = user
        self.token = token
        self.session = None

    def login(self):
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"token {self.token}"
            }
        )

    def from_env():
        user = os.environ.get("GITHUB_USERNAME")
        token = os.environ.get("GITHUB_TOKEN")
        return Client(user, token)

    def list_repos(self):
        response = self.session.get("https://api.github.com/user/repos")
        repos_json = json.loads(response.text)
        result = list()
        for repo in repos_json:
            result.append(repo["name"])
        return result

    def _clone_repo(self, name):
        if not os.path.exists(name):
            subprocess.run(
                f"git clone https://{self.token}@github.com/{self.user}/{name}.git",
                shell=True
            )
        else:
            subprocess.run(
                f"cd {name} && git pull",
                shell=True
            )

    def clone_repo(self, name):
        try:
            self._clone_repo(name)
        except:
            now = datetime.now()
            dt_string = now.strftime("%Y_%m_%d-%H_%M_%S")
            os.rename(name, f"{name}-{dt_string}") 
            self._clone_repo(name)
