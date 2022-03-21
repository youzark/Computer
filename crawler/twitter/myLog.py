#!/usr/bin/env python
def funcLogger(origFunc):
    from functools import wraps
    import logging
    from os.path import expanduser
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    fileHandler = logging.FileHandler(expanduser(f"~/Computer/crawler/twitter/log/{origFunc.__name__}.log"))
    formatter = logging.Formatter(f"%(asctime)s-%(levelname)s:%(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    @wraps(origFunc)
    def wrapper(*args, **kwargs):
        logger.info(
                f'{origFunc.__name__} Ran with args: {args}, and kwargs: {kwargs}'
                )
        return origFunc(*args,*kwargs)
    return wrapper
