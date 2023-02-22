#!/usr/bin/env python3
# coding: utf-8


import os


from git import Repo
from git import RemoteProgress


class GitDownloader(object):
    """
    This is git downloader class.
    It downloads files from git to the current working directory
    """

    def __init__(self, *args, **kwargs):
        self.cwd = os.getcwd()
        self.default_branch = "master"

        try:
            self.url = kwargs["url"]
        except KeyError:
            self.url = False
        try:
            self.user = kwargs["user"]
        except KeyError:
            self.user = False
        try:
            self.password = kwargs["password"]
        except KeyError:
            self.password = False
        try:
            self.token = kwargs["token"]
        except KeyError:
            self.token = False
        try:
            self.path = kwargs["path"]
        except KeyError:
            self.path = self.cwd
        try:
            self.git_branch = kwargs["git_branch"]
        except KeyError:
            self.git_branch = self.default_branch

    # Static method to comply with the DRY principle
    @staticmethod
    def checkout(url, path, branch, progress, ) -> None:
        # TODO: Maybe we need to parse url
        Repo.clone_from(url, path, branch, progress)

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
                branch=branch,
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

