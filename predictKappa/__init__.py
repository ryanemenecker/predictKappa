"""
short description of predictKappa.

pget kappa values but today!
"""

# Add imports here
from .pred_kappa import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
