import logging
from os import getenv

# Custom log levels
TRACE_LEVEL_NUM = 5
NOTICE_LEVEL_NUM = 25

# Register custom levels
logging.addLevelName(TRACE_LEVEL_NUM, "TRACE")
logging.addLevelName(NOTICE_LEVEL_NUM, "NOTICE")


# Add methods to handle custom levels
def trace(self, message, *args, **kws):
    if self.isEnabledFor(TRACE_LEVEL_NUM):
        self._log(TRACE_LEVEL_NUM, message, args, **kws)


def notice(self, message, *args, **kws):
    if self.isEnabledFor(NOTICE_LEVEL_NUM):
        self._log(NOTICE_LEVEL_NUM, message, args, **kws)


# Add methods to the Logger class
logging.Logger.trace = trace
logging.Logger.notice = notice


class FilenameFormatter(logging.Formatter):
    def format(self, record):
        # Get the filename and path
        filename = record.filename
        path = record.pathname

        # Customize the log record message to include filename and path
        record.msg = f"[{path}] {filename}: {record.msg}"

        return super().format(record)


def configure_logger(logger, level=logging.DEBUG):
    handler = logging.StreamHandler()
    formatter = FilenameFormatter(fmt='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(level)
    logger.propagate = False


def get_log_level():
    log_level_str = getenv('LOG_LEVEL', 'DEBUG').upper()
    log_level = logging.getLevelName(log_level_str)

    # Handle custom levels explicitly
    if log_level_str == 'TRACE':
        return TRACE_LEVEL_NUM
    elif log_level_str == 'NOTICE':
        return NOTICE_LEVEL_NUM

    return log_level
