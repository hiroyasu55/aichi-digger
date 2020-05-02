import settings  # noqa: F401
import os
from app import app
import config
import app.lib.log as log

logger = log.getLogger()

# Main
if __name__ == '__main__':
    logger.info('Running as %s mode.', os.getenv('FLASK_ENV'))

    app.run(debug=config.DEBUG)
