import logging

def setup_logger(app):
    app.logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler("app.log")
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
