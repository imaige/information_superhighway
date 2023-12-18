import logging


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