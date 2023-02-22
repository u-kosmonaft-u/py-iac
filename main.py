#!/usr/bin/env python3
# coding: utf-8


# import yaml
import sys


from os import path


from modules.makeurl.main import MakeURL

if __name__ == "__main__":
    # main entrypoint
    try:
        if path.exists(sys.argv[1]):
            main_yml = sys.argv[1]
        else:
            raise IndexError
    except IndexError:
        main_yml_file = "main.yml"
        main_yml = path.join(
            path.dirname(path.realpath(__file__)),
            main_yml_file
        )
    print(main_yml)

    url = MakeURL(url="tttttest")
    print(url.url)
    # try:
    #     with open(sys.argv[1], 'r') as iac_file:
    #         print("Checkout file!")
    #         iac = yaml.safe_load(iac_file)
    #         for stage in iac['stages']:
    #             git_url = iac['stages'][stage]['git']
    #             print("Checkout git from " + git_url)
    #             # TODO: Write a sequence of actions for each stage
    # except Exception as e:
    #     print(f"Some error occurred! {e}")
    #     exit(1)
