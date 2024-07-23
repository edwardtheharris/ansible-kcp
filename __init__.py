"""Module initialization for versioning."""
# pylint: disable=invalid-name

import pathlib
import version_query

def get_version():
    """Get the next version."""
    version = version_query.predict_git_repo(pathlib.Path('.'))
    print(version)
    return version.to_str()
