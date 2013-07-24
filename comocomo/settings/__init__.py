from __future__ import print_function
import sys
import imp

try:
    (file, path, description) = imp.find_module('local', __path__)
    if file:
        file.close()
except ImportError:
    print(u"You don't have a settings file in `settings/local.py`")
    print(u"You can use `settings/local.py.example` as a starting point")
    sys.exit(1)

from .local import *

