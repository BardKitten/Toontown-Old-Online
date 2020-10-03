import shutil
import LoggerPlus

from panda3d.core import loadPrcFile, ConfigPageManager

logger = LoggerPlus.LoggerPlus()

CONFIG_MGR = ConfigPageManager.getGlobalPtr()
# Set primary config file (default is first explicitly loaded):
CONFIG_FILE = None


