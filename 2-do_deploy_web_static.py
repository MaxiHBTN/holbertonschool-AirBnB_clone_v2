#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers,
using the function do_deploy
"""

from fabric.api import put, run, env
from os.path import exists

env.hosts = ['34.227.197.193', '52.55.214.253']


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers
    """

    if exists(archive_path):
        filename = archive_path.split("/")[-1]
        filename_noext = filename.split(".")[0]
        put(archive_path, "/tmp/")
        r1 = run(f"mkdir -p /data/web_static/releases/{filename_noext}")
        r2 = run(f"tar -xzf /tmp/{filename} -C \
            /data/web_static/releases/{filename_noext}/")
        r3 = run(f"rm /tmp/{filename}")
        r1 = run(f"mv /data/web_static/releases/{filename_noext}/web_static/* \
            /data/web_static/releases/{filename_noext}/")
        r4 = run(f"rm -rf /data/web_static/releases/\
            {filename_noext}/web_static")
        r5 = run(f"rm -rf /data/web_static/current")
        r6 = run(f"ln -s /data/web_static/releases/{filename_noext}/ \
            /data/web_static/current")
        if (r1.failed or r2.failed or r3.failed or
                r4.failed or r5.failed or r6.failed):
            return True
    else:
        return False
