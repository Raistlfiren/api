"""
Phusion Passenger WSGI entrypoint
"""

import sys

if sys.version_info.major != 3:
    raise RuntimeError(
        "FAForever API requires python 3.\n"
        "Refer to passenger documentation on how to accomplish that.\n"
        "Good luck.")

from api import app, api_init

# Load Database config
DATABASE = dict(
    engine=  "playhouse.pool.PooledMySQLDatabase",
    name=    "bob",
    user=    "the",
    passwd=  "dinosaur",
    max_connections= 32, stale_timeout=600)

app.config.from_object(__name__)

api_init()

application = app