#!/bin/env python
from zeeguu_web.app import app as application
application.logger.debug (application.instance_path)
application.logger.debug (application.config.get("SQLALCHEMY_DATABASE_URI"))

# Uncomment following lines if you want to try it out w/o wsgi
#application.run(
#     host=application.config.get("HOST", "localhost"),
#     port=application.config.get("PORT", 9000)
#)
