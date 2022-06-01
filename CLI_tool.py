import argparse
import sys
import os

import json


def json_update(filename, dep_version):
    print(dep_version)
    package_name = dep_version.split('@')[0]
    param = dep_version.split('@')[1]
    print("tocheck: :", param)

    f = open(filename)

    data = json.load(f)
    f.close()
    current_version = data['packages']['']['dependencies'][package_name]
    try:
        current_version = current_version.split('^')[1]
    except:
        pass

    print("current: ", current_version)
    i = 0
    while (i < len(current_version.split('.'))):
        if current_version[i] > package_name[i]:

            return True

        else:
            f = open(filename, "w")
            data['packages']['']['dependencies'][package_name] = param
            json.dump(data, f)
            f.close()
            return "Version updated"


def calc(args):
    if args.o == "update":
        print("updating")
        return json_update(args.dep_path, args.ver)

    else:
        return ("pls mention to update")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dep_path', type=str)
    parser.add_argument('--ver', type=str)
    parser.add_argument('--o', type=str, help="specify the operator")
    args = parser.parse_args()

    sys.stdout.write(str(calc(args)))