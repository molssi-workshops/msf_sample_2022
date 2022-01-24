"""A sample repo for the MSF bootcamp 2022."""

# Add imports here
from msf_2022.visualize import *
from msf_2022.molecule import *
from msf_2022.measure import *

# Handle versioneer
from ._version import get_versions # type: ignore

versions = get_versions()
__version__ = versions["version"]
__git_revision__ = versions["full-revisionid"]
del get_versions, versions
