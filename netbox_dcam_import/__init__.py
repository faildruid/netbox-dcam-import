from importlib import metadata

from extras.plugins import PluginConfig


__version__ = metadata.version(__name__)
__author__ = "Pat McLean"
__email__ = "patrick.mclean@sap.com"


class DcamImportConfig(PluginConfig):
    name = "netbox_dcam_import"
    verbose_name = "NetBox DCAM Import"
    description = "A netbox plugin for managing DCAM rack imports"
    author = __author__
    author_email = __email__
    version = __version__
    base_url = "dcam-import"
    min_version = "3.5.0"


config = DcamImportConfig
