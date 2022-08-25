#!/usr/bin/python3
# Write a Fabric script that generates a .tgz archive
# from the contents of the web_static folder of your AirBnB
# Clone repo, using the function do_pack.

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Script that generates a .tgz archive from the contents of the web_static
    folder
    """
    name = "web_static_" +\
            datetime.strftime(datetime.now(), "%Y%m%d%H%M%S") + ".tgz"
    local("mkdir -p versions")
    try:
        local("tar -czvf ./versions/{} ./web_static" .format(name))
        return(name)
    except(Exception):
        return(None)
