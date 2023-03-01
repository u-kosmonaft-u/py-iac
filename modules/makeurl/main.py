#!/usr/bin/env python3
# coding: utf-8


import yaml


from os.path import (
    isfile,
    exists,
    )


class MakeURL(object):
    """
    Класс позволяет генерировать URL git-репозитория.
    """

    def __init__(self, *args, **kwargs) -> None:
        self._urls: dict = {}
        try:
            self._urls_file: str = kwargs["urls_file"]
        except KeyError:
            self._urls_file: bool = False

    @property
    def url(self):
        return self._urls_file

    def clean_git_url(self, url: str) -> None:
        """
        Удаление из URL имени пользователя и порта, если есть.
        """
        check_chars: dict = {"@": "//", ":": "/"}
        for key, value in check_chars.items():
            url = url.split(key)
            if len(url) == 2 and key != ":":
                url = "{0}{1}".format(
                    "".join(url[0].partition(value)[:2]),
                    url[1])
            elif len(url) == 3 and key != "@":
                url = (key.join(url[:2]), url[2])
                url = "{0}{1}".format(
                    url[0],
                    "".join(url[1].partition(value)[1:]))
            else:
                url = "".join(url)
        return url

    def yaml_parser(self) -> None:
        """
        Метод открывает и парсит yml-файл с параметрами git-репозиториев.
        """
        urls: dict = {}
        if isfile(self._urls_file) and exists(self._urls_file):
            with open(self._urls_file) as urls_file:
                yaml_content = yaml.safe_load(urls_file)
                match "stages" in yaml_content:
                    case True:
                        for stage in yaml_content["stages"]:
                            url = self.clean_git_url(
                                url=yaml_content["stages"][stage]["git"]["url"]
                                )
                            urls[stage] = url

                    case False:
                        return False
            return urls


if __name__ == "__main__":
    from sys import argv

    url: MakeURL = MakeURL(urls_file=argv[1])
    print(url.yaml_parser())
