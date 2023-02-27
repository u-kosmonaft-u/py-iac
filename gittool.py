from git import Repo
from git import RemoteProgress
import os


class GitDownloader(object):
    """

    This is git downloader class.

    It downloads files from git to the current working directory

    """
    cwd = os.getcwd()  # Just get current working directory to clone repos

    def __init__(self, url, user='', password='', token='', path=cwd, git_branch='master'):
        self.url = url
        self.user = user
        self.password = password
        self.token = token
        self.path = path
        self.git_branch = git_branch

    """
    Static method to comply with the DRY principle
    """

    @staticmethod
    def checkout(url, path, branch, progress, ) -> None:
        Repo.clone_from(url, path, branch, progress)    # TODO: Maybe we need to parse url

    def clone(self):
        print("Cloning repository into %s" % self.path)
        # TODO: Need to concatenate url with user and password
        if self.token == "":
            try:
                self.checkout(url=self.url,
                              path=self.path,
                              branch=self.git_branch,
                              progress=MyProgressPrinter())
            except Exception as e:
                print(f"There is some error {e}")
                exit(1)
        else:
            # TODO: Need to clone repo with token somehow, example below:
            """
            credentials = base64.b64encode(f"{GHE_TOKEN}:".encode("latin-1")).decode("latin-1")
            Repo.clone_from(
                url=repo_url,
                c=f"http.{repo_url}/.extraheader=AUTHORIZATION: basic {credentials}",
                single_branch=True,
                depth=1,
                to_path=f"/clone/to/here",
                branch=branch,w
                )
            """
            try:
                print("Cloning repo with token")
            except Exception as e:
                print(f"Something wrong!Error is {e}")


class MyProgressPrinter(RemoteProgress):
    """
    Class for progress from GitPython docs
    """
    def update(self, op_code, cur_count, max_count=None, message=""):
        print(
            op_code,
            cur_count,
            max_count,
            cur_count / (max_count or 100.0),
            message or "NO MESSAGE",
        )
