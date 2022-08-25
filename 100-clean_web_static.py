#!/usr/bin/python3
"""
Fabric script (based on the file 3-deploy_web_static.py)
that deletes out-of-date archives, using the function do_clean
"""

from fabric.api import local, run, env

env.hosts = ['34.227.197.193', '52.55.214.253']


def do_clean(number=0):
    """
    Deletes out-of-date archives,
    """

    files = local("ls -t versions", capture=True).split("\n")
    last = len(files)
    num = int(number)
    if num == 0:
        num = 1
    for i in range(num, last):
        local("rm versions/{}".format(files[i]))
        print(files[i])
    files_server = run("ls -t /data/web_static/releases").split("  ")
    last = len(files_server)
    for j in range(num, last):
        run("rm -rf /data/web_static/releases/{}".format(files_server[j]))
