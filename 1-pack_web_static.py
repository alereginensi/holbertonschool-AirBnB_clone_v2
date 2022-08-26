#!/usr/bin/python3
# Write a Fabric script that generates a .tgz archive
# from the contents of the web_static folder of your AirBnB
# Clone repo, using the function do_pack.

from fabric.api import local
from time import strftime


def do_pack():
    """
    Script that generates a .tgz archive
    """
    local("mkdir -p versions")
    name = "versions/web_static_{}.tgz".format(time)
    try:
        local("tar -czvf {} web_static/".format(name))
        return(name)
    except(Exception):
        return(None)
