import os
import logging.handlers

from django.conf import settings


class DefaultFileHandler(logging.handlers.TimedRotatingFileHandler):
    """
    按时间来滚动日志
    """

    def __init__(self):
        project_name = getattr(settings, "PROJECT_NAME", 'logs')
        log_path = os.path.abspath('logs')
        if not os.path.isdir(log_path):
            os.makedirs(log_path)
        filename = os.path.join(log_path, '%s.log' % (project_name,))
        logging.handlers.TimedRotatingFileHandler.__init__(self, filename, when='midnight')
