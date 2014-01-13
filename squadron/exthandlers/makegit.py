import git
import shutil
from extutils import get_filename
import os

def ext_git(abs_source, dest, **kwargs):
    """ Clones a git repository """
    with open(abs_source) as gitfile:
        contents = gitfile.read().split()
        url = contents[0]
        if len(contents) > 1:
            refspec = contents[1]
        else:
            refspec = None

    finalfile = get_filename(dest)
    repo = git.Repo.clone_from(url, finalfile)

    if refspec:
        repo.checkout(refspec)

    return finalfile
