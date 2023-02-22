import yaml
import sys


if __name__ == '__main__':
    # main entrypoint
    try:
        with open(sys.argv[1], 'r') as iac_file:
            print("Checkout file!")
            iac = yaml.safe_load(iac_file)
            for stage in iac['stages']:
                git_url = iac['stages'][stage]['git']
                print("Checkout git from " + git_url)
                # TODO: Write a sequence of actions for each stage
    except Exception as e:
        print(f"Some error occurred! {e}")
        exit(1)
