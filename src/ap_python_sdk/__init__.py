# 2000Charge Python bindings
# API docs at http://2000charge.com/api/
# Authors:
# Marjan Stojanovic <marjan.stojanovic90@gmail.com>
# Marjan Stojanovic <nenad.bozic@smartcat.io>

# Configuration variables

api_key = None
api_base = 'https://api.2000charge.com/api'
api_version = None
default_http_client = None

# Resource

from ap_python_sdk.util import json, logger
from ap_python_sdk.version import VERSION
