"""Settings package initialization."""

import dotenv
dotenv.load()

# Ensure development settings are not used in testing and production:
if dotenv.get('ENVIRONMENT') == 'PRODUCTION':
    from .production import *
else:
    from .local import *
