from __future__ import absolute_import
from __future__ import print_function

import logging


log_format = "[%(asctime)s: %(levelname)s/%(name)s/%(funcName)s] %(message)s"
logging.basicConfig(format=log_format, level=logging.WARNING)
logger = logging.getLogger('sdscli')
