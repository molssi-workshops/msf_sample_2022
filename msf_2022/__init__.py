"""A sample repo for the MSF bootcamp 2022."""

# Add imports here
from .molecool import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
